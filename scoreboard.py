from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.player1_score = 0
        self.player2_score = 0
        self.game_start = False
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write("Press SPACE to start the game!", align="center",
                   font=("courier", 30, "normal"))

    def update_score(self):
        self.clear()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.fillcolor("black")
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=6)
        self.stamp()
        self.goto(0, 255)
        self.write(str(self.player2_score) + " : " + str(self.player1_score), align="center",
                   font=("courier", 30, "normal"))

    def start_game(self):
        self.game_start = True
        self.update_score()

    def show_winner(self, winner):
        self.clear()
        self.write(winner + "wins the game!", align="center",
                   font=("courier", 30, "normal"))
