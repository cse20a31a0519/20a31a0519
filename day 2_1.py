Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
i=1
while(i<=5):
    j=1
    while(j<=i):
        print(i,end=" ")
        j=j+1
    print("\n")
    i=i+1

    
1 

2 2 

3 3 3 

4 4 4 4 

5 5 5 5 5 

age=[10,30,-50,60,100]
print(age)
[10, 30, -50, 60, 100]
age=[10,30,-50,60,100]
print(len(age))
5
for i in range(len(age)):
    print(age)

    
[10, 30, -50, 60, 100]
[10, 30, -50, 60, 100]
[10, 30, -50, 60, 100]
[10, 30, -50, 60, 100]
[10, 30, -50, 60, 100]

age=[10,30,-50,60,200,105,305,1000,11,22]
for i in range(len(age)):
    if(age[i]%100==0):
        print(age[i])

        
200
1000
>>> 
>>> l=[10,20,50,105]
>>> for i in range (len(l)):
...     if '0' in str(l[i]):
...         print(l[i])
... 
...         
10
20
50
105
>>> l=[101,220,150,105,26,59,1000,48,859634]
... for i in range (len(l)):
...     if '0' in str(l[i]):
...         print(l[i])
...         
SyntaxError: multiple statements found while compiling a single statement
>>> l=[101,220,150,105,26,59,1000,48,859634]
>>> for i in range (len(l)):
...     if '0' in str(l[i]):
...         print(l[i])
... 
...         
101
220
150
105
1000
