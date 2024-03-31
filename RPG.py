from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QListWidget, QInputDialog, QGroupBox

from PyQt5.QtCore import Qt
app = QApplication([])
win = QWidget()

start = QGroupBox('Начало')
name_start = QLabel('ДОБРО ПОЖАЛОВАТЬ НА ВАШУ ШКОЛЬНУЮ РПГ!')
start_bottom = QPushButton('START!')
name_start.setAlignment(Qt.AlignCenter)



V_Line = QVBoxLayout()
V2_Line = QVBoxLayout()
H_Line = QHBoxLayout()
H2_Line = QHBoxLayout()


V2_Line.addWidget(name_start)
V2_Line.addWidget(start_bottom)
H_Line.addLayout(V_Line)
H_Line.addLayout(H2_Line)
H_Line.addLayout(V2_Line)
win.setLayout(H_Line)

#start.setLayout(H_Line)
























win.resize(900, 600)
win.setWindowTitle('...---...')
win.show()
app.exec_()
