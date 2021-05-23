for i in range(int(input())):
    n=int(input())
    num=list(map(int,(input().split())))
    num=num[::-1]
    lst=[]
    for i in range(len(num)):
        mul=num[i]*num[i]
        lst.append(mul)
    
    for i in range(len(lst)):
        if i%2==1:
            lst[i]=-lst[i]
    print(sum(lst))
            
            