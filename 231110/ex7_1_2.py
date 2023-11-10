import time

def sum1to1000000():
    ans = 0
    for i in range(1000001):
        ans += i
    return ans

startTime = time.time()
for i in range(100):
    sum1to1000000()
endTime = time.time()

print("1에서 1,000,000까지의 합을 100번 반복해서 구하는 시간 : {:.5}초".format(endTime-startTime))
