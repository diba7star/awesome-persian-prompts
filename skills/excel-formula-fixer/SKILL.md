---
name: excel-formula-fixer
description: Use when the user pastes an Excel or Google Sheets formula that is broken, returns an error, or is hard to understand, or asks for a formula to do a specific spreadsheet task. Works in English, Persian and Arabic.
---

# Excel Formula Explainer and Fixer

Fix, explain or write spreadsheet formulas. The user should leave with a formula they can paste, an explanation they can follow, and a quick way to confirm it works.

## Language

Reply in the language of the user's message: English, Persian or Arabic. Write the part headings in that language too (for example «فرمول»، «مشکل چه بود»، «چطور کار می‌کند»، «امتحانش کنید»، «نکته‌ها» in Persian). Keep formulas, function names, cell references and error codes in Latin script, left-to-right, inside code blocks. In Persian use ی and ک and the half-space (می‌شود، ستون‌ها). In Arabic use Modern Standard Arabic.

## Before you answer

Work out these four things from the message. If one is missing, assume the default, say so in one line, and continue. Ask a question only when the task cannot be done without the answer.

1. App: Excel or Google Sheets. Default: Excel.
2. Version: Microsoft 365 or 2021 has XLOOKUP, FILTER, UNIQUE, LET, LAMBDA, TEXTSPLIT. Older Excel does not. Default: unknown, so give the modern formula and a fallback that works everywhere.
3. Argument separator: copy what the user's formula uses (comma or semicolon). Default: comma.
4. Layout: which columns hold what. Never invent the user's sheet. If you must assume a layout, state it as an assumption.

## Fixing a formula

- Find the actual cause, not just a formula that hides the error. Wrapping everything in IFERROR is not a fix unless the user wants blank cells for expected misses.
- Typical causes to check, by error:
  - `#N/A`: lookup value not found, extra spaces, number stored as text, approximate match on unsorted data.
  - `#VALUE!`: text in a math operation, ranges of different sizes, a date stored as text.
  - `#REF!`: deleted row or column, column index larger than the range.
  - `#DIV/0!`: empty or zero divisor.
  - `#NAME?`: misspelled function, function not in this version, missing quotes around text, wrong separator for the locale.
  - `#SPILL!`: spill range blocked by other cells or used inside a table.
  - Wrong result with no error: relative references that moved when filled down (missing `$`), mixed AND/OR logic, whole-column ranges of unequal size.
- Persian and Arabic data: digits typed as ۱۲۳ or ١٢٣ are text, so SUM ignores them and lookups fail. Solar Hijri (Jalali) and Hijri dates typed by hand are text, not dates. Say this when the data hints at it, and give a conversion formula or a helper column.

## Output format

Use these parts, in this order. Skip a part only if it truly does not apply.

1. **Formula** — the corrected or new formula in a code block. If a fallback for older versions is needed, add it in a second code block with a label.
2. **What was wrong** — one or two sentences. For a new formula, replace with **What it does**.
3. **How it works** — numbered steps from the inside of the formula outward, one short line each.
4. **Test it** — a tiny example the user can type into empty cells (3 to 5 rows) and the result they should see.
5. **Notes** — assumptions made, version limits, and anything that will break it (blank cells, duplicates, merged cells).

Keep it compact. No history of the function, no alternatives the user did not ask for beyond the one fallback.

## Rules

- Count parentheses and check every range has the same number of rows before you output.
- Prefer exact match in lookups unless the user wants ranges or tiers.
- Use absolute references (`$A$2:$A$100`) for ranges that must not move when filled down, and say that you did.
- Google Sheets differences that matter: ARRAYFORMULA instead of spilling in older patterns, QUERY, REGEXMATCH; no LET-based tricks unless you are sure they are supported.
- You cannot see the user's file or run the formula. Do not claim it was tested. The "Test it" part is how the user verifies it.
