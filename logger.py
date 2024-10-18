import csv
from datetime import datetime

# Initialize CSV file
def initialize_log(file_name="bandwidth_usage.csv"):
    """
    Initializes the CSV file and writes the header if the file doesn't exist.
    """
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Bytes Sent (KB)", "Bytes Received (KB)", "Upload Speed (KB/s)", "Download Speed (KB/s)"])

# Log bandwidth data to CSV
def log_to_csv(sent, recv, sent_per_sec, recv_per_sec, file_name="bandwidth_usage.csv"):
    """
    Logs bandwidth data (upload and download) to a CSV file with a timestamp.
    
    Parameters:
    - sent: Total bytes sent.
    - recv: Total bytes received.
    - sent_per_sec: Upload speed (bytes per second).
    - recv_per_sec: Download speed (bytes per second).
    - file_name: The name of the CSV file.
    """
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open the CSV file and append the data
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, sent / 1024, recv / 1024, sent_per_sec / 1024, recv_per_sec / 1024])

    # Optional: Print a confirmation for debugging
    print(f"Logged at {timestamp}: Upload: {sent_per_sec / 1024:.2f} KB/s, Download: {recv_per_sec / 1024:.2f} KB/s")
