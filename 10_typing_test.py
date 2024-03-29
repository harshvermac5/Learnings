# curses module enable using of Text based UI in terminal
import curses
# wrapper function is the rescource management utility for the curses module
from curses import wrapper
import time
import random

# function that displays the start screen
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Test.")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh() # refresh / update the screen

# function that loads the actual test from the text file
def load_test():
    with open("text.txt", "r") as f:
        lines = f.readlines() # returns list of the lines
        return random.choice(lines).strip() # strips the white space in the last of lines

# function to initialise the test
def wpm_test(stdscr):
    target_text = load_test() # opens the text file
    current_text = [] # empty list to store the user inputs
    wpm = 0 # wpm counter
    start_time = time.time() # current time
    stdscr.nodelay(True) # enables capturing of key

    while True:
        time_elapsed = time.time() - start_time # checks the difference between current and start time
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) # 5 is the average character length, dividing by this gives the words per minute from the former character per minute

        stdscr.clear() # clears the screen
        display_text(stdscr, target_text, current_text, wpm) # initialise the display_text function
        stdscr.refresh() # refreshes the screen

        if "".join(current_text) == target_text: # checks whether the entered text is equals to target text
            stdscr.nodelay(False) # if yes, then stop the the capturing of the key and break out of loop
            break

        # to continue the program running, even in the case of no input is provided
        try:
            key = stdscr.getkey()
        except KeyboardInterrupt:
            break
        
        if ord(key) == 27: # 27 is ASCII for Escape, if pressed break the loop
            break
        # delete the last word, if backspace or delete key is pressed
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        # limiting the entry of user input to the target text, to save from index out of range error
        elif len(current_text) < len(target_text):
            current_text.append(key)

# function to display the target text which is explained previously in wpm test
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}") # setting the coordinates to display, from 2nd line (1 as index) and from the first character (0 as index)

    # changing the color of the text, depending on correct or incorrect input
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

# main function with color and program attributes stored
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the test, Press any key to continue...")
        stdscr.refresh()
        stdscr.getkey() # asking user to exit the loop
        break
# initialising the curses enviroment
wrapper(main)