import turtle as t
import time as tm

hour = int(tm.strftime("%I"))
minute = int(tm.strftime("%M"))
second = int(tm.strftime("%S"))

t.title("code by @himanshuaryan")
t.Screen()
t.bgcolor("black")
t.color("yellow","red")
t.speed(0)
t.pu()
t.goto(0,-500)
t.pd()
t.begin_fill()
t.circle(500)
t.end_fill()
t.pu()
t.home()
t.goto(0,-400)
t.pd()
t.color("yellow","black")
t.begin_fill()
t.circle(400)
t.end_fill()

angel = 0
t.pu()
t.goto(-120,600)
t.pd()
t.write(f"TIME = {hour}:{minute}:{second}")

for num in range(1,13):
    t.pu()
    t.home()
    t.lt(90)
    t.rt(angel + (360/12))
    t.fd(450)
    t.write(num)
    t.home()
    angel+=(360/12)
    t.pd()
    
def hour_hand(hour):
    if (hour == 12):
        t.pensize(10)
        t.pu()
        t.home()
        t.lt(90)
        t.pd()
        t.fd(200)
    elif (hour == 1):
        t.pensize(10)
        t.pu()
        t.home()
        t.lt(60)
        t.pd()
        t.fd(200)
    elif (hour == 2):
        t.pensize(10)
        t.pu()
        t.home()
        t.lt(30)
        t.pd()
        t.fd(200)
    elif (hour == 3):
        t.pensize(10)
        t.pu()
        t.home()
        t.lt(0)
        t.pd()
        t.fd(200)
    elif (hour == 4):
        t.pensize(10)
        t.pu()
        t.home()
        t.rt(30)
        t.pd()
        t.fd(200)
    elif (hour == 5):
        t.pensize(10)
        t.pu()
        t.home()
        t.rt(60)
        t.pd()
        t.fd(200)
    elif (hour == 6):
        t.pensize(10)
        t.pu()
        t.home()
        t.rt(90)
        t.pd()
        t.fd(200)
    elif (hour == 7):
        t.pensize(10)
        t.pu()
        t.home()
        t.rt(120)
        t.pd()
        t.fd(200)
    elif (hour == 8):
        t.pensize(10)
        t.pu()
        t.home()
        t.rt(150)
        t.pd()
        t.fd(200)
    elif (hour == 9):
        t.pensize(10)
        t.pu()
        t.home()
        t.rt(180)
        t.pd()
        t.fd(200)
    elif (hour == 10):
        t.pensize(10)
        t.pu()
        t.home()
        t.lt(150)
        t.pd()
        t.fd(200)
    elif (hour == 11):
        t.pensize(10)
        t.pu()
        t.home()
        t.lt(120)
        t.pd()
        t.fd(200)
    
def minute_hand(min):
    if min == 1:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(6)
        t.pd()
        t.fd(400)
    elif min == 2:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(12)
        t.pd()
        t.fd(400)
    elif min == 3:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(18)
        t.pd()
        t.fd(400)
    elif min == 4:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(24)
        t.pd()
        t.fd(400)
    elif min == 5:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(30)
        t.pd()
        t.fd(400)
    elif min == 6:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(36)
        t.pd()
        t.fd(400)
    elif min == 7:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(42)
        t.pd()
        t.fd(400)
    elif min == 8:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(48)
        t.pd()
        t.fd(400)
    elif min == 9:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(54)
        t.pd()
        t.fd(400)
    elif min == 10:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(60)
        t.pd()
        t.fd(400)
    elif min == 11:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(66)
        t.pd()
        t.fd(400)
    elif min == 12:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(72)
        t.pd()
        t.fd(400)
    elif min == 13:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(78)
        t.pd()
        t.fd(400)
    elif min == 14:
        t.pensize(7)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(84)
        t.pd()
        t.fd(400)
    elif min == 15:
        t.pensize(7)
        t.pu()
        t.home()
        t.pd()
        t.fd(400)
    elif min == 16:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(6)
        t.pd()
        t.fd(400)
    elif min == 17:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(12)
        t.pd()
        t.fd(400)
    elif min == 18:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(18)
        t.pd()
        t.fd(400)
    elif min == 19:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(24)
        t.pd()
        t.fd(400)
    elif min == 20:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(30)
        t.pd()
        t.fd(400)
    elif min == 21:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(36)
        t.pd()
        t.fd(400)
    elif min == 22:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(42)
        t.pd()
        t.fd(400)
    elif min == 23:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(48)
        t.pd()
        t.fd(400)
    elif min == 24:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(54)
        t.pd()
        t.fd(400)
    elif min == 25:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(60)
        t.pd()
        t.fd(400)
    elif min == 26:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(66)
        t.pd()
        t.fd(400)
    elif min == 27:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(72)
        t.pd()
        t.fd(400)
    elif min == 28:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(78)
        t.pd()
        t.fd(400)
    elif min == 29:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(84)
        t.pd()
        t.fd(400)
    elif min == 30:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(90)
        t.pd()
        t.fd(400)
    elif min == 31:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(96)
        t.pd()
        t.fd(400)
    elif min == 32:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(102)
        t.pd()
        t.fd(400)
    elif min == 33:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(108)
        t.pd()
        t.fd(400)
    elif min == 34:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(114)
        t.pd()
        t.fd(400)
    elif min == 35:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(120)
        t.pd()
        t.fd(400)
    elif min == 36:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(126)
        t.pd()
        t.fd(400)
    elif min == 37:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(132)
        t.pd()
        t.fd(400)
    elif min == 38:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(138)
        t.pd()
        t.fd(400)
    elif min == 39:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(144)
        t.pd()
        t.fd(400)
    elif min == 40:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(150)
        t.pd()
        t.fd(400)
    elif min == 41:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(156)
        t.pd()
        t.fd(400)
    elif min == 42:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(162)
        t.pd()
        t.fd(400)
    elif min == 43:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(168)
        t.pd()
        t.fd(400)
    elif min == 44:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(174)
        t.pd()
        t.fd(400)
    elif min == 45:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(180)
        t.pd()
        t.fd(400)
    elif min == 46:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(186)
        t.pd()
        t.fd(400)
    elif min == 47:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(192)
        t.pd()
        t.fd(400)
    elif min == 48:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(198)
        t.pd()
        t.fd(400)
    elif min == 49:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(204)
        t.pd()
        t.fd(400)
    elif min == 50:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(210)
        t.pd()
        t.fd(400)
    elif min == 51:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(216)
        t.pd()
        t.fd(400)
    elif min == 52:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(222)
        t.pd()
        t.fd(400)
    elif min == 53:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(228)
        t.pd()
        t.fd(400)
    elif min == 54:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(234)
        t.pd()
        t.fd(400)
    elif min == 55:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(240)
        t.pd()
        t.fd(400)
    elif min == 56:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(246)
        t.pd()
        t.fd(400)
    elif min == 57:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(252)
        t.pd()
        t.fd(400)
    elif min == 58:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(258)
        t.pd()
        t.fd(400)
    elif min == 59:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(264)
        t.pd()
        t.fd(400)
    elif min == 00:
        t.pensize(7)
        t.pu()
        t.home()
        t.rt(270)
        t.pd()
        t.fd(400)
        
def second_hand(second):
        seconds = []
        for s in range(0,360,6):
            seconds.append(s+1)
        angle = seconds[second]
        t.pensize(3)
        t.pu()
        t.home()
        t.lt(90)
        t.rt(angle)
        t.pd()
        t.fd(400)
        
    
hour_hand(hour)
minute_hand(minute)
second_hand(second)


t.mainloop()
