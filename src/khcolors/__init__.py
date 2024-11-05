# SPDX-FileCopyrightText: 2024-present Sebastian Kazimierski <pykhaz@o2.pl>
#
# SPDX-License-Identifier: MIT
# ## `khcolors` ─  searching for colours

# The application allows for choosing a colour from
# the `ANSI_COLOR_NAMES` or `CSS4` palettes (from `rich` or `matplotlib`
# libraries, respectively).


"""
`khcolors` - a colour selection and insertion tool for terminal applications.

This package provides utilities for selecting and formatting colors in terminal
and data visualization applications, such as matplotlib. It also provides
assistance while working with the `rich` python library.

Source files:

    └── src
        └── khcolors
            ├── __about__.py
            ├── colors_util.py
            ├── __init__.py
            ├── lib.py
            └── __main__.py

Main modules:
    - `colors_util`: Core functionality for color selection.
    - `lib`: Helper functions for managing color names and palettes.

Most important functions:
    - in `colors_util`:
        - `find_color`: getting a list of colours with `name` in them
        - `get_color_name`: getting the colour name from rich or CSS4 palettes
        - `print_color`: printing the chosen colour

    (see <a href="reference/">Reference</a> for details)

Installation:
    `pip install khcolors`

    (see <a href="tutorials/#installation-footnote">Installation</a> for details)

Example usage:
    - terminal:

    <figure>
        <img src="/assets/khcolors_simple_salmon_nr3.png"
            alt="khcolors salmon" width="600" />
        </figure>

    (see <a href="how-to-guides/">How-to guides</a> for more examples.)

    - script/REPL:

        `>>> from khcolors.colors_util import ANSI_COLOR_NAMES as palette`

        `>>> from khcolors.colors_util import find_color`

        `>>> shades = find_color(palette, "red")`

        `>>> for i, color in enumerate(shades):`

        `...     print(f"{i}. {color}")`

        `...`

        `0. red`

        `1. bright_red`

        `2. dark_red`

        `3. red3`

        `4. medium_violet_red`

        `5. indian_red`

        `6. red1`

        `7. orange_red1`

        `8. indian_red1`

        `9. pale_violet_red1`

Dependencies:
    - `matplotlib`
    - `pyperclip`
    - `rich`

For `README` file, visit: <a href"https://github.com/heliotech/khcolors">
    https://github.com/heliotech/khcolors</a>
"""

PROJTITLE = "khcolors"
