def max2(m, n):
    if(m>n):
        return m
    else:
        return n
def min2(m, n):
    if(m>n):
        return n
    else:
        return m

print('100과 200중 큰 수는 :', max2(100, 200))
print('100과 200중 작은 수는 :', min2(100, 200))