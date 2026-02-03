# TerminalRGB - trgb

A library for styling text in a terminal using ANSI-codes for Python

-------------------------

Functional:

Colors, Styles, RGB and 256 palette

import:

'''bash

    pip install trgb

'''py

    from trgb import red, blue, bold, rgb ...

using:

'''py

    print(red("Print red text"))

    --------------------------- or

    style = red("Print red text")
    print(red)

the ability to stack styles: 

## WARNING: the interpreter may consider your action to be an error - use type ignore

'''py

    print(bold + rgb(1,1,1)("Hello World!"))

    --------------------------- or

    style = bold + rgb(4, 239, 8)
    print(style("Hello World!"))


you can stack as many styles as you want:

'''py

    style = bg_rgb(1,1,1) + rgb(2,2,2) + italic
    print(style("text"))

# I wish you a pleasant experience. Good luck!