
def check_battery(percent):
    if percent >= 90 and percent <= 100:
        print("Your battery is full, you can go out and have fun.")
    elif percent >= 50:
        print("Your battery is good, you can go out and have fun.")
    elif percent >= 0:
        print("Your battery is low, you should charge it before going out.")
    else:
        print("Invalid percentage!")

current_battery = int(input("Enter the battery percentage: "))
check_battery(current_battery)