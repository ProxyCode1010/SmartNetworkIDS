import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# CSV file
csv_file = "../data/packets.csv"

st.set_page_config(page_title="SmartNetworkIDS Dashboard", layout="wide")
st.title("📊 SmartNetworkIDS – Network Traffic Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv(csv_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = load_data()

# Map protocol numbers to names
protocol_map = {6: 'TCP', 17: 'UDP', 1: 'ICMP'}
df['protocol_name'] = df['protocol'].map(protocol_map).fillna('Other')

# --- Tabs for visualization ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📡 Protocols", 
    "🌍 Source IPs", 
    "🎯 Destination IPs", 
    "🚨 Anomalies"
])

with tab1:
    st.subheader("Packets per Protocol")
    proto_count = df['protocol_name'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=proto_count.index, y=proto_count.values, ax=ax, palette="Set2")
    ax.set_ylabel("Packet Count")
    ax.set_xlabel("Protocol")
    st.pyplot(fig)

with tab2:
    st.subheader("Top 5 Source IPs")
    top_src = df['src_ip'].value_counts().head(5)
    fig, ax = plt.subplots()
    sns.barplot(x=top_src.index, y=top_src.values, ax=ax, palette="Set1")
    ax.set_ylabel("Packet Count")
    ax.set_xlabel("Source IP")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab3:
    st.subheader("Top 5 Destination IPs")
    top_dst = df['dst_ip'].value_counts().head(5)
    fig, ax = plt.subplots()
    sns.barplot(x=top_dst.index, y=top_dst.values, ax=ax, palette="Set3")
    ax.set_ylabel("Packet Count")
    ax.set_xlabel("Destination IP")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab4:
    st.subheader("Traffic Over Time with Anomalies")
    traffic_time = df.set_index('timestamp').resample('1min').size()
    threshold = traffic_time.mean() + 3 * traffic_time.std()
    anomalies = traffic_time[traffic_time > threshold]

    fig, ax = plt.subplots()
    traffic_time.plot(ax=ax, color='blue', label='Traffic per Minute')
    ax.axhline(y=threshold, color='red', linestyle='--', label='Threshold')

    # Mark anomalies in red
    ax.scatter(
        anomalies.index.to_pydatetime(),
        anomalies.values,
        color='red', marker='o', s=80, label='Anomalies'
    )

    ax.set_ylabel("Packets per Minute")
    ax.set_xlabel("Time")
    ax.legend()
    st.pyplot(fig)
