import datetime
import logging

# Setup logging for alerts
logging.basicConfig(
    filename="alerts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_alert(message: str):
    """
    Logs an alert message to alerts.log and prints it.
    """
    alert_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{alert_time}] 🚨 ALERT: {message}"
    
    # Write to log file
    logging.warning(full_message)
    
    # Print on console
    print(full_message)


def alert_anomalies(anomalies):
    """
    Trigger alerts if anomalies are detected.
    """
    if anomalies.empty:
        print("✅ No anomalies detected.")
    else:
        log_alert(f"Detected {len(anomalies)} anomalies in network traffic!")


def alert_suspicious_ip(ip: str, count: int):
    """
    Raise an alert if a suspicious IP exceeds a threshold.
    """
    threshold = 50  # Example threshold, can be tuned
    if count > threshold:
        log_alert(f"Suspicious IP {ip} seen {count} times (above threshold {threshold})")


# --------------------------
# Self-test (runs only if executed directly)
# --------------------------
if __name__ == "__main__":
    print("🔔 Running alerts self-test...")
    
    # Test anomaly alert
    import pandas as pd
    fake_anomalies = pd.DataFrame({"ip": ["192.168.1.10", "10.0.0.5"]})
    alert_anomalies(fake_anomalies)

    # Test suspicious IP alert
    alert_suspicious_ip("192.168.1.200", 120)
    alert_suspicious_ip("8.8.8.8", 30)  # below threshold (won’t trigger)
