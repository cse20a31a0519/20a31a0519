Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(1,150):
     if(i%10==0):
         print(i)

         
10
20
30
40
50
60
70
80
90
100
110
120
130
140
for i in range(1,6,2):
    print(i*5)

    
5
15
25
for i in range(-10,0):
    print(i)

    
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
for i in range(-10,0,2):
    print(i)

    
-10
-8
-6
-4
-2
for i in range(1,6):
    for j in range(1,6):
        if(i==j):
            print("*")

            
*
*
*
*
*
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

    
* 

* * 

* * * 

* * * * 

* * * * * 

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")

    
1 

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5 

for i in range(97,123):
    for j in range(1,i+1):
        print(chr(j),end=" ")
    print("\n")

    
        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y 

        	 
 
 
 
               
 
 
    ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z 


for i in range(97,123):
    for j in range(97,i+1):
            print(chr(j),end=" ")

    
a a b a b c a b c d a b c d e a b c d e f a b c d e f g a b c d e f g h a b c d e f g h i a b c d e f g h i j a b c d e f g h i j k a b c d e f g h i j k l a b c d e f g h i j k l m a b c d e f g h i j k l m n a b c d e f g h i j k l m n o a b c d e f g h i j k l m n o p a b c d e f g h i j k l m n o p q a b c d e f g h i j k l m n o p q r a b c d e f g h i j k l m n o p q r s a b c d e f g h i j k l m n o p q r s t a b c d e f g h i j k l m n o p q r s t u a b c d e f g h i j k l m n o p q r s t u v a b c d e f g h i j k l m n o p q r s t u v w a b c d e f g h i j k l m n o p q r s t u v w x a b c d e f g h i j k l m n o p q r s t u v w x y a b c d e f g h i j k l m n o p q r s t u v w x y z 
for i in range(97,123):
     for j in range(97,i+1):
         print(chr(j),end=" ")
     print("\n")

     
a 

a b 

a b c 

a b c d 

a b c d e 

a b c d e f 

a b c d e f g 

a b c d e f g h 

a b c d e f g h i 

a b c d e f g h i j 

a b c d e f g h i j k 

>>> a b c d e f g h i j k l 
>>> 
... a b c d e f g h i j k l m 
... 
... a b c d e f g h i j k l m n 
... 
... a b c d e f g h i j k l m n o 
... 
... a b c d e f g h i j k l m n o p 
... 
a b c d e f g h i j k l m n o p q 
>>> 
>>> a b c d e f g h i j k l m n o p q r 
... 
... a b c d e f g h i j k l m n o p q r s 
... 
... a b c d e f g h i j k l m n o p q r s t 
... 
... a b c d e f g h i j k l m n o p q r s t u 
... 
a b c d e f g h i j k l m n o p q r s t u v 
>>> 
>>> a b c d e f g h i j k l m n o p q r s t u v w 
... 
... a b c d e f g h i j k l m n o p q r s t u v w x 
... 
... a b c d e f g h i j k l m n o p q r s t u v w x y 
... 
... a b c d e f g h i j k l m n o p q r s t u v w x y z 
... 
... for i in range(97,123,2):
    for j in range(97,i):
        print(chr(i),end=" ")
    print("\n")

    


c c 

e e e e 

g g g g g g 

i i i i i i i i 

k k k k k k k k k k 

m m m m m m m m m m m m 

o o o o o o o o o o o o o o 

q q q q q q q q q q q q q q q q 

s s s s s s s s s s s s s s s s s s 

u u u u u u u u u u u u u u u u u u u u 

w w w w w w w w w w w w w w w w w w w w w w 

y y y y y y y y y y y y y y y y y y y y y y y y 

for i in range(97,123,2):
    for j in range(97,i+1):
        print(chr(i),end=" ")
    print("\n")

    
a 

c c c 

e e e e e 

g g g g g g g 

i i i i i i i i i 

k k k k k k k k k k k 

m m m m m m m m m m m m m 

o o o o o o o o o o o o o o o 

q q q q q q q q q q q q q q q q q 

s s s s s s s s s s s s s s s s s s s 

u u u u u u u u u u u u u u u u u u u u u 

w w w w w w w w w w w w w w w w w w w w w w w 

y y y y y y y y y y y y y y y y y y y y y y y y y 

for i in range(97,123,2):
    for j in range(97,i-1):
        print(chr(i),end=" ")
    print("\n")

    


c 

e e e 

g g g g g 

i i i i i i i 

k k k k k k k k k 

m m m m m m m m m m m 

o o o o o o o o o o o o o 

q q q q q q q q q q q q q q q 
