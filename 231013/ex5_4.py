a = [2, 3, 4, 5, 6]
reverseda = list()

for i in range(len(a)):
    reverseda.append(a.pop())
    
print(reverseda)