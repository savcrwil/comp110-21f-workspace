"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730393320"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """String representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, repeats: int) -> None:
        """Fill a values list by mutating object called on."""
        self.values = []
        i: int = 0
        while i < repeats:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Delegate this algorithm to the built-in sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] + rhs.values[i])
                i += 1
            return Simpy(result)
        else:
            for item in self.values:
                result.append(item + rhs)
            return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for exponentiation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            for item in self.values:
                result.values.append(item ** rhs)
        return result

    def __eq__(self, x: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the equality of items in values to a float or another Simpy."""
        result: list[bool] = []
        if isinstance(x, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] == x:
                    result.append(True)
                else:
                    result.append(False)
                i += 1       
        else:
            i: int = 0
            while i < len(self.values):
                if self.values[i] == x.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __gt__(self, x: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on whether or not items in a list are greater than a float or items in another list."""
        result: list[bool] = []
        if isinstance(x, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > x:
                    result.append(True)
                else:
                    result.append(False)
                i += 1      
        else:
            i: int = 0
            while i < len(self.values):
                if self.values[i] > x.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads subscription notation to filter with a mask."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            new_list: list[float] = []
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    new_list.append(self.values[i])
                i += 1
            return Simpy(new_list)