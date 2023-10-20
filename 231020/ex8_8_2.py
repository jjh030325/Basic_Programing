f1 = open('random_numbers.txt','r')
f2 = open('random_even.txt','w')

data = list(f1.read().split())
for i in data:
    if (int(i)%2 == 0):
        f2.write(i)
        f2.write(" ")

f1.close()
f2.close()
