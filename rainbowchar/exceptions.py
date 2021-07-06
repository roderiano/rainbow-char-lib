class InvalidRainbowHexadecimalColor(Exception):
    """
    Exception raised for errors in hexadecimal color convertion.

    Attributes:
        color: input color which caused the error
        message: explanation of the error
    """

    def __init__(self, color, message="Color is not valid"):
        self.color = color
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.color} -> {self.message}'