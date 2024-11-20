# test_get_color_name.py

from unittest.mock import patch
import pytest
from matplotlib.colors import CSS4_COLORS
from rich.color import ANSI_COLOR_NAMES

# problems with testing:
from m_utils.printing import cprintd
from m_utils.misc import foritemin
# import sys
# sys.path.append("./src/khcolors/")

# foritemin(sys.path)

from khcolors.colors_util import get_color_name


TESTING = "testing"
CSS = "css"
RICH = "rich"


def _get_color_pool(name: str, kind: str = "rich") -> list:
    """ Getting the palette to search

        Args:
            kind (str): the palette to search the color, 'rich' or 'css'

        Returns:
            list: the list of colors to search
    """

    colors = list(CSS4_COLORS.keys()) if kind == CSS else\
        list(ANSI_COLOR_NAMES.keys())
    # for i, acolor in enumerate(colors[:]):
    #     cprintd(f"{i}. {name = } in {acolor} = {name in acolor}",
    #             location=TESTING)
    # cprintd(f"looking for {name!r} of kind {kind!r}: {colors = }, "
    #         f"{len(colors) = }",
    #         location=TESTING)

    result = [acolor for acolor in colors if name in acolor]
    # cprintd(f"{result = }", location=TESTING)
    return result


# def test_get_color_name_basic_red():
#     basecolor = "red"
#     looked_for = "red"
#     kind = "rich"
#     result = _get_color_pool(basecolor, kind=kind).index(looked_for) + 1
#     cprintd(f"looking for {looked_for!r} in {basecolor!r}, "
#             f"{kind!r} (nr {result}) →",
#             opening=TESTING)
#     assert get_color_name(basecolor, kind=kind) == looked_for


# def test_get_color_name_rich_blue():
#     basecolor = "blue"
#     looked_for = "bright_blue"
#     kind = "rich"
#     result = _get_color_pool(basecolor, kind=kind).index(looked_for) + 1
#     cprintd(f"looking for {looked_for!r} in {basecolor!r}, "
#             f"{kind!r} (nr {result}) →",
#             opening=TESTING)
#     assert get_color_name(basecolor, kind=kind) == looked_for


# def test_get_color_name_yellowgreen():
#     basecolor = "green"
#     looked_for = "yellowgreen"
#     kind = "css"
#     result = _get_color_pool(basecolor, kind=kind).index(looked_for) + 1
#     cprintd(f"looking for {looked_for!r} in {basecolor!r}, "
#             f"{kind!r} (nr {result}) →",
#             opening=TESTING)
#     assert get_color_name(basecolor, kind=kind) == looked_for


# Test z symulacją odpowiedzi użytkownika
# Spodziewane „bright_red” na podstawie wyboru „2”
# Spodziewane „red” na podstawie wyboru „1”
# Spodziewane „red” na podstawie wyboru „1”
# Testing is performed with user input: base_name, kind,
#     user_input is 'patched',
#     color is got from an auxiliary function `_get_color_pool`
@pytest.mark.parametrize("base_name, kind, user_input, color", [
    (base := "white", kind := CSS,
     _get_color_pool(base, kind=kind).index(c := "white") + 1, c),
    (base := "white", kind := RICH,
     _get_color_pool(base, kind=kind).index(c := "white") + 1, c),
    (base := "black", kind := CSS,
     _get_color_pool(base, kind=kind).index(c := "black") + 1, c),
    (base := "black", kind := RICH,
     _get_color_pool(base, kind=kind).index(c := "black") + 1, c),
    (base := "red", kind := CSS,
     _get_color_pool(base, kind=kind).index(c := "orangered") + 1, c),
    (base := "orange", kind := CSS,
     _get_color_pool(base, kind=kind).index(c := "orangered") + 1, c),
    (base := "red", kind := CSS,
     _get_color_pool(base, kind=kind).index(c := "indianred") + 1, c),
    (base := "red", kind := CSS,
     _get_color_pool(base, kind=kind).index(c := "darkred") + 1, c),
    ("green", CSS,
     _get_color_pool("green", kind=CSS).index(c := "yellowgreen") + 1, c),
    (base := "yellow", CSS,
     _get_color_pool(base, kind=CSS).index(c := "yellowgreen") + 1, c),
    (base := "green", kind := RICH,
     _get_color_pool(base, kind=kind).index(c := "green_yellow") + 1, c),
    (base := "yellow", kind := RICH,
     _get_color_pool(base, kind=kind).index(c := "green_yellow") + 1, c),
    (base := "red", CSS,
     _get_color_pool(base, kind=CSS).index(c := "mediumvioletred") + 1, c),
    (base := "violet", CSS,
     _get_color_pool(base, kind=CSS).index(c := "mediumvioletred") + 1, c),
    (base := "violet", CSS,
     _get_color_pool(base, kind=CSS).index(c := "blueviolet") + 1, c),
    (base := "blue", CSS,
     _get_color_pool(base, kind=CSS).index(c := "blueviolet") + 1, c),
    (base := "blue", kind := RICH,
     _get_color_pool(base, kind=kind).index(c := "blue_violet") + 1, c),
    (base := "violet", kind := RICH,
     _get_color_pool(base, kind=kind).index(c := "blue_violet") + 1, c),
    # ("green", CSS, "16", "yellowgreen"),
])
def test_get_color_name_auto(base_name, kind, user_input, color):
    counter = 0
    with patch("builtins.input", return_value=user_input):
        result = get_color_name(base_name, kind)[0]
        counter += 1
        assert result == color


# testing _get_color_pool
@pytest.mark.parametrize("base_name, kind, user_input, color", [
    (base := "white", kind := CSS,
     _get_color_pool(base, kind=kind), ""),
])
def test_get_color_pool_auto(base_name, kind, user_input, color):
    with patch("builtins.input", return_value=user_input):
        result = get_color_name(base_name, kind=kind)
        assert result == color
