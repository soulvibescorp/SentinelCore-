import os
import time
import platform
import logging

LOG_FILE = "logs/sentinel.log"
BLOCKED_PORTS = [22, 135, 445, 3389]
LOCKED_FOLDERS = ["sensitive_docs", "vault", "admin_only"]

def init_logger():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def simulate_port_monitor():
    init_logger()
    print("[🔍] Simulating Port Monitoring...")
    for port in BLOCKED_PORTS:
        logging.info(f"Detected suspicious activity on port {port}")
        print(f"[!] Alert: Suspicious activity on port {port}")

def simulate_folder_lockdown(base_path="."):
    init_logger()
    print("[🔐] Simulating Folder Lockdown...")
    for folder in LOCKED_FOLDERS:
        path = os.path.join(base_path, folder)
        if not os.path.exists(path):
            os.makedirs(path)
        os.chmod(path, 0o000)
        logging.info(f"Access blocked to {path}")
        print(f"[X] Access blocked to {path}")

def restore_folder_access(base_path="."):
    print("[🔓] Restoring folder access...")
    for folder in LOCKED_FOLDERS:
        path = os.path.join(base_path, folder)
        if os.path.exists(path):
            os.chmod(path, 0o755)
            print(f"[+] Access restored to {path}")

def advanced_firewall_integration():
    system = platform.system()
    if system == "Linux":
        print("[Linux] 🔧 Detected. You can use `iptables` or `ufw` for real firewall.")
        print("Example: sudo ufw deny 22")
    elif system == "Windows":
        print("[Windows] 🔧 Detected. Use Windows Defender Firewall via PowerShell.")
        print("Example: New-NetFirewallRule -DisplayName 'Block RDP' -Direction Inbound -LocalPort 3389 -Action Block -Protocol TCP")
    elif system == "Darwin":
        print("[MacOS] 🔧 Detected. Configure firewall via pf or GUI settings.")
    else:
        print("[!] Unsupported platform for deep integration")

if __name__ == "__main__":
    simulate_port_monitor()
    simulate_folder_lockdown()
    advanced_firewall_integration()
