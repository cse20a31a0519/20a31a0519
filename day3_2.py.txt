Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=[12,-2,-33,84,5,6,87,8,99,10]
print(sort(num))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(sort(num))
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
print(sorted(num))
[-33, -2, 5, 6, 8, 10, 12, 84, 87, 99]

num=[12,-2,-33,84]
num.append(0)
print(num)
[12, -2, -33, 84, 0]
print(num.count(5))
0
print(num.count(3))
0

num=[6,3,7,0,1,2,4,9]
print(num.index(7))
2
print(num.count(1))
1
print(num.insert(4,100))
None
print(num)
[6, 3, 7, 0, 100, 1, 2, 4, 9]
print(num.count(1))
1
print(num)
[6, 3, 7, 0, 100, 1, 2, 4, 9]
print(count)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(count)
NameError: name 'count' is not defined. Did you mean: 'round'?

num=[6,3,7,0,1,2,4,9]
print(num.index(7))
2
print(num.insert(4,100))
None
print(num)
[6, 3, 7, 0, 100, 1, 2, 4, 9]
print(num.remove(0))
None
print(num)
[6, 3, 7, 100, 1, 2, 4, 9]
print(num.remove(1))
None
print(num)
[6, 3, 7, 100, 2, 4, 9]
num.remove(2)
print(num)
[6, 3, 7, 100, 4, 9]
num.reverse()
print(num)
[9, 4, 100, 7, 3, 6]
print(num.reverse())
None
print(num)
[6, 3, 7, 100, 4, 9]


n=int(input("enter n value:"))
enter n value:371
s=0
while(n!=0):
    r=n%10
    s=r*r*r
    n=n//10

    
if(sum==n):
    print("avmstrom")

    
else:
    
SyntaxError: invalid syntax
else:
    
SyntaxError: invalid syntax
n=int(input("enter n value:"))
enter n value:371
s=0
while(n!=0):
    r=n%10
    s=r*r*r
    n=n//10
if(sum==n):
    
SyntaxError: multiple statements found while compiling a single statement
n=int(input("enter n value:"))
enter n value:371

n=10
for n in range(0,11):
    print(n*n*n,end=" ")

    
0 1 8 27 64 125 216 343 512 729 1000 

cubes=[]
for i in range(11):
    cubes.append(i**3)
    print(cubes)

    
[0]
[0, 1]
[0, 1, 8]
[0, 1, 8, 27]
[0, 1, 8, 27, 64]
[0, 1, 8, 27, 64, 125]
[0, 1, 8, 27, 64, 125, 216]
[0, 1, 8, 27, 64, 125, 216, 343]
[0, 1, 8, 27, 64, 125, 216, 343, 512]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
cubes=[]
for i in range(11):
    cubes.append(i**3)

    
print(cubes)
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

n=int(input("enter the n value:"))
enter the n value:1223

num=[int(d) for d in str(input("enter number:"))
     even,odd=0,0
     
SyntaxError: '[' was never closed
num=[int(d) for d in str(input("enter number:"))]
     
enter number:1223
even,odd=0,0
     
for i in range(0,len(num)):
     if i%2==0:
        even=even+num[i]
     else:
         odd=odd+num[i]

         
print(abs(odd-even))
2

num=[int(d) for d in str(input("enter number:"))]
enter number:4567
even,odd=0,0
for i in range(0,len(num)):
    if i%2==0:
       even=even+num[i]
    else:
         odd=odd+num[i]
print(abs(odd-even))
SyntaxError: invalid syntax
print(abs(odd-even))
0

for n in range(0,11):
    print(n*n*n,end="  ")

    
0  1  8  27  64  125  216  343  512  729  1000  
>>> 
>>> print([i**3 for i in range(11)])
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> 
>>> 
>>> term=int(input("enter the term:"))
enter the term:16
>>> if term%2==0:
...     term = term//2
...     print(3**(term-1))
... else:
...     term = term//2+1
...     print(2**(term-1))
... 
...     
2187
>>> 
>>> term=int(input("enter the term:"))
enter the term:13
>>> if term%2==0:
...     term = term//2
...     print(3**(term-1))
... else:
...     term = term//2+1
...     print(2**(term-1))
... 
...     
64
