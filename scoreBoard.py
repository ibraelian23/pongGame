from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.creat_right_score()
        self.creat_left_score()
        self.create_dashed_line()

    def create_dashed_line(self):
        self.pensize(width=5)
        self.penup()
        self.goto(x=0, y=-300)
        self.setheading(90)
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def creat_left_score(self):
        self.goto(x=-200, y=250)
        self.write(arg=f"{self.l_score}", align="center", move=False, font=("Arial", 28, "normal"))

    def creat_right_score(self):
        self.goto(x=200, y=250)
        self.write(arg=f"{self.r_score}", align="center", move=False, font=("Arial", 28, "normal"))

    def increase_right_score(self):
        self.r_score += 1
        self.clear()
        self.create_dashed_line()
        self.creat_left_score()
        self.creat_right_score()

    def increase_left_score(self):
        self.l_score += 1
        self.clear()
        self.create_dashed_line()
        self.creat_right_score()
        self.creat_left_score()


