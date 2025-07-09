import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)

class SecureUSBApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure USB Access Controller")
        self.setGeometry(100, 100, 420, 250)
        self.initUI()
        self.setStyleSheet("background-color: grey;")

    def initUI(self):
        layout = QVBoxLayout()

        # USB Status
        self.status_label = QLabel("USB Status: 🔒 Blocked")
        self.status_label.setStyleSheet("color: red; font-weight: bold; font-size: 16px;")
        layout.addWidget(self.status_label)

        # Device Info
        self.device_info = QLabel("VID: 1234 | PID: 5678 | Type: Mass Storage")
        layout.addWidget(self.device_info)

        # Buttons
        button_layout = QHBoxLayout()

        whitelist_btn = QPushButton("Add to Whitelist")
        whitelist_btn.clicked.connect(self.add_to_whitelist)
        button_layout.addWidget(whitelist_btn)

        sandbox_btn = QPushButton("Scan in Sandbox")
        sandbox_btn.clicked.connect(self.scan_sandbox)
        button_layout.addWidget(sandbox_btn)

        logs_btn = QPushButton("View Logs")
        logs_btn.clicked.connect(self.view_logs)
        button_layout.addWidget(logs_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def add_to_whitelist(self):
        QMessageBox.information(self, "Whitelist", "Device added to whitelist!")

    def scan_sandbox(self):
        QMessageBox.warning(self, "Sandbox", "Scanning device in sandbox...")

    def view_logs(self):
        QMessageBox.information(self, "Logs", "Opening event logs...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SecureUSBApp()
    window.show()
    sys.exit(app.exec_())
