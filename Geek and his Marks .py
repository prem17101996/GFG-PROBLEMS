for _ in range(int(input())):
    n=int(input())
    nnum=input().split()
    x=int(input())
    for _ in range(x):
        xnum=int(input())
        count=0
        for i in nnum:
            if xnum<int(i):
                count+=1
        print(count)
        