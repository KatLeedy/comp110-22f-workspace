"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor
    
    # def scale(self, factor: float) -> Point:
    #     """Immutable: multiplies components by factor."""
    #     return Point(self.x * factor, self.y * factor)

    # new magic method __mul__ does the function of scale()

    def __str__(self) -> str:
        """Produce a str representation of a Point for humans."""
        return(f"({self.x}, {self.y})")
    
    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"
        # repr is more for representing code as strings to import/export objects into different files
    
    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for a Point multiplied by a float."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    # Could use this to overload subscription notation, although it is not good design in this case.
    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


p0: Point = Point(1.0, 2.0)
p1: Point = p0 * 2.0
print(p0)
# str() method looks for the __str__ magic method to represent an object as a str
# print() calls str() behind the scenes
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1)
print(p1_repr)

p_total: Point = p0 + p1
print(p_total)

print(p_total[0])