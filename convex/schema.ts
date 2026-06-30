import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  products: defineTable({
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
    views: v.number(),
    dealer: v.string(),
    tank: v.string(),
    desc: v.string(),
    lease_ret: v.boolean(),
    imgs: v.optional(v.array(v.string())),
    isDeleted: v.optional(v.boolean()),
    deletedAt: v.optional(v.string()),
  }),
  
  productArchive: defineTable({
    action: v.string(),
    productId: v.string(),
    timestamp: v.string(),
    data: v.any(),
  }),
  
  users: defineTable({
    username: v.string(),
    passwordHash: v.string(),
    isDeleted: v.optional(v.boolean()),
  }),
  
  userArchive: defineTable({
    action: v.string(),
    username: v.string(),
    timestamp: v.string(),
    data: v.any(),
  }),
  
  loginAttempts: defineTable({
    ipAddress: v.string(),
    attemptTime: v.number(),
  }),
  
  sessions: defineTable({
    token: v.string(),
    userId: v.string(),
    expiresAt: v.number(),
  }),
});
