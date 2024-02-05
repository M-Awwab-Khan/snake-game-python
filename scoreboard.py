from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        with open('data.txt', 'r') as f:
            self.high_score = int(f.read())
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write('Game Over', align=ALIGNMENT, font=FONT)