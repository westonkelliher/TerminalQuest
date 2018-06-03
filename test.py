import app.display as display
from app.tiles import DirtTile, GrassTile
import app.grid as grid
import time


N=10
area = [ [DirtTile() for i in range(N)] for i in range(N)]

area[4][4] = GrassTile()

for i in range(1000):
    display.printScreen(area, 48, 20, 30+i*2, 30+(i/10))
    time.sleep(.1)



