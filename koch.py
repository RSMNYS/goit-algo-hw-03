import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    # Get user input for the recursion level
    while True:
        try:
            order = int(input("Please enter the recursion level (order) for the Koch snowflake: "))
            if order < 0:
                print("Please enter a non-negative integer for the order.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Call the function with user input
    draw_koch(order)