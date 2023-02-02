Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
email="teju123@gmail.com"
pwd=123456
cmail=input("enter mail")
enter mail teju123@gmail.com
cpwd=int(input("enter pass:"))
enter pass:123456
if(email==cmail and pwd==cpwd):
    print("login s")
else:
    print("login un")

    
login un
a=5
b=5.0
if(a==b):
    print("yes")
else:
    print("no")

    
yes
a=5
b=True

if(a==b):
    print("yes")
else:
    print("no")

    
no
a=int(input("enter a number"))
enter a number 21
if(a%7==0):
    print("it is divisible:")
else:
    print("it is not divisible:")

    
it is divisible:
email="teju6486@gmail.com"
pwd=123456
cemail=input("enter mail:")
enter mail:teju6486@gamil.com
cpwd=int(input("enter a pass:"))
enter a pass:123478
if(email==cemail and pwd==cpwd):
    print("login successful:")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(emial==cemail and pwd!=cpwd):
    print("login failed due to pass:")
elif(email!=cemail and pwd!=cpwd):
    print("login failed due to pass and mail:")

    
Traceback (most recent call last):
  File "<pyshell#46>", line 5, in <module>
    elif(emial==cemail and pwd!=cpwd):
NameError: name 'emial' is not defined. Did you mean: 'email'?
email="teju6486@gmail.com"
pwd=123456
cemail=input("enter mail:")
enter mail:teju6486@gamil.com
cpwd=int(input("enter a pass:"))
enter a pass:123478
if(email==cemail and pwd==cpwd):
    print("login successful:")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(emal==cemail and pwd!=cpwd):
    print("login failed due to pass:")
elif(email!=cemail and pwd!=cpwd):
    print("login failed due to pass and mail:")
    
SyntaxError: multiple statements found while compiling a single statement

email="teju6486@gmail.com"
pwd=123456
cemail=input("enter mail:")
enter mail: teju6486@gmail.com
cpwd=int(input("enter a pass:"))
enter a pass:123478
cpwd=int(input("enter a pass:"))
if(email==cemail and pwd==cpwd):
    
SyntaxError: multiple statements found while compiling a single statement
a="balaji"
print("y" in a)
False
b="teja"
print("t" in b)
True
print(b[2])
j
for i in range(1,10):
    print(i,end=" ")

    
1 2 3 4 5 6 7 8 9 
for i in range(10,1,-1):
...     print(i,end=" ")
... 
...     
10 9 8 7 6 5 4 3 2 
>>> for i in range(97,122):
...     print(chr(i),end=" ")
... 
...     
a b c d e f g h i j k l m n o p q r s t u v w x y 
>>> for i in range(97,123):
...     print(chr(i),end=" ")
... 
...     
a b c d e f g h i j k l m n o p q r s t u v w x y z 
>>> for i in range(65,91):
...     if(chr(i)=='A','E','I','O','U'):
...         print(chr(i),end=" ")



... 
...         
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
>>> for i in range(65,91):
...     if(i==65 or i==69 or i==73 or i==79 or i==85):
...         print(chr(i))
... 
...         
A
E
I
O
U
>>> for i in range(65,91):
...     if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
...         print(chr(i),end=" ")
... 
...         
B C D F G H J K L M N P Q R S T V W X Y Z 
>>> for i in range(90,64,-2):
...     if(i!=65 and i!=69 and i!=73 and i!=79 and i!=85):
...         print(chr(i),end=" ")
... 
...         
Z X V T R P N L J H F D B 
