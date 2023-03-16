import axios from "axios";
import { isListening } from "../store/listening.store";
import { usersaid } from "../store/usersaid.store";
import { playSound } from "./speak";
let mediaRecorder;
let chunks = [];
async function query(blob) {
  let fd = new FormData();
  fd.append("file", blob, getRandomFileName() + ".mp3");
  const { data } = await axios.post("http://localhost:5000/transcribe", fd);
  return data;
}

function getRandomFileName() {
  var timestamp = new Date().toISOString().replace(/[-:.]/g, "");
  var random = ("" + Math.random()).substring(2, 8);
  var random_number = timestamp + random;
  return random_number;
}
async function startRecording() {
  isListening.set(true);
  playSound("/audio/listenstart.mp3");
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = function (e) {
      chunks.push(e.data);
    };

    mediaRecorder.onstop = async function () {
      isListening.set(false);
      playSound("/audio/listenend.mp3");
      const blob = new Blob(chunks, { type: "audio/mp3" });
      const audioURL = URL.createObjectURL(blob);
      const audio = new Audio(audioURL);
      audio.controls = true;
      const transcript = await query(blob);

      if (transcript) {
        console.log(transcript);
        usersaid.set(
          transcript.transcription.text
            .toLowerCase()
            .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "")
        );
        chunks = [];
      }
    };

    mediaRecorder.start();
  } catch (err) {
    console.error("Unable to get media stream", err);
  }
}

function stopRecording() {
  mediaRecorder.stop();
}

export { startRecording, stopRecording };
