
for i in range(int(input())):
    n=int(input())
    re10=n%10
    de10=n/10
    re5=re10%5
    de5=re10/5
    re2=re5%2
    de2=re5/2
    print(int(de10)+int(de5)+int(de2)+int(re2))
    