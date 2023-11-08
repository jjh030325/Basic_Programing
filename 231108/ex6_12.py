t_list = [5,6,3,9,2,12,3,8,7]
print("주어진 리스트는 =  {}".format(t_list))

for i in range(len(t_list)-1):
    if t_list[i] > t_list[i+1]:
        t_list[i], t_list[i+1] = t_list[i+1], t_list[i]


print("가장 큰 수를 마지막으로 옮긴 결과:  {}".format(t_list))
