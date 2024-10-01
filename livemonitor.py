import psutil
import time
import os

def system_usage():

    while True:
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(' LIVE MONITOR VALUES')
        print(' -------------------')
        print(f' CPU Usage : {cpu_usage}%')
        print(f' RAM Usage : {ram_usage}%')
        print(f' Disk Usage: {disk_usage}%')
        
        time.sleep(1)