# colors_util.py

"""
Main module of the khcolors package/application.
"""

from matplotlib.colors import CSS4_COLORS
from rich.color import ANSI_COLOR_NAMES
from rich.console import Console
from rich.text import Text
import pyperclip
from platform import system

try:
    from .lib import COLOR_PALETTE, _get_rgb, _luminosity, byte_rgb
    from .lib import get_contrast_color as get_contrast
    # from .lib import cprintd
except ImportError:
    from lib import COLOR_PALETTE, _get_rgb, _luminosity, byte_rgb
    from lib import get_contrast_color as get_contrast
    # from lib import cprintd

ftitle = __file__.split("/", maxsplit=-1)[-1].split(".", maxsplit=-1)[0]

CN = Console()
cprint = CN.print

COLOR_BASE = {'css': CSS4_COLORS, 'rich': ANSI_COLOR_NAMES}

# markers for colour samples:
MARKER0 = "\u00a0"
# MARKER1 = "x"  # \u2501
# MARKER1 = "\u25cf"  # ●
# MARKER1 = "◉"

LMN_LT = int(255*0.35)  # luminosity threshold, for fg color
if system().lower() != "windows":  # platform.
    MARKER1 = "⏺"  # \u23fa
else:
    MARKER1 = "o"


def get_color_choices(name: str = "", kind: str = "rich",
                      palette: list = None) -> list:
    """ Getting the palette to search

        Args:
            kind (str): the palette to search the color, 'rich' or 'css'

        Returns:
            list: the list of colors to search
    """

    palette = palette or COLOR_BASE[kind]

    return [color for color in palette if name in color]


def find_color(colors_base: list, name: str) -> list:
    """ Getting a target list of colors including `name`

        Args:
            colors_base (list): the list of colors to search
            name (str): the color to search

        Returns:
            list: the list of colors to choose from
    """

    found = [color for color in colors_base if name in color]
    if not found:
        if name == "name":
            msg = Text.assemble(("Looking for color name ", ""),
                                (f"{name}", "bold italic"),
                                (" -- ", ""),
                                ("seriously?", "bold italic red"))
            cprint(msg)
            return []
        if name not in ["base", "base-bright"]:
            cprint(Text.assemble(("No color found for '", ""),
                                 (f"{name}", "bold"),
                                 ("', exiting.", "")))
        return []

    return found


def get_color_name(search_for: str, kind: str = "rich", rgb: bool = False,
                   palette: list = None) -> str:
    """ Getting the colour name from rich or CSS4 palettes

        Function returning the name of the colour, chosen by the user, from
        printed list of colours. The list is made from the rich or CSS4
        palettes; it includes all the colour names containing the base
        colour provided (`search_for`).
        (Main function of the application.)

        Args:
            search_for (str): name (or part of the name) of the colour
                              to look for.
            kind (str): the palette to search the color, 'rich' or 'css'
            rgb (bool): if True, the color rgb triplet is copied
                        to clipboard

        Returns:
            None: the application prints a list of colours found and allows
            copying a chosen name to clipboard.
    """

    if search_for in ["base", "base-bright"]:
        get_palette(search_for, kind, rgb=rgb)
    colors_base = get_color_choices(search_for, kind=kind, palette=palette)
    total_colors = len(colors_base)
    if total_colors > 35:
        ans = input(f"Display all of {total_colors} colors? [y/N]: ")
        if ans.lower() != "y":
            cprint("Exiting.", style="bold")
            return ""

    found = find_color(colors_base, search_for)
    if not found:
        return ""
    cprint(" Choose colour (number):", style="bold")
    marg = len(str(len(found)))
    for i, color in enumerate(found):
        print_color(i, color, color_base=kind, marg=marg)

    nr_to_copy = None
    while nr_to_copy is None:
        try:
            to_copy = input(f"Color number to copy? (1-{total_colors}, "
                            "<Enter> to exit): ")
            if to_copy == "":
                return ""
            nr_to_copy = int(to_copy) - 1
            if 0 <= nr_to_copy <= total_colors - 1:
                chosen_color = found[nr_to_copy]
                rgb_tp = _get_rgb(chosen_color)
                if not rgb:
                    pyperclip.copy(chosen_color)
                else:
                    pyperclip.copy(str(rgb_tp))
                print_found(chosen_color, kind=kind, rgb=rgb)
                return chosen_color
            cprint(f"Number should have been 0 ≤ i ≤ {total_colors}. "
                   "Not copying.")
            nr_to_copy = None
        except ValueError:
            cprint("Wrong number, leave empty to exit.")

    return ""


def print_found(color: str, kind: str = "rich", rgb: bool = False) -> None:
    """ Print a found color """

    if kind == "css":
        color_code = byte_rgb(color)
    else:
        color_code = color
    rgb_tp = _get_rgb(color)
    bg = get_contrast(color)
    msg = Text("Color ")
    # extra space, padding for color name, if bg is white:
    extra_spc = "" if bg == "black" else " "
    if not rgb:
        color_name_rgb = f"{extra_spc}{color} {rgb_tp}{extra_spc}"
    else:
        color_name_rgb = f"{extra_spc}{rgb_tp} ({color}){extra_spc}"
    msg.append(color_name_rgb,
               style=f"bold italic {color_code} on {bg}")
    msg.append(" copied to clipboard.")
    cprint(msg)


def debug():
    """ Function for debugging """

    # arrays of colours:
    # cprintd("CSS4_COLORS:")
    # for i, color in enumerate(CSS4_COLORS):
    #     cprintd(f"{i:>2}. {color = }", location="get_color_name")
    # cprintd("ANSI_COLOR_NAMES:")
    # for i, color in enumerate(ANSI_COLOR_NAMES):
    #     cprintd(f"{i:>2}. {color = }", location="get_color_name")

    cprint("_luminosity test", style="orange3 bold")
    cprint(f"{_luminosity((0, 0, 0)) = :.4f}")
    cprint(f"{_luminosity((1, 2, 3)) = :.4f}")
    cprint(f"{_luminosity((4.5, 6.7, 8.9)) = :.4f}")


def get_palette(palette, kind, rgb=False, dbg=False):
    """ Getting colors palette """

    colors = COLOR_PALETTE[kind][palette]
    if dbg:
        return colors
    get_color_name("", rgb=rgb, palette=colors)


def print_color(i, name, color_base="rich", marg=3):
    """ Printing a color tile """

    clr = name if color_base == "rich" else byte_rgb(name)
    triplet = _get_rgb(clr)
    fg = get_contrast(clr)
    tile_len = 7
    color_tile = Text("░", style=f"{fg} on {clr}")  # U+2591 -- ░
    color_tile.append(MARKER0*marg, style=f"white on {clr}")
    if system().lower != "windows":  # platform.
        color_tile.append(MARKER1*tile_len, style=f"bold black on {clr}")
        color_tile.append(MARKER1*tile_len, style=f"bold white on {clr}")
    color_tile.append(MARKER0*marg, style=f"white on {clr}")

    name_triplet_txt = f"{name} {str(triplet)}"
    name_txt = Text(f" {name_triplet_txt:<40}", style=f"{fg} on {clr}")
    name_txt.append("░", style=f"{fg} on {clr}")
    color_tile.append(f"{name_txt}", style=f"{fg} on {clr}")
    nr_txt = Text(f" ({i + 1}) ")

    cprint(color_tile, end="")
    cprint(nr_txt)
