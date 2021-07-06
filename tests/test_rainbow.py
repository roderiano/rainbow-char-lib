from rainbowchar import rainbow


def test_paint():
    assert rainbow.paint('hello world', '#ffffff') == '\033[38;2;255;255;255mhello world\033[0m'