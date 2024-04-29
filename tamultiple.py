# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:36:46 2024

@author: herma
"""

import subprocess
import concurrent.futures
import time
import signal
import os

# Define the paths to the scripts you want to run
script_paths = [
    r"C:\Users\herma\.spyder-py3\ta5min.py",
    r"C:\Users\herma\.spyder-py3\ta15min.py",
    r"C:\Users\herma\.spyder-py3\ta30min.py",
    r"C:\Users\herma\.spyder-py3\ta1hour.py",
    r"C:\Users\herma\.spyder-py3\ta4hours.py"
    # Add more script paths as needed
]

# List to store references to subprocesses
sub_processes = []

# Function to run a script
def run_script(script_path):
    subprocess.run(["python", script_path])

# Function to handle termination of subprocesses
def handle_termination(signum, frame):
    print("Terminating subprocesses...")
    for process in sub_processes:
        process.terminate()
    print("Subprocesses terminated.")
    exit(1)

# Set up signal handler for termination
signal.signal(signal.SIGTERM, handle_termination)
signal.signal(signal.SIGINT, handle_termination)

# Main loop to run the scripts every 90 minutes
while True:
    # Run scripts concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for script_path in script_paths:
            process = executor.submit(run_script, script_path)
            sub_processes.append(process)
    
    # Wait for 90 minutes before running the scripts again
    #time.sleep(3 * 60)  # 90 minutes in second