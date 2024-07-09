from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.write(f"left: {self.l_score} | right: {self.r_score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def l_increase_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"left: {self.l_score} | right: {self.r_score}", align=ALIGN, font=FONT)

    def r_increase_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"left: {self.l_score} | right: {self.r_score}", align=ALIGN, font=FONT)