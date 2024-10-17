import turtle

def draw_koch_curve(t, length, level):
    """
    Рекурсивная функция для рисования кривой Коха
    """
    if level == 0:
        t.forward(length)
    else:
        draw_koch_curve(t, length / 3, level - 1)
        t.left(60)
        draw_koch_curve(t, length / 3, level - 1)
        t.right(120)
        draw_koch_curve(t, length / 3, level - 1)
        t.left(60)
        draw_koch_curve(t, length / 3, level - 1)

def draw_koch_snowflake(t, length, level):
    """
    Рисует снежинку Коха, используя кривую Коха
    """
    for i in range(3):
        draw_koch_curve(t, length, level)
        t.right(120)

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

t.penup()
t.goto(-200, 0)
t.pendown()

draw_koch_snowflake(t, 400, 4)

screen.exitonclick()