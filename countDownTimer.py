import time

# Convert to seconds
def countdown(hours, minutes, seconds):
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    while total_seconds >= 0:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")

def main():
    user_input = input("Insert time to count down (h:m:s): ")

    try:
        hours, minutes, seconds = user_input.split(":")
        countdown(int(hours), int(minutes), int(seconds))
    except ValueError:
        print("Invalid input!(h:m:s)")

if __name__ == "__main__":
    main()