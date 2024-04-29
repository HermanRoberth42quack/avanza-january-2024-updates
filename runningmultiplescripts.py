# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:39:53 2024

@author: herma
"""
import subprocess
import concurrent.futures

# Define the paths to the scripts you want to run
script_paths = [r"C:\Users\herma\.spyder-py3\ta5min.py",
    r"C:\Users\herma\.spyder-py3\ta15min.py",r"C:\Users\herma\.spyder-py3\ta30min.py",
    r"C:\Users\herma\.spyder-py3\ta1hour.py",r"C:\Users\herma\.spyder-py3\ta4hours.py"
    # Add more script paths as needed
]

# Function to run a script
def run_script(script_path):
    subprocess.run(["python", script_path])

# Run scripts concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_script, script_paths)

#r"C:\Users\herma\.spyder-py3\ta5min.py",