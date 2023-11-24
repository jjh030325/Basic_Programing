def selection(arr):
    for i in range(len(arr)):
        now = arr[i]
        nowindex = i
        for j in range(i + 1, len(arr)):
            if(now > arr[j]):
                now = arr[j]
                nowindex = j
        tmp = arr[i]
        arr[i] = arr[nowindex]
        arr[nowindex] = tmp

arr = [11,3,7,1,9,7,12,5,4,9,8,10,2,6,5]
selection(arr)
print(arr)
