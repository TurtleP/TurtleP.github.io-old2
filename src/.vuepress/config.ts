import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "en-US",
  title: "TurtleP.github.io",
  description: "Gamer & Turtle",

  theme,

  // Enable it with pwa
  // shouldPrefetch: false,
});
