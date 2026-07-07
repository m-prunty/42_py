#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_mazegen.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/23 20:30:49 by maprunty         #+#    #+#              #
#    Updated: 2026/05/27 16:42:44 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""Test the MazeGenerator class."""

from typing import cast

import pytest

from mazegen import (
    ALGOS,
    AlgoName,
    Config,
    ConfigError,
    Grid,
    MazeGenerator,
    PathAlgoName,
    Vec2,
)


def test_basic_generation() -> None:
    """Generates a maze of correct dimensions with default config."""
    cfg = Config(
        width=10, height=10, entry=Vec2(0, 0), exit=Vec2(9, 9), gen_algo="dfs"
    )
    grid = Grid(cfg.width, cfg.height)
    mg = MazeGenerator(grid, cfg)
    mg.gen_grid(cfg.gen_algo)
    assert grid.width == 10
    assert grid.height == 10
    for row in grid.grid:
        assert len(row) == 10


def test_perfect_maze() -> None:
    """Maze is perfect if PERFECT=True."""
    cfg = Config(
        width=8, height=8, perfect=True, entry=Vec2(0, 0), exit=Vec2(7, 7)
    )
    grid = Grid(cfg.width, cfg.height)
    mg = MazeGenerator(grid, cfg)
    mg.gen_grid(cfg.gen_algo)
    mg.gen_path(cfg.path_algo)
    assert grid.path[0] == grid[0, 0].loc
    assert grid.path[-1] == grid[7, 7].loc


def test_invalid_entry_exit() -> None:
    """Raises ConfigError if entry/exit is out of bounds."""
    with pytest.raises(ConfigError):
        Config(width=5, height=5, entry=Vec2(6, 0), exit=Vec2(4, 4))
    with pytest.raises(ConfigError):
        Config(width=5, height=5, exit=Vec2(2, 8))


def test_all_algorithms_supported() -> None:
    """Each algorithm generates a valid maze without error."""
    algos: list[AlgoName] = [
        cast(AlgoName, a) for a in ALGOS if not "dijkstra"
    ]

    for algo in algos:
        cfg = Config(
            width=8, height=8, gen_algo=algo, entry=Vec2(0, 0), exit=Vec2(7, 7)
        )
        grid = Grid(cfg.width, cfg.height)
        mg = MazeGenerator(grid, cfg)
        mg.gen_grid(cfg.gen_algo)


def test_pathfinding_algorithms() -> None:
    """Each supported pathfinding algorithm finds a path."""
    algos: list[PathAlgoName] = ["dijkstra"]

    for algo in algos:
        cfg = Config(
            width=7,
            height=7,
            path_algo=algo,
            entry=Vec2(0, 0),
            exit=Vec2(6, 6),
        )
        grid = Grid(cfg.width, cfg.height)
        mg = MazeGenerator(grid, cfg)
        mg.gen_grid(cfg.gen_algo)
        mg.gen_path(cfg.path_algo)
        # There should always be a path from entry to exit
        assert grid.path[0] == grid[cfg.entry].loc
        assert grid.path[-1] == grid[cfg.exit].loc


def test_seed_reproducibility() -> None:
    """Given the same seed, two mazes are identical."""
    cfg1 = Config(
        width=6, height=6, seed=1234, entry=Vec2(0, 0), exit=Vec2(5, 5)
    )
    cfg2 = Config(
        width=6, height=6, seed=1234, entry=Vec2(0, 0), exit=Vec2(5, 5)
    )
    grid1 = Grid(cfg1.width, cfg1.height)
    grid2 = Grid(cfg2.width, cfg2.height)
    mg1 = MazeGenerator(grid1, cfg1)
    mg2 = MazeGenerator(grid2, cfg2)
    mg1.gen_grid(cfg1.gen_algo)
    mg2.gen_grid(cfg2.gen_algo)
    assert [[cell for cell in row] for row in grid1] == [
        [cell for cell in row] for row in grid2
    ]
