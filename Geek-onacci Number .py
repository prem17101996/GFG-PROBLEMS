
for i in range(int(input())):
    lst=[]
    lst1=[]
    a,b,c,n=map(int,(input().split()))
    lst1.append(n)
    lst.append(a)
    lst.append(b)
    lst.append(c)
    for i in range(max(lst1)-3):
        lst.append(lst[-1]+lst[-2]+lst[-3])

    for i in lst1:
        print(lst[i-1])