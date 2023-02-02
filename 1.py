Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b,c=10,20,30
print(a,b,c)
10 20 30
print(b,c,a,sep=?)
SyntaxError: invalid syntax
print(b,c,a,sep='?')
20?30?10
print(b,c,a,sep='-')
20-30-10
print('25','5','2002',sep='-')
25-5-2002
apple=100
banana=200
cherry=300
print(apple,banana,cherry)
100 200 300
print(apple)
100
print(apple,end='')
100
print(banana,end=' ')
200 
print(apple,end=' ',banana,end=' ',cherry, end=' ')
SyntaxError: positional argument follows keyword argument
x,y,z=input("enter a threee values:").split()
enter a threee values:100 200 300
print("total no of students:",x)
total no of students: 100
print("no of boys",y)
no of boys 200
print("no of girls:",z)
no of girls: 300
x,y,z=input("enter a threee values:").split('*')
enter a threee values:100 200 * 300 - 400 * 500 ) 600
print("total no of students:",x)
total no of students: 100 200 
x,y,z=input("enter a threee values:").split('0')
enter a threee values:1 0 2 0 3
print("no of boys",y)
no of boys  2 
x,y,z=input("enter a threee values:").split('0')
enter a threee values:100
print("total no of students:",x)
total no of students: 1
print("no of girls:",z)
no of girls: 
email="teju6486@gmail.com"
pwd=123456
cemail=
SyntaxError: incomplete input


... 
>>> 99
9
>>> email="teju6486@gmail.com"
>>> pwd=123456
>>> cmail=input("enter the email")
enter the email Ever456@gmail.com
>>> cpwd=input("enter password:")
enter password:456
>>> if(email==cmail and pwd==cpwd):
...     print("login successfully")
... else:
...     print("login unsuccessful:)
...           
SyntaxError: incomplete input
>>> 
>>> email="teju6486@gmail.com"
... pwd=123456
... cmail=input("enter the email")
...           
SyntaxError: multiple statements found while compiling a single statement
>>> email="teju6486@gmail.com"
...           
>>> email="teju6486@gmail.com"
...           
>>> pwd=123456
...           
>>> cmail=input("enter the mail:")
...           
enter the mail:teju6486@gmail.com
>>> cpwd=int(input("enter pass:")
... 
... email="teju6486@gmail.com"
... pwd=123456
... cmail=input("enter the email")
...          
SyntaxError: '(' was never closed
>>> email="teju123@gmail.com"
... pwd=123456
... cmail=input("enter mail")
...          
SyntaxError: multiple statements found while compiling a single statement
