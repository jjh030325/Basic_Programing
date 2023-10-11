import math

def cube(edge_length):
    return edge_length ** 3

def box(length, width, height):
    return length * width * height

def cone(radius, height):
    return (1/3) * 3.14 * radius**2 * height

def sphere(radius):
    return (4/3) * 3.14 * radius**3

def cylinder(radius, height):
    return 3.14 * radius**2 * height


print("정육면체 부피:", cube(12))
print("직육면체 부피:", box(3, 5, 6))
print("원뿔 부피:", cone(20, 10))
print("구 부피:", sphere(15))
print("원기둥 부피:", cylinder(20, 10))
