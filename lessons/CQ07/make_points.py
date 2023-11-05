"""Examine the point file."""
from lessons.CQ07.point import Point

my_point: Point = Point(8,9)
my_new_point: Point = my_point.scale(2)
print(my_point)
print(my_new_point)
print(my_new_point.x)
print(my_new_point.y)