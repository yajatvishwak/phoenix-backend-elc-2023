// @ts-nocheck
import Home from "./pages/Home.svelte";
import Recorder from "./pages/Recorder.svelte";
import ProductDisplay from "./pages/ProductDisplay.svelte";
import Preference from "./pages/Preference.svelte";
import Cart from "./pages/Cart.svelte";
import Preview from "./pages/Preview.svelte";
import Share from "./pages/Share.svelte";
import Thankyou from "./pages/Thankyou.svelte";

const routes = {
  "/preference": Preference,
  "/cart": Cart,
  "/products": ProductDisplay,
  "/preview": Preview,
  "/shared/:id": Share,
  "/thankyou": Thankyou,
  "*": Recorder,
};
export default routes;
