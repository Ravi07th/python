import turtle as t
import random as r
win = t.getscreen()
rr = t.Turtle()
win.bgcolor("black")
win.title("Square Project")
rr.speed(10)
rr.color("white")
c = ["red","skyblue","pink","yellow","orange","blue"]


#win.delay(100) # **** TIME TAKE FOR DRAW TURTLE ****#

#rr.ht() # **** HIDE ARROW(TURTLE) **** #

#win.tracer(25)  # ******* CONTROL SPEED OF  TURTLE ****#

def square(m,n):
  for i in range(4):
    r.shuffle(c)
    rr.color(c[0])
    rr.lt(n)
    rr.fd(m)

def square1(m,n):
    for i in range(90):
        square(m,n)
        rr.rt(20)
win.update()
        

