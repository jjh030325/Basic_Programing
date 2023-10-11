import math

def  distance(x1, y1, x2, y2):
    dap = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    return dap

x1 = int(input("x1 좌표를 입력하시오 : "))
y1 = int(input("y1 좌표를 입력하시오 : "))
x2 = int(input("x2 좌표를 입력하시오 : "))
y2 = int(input("y2 좌표를 입력하시오 : "))

print("두 점의 거리: {:.1f}".format(distance(x1,y1,x2,y2)))