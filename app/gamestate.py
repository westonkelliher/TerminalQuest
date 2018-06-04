import app.data_loader as loader
from app.tiles import DirtTile, GrassTile

LOAD_RADIUS = 16

def tile(c):
    if c == 'g':
        return GrassTile()
    elif c == 'd':
        return DirtTile()

class GameState():

    def load_local(self):
        terrain_timage = loader.loadData('terrain')
        self.local_terrain = [ [tile(c) for c in row[:-1]] for row in terrain_timage[:-1]]
        self.local_objects = []
    
    def __init__(self, x, y):
        self.camera_x = x
        self.camera_y = y
        self.load_radius = 16
        self.load_local()
