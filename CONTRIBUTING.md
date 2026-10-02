<div dir="rtl">

# راهنمای مشارکت

ممنون که می‌خواهید پرامپت اضافه کنید! چند قاعده‌ی ساده:

1. پرامپت را در فایل دسته‌ی درست بگذارید: `prompts/<دسته>.json` (کلید دسته‌ها و زیردسته‌ها در `categories.json`).
2. هر پرامپت باید همه‌ی فیلدها را داشته باشد: `slug`، `category`، `sub`، `title`، `fa`، `en`، `summary`، `tools`، `tags`.
3. `slug` انگلیسی، کوچک و با خط تیره (`iranian-wedding-portrait`) و در کل مجموعه یکتا باشد.
4. جاهای خالی را داخل کروشه بنویسید: `[موضوع]` در فارسی و `[topic]` در انگلیسی.
5. پرامپت باید کوتاه، دقیق و آماده‌ی استفاده باشد (نقش، خروجی و محدودیت را بگوید). فارسی روان با نیم‌فاصله‌ی درست.
6. پیش از ارسال اجرا کنید: `python tools/build.py --check`
7. با ارسال، می‌پذیرید که پرامپت شما با مجوز CC0 منتشر شود.

محتوای نامناسب، تبلیغ شخصی، یا پرامپت‌هایی که برای فریب، آسیب یا نقض حریم خصوصی طراحی شده‌اند پذیرفته نمی‌شوند.

</div>

## Contributing (English)

Add prompts to `prompts/<category>.json` with all fields (`slug, category, sub, title, fa, en, summary, tools, tags`), keep slugs unique kebab-case, use `[placeholders]`, run `python tools/build.py --check`, and open a PR. Contributions are released under CC0.
