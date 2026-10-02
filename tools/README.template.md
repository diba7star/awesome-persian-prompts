<div dir="rtl">

# پرامپت‌های کوتاه فارسی برای هوش مصنوعی 🇮🇷

**{{TOTAL}} پرامپت یک‌خطی آماده، به سه زبان فارسی، انگلیسی و عربی، در {{CATS}} دسته و {{SUBS}} زیردسته** — برای ChatGPT، Claude، Gemini، DeepSeek، Midjourney، Veo، Sora و هر ابزار دیگری.

یک خط، یک نتیجه: کپی کنید، جای خالی `[...]` را پر کنید، بچسبانید. همه‌ی پرامپت‌ها با مجوز **CC0** (مالکیت عمومی) منتشر شده‌اند؛ استفاده‌ی شخصی و تجاری بدون نیاز به اجازه آزاد است.

🔎 **نسخه‌ی قابل‌جستجو با پرکردن خودکار جاهای خالی و دکمه‌ی «باز کردن در ChatGPT»:** [di9.ir/blog/prompts/short](https://di9.ir/blog/prompts/short)

[![CC0](https://img.shields.io/badge/license-CC0-green)](LICENSE) ![prompts](https://img.shields.io/badge/prompts-{{TOTAL_EN}}-orange) ![language](https://img.shields.io/badge/lang-فارسی%20%2B%20English%20%2B%20العربية-blue)

## دسته‌ها

| دسته | English | تعداد | زیردسته‌ها |
|---|---|---|---|
{{TABLE}}

## نمونه از هر دسته

{{SAMPLES}}

## ساختار هر پرامپت

```json
{
  "slug": "iranian-wedding-portrait-cinematic",
  "category": "image",
  "sub": "portrait",
  "title": "پرتره‌ی سینمایی عروسی ایرانی",
  "fa": "پرامپت فارسی با جای خالی مثل [نام]",
  "en": "English prompt with [placeholders]",
  "summary": "یک جمله: چه خروجی‌ای می‌دهد",
  "tools": ["midjourney", "gemini"],
  "tags": ["عروسی", "پرتره"]
}
```

- `prompts/<دسته>.json` — هر دسته یک فایل
- `categories.json` — فهرست دسته‌ها و زیردسته‌ها (فارسی/انگلیسی)
- `dist/all.json` — همه‌ی پرامپت‌ها در یک فایل، برای برنامه‌ها و API
- `tools/build.py` — اعتبارسنجی و ساخت همین README

## مشارکت

پرامپت خوب دارید؟ [CONTRIBUTING.md](CONTRIBUTING.md) را بخوانید و Pull Request بفرستید؛ GitHub Actions خودکار ساختار را بررسی می‌کند. هر پرامپت تأییدشده ظرف یک روز روی [di9.ir](https://di9.ir/blog/prompts/short) هم منتشر می‌شود.

اگر به کارتان آمد، ⭐ بدهید تا فارسی‌زبان‌های بیشتری پیدایش کنند.

</div>

---

## Persian AI short prompts (English)

**{{TOTAL_EN}} ready-to-use one-line prompts in Persian (Farsi), English and Arabic** for ChatGPT, Claude, Gemini, DeepSeek, Midjourney, DALL·E, Veo, Sora, Runway and more — organized into categories and sub-categories, released under **CC0** (public domain).

Browse, fill placeholders and open them directly in ChatGPT/Claude at **[di9.ir/blog/prompts/short](https://di9.ir/blog/prompts/short)**. Use `dist/all.json` to embed the whole set in your own app. Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

Maintained by [Debug (di9.ir)](https://di9.ir).
