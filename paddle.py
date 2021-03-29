from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, num):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.shape("square")
        # paddle_size: height = 20, width = 100
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.init_position(num)

    def init_position(self, num):
        if num == 1:
            self.goto(x=350, y=0)
        elif num == 2:
            self.goto(x=-350, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)


