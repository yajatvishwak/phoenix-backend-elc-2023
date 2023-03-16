<script>
  import { push } from "svelte-spa-router";
  import { onMount } from "svelte";
  import Navbar from "./components/Navbar.svelte";
  import { playDialogue } from "./listener/speak";
  import { cart } from "./store/cart.store";
  onMount(async () => {
    await playDialogue("Complete your purchase");
    setTimeout(async () => {
      await playDialogue("Your Payment has been processed");
      push("/thankyou");
    }, 4000);
  });
</script>

<section class="flex flex-col min-h-screen h-full p-10">
  <Navbar />

  <div
    class="flex flex-col justify-center items-center h-full    flex-1
  "
  >
    <div class="newfont text-5xl">Your Cart</div>

    <div class="flex gap-7 flex-col my-10 max-w-xl  divide-y-2 ">
      {#each $cart as item}
        <div class="flex gap-9 py-7 items-center">
          <div class="w-[700px] h-[200px]">
            <img
              class="w-full h-full  rounded-xl object-cover"
              src={item.img}
              alt=""
            />
          </div>

          <div>
            <div class="text-3xl font-bold">{item.name}</div>
            <div class="line-clamp-2">
              {item.description} Lorem ipsum dolor sit amet consectetur adipisicing
              elit. Laudantium cupiditate aliquam natus ducimus perferendis tenetur
              harum quam! Cupiditate, odit. Quam saepe corporis aperiam blanditiis
              quos ut quas nisi qui facere.
            </div>
          </div>
          <div class="text-xl col-span-2 justify-self-end font-bold">
            ${item.price}
          </div>
        </div>
      {/each}
    </div>
    <div class="border" />
    <div class="flex justify-between items-center w-full max-w-xl">
      <div>
        <div class="">Grand Total</div>
        <div class="text-xl font-bold ">
          $
          {$cart.reduce(
            (accumulator, current) => accumulator + Number(current["price"]),
            0
          )}
        </div>
      </div>
      <button on:click={() => push("/thankyou")} class="btn"
        >Pay and Check out >
      </button>
    </div>
  </div>
</section>
