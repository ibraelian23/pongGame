from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.x_range = 0
        self.y_range = 0
        self.blah = 0
        self.random_movement()

    def random_movement(self):
        self.x_range = random.choice([-380, 380])
        self.y_range = random.randint(-290, 290)
        self.goto(x=0, y=0)
        self.setheading(self.towards(x=self.x_range, y=self.y_range))
        self.shapetransform(0.8, 0.0, -0.0, 0.8)
        self.tilt(- self.towards(x=self.x_range, y=self.y_range))

    def bounce_movement(self, y_cord):
        if y_cord >= 280:
            if(self.heading() >=0 and self.heading() <=90):
                self.blah = random.randint(270, 360)
                self.setheading(self.blah)
                self.shapetransform(0.8, 0.0, -0.0, 0.8)
                self.tilt(- self.blah)
            elif (self.heading() >= 90 and self.heading() <= 180):
                self.blah = random.randint(180, 270)
                self.setheading(self.blah)
                self.shapetransform(0.8, 0.0, -0.0, 0.8)
                self.tilt(- self.blah)
        elif y_cord <= -280:
            if (self.heading() >= 180 and self.heading() <= 270):
                self.blah = random.randint(90, 180)
                self.setheading(self.blah)
                self.shapetransform(0.8, 0.0, -0.0, 0.8)
                self.tilt(- self.blah)
            elif (self.heading() >= 270 and self.heading() <= 360):
                self.blah = random.randint(0, 90)
                self.setheading(self.blah)
                self.shapetransform(0.8, 0.0, -0.0, 0.8)
                self.tilt(- self.blah)

    def collision(self, x_cord):
        if x_cord <= 0:
            if(self.heading() >=90 and self.heading() <=180):
                self.blah = random.randint(0, 90)
                self.setheading(self.blah)
                self.shapetransform(0.8, 0.0, -0.0, 0.8)
                self.tilt(- self.blah)
            elif (self.heading() >= 180 and self.heading() <= 270):
                self.blah = random.randint(270, 360)
                self.setheading(self.blah)
                self.shapetransform(0.8, 0.0, -0.0, 0.8)
                self.tilt(- self.blah)
        elif x_cord >= 0:
            if (self.heading() >= 0 and self.heading() <= 90):
                self.blah = random.randint(90, 180)
                self.setheading(self.blah)
                self.shapetransform(0.8, 0.0, -0.0, 0.8)
                self.tilt(- self.blah)
            elif (self.heading() >= 270 and self.heading() <= 360):
                self.blah = random.randint(180, 270)
                self.setheading(self.blah)
                self.shapetransform(0.8, 0.0, -0.0, 0.8)
                self.tilt(- self.blah)

    def move(self):
        self.forward(28)

