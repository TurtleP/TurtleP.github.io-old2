import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
    site: "https://TurtleP.github.io",
    integrations: [tailwind()],
    vite: {
        plugins: [tsconfigPaths()],
    }
});
