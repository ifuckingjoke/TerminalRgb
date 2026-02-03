"""
ANSI foreground and background color definitions.

This module provides predefined color style objects based on ANSI escape
codes. All exported objects are instances of `SW` and can be freely combined
with other styles (e.g. bold, underline) using the `+` operator.

Example:
    >>> from sw import red, bright_bg_white, bold
    >>> print((red + bold + bright_bg_white)("Hello"))
"""

from trgb.sw import SW


class Colors(SW):
    """
    Foreground text color.

    This class is a thin wrapper around `SW` used to represent
    ANSI foreground color codes.

    Instances of this class are intended to be used as constants
    (e.g. `red`, `green`, `bright_blue`).
    """

    def __init__(self, *code: str):
        """
        Initializes a foreground color.

        Args:
            *code (str): ANSI foreground color codes.
        """
        super().__init__(*code)


# Standard foreground colors
red = Colors('31')
green = Colors('32')
yellow = Colors('33')
blue = Colors('34')
magenta = Colors('35')
cyan = Colors('36')
white = Colors('37')
black = Colors('30')
gray = Colors('90')

# Bright foreground colors
bright_red = Colors('91')
bright_green = Colors('92')
bright_yellow = Colors('93')
bright_blue = Colors('94')
bright_magenta = Colors('95')
bright_cyan = Colors('96')
bright_white = Colors('97')


class BgColors(SW):
    """
    Background text color.

    This class represents ANSI background color codes and behaves
    identically to `Colors`, but affects the background instead
    of the foreground.
    """

    def __init__(self, *code: str):
        """
        Initializes a background color.

        Args:
            *code (str): ANSI background color codes.
        """
        super().__init__(*code)


# Standard background colors
bg_black = BgColors('40')
bg_red = BgColors('41')
bg_green = BgColors('42')
bg_yellow = BgColors('43')
bg_blue = BgColors('44')
bg_magenta = BgColors('45')
bg_cyan = BgColors('46')
bg_white = BgColors('47')
bg_gray = BgColors('100')

# Bright background colors
bright_bg_red = BgColors('101')
bright_bg_green = BgColors('102')
bright_bg_yellow = BgColors('103')
bright_bg_blue = BgColors('104')
bright_bg_magenta = BgColors('105')
bright_bg_cyan = BgColors('106')
bright_bg_white = BgColors('107')