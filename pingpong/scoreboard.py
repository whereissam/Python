from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        # 定義class中的function 再去做呼叫

    # add Score 每執行一次呼叫一次更新畫面
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 80, "normal"))

    def l_score_add(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_score_add(self):
        self.r_score += 1
        self.update_scoreboard()