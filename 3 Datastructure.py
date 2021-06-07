for i in range(int(input())):
    n=int(input())
    str1=""
    lst=[]
    lst1=[]
    lst2=[]
    lst3=[]
    for i in range(n):
        str2,num1=input().split()
        if str2=="1":
            lst1.append(int(num1))
    # print(lst1)        
        elif str2=="2":
            lst2.append(int(num1))
        elif str2=="3":
            lst3.append(int(num1))
    # print(lst1)       
    lst1.sort()
    # print(lst1)
    lst1=lst1[::-1]
    lst3=lst3[::-1]
    
    lst.extend(lst1)
    lst.extend(lst2)
    lst.extend(lst3)
    # print(lst)
    for i in lst:
        str1=str1+str(i)+" "
    print(str1)
        
