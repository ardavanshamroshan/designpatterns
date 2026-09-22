"""Liskov Substitution Principle (LSP).
The class should be substitutable for its parent class.
"""


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width  # private attribute
        self._height = height  # private attribute

    def __str__(self) -> str:
        return f"Width: {self.width}, Height: {self.height}"

    @property
    def area(self) -> int:
        return self._width * self._height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value


class Square(Rectangle):
    def __init__(self, size: int):
        super().__init__(size, size)
        
    @Rectangle.width.setter
    def width(self, value: int):
        self._width = self._height = value
        
    @Rectangle.height.setter
    def height(self, value: int):
        self._height = self._width = value

def use_it(rc: Rectangle):
    """
    This demonstrates a violation of the Liskov Substitution Principle (LSP).
    The function expects any Rectangle to behave in a way that setting height only affects the height,
    but if a Square subclass overrides the setters to keep width and height equal, assigning rc.height
    will change both dimensions. This breaks the contract expected by use_it and results in incorrect behavior.
    """

    w = rc.width
    rc.height = 10  # this will break the LSP
    expected = int(w * 10)
    actual = rc.area
    print(f"Expected: {expected}, Actual: {actual}")


def main():
    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(5)
    use_it(sq)


if __name__ == "__main__":
    main()
