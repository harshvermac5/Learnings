from tqdm import tqdm
import time

# Iterate over a list with tqdm
my_list = [1, 2, 3, 4, 5]
for item in tqdm(my_list):
    time.sleep(0.5)  # Simulate some work
