import app.display as display
import app.graphic as graphic
from app.data_loader import Animation
from app.tiles import DirtTile, GrassTile
from app.character import CharacterAnimation
from app.gamestate import GameState
import app.grid as grid
import time

game_state = GameState(50,50)


cTall = CharacterAnimation(6,5, 'tall', [[0,0],[1,0]],[[0,1],[1,1]],[[0,3],[1,3]],[[0,2],[1,2]])
cShort = CharacterAnimation(7,4, 'player', [[0,0],[1,0]],[[0,1],[1,1]],[[0,3],[1,3]],[[0,2],[1,2]])

d = DirtTile()
g = GrassTile()
print(d.graphic)
print(g.graphic)
graphic.printGraphic(d.graphic)
graphic.printGraphic(g.graphic)
for i in range(1000):
    display.printScreen(game_state, 48, 20)
    game_state.camera_y += 1
    if i%20 >= 10 and i%5 == 0:
        game_state.camera_x += 2
    if i%20 < 10 and i%5 == 0:
        game_state.camera_x -= 2
    time.sleep(.1)

'''
for x in range(100):
    graphic.printGraphic(cTall.nextGraphic())
    time.sleep(.1)
    if x%40 == 0:
        cTall.direction = 'up'
    elif x%40 == 10:
        cTall.direction = 'right'
    elif x%40 == 20:
        cTall.direction = 'down'
    elif x%40 == 30:
        cTall.direction = 'left'
'''
