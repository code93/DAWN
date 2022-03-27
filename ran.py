import math
def powdist(n):
    sum = 0
    rel = 0.25
    tot=str(pow(n,n)).count("0")+str(pow(n,n)).count("1")+str(pow(n,n)).count("2")+str(pow(n,n)).count("3")+str(pow(n,n)).count("4")+str(pow(n,n)).count("5")+str(pow(n,n)).count("6")+str(pow(n,n)).count("7")+str(pow(n,n)).count("8")+str(pow(n,n)).count("9")
    if(math.isclose(0.10,str(pow(n,n)).count("0")/tot,rel_tol=rel))==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("1")/tot,rel_tol=rel)==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("2")/tot,rel_tol=rel)==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("3")/tot,rel_tol=rel)==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("4")/tot,rel_tol=rel)==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("5")/tot,rel_tol=rel)==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("6")/tot,rel_tol=rel)==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("7")/tot,rel_tol=rel)==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("8")/tot,rel_tol=rel)==True:
        sum=sum+1
    if math.isclose(0.10,str(pow(n,n)).count("9")/tot,rel_tol=rel)==True:
        sum=sum+1
    
    return sum/10

rat = 0
a=500
b=10000
for i in range(a,b):
    ratio = powdist(i)
    print("[+] For number "+str(i)+" ratio in percentage is")
    print(ratio*100)
    if(ratio*100==100):
        rat = rat+1
    den = b-((b-a)/10)-a
    print(den)
print(str(rat*100/den))