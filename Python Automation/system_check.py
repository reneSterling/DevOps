#This program checks the system specs.

import psutil

def sys():
    print("Automated system health report")
    print("------------------------------")
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"Memory: {psutil.virtual_memory().percent}%")
    print(f"Disk: {psutil.disk_usage('/').percent}%")


if __name__ == "__main__":
    sys()

