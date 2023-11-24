def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right): #한쪽을 다 붙일 때까지 이어붙여줌
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):                #왼쪽이 남은 경우 이어붙여줌
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):               #오른쪽이 남은 경우 이어붙여줌
            arr[k] = right[j]
            j += 1
            k += 1


arr = [11,3,7,1,9,7,12,5,4,9,8,10,2,6,5]
merge_sort(arr)
print(arr)