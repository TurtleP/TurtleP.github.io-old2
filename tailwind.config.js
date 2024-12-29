// filepath: /d:/blog/tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{astro,html,js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        seafoam_dark: '#2dd4bf',
        seafoam: '#00b7c3',
        dark_modern: "#1f1f1f",
        dark_footer: "#181818",
        dark_contrast: "#111111"
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // Clean sans-serif font
        serif: ['Merriweather', 'serif'], // Optional serif for headings
      },
      typography: (theme) => ({
        DEFAULT: {
          css: {
            color: theme('colors.gray.700'),
            a: {
              color: theme('colors.seafoam'),
              '&:hover': {
                color: theme('colors.seafoam_dark'),
              },
            },
            h1: { color: theme('colors.gray.900') },
            h2: { color: theme('colors.gray.900') },
            h3: { color: theme('colors.gray.900') },
            h4: { color: theme('colors.gray.900') },
            code: { color: theme('colors.pink.500') },
            strong: { color: theme('colors.gray.900') }, // Ensure bold text is styled correctly
          },
        },
        dark: {
          css: {
            color: theme('colors.gray.300'),
            a: {
              color: theme('colors.seafoam'),
              '&:hover': {
                color: theme('colors.seafoam_dark'),
              },
            },
            h1: { color: theme('colors.gray.100') },
            h2: { color: theme('colors.gray.100') },
            h3: { color: theme('colors.gray.100') },
            h4: { color: theme('colors.gray.100') },
            code: { color: theme('colors.pink.400') },
            strong: { color: theme('colors.gray.100') }, // Ensure bold text is styled correctly in dark mode
          },
        },
      }),
    },
  },
  darkMode: ['class', '[data-theme="dark"]'],
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
