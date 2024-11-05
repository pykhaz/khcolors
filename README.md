[//]: <> (pandoc README.md -f markdown -t html5 -s -o README.html)

# khcolors 🎨
## *Searching for colour names in terminal*

![Python version](https://img.shields.io/badge/Python-3.10-blue)
![Packaged with hatch](https://img.shields.io/badge/Packaged%20with-hatch-60c7a8)

`khcolors` is a terminal application for searching colour names.

<!-- [![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url] -->

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Known Issues](#known-issues)
- [Release History](#release-history)
- [Links](#links)
- [License](#license)
- [Contact](#contact)
<!-- - [Acknowledgments](#acknowledgments) -->

## Introduction

<!-- One to two paragraph statement about your product and what it does. -->
The application helps choosing a colour name from `rich` or `CSS4` palettes. `khcolors` when given name, presents a list of all the colours containing the name; user can choose an index of a particular colour.

Sources for the colour names are `matplotlib.colors` and `rich.color.ANSI_COLOR_NAMES`. Thus the user can easily choose the appropriate colour shade, either working with `matplotlib`, or `rich`.

Searching for the colour name involves basic python data structures, lists and dictionaries, since datasets of all the colour names were considered small.

Since the application was designed as auxiliary tool, the command line interface was chosen, with minimalistic, though appealing, text formatting. Styling of the text was achieved mostly with the `rich` module; in one case ANSI codes were used.

A possibility of using/defining custom colour palettes is to be implemented in the future release.

- ## Installation

>   * Building locally

> > Clone \(`git clone https://github.com/pykhaz/khcolors.git`) or download the package \([github.com/pykhaz/khcolors](https://github.com/pykhaz/khcolors) → button/menu "Code" → "Download ZIP"), `cd` into `khcolors` and


> >     hatch build
> >     pip install .

>    - Installing from PyPI


 > >     pip install khcolors


## Usage

The easiest way to use the application is to type `khcolors` followed by the name of base colour, eg.

```bash
khcolors olive
```

All the colours containing the name given as the parameter, the base colour, are printed in the terminal, and user is asked to choose one. After confirming the choice, the colour name, or rgb triplet, are copied to clipboard and a confirmation message is displayed.

If the name of a palette is given as a parameter (currently two palettes are available: `base` and `base-bright`), the colours in the palette are displayed in the terminal and the user is asked to choose one.

Application options:

- `-c` / `--css` -- for using `matplotlib CSS4` palettes instead of `rich` (which is default),

- `-r` / `--rgb` -- for copying `(r, g, b)` tuple, instead of the name.

<!-- ![`khcolors` for colour `salmon`, cases for all the options (linux).](./assets/khcolors_salmon_x4_linux.png "This is the caption of the figure (a simple paragraph)."){ width=600px } -->

Screenshots:

<figure>
    <img src="./assets/khcolors_salmon_x4_linux.png" alt="`khcolors` for `salmon`" style="width:50%; height:auto;">
  <figcaption>khcolors for colour 'salmon', cases for all the options (linux).</figcaption>
</figure>

<br />

<figure>
    <img src="./assets/khcolors_salmon_x4_win11.png" alt="`khcolors` for `salmon`" style="width:50%; height:auto;">
  <figcaption>khcolors for colour 'salmon', cases for all the options (windows).</figcaption>
</figure>

<!-- [see file](./assets/outputfile_edited.html) -->

<!-- <figure> -->
<!--     <figcaption>khcolors, usage: on linux mint, in kitty</figcaption> -->
<!--     <img src="assets/khcolors_kitty.png" style="width: 50%;" title="usage: kitty linux" alt="image - usage: kitty linux" /> -->
<!-- </figure> -->

<!-- <br/> -->


<!-- <figure> -->
<!--     <figcaption>khcolors, usage: on windows, in powershell</figcaption> -->
<!--     <img src="assets/khcolors_powershell.png" style="width: 50%;" title="usage: powershell windows" alt="image - usage: powershell windows" /> -->
<!-- </figure> -->

<!--
## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```
-->

## Known issues

- Minimal terminal width -- as the width of the terminal grows smaller, the colour lines get messy. When the width drops below below 37 columns, a single colour line gets printed in two rows, which looks bad (but this is hardly a case, since the terminal window width is, in most cases, greater than 37 columns).

## Release History

- 0.3.3
  - updated README.md
- 0.3.2
  - new command line argument: `-r`/`--rgb` -- for copying `(r, g, b)` tuple,
      instead of the name; `-a`/`-all` removed
  - options for showing colors palette added: when `khcolors` called with
      the name of a palette (`base`, `base-bright`), the palette is shown
  - new file, `lib.py`; functions moved: `_get_rgb`, `_luminosity`, `byte_rgb`,
    `get_contrast_color`; vars: `LMN_CMPS`, `LMN_LT`, `COLOR_PALETTE`
  - `get_contrast_color`: new function for getting foreground/background colors
    right
  - 3 new functions carved out from `get_color_name`:
      `get_palette`, `get_color_choices`, `find_colors`
  - color tiles -- rows of colors printed -- remade completely
- 0.1.1
    - Minor change of the result message
- 0.1.0
    - First working version of the package
- 0.0.1
    - Work in progress

## Links

- [GitHub pages](https://pykhaz.github.io/khcolors/index.html)

## License

The `khcolors` application is distributed under the MIT license. See [LICENSE](LICENSE.txt) for more information.

<!-- [https://github.com/heliotech](https://github.com/heliotech/) -->


<!-- Markdown link & img dfn's -->
<!--
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
-->

## Contact

<!--
khaz – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com
-->
khaz –  pykhaz@o2.pl
