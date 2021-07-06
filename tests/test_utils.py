from rainbowchar import utils


def test_convert_hex_color_to_ansi():
    assert utils.convert_hex_color_to_ansi('#ffffff') == '\033[38;2;255;255;255m'   