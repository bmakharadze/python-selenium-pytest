from turtle import Screen, Turtle
import time
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create()
        self.snake_head = self.snake_parts[0]

    def create(self):
        for x in range(0, -41, -20):
            self.add_parts((x, 0))

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_xcor = self.snake_parts[part_num - 1].xcor()
            new_ycor = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_xcor, new_ycor)
        self.snake_head.forward(20)
        # self.snake_head.right(90)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def add_parts(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.snake_parts.append(square)

    def extend_snake(self):
        self.add_parts(self.snake_parts[-1].position())


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.speed("fastest")
        self.move_new_location()

    def move_new_location(self):
        rand_x = random.randint(-300, 300)
        rand_y = random.randint(-300, 300)
        self.goto(rand_x, rand_y)


screen = Screen()
screen.bgcolor("grey")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    #  Detect collision with food
    if snake.snake_head.distance(food) < 20:
        print("test")
        food.move_new_location()
        snake.extend_snake()

screen.exitonclick()