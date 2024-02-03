import platform
import socket
import psutil
import speedtest
import requests
from cpuinfo import get_cpu_info
import tkinter as tk
import uuid
import os

def get_wifi_mac_address():
    try:
        if platform.system().lower() == 'windows':
            for line in os.popen('ipconfig /all'):
                if 'Wireless LAN Adapter' in line:
                    mac_address = line.split(' ')[-1].strip()
                    return mac_address
        elif platform.system().lower() == 'linux':
            for line in open('/sys/class/net/wlan0/address'):
                mac_address = line.strip()
                return mac_address
        elif platform.system().lower() == 'darwin':
            mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
            return ":".join([mac_address[e:e+2] for e in range(0, 11, 2)])
    except Exception as e:
        return str(e)

def get_screen_resolution():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()  
    return screen_width, screen_height

# CPU Details
print("CPU Model: ", get_cpu_info()['brand_raw'])
print("CPU Cores: ", psutil.cpu_count(logical=False))
print("CPU Threads: ", psutil.cpu_count(logical=True))

# RAM Details
print("RAM Size: ", round(psutil.virtual_memory().total / (1024.0 **3)), "GB")

# System Details
print("Windows Version: ", platform.platform())

# Network Details
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        public_ip = data['ip']
        return public_ip
    except Exception as e:
        return f"Error: {e}"
    
def get_installed_software():
    software_list = []
    for item in psutil.process_iter(['pid', 'name']):
        software_list.append(item.info['name'])
    return software_list

if __name__ == "__main__":
    print("Installed Software:", get_installed_software())
import speedtest

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1024 / 1024 
    upload_speed = st.upload() / 1024 / 1024  
    return download_speed, upload_speed

if __name__ == "__main__":
    try:
        download_speed, upload_speed = get_internet_speed()
        print(f"Internet Speed - Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"Error: {e}")
        
        public_ip = get_public_ip()
    print(f"Public IP Address: {public_ip}")
    
    try:
        width, height = get_screen_resolution()
        print(f"Screen Resolution: {width}x{height}")
    except Exception as e:
        print(f"Error: {e}")
        
    wifi_mac_address = get_wifi_mac_address()
    print(f"Wifi MAC Address: {wifi_mac_address}")