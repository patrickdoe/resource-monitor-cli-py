import os
import time
from livemonitor import *

#Open and store the content within greetings.txt to a variable before printing it.
try:
    f = open('greeting.txt', 'r', encoding="utf8")
    greetings = f.read()
    f.close()
except FileNotFoundError:
    print("Error: The file 'greeting.txt' was not found.")
except OSError:
    print("Error: An OS error occurred while reading the file.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")
except Exception as e:
    print(f"Something went wrong! (Unexpected error: {e})")

alarm_thresholds = [
    ("cpu", None),
    ("ram", 10),
    ("disk", 40),
    ("battery", 20)
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print(greetings)
    
def option1_monitor():
    print('|\n|   * MONITORING ACTIVATED! *')
    input(')>> Press enter button to continue...')

def option2_show_monitor():
    try:
        while True:
            system_usage()
            time.sleep(1)
    except KeyboardInterrupt:
        print(')>> Sending you back to the main menu...')
        time.sleep(2)

def option3_create_alarms():
    while True:
        clear_screen()
        
        print('\n SET ALARM THRESHOLDS')
        print(' --------------------')
        print(f' 1. CPU Threshold: {alarm_thresholds[0][1]}%')
        print(f' 2. RAM Threshold: {alarm_thresholds[1][1]}%')
        print(f' 3. Disk Threshold: {alarm_thresholds[2][1]}%')
        print(f' 4. Battery Threshold: {alarm_thresholds[3][1]}%')
        print(' 5. Go back to the main menu')
        user_choice = input('\n User choice: ')

        if user_choice == '1':
            cpu_threshold = input('\n Set CPU threshold (%): ')
            alarm_thresholds[0] = ("cpu", int(cpu_threshold))
        elif user_choice == '2':
            ram_threshold = input('\n Set RAM threshold (%): ')
            alarm_thresholds[1] = ("ram", int(ram_threshold))
        elif user_choice == '3':
            disk_threshold = input('\n Set Disk threshold (%): ')
            alarm_thresholds[2] = ("disk", int(disk_threshold))
        elif user_choice == '4':
            battery_threshold = input('\n Set Battery threshold (%): ')
            alarm_thresholds[3] = ("battery", int(battery_threshold))
        elif user_choice == '5':
            break
        else:
            print(' Input error, try again...')
            time.sleep(1)

def option4_show_alarms():
    clear_screen()
    print('\n USER SET THRESHOLDS')
    print(' -------------------')
    # Sort the thresholds based on type
    sorted_alarms = sorted(alarm_thresholds, key=lambda x: x[0].upper())
    for alarm in sorted_alarms:
        alarm_type = alarm[0].upper()
        threshold = alarm[1] if alarm[1] is not None else 'Not Set'
        print(f' {alarm_type:<10} = {threshold:<10}')
    input('\n Press enter to go back...')
    
def option5_activate_alarms():
    print('|\n|   MONITOR ALARM(S)')
    print('|   ----------------')
    
    try:
        while True:
            clear_screen()
            # Collect current usage from livemonitor function and print the results
            current_usage = usage_report()
            print(' CURRENT SYSTEM USAGE')
            print(' --------------------')
            print(f' CPU Usage: {current_usage["cpu"]}%')
            print(f' RAM Usage: {current_usage["ram"]}%')
            print(f' Disk Usage: {current_usage["disk"]}%')
            print(f' Battery Level: {current_usage["battery"]}%\n')

            # Check against user set thresholds
            for alarm in alarm_thresholds:
                alarm_type, threshold = alarm
                if threshold is not None and current_usage[alarm_type] > threshold:
                    print(f' *** ALERT: {alarm_type.upper()} usage has exceeded the threshold! 'f'Current: {current_usage[alarm_type]}%, Threshold: {threshold}%')

            print('\n Press Ctrl+C to stop monitoring...')
            time.sleep(1)  # Adjust this for monitoring frequency

    except KeyboardInterrupt:
            print('\n Monitoring stopped.')
            time.sleep(0.5)
            input(' Press enter to return to the menu...')
    
def option6_remove_alarms():
    while True:
        clear_screen()
        print('\n REMOVE ACTIVE ALARM(S)')
        print(' ----------------------')
        set_thresholds = [(idx, alarm) for idx, alarm in enumerate(alarm_thresholds) if alarm[1] is not None]
        
        if not set_thresholds:
            print(' No threshold(s) found. \n Going back to main menu...')
            time.sleep(2)
            break
        
        for idx, (alarm_type, threshold) in set_thresholds:
            print(f' {idx}. Remove {alarm_type.upper():>8} Threshold ({threshold})')

        print('\n 0. Remove ALL Thresholds')
        print(' 9. Go back to the main menu')

        user_choice = input('\n User choice: ')
        
        if user_choice.isdigit():
            user_choice = int(user_choice)

            if 1 <= user_choice <= len(set_thresholds):
                alarm_to_remove = set_thresholds[user_choice - 1]
                alarm_type = alarm_to_remove[1][0]
                alarm_thresholds[alarm_to_remove[0]] = (alarm_type, None)
                print(f' {alarm_type.upper()} Threshold removed.')
            elif user_choice == 0:
                alarm_thresholds[:] = [(alarm[0], None) for alarm in alarm_thresholds]  # Reset all thresholds to None
                print(' All alarms has been removed.')
            elif user_choice == 9:
                break
            else:
                print(' Input error, try again...')
        else:
            print(' Input error, please enter a valid number.')
        
            time.sleep(2)
    
def quit_app():
    print('|>> Closing app in: ')
    goodbye = '|   3_____ 2_____ 1_____\n\n'
    for char in goodbye:
        print(char, end='', flush=True)
        time.sleep(0.15)
    exit()
    
def input_error():
    print('|\n|   Input error, try again...')
    input(')>> Press enter button to continue...')
    
def menu_selections():
    if user_input == "1":
        option1_monitor()
    elif user_input == "2":
        option2_show_monitor()
    elif user_input =="3":
        option3_create_alarms()
    elif user_input == "4":
        option4_show_alarms()
    elif user_input == "5":
        option5_activate_alarms()
    elif user_input == "6":
        option6_remove_alarms()
    elif user_input == 'x' or user_input == 'X':
        quit_app()
    else:
        input_error()

while True:
    display_menu()
    user_input = input('|   User choice: ')
    menu_selections()
