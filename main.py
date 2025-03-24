import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
myTurtle = Player()
score = Scoreboard()
screen.listen()

screen.onkey(myTurtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    
    #Detect collisions with car
    for car in car_manager.all_cars:
        print(car.heading())
        print(myTurtle.distance(car))     
        if car.distance(myTurtle) < 20:
            game_is_on = False
            score.game_over()
    
    # Detect Collision with the uper wall
    if myTurtle.ycor() > 300:
        myTurtle.goto(0, -280)
        car_manager.level_up()
        score.update_score()
        
        
        

screen.exitonclick()
   