from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

"""this is declared out side the while loop for some reason"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

""" Main game loop"""
game_is_on = True
while game_is_on:
    """after all the segments are moved, then the screen is updated.
    basically we are only writing to the canvas after positions are updated"""
    screen.update()
    time.sleep(.1)

    snake.move()

screen.exitonclick()