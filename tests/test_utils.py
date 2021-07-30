from rainbowchar import utils


def test_convert_hex_color_to_ansi():
    assert utils.convert_hex_color_to_rgb('#ffffff') == (255, 255, 255)
