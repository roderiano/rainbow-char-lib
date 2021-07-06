import re

def convert_hex_color_to_ansi(hex_color: str):
    if re.match(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})', hex_color):
        hex_color = hex_color.replace('#', '')
        
        rgb: tuple
        if len(hex_color) == 6:
            rgb = (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))
        else:
            rgb = (int(hex_color[0:1], 16), int(hex_color[1:2], 16), int(hex_color[2:3], 16))

        return '\033[38;2;{};{};{}m'.format(rgb[0], rgb[1], rgb[2])
    else:
        return None
