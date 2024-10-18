import psutil
import time
import logger

# Initialize the log file
logger.initialize_log()

# Function to get network statistics
def get_network_usage():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

# Store previous sent/recv values to calculate bandwidth usage
prev_sent, prev_recv = get_network_usage()

# Monitor bandwidth usage
try:
    while True:
        time.sleep(1)  # Capture data every second
        sent, recv = get_network_usage()

        # Calculate bandwidth usage
        sent_per_sec = (sent - prev_sent)  # Bytes per second
        recv_per_sec = (recv - prev_recv)  # Bytes per second

        # Update previous values
        prev_sent, prev_recv = sent, recv

        # Log bandwidth data to CSV
        logger.log_to_csv(sent, recv, sent_per_sec, recv_per_sec)

except KeyboardInterrupt:
    print("Monitoring stopped.")
