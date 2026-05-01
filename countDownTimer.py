import time

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds >= 0:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        print(f"{h:02}:{m:02}:{s:02}")
        time.sleep(1)
        total_seconds -= 1
    print("Time's up!")

def get_time_input():
    while True:
        user_input = input("Enter time in h:m:s format: ").strip()
        
        # Blank input check
        if not user_input:
            print("Error: Input cannot be blank. Try again.")
            continue
        
        try:
            h, m, s = map(int, user_input.split(":"))
        except ValueError:
            print("Error: Invalid format. Please enter numbers in h:m:s format (e.g., 01:30:45).")
            continue
        
        # Negative values check
        if h < 0 or m < 0 or s < 0:
            print("Error: Time values cannot be negative. Try again.")
            continue
        
        return h, m, s

# Main program
h, m, s = get_time_input()
countdown_timer(h, m, s)