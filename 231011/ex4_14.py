def sort3(a,b,c):
    min3 = a
    max3 = a
    if min3>b:
        min3 = b
    if min3>c:
        min3 = c
    if max3<b:
        max3 = b
    if max3<c:
        max3 = c
    middle3 = (a+b+c) - min3 - max3
    print("정렬된 리스트는 다음과 같습니다: {} {} {}".format(min3, middle3, max3)) 

print("세 수를 입력하세요:")
a = int(input())
b = int(input())
c = int(input())
sort3(a,b,c)