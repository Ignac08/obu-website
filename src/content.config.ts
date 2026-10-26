import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const pages = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/pages" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    h1: z.string().default(""),
    lead: z.string().default(""),
    template: z.string(),
    service: z.string().default(""),
    location: z.string().default(""),
    town: z.string().default(""),
    image: z.string().optional(),
    noindex: z.boolean().default(false),
  }),
});

const blog = defineCollection({
  loader: glob({ pattern: "*.md", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    author: z.string().default("Obedience Unleashed"),
    category: z.enum(["puppy", "training", "care", "local"]),
    also: z.string().default(""),
    image: z.string(),
    summary: z.string(),
    featured: z.boolean().default(false),
  }),
});

export const collections = { pages, blog };
