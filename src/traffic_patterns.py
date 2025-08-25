import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV file path
csv_file = "../data/packets.csv"

# Load CSV
df = pd.read_csv(csv_file)

# Ensure timestamp is datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df.dropna(subset=['timestamp'])

# --- Analysis 1: Traffic per minute ---
traffic_time = df.set_index('timestamp').resample('1T').size()
print("\nTraffic per minute:\n", traffic_time.head())

plt.figure(figsize=(10,5))
traffic_time.plot(kind='line', color='blue')
plt.title("Traffic Volume Over Time (per minute)")
plt.ylabel("Packet Count")
plt.xlabel("Time")
plt.tight_layout()
plt.show()

# --- Analysis 2: Top 5 Source Ports ---
if 'src_port' in df.columns:
    top_src_ports = df['src_port'].value_counts().head(5)
    print("\nTop 5 Source Ports:\n", top_src_ports)

    plt.figure(figsize=(6,4))
    sns.barplot(x=top_src_ports.index.astype(str), y=top_src_ports.values, palette="muted")
    plt.title("Top 5 Source Ports")
    plt.ylabel("Count")
    plt.xlabel("Source Port")
    plt.tight_layout()
    plt.show()

# --- Analysis 3: Top 5 Destination Ports ---
if 'dst_port' in df.columns:
    top_dst_ports = df['dst_port'].value_counts().head(5)
    print("\nTop 5 Destination Ports:\n", top_dst_ports)

    plt.figure(figsize=(6,4))
    sns.barplot(x=top_dst_ports.index.astype(str), y=top_dst_ports.values, palette="dark")
    plt.title("Top 5 Destination Ports")
    plt.ylabel("Count")
    plt.xlabel("Destination Port")
    plt.tight_layout()
    plt.show()

# --- Analysis 4 (extra idea): Protocol trend over time ---
if 'protocol' in df.columns:
    protocol_time = df.set_index('timestamp').groupby('protocol').resample('1T').size().unstack(fill_value=0).T
    print("\nProtocol traffic trend (per minute):\n", protocol_time.head())

    protocol_time.plot(figsize=(10,6))
    plt.title("Protocol Traffic Trend Over Time")
    plt.ylabel("Packet Count")
    plt.xlabel("Time")
    plt.legend(title="Protocol")
    plt.tight_layout()
    plt.show()
