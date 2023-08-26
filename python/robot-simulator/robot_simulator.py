# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x = x_pos
        self.y = y_pos
        self.coordinates = (x_pos, y_pos)

    def advance(self):
        moves = {EAST: 1, NORTH: 1, WEST: -1, SOUTH: -1}
        if self.direction in (EAST, WEST):
            self.x += moves[self.direction]
        else:
            self.y += moves[self.direction]
        self.coordinates = (self.x, self.y)

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def move(self, type):
        for x in type:
            if x == 'A':
                self.advance()
            elif x == 'L':
                self.turn_left()
            else:
                self.turn_right()

