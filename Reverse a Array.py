for i in range(int(input())):
    n=int(input())
    str1=list(map(int,(input().split())))
    str1=str1[::-1]
    str2=""
    for i in str1:
        str2=str2+str(i)+" "
    print(str2)