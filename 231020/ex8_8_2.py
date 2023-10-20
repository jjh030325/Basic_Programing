f1 = open('random_numbers.txt','r')
f2 = open('random_even.txt','w')

data = list(f1.read().split())
for i in range(len(data)):
    if(i != 0 and i!=len(data)-1):
        f2.write(data[i])
        f2.write(" ")

f1.close()
f2.close()
