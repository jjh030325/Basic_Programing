t = (1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)

print("주어진 튜플은: {}".format(t))
most = 0
ans = 0

for i in t:
    if t.count(i) > most:
        most = t.count(i)
        ans = i

print("가장 많이 나타나는 원소는: {}".format(i))