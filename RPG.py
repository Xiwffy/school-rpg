from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QListWidget, QInputDialog, QGroupBox,QLineEdit, QRadioButton
from PyQt5.QtCore import Qt
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont


name = 'h'

def vstrecha():
    print(start_bottom.text())
    if start_bottom.text() == 'START!':
        name_start.setText('Приветсвую тебя в твоей игре! \nКак ты знаешь в школе часто бывает скучно и хотелось бы немного веселья и разнообразия\nРешение этого данная "игра" которая поднимет твою мотивацию!')
        start_bottom.setText('Дальше»')
    elif start_bottom.text() == 'Дальше»':
        loadImage()
        
        safeandsound.show()
        start_bottom.setText('Начнём!')
    elif start_bottom.text() == 'Начнём!':
        safeandsound.hide()
        name_puro.hide()
        boxs.hide()
        dude.hide()
        # name_start.hide()
        pers.setText(name)
        pers.show()
        pers2.show()
        pers3.show()
        # purame.show
        




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
pers = QLabel(name)
pers2 = QLabel('Теперь его зовут:')
pers3 = QLabel('Давай начнём это!')

name_puro = QLineEdit()

start_bottom = QPushButton('START!')
safeandsound = QPushButton('Сохранить')




box_line = QVBoxLayout()
V_Line = QVBoxLayout()
V2_Line = QVBoxLayout()
H_Line = QHBoxLayout()
H2_Line = QHBoxLayout()

# V2_Line.addWidget(purame)
box_line.addWidget(label)
V2_Line.addWidget(pers2, alignment=Qt.AlignBottom)
V2_Line.addWidget(pers, alignment=Qt.AlignBottom)
V2_Line.addWidget(pers3, alignment=Qt.AlignBottom)
V2_Line.addWidget(dude)
V2_Line.addWidget(name_puro, alignment=Qt.AlignBottom)
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

name_start.setAlignment(Qt.AlignCenter)
name_puro.setAlignment(Qt.AlignBottom)
pers.setAlignment(Qt.AlignBottom)
pers2.setAlignment(Qt.AlignBottom)
pers3.setAlignment(Qt.AlignBottom)


font = QFont('Arial', 12)
font_4name = QFont('Verdana', 20)
# font.configure(weight = 'bold')
dude.setFont(font)
name_start.setFont(font)
label.setFont(font)
pers.setFont(font_4name)
pers2.setFont(font)
pers3.setFont(font)









pers.hide()
pers2.hide()
pers3.hide()

safeandsound.hide()
name_puro.hide()

dude.hide()
win.resize(900, 600)
win.setWindowTitle('...---...')
win.show()
app.exec_()
