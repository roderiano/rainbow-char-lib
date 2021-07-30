from rainbowchar import rainbow


def test_paint():
    tested_text = rainbow.paint('hello', foreground='#2DCA47') + ' '
    ansi_text = '\033[38;2;45;202;71mhello\033[0m '

    tested_text += rainbow.paint('world ', background='#BD3A32')
    ansi_text += '\033[48;2;189;58;50mworld \033[0m'
    
    tested_text += rainbow.paint(':)', '#2DCA47', '#BD3A32')
    ansi_text += '\033[48;2;189;58;50m\033[38;2;45;202;71m:)\033[0m\033[0m'

    assert tested_text == ansi_text