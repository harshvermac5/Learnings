import curses
from curses import wrapper
import time
import queue

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(5,0,"Hello")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)