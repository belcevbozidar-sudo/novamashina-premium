import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const getSession = query({
  args: { token: v.string() },
  handler: async (ctx, args) => {
    const session = await ctx.db
      .query("sessions")
      .filter((q) => q.eq(q.field("token"), args.token))
      .first();
    if (session && session.expiresAt > Date.now()) {
      return session;
    }
    return null;
  },
});

export const createSession = mutation({
  args: { token: v.string(), userId: v.string(), expiresAt: v.number() },
  handler: async (ctx, args) => {
    await ctx.db.insert("sessions", args);
  },
});

export const updateSessionExpiry = mutation({
  args: { token: v.string(), expiresAt: v.number() },
  handler: async (ctx, args) => {
    const session = await ctx.db
      .query("sessions")
      .filter((q) => q.eq(q.field("token"), args.token))
      .first();
    if (session) {
      await ctx.db.patch(session._id, { expiresAt: args.expiresAt });
    }
  },
});

export const deleteSession = mutation({
  args: { token: v.string() },
  handler: async (ctx, args) => {
    const session = await ctx.db
      .query("sessions")
      .filter((q) => q.eq(q.field("token"), args.token))
      .first();
    if (session) {
      await ctx.db.delete(session._id);
    }
  },
});

export const cleanupExpiredSessions = mutation({
  args: {},
  handler: async (ctx) => {
    const expired = await ctx.db
      .query("sessions")
      .collect();
    const toDelete = expired.filter(s => s.expiresAt < Date.now());
    for (const s of toDelete) {
      await ctx.db.delete(s._id);
    }
  },
});
