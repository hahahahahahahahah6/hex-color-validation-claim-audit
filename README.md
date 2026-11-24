# Hex-code claim audit

This offline static audit compares documentation claims about judging the shape of a color string with Python source evidence. It recognizes strings with a `#` followed by three or six hexadecimal digits. It does not execute the target's code.

Install a distribution with:

```sh
python3 -m pip install --no-cache-dir hex_color_validation_claim_audit-0.1.0-py3-none-any.whl
```

Run the audit with:

```sh
hex-color-validation-claim-audit audit .
python3 -m hex_color_validation_claim_audit audit . --json
```

The optional repository path defaults to the current directory. Use `--verbose` for details, `--ignore PREFIX` repeatedly to exclude paths, and `--fail-on medium` to include test-only evidence in the failure threshold. Exit status 0 indicates a pass at the selected threshold, 2 indicates findings at or above it, and 1 indicates a usage or I/O error. The default threshold is high. The `--version` option prints the version.

The finding identifiers are:

```
documented-hex-color-validation-claim-false
documented-no-hex-color-validation-claim-false
```

An affirmative claim without production evidence is high severity, or medium when the only evidence is in tests. A denial contradicted by production evidence is high severity. Root README and Markdown files under docs are scanned; fenced blocks are excluded and inline code counts. Python files are parsed without execution. Files under fixtures, docs, and examples are excluded from evidence, and symlinks are skipped.

## Differentiation

Generic input validation checks whether input is checked at all.

ISBN validation checks the ISBN-10 or ISBN-13 check digit of a book number.

ISSN validation checks the check digit of a serial number.

IBAN validation checks the check digit of a bank account number.

UUID validation checks the shape of a universally unique identifier.

Semver validation checks the shape of a semantic version.

MAC address validation checks a hardware address.

BIC validation checks a bank identifier code.

Cron-expression validation checks a schedule string.

Cron-expression description turns a schedule string into a human-readable sentence.

Scheduled execution runs a job on a schedule.

Date validation checks whether a date is a real calendar date.

Timeouts limit how long a call may run.

Payment processing takes a payment from a card.

Credit-card extraction reads card details from a document.

Authentication can prove account ownership with a one-time code or confirmation link.

Password authentication verifies a password against a stored hash.

Password hashing prepares a password for storage.

Password generation mints a random password.

PDF encryption protects a PDF with a password.

Email sending delivers mail.

SMS sending delivers a text message.

Document extraction reads data out of a document.

Barcode scanning decodes a code from an image.

Email validation judges an email address or its deliverability.

Phone number validation judges a number or its validity for a region.

Password strength evaluates how strong a password is.

JSON Schema validation checks JSON data against a schema.

Credit card validation judges a card number, its Luhn check, and recognized brand.

Domain validation checks a bare host name.

URL validation checks a web address.

IP address validation checks a numeric address.

JSON decoding turns text into a value.

Regex matching compares text with a pattern.

URL parsing splits a web address into parts.

Network fetching retrieves a web address.

DNS resolution looks up a name.

Barcode generation encodes an account number in a strip.

Account-number extraction reads a number from a document.

Vehicle-number extraction reads a number from a registration or image.

Vehicle-number decoding splits its sections or looks up make, model, and year.

Vehicle history lookup asks a service about a number’s past.

RGB-to-hex conversion produces a string from a triplet.

Name-to-hex conversion produces a string from a color name.

Legacy color parsing accepts named colors alongside hex strings.

RGB conversion turns any color specification into a tuple.

Base16 validation judges encoding without a `#` anchor or three-or-six length rule.

Image colorization adds colour to a greyscale image.

Stylesheet validation judges a whole stylesheet.

Palette generation picks colors without judging an input.

Spreadsheet reading is a separate claim family.

Spreadsheet generation is a separate claim family.

Word-document reading is a separate claim family.

Word-document generation is a separate claim family.

Presentation reading is a separate claim family.

Presentation generation is a separate claim family.

PDF extraction is a separate claim family.

PDF generation is a separate claim family.

PDF merging is a separate claim family.

PDF splitting is a separate claim family.

PDF rotation is a separate claim family.

PDF form-filling is a separate claim family.

PDF watermarking is a separate claim family.

PDF redaction is a separate claim family.

PDF compression is a separate claim family.

PDF annotation is a separate claim family.

Table extraction is a separate claim family.

OCR is a separate claim family.

Document extraction is a separate claim family.

E-signature is a separate claim family.

Screen recording is a separate claim family.

Video generation is a separate claim family.

QR code generation is a separate claim family.

Barcode generation is a separate claim family.

Barcode scanning is a separate claim family.

Audio mixing is a separate claim family.

Audio generation is a separate claim family.

Audio editing is a separate claim family.

Source separation is a separate claim family.

Speech recognition is a separate claim family.

Text-to-speech is a separate claim family.

Noise suppression is a separate claim family.

Music generation is a separate claim family.

Music transcription is a separate claim family.

## Limitations

```
validate hex color
```

The bare phrase above can describe a manual runbook step instead of implementation. The audit flags it for human review.

```
hex color validation
```

The bare phrase above can describe a roadmap feature instead of implementation. The audit flags it for human review.

```
hex color validator
```

The bare phrase above can describe a hosted page outside the project instead of implementation. The audit flags it for human review.

```
hex color check
```

The bare phrase above can describe a presence-only lint rule instead of implementation. The audit flags it for human review.

```
check hex color
```

The bare phrase above can describe a manual runbook step instead of implementation. The audit flags it for human review.

```
verify hex color
```

The bare phrase above can describe a visual brand comparison instead of implementation. The audit flags it for human review.

```
hex code validation
```

The bare phrase above can describe a base16 encoding check instead of implementation. The audit flags it for human review.

```
valid hex color
```

The bare phrase above can describe an example input instead of implementation. The audit flags it for human review.

```
hex color is valid
```

The bare phrase above can describe example output instead of implementation. The audit flags it for human review.

```
hex color is invalid
```

The bare phrase above can describe example error text instead of implementation. The audit flags it for human review.

```
hex color validity
```

The bare phrase above can describe a configuration flag or column instead of implementation. The audit flags it for human review.

```
hex color format validation
```

The bare phrase above can describe a format description instead of implementation. The audit flags it for human review.

```
hexadecimal color validation
```

The bare phrase above can describe a specification section instead of implementation. The audit flags it for human review.

```
validate hexadecimal color
```

The bare phrase above can describe a manual runbook step instead of implementation. The audit flags it for human review.

```
hex color code check
```

The bare phrase above can describe a style-guide checklist item instead of implementation. The audit flags it for human review.

```
check hex color code
```

The bare phrase above can describe a manual runbook step instead of implementation. The audit flags it for human review.

```
hex triplet validation
```

The bare phrase above can describe a specification section instead of implementation. The audit flags it for human review.

```
validate hex colour
```

The bare phrase above can describe a manual runbook step instead of implementation. The audit flags it for human review.

```
hex colour validation
```

The bare phrase above can describe a roadmap feature instead of implementation. The audit flags it for human review.

```
validate hex code
```

The bare phrase above can describe a base16 encoding check instead of implementation. The audit flags it for human review.

The first roadmap example can also describe a result from an external platform rather than the project's own code.

Webcolors `rgb_to_hex` is reverse conversion and is not evidence.

Webcolors `rgb_to_name` is reverse conversion and is not evidence.

Webcolors `rgb_percent_to_hex` is reverse conversion and is not evidence.

Webcolors `rgb_percent_to_name` is reverse conversion and is not evidence.

Webcolors `name_to_hex` is reverse conversion and is not evidence.

Webcolors `name_to_rgb` is reverse conversion and is not evidence.

Webcolors `name_to_rgb_percent` is reverse conversion and is not evidence.

Webcolors `html5_parse_legacy_color` accepts legacy syntax and is not evidence.

Webcolors `html5_serialize_simple_color` serializes a triplet and is not evidence.

Colour `rgb2hex` is reverse conversion and is not evidence.

Colour `web2hex` is reverse conversion and is not evidence.

Colour `hsl2rgb` is conversion and is not evidence.

Colour `rgb2hsl` is conversion and is not evidence.

A colour `Color` attribute read is not evidence.

Matplotlib `to_rgb` is conversion and is not evidence.

Matplotlib `to_rgba` is conversion and is not evidence.

Matplotlib `to_hex` is conversion and is not evidence.

Matplotlib `to_rgba_array` is conversion and is not evidence.

PIL `ImageColor.getrgb` is conversion and is not evidence.

PIL `ImageColor.getcolor` is conversion and is not evidence.

`validators.base16` judges encoding and is not evidence; validators has no color validator.

A regex match alone is not evidence.

Matplotlib `is_color_like` also accepts named colors, so a project using it solely for names can count as evidence.

Colour `Color` also accepts named colors, so a project using it solely for names can count as evidence.

Eight-digit alpha forms (`#RRGGBBAA`) are out of scope.

Bare imports are not evidence, even when the import is the only thing the module does.

A `.validate` call on a base that is not a webcolors, colour, or matplotlib-colors base is missed, even when the base holds a color object built in another module or through a helper the tracer cannot follow.

A route call must sit in a single module, even when two halves obviously belong together.

A route call on a name the module locally defines is shadowed and does not count, even when the local definition is a thin wrapper around the real library call.

A generic name called through an alias chain the tracer cannot follow is missed.

Dead code counts, because the audit reads code, not execution.

A subprocess call that shells out to an external checker is not evidence by design.

Syntax-invalid files give no evidence.

The audit matches exact phrases only, not meaning: a doc that paraphrases the capability without using any listed phrase is invisible to the claim side, and a doc that uses a listed phrase for a different capability is flagged anyway.

A doc that claims the checked capability in a roadmap, changelog, or TODO is still a claim, because the audit reads prose, not intent.

A doc that denies the checked capability with a phrase outside the denial list is not recognised as a denial.

A claim in a file that is not the root README or under a docs path is not read at all.

A validation implementation in another language in the same repo is invisible to the evidence side.

A validation route that only exists at runtime, such as a dynamically imported module or a plugin loaded by name, is invisible, because the audit never executes code and never touches the network.

This is static pattern matching, not a semantic judgement.
