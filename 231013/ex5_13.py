import math
data = list(input("임의의 갯수만큼 정수를 입력하세요: ").split())

s = 0
p = 0
pp = 0

for i in data:
    s += int(i)

p = s / len(data)

for i in data:
    pp += (int(i)-p)**2

pp = pp / len(data)

pp = math.sqrt(pp)

print("합: {}".format(s))
print("평균: {}".format(p))
print("표준편차:  {:.2f}".format(pp))