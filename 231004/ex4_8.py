from ex4_7 import mean3, max3, min3

def mean6(a, b, c, d, e, f):
    return mean3(a+b, c+d, e+f)/2

def max6(a, b, c, d, e, f):
    aa = max3(a,b,c)
    bb = max3(d,e,f)
    if aa > bb:
        return aa
    else:
        return bb

def min6(a, b, c, d, e, f):
    aa = min3(a,b,c)
    bb = min3(d,e,f)
    if aa > bb:
        return bb
    else:
        return aa

while(1):
    a, b, c, d, e, f = input('여섯 개의 수를 입력하세요: ').split()
    if(a.isdigit() == True and b.isdigit() == True and c.isdigit()==True and d.isdigit() == True and e.isdigit() == True and f.isdigit()==True):
        break

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)

print('평균값은 {}'.format(mean6(a,b,c,d,e,f)))
print('최댓값은 {}'.format(max6(a,b,c,d,e,f)))
print('최솟값은 {}'.format(min6(a,b,c,d,e,f)))
