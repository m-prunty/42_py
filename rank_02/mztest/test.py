from mazegen import Config, Grid, MazeGenerator

cfg = Config(
    width=12, height=12, entry=(0, 0), exit=(11, 11), gen_algo="kruskal"
)

grid = Grid(cfg.width, cfg.height)
grid.fill_empty_grid()

mg = MazeGenerator(grid, cfg)
mg.gen_grid(cfg.gen_algo)  # Generate a maze with selected algorithm
mg.gen_path(cfg.path_algo)  # Generate a maze with selected algorithm

print(grid)  # Grid/wall output
