from turtle import Turtle
# dimensions of paddle:
# y.cor() + - 30
# x.cor() + - 7
class Padel(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=0.7)
        self.x_cord = 360
        self.y_cord = 0


    def left_padel(self):
        self.goto(x=-self.x_cord, y=self.y_cord)

    def right_padel(self):
        self.goto(x=+self.x_cord, y=self.y_cord)

    def left_padel_move_up(self):
        if(self.ycor() <= 250):
            self.y_cord += 30
            self.goto(x=-self.x_cord, y=self.y_cord)

    def left_padel_move_down(self):
        if (self.ycor() >= -250):
            self.y_cord -= 30
            self.goto(x=-self.x_cord, y=self.y_cord)

    def right_padel_move_up(self):
        if (self.ycor() <= 250):
            self.y_cord += 30
            self.goto(x=+self.x_cord, y=self.y_cord)

    def right_padel_move_down(self):
        if (self.ycor() >= -250):
            self.y_cord -= 30
            self.goto(x=+self.x_cord, y=self.y_cord)