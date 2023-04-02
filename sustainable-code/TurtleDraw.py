import turtle


def draw_trash_bin(x, color, label):
    """Draw a trash bin at the specified x-coordinate with the specified color and label.

    Args:
        x (int): The x-coordinate of the trash bin
        color (str): The color of the trash bin
        label (str): The label of the trash bin

    Returns:
        None
    """
    t.speed(5)
    t.color(color)

    t.penup()
    t.goto(x - 50, 0)
    t.pendown()

    t.begin_fill()
    t.goto(x + 50, 0)
    t.goto(x + 50, -100)
    t.goto(x - 50, -100)
    t.goto(x - 50, 0)
    t.end_fill()

    t.begin_fill()
    t.penup()
    t.goto(x - 30, 0)
    t.pendown()
    t.goto(x + 30, 0)
    t.goto(x + 25, 10)
    t.goto(x - 25, 10)
    t.goto(x - 30, 0)
    t.end_fill()

    t.color("white")
    t.penup()
    t.goto(x, -40)
    t.pendown()
    t.circle(10)
    t.penup()
    t.goto(x, -33)
    t.pendown()
    t.circle(3)

    t.color("black")
    t.penup()
    t.goto(x, -80)
    t.write(label, align="center", font=("Arial", 16, "bold"))

    t.hideturtle()


t = turtle.Turtle()
draw_trash_bin(-100, "blue", "Recycle")
draw_trash_bin(100, "green", "Trash")

t.penup()
t.goto(0, 60)
t.write("Recycle for a Better Future", align="center", font=("Arial", 16, "bold"))
t.hideturtle()

turtle.done()
