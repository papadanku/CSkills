
# BBCode Syntax Reference

Source: [BBCode - Wikipedia](https://en.wikipedia.org/wiki/BBCode)

## Overview

**BBCode** ("Bulletin Board Code") is a lightweight markup language used to format messages in many Internet forum software packages. First introduced in 1998, BBCode uses tags typically indicated by square brackets (`[` and `]`) surrounding a keyword, which are translated into HTML before being sent to the user.

## Tags

### Bold

- **HTML/CSS:** `<b>bolded text</b>` or `<span style="font-weight: bold;">bolded text</span>`
- **BBCode:** `[b]bolded text[/b]`
- **Output:** **bolded text**

### Italic

- **HTML/CSS:** `<i>italicized text</i>` or `<span style="font-style: italic;">italicized text</span>`
- **BBCode:** `[i]italicized text[/i]`
- **Output:** *italicized text*

### Underline

- **HTML/CSS:** `<u>underlined text</u>` or `<span style="text-decoration: underline;">underlined text</span>`
- **BBCode:** `[u]underlined text[/u]`
- **Output:** Underlined text

### Strikethrough

- **HTML/CSS:** `<s>strikethrough text</s>` or `<del>strikethrough text</del>` or `<span style="text-decoration: line-through;">strikethrough text</span>`
- **BBCode:** `[s]strikethrough text[/s]`
- **Output:** Strikethrough text (text rendered with a horizontal line through it)

### URL (Hyperlink)

- **HTML/CSS:**
    - `<a href="https://en.wikipedia.org">https://en.wikipedia.org</a>`
    - `<a href="https://en.wikipedia.org">English Wikipedia</a>`
- **BBCode:**
    - `[url]https://en.wikipedia.org[/url]`
    - `[url=https://en.wikipedia.org]English Wikipedia[/url]`
- **Output:** Clickable links displaying `https://en.wikipedia.org` and `English Wikipedia`.

### Image

- **HTML/CSS:** `<img src="https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png" alt="Example image">`
- **BBCode:** `[img alt="Example image" ]https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png[/img]`
- **Output:** Displays the image with `Example image` alt text.
- **Notes:** Also commonly written as `[img]url_img[/img]`.

### Emoticons / Smileys

- **HTML/CSS:** `<img src="Smileys/Face-smile.svg" alt=":-)">`
- **BBCode:** `:)` or `[:-)]`
- **Output:** `:-)` (specific image and size vary).
- **Notes:** Functions as another way to use `[img]url_img[/img]` and must be pre-configured by the forum administrator. Applies to this and other emoticons depending on the variant. Most BBCodes do not enclose emoticons in square brackets, leading to frequent accidental usage.

### Quote

- **HTML/CSS:**
    - `<blockquote><p>quoted text</p></blockquote>`
    - `<blockquote><p>quoted text</p><cite>&mdash; author</cite></blockquote>`
- **BBCode:**
    - `[quote]quoted text[/quote]`
    - `[quote="author"]quoted text[/quote]` (including optional `author`)
- **Output:** Blockquote displaying `quoted text`, or `quoted text` followed by `— author`.
- **Notes:** Usually implemented in more advanced ways.

### Code

- **HTML/CSS:** `<pre><code>computer code</code></pre>`
- **BBCode:** `[code]computer code[/code]`
- **Output:** Monospaced code block displaying `computer code`.

### Preformatted Text

- **HTML/CSS:** `<pre>monospaced text</pre>`
- **BBCode:** `[pre]monospaced text[/pre]`
- **Output:** Monospaced preformatted text displaying `monospaced text`.

### Font Size

- **HTML/CSS:** `<span style="font-size:30px">Large Text</span>` or `<span style="font-size:85%">Smaller Text</span>`
- **BBCode:**
    - `[style size="30px"]Large Text[/style]` / `[style size="85"]Smaller Text[/style]`
    - `[size="30px"]Large Text[/size]` / `[size="85"]Smaller Text[/size]`
- **Output:** Large Text / Smaller Text
- **Notes:** The unit of measurement varies with each BBCode variant and could represent pixels, points, or relative HTML sizes.

### Font Color

- **HTML/CSS:** `<span style="color:fuchsia;">Text in fuchsia</span>` or `<span style="color:#FF00FF;">Text in fuchsia</span>`
- **BBCode:**
    - `[style color="fuchsia"]Text in fuchsia[/style]`
    - `[style color=#FF00FF]Text in fuchsia[/style]`
    - `[color=#FF00FF]Text in fuchsia[/color]`
- **Output:** Text in fuchsia
- **Notes:** Both HTML color names and hexadecimal color values are generally supported, although on some boards, you must omit the `#` when selecting a hexadecimal color.

### Lists (Unordered and Ordered)

- **HTML/CSS:**

```html
<ul>
  <li>Entry A</li>
  <li>Entry B</li>
</ul>

<ol>
  <li>Entry 1</li>
  <li>Entry 2</li>
</ol>
```

- **BBCode:**

```text
[list]
  [*]Entry A
  [*]Entry B
[/list]

[list=1]
  [*]Entry 1
  [*]Entry 2
[/list]
```

- **Output:** Bulleted list (`Entry A`, `Entry B`) and numbered list (`1. Entry 1`, `2. Entry 2`).
- **Notes:**
    - Some message boards do not need the square brackets around the markers (for example, BOINC Project Forums et al.).
    - Many variants exist for `li` and `/li`, list types (unordered and ordered, with different bullets or counter formats), etc.

### Tables

- **HTML/CSS:**

```html
<table>
  <tr>
    <th>column header 1</th>
    <th>column header 2</th>
  </tr>
  <tr>
    <td>table cell 1</td>
    <td>table cell 2</td>
  </tr>
</table>
```

- **BBCode:**

```text
[table]
  [tr]
    [th]column header 1[/th]
    [th]column header 2[/th]
  [/tr]
  [tr]
    [td]table cell 1[/td]
    [td]table cell 2[/td]
  [/tr]
[/table]
```

- **Output:** A table with headers `column header 1` and `column header 2`, and data cells `table cell 1` and `table cell 2`.
- **Notes:** Some variants exist for `thead`, rules, etc.

## Implementation

- **Regex-Based Replacement:** BBCode is typically implemented by applying a series of regular expression string-replace operations upon the input.
- **Non-Hierarchical HTML Artifact:** Because regular expressions are limited in analyzing the structure of text input, any non-hierarchical BBCode input will be transformed into invalid non-hierarchical HTML without error.
- **Parsing Ambiguities:** Applying traditional parsing techniques is made difficult by ambiguities in the markup, such as in `[quote=[b]text[/b][/quote]`, where the input can either be interpreted as `"text"` quoted from someone called `[b`, or the bolded text `"text"` surrounded by `[quote=` and `[/quote]`, i.e., `[quote=text[/quote]`.

## See Also

Other lightweight markup languages:

- Wikitext
- Markdown

## References & External Links

- [BBCode - Wikipedia](https://en.wikipedia.org/wiki/BBCode)
- BBCode history (`www.bbcode.org`, retrieved 21 February 2025)
- HTML Text Formatting (W3Schools, retrieved 2021-05-01)
- BOINC Project Forums et al. (bracketless list markers)
- BBCode tags reference (`www.bbcode.org`, retrieved 12 January 2022)
- "Do NOT try parsing with regular expressions" (`kore-nordmann.de`, retrieved 2026-10-02)
- External links listed on Wikipedia: BBCode users guide; RTF/HTML to BBCode online converter
