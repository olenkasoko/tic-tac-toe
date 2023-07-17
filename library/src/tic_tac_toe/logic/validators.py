
from __future__ import annotations
from typing import TYPE_CHECKING

from tic_tac_toe.logic.exceptions import InvalidGameState

if TYPE_CHECKING: # Runs false at runtime
    from tic_tac_toe.logic.models import Grid, GameState, Mark

import re
def validate_grid(grid:Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Must contain 9 cells of: X, O, or space")


def validate_number_of_marks(grid):
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Wrong number of Xs and Os")


def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    valid = True
    if grid.x_count > grid.o_count and starting_mark != "X":
        valid = False
    elif grid.o_count > grid.x_count and starting_mark != "O" :
        valid = False
    if not valid:
        raise InvalidGameState("Wrong starting mark")

def validate_winner(grid: Grid, starting_mark: Mark, winner: Mark | None) -> None:
    if winner == "X":
        if starting_mark == "X":
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Incorrect amount of Xs")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Incorrect amount of Xs")
    elif winner == "O":
        if starting_mark == "O":
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("Incorrect amount of Os")
        else:
            if grid.o_count != grid.x_count:
                raise InvalidGameState("Incorrect amount of Os")


def validate_game_state(game_state:GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(game_state.grid, game_state.starting_mark, game_state.winner
    )
