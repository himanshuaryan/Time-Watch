import turtle as t
import time as tm

hour = int(tm.strftime("%I"))
minute = int(tm.strftime("%M"))
second = int(tm.strftime("%S"))
am_pm = tm.strftime("%p")

hours = {1:30, 2:60, 3:90, 4:120, 5:150, 6:180, 7:210, 8:240, 9:270, 10:300, 11:330, 12:360,}

minutes = {1: 6, 2: 12, 3: 18, 4: 24, 5: 30, 6: 36, 7: 42, 8: 48, 9: 54, 10: 60, 11: 66, 12: 72, 13: 78, 14: 84, 15: 90, 16: 96, 17: 102, 18: 108, 19: 114, 20: 120, 21: 126, 22: 132, 23: 138, 24: 144, 25: 150, 26: 156, 27: 162, 28: 168, 29: 174, 30: 180, 31: 186, 32: 192, 33: 198, 34: 204, 35: 210, 36: 216, 37: 222, 38: 228, 39: 234, 40: 240, 41: 246, 42: 252, 43: 258, 44: 264, 45: 270, 46: 276, 47: 282, 48: 288, 49: 294, 50: 300, 51: 306, 52: 312, 53: 318, 54: 324, 55: 330, 56: 336, 57: 342, 58: 348, 59: 354, 00:360}

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
t.write(f"TIME = {hour}:{minute}:{second}  {am_pm}")

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
    angle = hours[hour]
    t.pensize(20)
    t.pu()
    t.lt(90)
    t.rt(angle)
    t.pd()
    t.color("white","yellow")
    t.fd(200)
def minute_hand(minute):
            angle = minutes[minute]
            t.pensize(13)
            t.pu()
            t.home()
            t.lt(90)
            t.rt(angle)
            t.pd()
            t.color("green","yellow")
            t.fd(400)
        
def second_hand(second):
        seconds = []
        
        for s in range(0,360,6):
            seconds.append(s+1)
        angle = seconds[second]
        while True:
            t.pensize(3)
            t.pu()
            t.home()
            t.lt(90)
            t.rt(angle)
            t.pd()
            t.color("cyan","yellow")
            t.fd(400)
            tm.sleep(1)
            t.undo()
            angle += 360/60
        
    
hour_hand(hour)
minute_hand(minute)
second_hand(second)


t.mainloop()