f1 = open('number1to10.txt', 'r')
f2 = open('numberby10.txt','r')
f3 = open('merge.txt','w')

for i in range(1, 11):
    f3.write("{} : {}\n".format(int(f1.readline()), int(f2.readline())))

f1.close()
f2.close()
f3.close()