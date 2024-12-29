import rss from '@astrojs/rss';
import { config } from "../config";
const { title, subtitle } = config;

import { getCollection } from "astro:content";

export async function GET(context) {
  const blog = (await getCollection('blog')).sort((a, b) =>
    new Date(b.data.date) - new Date(a.data.date)
  );

  return rss({
    title: title,
    description: subtitle,
    site: context.site,
    items: blog.map((post) => ({
      title: post.data.title,
      description: post.data.excerpt,
      url: post.data.url,
      date: post.data.date,
      link: `/blog/${post.id}`,
    })),
    customData: `<language>en-us</language>`,
  });
}
