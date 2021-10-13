import turtle
import random

def drawing_fun(len):
    turtle.forward(len)
    turtle.left(90)
    turtle.forward(len)

def draw_square(len):
    x = 0
    while x < 4:
        x += 1
        turtle.left(90)
        turtle.forward(len)

def spiral_square(size,space):
    if size <= 0:
        return
    else:
        turtle.forward(size)
        turtle.left(90)
        spiral_square(size - space, space)

def star(len, n, step):
    if len <= 0:
        return
    else:
        turtle.forward(len)
        turtle.left(720/n)
        star(len - step, n, step)

def tree(len, n):
    if len >= 5:
        x = 1
        turtle.forward(len)
        turtle.left(60)
        tree(len / 2, n)
        while x < n:
            turtle.right(120 / (n - 1))
            tree(len / 2, n)
            x += 1
        tree(len / 2, n)
        turtle.left(60)
        turtle.forward(-len)

    else:
        #Stop the recursion
        return

def z (length, num):
    if num <= 0:
        return
    else:
        turtle.forward(length/2)
        turtle.right(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length/2)
        turtle.left(90)
        turtle.up()
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(5)
        turtle.down()
        z(length/2, num-1)

def main():
    turtle.speed(0)
    ##turtle.hideturtle()
    turtle.shape("turtle")
    turtle.pencolor("green")
    ##drawing_fun(100)
    ##z(150, 10)
    turtle.left(90)
    tree(100,5)
    ##star(100,9,1)
    ##draw_square(100)
    ##turtle.up()
    ##turtle.forward(120)
    ##turtle.width(4)
    ##turtle.down()
    ##turtle.pencolor("red")
    ##draw_square(100)
    ##turtle.up()
    ##turtle.forward(120)
    ##turtle.down()
    ##spiral_square(200,5)
    turtle.Screen().exitonclick()

main()