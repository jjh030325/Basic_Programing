import random
f1 = open('random_numbers.txt','w')

for i in range(1, 11):
    r = random.randint(1,1001)
    f1.write(str(r))
    f1.write(' ')

f1.close()