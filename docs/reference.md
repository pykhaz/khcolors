## Project Structure

Folders and source files of the project looked as follows:
```
khcolors
├── src
│   └── khcolors
│       ├── __about__.py
│       ├── colors_util.py
│       ├── __init__.py
│       ├── lib.py
│       └── __main__.py
└── tests
    ├── __init__.py
    └── test_get_color_name.py
```

## `khcolors.colors_util`

::: khcolors.colors_util

## Operation

The entry point of the application was defined in `pyproject.toml` as:

```toml
[project.scripts]
khcolors = "khcolors.__main__:main"
```

After defining `argparse.ArgumentParser`, adding the arguments and parsing
them, the main function of the application was called:

```python
get_color_name(search_for: str, kind: str = "rich", rgb: bool = False,
                   palette: list = None) -> str
```

Arguments:

- `search_for`: the name of the colour to look for, e.g. `olive`.
- `kind`: the kind of palette to use, e.g. `rich` or `css`.
- `rgb`: whether to copy the colour name or as an `(r, g, b)` tuple.
- `palette`: the palette to use instead of `ANSI_COLOR_NAMES` or `CSS4_COLORS`.

Returns:

- `None` -- the result of the search is printed via function `print_color`,
in a loop, for each found colour.

Finally `get_color_name` asks for the number of the chosen colour and copies
the result to the clipboard.
