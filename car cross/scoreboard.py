from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-150, 260)
        self.score = 0

        self.update_score()

    def update_score(self):
        self.clear()
        # self.goto(-100, 260)
        self.write(f"Your score : {self.score}", align='center', font=FONT)

    def get_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Game over", align='center', font=FONT)