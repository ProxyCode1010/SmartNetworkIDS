# 🔐 SmartNetworkIDS – Intelligent Intrusion Detection System  

A Python-based **Network Intrusion Detection System (IDS)** with packet sniffing, traffic logging, anomaly detection, visualization dashboard, and real-time alerts.  

The project demonstrates **network security fundamentals** and **advanced monitoring concepts**, combining **packet analysis, anomaly detection, logging, and visualization** into a modular system.  

---

## 📖 Project Explanation  

SmartNetworkIDS is designed to **monitor live network traffic**, detect **abnormal patterns**, and alert users of suspicious behavior. It consists of multiple Python scripts working together like components in a real IDS:

- **`sniffer.py`** → Captures raw packets in real time using **Scapy**. (The "ears" of the IDS – it listens to all network conversations).  
- **`packet_logger.py`** → Extracts packet details (timestamp, source IP, destination IP, protocol) and logs them into **`packets.csv`** (like a “black box” for the network).  
- **`analyze_traffic.py`** → Analyzes logs for **protocol usage, top source IPs, top destination IPs** (helps find dominant protocols or hosts).  
- **`traffic_patterns.py`** → Groups traffic into **time windows (per minute)** for spotting spikes or unusual flows.  
- **`anomaly_detection.py`** → Detects abnormal traffic using **threshold-based detection** (e.g., if packets > 100 in a minute → anomaly flagged).  
- **`alerts.py`** → Generates alerts if anomalies are detected. Alerts are written to **alerts.log** and printed in the terminal. Example:

[2025-08-23 08:07:38] 🚨 ALERT: Detected 2 anomalies in network traffic! [2025-08-23 08:07:38] 🚨 ALERT: Suspicious IP 192.168.1.200 seen 120 times (above threshold 50)

- **`dashboard.py`** → Streamlit-powered visualization. Provides interactive graphs for protocol distribution, top talkers, and anomalies.  

---

## 🚀 Features  

- Live packet sniffing with **Scapy**  
- Traffic logging into **CSV files**  
- Protocol & IP analysis (TCP, UDP, ICMP, Others)  
- Time-based traffic aggregation  
- **Threshold-based anomaly detection**  
- **Real-time alerts** written to `alerts.log`  
- Interactive **Streamlit dashboard** with filters and graphs  

---

## 🛠 Installation & Quick Start  

### Requirements  
- Python 3.8+  
- Install dependencies:  
```bash
pip install scapy pandas matplotlib seaborn streamlit

Run the System Step by Step

1. Run Packet Sniffer

python sniffer.py


2. Log Packets

python packet_logger.py


3. Analyze Traffic

python analyze_traffic.py


4. Detect Anomalies

python anomaly_detection.py


5. Generate Alerts

python alerts.py


6. Launch Dashboard

streamlit run dashboard.py




---

📊 Dashboard Features

Protocol distribution pie chart

Top source & destination IP bar charts

Anomaly timeline line chart

Filters by protocol, source IP, destination IP

Auto-refresh from packets.csv



---

✅ Future Improvements

ML-based anomaly detection (instead of fixed thresholds)

Threat intelligence integration

Automated response (e.g., block malicious IPs)



---

📌 Summary

SmartNetworkIDS is a mini but realistic Intrusion Detection System.
It shows how packets can be captured, logged, analyzed, visualized, and monitored for anomalies in a modular and scalable way.
It demonstrates networking, security, and software engineering concepts in one project.
