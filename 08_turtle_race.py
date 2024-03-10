import time
import random
import turtle

# Store the width and height of the screen in variables to enable easy updating without code modification
WIDTH, HEIGHT = 500, 500
# Declare a list of colors for the turtles
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "pink", "brown", "cyan", "purple"]

# Define a function to start the turtle race, taking the available colors as input
def race(colors):
    # Create turtle objects using a function that prompts the user to input the number of racers
    turtles = create_turtles(colors)
    # Initiate a loop until a turtle crosses the finish line
    while True:
        for racer in turtles:
            # Determine a random distance for each turtle to move and then move it forward
            distance = random.randint(1, 20)
            racer.forward(distance)
            
            # Check if a turtle has reached or crossed the finish line
            x, y = racer.pos()
            # The finish line is set slightly below the halfway point of the screen's height
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]  # Return the color of the winning turtle

# Initialize the turtle screen
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

# Prompt the user to input the number of racers and validate the input
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

# Function to create turtle objects based on the provided colors
def create_turtles(colors):
    turtles = []
    # Calculate the spacing between turtles based on the screen width and the number of colors
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        # Create a new turtle object
        racer = turtle.Turtle()
        # Set the color and shape of the turtle
        racer.color(color)
        racer.shape("turtle")
        # Orient the turtle to face upward
        racer.left(90)
        racer.penup()
        # Set the initial position of the turtle based on the index and spacing between turtles
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

# Get the number of racers from the user and initialize the turtle screen
racers = get_number_of_racers()
init_turtle()

# Shuffle the list of colors and select the required number of colors for the race
random.shuffle(COLORS)
colors = COLORS[:racers]

# Start the race and store the color of the winning turtle
winner = race(colors)
print(f"The winner is the turtle with the color: {winner}.")
