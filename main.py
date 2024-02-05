from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        print('collided')
    

