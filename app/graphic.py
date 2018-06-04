from __future__ import print_function
import os
import sys


def subGraphic(g, x, y, w, h):
    return [line[x:x+w] for line in g[y:y+h] ]

def injectString(line, inj, i):
    line_l = list(line)
    inj_l = list(inj)
    for k in range(len(inj)):
        if inj_l[k] != '@':
            line_l[i+k] = inj_l[k]
    return ''.join(line_l)

def blit(g, surface, x, y):
    for i in range(len(g)):
        if i+x >= len(surface):
            return surface
        surface[i+x] = injectString(surface[i+x], g[i], y)
    return surface

def combineGraphics(grid):
    return concat_graphics_v([concat_graphics_h(grid[i]) for i in range(len(grid))])

def concat_graphics_h(Gs):
    end_graphic = Gs[0]
    for g in Gs[1:]:
        for i in range(len(g)):
            end_graphic[i] += g[i]
    return end_graphic

def concat_graphics_v(Gs):
    end_graphic = Gs[0]
    for g in Gs[1:]:
        end_graphic += g
    return end_graphic

def printGraphic(g):
    os.system('clear')
    outS = ''
    for line in g:
        outS += line+'\n'
    print(outS)
    sys.stdout.flush()
