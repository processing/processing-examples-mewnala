# processing-examples

This is a port of the Processing examples to Python, using mewnala (libprocessing), forked from https://github.com/processing/processing-examples.

The original examples were designed so that each sketch demonstrates a specific function or feature. This makes them a useful baseline for identifying missing functionality or differences in behavior. The goal of this project is not just to translate examples to Python, but to use them as a systematic way to test libprocessing and mewnala. Both libprocessing and mewnala are still in early development. Some features are not yet implemented, and some examples may not be possible to port yet. This is expected.

For more information about libprocessing and mewnala, see https://github.com/processing/libprocessing/.

## Porting examples

To get involved, go to the [progress tracker](https://github.com/processing/processing-examples-mewnala/issues/1), comment on the issue to let us know which example you'd like to work on. Feel free to ask for help if you need it.

To port an example, copy the `.pde` file to a `.py` file in this repository and adapt it to work with mewnala. The examples are organized by topic, and the original `.pde` files are included for reference.

Always compare your port with the original by running the `.pde` file in the Processing IDE. This helps you understand the intended behavior and makes it easier to spot differences.

If an example cannot be ported, or behaves differently please report it here: https://github.com/processing/libprocessing/issues

When reporting issues, include:

* which example you are working on
* what you expected to happen
* what actually happens
* any missing functions or unexpected behavior
* include screenshots or code snippets if helpful

## Community
If you have any questions, suggestions, or want to get involved, please join the discussion on Discord (https://discord.processing.org) in the #libprocessing channel. 

## Credits
The examples without a credit line were written by Casey Reas or Ben Fry and they are in the public domain. Daniel Shiffman's examples are in the public domain. We appreciate a link back to the original and/or an acknowledgement when they are used. The copyrights for other credited files remains with the original authors.