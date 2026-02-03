"""
256-color (8-bit) ANSI color support.

This module provides utilities for using the ANSI 256-color palette
(also known as 8-bit colors). It allows selecting both foreground and
background colors by index in the range [0, 255].

All returned objects are instances of `SW` and can be freely combined
with other styles and colors.

Example:
    >>> from sw import custom_color, custom_bg, bold
    >>> print((custom_color(196) + bold)("Error"))
    >>> print((custom_bg(22))("Success"))
"""

from trgb.sw import SW


class Colors256(SW):
    """
    Foreground color from the ANSI 256-color palette.

    This class represents a foreground color selected by its numeric
    index in the 256-color table.
    """

    def __init__(self, color: int):
        """
        Initializes a 256-color foreground style.

        Args:
            color (int): Color index in the range [0, 255].

        Raises:
            ValueError: If `color` is outside the valid range.
        """
        if not 0 <= color <= 255:
            raise ValueError("Color index must be in range 0..255")
        super().__init__(f"38;5;{color}")


def custom_color(color: int) -> Colors256:
    """
    Creates a foreground color from the ANSI 256-color palette.

    Args:
        color (int): Color index in the range [0, 255].

    Returns:
        Colors256: Foreground color style.

    Example:
        >>> print(custom_color(202)("Orange text"))
    """
    return Colors256(color)


class BgColors256(SW):
    """
    Background color from the ANSI 256-color palette.

    This class represents a background color selected by its numeric
    index in the 256-color table.
    """

    def __init__(self, color: int):
        """
        Initializes a 256-color background style.

        Args:
            color (int): Color index in the range [0, 255].

        Raises:
            ValueError: If `color` is outside the valid range.
        """
        if not 0 <= color <= 255:
            raise ValueError("Color index must be in range 0..255")
        super().__init__(f"48;5;{color}")


def custom_bg(color: int) -> BgColors256:
    """
    Creates a background color from the ANSI 256-color palette.

    Args:
        color (int): Color index in the range [0, 255].

    Returns:
        BgColors256: Background color style.

    Example:
        >>> print(custom_bg(17)("Dark blue background"))
    """
    return BgColors256(color)