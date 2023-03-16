<script>
  import Navbar from "./components/Navbar.svelte";
  import anycontrol from "anycontrol";
  import { push } from "svelte-spa-router";
  import { onMount } from "svelte";
  let ctrl = new anycontrol();

  onMount(() => {
    ctrl.DEBUG = true;
    ctrl.addCommand("suggestions", () => {
      ctrl.stop();
      push("/preference");
    });
    ctrl.start();
  });

  let shopData = {
    foundation: [
      {
        name: "foundation1",
        price: 100,
        image:
          "https://www.esteelauder.in/media/export/cms/products/558x768/el_sku_1G5Y84_558x768_0.jpg",
        href: "/foundation/1n1",
        foundationCode: "1n1",
        foundationDesc: "foundation1 description",
      },
      {
        name: "foundation2",
        price: 200,
        image:
          "https://www.esteelauder.in/media/export/cms/products/558x768/el_sku_1G5YC8_558x768_0.jpg",
        href: "/foundation/2n2",
        foundationCode: "2n2",
        foundationDesc: "foundation2 description",
      },
      {
        name: "foundation3",
        price: 300,
        image:
          "https://www.esteelauder.in/media/export/cms/products/558x768/el_sku_1G5Y17_558x768_0.jpg",
        href: "/foundation/3n3",
        foundationCode: "3n3",
        foundationDesc: "foundation3 description",
      },
    ],
    lipsticks: [
      {
        name: "lipstick1",
        price: 100,
        image: "https:via.placeholder.com/234",
        href: "/lipstick/1n1",
        lipstickCode: "1n1",
        lipstickDesc: "lipstick1 description",
      },
      {
        name: "lipstick2",
        price: 200,
        image: "https:via.placeholder.com/234",
        href: "/lipstick/2n2",
        lipstickCode: "2n2",
        lipstickDesc: "lipstick2 description",
      },
      {
        name: "lipstick3",
        price: 300,
        image: "https:via.placeholder.com/234",
        href: "/lipstick/3n3",
        lipstickCode: "3n3",
        lipstickDesc: "lipstick3 description",
      },
    ],
    concealor: [
      {
        name: "concealor1",
        price: 100,
        image: "https:via.placeholder.com/234",
        href: "/concealor/1n1",
        concealorCode: "1n1",
        concealorDesc: "concealor1 description",
      },
      {
        name: "concealor2",
        price: 200,
        image: "https:via.placeholder.com/234",
        href: "/concealor/2n2",
        concealorCode: "2n2",
        concealorDesc: "concealor2 description",
      },
      {
        name: "concealor3",
        price: 300,
        image: "https:via.placeholder.com/234",
        href: "/concealor/3n3",
        concealorCode: "3n3",
        concealorDesc: "concealor3 description",
      },
    ],
  };
</script>

<section class="bg-slate-50 h-full min-h-screen ">
  <Navbar />

  <div class="w-full relative">
    <img src="hero.webp" class=" blur-md " alt="" />
    <div
      class="absolute  top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2  flex items-center justify-center gap-3 flex-col"
    >
      <div class="text-7xl font-black text-white ">
        We are <span class="newfont font-normal text-amber-900"
          >Prestige Beauty
        </span>
      </div>
      <div class="text-white  font-semibold text-3xl">It’s in our DNA</div>
    </div>
  </div>

  <div class="flex flex-col mt-7 p-10">
    <div class="text-8xl font-bold">
      Complete Your <span class="newfont font-normal text-amber-900">
        Look
      </span>
    </div>
    <div class="text-2xl opacity-75 text-amber-900">
      Face the season beautifully with these complexion must-haves.
    </div>
  </div>
  <div id="shop" class="p-10">
    <div class="flex justify-between">
      <div class="py-3 text-3xl font-bold">Foundations</div>
      <button
        class="py-3 hover:opacity-100 transition-all opacity-60  text-xl font-bold"
        >View More ></button
      >
    </div>

    <div class="flex gap-7 w-full">
      {#each shopData.foundation as foundation}
        <a class="flex-1" href={foundation.href}>
          <img src={foundation.image} class="w-full" alt="" />
          <div class="flex justify-between">
            <div class="mt-2 text-2xl newfont">{foundation.name}</div>
            <div class="mt-2 font-bold text-xl">${foundation.price}</div>
          </div>
          <div class="mt-2 text-lg opacity-75">{foundation.foundationDesc}</div>
        </a>
      {/each}
    </div>
    <div class="divider py-10" />
    <div class="flex justify-between">
      <div class="py-3 text-3xl font-bold">Concealor</div>
      <button
        class="py-3 hover:opacity-100 transition-all opacity-60  text-xl font-bold"
        >View More ></button
      >
    </div>
    <div class="flex gap-7 w-full">
      {#each shopData.concealor as concealor}
        <a class="flex-1" href={concealor.href}>
          <img src={concealor.image} class="w-full" alt="" />
          <div class="flex justify-between">
            <div class="mt-2 text-2xl newfont">{concealor.name}</div>
            <div class="mt-2 font-bold text-xl">${concealor.price}</div>
          </div>
          <div class="mt-2 text-lg opacity-75">{concealor.concealorDesc}</div>
        </a>
      {/each}
    </div>
    <div class="divider py-10" />
    <div class="flex justify-between">
      <div class="py-3 text-3xl font-bold">Lipsticks</div>
      <button
        class="py-3 hover:opacity-100 transition-all opacity-60  text-xl font-bold"
        >View More ></button
      >
    </div>
    <div class="flex gap-7 w-full">
      {#each shopData.lipsticks as lipsticks}
        <a class="flex-1" href={lipsticks.href}>
          <img src={lipsticks.image} class="w-full" alt="" />
          <div class="flex justify-between">
            <div class="mt-2 text-2xl newfont">{lipsticks.name}</div>
            <div class="mt-2 font-bold text-xl">${lipsticks.price}</div>
          </div>
          <div class="mt-2 text-lg opacity-75">{lipsticks.concealorDesc}</div>
        </a>
      {/each}
    </div>
  </div>
</section>
