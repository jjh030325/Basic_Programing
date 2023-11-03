t = (100,121,120,130,140,120,122,123,190,125)

print("일일 매출 기록: {}".format(t))
before = 0
ans = 0
count = 0

for i in t:
    count += 1
    if before>i:
        ans += 1
    before = i

print("지난 {}일 동안 전일대비 매출이 감소한 날은 {}일입니다.".format(count, ans))
