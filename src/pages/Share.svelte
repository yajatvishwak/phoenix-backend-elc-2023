<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import Navbar from "./components/Navbar.svelte";
  import Step2 from "./preference/Step2.svelte";
  import { suggestions } from "./store/suggestions.store";

  export let params = {};

  let loading = true;

  onMount(async () => {
    let { data } = await axios.get("http://localhost:5000/getmakeupshared");
    console.log(data);
    $suggestions = data;
    loading = false;
  });
</script>

<section class="">
  <Navbar />
  {#if loading}
    <div
      class="flex flex-col justify-center items-center h-full flex-1 animate-pulse"
    >
      Waiting for data...
    </div>
  {:else}
    <div
      class="flex flex-col justify-center items-center h-full flex-1
  "
    >
      <Step2 isShared={true} />
    </div>
  {/if}
</section>
