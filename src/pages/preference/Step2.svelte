<script>
  // @ts-nocheck

  import { onMount } from "svelte";
  import { playDialogue } from "../listener/speak";
  import { animateScroll } from "svelte-scrollto-element";
  import { suggestions } from "../store/suggestions.store";
  import { push } from "svelte-spa-router";
  import anycontrol from "anycontrol";
  import axios from "axios";

  export let dialogues = [];
  export let isShared = false;
  export let nextStep = () => {};
  export let prevStep = () => {};
  // $suggestions = {
  //   image: "image.png",
  //   makeup: {
  //     skinColorHex: "564743",
  //     skinUndertone: "Neutral",
  //     suggestedConcealer: {
  //       darkColor: [
  //         null,
  //         {
  //           concealerCode: "8n",
  //           concealerHex: "6E3623",
  //           concealerIntensity: "Very Deep",
  //           concealerName: "Double Wear Radiant Concealer",
  //           concealerUndertone: "Neutral",
  //           distance: 10.026412476142404,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE22_640x640_0.jpg",
  //         },
  //         {
  //           concealerCode: "7n",
  //           concealerHex: "744326",
  //           concealerIntensity: "Ultra Deep",
  //           concealerName: "Double Wear Radiant Concealer",
  //           concealerUndertone: "Neutral",
  //           distance: 13.043120025518256,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE11_640x640_0.jpg",
  //         },
  //       ],
  //       lightColor: [
  //         {
  //           concealerCode: "7n",
  //           concealerHex: "744326",
  //           concealerIntensity: "Ultra Deep",
  //           concealerName: "Double Wear Radiant Concealer",
  //           concealerUndertone: "Neutral",
  //           distance: 13.043120025518256,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE11_640x640_0.jpg",
  //         },
  //         {
  //           concealerCode: "6n",
  //           concealerHex: "A56437",
  //           concealerIntensity: "Extra Deep",
  //           concealerName: "Double Wear Radiant Concealer",
  //           concealerUndertone: "Neutral",
  //           distance: 34.35778479813335,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE06_640x640_0.jpg",
  //         },
  //         {
  //           concealerCode: "5n",
  //           concealerHex: "AA6B3B",
  //           concealerIntensity: "Deep",
  //           concealerName: "Double Wear Radiant Concealer",
  //           concealerUndertone: "Neutral",
  //           distance: 36.35528565608081,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE05_640x640_0.jpg",
  //         },
  //       ],
  //       skinColor: [
  //         {
  //           concealerCode: "8n",
  //           concealerHex: "6E3623",
  //           concealerIntensity: "Very Deep",
  //           concealerName: "Double Wear Radiant Concealer",
  //           concealerUndertone: "Neutral",
  //           distance: 10.026412476142404,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE22_640x640_0.jpg",
  //         },
  //         {
  //           concealerCode: "7n",
  //           concealerHex: "744326",
  //           concealerIntensity: "Ultra Deep",
  //           concealerName: "Double Wear Radiant Concealer",
  //           concealerUndertone: "Neutral",
  //           distance: 13.043120025518256,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE11_640x640_0.jpg",
  //         },
  //         {
  //           concealerCode: "6n",
  //           concealerHex: "A56437",
  //           concealerIntensity: "Extra Deep",
  //           concealerName: "Double Wear Radiant Concealer",
  //           concealerUndertone: "Neutral",
  //           distance: 34.35778479813335,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE06_640x640_0.jpg",
  //         },
  //       ],
  //     },
  //     suggestedFoundation: [
  //       {
  //         colorDetails: {
  //           shadeCode: "8n1",
  //           shadeHex: "5E351A",
  //           shadeName: "Esspresso",
  //           shadeSkinType: "Deep",
  //           shadeUndertone: "Neutral",
  //         },
  //         distance: 15.683398012142446,
  //       },
  //       {
  //         colorDetails: {
  //           shadeCode: "7n1",
  //           shadeHex: "72462A",
  //           shadeName: "Deep Amber",
  //           shadeSkinType: "Deep",
  //           shadeUndertone: "Neutral",
  //         },
  //         distance: 19.00226631235046,
  //       },
  //       {
  //         colorDetails: {
  //           shadeCode: "7c1",
  //           shadeHex: "764122",
  //           shadeName: "Rich Mahogany",
  //           shadeSkinType: "Deep",
  //           shadeUndertone: "Cool",
  //         },
  //         distance: 22.132291427443693,
  //       },
  //     ],
  //     suggestedLipstick: {
  //       coral: [
  //         {
  //           distance: 38.147258409267735,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW24_640x640_0.jpg",
  //           lipstickCode: "662",
  //           lipstickHex: "A63E4C",
  //           lipstickName: "Rule Maker, Pure Color Matte Lipstick",
  //           lipstickType: "Coral",
  //           lipstickUndertone: "Neutral",
  //         },
  //       ],
  //       mauve: [
  //         {
  //           distance: 15.754093987925046,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT08_640x640_0.jpg",
  //           lipstickCode: "672",
  //           lipstickHex: "501F22",
  //           lipstickName: "Intoxicating",
  //           lipstickType: "Mauve",
  //           lipstickUndertone: "Neutral",
  //         },
  //         {
  //           distance: 17.069264812478433,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT01_640x640_0.jpg",
  //           lipstickCode: "697",
  //           lipstickHex: "702025",
  //           lipstickName: "Renegade",
  //           lipstickType: "Mauve",
  //           lipstickUndertone: "Neutral",
  //         },
  //         {
  //           distance: 27.332661008948072,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW07_640x640_0.jpg",
  //           lipstickCode: "690",
  //           lipstickHex: "854950",
  //           lipstickName: "Don't stop, Pure Color Matte Lipstick",
  //           lipstickType: "Mauve",
  //           lipstickUndertone: "Neutral",
  //         },
  //       ],
  //       nude: [
  //         {
  //           distance: 14.578526406881448,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW17_640x640_0.jpg",
  //           lipstickCode: "860",
  //           lipstickHex: "604441",
  //           lipstickName: "Sultry, Pure Color Matte Lipstick",
  //           lipstickType: "Nude",
  //           lipstickUndertone: "Neutral",
  //         },
  //         {
  //           distance: 15.203368700676604,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW12_640x640_0.jpg",
  //           lipstickCode: "812",
  //           lipstickHex: "6C3736",
  //           lipstickName: "Change the world, Pure color matte lipstick,",
  //           lipstickType: "Nude",
  //           lipstickUndertone: "Neutral",
  //         },
  //         {
  //           distance: 36.210970960206396,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW15_640x640_0.jpg",
  //           lipstickCode: "809",
  //           lipstickHex: "99656F",
  //           lipstickName: "Secret Scandal, Pure Color Matte Lipstick",
  //           lipstickType: "Nude",
  //           lipstickUndertone: "Neutral",
  //         },
  //       ],
  //       pink: [
  //         {
  //           distance: 14.113873592339603,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW03_640x640_0.jpg",
  //           lipstickCode: "888",
  //           lipstickHex: "61171A",
  //           lipstickName: "Power Kiss, Pure color matte lipstick,",
  //           lipstickType: "Pink",
  //           lipstickUndertone: "Neutral",
  //         },
  //         {
  //           distance: 39.86615232522734,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT20_640x640_0.jpg",
  //           lipstickCode: "882",
  //           lipstickHex: "AB4351",
  //           lipstickName: "Guilty Pleasure",
  //           lipstickType: "Pink",
  //           lipstickUndertone: "Neutral",
  //         },
  //         {
  //           distance: 42.42359414351608,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFWRR_640x640_0.jpg",
  //           lipstickCode: "420",
  //           lipstickHex: "B05363",
  //           lipstickName: "Rebellious Red, Pure color matte lipstick,",
  //           lipstickType: "Pink",
  //           lipstickUndertone: "Neutral",
  //         },
  //       ],
  //       red: [
  //         {
  //           distance: 19.83268040944013,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW28_640x640_0.jpg",
  //           lipstickCode: "689",
  //           lipstickHex: "7A1E21",
  //           lipstickName: "Dark Desire, Pure Color Matte Lipstick",
  //           lipstickType: "Red",
  //           lipstickUndertone: "Neutral",
  //         },
  //         {
  //           distance: 29.013511085739186,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW29_640x640_0.jpg",
  //           lipstickCode: "606",
  //           lipstickHex: "932529",
  //           lipstickName: "Red Ego, Pure Color Matte Lipstick",
  //           lipstickType: "Red",
  //           lipstickUndertone: "Neutral",
  //         },
  //         {
  //           distance: 38.65545598227306,
  //           img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW46_640x640_0.jpg",
  //           lipstickCode: "559",
  //           lipstickHex: "B0282D",
  //           lipstickName: "Demand, Pure Color Matte Lipstick",
  //           lipstickType: "Red",
  //           lipstickUndertone: "Neutral",
  //         },
  //       ],
  //     },
  //   },
  // };

  let loading = false;
  let foundationHighlight = false;
  let darkconcealerHighlight = false;
  let skinconcealerHighlight = false;
  let lightconcealerHighlight = false;
  let redlipHighlight = false;
  let coralHighlight = false;
  let pinkHighlight = false;
  let mauveHighlight = false;
  let nudeHighlight = false;
  function removeNull(array) {
    return array.filter((x) => x !== null);
  }
  onMount(async () => {
    console.log(dialogues);

    $suggestions.makeup.suggestedConcealer.darkColor = removeNull(
      $suggestions.makeup.suggestedConcealer.darkColor
    );
    $suggestions.makeup.suggestedConcealer.lightColor = removeNull(
      $suggestions.makeup.suggestedConcealer.lightColor
    );
    $suggestions.makeup.suggestedConcealer.skinColor = removeNull(
      $suggestions.makeup.suggestedConcealer.skinColor
    );

    if (!isShared) {
      loading = true;
      await playDialogue(
        "You look gorgeous today! I've analysed your skin. And here's what I found out"
      );
      loading = false;

      let skintoneDialogue = [];
      if ($suggestions.makeup.skinUndertone === "Warm") {
        skintoneDialogue.push("You have a warm undertone");
        skintoneDialogue.push(
          "Warm tone is a beautiful characteristic that adds richness and depth to a person's appearance."
        );
        skintoneDialogue.push(
          "It is often described as having a golden, peachy, or yellow undertone that feels like sunshine or warmth against the skin. "
        );
        skintoneDialogue.push(
          "Just like the way a warm fire feels on a chilly evening or the way a comforting hug feels, warm skin tone can bring a sense of comfort and ease to those who possess it"
        );
        skintoneDialogue.push(
          "We've selected some foundation shades that suit you"
        );
        skintoneDialogue.push(
          "According to your skin tone, we recommend you to use " +
            $suggestions.makeup.suggestedFoundation[0].colorDetails.shadeName +
            " foundation to achieve a natural look"
        );
        skintoneDialogue.push(
          "The perfect true to your skintone concealer that goes along with the foundation is the " +
            $suggestions.makeup.suggestedConcealer.skinColor[0].concealerCode +
            " " +
            $suggestions.makeup.suggestedConcealer.skinColor[0]
              .concealerIntensity +
            " concealer"
        );

        skintoneDialogue.push(
          "We've also picked out darker, " +
            $suggestions.makeup.suggestedConcealer.darkColor[0].concealerCode +
            " and lighter, " +
            $suggestions.makeup.suggestedConcealer.lightColor[0].concealerCode +
            " concealer shades for you"
        );
        skintoneDialogue.push(
          "The red lipstick that goes along with your skin tone is the " +
            $suggestions.makeup.suggestedLipstick.red[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.red[0].lipstickName
        );
        skintoneDialogue.push(
          "The mauve lipstick that suits you is the " +
            $suggestions.makeup.suggestedLipstick.mauve[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.mauve[0].lipstickName
        );
        skintoneDialogue.push(
          "The pink lipstick that looks good on you is the " +
            $suggestions.makeup.suggestedLipstick.pink[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.pink[0].lipstickName
        );
        skintoneDialogue.push(
          "The coral lipstick that you could rock is the " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickName
        );
        skintoneDialogue.push(
          "The nude lipstick that you could use everyday is the " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickName
        );
      } else if ($suggestions.makeup.skinUndertone === "Cool") {
        skintoneDialogue.push("You have a cool undertone");
        skintoneDialogue.push(
          "Cool skin tone is a captivating characteristic that gives a person's appearance a touch of serenity and refinement."
        );
        skintoneDialogue.push(
          "It is often described as having pink, red, or blue undertones. Imagine the feeling of standing on a mountaintop, surrounded by the soft mist and serene silence."
        );
        skintoneDialogue.push(
          "That is the feeling of coolness that comes with a cool skin tone, a beautiful and unique characteristic that can enhance a person's beauty and create a sense of peace and wonder"
        );
        skintoneDialogue.push(
          "We've selected some foundation shades that suit you"
        );
        skintoneDialogue.push(
          "According to your skin tone, we recommend you to use " +
            $suggestions.makeup.suggestedFoundation[0].colorDetails.shadeName +
            " foundation to achieve a natural look"
        );
        skintoneDialogue.push(
          "The perfect true to your skintone concealer that goes along with the foundation is the " +
            $suggestions.makeup.suggestedConcealer.skinColor[0].concealerCode +
            " " +
            $suggestions.makeup.suggestedConcealer.skinColor[0]
              .concealerIntensity +
            " concealer"
        );

        skintoneDialogue.push(
          "We've also picked out darker, " +
            $suggestions.makeup.suggestedConcealer.darkColor[0].concealerCode +
            " and lighter, " +
            $suggestions.makeup.suggestedConcealer.lightColor[0].concealerCode +
            " concealer shades for you"
        );
        skintoneDialogue.push(
          "The red lipstick that goes along with your skin tone is the " +
            $suggestions.makeup.suggestedLipstick.red[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.red[0].lipstickName
        );
        skintoneDialogue.push(
          "The mauve lipstick that suits you is the " +
            $suggestions.makeup.suggestedLipstick.mauve[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.mauve[0].lipstickName
        );
        skintoneDialogue.push(
          "The pink lipstick that looks good on you is the " +
            $suggestions.makeup.suggestedLipstick.pink[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.pink[0].lipstickName
        );
        skintoneDialogue.push(
          "The coral lipstick that you could rock is the " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickName
        );
        skintoneDialogue.push(
          "The nude lipstick that you could use everyday is the " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickName
        );
      } else {
        skintoneDialogue.push("You have a neutral undertone");
        skintoneDialogue.push(
          "Neutral skin tone is a stunning characteristic that gives a person's appearance a sense of balance and versatility"
        );
        skintoneDialogue.push(
          "it is often described as having a combination of warm and cool undertones. imagine the soft and gentle touch of a warm summer breeze, as it moves gracefully through the air."
        );
        skintoneDialogue.push(
          "That is the feeling of natural beauty that comes with a neutral skin tone, a stunning and unique characteristic that can enhance a person's beauty and bring a sense of versatility to their appearance"
        );
        skintoneDialogue.push(
          "We've selected some foundation shades that suit you"
        );
        skintoneDialogue.push(
          "According to your skin tone, we recommend you to use " +
            $suggestions.makeup.suggestedFoundation[0].colorDetails.shadeName +
            " foundation to achieve a natural look"
        );
        skintoneDialogue.push(
          "The perfect true to your skintone concealer that goes along with the foundation is the " +
            $suggestions.makeup.suggestedConcealer.skinColor[0].concealerCode +
            " " +
            $suggestions.makeup.suggestedConcealer.skinColor[0]
              .concealerIntensity +
            " concealer"
        );

        skintoneDialogue.push(
          "We've also picked out darker, " +
            $suggestions.makeup.suggestedConcealer.darkColor[0].concealerCode +
            " and lighter, " +
            $suggestions.makeup.suggestedConcealer.lightColor[0].concealerCode +
            " concealer shades for you"
        );
        skintoneDialogue.push(
          "The red lipstick that goes along with your skin tone is the " +
            $suggestions.makeup.suggestedLipstick.red[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.red[0].lipstickName
        );
        skintoneDialogue.push(
          "The mauve lipstick that suits you is the " +
            $suggestions.makeup.suggestedLipstick.mauve[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.mauve[0].lipstickName
        );
        skintoneDialogue.push(
          "The pink lipstick that looks good on you is the " +
            $suggestions.makeup.suggestedLipstick.pink[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.pink[0].lipstickName
        );
        skintoneDialogue.push(
          "The coral lipstick that you could rock is the " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickName
        );
        skintoneDialogue.push(
          "The nude lipstick that you could use everyday is the " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickCode +
            " " +
            $suggestions.makeup.suggestedLipstick.coral[0].lipstickName
        );
      }
      for (let i = 0; i < skintoneDialogue.length; i++) {
        await playDialogue(skintoneDialogue[i]);
        if (i == 4) highlight("foundation");
        if (i == 5) highlight("skinconcealer");
        if (i == 6) highlight("darkconcealer");
        if (i == 6) highlight("lightconcealer");
        if (i == 7) highlight("redlip");
        if (i == 8) highlight("mauvelip");
        if (i == 9) highlight("pinklip");
        if (i == 10) highlight("corallip");
        if (i == 11) highlight("nudelip");
      }
      await playDialogue(
        "There's a few things you can do, ask me to preview or share your results"
      );
      await playDialogue(
        "I can also show you the recommended products or help you retake the picture for a better result"
      );
      let ctrl = new anycontrol();
      ctrl.DEBUG = true;
      ctrl.addCommand("products", () => {
        ctrl.stop();
        nextStep();
      });
      ctrl.addCommand("show", () => {
        ctrl.stop();
        nextStep();
      });
      ctrl.addCommand("next", () => {
        ctrl.stop();
        nextStep();
      });
      ctrl.addCommand("back", () => {
        ctrl.stop();
        prevStep();
      });
      ctrl.addCommand("retake", () => {
        ctrl.stop();
        prevStep();
      });
      ctrl.addCommand("preview", () => {
        ctrl.stop();
        push("/preview");
      });
      ctrl.addCommand("share", async () => {
        await axios.get("http://localhost:5000/sendmessage");
        await playDialogue(
          "We've shared your results with your saved contacts"
        );
      });
      ctrl.start();
    }
  });
  function showPreview() {
    push("/preview");
  }
  function highlight(type) {
    if (type === "foundation") {
      foundationHighlight = true;
      animateScroll.scrollTo({
        element: "#foundation",
        maxDuration: 2000,
      });
    } else if (type === "redlip") {
      redlipHighlight = true;
      animateScroll.scrollTo({
        element: "#redlip",
        maxDuration: 2000,
      });
    } else if (type === "darkconcealer") {
      darkconcealerHighlight = true;
      animateScroll.scrollTo({
        element: "#darkconcealer",
        maxDuration: 2000,
      });
    } else if (type === "lightconcealer") {
      lightconcealerHighlight = true;
      animateScroll.scrollTo({
        element: "#lightconcealer",
        maxDuration: 2000,
      });
    } else if (type === "skinconcealer") {
      skinconcealerHighlight = true;
      animateScroll.scrollTo({
        element: "#skinconcealer",
        maxDuration: 2000,
      });
    } else if (type === "mauvelip") {
      mauveHighlight = true;
      animateScroll.scrollTo({
        element: "#mauvelip",
        maxDuration: 2000,
      });
    } else if (type === "nudelip") {
      nudeHighlight = true;
      animateScroll.scrollTo({
        element: "#nudelip",
        maxDuration: 2000,
      });
    } else if (type === "pinklip") {
      pinkHighlight = true;
      animateScroll.scrollTo({
        element: "#pinklip",
        maxDuration: 2000,
      });
    } else if (type === "corallip") {
      coralHighlight = true;
      animateScroll.scrollTo({
        element: "#corallip",
        maxDuration: 2000,
      });
    }
  }
</script>

<div>
  {#if loading}
    <div class="flex flex-col justify-center items-center h-full flex-1">
      <div class="text-2xl animate-pulse">Analysing your skin...</div>
    </div>
  {:else}
    <div class="grid grid-cols-2 gap-14 mt-20">
      <div class="flex flex-col justify-center items-center gap-4 ">
        <div class="max-w-lg">
          <img
            class="w-full border rounded-lg"
            src={"http://localhost:5000/getfile/" + $suggestions.image}
            alt=""
          />
        </div>
        <div class="grid grid-cols-2  w-full gap-3 ">
          <div class="flex flex-col gap-2 ">
            <div
              class="w-16 h-16 rounded-full "
              style="width:64px; height:64px; background-color:{'#' +
                $suggestions.makeup.skinColorHex}"
            />
            <div>Your skin color</div>
          </div>
          <div class="flex flex-col  justify-center items-end">
            <div>You have a</div>
            <div
              class="text-5xl font-bold"
              style="color:{'#' + $suggestions.makeup.skinColorHex}"
            >
              {$suggestions.makeup.skinUndertone}
            </div>
            <div>undertone</div>
          </div>
        </div>
      </div>
      <div id="foundation" class="">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested foundations
        </div>
        <div class="flex flex-col  gap-4 mt-10">
          {#each $suggestions.makeup.suggestedFoundation as foundation, index}
            <div
              class="flex p-3 rounded-lg items-center justify-center gap-2 {foundationHighlight &&
              index == 0
                ? 'border border-blue-500'
                : ''}"
            >
              <div class="flex-1 text-xl">
                {foundation.colorDetails.shadeName}
              </div>
              <div
                class="w-16 h-16 rounded-full flex items-center justify-center p-2 "
                style="width:64px; height:64px; background-color:{'#' +
                  foundation.colorDetails.shadeHex}"
              >
                <span class="opacity-50 font-bold text-white"
                  >{foundation.colorDetails.shadeCode}</span
                >
              </div>
            </div>
          {/each}
        </div>
      </div>
      <div id="skinconcealer" class="my-8 col-span-2">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested Skin Concealers
        </div>

        <div class="flex flex-col gap-3 mt-10">
          {#each $suggestions.makeup.suggestedConcealer.skinColor as concealer, index}
            {#if concealer}
              <div
                class="flex  items-center justify-center gap-6  p-3 rounded-xl {skinconcealerHighlight &&
                index == 0
                  ? 'border border-blue-500'
                  : ''} "
              >
                <div class="text-xl">
                  {concealer.concealerIntensity}/{concealer.concealerUndertone}
                </div>
                <div
                  class="w-16 h-16 flex-1  rounded-full flex items-center justify-center p-2 "
                  style="width:64px; height:64px; background-color:{'#' +
                    concealer.concealerHex}"
                >
                  <span class="opacity-50 font-bold text-white"
                    >{concealer.concealerCode}</span
                  >
                </div>
              </div>
            {/if}
          {/each}
        </div>
      </div>
      <div id="darkconcealer" class="my-8">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested Dark Concealers
        </div>

        <div class="flex flex-col gap-3 mt-10">
          {#each $suggestions.makeup.suggestedConcealer.darkColor as concealer, index}
            {#if concealer}
              <div
                class="flex  items-center justify-center gap-6 p-3 rounded-xl  {darkconcealerHighlight &&
                index == 0
                  ? 'border border-blue-500'
                  : ''}"
              >
                <div
                  class="w-16 h-16 flex-1  rounded-full flex items-center justify-center p-2 "
                  style="width:64px; height:64px; background-color:{'#' +
                    concealer.concealerHex}"
                >
                  <span class="opacity-50 font-bold text-white"
                    >{concealer.concealerCode}</span
                  >
                </div>
                <div class="text-xl">
                  {concealer.concealerIntensity}/{concealer.concealerUndertone}
                </div>
              </div>
            {/if}
          {/each}
        </div>
      </div>
      <div id="lightconcealer" class="my-8">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested Light Concealers
        </div>

        <div class="flex flex-col gap-3 mt-10">
          {#each $suggestions.makeup.suggestedConcealer.lightColor as concealer, index}
            {#if concealer}
              <div
                class="flex  items-center justify-center gap-6 p-3 rounded-xl {lightconcealerHighlight &&
                index == 0
                  ? 'border border-blue-500'
                  : ''}"
              >
                <div
                  class="w-16 h-16 flex-1  rounded-full flex items-center justify-center"
                  style="width:64px; height:64px; background-color:{'#' +
                    concealer.concealerHex}"
                >
                  <span class="opacity-50 font-bold text-white"
                    >{concealer.concealerCode}</span
                  >
                </div>
                <div class="text-xl">
                  {concealer.concealerIntensity}/{concealer.concealerUndertone}
                </div>
              </div>
            {/if}
          {/each}
        </div>
      </div>
      <div id="redlip" class="col-span-2">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested Red Lipsticks
        </div>

        <div class="flex gap-6">
          {#each $suggestions.makeup.suggestedLipstick.red as lipstick, index}
            <div
              class="flex flex-col flex-1 items-center justify-center p-3  gap-4 text-center rounded-xl {redlipHighlight &&
              index == 0
                ? 'border border-blue-500'
                : ''}"
            >
              <div
                class="w-16 h-16 flex-1 py-10 rounded-full flex items-center justify-center p-2 "
                style="width:64px; height:64px; background-color:{'#' +
                  lipstick.lipstickHex}"
              >
                <span class="opacity-50 font-bold text-white"
                  >{lipstick.lipstickCode}</span
                >
              </div>
              <div>{lipstick.lipstickName}</div>
            </div>
          {/each}
        </div>
      </div>
      <div id="pinklip" class="max-w-md">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested Pink Lipsticks
        </div>

        <div class="flex gap-6">
          {#each $suggestions.makeup.suggestedLipstick.pink as lipstick, index}
            <div
              class="flex flex-col flex-1 items-center justify-center p-3 gap-4 text-center rounded-xl {pinkHighlight &&
              index == 0
                ? 'border border-blue-500'
                : ''}"
            >
              <div
                class="w-16 h-16 flex-1 py-10 rounded-full flex items-center justify-center p-2 "
                style="width:64px; height:64px; background-color:{'#' +
                  lipstick.lipstickHex}"
              >
                <span class="opacity-50 font-bold text-white"
                  >{lipstick.lipstickCode}</span
                >
              </div>
              <div class="">{lipstick.lipstickName}</div>
            </div>
          {/each}
        </div>
      </div>
      <div id="mauvelip" class="max-w-md">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested Mauve Lipsticks
        </div>

        <div class="flex gap-6">
          {#each $suggestions.makeup.suggestedLipstick.mauve as lipstick, index}
            <div
              class="flex flex-col flex-1 items-center justify-center p-3 rounded-xl  text-center gap-4 {mauveHighlight &&
              index == 0
                ? 'border border-blue-500'
                : ''}"
            >
              <div
                class="w-16 h-16 flex-1 py-10 rounded-full flex items-center justify-center p-2 "
                style="width:64px; height:64px; background-color:{'#' +
                  lipstick.lipstickHex}"
              >
                <span class="opacity-50 font-bold text-white"
                  >{lipstick.lipstickCode}</span
                >
              </div>
              <div>{lipstick.lipstickName}</div>
            </div>
          {/each}
        </div>
      </div>
      <div id="nudelip" class="max-w-md">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested Nude Lipsticks
        </div>

        <div class="flex gap-6">
          {#each $suggestions.makeup.suggestedLipstick.nude as lipstick, index}
            <div
              class="flex flex-col flex-1 items-center justify-center p-3 rounded-xl gap-4 text-center {nudeHighlight &&
              index == 0
                ? 'border border-blue-500'
                : ''}"
            >
              <div
                class="w-16 h-16 flex-1 py-10 rounded-full flex items-center justify-center p-2 "
                style="width:64px; height:64px; background-color:{'#' +
                  lipstick.lipstickHex}"
              >
                <span class="opacity-50 font-bold text-white"
                  >{lipstick.lipstickCode}</span
                >
              </div>
              <div>{lipstick.lipstickName}</div>
            </div>
          {/each}
        </div>
      </div>
      <div id="corallip" class="max-w-md">
        <div class="text-xl font-bold opacity-50 divider">
          Suggested Coral Lipsticks
        </div>

        <div class="flex gap-6">
          {#each $suggestions.makeup.suggestedLipstick.coral as lipstick, index}
            <div
              class="flex flex-col gap-4 flex-1 items-center justify-center p-3 rounded-xl text-center  {coralHighlight &&
              index == 0
                ? 'border border-blue-500'
                : ''}"
            >
              <div
                class="w-16 h-16 flex-1 py-10 rounded-full flex items-center justify-center p-2 "
                style="width:64px; height:64px; background-color:{'#' +
                  lipstick.lipstickHex}"
              >
                <span class="opacity-50 font-bold text-white"
                  >{lipstick.lipstickCode}</span
                >
              </div>
              <div>{lipstick.lipstickName}</div>
            </div>
          {/each}
        </div>
      </div>
    </div>
    <div class="my-6 flex gap-4 items-center">
      {#if !isShared}
        <button on:click={nextStep} class="btn"> Next </button>
      {/if}
      <button on:click={showPreview} class="btn btn-outline">
        Show Preview
      </button>
    </div>
  {/if}
</div>
