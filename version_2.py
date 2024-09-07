import turtle as t
import time as tm

# Draw two Circles
def draw_clock(radius1, radius2, tick_length):
    t.pu()
    t.goto(0, -radius1)
    t.pd()
    t.color("black", "darkgrey")
    t.begin_fill()
    t.circle(radius1)
    t.end_fill()
    t.pu()
    t.home()
    t.goto(0, -radius2)
    t.pd()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(radius2)
    t.end_fill()

    # Draw tick marks on the watch which shows minutes or seconds
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

# Write numbers (1-12)
def clock_numbers(distance):
    for num in range(1, 13):
        t.pu()
        t.home()
        t.goto(0, -25)
        t.lt(90)
        t.rt(num * 30)
        t.fd(distance)
        t.pd()
        t.pencolor("black")
        t.write(num, align="center", font=("fantasy", 12))

# Define displaying time
def display_time(hour, minute, second, am_pm):

    t.pu()
    t.home()
    t.goto(-220, 600)
    t.pd()
    t.color("black", "lightgrey")
    t.begin_fill()
    for side in range(2):  # draw rectangle
        t.fd(450)
        t.lt(90)
        t.fd(60)
        t.lt(90)
    t.end_fill()
    t.pencolor("red")
    t.write(f" TIME = {hour}:{minute}:{second}  {am_pm}")


# Define hour hand
def draw_hands(hour, minute, second, am_pm):
    
    display_time(hour, minute, second, am_pm)
     
    # Hour Hand
    t.pu()
    t.home()
    t.lt(90)
    t.rt(hour * 30)
    t.pd()
    t.pensize(20)
    t.pencolor("white")
    t.fd(200)

    # Minute Hand
    t.pu()
    t.home()
    t.lt(90)
    t.rt(minute * 6)
    t.pd()
    t.pensize(13)
    t.pencolor("green")
    t.fd(300)

    # Second Hand
    t.pensize(3)
    t.pu()
    t.home()
    t.lt(90)
    t.rt(second * 6)
    t.pd()
    t.pencolor("cyan")
    t.fd(360)

#define function which creates new hands
def new_hands(radius):
    t.pu()
    t.home()
    t.goto(0, -(radius-30))
    t.pd()
    t.color("black", "black")
    t.begin_fill()
    t.circle(radius-30)
    t.end_fill()
        
def main():

    # Set Screen
    t.getscreen()  # Calling the screen
    t.title("code by @himanshuaryan")  # Title
    t.bgcolor("black")  # Set background color
    t.tracer(0, 10)  # Set tracer(0, 10) for smoother animation

    # Clock Parameters
    radius1 = 500
    radius2 = 400
    tick_length = 15
    distance = 450

    # Draw Clock
    draw_clock(radius1, radius2, tick_length)
    clock_numbers(distance)

    while True:
       new_hands(radius2)
       
       # Display Time
       hour = int(tm.strftime("%I"))
       minute = int(tm.strftime("%M"))
       second = int(tm.strftime("%S"))
       am_pm = tm.strftime("%p")
    
       # Clear the hands and draw the new ones
       t.penup()
       t.home()
       t.pendown()
       draw_hands(hour, minute, second, am_pm)
       tm.sleep(0.4)
       t.update()  # Update the screen after drawing the hands

if __name__ == "__main__":
    main()

t.mainloop()
