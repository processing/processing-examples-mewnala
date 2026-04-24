# processing-examples-mewnala

This repo is a community effort to port the official Processing examples to Python using mewnala (libprocessing).

## About mewnala and libprocessing
**mewnala** (working title) is a new Python implementation of Processing built on top of libprocessing. 

**libprocessing** is an experimental Rust library that aims to support the Processing API across different programming languages. 

For more information about libprocessing and mewnala, see https://github.com/processing/libprocessing/.

## Motivation
This project exists to help develop mewnala and libprocessing. Each example in this repo focuses on a specific function or feature of Processing. This makes the collection a practical way to test how well those features are supported in mewnala.

By porting the examples, we can quickly identify missing features, inconsistencies, and differences in behavior compared to Processing (Java). Like their original counterpart, the examples will also serve as a reference for how to use mewnala in Python.

## Running the examples
To run the python examples install Python and mewnala following the instructions at https://github.com/processing/libprocessing/#getting-started and use `uv` to run the examples. For example:

```
uv run Basics/Color/Hue/Hue.py
```

## Getting involved
To get involved, go to the [progress tracker](https://github.com/processing/processing-examples-mewnala/issues/1), comment on the issue to let us know which example you'd like to work on. Feel free to ask for help if you need it.

If you have any questions, suggestions, or want to get involved, please join the discussion on Discord (https://discord.processing.org) in the #libprocessing channel. 

## Porting examples
The examples are organized by topic, and the original `.pde` files are included for reference.

To port an example, follow these steps:

1. copy the `.pde` file to a `.py` file in the same directory.
2. run `uv init --bare` to create the `pyproject.toml` file.
3. add `mewnala` as a dependency with `uv add mewnala` (this may take a while to complete the first time).
4. adapt the code to use mewnala and Python syntax.
5. test the example by running it with `uv run path/to/example.py`.

> [!IMPORTANT]
> Always compare your port with the original by running the `.pde` file in the Processing IDE.

If an example cannot be ported, or behaves differently please report it here: https://github.com/processing/libprocessing/issues

### Minimal example of a port

#### Processing (Java)

```java
void setup() {
  size(400, 400);
  background(255);
}

void draw() {
  fill(255, 100, 200);
  circle(200, 200, 100);
}
```

#### mewnala (Python)

```python
from mewnala import *

def setup():
    size(400, 400)
    background(255)

def draw():
    fill(255, 100, 200)
    circle(200, 200, 100)

run()
```

Python syntax is different from Java, but the structure of the code is very similar.

Note the import statement at the top to import the mewnala library, and the call to `run()` at the end to start the sketch. These may not be necessary in the future, but they are needed for now.

## Reporting issues
Some features are not yet implemented, and some examples may not be possible to port yet. This is expected and is part of why this porting project exists. If you encounter an issue while porting an example, please report it here: https://github.com/processing/libprocessing/issues

When reporting issues, include:

* which example you are working on
* what you expected to happen
* what actually happens
* any missing functions or unexpected behavior
* include screenshots or code snippets if helpful

## Prior work
Some of the examples have been ported to Python (Processing.py) before (see https://github.com/jdf/processing.py/tree/master/examples.py). However, only a subset of all examples have been ported, and Processing.py syntax uses camelCase for function names, which is different from the snake_case convention used in mewnala.

## Credits
The examples without a credit line were written by Casey Reas or Ben Fry and they are in the public domain. Daniel Shiffman's examples are in the public domain. We appreciate a link back to the original and/or an acknowledgement when they are used. The copyrights for other credited files remains with the original authors.