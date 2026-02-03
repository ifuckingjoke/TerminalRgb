"""
Truecolor (24-bit RGB) ANSI color support.

This module provides utilities for using 24-bit (truecolor) ANSI escape
codes, allowing precise specification of foreground and background colors
using RGB components.

All returned objects are instances of `SW` and can be freely combined
with other styles and colors.

Example:
    >>> from sw import rgb, bg_rgb, bold
    >>> print((rgb(255, 80, 80) + bold)("Error"))
    >>> print((bg_rgb(30, 30, 30))("Dark background"))
"""

from trgb.sw import SW


class RGBColors(SW):
    """
    Foreground color defined using 24-bit RGB values.

    This class represents a truecolor foreground style using
    explicit red, green, and blue components.
    """

    def __init__(self, r: int, g: int, b: int):
        """
        Initializes an RGB foreground color.

        Args:
            r (int): Red channel value in range [0, 255].
            g (int): Green channel value in range [0, 255].
            b (int): Blue channel value in range [0, 255].

        Raises:
            ValueError: If any channel value is outside the valid range.
        """
        for c in (r, g, b):
            if not 0 <= c <= 255:
                raise ValueError("RGB values must be in range 0..255")
        super().__init__(f"38;2;{r};{g};{b}")


def rgb(r: int, g: int, b: int) -> RGBColors:
    """
    Creates a foreground color using 24-bit RGB values.

    Args:
        r (int): Red channel value in range [0, 255].
        g (int): Green channel value in range [0, 255].
        b (int): Blue channel value in range [0, 255].

    Returns:
        RGBColors: Foreground RGB color style.

    Example:
        >>> print(rgb(0, 200, 255)("Cyan-like text"))
    """
    return RGBColors(r, g, b)


class BgRGBColors(SW):
    """
    Background color defined using 24-bit RGB values.

    This class represents a truecolor background style using
    explicit red, green, and blue components.
    """

    def __init__(self, r: int, g: int, b: int):
        """
        Initializes an RGB background color.

        Args:
            r (int): Red channel value in range [0, 255].
            g (int): Green channel value in range [0, 255].
            b (int): Blue channel value in range [0, 255].

        Raises:
            ValueError: If any channel value is outside the valid range.
        """
        for c in (r, g, b):
            if not 0 <= c <= 255:
                raise ValueError("RGB values must be in range 0..255")
        super().__init__(f"48;2;{r};{g};{b}")


def bg_rgb(r: int, g: int, b: int) -> BgRGBColors:
    """
    Creates a background color using 24-bit RGB values.

    Args:
        r (int): Red channel value in range [0, 255].
        g (int): Green channel value in range [0, 255].
        b (int): Blue channel value in range [0, 255].

    Returns:
        BgRGBColors: Background RGB color style.

    Example:
        >>> print(bg_rgb(255, 255, 0)("Yellow background"))
    """
    return BgRGBColors(r, g, b)