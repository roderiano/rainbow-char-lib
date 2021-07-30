from rainbowchar import utils, exceptions

def paint(text: str, foreground: str=None, background: str=None):
    """
    Format text string with style parameters.

    Parameters:
    text (str): Text to stylize
    foreground (str): Hexadecimal color of foreground
    background (str): Hexadecimal color of background

    Returns:
    str: return text formatted in ANSI code

   """
    result: str
    
    if foreground:
        rgb = utils.convert_hex_color_to_rgb(foreground)
        
        if not rgb:
            raise exceptions.InvalidRainbowHexadecimalColor(foreground)
            
        r, g, b = rgb

        result = '\033[38;2;{};{};{}m{}\033[0m'.format(r, g, b, text)

    if background:
        rgb = utils.convert_hex_color_to_rgb(background)
        
        if not rgb:
            raise exceptions.InvalidRainbowHexadecimalColor(background)
            
        r, g, b = rgb

        result = '\033[48;2;{};{};{}m{}\033[0m'.format(r, g, b, result if foreground else text)

    # print(result)
    
    return result