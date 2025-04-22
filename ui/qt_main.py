from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon
import sys

class SentinelGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SentinelCore Command Console")
        self.setFixedSize(800, 500)
        self.setStyleSheet(open("ui/styles.qss").read())
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("🛡 SentinelCore • Threat Intelligence Node")
        title.setStyleSheet("font-size: 20px; color: #00ffd5;")
        layout.addWidget(title)

        btn1 = QPushButton("🗄 Encrypt File")
        btn2 = QPushButton("🛡 Simulate Firewall")
        btn3 = QPushButton("🧪 Scan File")
        btn4 = QPushButton("🔐 Access Vault")

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout)

app = QApplication(sys.argv)
window = SentinelGUI()
window.show()
sys.exit(app.exec())
