# lib.py
# project: khcolors

"""
Auxiliary module for khcolors
"""

from matplotlib import colors as mcolors
from rich.color import ANSI_COLOR_NAMES, Color, ColorParseError, ColorType
from rich.console import Console
from rich.text import Text


LMN_CMPS = [0.2126, 0.7152, 0.0722]  # LUMINOSITY COMPONENTS
LMN_LT = int(255*0.35)  # luminosity threshold, for fg color


COLOR_PALETTE = {
    "rich": {"base": ["black", "red", "green", "yellow", "blue", "magenta",
                      "cyan", "white"],
             "bright": ["bright_black", "bright_red", "bright_green",
                        "bright_yellow", "bright_blue", "bright_magenta",
                        "bright_cyan", "bright_white"],
             "base-bright": ["black", "bright_black", "red", "bright_red",
                             "green", "bright_green", "yellow",
                             "bright_yellow", "blue", "bright_blue",
                             "magenta", "bright_magenta", "cyan",
                             "bright_cyan", "white", "bright_white"]},
    "css": {"base": ["black", "red", "green", "yellow", "blue", "magenta",
                     "cyan", "white"],
            "bright": ["#808080", "#FF5555", "#55FF55", "#FFFF55", "#5555FF",
                       "#FF55FF", "#55FFFF", "#FFFFFF"],  # each 'bright',
            #                            # but black can be #xxxx00 or #xxxxFF
            "base-bright": []}
            }

CN = Console()


for pair in zip(COLOR_PALETTE["css"]["base"], COLOR_PALETTE["css"]["bright"]):
    COLOR_PALETTE["css"]["base-bright"].extend(pair)


def _get_rgb(color):
    """ Converts color to r, g, b in range [0, 1] """

    try:
        r, g, b = Color.parse(color).get_truecolor()
    except ColorParseError:
        r, g, b = Color.parse(byte_rgb(color)).get_truecolor()
    # cprintd(f"{color = } →  {(r, g, b) = }", location="_get_rgb")

    return (r, g, b)


def _luminosity(rgb: tuple[float]) -> float:
    """ Calculates the luminosity of a color """

    return sum(rgb[i]*LMN_CMPS[i] for i in range(3))


def byte_rgb(color):
    """ Converts color to r, g, b in range [0, 1], to range [0, 255] """

    r, g, b = [item*255 for item in mcolors.to_rgb(color)]

    return f"rgb({r:.0f},{g:.0f},{b:.0f})"


def cprintd(message, opening="DBG:", location=""):
    """ Print debug message """

    dbg_message = Text(f" {opening} ", style="italic bold red on white")
    dbg_message.append(Text(f" {message}", style="dark_orange on black"))
    if location:
        dbg_message.append(Text(f" [{location}]", style="gray58 on black"))

    CN.print(dbg_message)


def get_contrast_color(color: Color) -> str:
    """ Returning #RRGGBB string background color for given one """

    # cprintd(f"{color = }, of type {type(color)}")
    try:
        color = Color.parse(color)
    except ColorParseError:
        color = Color.parse(byte_rgb(color))
    r, g, b = color.get_truecolor()
    luminosity = _luminosity((r, g, b))
    inv = 255 - luminosity  # inverse luminosity

    # luminosity_inv = 0 if inv < 127 else inv
    if inv < LMN_LT:
        # luminosity_inv = 0
        result = "black"
    else:
        # luminosity_inv = 255
        result = "bright_white"
    # lmn_inv_hex = "#" + f"{int(luminosity_inv):02x}" * 3
    # return lmn_inv_hex
    return result
