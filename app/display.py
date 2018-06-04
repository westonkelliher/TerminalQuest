import os
import app.graphic as graphic
from app.character import CharacterAnimation

cShort = CharacterAnimation(7,4, 'player', [[0,0],[1,0]],[[0,1],[1,1]],[[0,3],[1,3]],[[0,2],[1,2]])
cShort.direction = 'down'
cTall = CharacterAnimation(6,5, 'tall', [[0,0],[1,0]],[[0,1],[1,1]],[[0,3],[1,3]],[[0,2],[1,2]])
cTall.direction = 'down'


def printScreen(game_state, width, height):
    os.system('clear')
    x = game_state.camera_x
    y = game_state.camera_y
    char_grid = graphic.combineGraphics([ [tile.graphic for tile in row] for row in game_state.local_terrain])
    sub_grid = graphic.subGraphic(char_grid, x-(width/2), y-(height/2), width, height)
    with_dude = graphic.blit(cShort.nextGraphic(), sub_grid, 8,7)
    with_other_dude = graphic.blit(cTall.nextGraphic(), sub_grid, 7,30)
    graphic.printGraphic(with_dude)
