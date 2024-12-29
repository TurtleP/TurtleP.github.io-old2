import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";
import { rssSchema } from '@astrojs/rss';

const rssFeed = defineCollection({
  schema: rssSchema,
});

const blog = defineCollection({
  loader: glob({pattern:"**/*.md", base: "src/blog"}),
  schema: z.object({
    title: z.string().nonempty("Title is required"),
    date: z.date(),
    excerpt: z.string().nonempty("Excerpt is required"),
    tags: z.array(z.string()).optional(),
  })
});

export const collections = { blog, rssFeed };
