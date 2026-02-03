"""
Public API for the `trgb` text styling package.

This module exposes the high-level, user-facing API for terminal text
styling using ANSI escape codes.
"""

from .colors import red, green, yellow, black, blue, magenta, cyan, white, gray, bright_blue, bright_cyan, bright_green, bright_magenta, bright_red, bright_white, bright_yellow, bg_black, bg_blue, bg_cyan, bg_gray, bg_green, bg_magenta, bg_red, bg_white, bg_yellow, bright_bg_magenta, bright_bg_blue, bright_bg_cyan, bright_bg_green, bright_bg_red, bright_bg_white, bright_bg_yellow
from .styles import bold, dim, italic, underline, blink, blink_fast, reverse, hidden, strikethrough
from .colors256 import custom_color, custom_bg
from .rgb import rgb, bg_rgb

__all__ = ['red', 'green', 'yellow', 'black', 'blue', 'magenta', 'cyan', 'white', 'gray', 'bright_blue', 'bright_cyan', 'bright_green', 'bright_magenta', 'bright_red', 'bright_white', 'bright_yellow', 'bg_black', 'bg_blue', 'bg_cyan', 'bg_gray', 'bg_green', 'bg_magenta', 'bg_red', 'bg_white', 'bg_yellow', 'bright_bg_magenta', 'bright_bg_blue', 'bright_bg_cyan', 'bright_bg_green', 'bright_bg_red', 'bright_bg_white', 'bright_bg_yellow', 'bold', 'dim', 'italic', 'underline', 'blink', 'blink_fast', 'reverse', 'hidden', 'strikethrough', 'custom_color', 'custom_bg', 'rgb', 'bg_rgb']