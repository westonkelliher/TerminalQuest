from app.data_loader import Animation


class CharacterAnimation():

    def nextGraphic(self):
        if self.direction == 'up':
            return self.animation_up.nextGraphic()
        elif self.direction == 'down':
            return self.animation_down.nextGraphic()
        elif self.direction == 'left':
            return self.animation_left.nextGraphic()
        elif self.direction == 'right':
            return self.animation_right.nextGraphic()
        else:
            print("error: "+self.direction+"is not a valid direction")

    def __init__(self, width, height, file_name,
                 up_sequence, down_sequence, left_sequence, right_sequence):
        self.direction = 'up'
        self.animation_up = Animation(width, height, file_name, up_sequence)
        self.animation_down = Animation(width, height, file_name, down_sequence)
        self.animation_left = Animation(width, height, file_name, left_sequence)
        self.animation_right = Animation(width, height, file_name, right_sequence)
