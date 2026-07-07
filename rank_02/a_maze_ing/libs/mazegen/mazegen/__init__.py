# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 14:12:03 by maprunty         #+#    #+#              #
#    Updated: 2026/05/27 16:09:43 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""A-Maze-ing is a maze generation and pathfinding visualization project."""

from .config import AlgoName, Config, ConfigIO, PathAlgoName
from .errors import ConfigError, MazeError, RenderError, StartError
from .graph import Edge, Graph, GridGraph
from .grid_tools import Cell, Dir, Grid, Vec2
from .mazegenerator import MazeGenerator
from .registry import ALGOS, PICS

__all__ = [
    "MazeGenerator",
    "ALGOS",
    "PICS",
]

__all__ += [
    "Graph",
    "GridGraph",
    "Edge",
]

__all__ += [
    "Cell",
    "Grid",
    "Vec2",
    "Dir",
]

__all__ += [
    "ConfigError",
    "MazeError",
    "RenderError",
    "StartError",
]

__all__ += [
    "Config",
    "ConfigIO",
    "AlgoName",
    "PathAlgoName",
]
