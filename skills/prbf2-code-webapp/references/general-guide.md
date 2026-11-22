# Google HTML/CSS Style Guide

## Background

This document defines formatting and style rules for HTML and CSS. It aims at
improving collaboration, code quality, and enabling supporting infrastructure.
It applies to raw, working files that use HTML and CSS, including Sass and GSS
files. Tools are free to obfuscate, minify, and compile as long as the general
code quality is maintained.

## General

### General Style Rules

#### Protocol

Use HTTPS for embedded resources where possible.

Always use HTTPS (`https:`) for images and other media files, style sheets, and
scripts, unless the respective files are not available over HTTPS.

```html
<!-- Not recommended: omits the protocol -->
<script src="//ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>

<!-- Not recommended: uses HTTP -->
<script src="http://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
```

```html
<!-- Recommended -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
```

```css
/* Not recommended: omits the protocol */
@import '//fonts.googleapis.com/css?family=Open+Sans';

/* Not recommended: uses HTTP */
@import 'http://fonts.googleapis.com/css?family=Open+Sans';
```

```css
/* Recommended */
@import 'https://fonts.googleapis.com/css?family=Open+Sans';
```

### General Formatting Rules

#### Indentation

Indent by 2 spaces at a time.

Don’t use tabs or mix tabs and spaces for indentation.

```html
<ul>
  <li>Fantastic
  <li>Great
</ul>
```

```css
.example {
  color: blue;
}
```

#### Capitalization

Use only lowercase.

All code has to be lowercase: This applies to HTML element names, attributes,
attribute values (unless `text/CDATA`), CSS selectors, properties, and property
values (with the exception of strings).

```html
<!-- Not recommended -->
<A HREF="/">Home</A>
```

```html
<!-- Recommended -->
<img src="google.png" alt="Google">
```

```css
/* Not recommended */
color: #E5E5E5;
```

```css
/* Recommended */
color: #e5e5e5;
```

#### Trailing Whitespace

Remove trailing white spaces.

Trailing white spaces are unnecessary and can complicate diffs.

```html
<!-- Not recommended -->
<p>What?_
```

```html
<!-- Recommended -->
<p>Yes please.
```

### General Meta Rules

#### Encoding

Use UTF-8 (no BOM).

Make sure your editor uses UTF-8 as character encoding, without a byte order
mark.

Specify the encoding in HTML templates and documents via
`<meta charset="utf-8">`. Do not specify the encoding of style sheets as these
assume UTF-8.

(More on encodings and when and how to specify them can be found in
[Handling character encodings in HTML and CSS](https://www.w3.org/International/tutorials/tutorial-char-enc/).)

#### Comments

Explain code as needed, where possible.

Use comments to explain code: What does it cover, what purpose does it serve,
why is respective solution used or preferred?

(This item is optional as it is not deemed a realistic expectation to always
demand fully documented code. Mileage may vary heavily for HTML and CSS code and
depends on the project’s complexity.)

#### Action Items

Use `TODO` comments for code that is temporary, a short-term solution, or
good-enough but not perfect.

A `TODO` comment begins with the word `TODO` in all caps, and a parenthesized
link to a resource that contains the context, ideally a bug reference. A bug
reference is preferable because bugs are tracked and have follow-up comments.
Follow this piece of context with a colon and an explanatory string.

The purpose is to have a consistent `TODO` format that can be searched to find
out how to get more details.

```django
{# TODO(b/12345): Revisit centering. #}
<center>Test</center>
```

## Parting Words

*Be consistent.*

If you’re editing code, take a few minutes to look at the code around you and
determine its style. If they use spaces around all their arithmetic operators,
you should too. If their comments have little boxes of hash marks around them,
make your comments have little boxes of hash marks around them too.

The point of having style guidelines is to have a common vocabulary of coding so
people can concentrate on what you’re saying rather than on how you’re saying
it. We present global style rules here so people know the vocabulary, but local
style is also important. If code you add to a file looks drastically different
from the existing code around it, it throws readers out of their rhythm when
they go to read it. Avoid this.
