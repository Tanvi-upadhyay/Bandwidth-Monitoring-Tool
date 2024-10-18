import matplotlib.pyplot as plt
import pandas as pd

# Function to load data from CSV file and plot it
def plot_bandwidth_usage(file_name="bandwidth_usage.csv"):
    """
    Reads the bandwidth usage data from a CSV file and plots the upload and download speeds over time.
    
    Parameters:
    - file_name: The name of the CSV file to read data from.
    """
    # Load the CSV data into a Pandas DataFrame
    data = pd.read_csv(file_name)
    
    # Convert the 'Timestamp' column to datetime for better plotting
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    
    # Plot the upload and download speeds
    plt.figure(figsize=(10, 6))
    
    # Plot upload speed
    plt.plot(data['Timestamp'], data['Upload Speed (KB/s)'], label='Upload Speed (KB/s)', color='blue')
    
    # Plot download speed
    plt.plot(data['Timestamp'], data['Download Speed (KB/s)'], label='Download Speed (KB/s)', color='green')

    # Customize the plot
    plt.title("Bandwidth Usage Over Time")
    plt.xlabel("Time")
    plt.ylabel("Speed (KB/s)")
    plt.xticks(rotation=45)
    plt.legend(loc="upper left")
    plt.grid(True)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Run the plot function
if __name__ == "__main__":
    plot_bandwidth_usage()
