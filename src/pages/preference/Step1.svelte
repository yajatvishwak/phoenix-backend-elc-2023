<script>
  // @ts-nocheck
  import axios from "axios";
  import { onMount } from "svelte";
  import * as faceapi from "face-api.js";
  import { playDialogue, playSound, stopDialogue } from "../listener/speak";
  import canvasToImage from "canvas-to-image";
  import { suggestions } from "../store/suggestions.store";
  export let dialogues = [];
  export let steptitle = "Step 1";
  export let nextStep = () => {};
  let stream;
  let videoRef;
  let canvasRef;
  let detectFaceInterval;
  let takePictureInterval;
  let videoWidth;
  let videoHeight;

  onMount(() => {
    console.log(dialogues);
    Promise.all([
      faceapi.nets.tinyFaceDetector.loadFromUri("/models"),
      faceapi.nets.faceLandmark68Net.loadFromUri("/models"),
      faceapi.nets.faceRecognitionNet.loadFromUri("/models"),
      faceapi.nets.faceExpressionNet.loadFromUri("/models"),
    ]).then(async () => {
      console.log("models loaded");

      await playDialogue(
        "Hey there! I will help you find the perfect shades of foundation, concealer and lipsticks for your skin. We will start by having a look at your beautiful face. Make sure you have a camera and a good lighting."
      );
      startCamera();
    });
  });

  function isEnoughLight(canvas) {
    // Get the 2D context of the canvas
    let ctx = canvas.getContext("2d");

    // Get the image data from the canvas
    let imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);

    // Get the pixel data from the image
    let pixels = imageData.data;

    // Calculate the average pixel value
    let sum = 0;
    for (let i = 0; i < pixels.length; i += 4) {
      sum += (pixels[i] + pixels[i + 1] + pixels[i + 2]) / 3;
    }
    let avgBrightness = sum / (pixels.length / 4);

    // Set the brightness threshold
    let brightnessThreshold = 100;

    // Check if the average brightness is above the threshold
    if (avgBrightness > brightnessThreshold) {
      return true;
    } else {
      return false;
    }
  }

  async function detectFace(canvas) {
    const detections = await faceapi.detectAllFaces(
      canvas,
      new faceapi.TinyFaceDetectorOptions()
    );
    if (detections.length === 0) {
      return false;
    }

    // Get the center of the canvas
    const canvasCenterX = canvas.width / 2;
    const canvasCenterY = canvas.height / 2;

    // Check if any of the detected faces overlap with the center of the canvas
    const isCentered = detections.some((detection) => {
      const { x, y, width, height } = detection.box;
      const centerX = x + width / 2;
      const centerY = y + height / 2;
      const distanceFromCenter = Math.sqrt(
        (canvasCenterX - centerX) ** 2 + (canvasCenterY - centerY) ** 2
      );
      return distanceFromCenter < Math.min(canvasCenterX, canvasCenterY) / 2;
    });

    return isCentered;
  }

  async function takePicture() {
    // console.log(detectFace(canvasRef), checkLight(canvasRef));
    if (detectFace(canvasRef) && isEnoughLight(canvasRef)) {
      console.log("face detected");
      // play sound
      playSound("audio/shutter.mp3");
      let image = new FormData();
      canvasRef.toBlob(async (blob) => {
        const file = new File([blob], "image.png");
        image.append("file", file);
        // send to server
        const { data } = await axios.post(
          "http://localhost:5000/getmakeup",
          image,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        console.log(data);
        suggestions.set(data);
        nextStep();
      });

      canvasToImage(canvasRef, {
        name: "myImage",
        type: "png",
        quality: 1,
      });
      if (takePictureInterval) clearInterval(takePictureInterval);
      stopCamera();
    } else {
      await playDialogue(
        "Please make sure your face is in the center of the screen and there is enough light. Retrying..."
      );
    }
  }
  const startCamera = async () => {
    try {
      stream = await navigator.mediaDevices.getUserMedia({ video: true });
      videoRef.srcObject = stream;
      const ctx = canvasRef.getContext("2d");
      console.log(videoRef);
      canvas.width = 640;
      canvas.height = 480;
      console.log(videoWidth, videoHeight);
      videoRef.addEventListener("play", () => {
        detectFaceInterval = setInterval(() => {
          ctx.drawImage(videoRef, 0, 0, videoWidth, videoHeight);
        }, 100);
      });
      // live on camera now
      await playDialogue(
        "You are live on camera now! Make sure you face the camera. Don't forget to smile"
      );
      // clicking your picture, please wait
      await playDialogue("Clicking your picture, please wait...");
      // call take picture function
      takePictureInterval = setInterval(async () => {
        // console.log(await detectFace(canvasRef), isEnoughLight(canvasRef));
        await takePicture();
      }, 2000);
    } catch (error) {
      console.error(error);
    }
  };

  const stopCamera = () => {
    clearInterval(detectFaceInterval);
    stopDialogue();
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
    }
  };
</script>

<div class="-mt-28 flex flex-col items-center justify-center">
  <div class="text-3xl newfont">Let's have a look at your face!</div>
  <div class="">
    Take a picture so that we can analyse the perfect shade for you
  </div>
  <div class="flex flex-col">
    <video
      bind:this={videoRef}
      bind:videoHeight
      bind:videoWidth
      autoplay
      playsinline
      muted
      class="w-96 h-96"
    />
    <canvas id="canvas" bind:this={canvasRef} class="hidden" />
    <div class="flex flex-row gap-2 justify-center items-center">
      <button class="btn btn-outline" on:click={startCamera}
        >Start Camera</button
      >
      <button class="btn btn-outline" on:click={stopCamera}>Stop Camera</button>
    </div>
  </div>
</div>
