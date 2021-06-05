#code
for i in range(int(input())):
    n=int(input())
    str2=""
    lst=[]
    for i in range(n):
        str1=input()
        if str1[:5]=="place":
            str1=str1.split()
            lst.append(str1[-1])
        elif str1[:6]=="remove":
            if len(lst)<1:
                str2=str2+"-1"+" "
                
            else:
                
                str2=str2+lst[-1]+" "
                lst.remove(lst[-1])
    print(str2)

    
    