import os
import shutil
import datetime
import schedule
import time
import tkinter as tk
from tkinter import filedialog, ttk

def select_directories():
    root = tk.Tk()
    root.withdraw()  

    source_dir = filedialog.askdirectory(title="Select Source Directory")
    destination_dir = filedialog.askdirectory(title="Select Destination Directory")

    return source_dir, destination_dir

def select_backup_time():
    root = tk.Tk()
    root.title("Select Backup Time and Frequency")

    # Frame for time selection
    time_frame = ttk.LabelFrame(root, text="Backup Time")
    time_frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # Hour selection
    ttk.Label(time_frame, text="Hour:").grid(row=0, column=0, padx=5, pady=5)
    # conversion of number into string and zfill make sure that it always two digits long
    hour_combobox = ttk.Combobox(time_frame, values=[str(i).zfill(2) for i in range(24)])
    hour_combobox.grid(row=0, column=1, padx=5, pady=5)
    # sets the initial value to 00
    hour_combobox.set("00")

    # Minute selection
    ttk.Label(time_frame, text="Minute:").grid(row=1, column=0, padx=5, pady=5)
    minute_combobox.grid(row=1, column=1, padx=5, pady=5)
    # conversion of number into string and zfill make sure that it always two digits long
    minute_combobox = ttk.Combobox(time_frame, values=[str(i).zfill(2) for i in range(60)])
    # setting the initial value to 00
    minute_combobox.set("00")

    # Frequency selection
    freq_frame = ttk.LabelFrame(root, text="Backup Frequency")
    freq_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    freq_combobox = ttk.Combobox(freq_frame, values=["Daily", "Weekly", "Monthly"])
    freq_combobox.grid(row=0, column=0, padx=5, pady=5)
    # setting the default value to Daily
    freq_combobox.set("Daily")

    # Function to retrieve selected values
    def get_values():
        hour = hour_combobox.get()
        minute = minute_combobox.get()
        freq = freq_combobox.get()
        root.destroy()  # Close the window after getting values
        return hour, minute, freq

    # Button to confirm selections
    confirm_button = ttk.Button(root, text="Confirm", command=get_values)
    confirm_button.grid(row=2, column=0, padx=10, pady=10)

    root.mainloop()

def schedule_backup():
    source_dir, destination_dir = select_directories()
    hour, minute, freq = select_backup_time()

    def copy_to_folder(source, dest):
        today = datetime.date.today()
        dest_dir = os.path.join(dest, str(today))

        try:
            shutil.copytree(source, dest_dir)
            print(f"Folder copied to: {dest_dir}")

        except FileExistsError:
            print(f"Folder Already exists in: {dest}")

    # Adjust scheduling logic based on frequency
    if freq == "Daily":
        schedule.every().day.at(f"{hour}:{minute}").do(lambda: copy_to_folder(source_dir, destination_dir))
    elif freq == "Weekly":
        schedule.every().week.day.at(f"{hour}:{minute}").do(lambda: copy_to_folder(source_dir, destination_dir))
    elif freq == "Monthly":
        # Schedule on the first day of every month
        schedule.every().month.at("01").do(lambda: copy_to_folder(source_dir, destination_dir))

# running the code infinitely in order to do scheduled backups
while True:
    schedule_backup()
    schedule.run_pending()
    time.sleep(60)
