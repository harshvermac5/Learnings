import time

current_time = time.time()
print(f"Current time in seconds is {current_time}.")

current_time = time.localtime()

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(f"Current time in regular format is {formatted_time}")

current_time = time.time()
utc_time = time.gmtime(current_time)
local_time = time.localtime(current_time)

print("UTC time:", utc_time)
print("Local time:", local_time)

while True:
    time.sleep(3)
    print("Three seconds have been passed!")