# Examples

Real, unedited outputs from testing this skill with Claude Sonnet 5.5 (2026-10-10).

## Example 1

**User message**

> JavaScript regex to validate an Iranian mobile number: it starts with 09 or +989, then 9 more digits, and users may type Persian or English digits.

**Agent response**

**Pattern** (JavaScript)

```js
/^(?:[0۰][9۹]|\+[9۹][8۸][9۹])[0-9۰-۹]{9}$/
```

**Assumptions**

- Engine: JavaScript (as you said). Job: validating the whole string, so the pattern is anchored with `^` and `$`.
- "Persian or English digits" means `0-9` and `۰-۹`. This applies to every digit, including the leading `09` and the `98` after the plus sign. Arabic-Indic digits (`٠-٩`) are not accepted, because you did not ask for them.

**How it reads**

| Piece | What it does |
|---|---|
| `^` ... `$` | The whole input must match, with nothing before or after. |
| `(?:` ... `)` | Groups the two allowed prefixes without creating a capture group. |
| `[0۰][9۹]` | The local prefix `09`, with each digit in English or Persian form. |
| `\|` | Or, the international prefix instead. |
| `\+` | A literal plus sign. |
| `[9۹][8۸][9۹]` | `989` (country code 98, then the mobile 9), in English or Persian digits. |
| `[0-9۰-۹]{9}` | Exactly nine more digits, English or Persian. |

Example use:

```js
const re = /^(?:[0۰][9۹]|\+[9۹][8۸][9۹])[0-9۰-۹]{9}$/;
re.test("۰۹۱۲۳۴۵۶۷۸۹"); // true
```

**Tests**

Checked by reading, tracing each string through the pattern by hand. I did not run them, so please run them once in your own environment.

| String | Match? | Captured |
|---|---|---|
| `09123456789` | yes | whole string (09 + 9 digits) |
| `+989123456789` | yes | whole string (+989 + 9 digits) |
| `۰۹۱۲۳۴۵۶۷۸۹` | yes | whole string (all Persian digits) |
| `+۹۸۹۱۲۳۴۵۶۷۸۹` | yes | whole string (Persian digits after the plus) |
| `09۱۲۳۴۵۶۷۸۹` | yes | whole string (mixed English and Persian digits, allowed) |
| `0912345678` | no | only 8 digits after 09 |
| `091234567890` | no | 10 digits after 09, so `$` fails |
| `9123456789` | no | no `09` or `+989` prefix |
| `989123456789` | no | the plus sign is required for the international form |
| `00989123456789` | no | `0098` form is not allowed; the second character is `0`, not `9` |
| `08123456789` | no | the second digit must be 9 |
| `0912 345 6789` | no | spaces are not allowed |

**Watch out**

- A single number can mix English and Persian digits, as in `09۱۲3456789`. The pattern accepts it. If you store the number, convert it to English digits first: `s.replace(/[۰-۹]/g, d => d.charCodeAt(0) - 0x06F0)`.
- Spaces, dashes and the `0098` prefix are rejected on purpose. If your form should tolerate them, remove them before testing, for example with `s.replace(/[\s-]/g, "")`.
- This checks the shape only. It does not check that the digits after `09` belong to a real operator range.
- Arabic-Indic digits (`٠-٩`), which some keyboards produce, are not accepted. To allow them, add `٠-٩` to each digit class.

---

## Example 2

**User message**

> اشرح لي هذا التعبير ولماذا يتجمد مع النصوص الطويلة: `^(\w+\s?)+$` أستخدم Python.

**Agent response**

افترضتُ أن المحرك هو Python (وحدة `re`) وأن المهمة هي التحقق من النص كاملًا، لأن التعبير يبدأ بـ `^` وينتهي بـ `$`.

```
^(\w+\s?)+$
```

## كيف يُقرأ التعبير

| الجزء | ماذا يفعل |
|---|---|
| `^` | بداية النص. |
| `(` ... `)+` | مجموعة تُكرَّر مرة واحدة أو أكثر، وتحتفظ المجموعة بآخر تكرار فقط. |
| `\w+` | حرف واحد أو أكثر من حروف "الكلمة". في Python 3 يشمل `\w` الحروف والأرقام من كل اللغات (ومنها العربية والفارسية) إضافةً إلى الشرطة السفلية `_`. |
| `\s?` | فراغ واحد اختياري (مسافة أو Tab أو سطر جديد). |
| `$` | نهاية النص، أو قبل سطر جديد أخير. |

معنى التعبير المقصود: كلمات تفصل بينها مسافة واحدة. وهو يقبل أيضًا مسافة واحدة في آخر النص.

## انتبه

- **التجمّد ليس عطلًا في Python**: محرك `re` يعتمد على التراجع (backtracking) ولا يملك حماية من هذه الحالة. النص الصحيح يُقبل بسرعة، ولهذا يبدو التعبير سليمًا حتى يصل أول نص غير صالح، فيتجمّد.
- التعبير يرفض أي علامة ترقيم (فاصلة، نقطة، `،`، `؟`)، وأي نص طويل حقيقي يحتوي عادةً على شيء منها. فيفشل التعبير، وعند الفشل يبدأ التجمّد.
- يرفض الفراغين المتتاليين (`a  b`) ويقبل فراغًا واحدًا في الآخر (`a `).
- `\w` في Python لا يطابق النصف الفاصل غير المرئي (ZWNJ، U+200C)، فكلمة مثل `می‌شود` تُرفض.
- هذه القواعد لا تتغير في الحل أدناه عن قصد؛ الهدف تغيير السرعة فقط، لا ما يُقبل وما يُرفض.

## الأخطاء، ومثال يفشل لكل منها

**1. تكرار متداخل على رموز متداخلة (التراجع الكارثي).**
الجزء `\s?` اختياري، فيصبح التعبير عند غياب المسافات مثل `(\w+)+`. الكلمة `aaaa` يمكن تقسيمها إلى مجموعات بطرق كثيرة: `(aaaa)` أو `(aaa)(a)` أو `(aa)(aa)` أو `(a)(a)(a)(a)` وهكذا، أي 2 أس (n-1) طريقة لكلمة من n حرفًا. عندما يفشل التعبير في النهاية (عند `$`) يجرّب المحرك كل هذه الطرق قبل أن يعلن الفشل. وفي نص طويل تتضاعف الاحتمالات مع كل حرف إضافي.

مثال يتجمّد:

```python
import re
re.match(r'^(\w+\s?)+$', 'a' * 30 + '!')   # ينتظر وقتًا طويلًا جدًا
```

مع 30 حرفًا تبلغ المحاولات مئات الملايين على الأقل، وكل حرف إضافي يضاعف الزمن. جرّب ذلك بحذر.

**2. لا يقبل ZWNJ داخل الكلمات الفارسية.**
مثال يفشل: `می‌شود` (فيه U+200C). المطابقة تتوقف عند الحرف الفاصل لأنه ليس `\w` ولا `\s`. إن كان نصك فارسيًا فاسمح به صراحةً، كما في القسم التالي.

## التعبير المصحَّح

```python
import re
pattern = re.compile(r'^\w+(?:\s\w+)*\s?$')
pattern.match(text)
```

هذا يقبل ويرفض نفس النصوص تمامًا، لكنه خطي السرعة: الفاصل `\s` والكلمة `\w+` لا يتداخلان، فلا توجد طريقتان لتقسيم نفس النص، وعند الفشل لا يجرّب المحرك سوى مسار واحد.

- إن لم تكن تريد قبول المسافة الأخيرة، احذف `\s?` قبل `$`.
- إن كان نصك فارسيًا ويحتوي ZWNJ، استبدل `\w+` بـ `[\w‌]+`.

## الاختبارات

لا توجد مجموعات التقاط في التعبير المصحَّح، فالمطابقة كاملة هي كل ما يُلتقط.

| النص | هل يطابق؟ | ما الذي يُلتقط |
|---|---|---|
| `hello world` | نعم | النص كله |
| `hello` | نعم | النص كله |
| `مرحبا بالعالم` | نعم | النص كله |
| `hello_world 123` | نعم | النص كله (`_` والأرقام جزء من `\w`) |
| `hello ` (مسافة في الآخر) | نعم | النص كله (حالة حدّية) |
| `hello  world` (مسافتان) | لا | لا شيء |
| `hello, world` | لا | لا شيء |
| `می‌شود` (فيه ZWNJ) | لا | لا شيء |
| فراغ فقط، أو نص فارغ | لا | لا شيء |
| `a` مكررة 30 مرة ثم `!` | لا | لا شيء، والرفض فوري مع التعبير المصحَّح |

راجعتُ هذه الاختبارات بالقراءة وتتبّع كل نص خطوةً بخطوة، ولم أشغّل الكود. أنصحك بتجربتها عندك في Python:

```python
import re
p = re.compile(r'^\w+(?:\s\w+)*\s?$')
print(bool(p.match('hello world')))        # True
print(bool(p.match('hello  world')))       # False
print(bool(p.match('a' * 5000 + '!')))     # False، فوريًا
```
