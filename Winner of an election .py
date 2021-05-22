for i in range(int(input())):
    n=int(input())
    s=list(map(str,(input().split())))
    lst=[]
    l=list(set(s))
    for i in l:
        lst.append(s.count(i))
    m=max(lst)
    lst1=[]
    for i in l:
        if s.count(i)==m:
            lst1.append(i)
    sort_name=sorted(sorted(lst1), key=str.upper)
    print(sort_name[0])
            