import psutil
import os
import time

class SystemMonitor:
    def __init__(self):
        self.monitoring_activated = False

    def activate_monitoring(self):
        self.monitoring_activated = True
        print('|\n|   * MONITORING ACTIVATED! *')
        input('|\n|)>> Press enter button to continue...')

    def show_monitor(self):
        if not self.monitoring_activated:
            print('|\n|   You need to activate monitoring first!')
            input('|\n|)>> Press enter button to return to the menu...')
            return
        
        try:
            while True:
                self.system_usage()
                time.sleep(1)
        except KeyboardInterrupt:
            print(')>> Sending you back to the main menu...')
            time.sleep(2)

    def system_usage(self):
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        battery = psutil.sensors_battery()
        battery_level = int(battery.percent) if battery else None

        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(' LIVE MONITOR VALUES')
        print(' -------------------')
        print(f' CPU Usage ...: {cpu_usage}%')
        print(f' RAM Usage ...: {ram_usage}%')
        print(f' Disk Usage ..: {disk_usage}%')
        if battery:
            charging_status = "Currently charging" if battery.power_plugged else "Not charging"
            print(f' Battery Level: {battery_level}% ({charging_status})')
        print('\n\n USER CONFIGURATION')
        print(' ------------------')
        # Display some extra information about the users setup.
        print(f' {os.uname().nodename} @ {os.uname().sysname} {os.uname().release} ({os.uname().machine})')
        print('\n>>> Press CTRL+C to return to main menu.')

    def usage_report(self):
        # Define how to display the values through psutil.
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        battery = psutil.sensors_battery()
        battery_level = int(battery.percent) if battery else None
        
        return {
            "cpu": cpu_usage,
            "ram": ram_usage,
            "disk": disk_usage,
            "battery": battery_level
        }
