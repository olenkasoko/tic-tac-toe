import enum
import re
from dataclasses import dataclass
from functools import cached_property


# Two singleton instances of the Mark class
class Mark(enum.StrEnum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Mark":
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

# Defined as frozen data class to make its instances immutable
@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    def __post_init__(self) -> None:
        if not re.match(r"^[\sXO]{9}$", self.cells):
            raise ValueError("Must contain 9 cells of: X, O, or space")

    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")

    @cached_property
    def o_count(self) -> int:
        return self.cells.count("O")

    @cached_property
    def empty_count(self) -> int:
        return self.cells.count(" ")

@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

@dataclass(frozen=True)
class GameState:
    grid: Grid
    starting_mark: Mark = Mark("X")
    @cached_property
    def current_mark(self) -> Mark:
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        else:
            return self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.empty_count == 9

    @cached_property
    def game_over(self) -> bool:
        return self.winner is not None or self.tie

    @cached_property
    def tie(self) -> bool:
        return self.grid.empty_count==0 and self.winner is None


