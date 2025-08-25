import pandas as pd
import matplotlib.pyplot as plt

# CSV file path
csv_file = "../data/packets.csv"

# Load CSV
df = pd.read_csv(csv_file)

# Ensure timestamp is datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df.dropna(subset=['timestamp'])

# --- Step 1: Resample traffic per minute ---
traffic_time = df.set_index('timestamp').resample('1T').size()

# --- Step 2: Compute mean & std deviation ---
mean = traffic_time.mean()
std = traffic_time.std()

threshold = mean + 3 * std  # "3-sigma rule" for anomalies

# --- Step 3: Detect anomalies ---
anomalies = traffic_time[traffic_time > threshold]
print("\n🚨 Anomalies detected:\n", anomalies)

# --- Step 4: Plot traffic with anomalies ---
plt.figure(figsize=(10,5))
plt.plot(traffic_time.index, traffic_time.values, label="Traffic per minute", color="blue")
plt.axhline(y=threshold, color="red", linestyle="--", label="Anomaly Threshold")
plt.scatter(anomalies.index, anomalies.values, color="red", label="Anomalies")
plt.title("Traffic Anomaly Detection (3-sigma rule)")
plt.ylabel("Packet Count")
plt.xlabel("Time")
plt.legend()
plt.tight_layout()
plt.show()
