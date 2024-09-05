# Import turtle and time
import turtle as t
import time as tm

#Get Current Time
hour = int(tm.strftime("%I"))
minute = int(tm.strftime("%M"))
second = int(tm.strftime("%S"))
am_pm = tm.strftime("%p")

#Define hours with its respectibe angle
hours = {1:30, 2:60, 3:90, 4:120, 5:150, 6:180, 7:210, 8:240, 9:270, 10:300, 11:330, 12:360,}

#Define minutes with its respective angle
minutes = {1: 6, 2: 12, 3: 18, 4: 24, 5: 30, 6: 36, 7: 42, 8: 48, 9: 54, 10: 60, 11: 66, 12: 72, 13: 78, 14: 84, 15: 90, 16: 96, 17: 102, 18: 108, 19: 114, 20: 120, 21: 126, 22: 132, 23: 138, 24: 144, 25: 150, 26: 156, 27: 162, 28: 168, 29: 174, 30: 180, 31: 186, 32: 192, 33: 198, 34: 204, 35: 210, 36: 216, 37: 222, 38: 228, 39: 234, 40: 240, 41: 246, 42: 252, 43: 258, 44: 264, 45: 270, 46: 276, 47: 282, 48: 288, 49: 294, 50: 300, 51: 306, 52: 312, 53: 318, 54: 324, 55: 330, 56: 336, 57: 342, 58: 348, 59: 354, 00:360}

t.getscreen() # Calling the screen
t.title("code by @himanshuaryan") # Title
t.bgcolor("black") #Set background color
t.speed(0) #Set speed of animation

#Draw two Circles
t.pu()
t.goto(0,-520)
t.pd()
t.fillcolor("darkgrey")
t.begin_fill()
t.circle(520)
t.end_fill()
t.pu()
t.goto(0,-380)
t.pd()
t.fillcolor("black")
t.begin_fill()
t.circle(380)
t.end_fill()

# Write number (1-12)
for num in range(1,13):
    t.pu()
    t.home()
    t.lt(90)
    t.rt(num*30)
    t.fd(450)
    t.pd()
    t.write(num, align="center", font=("fantasy",10))

#Define Displaying Time
def display_time(hour, minute, second):
    t.ht()
    t.pu()
    t.home()
    t.goto(-220,600)
    t.color("black","grey")
    t.begin_fill()
    for side in range(1,3): #draw rectangle
        t.fd(450)
        t.lt(90)
        t.fd(60)
        t.lt(90)
    t.end_fill()
    t.pd()
    t.write(f"   TIME = {hour}:{minute}:{second}  {am_pm}")
        

#Define Hour Hand    
def hour_hand(hour):
    angle = hours[hour]
    t.pensize(20)
    t.pu()
    t.home()
    t.lt(90)
    t.rt(angle)
    t.pd()
    t.pencolor("white")
    t.fd(200)

#Define Minute Hand    
def minute_hand(minute):
            angle = minutes[minute]
            t.pensize(13)
            t.pu()
            t.home()
            t.lt(90)
            t.rt(angle)
            t.pd()
            t.pencolor("green")
            t.fd(378)

#Define Second Hand   
def second_hand(second):
        while True:
            t.pensize(3)
            t.pu()
            t.home()
            t.lt(90)
            t.rt(second*6)
            t.pd()
            t.pencolor("red")
            t.fd(400)
            tm.sleep(0.6)
            t.undo()
            hour = int(tm.strftime("%I"))
            minute = int(tm.strftime("%M"))
            second = int(tm.strftime("%S"))
            am_pm = tm.strftime("%p")
            display_time(hour, minute, second)
            
        
hour_hand(hour)
minute_hand(minute)
second_hand(second)

t.mainloop()
