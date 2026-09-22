"""Open Closed Principle (OCP), Separation of Concerns (SOC).
The class should be open for extension but closed for modification.
"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products: list[Product], color: Color) -> list[Product]:
        return [p for p in products if p.color == color]

    def filter_by_size(self, products: list[Product], size: Size) -> list[Product]:
        return [p for p in products if p.size == size]

    def filter_by_size_and_color(self, products: list[Product], size: Size, color: Color) -> list[Product]:
        return [p for p in products if p.size == size and p.color == color]


# Enterprise patterns: Specification
class Specification:
    def is_satisfied(self, item: Product) -> bool:
        pass

    def __and__(self, other: Specification) -> Specification:  # pyright: ignore[reportUndefinedVariable]
        return AndSpecification(self, other)


class Filter:
    def filter(self, items: list[Product], spec: Specification) -> list[Product]:
        pass


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args: Specification):
        self.args = args

    def is_satisfied(self, item: Product) -> bool:
        return all(spec.is_satisfied(item) for spec in self.args)


class BetterFilter(Filter):
    def filter(self, items: list[Product], spec: Specification) -> list[Product]:
        return [item for item in items if spec.is_satisfied(item)]


def main():
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print("Green products (old):")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    print("Green products (new):")
    pf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    for p in pf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products:")
    bf = BetterFilter()
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")

    print("Large blue products:")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")


if __name__ == "__main__":
    main()
