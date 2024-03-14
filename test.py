import sys
import time

print("Downloading file...", end='', flush=False)

# Simulating file download progress
for i in range(10):
    print(".", end='', flush=False)
    time.sleep(1)

print("\nDownload complete!")
