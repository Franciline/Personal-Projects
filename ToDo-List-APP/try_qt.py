from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QMenu, QAction 

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    """A class for the main window"""

    def __init__(self):
        super().__init__()
        
        #variable
        self.is_checked = False
        self.label = QLabel()
        self.input = QLineEdit()

        #self.input.textChanged.connect(self.label.setText)

        self.setWindowTitle("To Do List")
        self.setMinimumSize(QSize(400, 300))
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

        """
        self.button = QPushButton("Press Me!")

        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked) #link it to the function
        self.button.clicked.connect(self.button_check)

        self.windowTitleChanged.connect(self.window_title_changed)

        # Set the central widget of the Window
        self.setCentralWidget(self.button) 
        """

    def contextMenuEvent(self, e): #creates menu right click
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())
    """
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")
    """
    def window_title_changed(self, window_title):
        print("test title %s" % window_title)
    

    def button_clicked(self):
        self.button.setText("You clicked me!")
        self.setWindowTitle("oh no")
        #self.button.setEnabled(False)
        

    def button_check(self, checked): #the checked gives info, provided by the clicked signal
        self.is_checked = checked


    """def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        e.accept()
        e.ignore()

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")"""



#inside the brackets, command lines, there is one QApplication instance per applications
app = QApplication([])

window = MainWindow()
window.show()

#runs the app until closed, starts the loop
app.exec()
