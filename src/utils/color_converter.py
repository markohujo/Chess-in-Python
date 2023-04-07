from src.utils.enums.color import Color


class ColorConverter:
    @staticmethod
    def convert(color: Color) -> Color:
        return Color.BLACK if color == Color.WHITE else Color.WHITE