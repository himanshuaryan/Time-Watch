from turtle import *
import time as tm

def gt(x, y):
    """Goes to the specified coordinates (x, y) without drawing a line."""
    pu()
    goto(x, y)
    pd()

def pol(x, y, width, length, fillcolor, pencolor="white"):
    """Draws a polygon with the given coordinates, dimensions, and colors."""
    gt(x, y)
    color(pencolor, fillcolor)
    begin_fill()
    for i in range(2):
        fd(width)
        lt(90)
        fd(length)
        lt(90)
    end_fill()

def layout():
    """Draws the background and labels for the clock."""
    pol(-500, -500, 1000, 800, "darkgrey")  # Draw the background
    pol(-480, 10, 960, 270, "black")  # Draw the hour hand label
    pol(-480, -300, 960, 290, "black")  # Draw the minute hand label
    gt(-390, 20)
    pencolor("lightgreen")
    write("HOUR", font=("Arial", 10, "bold"))
    gt(-20, 20)
    write("MIN", font=("Arial", 10, "bold"))
    gt(305, 40)
    format = tm.strftime("%p")
    write(format, font=("Arial", 10, "bold"))

def greet(h):
    """Writes a greeting message based on the current hour (h)."""
    pencolor("aqua")
    gt(-400, -480)
    if 6 <= h <= 11:
        write("Good Morning", font=("Fantasy", 20, "bold"))
    elif 12 <= h <= 16:
        write("Good Afternoon", font=("Fantasy", 20, "bold"))
    elif 17 <= h <= 21:
        write("Good Evening", font=("Fantasy", 20, "bold"))
    else:
        write("Good Night", font=("Fantasy", 20, "bold"))

def display_date(day, date, month, m_n, year):
    """Displays the current date."""
    pencolor("lightgreen")
    gt(-450, -130)
    write(day, font=("Arial", 12, "bold"))
    gt(-100, -130)
    write(m_n, font=("Arial", 12, "bold"))
    gt(-400, -260)
    pencolor("red")
    write(date, font=("Arial", 18, "bold"))
    gt(0, -260)
    write(month, font=("Arial", 18, "bold"))
    gt(320, -150)
    write(20, font=("Arial", 18, "bold"))
    gt(320, -260)
    write(year, font=("Arial", 18, "bold"))

def display_time(hour, minute, second):
    """Displays the current time."""
    gt(-420, 70)
    pencolor("red")
    write(hour, font=("Arial", 30))
    gt(-70, 70)
    pencolor("red")
    write(minute, font=("Arial", 30))
    gt(300, 125)
    pencolor("green")
    write(second, font=("Arial", 15))

def main():
    """The main function that controls the clock's execution."""
    
    #Set screen
    getscreen()
    bgcolor("black")
    pensize(3)
    speed(0)
    tracer(2, 10)
    hideturtle()
    gt(-400, 400)
    pencolor("skyblue")
    write("DIGITAL CLOCK", font=("Arial",20,'bold'))
    pencolor('black')
    
    #Execute Current Date
    hh = int(tm.strftime("%H")) # 24 - Hour
    day = (tm.strftime("%A"))
    date = int(tm.strftime("%d"))
    month = int(tm.strftime("%m"))
    m_n = (tm.strftime("%B"))
    year = int(tm.strftime("%y"))
    
    layout()  # Draw the layout
    display_date(day, date, month, m_n, year)  # Display the date
    greet(hh)  # Display the greeting message

    while True:
        hour = int(tm.strftime("%I"))
        minute = int(tm.strftime("%M"))
        second = int(tm.strftime("%S"))
        display_time(hour, minute, second)  # Display the time
        undo()  # Undo second
        tm.sleep(0.7)
        if second == 59:
            pol(-70,100,200,150,"black","black")
            if minute == 59:
                pol(-420,100,200,150,"black","black")

if __name__ == "__main__":
    main()
mainloop()
