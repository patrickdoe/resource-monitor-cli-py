import psutil
import time
import os

def system_usage():
    
    while True:
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        battery_level = int(psutil.sensors_battery().percent)
        device_plugged_in = psutil.sensors_battery().power_plugged
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(' LIVE MONITOR VALUES')
        print(' -------------------')
        print(f' CPU Usage ...: {cpu_usage}%')
        print(f' RAM Usage ...: {ram_usage}%')
        print(f' Disk Usage ..: {disk_usage}%')
        
        if device_plugged_in == False:
            print(f' Battery Level: {battery_level}% (Not charging)')
        else:
            print(f' Battery Level: {battery_level}% (Currently charging)')
        
        print('\n\n USER CONFIGURATION')
        print(' ------------------')
        print(f' {os.uname().nodename} @ {os.uname().sysname} {os.uname().release} ({os.uname().machine})\n')
        
        print('\n>>> Press CTRL+C to return to main menu.')
        time.sleep(1)
        
def usage_report():
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    battery = psutil.sensors_battery()
    battery_level = int(battery.percent) if battery else None
    device_plugged_in = battery.power_plugged if battery else False
    
    return {
        "cpu": cpu_usage,
        "ram": ram_usage,
        "disk": disk_usage,
        "battery": battery_level
    }