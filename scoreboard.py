from turtle import Turtle
FONT = ("Arial", 24, "normal")
ALLIGN = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("file.txt") as data:
            self.high_score=int(data.read())
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"score : {self.score} High Score : {self.high_score}", align=ALLIGN, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("file.txt",mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALLIGN, font=FONT)


    def scoreboard(self):
        self.score += 1

        self.update()

