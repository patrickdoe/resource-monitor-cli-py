import json
import time
import os
from datetime import datetime

class Alarm:
    # Temporary threshold values for alarms, mainly for testing purposes but can be changed while running the app.
    def __init__(self, thresholds_file='thresholds.json'):
        self.thresholds = [
            ("cpu", None),
            ("ram", 10),
            ("disk", 40),
            ("battery", 20)
        ]
        self.thresholds_file = thresholds_file
        self.load_thresholds() # Load thresholds from file.

    def set_threshold(self, alarm_type, threshold):
        # Set new threshold through a next function that cycles through the threshold list for a match of alarm_type.
        index = next((i for i, (typ, _) in enumerate(self.thresholds) if typ == alarm_type), None)
        if index is not None:
            self.thresholds[index] = (alarm_type, threshold)
            self.save_thresholds() # Save thresholds.

    def show_alarms(self):
        # Sort the list of alarms based on type (not case sensitive).
        return sorted(self.thresholds, key=lambda x: x[0].upper())

    def remove_alarm(self, alarm_type):
        # Chosen alarm to remove will be set to none.
        index = next((i for i, (typ, _) in enumerate(self.thresholds) if typ == alarm_type), None)
        if index is not None:
            self.thresholds[index] = (alarm_type, None)
            self.save_thresholds() # Save thresholds after removing alarms.
            
    def remove_all_alarms(self):
        self.thresholds = [(alarm[0], None) for alarm in self.thresholds]
        self.save_thresholds()

    def save_thresholds(self):
        with open(self.thresholds_file, 'w') as file:
            json.dump(self.thresholds, file, indent=4)
            
    def load_thresholds(self):
        try:
            with open(self.thresholds_file, 'r') as file:
                self.thresholds = json.load(file)
                
            os.system('cls' if os.name == 'nt' else 'clear')
            print('JSON file found! Loading previously configured alarms...')
            time.sleep(3)
        except(FileNotFoundError, json.JSONDecodeError):
            pass # Uses default pre-defined thresholds if file doesn't exist.