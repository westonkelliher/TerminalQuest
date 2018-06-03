import os

def subGraphic(g, x, y, w, h):
    return [line[x:x+w] for line in g[y:y+h] ]

def blit(g, surface, x, y, opaque=False):
    for i in range(len(g)):
        for j in range(len(g[0])):
            if opaque or g[i][j] != ' ':
                surface[i+x][j+y] = g[i][j]


def printGraphic(g):
    os.system('clear')
    for line in g:
        print line
