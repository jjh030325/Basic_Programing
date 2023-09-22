for i in range(2, 13):
    check = False
    for j in range(2, i-1):
        if(i%j==0):
            check = True
    if(check==True):
        print(i, ": 합성수")
        check = False
    else:
        print(i,": 소수")