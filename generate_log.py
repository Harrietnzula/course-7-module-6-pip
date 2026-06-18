from datetime import datetime

def generate_log(entries):
    if not isinstance(entries, list):
        raise ValueError("Input must be a list")
    
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    with open(filename, "w") as file:
        file.write("\n".join(entries))
    
    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)