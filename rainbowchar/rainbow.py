from rainbowchar import utils, exceptions

def paint(text: str, color: str=None):
    """
    Format text string with style parameters.

    Parameters:
    text (str): Text to stylize
    color (str): Hexadecimal color of text

    Returns:
    str: return text formatted in ANSI code

   """
    result: str
    
    if color:
        ansi_code = utils.convert_hex_color_to_ansi(color)
        if ansi_code:
            result = '{}{}\033[0m'.format(ansi_code, text)
        else:
            raise exceptions.InvalidRainbowHexadecimalColor(color)

    return result
