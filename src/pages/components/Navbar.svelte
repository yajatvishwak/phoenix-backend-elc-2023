<script>
  import { cart } from "../store/cart.store";
</script>

<div class="flex justify-between p-10 ">
  <img src="logo.webp" class="w-64" alt="" />
  <div class="flex gap-7 items-center">
    <div class="flex flex-col items-end">
      <div class="font-bold">Hi, Yajat</div>
      <div>Mock Store Website</div>
    </div>

    <img
      class="w-12 mask mask-squircle "
      src="https://api.dicebear.com/5.x/big-ears-neutral/svg?seed=Samantha"
      alt=""
    />
    <div class="px-4 py-1 border rounded-full flex gap-3 ">
      <div>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z"
          />
        </svg>
      </div>
      <div>{$cart.length}</div>
    </div>
  </div>
</div>
