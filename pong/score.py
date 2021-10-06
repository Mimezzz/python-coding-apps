from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_point=0
        self.r_point=0

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-180, 280)
        self.write(self.l_point, font=(42))
        self.goto(180, 280)
        self.write(self.r_point, font=(42))

    def l_score(self):
        self.l_point+=1
        self.update_score()

    def r_score(self):
        self.r_point+=1
        self.update_score()
