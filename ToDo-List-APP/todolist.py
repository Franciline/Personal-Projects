from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#inside the brackets, command lines
#there is one QApplication instance per applications
app = QApplication([])

#we use widget, the window is a widget
window = QWidget()
window.show()

label = QLabel('Hello')
label.show()

#runs the app until closed, starts the loop
app.exec()
