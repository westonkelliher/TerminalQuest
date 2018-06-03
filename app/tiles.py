import random

uc = unichr


SHOW_GRID = True



dirt_chars=[uc(10241),uc(10242),uc(10244),' ']


def randomTile(chars, n, grid=False):
    t =  [ [random.choice(chars) for i in range(n*2)] for i in range(n)]
    if grid:
        t[-1] = t[-1][:-2]+['_',uc(9164)]
    return t


#dirt
class DirtTile():

    def gen_graphic(self):
        self.graphic = randomTile(dirt_chars, 3, SHOW_GRID)
    
    def __init__(self):
        self.gen_graphic()


#grass        
class GrassTile():

    graphic = [['|', '|', '|', '|', '|', '|'],
               ['|', '|', '|', '|', '|', '|'],
               ['|', '|', '|', '|', '|', '|']]

    
    
