a, b, c = input("세 정수를 입력하시오 : ").split()
a = int(a)
b = int(b)
c = int(c)

if(a>=b and a>=c): last = a
elif(b>=c and b>=a): last = b
else: last = c

if(a<=b and a<=c): first = a
elif(b<=c and b<=a): first = b
else: first = c

middle = (a+b+c)-first-last

print("오름차순으로 나열:", first, middle, last)