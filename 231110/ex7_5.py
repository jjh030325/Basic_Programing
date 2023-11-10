import math

for i in range(0, 181, 10):
    print("sin({:3}) = {:.3f}, cos({:3}) = {:.3f}, tan({:3}) = {:.3f}".format(i, math.sin(math.pi * (i)/180), i, math.cos(math.pi * (i)/180), i, math.tan(math.pi * (i)/180)))