"""
Text style (attribute) ANSI definitions.

This module provides predefined text styling attributes based on ANSI escape
codes, such as bold, italic, underline, and others.

All exported objects are instances of `SW` and can be freely combined
with colors and other styles using the `+` operator.

Example:
    >>> from sw import red, bold, underline
    >>> print((red + bold + underline)("Important"))
"""

from trgb.sw import SW


class Styles(SW):
    """
    Text style attribute.

    This class represents non-color ANSI text attributes such as bold,
    italic, or underline.

    Instances of this class are intended to be used as constants
    and combined with other styles.
    """

    def __init__(self, *code: str):
        """
        Initializes a text style attribute.

        Args:
            *code (str): ANSI style codes.
        """
        super().__init__(*code)


# Text style attributes
bold = Styles('1')
dim = Styles('2')
italic = Styles('3')
underline = Styles('4')
blink = Styles('5')
blink_fast = Styles('6')
reverse = Styles('7')
hidden = Styles('8')
strikethrough = Styles('9')