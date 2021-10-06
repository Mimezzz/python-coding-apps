from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

paddle=Turtle()
screen= Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
score=Score()

r_paddle =Paddle((370,0))
l_paddle=Paddle((-380,0))
ball=Ball()
# screen.update()
# time.sleep(0.1)

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')

screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on=True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

# detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
# detect collision with both paddles
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-350:
        ball.bounce_x()
        ball.speedup()


# detect when the paddle missed the ball
    if ball.xcor()>370:
        ball.reset()
        score.l_score()
    if ball.xcor()<-380:
        ball.reset()
        score.r_score()

screen.exitonclick()