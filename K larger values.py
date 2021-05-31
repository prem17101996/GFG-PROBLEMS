
t=int(input())
for i in range(t):
    n,k=list(map(int,(input().split())))
    arr=list(map(int,(input().split())))
    arr.sort()
    value=arr[::-1]
    value=value[:k]
    str1=""
    for i in value:
        str1=str1+str(i)+" "
    print(str1)
        
        
        