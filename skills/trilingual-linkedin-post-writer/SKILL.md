---
name: trilingual-linkedin-post-writer
description: Use when the user wants a LinkedIn post written from notes, an article, an announcement or an idea, in English, Persian, Arabic, or all three.
---

# Trilingual LinkedIn Post Writer

Turn the user's raw material into a LinkedIn post that reads as written by a person in that language. When more than one language is requested, write each version for its own audience. Do not translate sentence by sentence.

## Inputs

Required: the raw material (notes, a draft, an article summary, an announcement).

Optional. If missing, use the default and list the defaults used at the end:
- Languages: English, Persian, Arabic. Default: all three.
- Who is speaking: a person or a company page. Default: a person, first person singular.
- Audience. Default: professionals in the topic's field.
- Goal: comments, profile visits, link clicks, hiring, awareness. Default: comments.
- Tone. Default: direct and warm, no hype.
- Length. Default: as short as the material allows, usually 350 to 1,100 characters per version. Hard limit: 3,000. Never restate a point in different words to make the post longer; thin material gets a short post.

## How to write it

1. Find the one point of the post. If the material has several, pick the strongest and drop the rest. Mention what you dropped in the notes.
2. Hook: the first two lines must work alone, because LinkedIn hides the rest behind "see more". Keep the hook under 200 characters. Start with the specific fact, problem or result. Do not start with a greeting, a question that has an obvious answer, or an announcement of feelings.
3. Body: short paragraphs of one or two sentences with a blank line between them. Concrete details from the material. A short list is fine if the content is a list.
4. Close: one sentence that states the takeaway, then one real question that invites an answer from experience.
5. Hashtags: 3 to 5 on the last line, in the language of that version, specific to the topic. One broad tag at most.

## Honesty rules

- Use only facts, numbers, names and results that are in the material. Never invent a statistic, a client, a quote or a personal story. If the post needs a number the user did not give, write a placeholder in square brackets and flag it.
- No claims about results the reader will get.
- Banned openers and filler: "I'm thrilled to announce", "In today's fast-paced world", "Let that sink in", "Here's the thing", and their Persian and Arabic equivalents such as «خوشحالم اعلام کنم» and «يسعدني أن أعلن».
- No emojis unless the user asks. No bold or italic Unicode letter tricks; they break screen readers and search.

## Language rules

- English: plain words, active voice, contractions allowed.
- Persian: standard written Persian that still sounds like a person; Persian ی and ک; half-space in می‌شود، شرکت‌ها، بزرگ‌تر; punctuation ، ؛ ؟ and « »; Persian digits in text. Keep product and company names in Latin script.
- Arabic: Modern Standard Arabic that is light and readable; Arabic ي and ك, never Persian letters; punctuation ، ؛ ؟; Western digits unless asked otherwise. Keep product and company names in Latin script.
- Do not begin a line with a Latin word in the Persian and Arabic versions when you can reorder the sentence.
- Hashtags in Persian and Arabic use underscores between words (#هوش_مصنوعی، #الذكاء_الاصطناعي).

## Output format

For each language, in the order English, Persian, Arabic:

```
### English | ### فارسی | ### العربية

(the post, ready to paste, hashtags on the last line)

Characters: N
Alternative hooks:
1. ...
2. ...
```

After the last version, add **Notes**: defaults used, what you dropped, any placeholder that needs a real number, and a suggested first comment only if the user gave a link (links work better in the first comment than in the post).

Count the characters of each post before you report the number.
