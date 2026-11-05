"""EXERCISE: make overlapping polygon art like the reference image.
Complete polygon_shape.py first. Then adjust the parameters below to
create your own composition. The example uses a black background.
"""
import turtle
import random


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
screen.title("Student Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  # We draw the whole scene before refreshing the screen.

colors = ["cyan", "turquoise", "orange", "yellowgreen", "deepskyblue",
          "salmon", "plum", "lightgreen", "gold", "pink", "white"]
rng = random.Random(12)

polygons = []  # Hold references so the Polygon objects remain accessible.
for _ in range(20):
    sides = rng.randint(3, 6)
    side_length = rng.randint(35, 120)
    x = rng.randint(-350, 260)
    y = rng.randint(-225, 180)
    color = rng.choice(colors)
    pen_size = rng.randint(1, 7)
    angle = rng.randint(0, 359)
    polygon = Polygon(x, y, sides, side_length, color, pen_size, angle)
    polygon.draw()
    polygons.append(polygon)


screen.update()
screen.mainloop()
