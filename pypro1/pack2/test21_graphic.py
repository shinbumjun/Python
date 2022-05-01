'''
[참고]
https://docs.python.org/3/library/
https://docs.python.org/3/library/turtle.html
'''
from turtle import *

p = Pen() # pen 객체가 만들어짐 (펜을 준다)

p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()


















