Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> email="teju6486@gmail.com"
>>> pwd=123456
>>> cemail=input("enter mail:")
enter mail: teju6486@gmail.com
>>> cpwd=int(input("enter a pass:"))
enter a pass:124789
>>> if(email==cemail and pwd==cpwd):
...     print("login successful:")
... elif(email!=cemail and pwd==cpwd):
...     print("login failed due to mail")
... elif(email==cemail and pwd!=cpwd):
...     print("login failed due to pwd")
... elif(email!=cemail and pwd!=cpwd):
...     print("login failed due to pwd and mail")
... 
...     
login failed due to pwd and mail
>>> email="teju6486@gmail.com"
>>> pwd=123456
>>> otp=5689
>>> cemail=input("enter mail:")
enter mail: teju6486@gmail.com
>>> cpwd=int(input("enter a pass:"))
enter a pass:123456
>>> if(email==cemail and pwd==cpwd):
...     cotp=int(input("enter the otp:"))
...     if(otp==cotp):
...         print("ordered placed succesfully")
...     else:
...         print("ordered cancelled due to unsuccessfully")
... elif(email!=cemail and pwd==cpwd):
...     print("login failed due to mail")
... elif(email==cemail and pwd!=cpwd):
...     print("login failed due to pwd")
... elif(email!=cemail and pwd!=cpwd):
...     print("login failed due to pwd and mail")
... 
...     
login failed due to mail




