# Examples

Real, unedited outputs from testing this skill with Claude Sonnet 5.5 (2026-10-10).

## Example 1

**User message**

> Why does this return #N/A? `=VLOOKUP(A2,Sheet2!A:C,3)` The IDs in Sheet2 are not sorted. I use Excel 2016.

**Agent response**

Assumptions: Excel 2016, comma separators, the ID is in column A of Sheet2 and the value you want is in column C.

**Formula**

```
=VLOOKUP(A2,Sheet2!A:C,3,FALSE)
```

**What was wrong**

Your formula has no 4th argument, so VLOOKUP defaults to approximate match (TRUE). Approximate match only works when the first column of the lookup range is sorted ascending. Since your IDs in Sheet2 are not sorted, it can't find the ID and returns `#N/A`, or even a wrong value. Adding `FALSE` forces an exact match, which doesn't need sorting.

**How it works**

1. `A2` is the ID you are looking for.
2. `Sheet2!A:C` is the table. VLOOKUP searches the first column (A) of this range.
3. `3` returns the value from the 3rd column of the range, which is column C.
4. `FALSE` means exact match only.

**Test it**

Type this into an empty Sheet2:

| | A | B | C |
|---|---|---|---|
| 1 | 30 | Sara | Paris |
| 2 | 10 | Ali | Rome |
| 3 | 20 | Omid | Oslo |

In Sheet1, type `10` in A2 and the formula in B2. You should see `Rome`. Change A2 to `20` and you should see `Oslo`. Change A2 to `99` and you should see `#N/A`, which is correct because 99 does not exist.

**Notes**

- If you still get `#N/A` after the fix, the ID really isn't being matched. The usual reasons are an extra space in one of the cells, or an ID stored as text in one sheet and as a number in the other (a small green triangle in the cell is the clue).
- If you want a blank cell instead of `#N/A` for IDs that are genuinely missing, wrap it: `=IFERROR(VLOOKUP(A2,Sheet2!A:C,3,FALSE),"")`. Only do this if you expect misses, because it also hides real problems.
- If there are duplicate IDs in Sheet2, VLOOKUP returns the first one it finds.
- XLOOKUP is not available in Excel 2016, so VLOOKUP (or INDEX/MATCH) is the right choice for you.

---

## Example 2

**User message**

> این فرمول جمع را صفر نشان می‌دهد: `=SUM(B2:B20)` عددها را با کیبورد فارسی تایپ کرده‌ام، مثل ۱۲۵۰۰. چطور درستش کنم؟

**Agent response**

فرض کرده‌ام از اکسل استفاده می‌کنید، عددها در B2:B20 هستند و جداکننده آرگومان‌ها ویرگول است. اگر در سیستم شما نقطه‌ویرگول است، به‌جای هر `,` یک `;` بگذارید.

## فرمول

فرمول `=SUM(B2:B20)` خودش درست است و نیازی به تغییر ندارد. مشکل در خود داده‌هاست. این فرمول را در یک ستون کمکی (مثلاً C2) بنویسید و تا C20 به پایین بکشید:

```
=IF(B2="","",VALUE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(B2,"۰","0"),"۱","1"),"۲","2"),"۳","3"),"۴","4"),"۵","5"),"۶","6"),"۷","7"),"۸","8"),"۹","9")))
```

بعد جمع را از ستون کمکی بگیرید:

```
=SUM(C2:C20)
```

## مشکل چه بود

اکسل رقم‌های فارسی (۱۲۵۰۰) را عدد نمی‌داند و آن‌ها را متن حساب می‌کند، برای همین SUM آن‌ها را نادیده می‌گیرد و صفر می‌دهد. فرمول بالا هر رقم فارسی را به رقم انگلیسی تبدیل می‌کند تا اکسل آن را عدد بشناسد.

## چطور کار می‌کند

1. `SUBSTITUTE(B2,"۰","0")` رقم فارسی ۰ را به 0 تبدیل می‌کند.
2. نُه SUBSTITUTE دیگر به همین ترتیب، یکی‌یکی، رقم‌های ۱ تا ۹ را عوض می‌کنند و هر کدام روی خروجی قبلی کار می‌کند.
3. `VALUE(...)` متن حاصل (مثلاً "12500") را به عدد واقعی تبدیل می‌کند.
4. `IF(B2="","",...)` اگر خانه خالی باشد، به‌جای خطای `#VALUE!` خالی می‌گذارد.
5. `SUM(C2:C20)` عددهای واقعی ستون کمکی را جمع می‌زند.

## امتحانش کنید

در یک برگه خالی، با کیبورد فارسی بنویسید:

- B2: ۱۲۵۰۰
- B3: ۳۰۰۰
- B4: ۴۵۰۰

حالا `=SUM(B2:B4)` را جایی بنویسید. نتیجه 0 است، که همان مشکل شماست. فرمول تبدیل را در C2 بنویسید و تا C4 بکشید. باید 12500، 3000 و 4500 را ببینید. بعد `=SUM(C2:C4)` باید 20000 بدهد.

## نکته‌ها

- راه سریع و دائمی: اگر نمی‌خواهید ستون کمکی داشته باشید، ستون B را انتخاب کنید و با Ctrl+H هر رقم فارسی را با رقم انگلیسی جایگزین کنید (۱۰ بار، برای هر رقم یک بار). برای ورودی‌های بعدی هم بهتر است موقع تایپ عدد، کیبورد را روی انگلیسی بگذارید.
- اگر عددها جداکننده هزارگان دارند (مثلاً ۱۲٬۵۰۰)، باید یک SUBSTITUTE دیگر اضافه کنید که `"٬"` را با `""` عوض کند. در غیر این صورت VALUE خطا می‌دهد.
- اگر بعضی خانه‌ها رقم عربی (٠١٢٣٤٥٦٧٨٩) دارند، این فرمول آن‌ها را تبدیل نمی‌کند، چون کدشان با رقم فارسی فرق دارد. باید ده جایگزینی جدا برای آن‌ها بنویسید.
- خانه‌هایی که علاوه بر عدد، حرف یا واحد دارند (مثل «۱۲۵۰۰ تومان») خطای `#VALUE!` می‌دهند.
- این فرمول در همه نسخه‌های اکسل کار می‌کند و به نسخه 365 نیاز ندارد. من فایل شما را نمی‌بینم و فرمول را اجرا نکرده‌ام. با مثال بالا خودتان آن را امتحان کنید.
