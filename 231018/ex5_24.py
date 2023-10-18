def is_perfect_num(n):
    div_num = []
    for j in range(1, int(n/2 + 1)):            #자기 자신을 제외한 약수는 i/2+1을 넘어가지 않으니 최적화
        if n%j == 0:
            div_num.append(j)
    if(sum(div_num) == n):
        print("{}는 완전수입니다.".format(n))
        print("{}의 약수 : {}, 약수의 합 = {}".format(n, div_num, n))

start_num = 1
end_num = 10001
for i in range(start_num, end_num):
    is_perfect_num(i)