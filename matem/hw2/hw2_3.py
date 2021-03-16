from sympy import plot_implicit, Eq
from sympy.abc import x, y
import turtle
import math
# Окружность
a = 90
b = 90
dx = turtle.xcor()
dy = turtle.ycor()
for deg in range(722):  # чертит круг два раза
    rad = math.radians(deg)
    x = -a * math.sin(rad) + dx
    y = -b * math.cos(rad) + b + dy
    turtle.goto(x, y)
# эллипс
a = 190
b = 90
dx = turtle.xcor()
dy = turtle.ycor()
for deg in range(722):  # чертит эллипс два раза
    rad = math.radians(deg)
    x = -a * math.sin(rad) + dx
    y = -b * math.cos(rad) + b + dy
    turtle.goto(x, y)
# гиперпола
a = -1
b = 3
plot_implicit(Eq((y - a * x) * (y - b * x), -1), (x, -10, 10), (y, -10, 10))

# Плоскость
import numpy as np
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


plt3d = plt.figure().gca(projection='3d')
xx, zz = np.meshgrid(range(10), range(10))
yy =1
yy1=2

for _ in itertools.repeat(None, 20):
    plt3d.plot_surface(xx, yy, zz)
    plt3d.plot_surface(xx, yy1, zz)

    plt.hold(True)
    yy=yy+.1
    yy1=yy1+.1

    plt.show()
