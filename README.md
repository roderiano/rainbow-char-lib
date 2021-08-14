# rainbow-char-lib
RainbowChar is a lib that stylizes text by formatting in ANSI escape code. **It only supports true color terminals**. 

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rainbow-char-lib.

```bash
pip install rainbowchar
```

## Usage
A simple example of a hello world.

``` python
from rainbowchar.rainbow import paint

def showcase():
    hello = paint('hello', foreground='#00FF28', italic=True)
    world = paint('world!', foreground='#00FF28', italic=True)

    print('{} {}'.format(hello, world))
    print(paint(':D', foreground='#000000', background='#FFFF0A', bold=True))


if __name__ == '__main__':
    showcase()

```


## Parameters
Function paint parameter list.

| Parameter  | Description                     | Type | Default |
|:-----------|:--------------------------------|:----:|:-------:|
| text       | Text to stylize                 | str  |   None  |
| foreground | Hexadecimal color of foreground | str  |   None  |
| background | Hexadecimal color of background | str  |   None  |
| bold       | Bold flag                       | bool |   False |
| italic     | Italic flag                     | bool |   False |
| underline  | Underline flag                  | bool |   False |


## License
[MIT](https://choosealicense.com/licenses/mit/)
