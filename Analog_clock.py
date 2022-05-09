# ABEL YOHANNES
# SECTION 2
# UGR/ 8254 / 12

import turtle
import time
import os.path

lift = turtle.Screen()
lift.title("clock")

lift.tracer(0)
lift.bgpic(os.path.expanduser('D:\\Turtle_time\\naruto.gif'))
# please do use this image from your path it is worth the drag :)


q = turtle.Turtle()
q.speed(10)



def clock():
    q.color('white')

    q.home()
    q.penup()
    q.goto(-300, -160)
    q.pendown()
    q.right(90)
    for zigzag in range(24):
        q.forward(50)
        q.left(35)
        q.forward(50)
        q.right(20)




    q.penup()
    q.goto(50, -110)




    q.home()
    q.goto(60, -400)
    q.pendown()
    q.circle(300)




    q.penup()
    q.goto(50, -110)
    q.pendown()
    q.left(90)

    for hour_no in range(12):
        q.right(360 / 12)
        q.penup()
        q.pensize(10)
        q.forward(330)

        q.color('white')
        q.write((hour_no + 1), font=("arial", 25, "italic"))
        q.goto(50, -110)

    q.penup()
    for minute_points in range(60):
        q.right(360 / 60)
        q.forward(320)
        q.color('yellow')
        q.pensize(3)
        q.write('.', font=("arial", 20, "bold"))
        q.goto(50, -110)

    q.penup()
    q.goto(-30,-280)
    q.color('black')
    q.write("Rolex...not really", font= ("times new roman", 25 , "italic bold"))
    q.penup()
    q.goto(50, -110)

def outer(h, m, s):

    each_hand = [("yellow", 12, 125), ("green", 60, 250), ("white", 60, 270)]
    # hours, minutes and seconds respectively in the function and the each_hand inference
    all_hashes = (h, m, s)
    for line_hash in each_hand:
        each_time_difference = all_hashes[each_hand.index(line_hash)]
        angle = (each_time_difference / line_hash[1]) * 360
        q.penup()
        q.goto(50, -110)
        q.color(line_hash[0])
        q.setheading(90)
        q.right(angle)
        q.pendown()
        q.pensize(7)
        q.forward(line_hash[2])
        for i in range (6):
            q.color('indigo')
            q.right(90)
            q.forward(10)
            q.backward(20)
            q.left(45)
            q.forward(10)

    q.penup()
    q.goto(50, -110)



q.penup()
q.goto(50, -110)
q.right(180)

while True:
    q.shape("turtle")   
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    clock()
    outer(h, m, s)
    lift.update()
    time.sleep(0.9)
    q.undo()
    q.clear()





lift.mainloop()
 

