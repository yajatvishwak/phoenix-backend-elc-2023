import cv2
import dlib
import faceBlendCommon as face
from detect_face import FaceDetector
import numpy as np
import mediapipe as mp
import pandas as pd

PREDICTOR_PATH = r"shape_predictor_68_face_landmarks.dat"
faceDetector = dlib.get_frontal_face_detector()
landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)

mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.mediapipe.python.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils


# experimental code: This code does not work yet
class MakeupApplier:
    def HEXToRGB(self, hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    def applyLipstick(self, imgpath, color, product):
        im = cv2.imread(imgpath)
        landmarks = face.getLandmarks(faceDetector, landmarkDetector, im)
        lipsPoints = landmarks[48:60]

        mask = np.zeros((im.shape[0], im.shape[1], 3), dtype=np.float32)
        cv2.fillConvexPoly(mask, np.int32(lipsPoints), (1.0, 1.0, 1.0))
        mask = 255*np.uint8(mask)
        # Apply close operation to improve mask
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, 1)
        mask = mask.astype(float)

        op = np.copy(im)

        colorRGB = self.HEXToRGB(color)
        colorBGR = (colorRGB[2], colorRGB[1], colorRGB[0])
        op[(mask == 255).all(-1)] = list(colorBGR)
        op_w = cv2.addWeighted(op, 0.4, im, 0.7, 0, op)
        cv2.imwrite("./makeup_images/lipsticks/" + product + ".png", op_w)
        return "makeup_images/lipsticks/" + product + ".png"

    def applyFoundation(self,  imgpath, color, product):
        img = cv2.imread(imgpath)
        face_mesh = mp_face_mesh.FaceMesh(
            static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)
        results = face_mesh.process(img[:, :, ::-1])
        landmarks = results.multi_face_landmarks[0]

        df = pd.DataFrame(list(mp_face_mesh.FACEMESH_FACE_OVAL),
                          columns=["p1", "p2"])
        routes = []
        p1 = df.iloc[0]["p1"]
        p2 = df.iloc[0]["p2"]

        for i in range(0, df.shape[0]):
            obj = df[df["p1"] == p2]
            # print("GOOO", obj["p"].values[0])
            p1 = obj["p1"].values[0]
            p2 = obj["p2"].values[0]
            routes.append([p1, p2])
        lines_to_draw = []
        for s, t in routes:
            source = landmarks.landmark[s]
            target = landmarks.landmark[t]
            relative_source = (
                int(source.x * img.shape[1]), int(source.y * img.shape[0]))
            relative_target = (
                int(target.x * img.shape[1]), int(target.y * img.shape[0]))
            lines_to_draw.append(relative_source)
            lines_to_draw.append(relative_target)

        mask = np.zeros((img.shape[0], img.shape[1]))
        mask = cv2.fillPoly(mask, [np.array(lines_to_draw)], 1) * 255

        cv2.imwrite("images/mask.png", mask)
        op = np.copy(img)
        colorRGB = self.HEXToRGB(color)
        colorBGR = (colorRGB[2], colorRGB[1], colorRGB[0])
        op[(cv2.imread("images/mask.png") == 255).all(-1)] = colorBGR
        op_w = cv2.addWeighted(op, 0.3, img, 0.7, 0, op)
        cv2.imwrite("./makeup_images/foundation/" +
                    product + ".png", op_w)

        return "makeup_images/foundation/" + product + ".png"
