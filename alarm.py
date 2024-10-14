class Alarm:
    # Temporary threshold values for alarms, mainly for testing purposes but can be changed while running the app.
    def __init__(self):
        self.thresholds = [
            ("cpu", None),
            ("ram", 10),
            ("disk", 40),
            ("battery", 20)
        ]

    def set_threshold(self, alarm_type, threshold):
        # Set new threshold through a next function that cycles through the threshold list for a match of alarm_type.
        index = next((i for i, (typ, _) in enumerate(self.thresholds) if typ == alarm_type), None)
        if index is not None:
            self.thresholds[index] = (alarm_type, threshold)

    def show_alarms(self):
        # Sort the list of alarms based on type (not case sensitive).
        return sorted(self.thresholds, key=lambda x: x[0].upper())

    def remove_alarm(self, alarm_type):
        # Chosen alarm to remove will be set to none.
        index = next((i for i, (typ, _) in enumerate(self.thresholds) if typ == alarm_type), None)
        if index is not None:
            self.thresholds[index] = (alarm_type, None)
