from turtle import *
import time as tm

def gt(x,y):
    pu()
    goto(x,y)
    pd()

def pol(x, y, width, length, fillcolor, pencolor = "white"):
    gt(x,y)
    color(pencolor,fillcolor)
    begin_fill()
    for i in range(2):
        fd(width)
        lt(90)
        fd(length)
        lt(90)
    end_fill()

def layout():
    pol(-500,-500,1000,800,"darkgrey")
    pol(-480,10,960,270,"black")
    pol(-480,-300,960,290,"black")
    gt(-390,20)
    pencolor("lightgreen")
    write("HOUR", font=("Arial",10,"bold"))
    gt(-20,20)
    write("MIN", font=("Arial",10,"bold"))
    gt(305,40)
    format = tm.strftime("%p")
    write(format,font=("Arial",10,"bold"))

def greet(h):
    pencolor("aqua")
    gt(-400,-480)
    if ((h>=6) and (h<=11)):
                write("Good Morning", font=("Fantasy",20,"bold"))
    elif ((h>=12) and (h<=16)):
                write("Good Afternoon", font=("Fantasy",20,"bold"))
    elif h>=17 and h<=21:
                write("Good Evening", font=("Fantasy",20,"bold"))
    elif h>=22 and h<=23:
                write("Good Night", font=("Fantasy",20,"bold"))
    elif h>=00 and h<=5:
                write("Good Night", font=("Fantasy",20,"bold"))
       
def dating(day,date,month,m_n,year):
     pencolor("lightgreen")
     gt(-450,-130)
     write(day, font=("Arial",12,"bold"))
     gt(-100,-130)
     write(m_n, font=("Arial",12,"bold"))
     gt(-400,-260)
     pencolor("red")
     write(date, font=("Arial",18,"bold"))
     gt(0,-260)
     write(month, font=("Arial",18,"bold"))
     gt(320,-150)
     write(20, font=("Arial",18,"bold"))
     gt(320,-260)
     write(year, font=("Arial",18,"bold"))

def show(hour, minute, second):
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
    
    getscreen()
    bgcolor("black")
    pensize(3)
    speed(0)
    tracer(2,10)
    hideturtle()
    
    hour = int(tm.strftime("%I"))
    hh = int(tm.strftime("%H"))
    minute = int(tm.strftime("%M"))
    second = int(tm.strftime("%S"))
    day = (tm.strftime("%A"))
    date = int(tm.strftime("%d"))
    month = int(tm.strftime("%m"))
    m_n = (tm.strftime("%B"))
    year = int(tm.strftime("%y"))
    
    layout()
    dating(day,date,month,m_n,year)
    greet(hh)
    
    while True:
        hour = int(tm.strftime("%I"))
        minute = int(tm.strftime("%M"))
        second = int(tm.strftime("%S"))
        show(hour, minute, second)
        tm.sleep(0.7)
        undo()
        if second == 59:
            pol(-70,100,200,150,"black","black")
            if minute == 59:
                pol(-420,100,200,150,"black","black")
    
if __name__ == "__main__":
    main()
mainloop()
