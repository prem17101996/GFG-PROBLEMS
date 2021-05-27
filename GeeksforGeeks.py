for i in range(int(input())):
    n=int(input())
    
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    
    for i in range(len(lst)-1):
        lst.append(lst[0])
        lst.remove(lst[0])
        lst.remove(lst[0])
    print(lst[0])