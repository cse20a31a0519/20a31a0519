'''list a=(1,2,3,4)
list b=()
list c=()
def swap(b,c):
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
hanoi(len(a),a,b,c)
print("after puzzle")
print(a,b,c)
from datetime import *
d= date.today()
print(d)
d=date(2023,5,13)
for x in range(1,30):
    nextdate= d+timedelta(days=x)
    print(nextdate)'''
def fact(n):
    if n==1:
        return 1
    else:
        f=n*fact(n-1)
sum,temp=0
n=int(input("enter a number:"))
temp=n
while(n!=0):
    r=n%10
    sum=sum+fact(r)
    n=n//10
    if(temp==sum):
        print("krishnamurty no")
    else:
        print("not krisnamurty no")
fact(n)
    
