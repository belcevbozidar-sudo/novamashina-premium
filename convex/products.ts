import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  args: {},
  handler: async (ctx) => {
    // Only return products that are not soft-deleted
    const items = await ctx.db.query("products").collect();
    return items.filter(m => !m.isDeleted);
  },
});

export const get = query({
  args: { id: v.id("products") },
  handler: async (ctx, args) => {
    return await ctx.db.get(args.id);
  },
});

export const add = mutation({
  args: {
    slug: v.string(),
    brand: v.string(),
    model: v.string(),
    title: v.string(),
    cat: v.string(),
    state: v.string(),
    img: v.string(),
    price: v.number(),
    monthly: v.number(),
    fuel: v.string(),
    hp: v.string(),
    trans: v.string(),
    loc: v.string(),
    year: v.string(),
    hours: v.union(v.string(), v.null()),
    engine: v.string(),
    offer: v.string(),
    dealer: v.string(),
    tank: v.string(),
    desc: v.string(),
    lease_ret: v.boolean(),
  },
  handler: async (ctx, args) => {
    const data = {
      ...args,
      views: 0,
      isDeleted: false,
    };
    const productId = await ctx.db.insert("products", data);
    
    // Archive snapshot (Write-only log)
    await ctx.db.insert("productArchive", {
      action: "insert",
      productId: productId,
      timestamp: new Date().toISOString(),
      data: data,
    });
    
    return productId;
  },
});

export const update = mutation({
  args: {
    id: v.id("products"),
    slug: v.string(),
    brand: v.string(),
    model: v.string(),
    title: v.string(),
    cat: v.string(),
    state: v.string(),
    img: v.string(),
    price: v.number(),
    monthly: v.number(),
    fuel: v.string(),
    hp: v.string(),
    trans: v.string(),
    loc: v.string(),
    year: v.string(),
    hours: v.union(v.string(), v.null()),
    engine: v.string(),
    offer: v.string(),
    dealer: v.string(),
    tank: v.string(),
    desc: v.string(),
    lease_ret: v.boolean(),
    views: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const { id, ...data } = args;
    const current = await ctx.db.get(id);
    if (!current) throw new Error("Product not found");
    
    await ctx.db.patch(id, data);
    
    // Archive snapshot (Write-only log)
    await ctx.db.insert("productArchive", {
      action: "update",
      productId: id,
      timestamp: new Date().toISOString(),
      data: data,
    });
  },
});

export const remove = mutation({
  args: { id: v.id("products") },
  handler: async (ctx, args) => {
    const current = await ctx.db.get(args.id);
    if (!current) throw new Error("Product not found");
    
    // Soft delete
    await ctx.db.patch(args.id, {
      isDeleted: true,
      deletedAt: new Date().toISOString(),
    });
    
    // Archive snapshot (Write-only log)
    await ctx.db.insert("productArchive", {
      action: "delete",
      productId: args.id,
      timestamp: new Date().toISOString(),
      data: current,
    });
  },
});

export const incrementViews = mutation({
  args: { id: v.id("products") },
  handler: async (ctx, args) => {
    const current = await ctx.db.get(args.id);
    if (current) {
      await ctx.db.patch(args.id, {
        views: (current.views || 0) + 1,
      });
    }
  },
});

export const hardDeleteForTest = mutation({
  args: { id: v.id("products") },
  handler: async (ctx, args) => {
    // Delete product physically (only for tests)
    await ctx.db.delete(args.id);
  },
});

export const generateUploadUrl = mutation({
  args: {},
  handler: async (ctx) => {
    return await ctx.storage.generateUploadUrl();
  },
});
