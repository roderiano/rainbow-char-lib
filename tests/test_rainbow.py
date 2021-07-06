from rainbowchar import rainbow


def test_text_color():
    print(rainbow.rainbow_test('ok'))
    assert rainbow.rainbow_test('ok') == '\033[91m ok \033[0m'