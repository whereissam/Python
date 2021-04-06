from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_car = []
        # if we need to loop class, first, we need to create a list
        self.new_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # create a chance to generate new car by 1/6
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)


    def move_car(self):
        for car in self.all_car:
            car.backward(self.new_speed)

    def get_speed(self):
        self.new_speed += MOVE_INCREMENT
        print(self.new_speed)