#!/bin/bash

# serving mkdocs for files from the src
# (can be also `PYTHONPATH=src mkdocs serve`)

export PYTHONPATH=src
mkdocs serve

