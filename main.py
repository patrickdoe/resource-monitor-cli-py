from menu import Menu
from alarm import Alarm

# Open and store the content within greetings.txt to a variable before printing it.
try:
    with open('greeting.txt', 'r', encoding="utf8") as f:
        greetings = f.read()
except FileNotFoundError:
    print("Error: The file 'greeting.txt' was not found.")
except OSError:
    print("Error: An OS error occurred while reading the file.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")
except Exception as e:
    print(f"Something went wrong! (Unexpected error: {e})")

# Initialize Alarm and Menu from the other .py files.
alarm_thresholds = Alarm()
menu = Menu(greetings, alarm_thresholds)

while True:
    menu.display_menu()
    user_input = input('|   User choice: ')
    menu.menu_selections(user_input)
