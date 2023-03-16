from detect_face import FaceDetector
from extract_skintone import SkinColorDetector
from makeup_generator import MakeupPaletteGenerator
from pprint import pprint

face_detector = FaceDetector()
skin_tone_extractor = SkinColorDetector()
makeup_palette_generator = MakeupPaletteGenerator()

facePath = face_detector.getFaceImage(
    "images/1111.jpeg", showPreview=False, saveImage=True)

skincolor_palette = skin_tone_extractor.getColorPalette(
    facePath, show_chart=False)

foundationColor = makeup_palette_generator.getMakeupColorPalette(
    skincolor_palette)

# pprint(foundationColor)
