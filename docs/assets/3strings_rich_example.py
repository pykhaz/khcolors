#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3strings_rich_example.py

from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

styles = {
    'fstring': 'bold cyan',
    'raw': 'bold red3',
    'regular': 'bold  bright_yellow',  # …should be some shade of yellow…
    'title': 'bold bright_blue',
}

panel_colors = {
    'fstring': 'cyan1',
    'raw': 'red1',
    'regular': 'light_yellow3',
    'title': 'deep_sky_blue3',
}

fstring = Text('f"{strings}"', justify='center', style=styles['fstring'])
raw = Text('r"raw strings"', justify='center', style=styles['raw'])
regular = Text('"regular string"', justify='center', style=styles['regular'])
title = Text('3 kinds of string in python', justify='center',
             style=styles['title'])

cn = Console()
cn.print(Panel(title, border_style=panel_colors['title']))
panels = [
    Panel(regular, border_style=panel_colors['regular']),
    Panel(fstring, border_style=panel_colors['fstring']),
    Panel(raw, border_style=panel_colors['raw']),
]

cn.print(Columns(panels, expand=True))
