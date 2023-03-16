import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_file
from transformers import pipeline
import datetime
from werkzeug.utils import secure_filename
from detect_face import FaceDetector
from extract_skintone import SkinColorDetector
from makeup_generator import MakeupPaletteGenerator
from pprint import pprint
import pywhatkit
import json
from flask_cors import CORS


load_dotenv()


whisper = pipeline("automatic-speech-recognition",
                   model="openai/whisper-base")
face_detector = FaceDetector()
skin_tone_extractor = SkinColorDetector()
makeup_palette_generator = MakeupPaletteGenerator()


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_AUDIO'] = "./audio"


lipdata = []
with open('json/lipstick_shades.json') as json_file:
    lipdata = json.load(json_file)

foundationdata = []
with open('json/foundation_shades.json') as json_file:
    foundationdata = json.load(json_file)


@app.route('/')
def index():
    return "Hello world!"


@app.route('/getmakeup', methods=['POST'])
def getmakeup():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"})
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pathofimg = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        facePath = face_detector.getFaceImage(
            pathofimg, showPreview=False, saveImage=True)

        skincolor_palette = skin_tone_extractor.getColorPalette(
            facePath, show_chart=False)

        makeupDetails = makeup_palette_generator.getMakeupColorPalette(
            skincolor_palette)

        return jsonify({"makeup": makeupDetails, "image": filename})


@app.route('/getmakeupshared', methods=['GET'])
def getmakeupshared():
    pathofimg = os.path.join(app.config['UPLOAD_FOLDER'], "image.png")

    facePath = face_detector.getFaceImage(
        pathofimg, showPreview=False, saveImage=True)

    skincolor_palette = skin_tone_extractor.getColorPalette(
        facePath, show_chart=False)

    makeupDetails = makeup_palette_generator.getMakeupColorPalette(
        skincolor_palette)

    return jsonify({"makeup": makeupDetails, "image": "image.png"})


@app.route('/sendmessage', methods=['GET'])
def sendmessage():

    pywhatkit.sendwhatmsg_instantly(
        "+91"+os.environ["PHONE"], "http://localhost:5173/#/shared/image.png")

    return jsonify({"status": "success"})


@app.route("/getfile/<filename>")
def getfile(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(filepath)


@app.route("/getpreviewlinks", methods=["POST"])
def getpreviewlinks():
    foundations = request.json['foundations']
    lipstick = request.json['lipsticks']
    foundationsList = []
    for foundation in foundations:
        for f in foundationdata:
            if f['shadeCode'] == foundation:
                foundationsList.append({"link": "http://localhost:5000/getmakeupapplied/foundation/" +
                                       f['shadeCode']+".png", "productname": f['shadeName'] + " - " + f['shadeCode']})
    lipstickList = []
    for lip in lipstick:
        for l in lipdata:
            if l['lipstickCode'] == lip:
                lipstickList.append({"link": "http://localhost:5000/getmakeupapplied/lipsticks/" +
                                     l['lipstickCode']+".png", "productname": l['lipstickName'] + " - " + l['lipstickCode']})

    return jsonify({"foundations": foundationsList, "lipstick": lipstickList})


@app.route("/getmakeupapplied/foundation/<filename>")
def getmakeupfile(filename):
    filepath = os.path.join("makeup_images/foundation", filename)
    return send_file(filepath)


@app.route("/getmakeupapplied/lipsticks/<filename>")
def getmakeupfilelip(filename):
    filepath = os.path.join("makeup_images/lipsticks", filename)
    return send_file(filepath)


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(
            app.config['UPLOAD_FOLDER_AUDIO'], filename))
        pathofaudio = os.path.join(app.config['UPLOAD_FOLDER_AUDIO'], filename)
        p = whisper(pathofaudio)
        return jsonify({"transcription": p})


if __name__ == '__main__':
    app.debug = True
    app.run()  # go to http://localhost:5000/ to view the page.
