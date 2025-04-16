import math

def area_triangle(base, height):
    return base * height / 2

def area_rectangle(length, width):
    return length* width

def area_circle(radius):
    return math.pi*radius**2

def area_cone(radius,height):
    return math.pi*radius*(radius+height)