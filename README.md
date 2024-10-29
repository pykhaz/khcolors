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
- [Release History](#release-history)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Introduction

<!-- One to two paragraph statement about your product and what it does. -->
The application helps choosing a colour name from `rich` or `CSS4` palettes. Presents a list of all the colours containing name given as a parameter.

Sources for the colour names are `matplotlib.colors` and `rich.color.ANSI_COLOR_NAMES` thus the user can easily choose the appropriate colour shade, either working with `matplotlib`, or `rich`.

Searching for the colour name involved basic python data structures, lists and dictionaries, since datasets of all the colour names were considered small.

Since the application was designed as auxiliary tool, the command line interface was chosen, with minimalistic, though appealing, text formatting. Styling of the text was achieved mostly with the `rich` module; in one case ANSI codes were used.

A possibility of using/defining custom colour palettes is to be implemented in the future release.

- ## Installation

*!TODO: about downloading the package/cloning the repo; cding to the directory`*

- Building locally

    ```bash
    hatch build
    pip install .
    ```

- Installing from PyPI

    ```bash
    pip install khcolors
    ```

    **To be implemented.**


## Usage

The easiest way to use the application is to type `khcolors` followed by the name of base colour, eg.

```bash
khcolors olive
```

All the colours containing the name given as the parameter, the base colour, are printed in the terminal, and user is asked to choose one. After confirming the choice, the colour name, or rgb triplet, are copied to clipboard and a confirmation message is displayed.

*`khcolors` usage example -- simple:*

<style>
    pre.example {
        background-color: black;
        padding: 0.5em;
        width: 45em;
        border: 2px solid white;
    }
    body {
        background-color: none;
    }
    div.container {
        width: 100%;
    }
    @keyframes blink {
        50% {
        opacity: 0.0;
        }
    }
    .blink {
      animation: blink 1s step-start 0s infinite;
    }
</style>
<div class="container">
<pre class="example">
<span style="font-weight:bold;color:lime;">khaz@mainframe</span>:<span style="font-weight:bold;color:#3333FF;">~/spy/dev/cli/utils/khcolors/assets</span>$ khcolors olive
<span style="font-weight:bold;"> Choose colour </span><span style="font-weight:bold;">(</span><span style="font-weight:bold;">number</span><span style="font-weight:bold;">)</span><span style="font-weight:bold;">:</span>
<span style="color:dimgray;background-color:#afd75f;">░</span><span style="color:white;background-color:#afd75f;"> </span><span style="font-weight:bold;color:dimgray;background-color:#afd75f;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#afd75f;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#afd75f;"> </span><span style="color:dimgray;background-color:#afd75f;"> dark_olive_green3 (175, 215, 95)        ░</span> (1) 
<span style="color:dimgray;background-color:#afff5f;">░</span><span style="color:white;background-color:#afff5f;"> </span><span style="font-weight:bold;color:dimgray;background-color:#afff5f;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#afff5f;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#afff5f;"> </span><span style="color:dimgray;background-color:#afff5f;"> dark_olive_green2 (175, 255, 95)        ░</span> (2) 
<span style="color:dimgray;background-color:#d7ff87;">░</span><span style="color:white;background-color:#d7ff87;"> </span><span style="font-weight:bold;color:dimgray;background-color:#d7ff87;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#d7ff87;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#d7ff87;"> </span><span style="color:dimgray;background-color:#d7ff87;"> dark_olive_green1 (215, 255, 135)       ░</span> (3) 
Color number to copy? (1-3, &lt;Enter&gt; to exit): 2
Color <span style="font-weight:bold;font-style:italic;color:#afff5f;background-color:black;">dark_olive_green2 (175, 255, 95)</span> copied to clipboard.
<span style="font-weight:bold;color:lime;">khaz@mainframe</span>:<span style="font-weight:bold;color:#3333FF;">~/spy/dev/cli/utils/khcolors/assets</span>$ <span class="blink">&#x2581;</span>
</pre>
</div>

If the name of a palette is given as a parameter (currently two palettes are available: `base` and `base-dark`), the colours in the palette are displayed in the terminal and the user is asked to choose one.

Application options:

- `-c` / `--css` -- for using `matplotlib CSS4` palettes instead of `rich` (which is default),

- `-r` / `--rgb` -- for copying `(r, g, b)` tuple, instead of the name.

*`khcolors` usage example -- option -c:*

<pre class="example">
<span style="font-weight:bold;color:lime;">khaz@mainframe</span>:<span style="font-weight:bold;color:#3333FF;">~/spy/dev/cli/utils/khcolors/assets</span>$ khcolors olive -c
<span style="font-weight:bold;"> Choose colour </span><span style="font-weight:bold;">(</span><span style="font-weight:bold;">number</span><span style="font-weight:bold;">)</span><span style="font-weight:bold;">:</span>
<span style="color:white;background-color:#556b2f;">░</span><span style="color:white;background-color:#556b2f;"> </span><span style="font-weight:bold;color:dimgray;background-color:#556b2f;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#556b2f;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#556b2f;"> </span><span style="color:white;background-color:#556b2f;"> darkolivegreen (85, 107, 47)            ░</span> (1) 
<span style="color:white;background-color:#808000;">░</span><span style="color:white;background-color:#808000;"> </span><span style="font-weight:bold;color:dimgray;background-color:#808000;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#808000;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#808000;"> </span><span style="color:white;background-color:#808000;"> olive (128, 128, 0)                     ░</span> (2) 
<span style="color:white;background-color:#6b8e23;">░</span><span style="color:white;background-color:#6b8e23;"> </span><span style="font-weight:bold;color:dimgray;background-color:#6b8e23;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#6b8e23;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#6b8e23;"> </span><span style="color:white;background-color:#6b8e23;"> olivedrab (107, 142, 35)                ░</span> (3) 
Color number to copy? (1-3, &lt;Enter&gt; to exit): 2 1
Color <span style="font-weight:bold;font-style:italic;filter: contrast(70%) brightness(190%);color:#556b2f;background-color:white;"> darkolivegreen (85, 107, 47) </span> copied to clipboard.
<span style="font-weight:bold;color:lime;">khaz@mainframe</span>:<span style="font-weight:bold;color:#3333FF;">~/spy/dev/cli/utils/khcolors/assets</span>$ <span class="blink">&#x2581;</span>
</pre>
</div>

*`khcolors` usage example -- option -cr:*

<div class="container">
<pre class="example">
<span style="font-weight:bold;color:lime;">khaz@mainframe</span>:<span style="font-weight:bold;color:#3333FF;">~/spy/dev/cli/utils/khcolors/assets</span>$ khcolors blue -cr
<span style="font-weight:bold;"> Choose colour </span><span style="font-weight:bold;">(</span><span style="font-weight:bold;">number</span><span style="font-weight:bold;">)</span><span style="font-weight:bold;">:</span>
<span style="color:dimgray;background-color:#f0f8ff;">░</span><span style="color:white;background-color:#f0f8ff;">  </span><span style="font-weight:bold;color:dimgray;background-color:#f0f8ff;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#f0f8ff;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#f0f8ff;">  </span><span style="color:dimgray;background-color:#f0f8ff;"> aliceblue (240, 248, 255)               ░</span> (1) 
<span style="color:white;background-color:#0000ff;">░</span><span style="color:white;background-color:#0000ff;">  </span><span style="font-weight:bold;color:dimgray;background-color:#0000ff;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#0000ff;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#0000ff;">  </span><span style="color:white;background-color:#0000ff;"> blue (0, 0, 255)                        ░</span> (2) 
<span style="color:white;background-color:#8a2be2;">░</span><span style="color:white;background-color:#8a2be2;">  </span><span style="font-weight:bold;color:dimgray;background-color:#8a2be2;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#8a2be2;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#8a2be2;">  </span><span style="color:white;background-color:#8a2be2;"> blueviolet (138, 43, 226)               ░</span> (3) 
<span style="color:white;background-color:#5f9ea0;">░</span><span style="color:white;background-color:#5f9ea0;">  </span><span style="font-weight:bold;color:dimgray;background-color:#5f9ea0;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#5f9ea0;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#5f9ea0;">  </span><span style="color:white;background-color:#5f9ea0;"> cadetblue (95, 158, 160)                ░</span> (4) 
<span style="color:white;background-color:#6495ed;">░</span><span style="color:white;background-color:#6495ed;">  </span><span style="font-weight:bold;color:dimgray;background-color:#6495ed;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#6495ed;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#6495ed;">  </span><span style="color:white;background-color:#6495ed;"> cornflowerblue (100, 149, 237)          ░</span> (5) 
<span style="color:white;background-color:#00008b;">░</span><span style="color:white;background-color:#00008b;">  </span><span style="font-weight:bold;color:dimgray;background-color:#00008b;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#00008b;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#00008b;">  </span><span style="color:white;background-color:#00008b;"> darkblue (0, 0, 139)                    ░</span> (6) 
<span style="color:white;background-color:#483d8b;">░</span><span style="color:white;background-color:#483d8b;">  </span><span style="font-weight:bold;color:dimgray;background-color:#483d8b;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#483d8b;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#483d8b;">  </span><span style="color:white;background-color:#483d8b;"> darkslateblue (72, 61, 139)             ░</span> (7) 
<span style="color:white;background-color:#00bfff;">░</span><span style="color:white;background-color:#00bfff;">  </span><span style="font-weight:bold;color:dimgray;background-color:#00bfff;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#00bfff;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#00bfff;">  </span><span style="color:white;background-color:#00bfff;"> deepskyblue (0, 191, 255)               ░</span> (8) 
<span style="color:white;background-color:#1e90ff;">░</span><span style="color:white;background-color:#1e90ff;">  </span><span style="font-weight:bold;color:dimgray;background-color:#1e90ff;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#1e90ff;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#1e90ff;">  </span><span style="color:white;background-color:#1e90ff;"> dodgerblue (30, 144, 255)               ░</span> (9) 
<span style="color:dimgray;background-color:#add8e6;">░</span><span style="color:white;background-color:#add8e6;">  </span><span style="font-weight:bold;color:dimgray;background-color:#add8e6;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#add8e6;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#add8e6;">  </span><span style="color:dimgray;background-color:#add8e6;"> lightblue (173, 216, 230)               ░</span> (10) 
<span style="color:dimgray;background-color:#87cefa;">░</span><span style="color:white;background-color:#87cefa;">  </span><span style="font-weight:bold;color:dimgray;background-color:#87cefa;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#87cefa;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#87cefa;">  </span><span style="color:dimgray;background-color:#87cefa;"> lightskyblue (135, 206, 250)            ░</span> (11) 
<span style="color:dimgray;background-color:#b0c4de;">░</span><span style="color:white;background-color:#b0c4de;">  </span><span style="font-weight:bold;color:dimgray;background-color:#b0c4de;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#b0c4de;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#b0c4de;">  </span><span style="color:dimgray;background-color:#b0c4de;"> lightsteelblue (176, 196, 222)          ░</span> (12) 
<span style="color:white;background-color:#0000cd;">░</span><span style="color:white;background-color:#0000cd;">  </span><span style="font-weight:bold;color:dimgray;background-color:#0000cd;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#0000cd;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#0000cd;">  </span><span style="color:white;background-color:#0000cd;"> mediumblue (0, 0, 205)                  ░</span> (13) 
<span style="color:white;background-color:#7b68ee;">░</span><span style="color:white;background-color:#7b68ee;">  </span><span style="font-weight:bold;color:dimgray;background-color:#7b68ee;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#7b68ee;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#7b68ee;">  </span><span style="color:white;background-color:#7b68ee;"> mediumslateblue (123, 104, 238)         ░</span> (14) 
<span style="color:white;background-color:#191970;">░</span><span style="color:white;background-color:#191970;">  </span><span style="font-weight:bold;color:dimgray;background-color:#191970;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#191970;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#191970;">  </span><span style="color:white;background-color:#191970;"> midnightblue (25, 25, 112)              ░</span> (15) 
<span style="color:dimgray;background-color:#b0e0e6;">░</span><span style="color:white;background-color:#b0e0e6;">  </span><span style="font-weight:bold;color:dimgray;background-color:#b0e0e6;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#b0e0e6;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#b0e0e6;">  </span><span style="color:dimgray;background-color:#b0e0e6;"> powderblue (176, 224, 230)              ░</span> (16) 
<span style="color:white;background-color:#4169e1;">░</span><span style="color:white;background-color:#4169e1;">  </span><span style="font-weight:bold;color:dimgray;background-color:#4169e1;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#4169e1;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#4169e1;">  </span><span style="color:white;background-color:#4169e1;"> royalblue (65, 105, 225)                ░</span> (17) 
<span style="color:dimgray;background-color:#87ceeb;">░</span><span style="color:white;background-color:#87ceeb;">  </span><span style="font-weight:bold;color:dimgray;background-color:#87ceeb;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#87ceeb;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#87ceeb;">  </span><span style="color:dimgray;background-color:#87ceeb;"> skyblue (135, 206, 235)                 ░</span> (18) 
<span style="color:white;background-color:#6a5acd;">░</span><span style="color:white;background-color:#6a5acd;">  </span><span style="font-weight:bold;color:dimgray;background-color:#6a5acd;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#6a5acd;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#6a5acd;">  </span><span style="color:white;background-color:#6a5acd;"> slateblue (106, 90, 205)                ░</span> (19) 
<span style="color:white;background-color:#4682b4;">░</span><span style="color:white;background-color:#4682b4;">  </span><span style="font-weight:bold;color:dimgray;background-color:#4682b4;">⏺⏺⏺⏺⏺⏺⏺</span><span style="font-weight:bold;color:white;background-color:#4682b4;">⏺⏺⏺⏺⏺⏺⏺</span><span style="color:white;background-color:#4682b4;">  </span><span style="color:white;background-color:#4682b4;"> steelblue (70, 130, 180)                ░</span> (20) 
Color number to copy? (1-20, &lt;Enter&gt; to exit): 7
Color <span style="font-weight:bold;font-style:italic;filter: contrast(70%) brightness(190%);color:#483d8b;background-color:white;"> (72, 61, 139) (darkslateblue) </span> copied to clipboard.
<span style="font-weight:bold;color:lime;">khaz@mainframe</span>:<span style="font-weight:bold;color:#3333FF;">~/spy/dev/cli/utils/khcolors/assets</span>$ <span class="blink">&#x2581;</span>
</pre>
</div>

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

## Release History

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

## Contact

<!--
khaz – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com
-->
khaz –  pykhaz@o2.pl

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
