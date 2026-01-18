import time

user_input = input("Insert time to count down (h:m:s): ")

# Split input
h, m, s = user_input.split(":")

# Convert to seconds
total_seconds = int(h) * 3600 + int(m) * 60 + int(s)

while total_seconds >= 0:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
    total_seconds -= 1

print("Time's up!")