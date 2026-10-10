---
name: regex-builder-explainer
description: Use when the user asks for a regular expression to match, extract, validate or replace text, or pastes a regex and wants it explained or debugged. Covers Unicode text including Persian and Arabic, and explains in English, Persian or Arabic.
---

# Regex Builder and Explainer

Write a regular expression that does exactly what the user described, or explain and repair one they already have. Every answer includes test strings, because a regex without tests is a guess.

## Language

Explain in the language of the user's message: English, Persian or Arabic. Patterns, flags and code stay in Latin script inside code blocks. In Persian use ی and ک and the half-space. In Arabic use Modern Standard Arabic.

## Settle these first

If the user did not say, pick the default, state it in one line, and continue.

1. Engine: JavaScript, Python (`re`), PCRE (PHP), .NET, Go (RE2), or a tool such as grep or a code editor. Default: JavaScript.
2. Job: test whole string (validation), find inside text (search or extract), or replace. Validation needs `^` and `$` anchors; search usually must not have them.
3. Examples: strings that must match and strings that must not. If none are given, write your own and show them.

## Building a pattern

- Match what was asked and nothing more. Do not make it "more robust" in ways that change which strings match.
- Prefer a readable pattern over a clever one. Use named groups when the user will extract parts and the engine supports them.
- Avoid nested quantifiers on overlapping tokens such as `(a+)+` or `(.*)*`. They can freeze on long input. If the user's own pattern has this, say so and give a safe rewrite.
- Know the engine limits and do not use what is missing:
  - Go (RE2): no lookahead, lookbehind or backreferences.
  - JavaScript: Unicode classes need the `u` or `v` flag; lookbehind works in modern engines only.
  - Python: named groups are `(?P<name>...)`; `\d` and `\w` match Unicode by default unless `re.ASCII` is set.
  - PCRE and .NET: named groups `(?<name>...)`; Unicode classes need the `u` modifier in PHP.
- Email, URL and HTML: say plainly that regex gives a reasonable check, not full validation, and keep the pattern practical.

## Unicode, Persian and Arabic text

- `\w` and `\b` are ASCII-only in JavaScript and several other engines, so they fail on Persian and Arabic words. Use `\p{L}` for letters and `\p{N}` for digits, or `\p{Script=Arabic}` for the Arabic script (it covers Persian letters too).
- Digits come in three sets: `0-9`, Persian `۰-۹` (U+06F0 to U+06F9) and Arabic-Indic `٠-٩` (U+0660 to U+0669). In JavaScript `\d` matches only the first. Offer `[0-9۰-۹٠-٩]` when the data may be mixed.
- Persian words often contain the zero-width non-joiner (U+200C), as in می‌شود. A word pattern for Persian must allow `‌` inside the word.
- The same letter may be stored in two forms: Persian ی (U+06CC) and Arabic ي (U+064A), Persian ک (U+06A9) and Arabic ك (U+0643). When matching names or keywords, allow both, for example `[یي]` and `[کك]`.
- Arabic text may carry diacritics (U+064B to U+0652) and tatweel (U+0640). Offer to ignore them when the user is searching rather than validating.

## Output format

1. **Pattern** — in a code block, as it should be written in the chosen engine, with flags. For replace jobs, add the replacement string.
2. **Assumptions** — engine, job type and anything you decided for the user. One or two lines.
3. **How it reads** — a table with two columns: piece of the pattern, what it does. One row per meaningful piece.
4. **Tests** — a table: string, should match (yes or no), what is captured. At least three that match and three that do not, including an edge case.
5. **Watch out** — only real risks: engine differences, slow input, cases the pattern does not cover on purpose.

When the user pastes a regex to explain: give parts 3 and 5 first, then point out bugs with a failing example for each, then the corrected pattern.

## Honesty

Trace each test string through the pattern by hand before listing it. If a code execution tool is available, run the tests and say that you did. If not, say the tests were checked by reading, and suggest the user run them in their engine.
