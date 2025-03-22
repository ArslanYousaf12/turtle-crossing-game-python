from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len= 2)
        self.start_position()
        
    
    def start_position(self):
        random_y = random.randint(-290, 290)
        self.goto(300, random_y)
        # self.goto(0,0)
    
    def move(self):
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)
