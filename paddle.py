from turtle import Turtle

EDGE_Y = 300


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.speed('fastest')
        self.x_pos = x_pos
        self.y_pos = 0
        self.draw_paddle()
        self.penup()

    def draw_paddle(self):
        self.penup()
        self.goto(self.x_pos, self.y_pos)
        self.pendown()
        # all turtles starts as 20x20. this makes it 100x20
        self.shapesize(5, 1)

    def up(self):
        y_coord = self.ycor()
        if y_coord < EDGE_Y - 55:
            self.goto(self.xcor(), y_coord + 20)

    def down(self):
        y_coord = self.ycor()
        if y_coord > - EDGE_Y + 55:
            self.goto(self.xcor(), y_coord - 20)
