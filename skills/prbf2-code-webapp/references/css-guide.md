
# CSS

## CSS Style Rules

### CSS Validity

Use valid CSS where possible.

Unless dealing with CSS validator bugs or requiring proprietary syntax, use
valid CSS code.

Use tools such as the [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
to test.

Using valid CSS is a measurable baseline quality attribute that allows to spot
CSS code that may not have any effect and can be removed, and that ensures
proper CSS usage.

### Class Naming

Use meaningful or generic class names.

Instead of presentational or cryptic names, always use class names that reflect
the purpose of the element in question, or that are otherwise generic.

Names that are specific and reflect the purpose of the element should be
preferred as these are most understandable and the least likely to change.

Generic names are simply a fallback for elements that have no particular or no
meaning different from their siblings. They are typically needed as “helpers.”

Using functional or generic names reduces the probability of unnecessary
document or template changes.

```css
/* Not recommended: meaningless */
.yee-1901 {}

/* Not recommended: presentational */
.button-green {}
.clear {}
```

```css
/* Recommended: specific */
.gallery {}
.login {}
.video {}

/* Recommended: generic */
.aux {}
.alt {}
```

### Class Name Style

Use class names that are as short as possible but as long as necessary.

Try to convey what a class is about while being as brief as possible.

Using class names this way contributes to acceptable levels of understandability
and code efficiency.

```css
/* Not recommended */
.navigation {}
.atr {}
```

```css
/* Recommended */
.nav {}
.author {}
```

### Class Name Delimiters

Separate words in class names by a hyphen.

Do not concatenate words and abbreviations in selectors by any characters
(including none at all) other than hyphens, in order to improve understanding
and scannability.

```css
/* Not recommended: does not separate the words “demo” and “image” */
.demoimage {}

/* Not recommended: uses underscore instead of hyphen */
.error_status {}
```

```css
/* Recommended */
.video-id {}
.ads-sample {}
```

### Prefixes

Prefix selectors with an application-specific prefix (optional).

In large projects as well as for code that gets embedded in other projects or on
external sites use prefixes (as namespaces) for class names. Use short, unique
identifiers followed by a dash.

Using namespaces helps preventing naming conflicts and can make maintenance
easier, for example in search and replace operations.

```css
.adw-help {} /* AdWords */
.maia-note {} /* Maia */
```

### Type Selectors

Avoid qualifying class names with type selectors.

Unless necessary (for example with helper classes), do not use element names in
conjunction with classes.

Avoiding unnecessary ancestor selectors is useful for
[performance reasons](https://www.stevesouders.com/blog/2009/06/18/simplifying-css-selectors/).

```css
/* Not recommended */
ul.example {}
div.error {}
```

```css
/* Recommended */
.example {}
.error {}
```

### ID Selectors

Avoid ID selectors.

ID attributes are expected to be unique across an entire page, which is
difficult to guarantee when a page contains many components worked on by many
different engineers. Class selectors should be preferred in all situations.

```css
/* Not recommended */
#example {}
```

```css
/* Recommended */
.example {}
```

### Shorthand Properties

Use shorthand properties where possible.

CSS offers a variety of
[shorthand](https://www.w3.org/TR/CSS21/about.html#shorthand) properties (like
`font`) that should be used whenever possible, even in cases where only one
value is explicitly set.

Using shorthand properties is useful for code efficiency and understandability.

```css
/* Not recommended */
border-top-style: none;
font-family: palatino, georgia, serif;
font-size: 100%;
line-height: 1.6;
padding-bottom: 2em;
padding-left: 1em;
padding-right: 1em;
padding-top: 0;
```

```css
/* Recommended */
border-top: 0;
font: 100%/1.6 palatino, georgia, serif;
padding: 0 1em 2em;
```

### 0 and Units

Omit unit specification after “0” values, unless required.

Do not use units after `0` values unless they are required.

```css
flex: 0px; /* This flex-basis component requires a unit. */
flex: 1 1 0px; /* Not ambiguous without the unit, but needed in IE11. */
margin: 0;
padding: 0;
```

### Leading 0s

Always include leading “0”s in values.

Put `0`s in front of values or lengths between -1 and 1.

```css
font-size: 0.8em;
```

### Hexadecimal Notation

Use 3 character hexadecimal notation where possible.

For color values that permit it, 3 character hexadecimal notation is shorter and
more succinct.

```css
/* Not recommended */
color: #eebbcc;
```

```css
/* Recommended */
color: #ebc;
```

### Important Declarations

Avoid using `!important` declarations.

These declarations break the natural cascade of CSS and make it difficult to
reason about and compose styles. Use [selector specificity] to override
properties instead.

[selector specificity]: https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity

```css
/* Not recommended */
.example {
  font-weight: bold !important;
}
```

```css
/* Recommended */
.example {
  font-weight: bold;
}
```

### Hacks

Avoid user agent detection as well as CSS “hacks”—try a different approach
first.

It’s tempting to address styling differences over user agent detection or
special CSS filters, workarounds, and hacks. Both approaches should be
considered last resort in order to achieve and maintain an efficient and
manageable code base. Put another way, giving detection and hacks a free pass
will hurt projects in the long run as projects tend to take the way of least
resistance. That is, allowing and making it easy to use detection and hacks
means using detection and hacks more frequently—and more frequently is too
frequently.

## CSS Formatting Rules

### Declaration Order

Alphabetize declarations (optional).

Sort declarations consistently within a project. In the absence of tooling to
automate and enforce a consistent sort order, consider putting declarations in
alphabetical order in order to achieve consistent code in a way that is easy to
learn, remember, and manually maintain.

Ignore vendor-specific prefixes for sorting purposes. However, multiple
vendor-specific prefixes for a certain CSS property should be kept sorted (e.g.
-moz prefix comes before -webkit).

```css
background: fuchsia;
border: 1px solid;
-moz-border-radius: 4px;
-webkit-border-radius: 4px;
border-radius: 4px;
color: black;
text-align: center;
text-indent: 2em;
```

### Block Content Indentation

Indent all block content.

Indent all [block content](https://www.w3.org/TR/CSS21/syndata.html#block), that
is rules within rules as well as declarations, so to reflect hierarchy and
improve understanding.

```css
@media screen, projection {

  html {
    background: #fff;
    color: #444;
  }

}
```

### Declaration Stops

Use a semicolon after every declaration.

End every declaration with a semicolon for consistency and extensibility
reasons.

```css
/* Not recommended */
.test {
  display: block;
  height: 100px
}
```

```css
/* Recommended */
.test {
  display: block;
  height: 100px;
}
```

### Property Name Stops

Use a space after a property name’s colon.

Always use a single space between property and value (but no space between
property and colon) for consistency reasons.

```css
/* Not recommended */
h3 {
  font-weight:bold;
}
```

```css
/* Recommended */
h3 {
  font-weight: bold;
}
```

### Declaration Block Separation

Use a space between the last selector and the declaration block.

Always use a single space between the last selector and the opening brace that
begins the
[declaration block](https://www.w3.org/TR/CSS21/syndata.html#rule-sets).

The opening brace should be on the same line as the last selector in a given
rule.

```css
/* Not recommended: missing space */
.video{
  margin-top: 1em;
}

/* Not recommended: unnecessary line break */
.video
{
  margin-top: 1em;
}
```

```css
/* Recommended */
.video {
  margin-top: 1em;
}
```

### Selector and Declaration Separation

Separate selectors and declarations by new lines.

Always start a new line for each selector and declaration.

```css
/* Not recommended */
a:focus, a:active {
  position: relative; top: 1px;
}
```

```css
/* Recommended */
h1,
h2,
h3 {
  font-weight: normal;
  line-height: 1.2;
}
```

### Rule Separation

Separate rules by new lines.

Always put a blank line (two line breaks) between rules.

```css
html {
  background: #fff;
}

body {
  margin: auto;
  width: 50%;
}
```

### CSS Quotation Marks

Use single (`''`) rather than double (`""`) quotation marks for attribute
selectors and property values.

Do not use quotation marks in URI values (`url()`).

Exception: If you do need to use the `@charset` rule, use double quotation
marks—[single quotation marks are not permitted](https://www.w3.org/TR/CSS21/syndata.html#charset).

```css
/* Not recommended */
@import url("https://www.google.com/css/maia.css");

html {
  font-family: "open sans", arial, sans-serif;
}
```

```css
/* Recommended */
@import url(https://www.google.com/css/maia.css);

html {
  font-family: 'open sans', arial, sans-serif;
}
```

## CSS Meta Rules

### Section Comments

Group sections by a section comment (optional).

If possible, group style sheet sections together by using comments. Separate
sections with new lines.

```css
/* Header */

.adw-header {}

/* Footer */

.adw-footer {}

/* Gallery */

.adw-gallery {}
```
