import app.display as display
import app.graphic as graphic
from app.data_loader import Animation
from app.tiles import DirtTile, GrassTile
import app.grid as grid
import time


N=10
area = [ [DirtTile() for i in range(N)] for i in range(N)]

area[4][4] = GrassTile()
'''
for i in range(1000):
    display.printScreen(area, 48, 20, 30+i*2, 30+(i/10))
    time.sleep(.1)
'''

x1 = Animation(7,4, 'player', [[0,0],[1,0]])
x2 = Animation(7,4, 'player', [[0,2],[1,2]])
x3 = Animation(7,4, 'player', [[0,1],[1,1]])
x4 = Animation(7,4, 'player', [[0,3],[1,3]])


for x in range(10):
    for i in range(10):
        graphic.printGraphic(x1.nextGraphic())
        time.sleep(.1)
    for i in range(10):
        graphic.printGraphic(x2.nextGraphic())
        time.sleep(.1)
    for i in range(10):
        graphic.printGraphic(x3.nextGraphic())
        time.sleep(.1)
    for i in range(10):
        graphic.printGraphic(x4.nextGraphic())
        time.sleep(.1)        




