# processing-examples

This is a port of the Processing examples to Python, using mewnala (libprocessing), forked from https://github.com/processing/processing-examples.

The original examples were designed so that each sketch demonstrates a specific function or feature. This makes them a useful baseline for identifying missing functionality or differences in behavior. The goal of this project is not just to translate examples to Python, but to use them as a systematic way to test libprocessing and mewnala. Both libprocessing and mewnala are still in early development. 

The examples are organized by topic, and the original `.pde` files are included for reference.

For more information about libprocessing and mewnala, see https://github.com/processing/libprocessing/.

## Running the examples

To run the python examples install Python and mewnala following the instructions at https://github.com/processing/libprocessing/#getting-started and use `uv` to run the examples. For example:

```
uv run Basics/Color/Hue/Hue.py
```

## Getting involved
To get involved, go to the [progress tracker](https://github.com/processing/processing-examples-mewnala/issues/1), comment on the issue to let us know which example you'd like to work on. Feel free to ask for help if you need it.

If you have any questions, suggestions, or want to get involved, please join the discussion on Discord (https://discord.processing.org) in the #libprocessing channel. 

## Porting examples

To port an example, follow these steps:

1. copy the `.pde` file to a `.py` file in the same directory.
2. run `uv init --bare` to create the `pyproject.toml` file.
3. add `mewnala` as a dependency with `uv add mewnala` (this may take a while to complete the first time).
4. adapt the code to use mewnala and Python syntax.
5. test the example by running it with `uv run path/to/example.py`.

> [!IMPORTANT]
> Always compare your port with the original by running the `.pde` file in the Processing IDE.

If an example cannot be ported, or behaves differently please report it here: https://github.com/processing/libprocessing/issues

## Reporting issues

Some features are not yet implemented, and some examples may not be possible to port yet. This is expected and is part of why this porting project exists. If you encounter an issue while porting an example, please report it here: https://github.com/processing/libprocessing/issues

When reporting issues, include:

* which example you are working on
* what you expected to happen
* what actually happens
* any missing functions or unexpected behavior
* include screenshots or code snippets if helpful

## Credits
The examples without a credit line were written by Casey Reas or Ben Fry and they are in the public domain. Daniel Shiffman's examples are in the public domain. We appreciate a link back to the original and/or an acknowledgement when they are used. The copyrights for other credited files remains with the original authors.