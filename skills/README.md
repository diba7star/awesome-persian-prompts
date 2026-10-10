# Free agent skills for Claude — English, Persian, Arabic

Four free `SKILL.md` skills for Claude Code and the Claude apps. Each one answers in English, Persian (Farsi) or Arabic, matching the language you write in, and handles right-to-left text correctly. Released under **CC0**: use them, change them, ship them, no permission needed.

Every skill folder has an `examples.md` with real, unedited outputs from testing with Claude Sonnet 5.5.

| Skill | What it does | Examples |
|---|---|---|
| [rtl-article-localizer](rtl-article-localizer/SKILL.md) | Turns an English article into publication-ready Persian and Arabic: correct typography, per-language SEO title, slug, meta description and a term-decision table. | [examples](rtl-article-localizer/examples.md) |
| [excel-formula-fixer](excel-formula-fixer/SKILL.md) | Fixes and explains Excel and Google Sheets formulas, with a small test you can type in. Catches Persian and Arabic digits stored as text. | [examples](excel-formula-fixer/examples.md) |
| [trilingual-linkedin-post-writer](trilingual-linkedin-post-writer/SKILL.md) | Writes a LinkedIn post from your notes in English, Persian and Arabic, each for its own audience. No invented numbers or stories. | [examples](trilingual-linkedin-post-writer/examples.md) |
| [regex-builder-explainer](regex-builder-explainer/SKILL.md) | Builds, explains and repairs regular expressions with a test table. Handles Unicode, Persian and Arabic text where `\w` and `\d` fail. | [examples](regex-builder-explainer/examples.md) |

## Install

No tools, API keys or dependencies are needed.

**Claude Code** — copy the skill folder into `.claude/skills/` in your project, or into `~/.claude/skills/` to use it everywhere:

```bash
git clone https://github.com/diba7star/awesome-persian-prompts.git
cp -r awesome-persian-prompts/skills/excel-formula-fixer ~/.claude/skills/
```

**Claude apps** — zip one skill folder (the folder that contains `SKILL.md`) and upload it under Settings > Capabilities > Skills.

Then just ask for the task in your own words. The skill activates when your request matches its description.

<div dir="rtl">

## فارسی

چهار اسکیل رایگان برای Claude Code و اپ‌های Claude. هر اسکیل به زبانی که می‌نویسید جواب می‌دهد (فارسی، انگلیسی یا عربی) و متن راست‌به‌چپ را درست می‌نویسد: نیم‌فاصله، «ی» و «ک» فارسی و علائم نگارشی درست. مجوز **CC0** است؛ استفادهٔ شخصی و تجاری آزاد است.

- **rtl-article-localizer** — مقالهٔ انگلیسی را به فارسی و عربیِ آمادهٔ انتشار تبدیل می‌کند، همراه با عنوان سئو، اسلاگ و توضیح متا.
- **excel-formula-fixer** — فرمول اکسل و Google Sheets را درست می‌کند و قدم‌به‌قدم توضیح می‌دهد؛ مشکل عددهای تایپ‌شده با کیبورد فارسی را هم می‌گیرد.
- **trilingual-linkedin-post-writer** — از یادداشت‌های شما پست لینکدین به سه زبان می‌نویسد، بدون آمار و داستان ساختگی.
- **regex-builder-explainer** — عبارت باقاعده (Regex) می‌سازد، توضیح می‌دهد و اشکالش را می‌گیرد؛ با پشتیبانی درست از متن و رقم فارسی و عربی.

**نصب در Claude Code:** پوشهٔ اسکیل را در `.claude/skills/` پروژه یا `~/.claude/skills/` کپی کنید.
**نصب در اپ Claude:** پوشهٔ اسکیل را فشرده (zip) کنید و در Settings > Capabilities > Skills بارگذاری کنید.

در هر پوشه، فایل `examples.md` خروجی واقعی و دست‌نخوردهٔ تست را نشان می‌دهد.

## العربية

أربع مهارات مجانية لـ Claude Code وتطبيقات Claude. تجيب كل مهارة باللغة التي تكتب بها (العربية أو الفارسية أو الإنجليزية) وتكتب النص من اليمين إلى اليسار بشكل صحيح. الترخيص **CC0**: الاستخدام الشخصي والتجاري متاح دون إذن.

- **rtl-article-localizer** — تحوّل مقالًا إنجليزيًا إلى نسختين عربية وفارسية جاهزتين للنشر، مع عنوان SEO والرابط المختصر والوصف التعريفي.
- **excel-formula-fixer** — تصحّح صيغ Excel وGoogle Sheets وتشرحها خطوة بخطوة، وتكتشف الأرقام العربية المخزّنة كنص.
- **trilingual-linkedin-post-writer** — تكتب منشور LinkedIn من ملاحظاتك بثلاث لغات، دون أرقام أو قصص مختلقة.
- **regex-builder-explainer** — تبني التعابير النمطية (Regex) وتشرحها وتصلحها، مع دعم صحيح للنصوص والأرقام العربية والفارسية.

**التثبيت في Claude Code:** انسخ مجلد المهارة إلى `.claude/skills/` في مشروعك أو إلى `~/.claude/skills/`.
**التثبيت في تطبيق Claude:** اضغط مجلد المهارة في ملف zip وارفعه من Settings > Capabilities > Skills.

في كل مجلد ملف `examples.md` يعرض مخرجات حقيقية من الاختبار دون تعديل.

</div>

---

Maintained by [Debug (di9.ir)](https://di9.ir).
