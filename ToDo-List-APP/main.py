from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QMenu, QAction 


class MainWindow(QMainWindow):
    """A class for the main window"""

    def __init__(self):
        super().__init__()
        
        #variableS
        self.label = QLabel("Tâches")

        #self.input.textChanged.connect(self.label.setText)

        self.setWindowTitle("To Do List")
        self.setMinimumSize(QSize(400, 300))
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

app = QApplication([])

window = MainWindow()
window.show()

#runs the app until closed, starts the loop
app.exec()
