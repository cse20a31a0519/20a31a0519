Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: C:/Users/revat/Desktop/day_6/day_6project.py ============
player 1 choice (X or O):X
Traceback (most recent call last):
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 69, in <module>
    play_game()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 56, in play_game
    printf(f"player 1:{m1},player2:{m2}")
NameError: name 'printf' is not defined. Did you mean: 'print'?

============= RESTART: C:/Users/revat/Desktop/day_6/day_6project.py ============
player 1 choice (X or O):X
player 1:X,player2:O
||
------------
||
------------
||
enter coordinates:00
Traceback (most recent call last):
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 69, in <module>
    play_game()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 60, in play_game
    x,y = get_coordinates()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 21, in get_coordinates
    x,y=list(map(int,input("enter coordinates:").split()))
ValueError: not enough values to unpack (expected 2, got 1)

============= RESTART: C:/Users/revat/Desktop/day_6/day_6project.py ============
player 1 choice (X or O):X
player 1:X,player2:O
||
------------
||
------------
||
enter coordinates:01
Traceback (most recent call last):
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 69, in <module>
    play_game()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 60, in play_game
    x,y = get_coordinates()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 21, in get_coordinates
    x,y=list(map(int(input("enter coordinates:").split())))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

================================================= RESTART: C:/Users/revat/Desktop/day_6/day_6project.py =================================================
player 1 choice (X or O):X
player 1:X,player2:O
  |    |  
------------
  |    |  
------------
  |    |  
enter coordinates:0 1
Traceback (most recent call last):
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 69, in <module>
    play_game()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 60, in play_game
    x,y = get_coordinates()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 21, in get_coordinates
    x,y=list(map(int(input("enter coordinates:").split())))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

================================================= RESTART: C:/Users/revat/Desktop/day_6/day_6project.py =================================================
player 1 choice (X or O):o
player 1:O,player2:X
  |    |  
------------
  |    |  
------------
  |    |  
enter coordinates:1 1
Traceback (most recent call last):
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 69, in <module>
    play_game()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 60, in play_game
    x,y = get_coordinates()
  File "C:/Users/revat/Desktop/day_6/day_6project.py", line 21, in get_coordinates
    x,y=list(map(int(input("enter coordinates:").split())))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> 
================================================= RESTART: C:/Users/revat/Desktop/day_6/day_6project.py =================================================
Player 1 choice(X or O):x
player 1:X,player 2:0
||
---------
||
---------
||
Enter the cordinaTES:1 0
||
---------
X||
---------
||
Enter the cordinaTES:2 0
||
---------
X||
---------
0||
Enter the cordinaTES:0 2
||X
---------
X||
---------
0||
Enter the cordinaTES:1 0
||X
---------
0||
---------
0||
Enter the cordinaTES:0 1
|X|X
---------
0||
---------
0||
Enter the cordinaTES:0 0
Player 2 wins
