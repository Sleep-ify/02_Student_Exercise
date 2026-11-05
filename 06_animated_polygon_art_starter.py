"""EXERCISE: animate multiple polygons by moving existing objects.
First finish polygon_shape.py. Then change the motion, colors, sizes,
number of polygons, and frame count to create your own artwork.
"""
import turtle
import random
import math
import time

class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        if sides < 3:
            raise ValueError("size must be more than 3")
        if side_length <=0:
            raise ValueError("side length must be more than 0")
        if pen_size <= 0:
            raise ValueError("pen size must be more than 0")
        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen = turtle.Turtle()
        self._pen.pensize(pen_size)
        self._pen.hideturtle()
        self._angle = angle
        self._pen.speed(0)


    def draw(self):
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(0)
        self._pen.pencolor(self._color)
        self._pen.pendown()
        self._pen.left(self._angle)
        for _ in range(self._sides):
            self._pen.forward(self._side_length)
            self._pen.left(360//self._sides)
        self._pen.penup()


    def move_to(self, x, y):
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  # The entire frame is displayed with screen.update().


rng = random.Random(17)
colors = ["cyan", "springgreen", "orange", "deepskyblue", "plum", "yellow"]
shapes = []
for _ in range(12):
    x = rng.randint(-350, 210)
    y = rng.randint(-170, 120)
    shape = Polygon(x, y, rng.randint(3, 6), rng.randint(35, 105),
                    rng.choice(colors), rng.randint(1, 6), rng.randint(0, 359))
    shape.draw()
    # Store the home position and motion phase, not a second copy of
    # the shape's current position.
    shapes.append((shape, x, y, rng.random() * 6.28))

for frame in range(1000):
    for shape, home_x, home_y, phase in shapes:
        x = home_x + 32 * math.cos(frame * 0.07 + phase)
        y = home_y + 23 * math.sin(frame * 0.07 + phase)
        shape.move_to(x, y)  # Reuse the same object and its internal turtle.
    screen.update()
    time.sleep(0.045)  # A short delay makes motion visible.


screen.update()
screen.mainloop()
