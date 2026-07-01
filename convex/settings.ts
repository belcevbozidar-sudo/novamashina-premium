import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

const DEFAULT_SETTINGS = {
  heroSlides: [
    {
      title: "Вземи John Deere 6R 150<br>с 3,33% лихва и подаръци до<br>30.6.2026г.",
      desktopImg: "img/hero-desktop.webp",
      mobileImg: "img/hero-mobile.webp",
      badgeTitle: "ПРОЛЕТНА",
      badgeSubtitle: "КАМПАНИЯ",
      badgeText: "-3,33% ЛИХВА",
    }
  ],
  categories: [
    { id: "tractors", name: "Трактори", count: "412 активни оферти", img: "img/cat-tractors.webp" },
    { id: "combines", name: "Комбайни", count: "126 активни оферти", img: "img/cat-combines.webp" },
    { id: "seeders", name: "Сеялки", count: "98 активни оферти", img: "img/cat-seeders.webp" },
    { id: "sprayers", name: "Пръскачки", count: "74 активни оферти", img: "img/cat-sprayers.webp" },
    { id: "trailers", name: "Ремаркета", count: "63 активни оферти", img: "img/cat-trailers.webp" },
    { id: "inventar", name: "Инвентар", count: "187 активни оферти", img: "img/cat-inventar.webp" }
  ],
  fendtPromo: {
    title: "Немско инженерство на нова цена: Вземи своя нов Fendt от ЗЛАТЕКС с вноска от 950 €!",
    subtitle: "Специални условия: лихва 3,65% и атрактивни вноски до 30.06.2026 г",
    img: "img/promo-fleet.webp"
  },
  aboutPage: {
    sec1Title: "Нова Машина е платформа на ЗЛАТЕКС, която прави избора и закупуването на земеделска техника лесно, бързо и удобно",
    sec1Desc: "Предлагаме ви лесен и удобен дигитален асистент в избора на Вашата Нова Машина. В тази динамично променяща се среда, където дистанционните услуги вече са ежедневие, ние ви даваме възможността да изберете, тествате и купите на лизинг своята мечтана нова машина изцяло дистанционно.",
    sec1Img: "img/about-1.webp",
    sec2Title: "Желаната Нова Машина е само на няколко клика разстояние",
    sec2Desc: "Платформата е интуитивна и лесна за използване, като с няколко клика задавате критериите си за мечтаната машина и веднага получавате списък с най-подходящите оферти, от които можете да избирате, както и да заявите демонстрация в стопанството. По този начин ви даваме възможност да изберете своята Нова Машина и да я вземете при най-добрите условия за лизинг.",
    sec2Img: "img/about-2.webp",
    sec3Title: "Финансиране, застраховка и регистрация — на едно място",
    sec3Desc: "Чрез ЗЛАТЕКС Лизинг получавате пълно съдействие: индивидуален лизингов план, застраховка на техниката, регистрация и доставка до стопанството. Нашите консултанти са до вас на всяка стъпка — от избора до първата бразда.",
    sec3Img: "img/budget-side.webp"
  },
  contactsPage: {
    officeTitle: "Централен офис на ЗЛАТЕКС",
    officeAddress: "гр. Стара Загора, бул. \"Патриарх Евтимий\" №52, Офис сграда ЗЛАТЕКС",
    workingHoursTitle: "Работно време",
    workingHoursDesc: "От понеделник до петък: 8:00 - 17:00 ч.",
    phoneTitle: "Телефон за връзка",
    phoneNum: "042/919 700",
    phoneDesc: "Обадете ни се или ни потърсете на картата по-долу",
    networksTitle: "Търговско-сервизни комплекси",
    networksDesc: "За удобство на нашите клиенти ЗЛАТЕКС разполага със 7 собствени търговско-сервизни комплекси на територията на цялата страна:",
    cities: ["Стара Загора", "Чирпан", "Ямбол", "Добрич", "Разград", "Плевен", "Враца"]
  }
};

export const get = query({
  args: {},
  handler: async (ctx) => {
    const doc = await ctx.db.query("settings").first();
    if (doc) {
      return doc;
    }
    // Return default fallback settings
    return { ...DEFAULT_SETTINGS, _id: "default" };
  },
});

export const update = mutation({
  args: {
    heroSlides: v.array(v.object({
      title: v.string(),
      desktopImg: v.string(),
      mobileImg: v.string(),
      badgeTitle: v.string(),
      badgeSubtitle: v.string(),
      badgeText: v.string(),
    })),
    categories: v.array(v.object({
      id: v.string(),
      name: v.string(),
      count: v.string(),
      img: v.string(),
    })),
    fendtPromo: v.object({
      title: v.string(),
      subtitle: v.string(),
      img: v.string(),
    }),
    aboutPage: v.object({
      sec1Title: v.string(),
      sec1Desc: v.string(),
      sec1Img: v.string(),
      sec2Title: v.string(),
      sec2Desc: v.string(),
      sec2Img: v.string(),
      sec3Title: v.string(),
      sec3Desc: v.string(),
      sec3Img: v.string(),
    }),
    contactsPage: v.object({
      officeTitle: v.string(),
      officeAddress: v.string(),
      workingHoursTitle: v.string(),
      workingHoursDesc: v.string(),
      phoneTitle: v.string(),
      phoneNum: v.string(),
      phoneDesc: v.string(),
      networksTitle: v.string(),
      networksDesc: v.string(),
      cities: v.array(v.string()),
    })
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db.query("settings").first();
    if (existing) {
      await ctx.db.replace(existing._id, args);
      return existing._id;
    } else {
      return await ctx.db.insert("settings", args);
    }
  },
});
