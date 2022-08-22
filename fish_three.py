from itertools import combinations
import pandas as pd




powdig = []
d = []
for i in range(1, 1000):
    p = str(pow(i,i))    
    for j in range(0,10):
        d.append(p.count(str(j)))
    powdig.append(d)
    d = []
# print(powdig[2])
# powdig = [powdig[1]]
# print(powdig)


var = []

def par(N=10, m=3):
    x = range(N)
    comb = [com for com in combinations(x,m)]
    tot = int(len(list(combinations(x,m)))/2)
    for j in range(tot):
        j+1
        var.append(comb[j])
    return var

comb = par()

numb = [0,1,2,3,4,5,6,7,8,9]

for l in range(0,len(comb)):
    print(str(list(set(comb[l])))+"="+str(list(set(numb) - set(comb[l]))))
    for i in range(0,len(powdig)):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for com in list(comb[l]):
            sum1 =  sum1 + powdig[i][com]
        for num in list(set(numb) - set(comb[l])):
            sum2 = sum2 + powdig[i][num]
        
        # print("number="+str(i+1))

        if str(sum1)==str(sum2):
            print(str(i+1))

            


