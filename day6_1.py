'''def Happyno(num):

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
#object oriennted progm
#to create and acess an obj
class abc:
    var=10
obj=abc()
print(obj.var)
class abc:
    attri=10
obj=abc()
print(obj.attri)
#to create self arguments
class abc:
    attri=10
    def display(self):
        print("this is class")
obj=abc()
print(obj.attri)
obj.display()
#creation of constructor
class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value
        print("the value is",value)
obj=abc(100)
class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var
        print("this obj value is",var)
        print("the  class value is",abc.class_var)
obj1= abc(101)
obj2= abc(102)
obj3= abc(103)

class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even= 1
        def even_odd(self,num):
            self.check(num)
            if(self.even==1):
                print(num ,"is even")
            else:
                print(num ,"is odd")
n=number()
n.even_odd(21)'''
class circle:
    pi=3.1459
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi*self.r*self.r
    def circumstance (self):
        return 2*circle.pi*self.r
c1=circle(7.5)
print("area",c1.area())
print("circum",c1.circumstance())

