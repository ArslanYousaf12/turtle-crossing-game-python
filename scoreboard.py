from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.score = 0
      self.penup()
      self.color("black")
      self.hideturtle()
      self.goto(0, 270)
      self.shapesize(stretch_wid=2, stretch_len=2 )
      self.write(arg=f"Score: {self.score}", font=("Courier", 24, "normal"), align="center")
    
   def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", font=("Courier", 24, "normal"), align="center")
    
   def game_over(self):
       self.goto(0,0)
       self.write(arg=f"Game Over", font=("Courier", 24, "normal"), align="center")
        
      
        
