# Examples

Real, unedited outputs from testing this skill with Claude Sonnet 5.5 (2026-10-10).

## Example 1

**User message**

> Write a LinkedIn post in all three languages. Notes: we moved our blog from a custom Laravel app to WordPress in 3 weeks. 4,200 pages migrated, no URL changed. The old system needed a developer for every new page type, now editors publish alone. Speaker: me, a small tech publisher. Goal: comments.

**Agent response**

### English

We moved our blog from a custom Laravel app to WordPress in 3 weeks. 4,200 pages migrated, and no URL changed.

With the old system, every new page type needed a developer. Now our editors publish on their own.

The lesson for us: judge a CMS by what editors can do alone, not by how it was built.

Which page type on your site still can't be published without a developer?

#WordPress #CMSMigration #ContentOps #Laravel

Characters: 420
Alternative hooks:
1. Our editors used to need a developer for every new page type. Now they publish alone.
2. We kept all 4,200 URLs and replaced the whole system underneath them in 3 weeks.

### فارسی

وبلاگ‌مان را در ۳ هفته از یک برنامهٔ اختصاصی Laravel به WordPress منتقل کردیم. ۴٬۲۰۰ صفحه جابه‌جا شد و نشانی (URL) هیچ صفحه‌ای تغییر نکرد.

در سیستم قبلی، برای هر نوع صفحهٔ جدید به یک توسعه‌دهنده نیاز داشتیم. حالا ویراستارها خودشان منتشر می‌کنند.

درس ما: سیستم مدیریت محتوا را با کارهایی بسنجید که ویراستارها خودشان می‌توانند انجام دهند.

کدام نوع صفحه در سایت شما هنوز بدون توسعه‌دهنده منتشر نمی‌شود؟

#وردپرس #مهاجرت_سایت #مدیریت_محتوا #لاراول

Characters: 436
Alternative hooks:
1. ویراستارهای ما برای هر نوع صفحهٔ جدید به توسعه‌دهنده نیاز داشتند. حالا خودشان منتشر می‌کنند.
2. ۴٬۲۰۰ صفحه را در ۳ هفته منتقل کردیم و نشانی هیچ‌کدام عوض نشد.

### العربية

نقلنا مدونتنا من تطبيق Laravel مخصص إلى WordPress في 3 أسابيع. انتقلت 4,200 صفحة دون أن يتغير أي رابط.

في النظام القديم، كان كل نوع جديد من الصفحات يحتاج إلى مطور. أما الآن فالمحررون ينشرون بأنفسهم.

ما تعلمناه: احكموا على أي نظام لإدارة المحتوى بما يستطيع المحررون فعله وحدهم.

أي نوع صفحة في موقعكم لا يمكن نشره حتى الآن دون مطور؟

#ووردبريس #ترحيل_المواقع #إدارة_المحتوى #لارافيل

Characters: 381
Alternative hooks:
1. كان محررونا يحتاجون إلى مطور لكل نوع جديد من الصفحات. اليوم ينشرون بأنفسهم.
2. أبقينا روابط 4,200 صفحة كما هي، وغيرنا النظام كله في 3 أسابيع.

**Notes**

- Defaults used: audience is professionals in web publishing and content teams, tone is direct and warm with no hype, length is as short as the material allows. You gave the speaker (you, first person), the goal (comments) and the languages (all three), so those are not defaults.
- One point only: editors now publish without a developer. The 3 weeks, the 4,200 pages and the unchanged URLs are supporting facts. Nothing else was dropped, except that "small tech publisher" is not stated in the posts. Add it to the second paragraph if you want the audience to know who is speaking.
- The Persian and Arabic versions are written for their own readers, not translated line by line. Persian uses Persian digits and Arabic uses Western digits.
- No placeholders are needed, because every number comes from your notes. You gave no link, so there is no suggested first comment.
- Character counts include line breaks and hashtags.

---

## Example 2

**User message**

> Arabic only, company page voice, short. Announcement: our free glossary of 583 tech terms is now live in English, Persian and Arabic. Link: https://example.com/glossary

**Agent response**

### العربية

أصبح قاموسنا المجاني، بما فيه من 583 مصطلحاً تقنياً، متاحاً الآن بالعربية والفارسية والإنجليزية.

يمكنكم قراءة كل مصطلح بأي من اللغات الثلاث. الرابط في أول تعليق.

اللغة المشتركة بين الفرق تبدأ من مصطلحات متفق عليها.

ما المصطلح التقني الذي تجدون صعوبة في شرحه بالعربية؟

#مصطلحات_تقنية #قاموس_تقني #تعريب #التقنية

Characters: 316
Alternative hooks:
1. 583 مصطلحاً تقنياً في قاموس مجاني واحد، بثلاث لغات: العربية والفارسية والإنجليزية.
2. قاموس تقني مجاني بثلاث لغات صار متاحاً الآن، وفيه 583 مصطلحاً.

**Notes**
- Defaults used: audience = professionals in the tech field; goal = comments; tone = direct and warm, no hype. Voice = company page (plural "we/our"), as you asked. Length is deliberately below the usual 600 to 1,100 characters because you asked for short.
- Dropped: nothing. The material had one point.
- Placeholders: none needed. Every number and fact comes from your announcement.
- Suggested first comment (the link works better there than in the post): «القاموس المجاني بثلاث لغات: https://example.com/glossary»
