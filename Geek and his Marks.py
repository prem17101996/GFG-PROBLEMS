for i in range(int(input())):
    n,g=map(int,(input().split()))
    lst=list(map(int,(input().split())))
    cou=0
    for i in lst:
        if i>g:
            cou+=1
    print(cou)