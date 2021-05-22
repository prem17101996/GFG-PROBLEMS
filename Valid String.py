for i in range(int(input())):
    n=int(input())
    s=input()
    cou0=0
    cou1=0
    for i in s:
        if i=="0":
            cou0+=1
        else:
            cou1+=1
    cou11=0
    cou00=0
    if cou0==cou1:
        for i in s:
            if i=="0":
                cou00+=1
            else:
                cou11+=1
            if cou00<cou11:
                print("no")
                break
        else:
            
            print("yes")
    else:
        print("no")