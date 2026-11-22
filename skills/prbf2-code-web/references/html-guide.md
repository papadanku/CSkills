
# HTML

## HTML Style Rules

### Document Type

Use `<!doctype html>`.

Always put your HTML in
[no-quirks mode](https://developer.mozilla.org/en-US/docs/Web/HTML/Quirks_Mode_and_Standards_Mode)
by including `<!doctype html>` at the beginning of the document.

A document without a doctype is rendered in “quirks mode”, and one with a
different doctype may be rendered in “limited-quirks mode”. These modes don’t
follow the widely-understood, widely-documented behavior for various core HTML
and CSS constructs, and are likely to cause subtle failures and
incompatibilities especially when reusing code that expects no-quirks mode.

### HTML Validity

Use valid HTML where possible.

Use valid HTML code unless that is not possible due to otherwise unattainable
performance goals regarding file size.

Use tools such as the [W3C HTML validator](https://validator.w3.org/nu/) to
test.

Using valid HTML is a measurable baseline quality attribute that contributes to
learning about technical requirements and constraints, and that ensures proper
HTML usage.

```html
<!-- Not recommended -->
<title>Test</title>
<article>This is only a test.
```

```html
<!-- Recommended -->
<!doctype html>
<meta charset="utf-8">
<title>Test</title>
<article>This is only a test.</article>
```

### Semantics

Use HTML according to its purpose.

Use elements (sometimes incorrectly called “tags”) for what they have been
created for. For example, use heading elements for headings, `p` elements for
paragraphs, `a` elements for anchors, etc.

Using HTML according to its purpose is important for accessibility, reuse, and
code efficiency reasons.

```html
<!-- Not recommended -->
<div onclick="goToRecommendations();">All recommendations</div>
```

```html
<!-- Recommended -->
<a href="recommendations/">All recommendations</a>
```

### Multimedia Fallback

Provide alternative contents for multimedia.

For multimedia, such as images, videos, animated objects via `canvas`, make sure
to offer alternative access. For images that means use of meaningful alternative
text (`alt`) and for video and audio transcripts and captions, if available.

Providing alternative contents is important for accessibility reasons: A blind
user has few cues to tell what an image is about without `@alt`, and other users
may have no way of understanding what video or audio contents are about either.

(For images whose `alt` attributes would introduce redundancy, and for images
whose purpose is purely decorative which you cannot immediately use CSS for, use
no alternative text, as in `alt=""`.)

```html
<!-- Not recommended -->
<img src="spreadsheet.png">
```

```html
<!-- Recommended -->
<img src="spreadsheet.png" alt="Spreadsheet screenshot.">
```

### Separation of Concerns

Separate structure from presentation from behavior.

Strictly keep structure (markup), presentation (styling), and behavior
(scripting) apart, and try to keep the interaction between the three to an
absolute minimum.

That is, make sure documents and templates contain only HTML and HTML that is
solely serving structural purposes. Move everything presentational into style
sheets, and everything behavioral into scripts.

In addition, keep the contact area as small as possible by linking as few style
sheets and scripts as possible from documents and templates.

Separating structure from presentation from behavior is important for
maintenance reasons. It is always more expensive to change HTML documents and
templates than it is to update style sheets and scripts.

```html
<!-- Not recommended -->
<!doctype html>
<title>HTML sucks</title>
<link rel="stylesheet" href="base.css" media="screen">
<link rel="stylesheet" href="grid.css" media="screen">
<link rel="stylesheet" href="print.css" media="print">
<h1 style="font-size: 1em;">HTML sucks</h1>
<p>I’ve read about this on a few sites but now I’m sure:
  <u>HTML is stupid!!1</u>
<center>I can’t believe there’s no way to control the styling of
  my website without doing everything all over again!</center>
```

```html
<!-- Recommended -->
<!doctype html>
<title>My first CSS-only redesign</title>
<link rel="stylesheet" href="default.css">
<h1>My first CSS-only redesign</h1>
<p>I’ve read about this on a few sites but today I’m actually
  doing it: separating concerns and avoiding anything in the HTML of
  my website that is presentational.
<p>It’s awesome!
```

### Entity References

Do not use entity references.

There is no need to use entity references like `&mdash;`, `&rdquo;`, or
`&#x263a;`, assuming the same encoding (UTF-8) is used for files and editors as
well as among teams.

The only exceptions apply to characters with special meaning in HTML (like `<`
and `&`) as well as control or “invisible” characters (like no-break spaces).

```html
<!-- Not recommended -->
The currency symbol for the Euro is &ldquo;&eur;&rdquo;.
```

```html
<!-- Recommended -->
The currency symbol for the Euro is “€”.
```

### Optional Tags

Omit optional tags (optional).

For file size optimization and scannability purposes, consider omitting optional
tags. The
[HTML5 specification](https://html.spec.whatwg.org/multipage/syntax.html#syntax-tag-omission)
defines what tags can be omitted.

(This approach may require a grace period to be established as a wider guideline
as it’s significantly different from what web developers are typically taught.
For consistency and simplicity reasons it’s best served omitting all optional
tags, not just a selection.)

```html
<!-- Not recommended -->
<!doctype html>
<html>
  <head>
    <title>Spending money, spending bytes</title>
  </head>
  <body>
    <p>Sic.</p>
  </body>
</html>
```

```html
<!-- Recommended -->
<!doctype html>
<title>Saving money, saving bytes</title>
<p>Qed.
```

### `type` Attributes

Omit `type` attributes for style sheets and scripts.

Do not use `type` attributes for style sheets (unless not using CSS) and scripts
(unless not using JavaScript, or when loading a JavaScript module with
`type="module"`).

Specifying `type` attributes in these contexts is not necessary as HTML5 implies
[`text/css`](https://html.spec.whatwg.org/multipage/obsolete.html#attr-style-type)
and
[`text/javascript`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type)
as defaults. This can be safely done even for older browsers.

```html
<!-- Not recommended -->
<link rel="stylesheet" href="https://www.google.com/css/maia.css"
    type="text/css">
```

```html
<!-- Recommended -->
<link rel="stylesheet" href="https://www.google.com/css/maia.css">
```

```html
<!-- Not recommended -->
<script src="https://www.google.com/js/gweb/analytics/autotrack.js"
    type="text/javascript"></script>
```

```html
<!-- Recommended -->
<script src="https://www.google.com/js/gweb/analytics/autotrack.js"></script>
```

[JavaScript modules](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type)
must use `type="module"` when loading via `<script>`.

```html
<!-- Recommended -->
<script src="https://example.com/js/app.js" type="module"></script>
```

### `id` Attributes

Avoid unnecessary `id` attributes.

Prefer `class` attributes for styling and `data` attributes for scripting.

Where `id` attributes are strictly required, always include a hyphen in the
value to ensure it does not match the JavaScript identifier syntax, e.g. use
`user-profile` rather than just `profile` or `userProfile`.

When an element has an `id` attribute, browsers will make that available as a
[named property on the global `window` prototype](https://html.spec.whatwg.org/multipage/window-object.html#named-access-on-the-window-object),
which may cause unexpected behavior. While `id` attribute values containing a
hyphen are still available as property names, these cannot be referenced as
global JavaScript variables.

```html
<!-- Not recommended: `window.userProfile` will resolve to reference the <div> node -->
<div id="userProfile"></div>
```

```html
<!-- Recommended: `id` attribute is required and its value includes a hyphen -->
<div aria-describedby="user-profile">
  …
  <div id="user-profile"></div>
  …
</div>
```

## HTML Formatting Rules

### General Formatting

Use a new line for every block, list, or table element, and indent every such
child element.

Independent of the styling of an element (as CSS allows elements to assume a
different role per `display` property), put every block, list, or table element
on a new line.

Also, indent them if they are child elements of a block, list, or table element.

(If you run into issues around whitespace between list items it’s acceptable to
put all `li` elements in one line. A linter is encouraged to throw a warning
instead of an error.)

```html
<blockquote>
  <p><em>Space</em>, the final frontier.</p>
</blockquote>
```

```html
<ul>
  <li>Moe
  <li>Larry
  <li>Curly
</ul>
```

```html
<table>
  <thead>
    <tr>
      <th scope="col">Income
      <th scope="col">Taxes
  <tbody>
    <tr>
      <td>$ 5.00
      <td>$ 4.50
</table>
```

### HTML Line-Wrapping

Break long lines (optional).

While there is no column limit recommendation for HTML, you may consider
wrapping long lines if it significantly improves readability.

When line-wrapping, each continuation line should be indented to distinguish
wrapped attributes from child elements. Lines should be wrapped consistently
within a project, ideally enforced by automated code formatting tools.

```html
<button
  mat-icon-button
  color="primary"
  class="menu-button"
  (click)="openMenu()"
>
  <mat-icon>menu</mat-icon>
</button>
```

```html
<button mat-icon-button color="primary" class="menu-button"
    (click)="openMenu()">
  <mat-icon>menu</mat-icon>
</button>
```

```html
<button
    mat-icon-button
    color="primary"
    class="menu-button"
    (click)="openMenu()">
  <mat-icon>menu</mat-icon>
</button>
```

```html
<button mat-icon-button
        color="primary"
        class="menu-button"
        (click)="openMenu()">
  <mat-icon>menu</mat-icon>
</button>
```

### HTML Quotation Marks

When quoting attribute values, use double quotation marks.

Use double (`""`) rather than single quotation marks (`''`) around attribute
values.

```html
<!-- Not recommended -->
<a class='maia-button maia-button-secondary'>Sign in</a>
```

```html
<!-- Recommended -->
<a class="maia-button maia-button-secondary">Sign in</a>
```
