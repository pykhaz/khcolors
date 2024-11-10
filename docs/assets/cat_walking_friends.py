#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# cat_walking_friends.py

from rich.console import Console
from rich.text import Text
import emoji

cat = "🐈"
tiger = "🐅"
turtle = "🐢"
camel = "🐫"

friends = [cat, tiger, turtle, camel]

styles = {cat: "gray93",
          turtle: ["bold green3", "bold dark_sea_green4",
                   "bold green_yellow"],
          tiger: "bold violet",
          camel: "bold light_goldenrod1"}

# for i, friend in enumerate(friends):
#     token = next(emoji.analyze(friend))
#     value = token.value
#     data = value.data
#     print(f"{i}. {friend}:")
#     print(f"\t{token = }")
#     print(f"\t{value = }")
#     print(f"\t{data['en'] = }")
#     print(f"\t{emoji.emojize(data['en']) = }")

cat_text = Text.assemble("A ",
                         (f"silver {cat} ", styles[cat]),
                         " took his friends for a walk:\n",
                         "\t- three ",
                         (f"green {turtle*3}", "bold green"),
                         ": ",
                         (f"Jane", styles[turtle][0]),
                         ", ",
                         (f"John", styles[turtle][1]),
                         " and ",
                         (f"Tom", styles[turtle][2]),
                         ","
                         "\n\t- a ",
                         ("violet ", "dark_violet"),
                         (f"{tiger}", styles[tiger]),
                         ", ",
                         (f"Mustafa", styles[tiger]),
                         "\n\t- and a ",
                         (f"golden  ", "bold gold3"),
                         (f"{camel}", styles[camel]),
                         ", ",
                         ("Sharif", styles[camel]), ".")
c = Console()
c.print(cat_text)
