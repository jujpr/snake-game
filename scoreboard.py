from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_data.txt", "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 270)

    def write_score(self):
        self.clear()
        self.write(f"Score: {str(self.score)} High Score: {self.high_score}", align="center", font=("Courier", 12, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Courer", 12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_high_score()
        self.score = 0
        self.write_score()

    def new_high_score(self):
        with open("snake_data.txt", "w") as file:
            file.write(str(self.high_score))


