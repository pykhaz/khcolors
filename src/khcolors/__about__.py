# SPDX-FileCopyrightText: 2024-present Sebastian Kazimierski <pykhaz@o2.pl>
#
# SPDX-License-Identifier: MIT

__version__ = "0.3.2"
# big change/many changes:
#  - new command line argument: -r/--rgb -- for copying (r, g, b) tuple,
#      instead of the name; -a/-all removed
#  - options for showing colors palette added: when `khcolors` called with
#      the name of a palette (base, base-bright), the palette is shown
#  - new file, lib.py; functions moved: _get_rgb, _luminosity, byte_rgb,
#    get_contrast_color; vars: LMN_CMPS, LMN_LT, COLOR_PALETTE
#  - get_contrast_color: new function for getting foreground/background colors
#    right
#  - 3 new functions carved out from get_color_name:
#      get_palette, get_color_choices, find_colors
#  - color tiles -- rows of colors printed -- remade completely

# __version__ = "0.1.2"

# __version__ = "0.1.1" -- minor change, when looking for color name "name"...

# __version__ = "0.1.0"
