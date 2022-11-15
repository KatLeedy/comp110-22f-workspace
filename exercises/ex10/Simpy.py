"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730610012"


class Simpy:
    """A class of utility methods for working with sequences of numerical data."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructs a Simpy object and initiates its values attribute to a list of floats."""
        self.values = values
    
    def __repr__(self) -> str:
        """Returns a string representation of a Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, value: float, quant: int) -> None:
        """Fills the Simpy object with a set number of a certain float value."""
        self.values.clear()
        for _ in range(quant):
            self.values.append(value)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the values attribute with a range of float values from start (inclusive) to stop (not inclusive), by an optional step."""
        assert step != 0.0
        self.values.clear()
        i: float = start
        if step > 0.0:
            while i < stop:
                self.values.append(i)
                i += step
        else:
            while i > stop:
                self.values.append(i)
                i += step
    
    def sum(self) -> float:
        """Adds up all values in the values attribute."""
        total: float = sum(self.values)
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the corresponding value of rhs to each item of the values attribute."""
        total: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                total.values.append(self.values[i] + rhs.values[i])
        else:
            for value in self.values:
                total.values.append(value + rhs)
        return total

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raises each item of the values attribute to the power of the corresponding value of rhs."""
        total: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                total.values.append(self.values[i] ** rhs.values[i])
        else:
            for value in self.values:
                total.values.append(value ** rhs)
        return total

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a mask of bool indicating whether the corresponding value of rhs equals each item of the values attribute."""
        mask: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            for value in self.values:
                if value == rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a mask of bool indicating whether each item of the values attribute is greater than the corresponding value of rhs."""
        mask: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            for value in self.values:
                if value > rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns an indicated value of values or a new Simpy object with items that correspond to 'True' in a mask."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            masked: Simpy = Simpy([])
            for i in range(len(self.values)):
                if rhs[i]:
                    masked.values.append(self.values[i])
            return masked