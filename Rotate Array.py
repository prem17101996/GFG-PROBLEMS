for i in range(int(input())):
    n,d=map(int,(input().split()))
    arr=input().split()
    result=arr[d:]+arr[:d]
    str1=" "
    for i in result:
        str1=str1+i+" "
    print(str1[1:])   