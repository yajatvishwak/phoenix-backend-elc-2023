const config = {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {},
  },

  plugins: [require("daisyui"), require("@tailwindcss/line-clamp")],
};

module.exports = config;
