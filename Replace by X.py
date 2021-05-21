t=int(input())
for i in range(t):
    s=input()
    st=input()
    s=s.replace(st,"X")
    for i in range(len(s)-1):
        s=s.replace("XX","X")
    print(s)