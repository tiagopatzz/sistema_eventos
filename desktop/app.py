import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Check-in de Eventos")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Bem-vindo ao Sistema de Check-in")
        layout.addWidget(self.label)

        self.checkin_button = QPushButton("Registrar Presença")
        self.checkin_button.clicked.connect(self.register_presence)
        layout.addWidget(self.checkin_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def register_presence(self):
        # Lógica para registrar presença
        self.label.setText("Presença registrada com sucesso!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())