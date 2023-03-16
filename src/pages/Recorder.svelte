<script>
  // @ts-nocheck

  import { onMount } from "svelte";
  const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

  let mediaRecorder;
  let chunks = [];
  let isRecording = false;

  async function startRecording() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.ondataavailable = function (e) {
        chunks.push(e.data);
      };

      mediaRecorder.onstop = function () {
        const blob = new Blob(chunks, { type: "audio/webm" });
        const audioURL = URL.createObjectURL(blob);
        const audio = new Audio(audioURL);
        audio.controls = true;
        document.body.appendChild(audio);
      };

      mediaRecorder.start();
      isRecording = true;
    } catch (err) {
      console.error("Unable to get media stream", err);
    }
  }

  function stopRecording() {
    mediaRecorder.stop();
    isRecording = false;
  }
</script>

<div>
  {#if isRecording}
    <button on:click={stopRecording}>Stop Recording</button>
  {:else}
    <button on:click={startRecording}>Start Recording</button>
  {/if}
</div>
