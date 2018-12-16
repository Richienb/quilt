# How you can help

At the moment, you can help by

- Adding more functions which you or someone else might find useful
- Adding and maintaining the docstrings

## Testing Guide

Using **GNU Make**, you can execute multiple commands with a single one.

- Force install the latest production version of Quilt: `make inst`
- Install the dependencies: `make deps`
- Minify the code (Linux only): `make min`
- Generate the Mkdocs documentation: `make mdoc`
- Generate the Sphinx documentation: `make cdoc`
- Build the PyPi package: `make pack`
