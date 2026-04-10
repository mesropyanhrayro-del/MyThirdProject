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

def get_time_input():
    user_input = input("Enter time in h:m:s format: ").strip()
    
    # Check for blank input
    if not user_input:
        print("Error: Input cannot be blank.")
        return None
    
    try:
        h, m, s = map(int, user_input.split(":"))
    except ValueError:
        print("Error: Input must contain only numbers separated by colons (e.g., 1:30:45).")
        return None
    
    # Check for negative values
    if h < 0 or m < 0 or s < 0:
        print("Error: Time values cannot be negative.")
        return None
    
    return h, m, s

# Main program
time_values = get_time_input()
if time_values:
    h, m, s = time_values
    countdown_timer(h, m, s)



import time

def countdown_timer(total_seconds):
    while total_seconds > 0:
        hrs, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        print(f"{hrs:02}:{mins:02}:{secs:02}")
        time.sleep(1)
        total_seconds -= 1
    print("00:00:00")  # final display at zero

def get_time_input():
    user_input = input("Enter time in h:m:s format: ").strip()
    
    if not user_input:
        print("Error: Input cannot be blank.")
        return None
    
    try:
        h, m, s = map(int, user_input.split(":"))
    except ValueError:
        print("Error: Input must contain only numbers separated by colons (e.g., 1:30:45).")
        return None
    
    if h < 0 or m < 0 or s < 0:
        print("Error: Time values cannot be negative.")
        return None
    
    if m > 59 or s > 59:
        print("Error: Minutes and seconds must be between 0 and 59.")
        return None
    
    return h, m, s

# Main program
time_values = get_time_input()
if time_values:
    h, m, s = time_values
    total_seconds = h * 3600 + m * 60 + s
    countdown_timer(total_seconds)
