import time
import random
import turtle

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "pink", "brown", "cyan", "purple"]

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:  # Fixed the typo 'turtle' to 'turtles'
            distance = random.randint(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles.index(racer)]

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

def get_number_of_racers():
    while True:
        racers = input("Enter the number of Racers (2-10): ")

        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not valid... Try Again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range. Try Again! ")

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)  # Fixed appending the turtles to the 'turtles' list
    return turtles

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the turtle with the color: {winner}.")
# Removed time.sleep(5) as it's not necessary
