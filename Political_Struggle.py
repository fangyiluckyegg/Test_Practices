a = int(input())
b = int(input())
c = int(input())

num=a+b+c
if num%3==0:
    a=a+a/3
    print(int(a)) 
else:
    print("总数不能被3整除，请重新输入")
    a = int(input())
    b = int(input())
    c = int(input())


#6,4,2