import app.graphic as graphic
import codecs


def loadSpriteSheet(file_name):
    f = codecs.open('./app/graphics/'+file_name, encoding='utf-8', mode='r')
    content = f.readlines()
    f.close()
    return content


class Animation():

    def nextGraphic(self):
        g = graphic.subGraphic(self.sprite_sheet,
                           self.sequence[self.step][0]*self.width,
                           self.sequence[self.step][1]*self.height,
                           self.width,
                           self.height)
        self.step += 1
        if self.step >= len(self.sequence):
            self.step = 0
        return g

    def __init__(self, width, height, file_name, sequence):
        self.width = width
        self.height = height
        self.sprite_sheet = loadSpriteSheet(file_name)
        self.sequence = sequence
        self.step = 0
