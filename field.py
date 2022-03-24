from turtle import Turtle

EDGE_Y = 300


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.pensize(3)
        self.new_distance = round(EDGE_Y*2/16)
        self.draw_dashed_line()

    def draw_dashed_line(self):
        self.penup()
        self.goto(0, EDGE_Y)
        self.setheading(270)
        for i in range(self.new_distance):
            self.forward(8)
            self.penup()
            self.forward(8)
            self.pendown()
