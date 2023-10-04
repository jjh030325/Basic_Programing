def mean3(a, b, c):
    return ((a+b+c)/3)
def max3(a, b, c):
    m = a
    if m<b:
        m = b
    if m<c:
        m = c
    return m  
def min3(a, b, c):
    m = a
    if m>b:
        m = b
    if m>c:
        m = c
    return m

if __name__ == "__main__":
    a, b, c = input('세 수를 입력하시오 : ').split()
    a = int(a)
    b = int(b)
    c = int(c)
    print('{}, {}, {}의 평균값은 {}'.format(a, b, c, mean3(a,b,c)))
    print('{}, {}, {}의 최댓값은 {}'.format(a, b, c, max3(a,b,c)))
    print('{}, {}, {}의 최솟값은 {}'.format(a, b, c, min3(a,b,c)))
