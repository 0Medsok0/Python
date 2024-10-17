import turtle
import time

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(t, instructions, angle, distance):
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]
    color_index = 0
    start_time = time.time()
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
            if time.time() - start_time >= 5:
                color_index = (color_index + 1) % len(colors)
                t.pencolor(colors[color_index])
                start_time = time.time()
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)


def main(iterations, axiom, rules, angle, length=2, size=1, y_offset=0,
        x_offset=0, offset_angle=0, width=450, height=450):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()
    wn.exitonclick()


main(iterations=15, axiom="FX+FX+FX", rules={"X":"X+YF+", "Y":"-FX-Y"}, angle=90)