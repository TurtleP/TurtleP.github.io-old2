import { defineUserConfig } from "vuepress";
import theme from "./theme.js";
import { redirectPlugin } from "vuepress-plugin-redirect";

export default defineUserConfig({
  base: "/",

  lang: "en-US",
  title: "TurtleP.github.io",
  description: "Gamer & Turtle",

  theme,

  plugins: [
    redirectPlugin({
      "config": {
        "gallery/index.html": "gallery/2019.html"
      }
    })
  ]

  // Enable it with pwa
  // shouldPrefetch: false,
});
