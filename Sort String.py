for i in range(int(input())):
    str1=input()
    lst=[]
    for i in str1:
        lst.append(i)
    lst.sort()
    str2=""
    for i in lst:
        str2=str2+str(i)
    print(str2)
        