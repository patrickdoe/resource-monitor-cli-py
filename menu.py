import os
import time
from livemonitor import SystemMonitor
from alarm import Alarm

class Menu:
    def __init__(self, greetings, alarm_thresholds):
        self.greetings = greetings
        self.alarm_thresholds = alarm_thresholds
        self.monitor = SystemMonitor()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        self.clear_screen()
        print(self.greetings)

    def menu_selections(self, user_input):
        if user_input == "1":
            self.monitor.activate_monitoring()
        elif user_input == "2":
            self.monitor.show_monitor()
        elif user_input == "3":
            self.set_alarm()
        elif user_input == "4":
            self.show_alarms()
        elif user_input == "5":
            self.activate_alarms()
        elif user_input == "6":
            self.remove_alarms()
        elif user_input.lower() == 'x': # Make user input case insensitive and accept 'x' and 'X'.
            self.quit_app()
        else:
            self.input_error()

    def set_alarm(self):
        while True:
            self.clear_screen()
            print('\n SET ALARM THRESHOLDS')
            print(' --------------------')
            # List thresholds with a for-loop, if a value is "None" display it as "Not Set".
            for idx, (typ, thr) in enumerate(self.alarm_thresholds.show_alarms()):
                print(f' {idx + 1}. {typ.upper()} Threshold: {thr if thr is not None else "Not Set"}')

            print(' 5. Go back to the main menu')
            user_choice = input('\n User choice: ')

            # Associate user input (numbers) to the alarm type to set / change.
            if user_choice.isdigit() and 1 <= int(user_choice) <= 4:
                alarm_type = self.alarm_thresholds.show_alarms()[int(user_choice) - 1][0]
                threshold = int(input(f'Set {alarm_type.upper()} threshold (%): '))
                self.alarm_thresholds.set_threshold(alarm_type, threshold)
            elif user_choice == '5':
                break
            else:
                print('\n Input error, try again...')
                time.sleep(1)

    def show_alarms(self):
        self.clear_screen()
        print('\n USER SET THRESHOLDS')
        print(' -------------------')
        # Show alarms using a for-loop, change "None" value to "Not Set". Also added some layout formatting.
        for alarm in self.alarm_thresholds.show_alarms():
            print(f' {alarm[0].upper():<10} = {alarm[1] if alarm[1] is not None else "Not Set":<10}')
        input('\n Press enter to go back...')

    def activate_alarms(self):
        print('|\n|   MONITOR ALARM(S)')
        print('|   ----------------')
        
        try:
            while True:
                current_usage = self.monitor.usage_report()
                self.clear_screen()
                print(' CURRENT SYSTEM USAGE')
                print(' --------------------')
                for k, v in current_usage.items():
                    print(f' {k.capitalize()} Usage: {v}%')

                for alarm in self.alarm_thresholds.show_alarms():
                    alarm_type, threshold = alarm
                    
                    if threshold is not None:
                        # Trigger battery threshold when BELOW threshold.
                        if alarm_type == "battery":
                            if current_usage[alarm_type] < threshold:
                                print(f'\n *** ALERT: {alarm_type.upper()} usage is below the threshold!'
                                    f' Current: {current_usage[alarm_type]}%, Threshold: {threshold}')
                        # Trigger the rest of the alarms ABOVE the user set threshold.
                        else:
                            if current_usage[alarm_type] > threshold:
                                print(f'\n *** ALERT: {alarm_type.upper()} usage has exceeded the threshold!'
                                    f' Current: {current_usage[alarm_type]}%, Threshold: {threshold}')

                print('\n Press Ctrl+C to stop monitoring...')
                time.sleep(1)

        except KeyboardInterrupt:
            print('\n Monitoring stopped.')
            time.sleep(0.5)
            input('\n Press enter to return to the menu...')

    def remove_alarms(self):
        while True:
            self.clear_screen()
            print('\n REMOVE ACTIVE ALARM(S)')
            print(' ----------------------')
            # Create a new filtered list only containing thresholds, exclude "None".
            set_thresholds = [(idx, alarm) for idx, alarm in enumerate(self.alarm_thresholds.show_alarms()) if alarm[1] is not None]
            
            # Return to main menu if no thresholds can be found.
            if not set_thresholds:
                print(' No threshold(s) found. \n Going back to main menu...')
                time.sleep(2)
                break
            
            # List the filtered list with thresholds.
            for display_idx, (internal_idx, (alarm_type, threshold)) in enumerate(set_thresholds, start=1):
                print(f' {display_idx}. Remove {alarm_type.upper():>8} Threshold ({threshold})')


            print('\n 0. Remove ALL Thresholds')
            print(' 9. Go back to the main menu')

            user_choice = input('\n User choice: ')
            
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(set_thresholds):
                    alarm_to_remove = set_thresholds[user_choice - 1]
                    alarm_type = alarm_to_remove[1][0]
                    self.alarm_thresholds.remove_alarm(alarm_type)
                    print(f' {alarm_type.upper()} Threshold removed.')
                elif user_choice == 0:
                    self.alarm_thresholds.thresholds = [(alarm[0], None) for alarm in self.alarm_thresholds.thresholds]
                    print(' All alarms have been removed.')
                elif user_choice == 9:
                    break
                else:
                    print(' Input error, try again...')
            else:
                print(' Input error, please enter a valid number.')

            time.sleep(2)

    def quit_app(self):
        print('|>> Closing app in: ')
        goodbye = '|   3_____ 2_____ 1_____\n\n'
        # My attempt to animate the "good bye" message a little.
        for char in goodbye:
            print(char, end='', flush=True)
            time.sleep(0.15)
        exit()

    def input_error(self):
        print('|\n|   Input error, try again...')
        input(')>> Press enter button to continue...')
