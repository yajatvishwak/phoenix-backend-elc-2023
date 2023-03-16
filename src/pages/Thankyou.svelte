<script>
  import JSConfetti from "js-confetti";
  import { onMount } from "svelte";
  import Navbar from "./components/Navbar.svelte";
  import { playDialogue, playSound } from "./listener/speak";
  const jsConfetti = new JSConfetti();
  let loading = false;
  onMount(() => {
    loading = true;
    jsConfetti.addConfetti();
    playDialogue(
      "Thank you for ordering with phoenix handsfree! Hope you have a great day!"
    );
    playSound("audio/done.wav");
    setTimeout(() => {
      loading = false;
    }, 3000);
  });
</script>

<section class="flex flex-col h-screen">
  <Navbar />
  <div class="flex-1 flex-col flex items-center justify-center">
    {#if loading}
      <div class="animate-pulse">Loading...</div>
    {:else}
      <img
        src={"https://i.giphy.com/media/Ju7l5y9osyymQ/giphy.gif"}
        class="rounded-xl"
        alt=""
      />
    {/if}

    <div class="text-6xl mt-7 newfont">Order placed successfully!</div>
    <div class="mt-2 text-xl">Completed order, handsfree!</div>
  </div>
</section>
