a, b = input('두 정수를 입력하시오 : ').split()
a = int(a)
b = int(b)

if (a%b==0):
    print(a,"는",b,"의 배수입니다.")
else:
    print(a,"는",b,"의 배수가 아닙니다.")