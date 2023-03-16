<script>
  // @ts-nocheck

  import { onMount } from "svelte";
  import { cart } from "../store/cart.store";
  import { usersaid } from "../store/usersaid.store";
  import { playDialogue, playSound } from "../listener/speak";
  import anycontrol from "anycontrol";
  import { startRecording, stopRecording } from "../listener/listen";
  import wordsToNumbers from "word-to-numbers";
  import { push } from "svelte-spa-router";
  import { suggestions } from "../store/suggestions.store";
  let ctrl = new anycontrol();
  export let prevStep = () => {};

  $suggestions = {
    image: "image.png",
    makeup: {
      skinColorHex: "92796e",
      skinUndertone: "Warm",
      suggestedConcealer: {
        darkColor: [
          {
            concealerCode: "6w",
            concealerHex: "B07255",
            concealerIntensity: "Extra Deep",
            concealerName: "Double Wear Radiant Concealer",
            concealerUndertone: "Warm",
            distance: 10.111346656288491,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE19_640x640_0.jpg",
          },
          {
            concealerCode: "5w",
            concealerHex: "B97E57",
            concealerIntensity: "Deep",
            concealerName: "Double Wear Radiant Concealer",
            concealerUndertone: "Warm",
            distance: 12.303776105533213,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE17_640x640_0.jpg",
          },
        ],
        lightColor: [
          {
            concealerCode: "5w",
            concealerHex: "B97E57",
            concealerIntensity: "Deep",
            concealerName: "Double Wear Radiant Concealer",
            concealerUndertone: "Warm",
            distance: 12.303776105533213,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE17_640x640_0.jpg",
          },
          {
            concealerCode: "4w",
            concealerHex: "CB9870",
            concealerIntensity: "Medium Deep",
            concealerName: "Double Wear Radiant Concealer",
            concealerUndertone: "Warm",
            distance: 19.400438251082438,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE15_640x640_0.jpg",
          },
          {
            concealerCode: "3w",
            concealerHex: "E4AA68",
            concealerIntensity: "Medium",
            concealerName: "Double Wear Radiant Concealer",
            concealerUndertone: "Warm",
            distance: 25.306066828730415,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE09_640x640_0.jpg",
          },
        ],
        skinColor: [
          {
            concealerCode: "6w",
            concealerHex: "B07255",
            concealerIntensity: "Extra Deep",
            concealerName: "Double Wear Radiant Concealer",
            concealerUndertone: "Warm",
            distance: 10.111346656288491,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE19_640x640_0.jpg",
          },
          {
            concealerCode: "5w",
            concealerHex: "B97E57",
            concealerIntensity: "Deep",
            concealerName: "Double Wear Radiant Concealer",
            concealerUndertone: "Warm",
            distance: 12.303776105533213,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE17_640x640_0.jpg",
          },
          {
            concealerCode: "4w",
            concealerHex: "CB9870",
            concealerIntensity: "Medium Deep",
            concealerName: "Double Wear Radiant Concealer",
            concealerUndertone: "Warm",
            distance: 19.400438251082438,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_PCCE15_640x640_0.jpg",
          },
        ],
      },
      suggestedFoundation: [
        {
          colorDetails: {
            shadeCode: "6w1",
            shadeHex: "9C633A",
            shadeName: "Sandalwood",
            shadeSkinType: "Deep",
            shadeUndertone: "Warm",
          },
          distance: 13.482330073343302,
        },
        {
          colorDetails: {
            shadeCode: "6w2",
            shadeHex: "915A32",
            shadeName: "Nutmeg",
            shadeSkinType: "Deep",
            shadeUndertone: "Warm",
          },
          distance: 14.744389913109403,
        },
        {
          colorDetails: {
            shadeCode: "5n1.5",
            shadeHex: "A76739",
            shadeName: "Maple",
            shadeSkinType: "Deep",
            shadeUndertone: "Neutral",
          },
          distance: 15.938865732405974,
        },
      ],
      suggestedLipstick: {
        coral: [
          {
            distance: 6.47336011257459,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW50_640x640_0.jpg",
            lipstickCode: "570",
            lipstickHex: "A15642",
            lipstickName: "Fiercely, Pure Color Matte Lipstick",
            lipstickType: "Coral",
            lipstickUndertone: "Warm",
          },
          {
            distance: 10.788680771398555,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW26_640x640_0.jpg",
            lipstickCode: "681",
            lipstickHex: "A15D54",
            lipstickName: "Lure you in, Pure Color Matte Lipstick",
            lipstickType: "Coral",
            lipstickUndertone: "Warm",
          },
          {
            distance: 12.517938716250915,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW44_640x640_0.jpg",
            lipstickCode: "557",
            lipstickHex: "A3504E",
            lipstickName: "Fragile Ego, Pure Color Matte Lipstick",
            lipstickType: "Coral",
            lipstickUndertone: "Warm",
          },
        ],
        mauve: [
          {
            distance: 16.075784908115335,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT18_640x640_0.jpg",
            lipstickCode: "561",
            lipstickHex: "AA6B6D",
            lipstickName: "Intense Nude",
            lipstickType: "Mauve",
            lipstickUndertone: "Warm",
          },
          {
            distance: 17.336076277417668,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW05_640x640_0.jpg",
            lipstickCode: "669",
            lipstickHex: "AF5F66",
            lipstickName: "Stolen heart",
            lipstickType: "Mauve",
            lipstickUndertone: "Warm",
          },
        ],
        nude: [
          {
            distance: 12.271392566198948,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT14_640x640_0.jpg",
            lipstickCode: "818",
            lipstickHex: "A5665E",
            lipstickName: "Covetable",
            lipstickType: "Nude",
            lipstickUndertone: "Warm",
          },
          {
            distance: 13.685234394437849,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW14_640x640_0.jpg",
            lipstickCode: "829",
            lipstickHex: "9C706B",
            lipstickName: "Expose, Pure Color Matte Lipstick",
            lipstickType: "Nude",
            lipstickUndertone: "Warm",
          },
          {
            distance: 15.452506130631578,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW51_640x640_0.jpg",
            lipstickCode: "867",
            lipstickHex: "81423B",
            lipstickName: "Knowing, Pure Color Matte Lipstick",
            lipstickType: "Nude",
            lipstickUndertone: "Warm",
          },
        ],
        pink: [
          {
            distance: 16.99982725819526,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW01_640x640_0.jpg",
            lipstickCode: "856",
            lipstickHex: "A64A55",
            lipstickName: "Object of Desire, Pure color matte lipstick,",
            lipstickType: "Pink",
            lipstickUndertone: "Warm",
          },
          {
            distance: 17.515781157937205,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT57_640x640_0.jpg",
            lipstickCode: "131",
            lipstickHex: "B04D56",
            lipstickName: "Bois De Rose",
            lipstickType: "Pink",
            lipstickUndertone: "Warm",
          },
          {
            distance: 24.051988761004228,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFT23_640x640_0.jpg",
            lipstickCode: "260",
            lipstickHex: "CA6674",
            lipstickName: "Eccentric",
            lipstickType: "Pink",
            lipstickUndertone: "Warm",
          },
        ],
        red: [
          {
            distance: 16.794186413841988,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW27_640x640_0.jpg",
            lipstickCode: "699",
            lipstickHex: "AD2D2F",
            lipstickName: "Thrill me, Pure Color Matte Lipstick",
            lipstickType: "Red",
            lipstickUndertone: "Warm",
          },
          {
            distance: 19.016813052772385,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW49_640x640_0.jpg",
            lipstickCode: "569",
            lipstickHex: "8F252B",
            lipstickName: "Fearless, Pure Color Matte Lipstick",
            lipstickType: "Red",
            lipstickUndertone: "Warm",
          },
          {
            distance: 27.344283336543263,
            img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW30_640x640_0.jpg",
            lipstickCode: "667",
            lipstickHex: "C92335",
            lipstickName: "Deny all, Pure Color Matte Lipstick",
            lipstickType: "Red",
            lipstickUndertone: "Warm",
          },
        ],
      },
    },
  };
  let data = {
    foundations: [
      // {
      //   itemID: 1,
      //   name: "Foundation 1",
      //   price: 1000,
      //   description: "A foundation",
      //   img: "https://www.esteelauder.in/media/export/cms/products/558x768/el_sku_1G5Y84_558x768_0.jpg",
      // },
      // {
      //   itemID: 11,
      //   name: "Foundation 2",
      //   price: 1000,
      //   description: "A foundation",
      //   img: "https://www.esteelauder.in/media/export/cms/products/558x768/el_sku_1G5Y93_558x768_0.jpg",
      // },
      // {
      //   itemID: 111,
      //   name: "Foundation 3",
      //   price: 1000,
      //   description: "A foundation",
      //   img: "https://www.esteelauder.in/media/export/cms/products/558x768/el_sku_1G5Y38_558x768_0.jpg",
      // },
    ],
    concealers: [
      // {
      //   itemID: 2,
      //   name: "Concealer 1",
      //   price: 1000,
      //   description: "A concealer",
      //   img: "https://www.esteelauder.in/media/export/cms/products/558x768/el_sku_PCCE09_558x768_0.jpg",
      // },
    ],
    lipsticks: [
      // {
      //   itemID: 3,
      //   name: "Lipstick",
      //   price: 1000,
      //   description: "A lipstick",
      //   img: "https://www.esteelauder.com/media/export/cms/products/640x640/el_sku_GRFW21_640x640_0.jpg",
      // },
    ],
  };

  onMount(async () => {
    console.log($suggestions);
    data.concealers = [
      ...$suggestions.makeup.suggestedConcealer.darkColor,
      ...$suggestions.makeup.suggestedConcealer.lightColor,
      ...$suggestions.makeup.suggestedConcealer.skinColor,
    ];

    data.foundations = [
      ...$suggestions.makeup.suggestedFoundation.map((f) => f.colorDetails),
    ];
    data.lipsticks = [
      ...$suggestions.makeup.suggestedLipstick.coral,
      ...$suggestions.makeup.suggestedLipstick.mauve,
      ...$suggestions.makeup.suggestedLipstick.red,
      ...$suggestions.makeup.suggestedLipstick.pink,
    ];

    data.concealers = data.concealers.map((concealer) => {
      if (concealer)
        return {
          itemID: concealer.concealerCode,
          name: concealer.concealerIntensity,
          price: 32,
          description: "A concealer",
          img: concealer.img,
        };
    });
    data.foundations = data.foundations.map((foundation) => {
      if (foundation)
        return {
          itemID: foundation.shadeCode,
          name: foundation.shadeName,
          price: 48,
          description: "A foundation",
          img: foundation.img || "https://via.placeholder.com/150",
        };
    });
    data.lipsticks = data.lipsticks.map((lipstick) => {
      if (lipstick)
        return {
          itemID: lipstick.lipstickCode,
          name: lipstick.lipstickName,
          price: 32,
          description: "A lipstick",
          type: lipstick.lipstickType,
          img: lipstick.img || "https://via.placeholder.com/150",
        };
    });

    //remove undefined
    data.concealers = data.concealers.filter((concealer) => {
      if (concealer) return concealer;
    });
    data.foundations = data.foundations.filter((foundation) => {
      if (foundation) return foundation;
    });
    data.lipsticks = data.lipsticks.filter((lipstick) => {
      if (lipstick) return lipstick;
    });

    // remove duplicates
    data.concealers = data.concealers.filter(
      (concealer, index, self) =>
        index === self.findIndex((t) => t.itemID === concealer.itemID)
    );
    data.foundations = data.foundations.filter(
      (foundation, index, self) =>
        index === self.findIndex((t) => t.itemID === foundation.itemID)
    );
    data.lipsticks = data.lipsticks.filter(
      (lipstick, index, self) =>
        index === self.findIndex((t) => t.itemID === lipstick.itemID)
    );

    console.log(data);

    await playDialogue(
      "You can add the items to your cart, say 'hi' or 'hello' and the product name"
    );
    ctrl.DEBUG = true;
    ctrl.addCommand("hello", () => {
      ctrl.stop();
      startRecording();
      setTimeout(() => {
        ctrl.start();
        stopRecording();
      }, 5000);
    });
    ctrl.addCommand("hi", () => {
      ctrl.stop();
      startRecording();
      setTimeout(() => {
        stopRecording();
        ctrl.start();
      }, 5000);
    });
    ctrl.addCommand("checkout", async () => {
      await playDialogue("Nice choice, taking you to the checkout page");
      ctrl.stop();
      push("/cart");
    });
    ctrl.addCommand("next", async () => {
      await playDialogue("Nice choice, taking you to the checkout page");
      ctrl.stop();

      push("/cart");
    });
    ctrl.addCommand("red", async () => {
      let ld = $suggestions.makeup.suggestedLipstick.red.map(
        (l) => l.lipstickCode + ", " + l.lipstickName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.addCommand("pink", async () => {
      let ld = $suggestions.makeup.suggestedLipstick.pink.map(
        (l) => l.lipstickCode + ", " + l.lipstickName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.addCommand("mauve", async () => {
      let ld = $suggestions.makeup.suggestedLipstick.mauve.map(
        (l) => l.lipstickCode + ", " + l.lipstickName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.addCommand("coral", async () => {
      let ld = $suggestions.makeup.suggestedLipstick.coral.map(
        (l) => l.lipstickCode + ", " + l.lipstickName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.addCommand("nude", async () => {
      let ld = $suggestions.makeup.suggestedLipstick.nude.map(
        (l) => l.lipstickCode + ", " + l.lipstickName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.addCommand("foundation", async () => {
      let ld = $suggestions.makeup.suggestedFoundation.map(
        (l) => l.shadeCode + ", " + l.shadeName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.addCommand("dark concealer", async () => {
      let ld = $suggestions.makeup.suggestedConcealer.darkColor.map(
        (l) => l.concealerCode + ", " + l.concealerName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.addCommand("light concealer", async () => {
      let ld = $suggestions.makeup.suggestedConcealer.lightColor.map(
        (l) => l.concealerCode + ", " + l.concealerName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.addCommand("skin concealer", async () => {
      let ld = $suggestions.makeup.suggestedConcealer.lightColor.map(
        (l) => l.concealerCode + ", " + l.concealerName
      );
      ctrl.stop();
      for (let l of ld) {
        await playDialogue(l);
      }
      ctrl.start();
    });
    ctrl.start();
  });

  function checkInventory(usersaid) {
    usersaid = wordsToNumbers(usersaid.toLowerCase());
    console.log("bsdk", usersaid);
    for (let key of Object.keys(data)) {
      let items = data[key];
      for (let item of items) {
        if (!item) continue;
        const regex = /[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g;
        let itemname = item.name.toLowerCase().replace(regex, "");
        let itemnameparts = itemname.split(" ");
        let everywordfound = itemnameparts.every((part) =>
          usersaid.includes(part)
        );
        if (everywordfound) {
          return item.itemID;
        }
      }
    }
    return "";
  }
  $: {
    if ($usersaid) {
      if ($usersaid.includes("add")) {
        addToCart(checkInventory($usersaid));
      }
      if ($usersaid.includes("remove")) {
        removeFromCart(checkInventory($usersaid));
      }
    }
  }

  async function addToCart(itemID, touchCTRL = true) {
    //find the item in the data
    console.log("itemID", itemID);
    if (!itemID) {
      ctrl.stop();
      await playDialogue("Sorry, I didn't get that");
      ctrl.start();
      return;
    }
    let item;
    for (let key of Object.keys(data)) {
      item = data[key].find((item) => {
        if (item) return item.itemID === itemID;
      });
      if (item) {
        break;
      }
    }
    if (item) {
      $cart = [...$cart, item];
      if (touchCTRL) ctrl.stop();
      await playDialogue("Added" + item.name + " to cart");
      if (touchCTRL) ctrl.start();
    }
    console.log($cart);
  }
  async function removeFromCart(itemID, touchCTRL) {
    //find the item in the data
    if (!itemID) {
      ctrl.stop();
      await playDialogue("Sorry, I didn't get that");
      ctrl.start();
      return;
    }
    let itemname = "item";
    for (let key of Object.keys(data)) {
      let item = data[key].find((item) => {
        if (item) return item.itemID === itemID;
      });
      if (item) {
        itemname = item.name;
        break;
      }
    }
    $cart = $cart.filter((item) => item.itemID !== itemID);
    if (touchCTRL) ctrl.stop();
    await playDialogue("Removed" + itemname + " from cart");
    if (touchCTRL) ctrl.start();
    console.log($cart);
  }
</script>

<div>
  <div class="flex justify-between px-96 items-center">
    <div class="newfont text-3xl ">Choose items you want to add to cart</div>
  </div>
  <div class="flex flex-col px-96">
    <div class="divider text-xl">Foundations</div>
    <div class="flex overflow-auto gap-3">
      {#each data.foundations as foundation}
        <button
          on:click={() => {
            if ($cart.find((item) => foundation.itemID == item.itemID))
              removeFromCart(foundation.itemID, false);
            else addToCart(foundation.itemID, false);
          }}
          class="flex flex-col {$cart.find(
            (item) => foundation.itemID == item.itemID
          )
            ? 'border p-2 rounded-lg border-blue-800'
            : ''} "
        >
          <img src={foundation.img} class="w-52" alt={foundation.name} />
          <div class="text-xl newfont mt-5">
            {foundation.itemID + ", " + foundation.name}
          </div>
          <div>${foundation.price}</div>
          <div>{foundation.description}</div>
        </button>
      {/each}
    </div>
    <div class="divider text-xl  my-10">Concealer</div>
    <div class="grid grid-cols-4 overflow-auto gap-6 ">
      {#each data.concealers as concealer}
        {#if concealer}
          <button
            on:click={() => {
              if ($cart.find((item) => concealer.itemID == item.itemID))
                removeFromCart(concealer.itemID, false);
              else addToCart(concealer.itemID, false);
            }}
            class="flex flex-col {$cart.find(
              (item) => concealer.itemID == item.itemID
            )
              ? 'border p-2 rounded-lg border-blue-800'
              : ''} "
          >
            <img src={concealer.img} class="w-full" alt={concealer.name} />
            <div class="text-2xl font-bold mt-5">
              {concealer.itemID + ", " + concealer.name}
            </div>
            <div>${concealer.price}</div>
            <div>{concealer.description}</div>
          </button>
        {/if}
      {/each}
    </div>
    <div class="divider text-xl  my-10">Lipstick</div>
    <div class="grid grid-cols-4 overflow-auto gap-6  mb-20">
      {#each data.lipsticks as lipstick}
        <button
          on:click={() => {
            if ($cart.find((item) => lipstick.itemID == item.itemID))
              removeFromCart(lipstick.itemID, false);
            else addToCart(lipstick.itemID, false);
          }}
          class="flex flex-col {$cart.find(
            (item) => lipstick.itemID == item.itemID
          )
            ? 'border p-2 rounded-lg border-blue-800'
            : ''} "
        >
          <img src={lipstick.img} class="w-full" alt={lipstick.name} />
          <div class="text-xl font-bold mt-5 text-left">
            {lipstick.name + "," + lipstick.type}
          </div>
          <div>${lipstick.price}</div>
          <div>{lipstick.description}</div>
        </button>
      {/each}
    </div>
  </div>
</div>
