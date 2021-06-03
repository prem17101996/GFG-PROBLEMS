for i in range(int(input())):
    n,k=input().split()
    num=list(map(int,(input().split())))
    num.sort()
    str1=""
    for i in num:
        str1=str1+str(i)+" "
    print(str1)