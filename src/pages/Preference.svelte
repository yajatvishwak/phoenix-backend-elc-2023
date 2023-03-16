<script>
  import { onMount } from "svelte";

  // @ts-nocheck

  import Navbar from "./components/Navbar.svelte";
  import { initVoice } from "./listener/speak";
  import Step1 from "./preference/Step1.svelte";
  import Step2 from "./preference/Step2.svelte";
  import Step3 from "./preference/Step3.svelte";
  import { suggestions } from "./store/suggestions.store";

  let currentStep = 2;
  onMount(() => {
    initVoice();
    // if (Object.keys($suggestions).length !== 0) currentStep = 1;
  });

  function nextStep() {
    if (currentStep === 2) return;
    currentStep += 1;
  }
  function prevStep() {
    if (currentStep === 0) return;
    currentStep -= 1;
  }
</script>

<section class="flex flex-col min-h-screen h-full ">
  <Navbar />

  <div
    class="flex flex-col justify-center items-center h-full flex-1
  "
  >
    {#if currentStep === 0}
      <Step1 {nextStep} />
    {/if}
    {#if currentStep === 1}
      <Step2 {nextStep} {prevStep} />
    {/if}
    {#if currentStep === 2}
      <Step3 {prevStep} />
    {/if}
  </div>
</section>
