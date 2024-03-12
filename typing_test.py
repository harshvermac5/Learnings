import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()

def wpm_test(stdscr):
    target_text = "Hello"
    current_text = []

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
        key = stdscr.getkey()
        current_text.append(key)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target_text)

    for i, char in enumerate(current_text)

def main(stdscr):
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)