from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


scoreboard = Scoreboard()

screen.listen()

paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball()

screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
screen.onkey(scoreboard.start_game, "space")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if scoreboard.game_start:
        paddle1.showturtle()
        paddle2.showturtle()
        ball.showturtle()
        ball.move()
# Detect collision with the wall then bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

# Detect collision the paddle then bounce
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

# Restart the game if anyone miss the ball
    if ball.xcor() > 400:
        scoreboard.player2_score += 1
        scoreboard.update_score()
        ball.new_round()
    if ball.xcor() < -400:
        scoreboard.player1_score += 1
        scoreboard.update_score()
        ball.new_round()

    if scoreboard.player1_score > 3 or scoreboard.player2_score > 3:
        if scoreboard.player1_score > scoreboard.player2_score:
            winner_name = "Player on the left hand side "
        else:
            winner_name = "Player on the right hand side "
        scoreboard.show_winner(winner_name)
        game_is_on = False


screen.exitonclick()
