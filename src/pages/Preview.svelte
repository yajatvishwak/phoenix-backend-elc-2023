<script>
  // @ts-nocheck

  import { onMount } from "svelte";
  import anycontrol from "anycontrol";
  import Navbar from "./components/Navbar.svelte";
  import { pop, push } from "svelte-spa-router";
  import axios from "axios";
  import { suggestions } from "./store/suggestions.store";
  let data = {
    foundations: [
      { link: "https://via.placeholder.com/500", productname: "foundation 1" },
      { link: "https://via.placeholder.com/500", productname: "foundation 2" },
      { link: "https://via.placeholder.com/500", productname: "foundation 3" },
      { link: "https://via.placeholder.com/500", productname: "foundation 4" },
    ],
  };
  //   $suggestions = {
  //     image: "image.png",
  //     makeup: {
  //       skinColorHex: "564743",
  //       skinUndertone: "Neutral",
  //       suggestedConcealer: {
  //         darkColor: [
  //           null,
  //           {
  //             concealerCode: "8n",
  //             concealerHex: "6E3623",
  //             concealerIntensity: "Very Deep",
  //             concealerName: "Double Wear Radiant Concealer",
  //             concealerUndertone: "Neutral",
  //             distance: 10.026412476142404,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE22_640x640_0.jpg",
  //           },
  //           {
  //             concealerCode: "7n",
  //             concealerHex: "744326",
  //             concealerIntensity: "Ultra Deep",
  //             concealerName: "Double Wear Radiant Concealer",
  //             concealerUndertone: "Neutral",
  //             distance: 13.043120025518256,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE11_640x640_0.jpg",
  //           },
  //         ],
  //         lightColor: [
  //           {
  //             concealerCode: "7n",
  //             concealerHex: "744326",
  //             concealerIntensity: "Ultra Deep",
  //             concealerName: "Double Wear Radiant Concealer",
  //             concealerUndertone: "Neutral",
  //             distance: 13.043120025518256,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE11_640x640_0.jpg",
  //           },
  //           {
  //             concealerCode: "6n",
  //             concealerHex: "A56437",
  //             concealerIntensity: "Extra Deep",
  //             concealerName: "Double Wear Radiant Concealer",
  //             concealerUndertone: "Neutral",
  //             distance: 34.35778479813335,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE06_640x640_0.jpg",
  //           },
  //           {
  //             concealerCode: "5n",
  //             concealerHex: "AA6B3B",
  //             concealerIntensity: "Deep",
  //             concealerName: "Double Wear Radiant Concealer",
  //             concealerUndertone: "Neutral",
  //             distance: 36.35528565608081,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE05_640x640_0.jpg",
  //           },
  //         ],
  //         skinColor: [
  //           {
  //             concealerCode: "8n",
  //             concealerHex: "6E3623",
  //             concealerIntensity: "Very Deep",
  //             concealerName: "Double Wear Radiant Concealer",
  //             concealerUndertone: "Neutral",
  //             distance: 10.026412476142404,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE22_640x640_0.jpg",
  //           },
  //           {
  //             concealerCode: "7n",
  //             concealerHex: "744326",
  //             concealerIntensity: "Ultra Deep",
  //             concealerName: "Double Wear Radiant Concealer",
  //             concealerUndertone: "Neutral",
  //             distance: 13.043120025518256,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE11_640x640_0.jpg",
  //           },
  //           {
  //             concealerCode: "6n",
  //             concealerHex: "A56437",
  //             concealerIntensity: "Extra Deep",
  //             concealerName: "Double Wear Radiant Concealer",
  //             concealerUndertone: "Neutral",
  //             distance: 34.35778479813335,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE06_640x640_0.jpg",
  //           },
  //         ],
  //       },
  //       suggestedFoundation: [
  //         {
  //           colorDetails: {
  //             shadeCode: "8n1",
  //             shadeHex: "5E351A",
  //             shadeName: "Esspresso",
  //             shadeSkinType: "Deep",
  //             shadeUndertone: "Neutral",
  //           },
  //           distance: 15.683398012142446,
  //         },
  //         {
  //           colorDetails: {
  //             shadeCode: "7n1",
  //             shadeHex: "72462A",
  //             shadeName: "Deep Amber",
  //             shadeSkinType: "Deep",
  //             shadeUndertone: "Neutral",
  //           },
  //           distance: 19.00226631235046,
  //         },
  //         {
  //           colorDetails: {
  //             shadeCode: "7c1",
  //             shadeHex: "764122",
  //             shadeName: "Rich Mahogany",
  //             shadeSkinType: "Deep",
  //             shadeUndertone: "Cool",
  //           },
  //           distance: 22.132291427443693,
  //         },
  //       ],
  //       suggestedLipstick: {
  //         coral: [
  //           {
  //             distance: 38.147258409267735,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW24_640x640_0.jpg",
  //             lipstickCode: "662",
  //             lipstickHex: "A63E4C",
  //             lipstickName: "Rule Maker, Pure Color Matte Lipstick",
  //             lipstickType: "Coral",
  //             lipstickUndertone: "Neutral",
  //           },
  //         ],
  //         mauve: [
  //           {
  //             distance: 15.754093987925046,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT08_640x640_0.jpg",
  //             lipstickCode: "672",
  //             lipstickHex: "501F22",
  //             lipstickName: "Intoxicating",
  //             lipstickType: "Mauve",
  //             lipstickUndertone: "Neutral",
  //           },
  //           {
  //             distance: 17.069264812478433,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT01_640x640_0.jpg",
  //             lipstickCode: "697",
  //             lipstickHex: "702025",
  //             lipstickName: "Renegade",
  //             lipstickType: "Mauve",
  //             lipstickUndertone: "Neutral",
  //           },
  //           {
  //             distance: 27.332661008948072,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW07_640x640_0.jpg",
  //             lipstickCode: "690",
  //             lipstickHex: "854950",
  //             lipstickName: "Don't stop, Pure Color Matte Lipstick",
  //             lipstickType: "Mauve",
  //             lipstickUndertone: "Neutral",
  //           },
  //         ],
  //         nude: [
  //           {
  //             distance: 14.578526406881448,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW17_640x640_0.jpg",
  //             lipstickCode: "860",
  //             lipstickHex: "604441",
  //             lipstickName: "Sultry, Pure Color Matte Lipstick",
  //             lipstickType: "Nude",
  //             lipstickUndertone: "Neutral",
  //           },
  //           {
  //             distance: 15.203368700676604,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW12_640x640_0.jpg",
  //             lipstickCode: "812",
  //             lipstickHex: "6C3736",
  //             lipstickName: "Change the world, Pure color matte lipstick,",
  //             lipstickType: "Nude",
  //             lipstickUndertone: "Neutral",
  //           },
  //           {
  //             distance: 36.210970960206396,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW15_640x640_0.jpg",
  //             lipstickCode: "809",
  //             lipstickHex: "99656F",
  //             lipstickName: "Secret Scandal, Pure Color Matte Lipstick",
  //             lipstickType: "Nude",
  //             lipstickUndertone: "Neutral",
  //           },
  //         ],
  //         pink: [
  //           {
  //             distance: 14.113873592339603,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW03_640x640_0.jpg",
  //             lipstickCode: "888",
  //             lipstickHex: "61171A",
  //             lipstickName: "Power Kiss, Pure color matte lipstick,",
  //             lipstickType: "Pink",
  //             lipstickUndertone: "Neutral",
  //           },
  //           {
  //             distance: 39.86615232522734,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT20_640x640_0.jpg",
  //             lipstickCode: "882",
  //             lipstickHex: "AB4351",
  //             lipstickName: "Guilty Pleasure",
  //             lipstickType: "Pink",
  //             lipstickUndertone: "Neutral",
  //           },
  //           {
  //             distance: 42.42359414351608,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFWRR_640x640_0.jpg",
  //             lipstickCode: "420",
  //             lipstickHex: "B05363",
  //             lipstickName: "Rebellious Red, Pure color matte lipstick,",
  //             lipstickType: "Pink",
  //             lipstickUndertone: "Neutral",
  //           },
  //         ],
  //         red: [
  //           {
  //             distance: 19.83268040944013,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW28_640x640_0.jpg",
  //             lipstickCode: "689",
  //             lipstickHex: "7A1E21",
  //             lipstickName: "Dark Desire, Pure Color Matte Lipstick",
  //             lipstickType: "Red",
  //             lipstickUndertone: "Neutral",
  //           },
  //           {
  //             distance: 29.013511085739186,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW29_640x640_0.jpg",
  //             lipstickCode: "606",
  //             lipstickHex: "932529",
  //             lipstickName: "Red Ego, Pure Color Matte Lipstick",
  //             lipstickType: "Red",
  //             lipstickUndertone: "Neutral",
  //           },
  //           {
  //             distance: 38.65545598227306,
  //             img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW46_640x640_0.jpg",
  //             lipstickCode: "559",
  //             lipstickHex: "B0282D",
  //             lipstickName: "Demand, Pure Color Matte Lipstick",
  //             lipstickType: "Red",
  //             lipstickUndertone: "Neutral",
  //           },
  //         ],
  //       },
  //     },
  //   };
  let loading = true;
  onMount(async () => {
    let lipsticks = [];
    lipsticks = [
      ...$suggestions.makeup.suggestedLipstick.coral,
      ...$suggestions.makeup.suggestedLipstick.mauve,
      ...$suggestions.makeup.suggestedLipstick.red,
      ...$suggestions.makeup.suggestedLipstick.pink,
    ];
    lipsticks = lipsticks.map((lipstick) => lipstick.lipstickCode);
    let foundations = [
      ...$suggestions.makeup.suggestedFoundation.map((f) => f.colorDetails),
    ];
    foundations = foundations.map((foundation) => foundation.shadeCode);
    loading = true;
    const res = await axios.post("http://localhost:5000/getpreviewlinks", {
      foundations,
      lipsticks,
    });
    loading = false;
    data = res.data;
    console.log(data);

    let ctrl = new anycontrol();
    ctrl.DEBUG = true;

    ctrl.addCommand("back", () => {
      ctrl.stop();
      pop();
    });
    ctrl.start();
  });
</script>

<section class="">
  <Navbar />

  {#if loading}
    <div>Loading...</div>
  {:else}
    <div class="px-60 font-bold text-3xl my-6">Foundations</div>

    <div class="grid grid-cols-3 gap-10 px-60">
      {#each data.foundations as { link, productname }}
        <div class="flex flex-col gap-2">
          <img src={link} alt="" srcset="" />
          <div class="text-xl ">{productname}</div>
        </div>
      {/each}
    </div>
    <div class="divider px-80 pt-10" />
    <div class="px-60 font-bold text-3xl my-6 ">Lipsticks</div>

    <div class="grid grid-cols-3 gap-10 px-60">
      {#each data.lipstick as { link, productname }}
        <div class="flex flex-col gap-2">
          <img src={link} alt="" srcset="" />
          <div class="text-xl ">{productname}</div>
        </div>
      {/each}
    </div>
  {/if}
</section>
