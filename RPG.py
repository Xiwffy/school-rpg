from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QListWidget, QInputDialog, QGroupBox
from PyQt5.QtCore import Qt
from PIL import Image
from PyQt5.QtGui import QPixmap


def vstrecha():
    print(start_bottom.text())
    if start_bottom.text() == 'START!':
        name_start.setText('Приветсвую тебя в твоей игре! \nКак ты знаешь в школе часто бывает скучно и хотелось бы немного веселья и разнообразия\nРешение этого данная "игра" которая поднимет твою мотивацию!')
        start_bottom.setText('Дальше»')
    elif start_bottom.text() == 'Дальше»':
        loadImage()
        start_bottom.setText('Начнём!')
    elif start_bottom.text() == 'Начнём!':
        dude.setText('Всё разъяснили\nПора приступать!')
        w, h = 300, 500
        loadImage()




def loadImage():
    pixmapimage = QPixmap('puro.png')
    w, h = 300, 500
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)
    name_start.setAlignment(Qt.AlignRight)
    dude.show()
    




app = QApplication([])
win = QWidget()


name_start = QLabel('ДОБРО ПОЖАЛОВАТЬ НА ВАШУ ШКОЛЬНУЮ РПГ!')

dude = QLabel('Это твой дружище\nПри помощи твоих знаний ты усилишь его\nНапример: Сделал домашку по матиматике - +5 баллов к уму\nНаписал контрольную работу на 5 - +40 к ХП и тд')


start_bottom = QPushButton('START!')
name_start.setAlignment(Qt.AlignCenter)

box_line = QVBoxLayout()
V_Line = QVBoxLayout()
V2_Line = QVBoxLayout()
H_Line = QHBoxLayout()
H2_Line = QHBoxLayout()

V2_Line.addWidget(dude)
V2_Line.addWidget(name_start)
V2_Line.addWidget(start_bottom)
H_Line.addLayout(V_Line)
H_Line.addLayout(H2_Line)
H_Line.addLayout(V2_Line)
win.setLayout(H_Line)
win.setLayout(box_line)


start_bottom.clicked.connect(vstrecha)

#start.setLayout(H_Line)






















dude.hide()
win.resize(900, 600)
win.setWindowTitle('...---...')
win.show()
app.exec_()
