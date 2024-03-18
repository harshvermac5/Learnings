import time
import winsound
import sys
from tqdm import tqdm

# Constants
WORK_DURATION = 25 * 60  # 25 minutes in seconds
BREAK_DURATION = 5 * 60   # 5 minutes break
LONG_BREAK_DURATION = 15 * 60  # 15 minutes break after two work sessions

def pomodoro_timer():
    work_sessions = 0

    while True:
        # Work session
        for _ in range(2):  # Run two work sessions
            pomodoro_session("Work", WORK_DURATION)
            work_sessions += 1

        # Take a long break after two work sessions
        if work_sessions % 2 == 0:
            pomodoro_session("Long Break", LONG_BREAK_DURATION)

def pomodoro_session(session_type, duration):
    try:
        # Use tqdm to show progress bar for the session duration
        for _ in tqdm(range(duration), desc=session_type, unit="s", ncols=100):
            time.sleep(1)

        # Play notification sound
        winsound.PlaySound("notification.wav", winsound.SND_FILENAME)

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nPomodoro interrupted. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    pomodoro_timer()
