from turtle import Turtle, Screen
from padel import Padel
from ball import Ball
from scoreBoard import Score
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()

right_padel = Padel()
right_padel.right_padel()
left_padel = Padel()
left_padel.left_padel()

score = Score()

screen.listen()
screen.onkeypress(fun=left_padel.left_padel_move_up, key="Up")
screen.onkeypress(fun=left_padel.left_padel_move_down, key="Down")
screen.onkeypress(fun=right_padel.right_padel_move_up, key="w")
screen.onkeypress(fun=right_padel.right_padel_move_down, key="s")

# touch the right or left walls => (lose game) : range of x_cordinate for the ball(-380, +380)


# touch the up or down walls => (ball rebounces) : range of y_coordinates:
#     if ball hits (up wall) then the ball should bounce in a range of y_coordinate < + 290
#     if ball hits (down wall) then the ball should bounce in a range of y_coordinate > - 290

# the ball's random movement inside the canvas when the game starts
#
# ball.random_movement()

game_is_on = True
while (game_is_on):
    screen.update()
    time.sleep(0.1)
    ball.move()

# if the ball hits the east or west side of the wall => score Changes
    if(ball.xcor() >= 380) :
        ball.random_movement()
        score.increase_left_score()
    elif(ball.xcor() <= -380) :
        ball.random_movement()
        score.increase_right_score()

# if the ball hits the north or south side of the wall => ball bounces
    if (ball.ycor() +8 >= 280 or ball.ycor() -8 <= -280):
        ball.bounce_movement(ball.ycor())

# if the ball hits the padells => ball bounces
    if (ball.ycor() >= (left_padel.ycor() -30) and ball.ycor() <= left_padel.ycor() +30) and ball.xcor() -7 < -340:
        ball.collision(ball.xcor())
    elif (ball.ycor() >= (right_padel.ycor() -30) and ball.ycor() <= right_padel.ycor() +30) and ball.xcor() +7 > 340:
        ball.collision(ball.xcor())


screen.exitonclick()
