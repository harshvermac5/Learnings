import time
import winsound

def pomodoro_timer():
    work_duration = 25 * 60  # 25 minutes in seconds
    break_duration = 5 * 60  # 5 minutes break

    while True:
        # Work session
        print("Work for 25 minutes.")
        time.sleep(work_duration)
        
        # Play sound notification
        winsound.PlaySound("notification.wav", winsound.SND_FILENAME)

        # Break session
        print("Take a 5-minute break.")
        time.sleep(break_duration)

if __name__ == "__main__":
    pomodoro_timer()

