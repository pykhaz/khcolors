# src/khcolors/__main__.py

"""
Main module of khcolors package
"""

import argparse
from rich.console import Console
# from softdev.debug import cprintd

try:
    from .colors_util import get_color_name

    from . import PROJTITLE
    from . import __version__
except ImportError:
    from colors_util import get_color_name

    from __init__ import PROJTITLE
    from __init__ import __version__
CN = Console()
cprint = CN.print

DBG = True
DBG = False
SHARED = {'menu': None}


def main():
    """ Entry point """

    desc = ("searching for a colour in the rich  or css library "
            "(ie. in the python `rich.color` or `matplotlib.colors` modules). "
            "result: list of all the colours with `name` in them; "
            "user can choose the colour number and its name or RGB triplet "
            "is copied to the clipboard. "
            "(`name` may contain only a part of the colour name.)")
    epilog = (f"example: {PROJTITLE} red;\n"
              f"{PROJTITLE} sea")

    parser = argparse.ArgumentParser(prog=f"{PROJTITLE}",
                                     description=desc, epilog=epilog)

    parser.add_argument("name", type=str, nargs="?", default="",
                        help="name of the colour to look for, "
                        "or of the palette to choose from "
                        "(base or base-bright)")

    parser.add_argument("-c", "--css", action="store_true",
                        default=False, help="css4 colours")
    parser.add_argument("-r", "--rgb", action="store_true", default=False,
                        help="copying rgb triplet to clipboard "
                        "instead of colour name")
    parser.add_argument("-v", "--version", action="version",
                        version=f"%(prog)s version {__version__}",
                        help="printing the application version")

    args = parser.parse_args()
    SHARED['args'] = args
    run()


def run():
    """ Function running the application """

    args = SHARED['args']
    name = args.name
    kind = "rich" if not args.css else "css"
    copy_rgb = args.rgb

    get_color_name(name, kind, rgb=copy_rgb)


def debug():
    """ Auxiliary/debug function, for development purposes """

    from rich.color import Color, ColorParseError  # pylint: disable=C0415
    try:
        from .colors_util import byte_rgb  # pylint: disable=C0415
        from .lib import cprintd  # pylint: disable=C0415
    except ImportError:
        from colors_util import byte_rgb  # pylint: disable=C0415
        from lib import cprintd  # pylint: disable=C0415

    cprintd(f"{SHARED = }", location="khcolors: __main__.debug")
    color_test = "springgreen"
    bt_rgb = None
    try:
        r, g, b = Color.parse(color_test).get_truecolor()
    except ColorParseError:
        bt_rgb = Color.parse(byte_rgb(color_test))
        r, g, b = Color.parse(byte_rgb(color_test)).get_truecolor()
        cprintd(f"{bt_rgb.get_truecolor() = }", location="khcolors")
    cprintd(f"{color_test = }, {r = }, {g = }, {b = }, {bt_rgb = }",
            location="khcolors")


if __name__ == "__main__":
    main()
