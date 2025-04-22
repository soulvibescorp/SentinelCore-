import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QFont
from core.utils import log_event, hash_string
from core.auth import store_password, retrieve_password
from core.firewall import monitor_ports  # assuming firewall.py exists

class SentinelCoreApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SentinelCore - Secure & Protect")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(self.load_styles())

        # Layouts
        self.main_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        # UI Elements
        self.status_label = QLabel("Status: Offline")
        self.status_label.setStyleSheet("color: red; font-size: 16px;")
        self.main_layout.addWidget(self.status_label)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.main_layout.addWidget(self.log_output)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password for service (e.g., example.com)")
        self.main_layout.addWidget(self.password_input)

        self.get_password_button = QPushButton("Retrieve Password")
        self.get_password_button.clicked.connect(self.retrieve_password)
        self.main_layout.addWidget(self.get_password_button)

        self.start_button = QPushButton("Start Firewall")
        self.start_button.clicked.connect(self.start_firewall)
        self.button_layout.addWidget(self.start_button)

        self.start_encryption_button = QPushButton("Start Encryption")
        self.start_encryption_button.clicked.connect(self.start_encryption)
        self.button_layout.addWidget(self.start_encryption_button)

        self.main_layout.addLayout(self.button_layout)

        # Set the layout of the window
        self.setLayout(self.main_layout)

        # Periodic refresh every second (for logs)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_log_output)
        self.timer.start(1000)

        # Initial log
        log_event("SentinelCore UI initialized.")
        self.status_label.setText("Status: Ready")

    def load_styles(self):
        """Load a futuristic neon dark theme for the UI"""
        return """
        QWidget {
            background-color: #2d2d2d;
            color: #d1d1d1;
            font-family: "Arial", sans-serif;
        }
        QPushButton {
            background-color: #444444;
            color: #ffffff;
            border: 2px solid #a1c4fd;
            padding: 10px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #555555;
        }
        QTextEdit {
            background-color: #1a1a1a;
            color: #ffffff;
            border: 1px solid #555555;
            padding: 10px;
        }
        QLineEdit {
            background-color: #333333;
            color: #ffffff;
            padding: 10px;
        }
        QLabel {
            font-size: 18px;
        }
        """

    def update_log_output(self):
        """Update logs in the text box"""
        log_file = "logs/sentinel.log"
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                logs = f.read()
                self.log_output.setText(logs)

    def start_firewall(self):
        """Simulate starting the firewall"""
        log_event("Starting firewall...")
        self.status_label.setText("Status: Firewall Active")
        self.monitor_ports()

    def monitor_ports(self):
        """Simulate monitoring ports for activity (Firewall behavior)"""
        # Real dynamic port monitoring logic goes here
        log_event("Monitoring ports...")
        self.status_label.setText("Status: Monitoring Ports")

    def start_encryption(self):
        """Simulate starting encryption"""
        log_event("Starting encryption...")
        self.status_label.setText("Status: Encryption Active")

    def retrieve_password(self):
        """Retrieve password for service from vault"""
        service = self.password_input.text()
        if service:
            username, password = retrieve_password(service)
            if username and password:
                log_event(f"Retrieved password for {service}: {username}")
                self.status_label.setText(f"Password for {service}: {password}")
            else:
                log_event(f"No password found for {service}")
                self.status_label.setText(f"No password found for {service}")
        else:
            log_event("No service entered")
            self.status_label.setText("Enter a service to retrieve password")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SentinelCoreApp()
    window.show()
    sys.exit(app.exec())
