from __future__ import print_function


def subgrid(grid, x, y, w, h):
    end_grid = grid[y:y+h]
    for i in range(len(end_grid)):
        end_grid[i] = end_grid[i][x:x+w]
    return end_grid



def combineGrids(gridArr):
    return concat_grids_v([concat_grids_h(gridArr[i]) for i in range(len(gridArr))])

def concat_grids_h(grids):
    end_grid = grids[0]
    for g in grids[1:]:
	for i in range(len(g)):
	    end_grid[i] += g[i]
    return end_grid

def concat_grids_v(grids):
    end_grid = grids[0]
    for g in grids[1:]:
	end_grid += g
    return end_grid


def print_grid(g):
    for row in g:
        for elem in row:
	    print(elem,end='')
	print()
				
