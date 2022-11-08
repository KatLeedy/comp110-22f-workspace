"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730610012"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other_cell: Point) -> float:
        """Calculate the distance between the locations of two cells."""
        x_diff: float = other_cell.x - self.x
        y_diff: float = other_cell.y - self.y
        return sqrt((x_diff ** 2) + (y_diff ** 2))


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Updates the state of the cell, including location and infection status."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_immune():
            return "green"
        elif self.is_infected():
            return "red"
        else:
            return "gray" 

    def contract_disease(self) -> None:
        """Changes sickness attribute to infected."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns bool regarding whether sickness attribute is 'vulnerable'."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returns bool regarding whether sickness attribute is 'infected'."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, other_cell: Cell) -> None:
        """Infects an uninfected cell if it comes into contact with an infected cell."""
        if self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()
        elif other_cell.is_vulnerable() and self.is_infected():
            other_cell.contract_disease()

    def immunize(self) -> None:
        """Sets sickness attribute to 'immune'."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns bool regarding whether sickness attribute is 'immune'."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infections: int, immunities: int = 0):
        """Initialize the cells with random locations and directions."""
        if infections < 1 or infections > cells:
            raise ValueError("Please provide a valid for the number of initial infections. Some number of cells must begin infected.")
        elif immunities < 0 or immunities > cells:
            raise ValueError("Please provide a valid for the number of initial immunities.")
        elif infections + immunities >= cells:
            raise ValueError("The total infected and immune cells can't equal or exceed the total number of cells.")
        else:
            self.population = []
            for i in range(cells):
                start_location: Point = self.random_location()
                start_direction: Point = self.random_direction(speed)
                cell: Cell = Cell(start_location, start_direction)
                if i < infections:
                    cell.contract_disease()
                elif i < (infections + immunities):
                    cell.immunize()
                self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Checks positions of all cells and initiates contact method between two cells if they touch."""
        for i in range(len(self.population)):
            current_cell: Cell = self.population[i]
            for j in range(i + 1, len(self.population)):
                compared_cell: Cell = self.population[j]
                if current_cell.location.distance(compared_cell.location) < constants.CELL_RADIUS:
                    current_cell.contact_with(compared_cell)  