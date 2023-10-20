f1 = open('number1to10.txt','r')
f2 = open('numberby10.txt', 'w')

for i in range(1, 11):
    f2.write("{}\n".format(int(f1.readline())*10))

f1.close()
f2.close()