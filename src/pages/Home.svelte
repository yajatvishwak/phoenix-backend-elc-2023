<script>
  // @ts-nocheck
  import * as faceapi from "face-api.js";
  import { onMount } from "svelte";

  let stream;
  let videoRef;
  let canvasRef;
  let context;
  let isUserFacingCamera = false;

  onMount(async () => {
    Promise.all([
      faceapi.nets.tinyFaceDetector.loadFromUri("/models"),
      faceapi.nets.faceLandmark68Net.loadFromUri("/models"),
      faceapi.nets.faceRecognitionNet.loadFromUri("/models"),
      faceapi.nets.faceExpressionNet.loadFromUri("/models"),
    ]).then(() => console.log("models loaded"));
  });

  const startCamera = async () => {
    try {
      stream = await navigator.mediaDevices.getUserMedia({ video: true });
      videoRef.srcObject = stream;
    } catch (error) {
      console.error(error);
    }
  };

  const stopCamera = () => {
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
    }
    if (interval) {
      clearInterval(interval);
    }
  };

  const drawFrame = () => {
    context.drawImage(videoRef, 0, 0, canvasRef.width, canvasRef.height);
    requestAnimationFrame(drawFrame);
  };
  let interval = null;

  const drawFace = () => {
    const canvas = faceapi.createCanvasFromMedia(videoRef);
    document.body.append(canvas);
    console.log(videoRef.videoWidth, videoRef.videoHeight);
    const displaySize = {
      width: videoRef.videoWidth,
      height: videoRef.videoHeight,
    };
    faceapi.matchDimensions(canvas, displaySize);
    interval = setInterval(async () => {
      const detections = await faceapi
        .detectAllFaces(videoRef, new faceapi.TinyFaceDetectorOptions())
        .withFaceLandmarks()
        .withFaceExpressions();
      const resizedDetections = faceapi.resizeResults(detections, displaySize);
      canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
      faceapi.draw.drawDetections(canvas, resizedDetections);
      faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
      faceapi.draw.drawFaceExpressions(canvas, resizedDetections);
    }, 100);
  };

  $: if (videoRef && canvasRef) {
    context = canvasRef.getContext("2d");
    drawFrame();
  }
</script>

<video on:play={drawFace} bind:this={videoRef} autoplay muted />
<canvas bind:this={canvasRef} />

<button on:click={startCamera}>Start Camera</button>
<button on:click={stopCamera}>Stop Camera</button>
