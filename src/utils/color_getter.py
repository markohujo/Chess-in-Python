from src.utils.enums.color import Color


class ColorGetter:
    @staticmethod
    def get(color_str: str) -> Color:
        """Return color from the given string"""
        color_str = color_str.lower()
        if color_str == 'white':
            return Color.WHITE
        if color_str == 'black':
            return Color.BLACK
        raise Exception
