from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QListWidget, QInputDialog, QGroupBox
from PyQt5.QtCore import Qt

def vstrecha():
    sos.hide()
    start.setLayout(box_line)
    start.show()
app = QApplication([])
win = QWidget()

sos = QGroupBox('')
start = QGroupBox('Начало')
name_start = QLabel('ДОБРО ПОЖАЛОВАТЬ НА ВАШУ ШКОЛЬНУЮ РПГ!')
start_bottom = QPushButton('START!')
name_start.setAlignment(Qt.AlignCenter)

s_label = QLabel('Приветсвую тебя в твоей игре! \nКак ты знаешь в школе часто бывает скучно и хотелось бы немного веселья и разнообразия\nРешение этого данная "игра" которая поднимет твою мотивацию!')

box_line = QVBoxLayout()
V_Line = QVBoxLayout()
V2_Line = QVBoxLayout()
H_Line = QHBoxLayout()
H2_Line = QHBoxLayout()

sos.setLayout(H_Line)
box_line.addWidget(s_label)
V2_Line.addWidget(name_start)
V2_Line.addWidget(start_bottom)
H_Line.addLayout(V_Line)
H_Line.addLayout(H2_Line)
H_Line.addLayout(V2_Line)
win.setLayout(H_Line)
win.setLayout(box_line)


start_bottom.clicked.connect(vstrecha)
#start.setLayout(H_Line)
























win.resize(900, 600)
win.setWindowTitle('...---...')
win.show()
app.exec_()
