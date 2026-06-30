import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const getAttempts = query({
  args: { ipAddress: v.string() },
  handler: async (ctx, args) => {
    const oneHourAgo = Date.now() - 3600000;
    const attempts = await ctx.db
      .query("loginAttempts")
      .filter((q) => q.eq(q.field("ipAddress"), args.ipAddress))
      .collect();
    
    // Filter attempts in the last 1 hour locally (convex filters are best supplemented)
    const recentAttempts = attempts.filter(a => a.attemptTime >= oneHourAgo);
    
    // Sort in descending order
    recentAttempts.sort((a, b) => b.attemptTime - a.attemptTime);
    return recentAttempts;
  },
});

export const recordAttempt = mutation({
  args: { ipAddress: v.string() },
  handler: async (ctx, args) => {
    await ctx.db.insert("loginAttempts", {
      ipAddress: args.ipAddress,
      attemptTime: Date.now(),
    });
  },
});

export const clearAttempts = mutation({
  args: { ipAddress: v.string() },
  handler: async (ctx, args) => {
    const attempts = await ctx.db
      .query("loginAttempts")
      .filter((q) => q.eq(q.field("ipAddress"), args.ipAddress))
      .collect();
    for (const attempt of attempts) {
      await ctx.db.delete(attempt._id);
    }
  },
});

export const cleanupOldAttempts = mutation({
  args: {},
  handler: async (ctx) => {
    const oneDayAgo = Date.now() - 24 * 3600000;
    const oldAttempts = await ctx.db
      .query("loginAttempts")
      .collect();
    const toDelete = oldAttempts.filter(a => a.attemptTime < oneDayAgo);
    for (const attempt of toDelete) {
      await ctx.db.delete(attempt._id);
    }
  },
});
