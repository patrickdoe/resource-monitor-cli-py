import os
import time

#Open and store the content within greetings.txt to a variable before printing it.
f = open('greeting.txt', 'r', encoding="utf8")
greetings = f.read()
f.close()

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(greetings)
    
def option1_monitor():
    print('|\n|   * MONITORING ACTIVATED! *')
    input('|   Press enter button to continue...')

def option2_show_monitor():
    print('|\n|   LIVE MONITOR VALUES')
    print('|   -------------------')
    input('|   Press enter button to continue...')

def option3_create_alarms():
    print('|\n|   CREATE NEW ALARMS')
    print('|   -----------------')
    input('|   Press enter button to continue...')

def option4_show_alarms():
    print('|\n|   SHOW ALARMS')
    print('|   -----------')
    input('|   Press enter button to continue...')
    
def option5_activate_alarms():
    print('|\n|   MONITOR ALARM(S)')
    print('|   ----------------')
    input('|   Press enter button to continue...')
    
def option6_remove_alarms():
    print('|\n|   REMOVE ALARM(S)')
    print('|   ---------------')
    input('|   Press enter button to continue...')
    
def quit_app():
    goodbye = '!_________________________________________________________________________________________________ CLOSING APP!'
    for char in goodbye:
        print(char, end='', flush=True)
        time.sleep(0.02)
    exit()
    
def input_error():
    print('|\n|   Input error, try again...')
    input('|   Press enter button to continue...')

while True:
    display_menu()
    userInput = input('|   User choice: ')
    
    if userInput == "1":
        option1_monitor()
    elif userInput == "2":
        option2_show_monitor()
    elif userInput =="3":
        option3_create_alarms()
    elif userInput == "4":
        option4_show_alarms()
    elif userInput == "5":
        option5_activate_alarms()
    elif userInput == "6":
        option6_remove_alarms()
    elif userInput == 'x' or userInput == 'X':
        quit_app()
    else:
        input_error()