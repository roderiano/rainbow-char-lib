import re

def convert_hex_color_to_rgb(hex_color: str):
    """
    Convert hexadecimal color to RGB tuple.

    Parameters:
    hex_color (str): hexadecimal color formatted (Example: #FFFFFF)

    Returns:
    str | None: return ANSI code or None if hex_color is not valid

   """

    if re.match(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})', hex_color):
        hex_color = hex_color.replace('#', '')
        
        rgb: tuple
        if len(hex_color) == 6:
            rgb = (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))
        else:
            rgb = (int(hex_color[0:1], 16), int(hex_color[1:2], 16), int(hex_color[2:3], 16))

        return rgb
    else:
        return None
