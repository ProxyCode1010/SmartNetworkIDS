import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV file path
csv_file = "../data/packets.csv"

# Load CSV
df = pd.read_csv(csv_file)

# Filter only packets with IPs
df = df[df['src_ip'].notnull() & df['dst_ip'].notnull()]

# Map protocol numbers to names
protocol_map = {6: 'TCP', 17: 'UDP', 1: 'ICMP'}
df['protocol_name'] = df['protocol'].map(protocol_map).fillna('Other')

# --- Analysis 1: Packet count per protocol ---
protocol_count = df['protocol_name'].value_counts()
print("Packet count per protocol:\n", protocol_count)

# Plot packet count per protocol
plt.figure(figsize=(6,4))
sns.barplot(x=protocol_count.index, y=protocol_count.values, palette="Set2")
plt.title("Packets per Protocol")
plt.ylabel("Count")
plt.xlabel("Protocol")
plt.tight_layout()
plt.show()

# --- Analysis 2: Top 5 source IPs ---
top_src = df['src_ip'].value_counts().head(5)
print("\nTop 5 Source IPs:\n", top_src)

plt.figure(figsize=(6,4))
sns.barplot(x=top_src.index, y=top_src.values, palette="Set1")
plt.title("Top 5 Source IPs")
plt.ylabel("Count")
plt.xlabel("Source IP")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Analysis 3: Top 5 destination IPs ---
top_dst = df['dst_ip'].value_counts().head(5)
print("\nTop 5 Destination IPs:\n", top_dst)

plt.figure(figsize=(6,4))
sns.barplot(x=top_dst.index, y=top_dst.values, palette="Set3")
plt.title("Top 5 Destination IPs")
plt.ylabel("Count")
plt.xlabel("Destination IP")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
