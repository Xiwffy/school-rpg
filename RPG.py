from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QListWidget, QInputDialog, QGroupBox,QLineEdit, QRadioButton
from PyQt5.QtCore import Qt
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont

name = ''

def vstrecha():
    print(start_bottom.text())
    if start_bottom.text() == 'START!':
        name_start.setText('Приветсвую тебя в твоей игре! \nКак ты знаешь в школе часто бывает скучно и хотелось бы немного веселья и разнообразия\nРешение этого данная "игра" которая поднимет твою мотивацию!')
        start_bottom.setText('Дальше»')
    elif start_bottom.text() == 'Дальше»':
        loadImage()
        
        start_bottom.setText('Начнём!')
        safeandsound.show()
    elif start_bottom.text() == 'Начнём!':
        dude.hide()
        # pers.show()
        # purame.show
        loadImage()




def loadImage():
    pixmapimage = QPixmap('puro.png')
    w, h = 300, 500
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)
    name_start.setAlignment(Qt.AlignRight)
    dude.show()
    name_puro.show()
    
def save_name():
    global name
    name = name_puro.text()
    print(name)
def perfect():
    boxs.setLayout(box_line)
    boxs.show()          








app = QApplication([])
win = QWidget()

boxs = QGroupBox('')
label = QLabel('Имя сохранено!')

name_start = QLabel('ДОБРО ПОЖАЛОВАТЬ НА ВАШУ ШКОЛЬНУЮ РПГ!')
dude = QLabel('Это твой дружище\nПри помощи твоих знаний ты усилишь его\nНапример: Сделал домашку по матиматике - +5 баллов к уму\nНаписал контрольную работу на 5 - +40 к ХП и тд\n\nТы можешь его назвать:')
# purame = QLabel(str(name_puro))
pers = QLabel('Теперь его зовут\n\nВсё разъяснили\nПора приступать!')

name_puro = QLineEdit()

start_bottom = QPushButton('START!')
safeandsound = QPushButton('Сохранить')

name_start.setAlignment(Qt.AlignCenter)
name_puro.setAlignment(Qt.AlignBottom)

box_line = QVBoxLayout()
V_Line = QVBoxLayout()
V2_Line = QVBoxLayout()
H_Line = QHBoxLayout()
H2_Line = QHBoxLayout()

# V2_Line.addWidget(purame)
box_line.addWidget(label)
V2_Line.addWidget(dude)
V2_Line.addWidget(name_puro)
V2_Line.addWidget(safeandsound)
V2_Line.addWidget(name_start)
V2_Line.addWidget(start_bottom)
H_Line.addLayout(V_Line)
H_Line.addLayout(H2_Line)
H_Line.addLayout(V2_Line)
win.setLayout(H_Line)
win.setLayout(box_line)

start_bottom.clicked.connect(vstrecha)
safeandsound.clicked.connect(save_name)
safeandsound.clicked.connect(perfect)

#start.setLayout(H_Line)


# dawn = name_puro.text()

# print(dawn)

font = QFont('Arial', 12)
dude.setFont(font)
name_start.setFont(font)
label.setFont(font)











safeandsound.hide()
name_puro.hide()
# purame.hide()
dude.hide()
# start_bottom.resize(10,10)
win.resize(900, 600)
win.setWindowTitle('...---...')
win.show()
app.exec_()
