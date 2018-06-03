import os
import app.grid as grid


def printScreen(tile_grid, width, height, x, y):
    os.system('clear')
    char_grid = grid.combineGrids([ [tile.graphic for tile in row] for row in tile_grid])
    grid.print_grid(grid.subgrid(char_grid, x-(width/2), y-(width/2), width, height))
