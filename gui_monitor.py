import psutil
import time
import csv
from datetime import datetime
from tkinter import *

# File to store the bandwidth usage data
csv_file = "bandwidth_usage.csv"

# Create the CSV file and write the header if it doesn't exist
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Bytes Sent (KB)", "Bytes Received (KB)", "Upload Speed (KB/s)", "Download Speed (KB/s)"])

# Function to get network statistics
def get_network_usage():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

# Function to update the GUI and log data
def update_monitor():
    global prev_sent, prev_recv

    # Get current data
    sent, recv = get_network_usage()

    # Calculate bandwidth usage in the last second
    sent_per_sec = (sent - prev_sent) / 1024  # KB/s
    recv_per_sec = (recv - prev_recv) / 1024  # KB/s

    # Update previous values for next calculation
    prev_sent, prev_recv = sent, recv

    # Get current timestamp for logging
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log data to CSV file
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, sent / 1024, recv / 1024, sent_per_sec, recv_per_sec])

    # Update the labels in the GUI with real-time values
    upload_label.config(text=f"Upload Speed: {sent_per_sec:.2f} KB/s")
    download_label.config(text=f"Download Speed: {recv_per_sec:.2f} KB/s")

    # Call this function again after 1000 ms (1 second)
    root.after(1000, update_monitor)

# Set up the GUI
root = Tk()
root.title("Bandwidth Monitoring Tool")

# Create labels for displaying upload and download speeds
upload_label = Label(root, font=("Helvetica", 16))
upload_label.pack(pady=10)

download_label = Label(root, font=("Helvetica", 16))
download_label.pack(pady=10)

# Get initial network usage data
prev_sent, prev_recv = get_network_usage()

# Start updating the GUI
update_monitor()

# Start the Tkinter main loop
root.mainloop()
