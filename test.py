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

x = Animation(7,4, 'player', [[0,1],[1,1]])

for i in range(20):
    graphic.printGraphic(x.nextGraphic())
    time.sleep(.1)




