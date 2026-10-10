---
name: rtl-article-localizer
description: Use when the user wants an English article, blog post or documentation page localized into Persian (Farsi) and/or Arabic with correct right-to-left typography and per-language SEO metadata.
---

# RTL Article Localizer (Persian and Arabic)

Localize an English article into Persian, Arabic, or both. The goal is a text a native editor would publish with only light review: natural phrasing, correct typography, and search metadata written for that language rather than translated from English.

## Inputs

Required: the English source text.

Optional, use if given, otherwise apply the default and say so in the notes:
- Target languages. Default: both Persian and Arabic.
- Audience or region. Default: general readers; Arabic in Modern Standard Arabic.
- Tone. Default: match the source.
- Focus keyword in English. Default: infer it from the title and first paragraph.
- Brand glossary: terms that must be kept or translated in a fixed way.

If the source is longer than about 1,500 words, localize it section by section in the same order and do not summarize or drop content.

## Workflow

1. Read the whole source first. Identify the focus keyword, the audience, and every term that needs a decision: product names, technical terms, acronyms, idioms, culture-specific examples.
2. Decide each term once and use that decision everywhere. Record it in the term table.
3. Write each target version from meaning, not word order. Break up long English sentences. Replace idioms with an equivalent a native speaker would actually use; if there is none, state the plain meaning.
4. Apply the typography rules for that language (below).
5. Write the metadata for that language.
6. Run the self-check, fix what fails, then output.

## What never changes

- Code blocks, inline code, commands, file paths, URLs, email addresses: copy exactly, left-to-right.
- Brand and product names stay in Latin script (Google Search Console, WordPress, GitHub) unless the brand glossary says otherwise.
- Facts, numbers, prices, units, dates and quotations keep their value. Do not convert currencies or calendars. Write Gregorian month names in the target language.
- Markdown structure: same heading levels, lists, tables and link targets. Translate link text, keep the link URL.
- Do not add claims, examples or sections that are not in the source. Do not remove any.

## Persian rules

- Letters: use Persian ی and ک, never Arabic ي and ك. No Arabic ة in native Persian words.
- Half-space (zero-width non-joiner, U+200C) instead of a full space or a joined form in: می‌ and نمی‌ verb prefixes (می‌شود), plural ها (کتاب‌ها), comparative تر and ترین (بزرگ‌تر), ای after silent ه (خانه‌ای), and compound words such as نرم‌افزار and به‌روزرسانی.
- Punctuation: ، ؛ ؟ and quotation marks « ». No space before punctuation, one space after.
- Digits: Persian digits ۰ to ۹ in running text. Keep Latin digits inside code, URLs, version numbers and model names (Windows 11, GPT-4).
- Percent as ۲۰ درصد or ۲۰٪. Thousands separator ٬ and decimal ٫ when digits are Persian.
- Prefer the established Persian term when one is in common use (نرم‌افزار، رایانش ابری). Keep the English term when readers actually search for it that way (API، SEO as سئو). On first use of a less familiar term, give the Persian term followed by the English in parentheses.
- Register: clear standard written Persian. Avoid heavy Arabic-origin formal words when a simple Persian word exists. No spoken forms unless the source is conversational.

## Arabic rules

- Modern Standard Arabic unless a region is requested. No dialect words.
- Letters: Arabic ي and ك. Never use the Persian letters ی ک گ چ پ ژ. Write ة and ى correctly, and write hamza forms (أ إ آ ؤ ئ) rather than a bare alef.
- Punctuation: ، ؛ ؟ with quotation marks « » or " ". No space before punctuation.
- Digits: Western digits 0 to 9 by default, because they are standard in Arabic tech writing and across the Maghreb. Switch to ٠ to ٩ only on request, and then use them consistently.
- No tashkeel except where a word would be misread without it.
- Technical terms: use the widely adopted Arabic term (الذكاء الاصطناعي، محرك البحث). For terms with no settled Arabic form, give an Arabic rendering followed by the English in parentheses on first use.
- Arabic sentences may start with the verb. Do not copy English subject-first order where it reads as translated.

## Mixed-direction text

- Do not start a heading or a list item with a Latin word when the sentence can be reordered, because it breaks alignment in many editors.
- Keep a Latin phrase together; do not split a product name across RTL words.
- Parentheses and slashes around Latin terms: place them so the pair wraps the Latin term only.
- Never insert invisible direction marks other than the Persian half-space.

## Metadata per language

- Focus keyword: the phrase people in that language actually search for the topic. It is often not the literal translation. If you are not sure which of two forms is more common, pick one, list the other as an alternative, and flag it.
- SEO title: 60 characters or fewer, keyword near the start.
- Meta description: 120 to 155 characters, one or two full sentences, includes the keyword once.
- Slug: lowercase Latin letters and hyphens, taken from the English keyword, so the URL stays short and shareable.

## Output format

For each requested language, in this order:

```
## Persian (fa)  |  ## Arabic (ar)

**SEO title:** ...
**Slug:** ...
**Meta description:** ...
**Focus keyword:** ... (alternative: ...)

### Article
(full localized article in Markdown)

### Term decisions
| English | Rendered as | Why |

### Notes for the editor
- Defaults applied
- Anything uncertain, with the reason
```

Keep the notes short and specific. If nothing is uncertain, say "No open issues".

## Self-check before output

- Every heading, paragraph, list item, table row and link of the source is present.
- No Arabic ي or ك in the Persian text; no Persian ی ک گ چ پ ژ in the Arabic text.
- Persian verb prefixes and plurals use the half-space.
- Digits follow the rule for that language, and code, URLs and version numbers are untouched.
- Each term is rendered the same way everywhere and matches the term table.
- Title and meta description are within their limits. Count them.

## Limits to state honestly

- You cannot see search volumes. Keyword choices come from language knowledge, not live data; say so when you flag an alternative.
- Legal, medical and financial texts need review by a qualified native professional. Add that line to the notes for such sources.
