import random
import cv2
import mediapipe as mp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Constants
FACE_IMAGE_FOLDER = 'justfaces'


mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.mediapipe.python.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils


class FaceDetector:

    # function generates a random 6 digit number
    def generateRandom6DigitNumber(self):
        code = ''
        for i in range(6):
            code += str(random.randint(0, 9))
        return code

    # function detects face in image and
    # 1. showPreview: if True, shows the image with face detected returns the image object
    # 2. saveImage: if True, saves the image with face detected and returns the path
    def getFaceImage(self, imagePath, showPreview=False, saveImage=True, savePath=None):
        img = cv2.imread(imagePath)
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
        mask = cv2.fillPoly(mask, [np.array(lines_to_draw)], 1)
        mask = mask.astype(bool)

        output = np.zeros_like(img)
        output[mask] = img[mask]

        output = output[:, :, ::-1]  # BGR to RGB
        if showPreview:
            plt.imshow(output)
            plt.show()
        if saveImage:
            # save the image to the justface folder
            if savePath == None:
                face_pic_path = os.path.join(
                    FACE_IMAGE_FOLDER, self.generateRandom6DigitNumber() + '.png')
            else:
                face_pic_path = savePath
            cv2.imwrite(face_pic_path, cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
            return face_pic_path
        return output
