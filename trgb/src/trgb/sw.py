class SW:
    """
    Wrapper around ANSI escape codes for terminal text styling.

    The class allows:
    - combining styles and colors using the `+` operator
    - applying styles to text by calling the object as a function

    Example:
        >>> from sw import red, bold
        >>> print((red + bold)("Hello"))
    """

    RESET = "\033[0m"

    def __init__(self, *code: str):
        """
        Initializes a style object.

        Args:
            *code (str): ANSI codes without the `\033[` prefix and trailing `m`.
                For example: `"31"` (red), `"1"` (bold).

        Example:
            >>> style = SW('31', '1')  # red + bold
        """
        self.code = tuple(code)

    def __add__(self, other):
        """
        Combines two `SW` objects.

        Args:
            other (SW): Another style object.

        Returns:
            SW: A new `SW` instance with merged ANSI codes.
        """
        if hasattr(other, "code"):
            return SW(*(self.code + other.code))
        return NotImplemented

    def __radd__(self, other):
        """
        Combines two `SW` objects in reverse order.

        Enables correct behavior regardless of operand order
        when using the `+` operator.

        Args:
            other (SW): Another style object.

        Returns:
            SW: A new `SW` instance with merged ANSI codes.
        """
        if hasattr(other, "code"):
            return SW(*(other.code + self.code))
        return NotImplemented

    def __call__(self, *args, sep: str = '', reset: bool = True) -> str:
        """
        Applies the style to the given text.

        Args:
            *args: Values converted to strings and joined into the final text.
            sep (str, optional): Separator between arguments.
                Defaults to an empty string.
            reset (bool, optional): Whether to reset styles at the end.
                Defaults to `True`.

        Returns:
            str: A string wrapped with ANSI escape codes.

        Example:
            >>> print(red("Error"))
            >>> print((bold + underline)("Important"))
        """
        text = sep.join(map(str, args))
        codes = ";".join(self.code)
        prefix = f"\033[{codes}m"
        suffix = self.RESET if reset else ''
        return f"{prefix}{text}{suffix}"
