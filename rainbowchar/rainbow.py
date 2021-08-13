from rainbowchar import utils, exceptions

def paint(text: str, foreground: str=None, background: str=None, bold: bool=False, italic: bool=False, underline: bool=False):
    """
    Format text string with style parameters.

    Parameters:
    text (str): Text to stylize
    foreground (str): Hexadecimal color of foreground
    background (str): Hexadecimal color of background
    bold (bool): Bold flag
    italic (bool): Italic flag
    underline (bool): Underline flag

    Returns:
    str: return text formatted in ANSI code

   """
    result = '\033['
    
    if foreground:
        rgb = utils.convert_hex_color_to_rgb(foreground)
        
        if not rgb:
            raise exceptions.InvalidRainbowHexadecimalColor(foreground)
            
        r, g, b = rgb

        result += '38;2;{};{};{};'.format(r, g, b)

    if background:
        rgb = utils.convert_hex_color_to_rgb(background)
        
        if not rgb:
            raise exceptions.InvalidRainbowHexadecimalColor(background)
            
        r, g, b = rgb

        result += '48;2;{};{};{};'.format(r, g, b)

    if bold:
        result += '1;'.format(result)
    
    if italic:
        result += '3;'.format(result)

    if underline:
        result += '4;'.format(result)
    
    if result != '\033[':
        result = result[:-1]

    result += 'm{}\033[0m'.format(text)
    
    return result