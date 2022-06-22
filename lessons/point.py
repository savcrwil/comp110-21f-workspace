"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float
    
    def __init__(self, x: float, y: float):
        """Initialize a point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiple components by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point."""
        x: float = self.x * factor
        y: float = self.y * factor
        p: Point = Point(x, y)
        return p

    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        print("__mul__ was called")
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python."""
        return f"Point({self.x}, {self.y})"


p0: Point = Point(1.0, 2.0)
p1: Point = p0 * 2.0
p2: Point = p0 + p1
print(p0)
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1)
print(p1_repr)
print(f"p2: {p2}")

print(p0[0])
print(p0[1])