# colors_util.py

"""
Main module for choosing colour name from rich or css library.

Functions:

    debug() -> None
    find_color(colors_base: list, name: str) -> list
    get_color_choices(name: str = "", kind: str = "rich",
                      palette: list = None) -> list
    get_color_name(search_for: str, kind: str = "rich", rgb: bool = False,
                   palette: list = None) -> str
    get_palette(palette, kind, rgb=False, dbg=False) -> list
    print_color(i, name, color_base="rich", marg=3, total_colors=10) -> None
    print_found(color: str, kind: str = "rich", rgb: bool = False) -> None

Constants:

    CN: Console
    COLOR_BASE: dict
    MARKER0: str
    MARKER1: str
    FTITLE: str

"""

from shutil import get_terminal_size
import sys
from matplotlib.colors import CSS4_COLORS
from rich.color import ANSI_COLOR_NAMES
from rich.console import Console
from rich.text import Text
import pyperclip

try:
    from .lib import COLOR_PALETTE, _get_rgb, _luminosity, byte_rgb
    from .lib import get_contrast_color as get_contrast
    from .lib import get_integer
    from .lib import cprintd
except ImportError:
    from lib import COLOR_PALETTE, _get_rgb, _luminosity, byte_rgb
    from lib import get_contrast_color as get_contrast
    from lib import get_integer
    # from lib import cprintd

FTITLE = __file__.split("/", maxsplit=-1)[-1].split(".", maxsplit=-1)[0]

CN = Console()
cprint = CN.print

COLOR_BASE = {'css': CSS4_COLORS, 'rich': ANSI_COLOR_NAMES}

LMN_LT = int(255*0.35)  # luminosity threshold, for fg color
CL_MAX_CPY = 10  # arbitrary chosen number of colors being copied to clipboard
#            #   without question
# CL_MAX_CPY = 2  # value for dbg.
CL_MAX_LST = 35  # arbitrary chosen number of colors being displayed
#                #   as colour choices

# markers for colour samples:
MARKER0 = "\u00a0"
# MARKER1 = "x"  # \u2501
# MARKER1 = "\u25cf"  # ●
# MARKER1 = "◉"
MARKER1 = "■"
# if system().lower() != "windows":  # platform.
#     MARKER1 = "⏺"  # \u23fa
# else:
#     MARKER1 = "o"


def _again(args, msg="") -> None:
    """ Asking user if he wants to try again

        Args:
            args (dict): dictionary of arguments for `get_color_name`
            msg (str): message to print

        Efect:
            Calls `get_color_name` again.
    """

    # return input("\nTry again? (y/n): ").lower().startswith("y")
    ans = input(f"{msg} Try again? (y/n): ").lower()
    if ans == "y":
        cprintd(f"Again, args = {args}", location="_again")
        get_color_name(**args)
        sys.exit(0)
    else:
        sys.exit("Exiting, no colours copied.")


def debug():
    """ Function for debugging """

    cprint("_luminosity test", style="orange3 bold")
    cprint(f"{_luminosity((0, 0, 0)) = :.4f}")
    cprint(f"{_luminosity((1, 2, 3)) = :.4f}")
    cprint(f"{_luminosity((4.5, 6.7, 8.9)) = :.4f}")


# def find_color(colors_base: list, name: str) -> list:
#     """ Getting a target list of colors including `name`

#         Args:
#             colors_base (list): the list of colors to search
#             name (str): the color to search

#         Returns:
#             list: the list of colors to choose from
#     """

#     found = [color for color in colors_base if name in color]
#     if not found:
#         if name == "name":
#             msg = Text.assemble(("Looking for color name ", ""),
#                                 (f"{name}", "bold italic"),
#                                 (" -- ", ""),
#                                 ("seriously?", "bold italic red"))
#             cprint(msg)
#             return []
#         if name not in ["base", "base-bright"]:
#             cprint(Text.assemble(("No color found for '", ""),
#                                  (f"{name}", "bold"),
#                                  ("', exiting.", "")))
#         return []

#     cprintd(f"{found = } of type {type(found)}, len = {len(found)}",
#             location="find_color")

#     return found


def get_color_choices(name: str = "", kind: str = "rich",
                      palette: list = None) -> list:
    """ Getting possible colour choices

        Args:
            name (str): the color to search for
            kind (str): the palette to search the color, 'rich' or 'css'
            palette (list): optionally a specific palette to search through

        Returns:
            list: the list of colors to search
    """

    result = [color for color in (palette or COLOR_BASE[kind])
              if name in color]

    # cprintd(f"{result = } of type {type(result)}, len = {len(result)}",
    #         location="get_color_choices")

    return result


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
            kind (str): the palette to search the colour, 'rich' or 'css'
            rgb (bool): if True, the color rgb triplet is copied
                        to clipboard

        Returns:
            None: the application prints a list of colours found and allows
            copying a chosen name to clipboard.
    """

    # when there is a palette name, instead of a colour:
    if search_for in ["base", "base-bright"]:
        get_palette(search_for, kind, rgb=rgb)

    colors_base = get_color_choices(search_for, kind=kind, palette=palette)
    total_colors = len(colors_base)
    if total_colors > CL_MAX_LST:
        ans = input(f"Display all of {total_colors} colors? [y/N]: ")
        if ans.lower() != "y":
            cprint("Exiting.", style="bold")
            return ""

    # cprintd("Calling `find_color`", location="get_color_name")
    # RFC: replacing `found` with `colors_base`…
    # found = find_color(colors_base, search_for)
    # if not found:
    #     return ""
    cprint(" Choose colour (number):", style="bold")
    # marg = len(str(len(found)))
    marg = len(str(len(colors_base)))
    for i, color in enumerate(colors_base):
        print_color(i, color, color_base=kind, marg=marg,
                    total_colors=total_colors)

    prompt = (f"Colour number to copy? (1-{total_colors}, "
              "<Enter> to exit): ")
    while True:
        try:
            nr_to_copy = get_integer(prompt, limits=(1, total_colors))
            if nr_to_copy is None:
                return ""
            try:
                chosen_color = colors_base[nr_to_copy - 1]
            except TypeError:
                chosen_color = [colors_base[nr - 1] for nr in nr_to_copy]

            chosen_color = [chosen_color] if isinstance(chosen_color, str) \
                else chosen_color

            if len(chosen_color) > CL_MAX_CPY:
                prompt = f"Copy all of {len(chosen_color)} colors? [y/N]: "
                ans = input(prompt)
                args = dict(search_for=search_for, kind=kind, rgb=rgb,)
                actions = {"n": lambda: _again(args, "No colours copied. "),
                           "y": lambda: None, }
                actions.get(ans.lower(), actions['n'])()

            if not rgb:
                pyperclip.copy(", ".join(chosen_color))
            else:
                rgb_tp = ", ".join(str(tp) for tp in _get_rgb(chosen_color))
                pyperclip.copy(rgb_tp)
            print_found(chosen_color, kind=kind, rgb=rgb)
            return chosen_color
        except ValueError:
            cprint("Wrong number, leave empty to exit.")

    return ""


def get_palette(palette, kind, rgb=False, dbg=False):
    """ Getting colors palette """

    colors = COLOR_PALETTE[kind][palette]
    if dbg:
        return colors
    return get_color_name("", rgb=rgb, palette=colors)


def print_color(i, name, color_base="rich", marg=3, total_colors=10) -> None:
    """ Printing a color tile

        Args:
            i (int): the index of the color
            name (str): the name of the color
            color_base (str): the base color
            marg (int): the margin
            total_colors (int): the total number of colors, for adjusting
                the line width

        Returns:
            None (prints)
    """

    clr = name if color_base == "rich" else byte_rgb(name)
    triplet = _get_rgb(clr)
    if get_terminal_size().columns > 60:  # 61 -- max name + (r, g, b) length
        name_triplet_txt = f"{name} {str(triplet)}"
    else:
        name_triplet_txt = f"{name}"
    fg = get_contrast(clr)
    tile_len = 7
    style = f"{fg} on {clr}"
    nr_txt = f" ({i + 1}) "
    nr_txt_len = len(str(total_colors)) + 4
    fill_len = (get_terminal_size().columns - tile_len*2 - nr_txt_len -
                len(name_triplet_txt) - 2*marg - 3)

    color_line = Text.assemble(("░", style),
                               (MARKER0*marg, style),
                               (MARKER1*tile_len, f"bold #000000 on {clr}"),
                               (MARKER1*tile_len, f"bold #ffffff on {clr}"),
                               (MARKER0*marg, style),
                               (f"{nr_txt:>{nr_txt_len}}",
                                "#ffffff on #000000"),
                               (f" {name_triplet_txt}", style),
                               (f"{' '*fill_len}", style),
                               ("░", style))
    cprint(color_line)


def print_found(colors: str, kind: str = "rich", rgb: bool = False) -> None:
    """ Print a found color """

    if len(colors) > 1:
        plural = "s"
        nl = Text("\n    ", style="")
    else:
        plural = ""
        nl = Text("", style="")
    msg = Text(f"Color{plural} ")
    for i, color in enumerate(colors):
        if kind == "css":
            color_code = byte_rgb(color)
        else:
            color_code = color
        rgb_tp = _get_rgb(color)
        bg = get_contrast(color)
        # extra space, padding for colour name, if bg is white:
        extra_spc = "" if bg == "black" else " "
        if not rgb:
            color_name_rgb = f"{extra_spc}{color} {rgb_tp}{extra_spc}"
        else:
            color_name_rgb = f"{extra_spc}{rgb_tp} ({color}){extra_spc}"
        msg.append(nl)
        msg.append(color_name_rgb,
                   style=f"bold italic {color_code} on {bg}")
    msg.append(" copied to clipboard.")
    cprint(msg)
