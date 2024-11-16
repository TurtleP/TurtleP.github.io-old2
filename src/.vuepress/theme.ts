import { hopeTheme } from "vuepress-theme-hope";
import navbar from "./navbar.js";
import sidebar from "./sidebar.js";

export default hopeTheme({
  hostname: "https://TurtleP.github.io",

  iconAssets: "fontawesome-with-brands",

  logo: "/logo.png",
  favicon: "/logo.png",

  repo: "vuepress-theme-hope/vuepress-theme-hope",

  docsDir: "src",

  // navbar
  navbar,

  // sidebar
  sidebar,

  footer: "Serena S. Postelnek",
  copyright: "ⓒ 2024",

  displayFooter: true,
  sidebarSorter: "date-desc",

  blog: {
    description: "Gamer & Turtle",
    medias: {
      GitHub: "https://github.com/TurtleP",
    },
    articlePerPage: 5
  },

  plugins: {
    blog: true,
    photoSwipe: true,

    mdEnhance: {
      align: true,
      attrs: true,
      figure: true,
      gfm: true,
      imgLazyload: true,
      imgSize: true,
      include: true,
      mark: true,
      stylize: [
        {
          matcher: "Recommended",
          replacer: ({ tag }) => {
            if (tag === "em")
              return {
                tag: "Badge",
                attrs: { type: "tip" },
                content: "Recommended",
              };
          },
        },
      ],
      sub: true,
      sup: true,
      tabs: true,
      vPre: true,
    },

    feed: {
      rss: true
    }
  },
});
