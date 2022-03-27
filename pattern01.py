def num():
    for i in range(1,10000):
        j = len(str(i))
        if j==2:
            if str(pow(i,i))[-2:]==str(i):
                print(i)
        if j==3:
            if str(pow(i,i))[-3:]==str(i):
                print(i)
        if j==4:
            if str(pow(i,i))[-4:]==str(i):
                print(i)