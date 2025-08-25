# main_ids.py
import subprocess
import time
import os
import sys

def run_sniffer():
    print("🐍 Starting packet sniffer (press Ctrl+C to stop)...")
    subprocess.run([sys.executable, "packet_logger.py"])

def run_analyzer():
    print("📊 Running traffic analysis...")
    subprocess.run([sys.executable, "analyze_traffic.py"])

def run_anomaly_detection():
    print("🔍 Running anomaly detection...")
    subprocess.run([sys.executable, "anomaly_detection.py"])

def run_alerts():
    print("🔔 Checking alerts...")
    subprocess.run([sys.executable, "alerts.py"])

def run_dashboard():
    print("🖥️ Launching dashboard (Streamlit)...")
    subprocess.run(["streamlit", "run", "dashboard.py"])

def menu():
    while True:
        print("\n=== Smart Network IDS ===")
        print("1. Start Packet Sniffer")
        print("2. Analyze Traffic")
        print("3. Run Anomaly Detection")
        print("4. Check Alerts")
        print("5. Launch Dashboard")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            run_sniffer()
        elif choice == "2":
            run_analyzer()
        elif choice == "3":
            run_anomaly_detection()
        elif choice == "4":
            run_alerts()
        elif choice == "5":
            run_dashboard()
        elif choice == "6":
            print("👋 Exiting Smart Network IDS.")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
