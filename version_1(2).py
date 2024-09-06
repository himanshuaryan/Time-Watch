# Import turtle and time
import turtle as t
import time as tm

#Draw two Circles
def draw_clock(radius1, radius2, tick_length):
    t.pu()
    t.goto(0,-radius1)
    t.pd()
    t.color("black","darkgrey")
    t.begin_fill()
    t.circle(radius1)
    t.end_fill()
    t.pu()
    t.home()
    t.goto(0,-radius2)
    t.pd()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(radius2)
    t.end_fill()
    
    #draw tick mark on watch which shows minutes or seconds
    for i in range(60):
        angle = i * 6
        t.penup()
        t.home()
        t.left(90)
        t.right(angle)
        t.forward(radius2 - tick_length)
        t.pendown()
        t.pencolor("grey")
        t.pensize(3)
        t.forward(tick_length)

# Write number (1-12)
def clock_numbers(distance):
    for num in range(1,13):
        t.pu()
        t.home()
        t.goto(0,-25)
        t.lt(90)
        t.rt(num*30)
        t.fd(distance)
        t.pd()
        t.pencolor("black")
        t.write(num, align="center", font=("fantasy",12))

#Define Displaying Time
def display_time(hour, minute, second, am_pm):
    
    t.pu()
    t.home()
    t.goto(-220,600)
    t.pd()
    t.color("black","lightgrey")
    t.begin_fill()
    for side in range(2): #draw rectangle
        t.fd(450)
        t.lt(90)
        t.fd(60)
        t.lt(90)
    t.end_fill()
    t.pencolor("red")
    t.write(f" TIME = {hour}:{minute}:{second}  {am_pm}")
        

#Define Hour Hand    
def draw_hands(hour, minute, second):
     
    #Hour Hand
    t.pu()
    t.home()
    t.lt(90)
    t.rt(hour*60)
    t.pd()
    t.pensize(20)
    t.pencolor("white")
    t.fd(200)
    
    #Minute Hand    
    t.pu()
    t.home()
    t.lt(90)
    t.rt(minute*6)
    t.pd()
    t.pensize(13)
    t.pencolor("green")
    t.fd(365)
     
    #Second Hand
    t.pensize(3)
    t.pu()
    t.home()
    t.lt(90)
    t.rt(second*6)
    t.pd()
    t.pencolor("cyan")
    t.fd(400)
     

def main():
    
    #Set Screen
    t.getscreen() # Calling the screen
    t.title("code by @himanshuaryan") # Title
    t.bgcolor("black") #Set background color
    t.speed(0) #Set speed of animation
    t.hideturtle()
    
    #Clock Parameters
    radius1 = 500
    radius2 = 400
    tick_length = 15
    distance = 450
    
    #Display Time
    hour = int(tm.strftime("%I"))
    minute = int(tm.strftime("%M"))
    second = int(tm.strftime("%S"))
    am_pm = tm.strftime("%p")
    display_time(hour, minute, second, am_pm)
    
    #draw Clock
    draw_clock(radius1, radius2, tick_length)
    clock_numbers(distance)
    
    while True:
        # Get the current time
        hour = int(tm.strftime("%I"))
        minute = int(tm.strftime("%M"))
        second = int(tm.strftime("%S"))
        display_time(hour, minute, second, am_pm)
        
        if second == 0:
            t.pu()
            t.home()
            t.goto(0,-371)
            t.pd()
            t.color("black","black")
            t.begin_fill()
            t.circle(370)
            t.end_fill()

        # Clear the hands and draw the new ones
        t.penup()
        t.home()
        t.pendown()
        draw_hands(hour, minute, second)
        tm.sleep(0.2)
        t.undo()
        
        
if __name__=="__main__":
    main()

t.mainloop()
