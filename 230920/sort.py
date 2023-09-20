a, b, c = input("세 정수를 입력하시오 : ").split()
a = int(a)
b = int(b)
c = int(c)
first = min(a,b,c)
last = max(a,b,c)
middle = (a+b+c)-first-last

print("오름차순으로 나열:", first, middle, last)