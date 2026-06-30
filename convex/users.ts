import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const getByUsername = query({
  args: { username: v.string() },
  handler: async (ctx, args) => {
    const user = await ctx.db
      .query("users")
      .filter((q) => q.eq(q.field("username"), args.username))
      .first();
    if (user && !user.isDeleted) {
      return user;
    }
    return null;
  },
});

export const createAdmin = mutation({
  args: { username: v.string(), passwordHash: v.string() },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("users")
      .filter((q) => q.eq(q.field("username"), args.username))
      .first();
    if (existing) return existing._id;
    
    const userId = await ctx.db.insert("users", {
      username: args.username,
      passwordHash: args.passwordHash,
      isDeleted: false,
    });
    
    // Archive snapshot (Write-only log)
    await ctx.db.insert("userArchive", {
      action: "insert",
      username: args.username,
      timestamp: new Date().toISOString(),
      data: { username: args.username, passwordHash: args.passwordHash },
    });
    
    return userId;
  },
});
