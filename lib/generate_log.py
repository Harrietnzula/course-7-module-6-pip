#!/usr/bin/env python3
from datetime import datetime

def generate_log(entries):
    if not isinstance(entries, list):
        raise ValueError("Input must be a list")
    
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    with open(filename, "w") as file:
        file.write("\n".join(entries))
    
    print(f"Log file created: {filename}")
    return filename