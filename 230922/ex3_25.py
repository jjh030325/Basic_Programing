bug = 0
day = 1
while True:
    bug += 7
    print("day : {}    달팽이의 위치 : {} 미터".format(day, bug))
    if(bug>=30):
        print("\n우물을 탈출하는 데 걸린 날은 {}일 입니다.".format(day))
        break
    bug -= 5
    day += 1