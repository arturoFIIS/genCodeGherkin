from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from parser.parser import procesar_requisito, validar_requisito
from generator.generator import generar_html_ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Interfaces")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.generate_button = QPushButton("Generar HTML", self)
        self.generate_button.clicked.connect(self.generar_html)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.generate_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generar_html(self):
        requisito = self.text_edit.toPlainText()
        try:
            validar_requisito(requisito)
            datos = procesar_requisito(requisito)
            print(datos)  # Debug: Imprimir los datos procesados
            generar_html_ui(datos)
            QMessageBox.information(self, "Éxito", "Archivo HTML generado correctamente.")
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()