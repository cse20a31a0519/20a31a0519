def Happyno(num):

    rem=0
    sum=0
    while(num>0):
       rem=num%10
       sum=sum+(rem*rem)
       num=num//10
    return sum
num=int(input("enter a no:"))
result=num
while(result!=1 and result!=4):
    result=Happyno(result)
if(result==1):
    print("happy no",str(num))
else:
    print("not happy no",str(num))
