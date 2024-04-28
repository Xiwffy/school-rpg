from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QListWidget, QInputDialog, QGroupBox,QLineEdit, QRadioButton, QCheckBox
from PyQt5.QtCore import Qt
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont

hp = 0
sheld = 0from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QListWidget, QInputDialog, QGroupBox,QLineEdit, QRadioButton, QCheckBox
from PyQt5.QtCore import Qt
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont

hp = 0
sheld = 0
brain = 0
talking = 0
poison = 0
world_edu = 0

final = 0
lvl = 0


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
        start_bottom.setText('Начнём!!!')
    elif start_bottom.text() == 'Начнём!!!':
        H2_Line.addWidget(pers)
        H2_Line.addWidget(name_start)
        H2_Line.addWidget(razvilka)
        pers.setAlignment(Qt.AlignTop) 
        name_start.setAlignment(Qt.AlignTop) 
        pers2.hide()
        pers3.hide()
        start_bottom.hide()
        loadImage2()
        razvilka.show()
        homework.show()
        works.show()
        info.show()
def score():
    global hp, sheld, brain, talking, poison, world_edu, final
    if bio.isChecked():

        hp += 15
        sheld += 15

        final += 30
        
    if chemist.isChecked():
        poison += 15
        hp += 15

        final += 30
    if obg.isChecked():
        world_edu += 10
        sheld += 15
        hp += 15

        final += 40
    if russian.isChecked():
        talking += 15
        world_edu += 15

        final += 30
    if literatur.isChecked():
        brain += 15
        talking += 10
        world_edu += 15

        final += 40
    if manth.isChecked():
        brain += 20
        final += 20
    if history.isChecked():
        world_edu += 15
        talking += 15

        final += 30
    if piple.isChecked():
        hp += 10
        brain += 15
        world_edu += 15
        talking += 10

        final += 50
    if geo.isChecked():
        brain += 10
        world_edu += 20

        final += 30
    if phisics.isChecked():
        brain += 20
        final += 20
    if informatik.isChecked():
        sheld += 30
        brain += 10

        final += 40
    if eng.isChecked():
        talking += 45

        final += 45
    now.setText(f"За домашку вы получили: {final} очков!!!")
        
def good_job():
    global lvl
    russian.hide()
    literatur.hide()
    manth.hide()
    chemist.hide()
    bio.hide()
    history.hide() 
    piple.hide() 
    geo.hide() 
    phisics.hide() 
    informatik.hide() 
    eng.hide() 
    obg.hide()
    next.hide()
    if final >= 200:
        lvl += 1
        show_lvl.setText(f"Ваш уровень: {lvl}")
    if final >= 405:
        lvl += 1
        show_lvl.setText(f"Ваш уровень: {lvl}")
    
    V2_Line.addWidget(back)
    V_Line.addWidget(now)
    V_Line.addWidget(show_lvl)
    now.setAlignment(Qt.AlignCenter)

def sexyback():
    back.hide()
    now.hide()
    show_lvl.hide()

    razvilka.show()
    homework.show()
    works.show()
    info.show()

    

def loadImage2():
    pixmapimage = QPixmap('puro.png')
    w, h = 100, 100
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)
    #name_start.setAlignment(Qt.AlignRight)
    #name_start.setAlignment(Qt.AlignTop)        

def homeworking():
    razvilka.hide()
    homework.hide()
    works.hide()
    info.hide()

    V_Line.addWidget(russian)
    V2_Line.addWidget(literatur)
    V_Line.addWidget(manth)
    V2_Line.addWidget(geo)
    V_Line.addWidget(chemist)
    V2_Line.addWidget(bio)

    V_Line.addWidget(history)
    V2_Line.addWidget(piple)
    V_Line.addWidget(phisics)
    V2_Line.addWidget(obg)
    V_Line.addWidget(informatik)
    V2_Line.addWidget(eng)

    H_Line.addWidget(next)

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

razvilka = QLabel('Чем сегодня займёмся?')

name_puro = QLineEdit()

start_bottom = QPushButton('START!')
safeandsound = QPushButton('Сохранить')

homework = QPushButton('Домашка')
works = QPushButton('Работы')
info = QPushButton('Инфа о друге')
back = QPushButton('Вернуться в меню')

russian = QCheckBox('Русский')
literatur = QCheckBox('Литра')
manth = QCheckBox('Математика (алгебра/геометрия)')
chemist = QCheckBox('Химия')
bio = QCheckBox('Биология')
history = QCheckBox('История')
piple = QCheckBox('Обществознание')
geo = QCheckBox('География')
phisics = QCheckBox('Физика')
informatik = QCheckBox('Информатика')
eng = QCheckBox('Английский')
obg = QCheckBox('ОБЖ')

next = QPushButton('Закончить')

klass_work = QPushButton('Классная работа')
sam_work = QPushButton('Самостоятельная работа')
check_work = QPushButton('Проверочная работа')
ctrl_work = QPushButton('Контрольная работа')
exam = QPushButton('Экзамен')

russian = QPushButton('Русский')
literatur = QPushButton('Литра')
manth = QPushButton('Математика (алгебра/геометрия)')
chemist = QPushButton('Химия')
bio = QPushButton('Биология')
history = QPushButton('История')
piple = QPushButton('Обществознание')
geo = QPushButton('География')
phisics = QPushButton('Физика')
informatik = QPushButton('Информатика')
eng = QPushButton('Английский')
obg = QPushButton('ОБЖ')

what_mark = QLabel('На какую оценку?')

best_mark = QRadioButton('5')
well_mark = QRadioButton('4')
good_mark = QRadioButton('3')
bad_mark = QRadioButton('2')


now = QLabel(f"За домашку вы получили: {final} очков!!!")
show_lvl = QLabel(f"Ваш уровень: {lvl}")


box_line = QVBoxLayout()
V_Line = QVBoxLayout()
V2_Line = QVBoxLayout()
H_Line = QHBoxLayout()
H2_Line = QHBoxLayout()

# V2_Line.addWidget(purame)
box_line.addWidget(label)


V2_Line.addWidget(pers2, alignment=Qt.AlignBottom)
V2_Line.addWidget(pers)
V2_Line.addWidget(pers3, alignment=Qt.AlignBottom)
V2_Line.addWidget(dude)
V2_Line.addWidget(name_puro, alignment=Qt.AlignBottom)
V2_Line.addWidget(safeandsound)
V2_Line.addWidget(name_start)
V2_Line.addWidget(start_bottom)

V2_Line.addWidget(razvilka)
V2_Line.addWidget(homework)
V2_Line.addWidget(works)
V2_Line.addWidget(info)

H_Line.addLayout(V_Line)
H_Line.addLayout(H2_Line)
H_Line.addLayout(V2_Line)
win.setLayout(H_Line)
win.setLayout(box_line)

homework.clicked.connect(homeworking)
start_bottom.clicked.connect(vstrecha)
safeandsound.clicked.connect(save_name)
safeandsound.clicked.connect(perfect)
next.clicked.connect(score)
next.clicked.connect(good_job)
back.clicked.connect(sexyback)
razvilka.setAlignment(Qt.AlignCenter)


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
razvilka.setFont(font)
now.setFont(font)
show_lvl.setFont(font_4name)





razvilka.hide()
homework.hide()
works.hide()
info.hide()
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

brain = 0
talking = 0
lvl = 0
poison = 0
world_edu = 0

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
        start_bottom.setText('Начнём!!!')
    elif start_bottom.text() == 'Начнём!!!':
        H2_Line.addWidget(pers)
        H2_Line.addWidget(name_start)
        H2_Line.addWidget(razvilka)
        pers.setAlignment(Qt.AlignTop) 
        name_start.setAlignment(Qt.AlignTop) 
        pers2.hide()
        pers3.hide()
        start_bottom.hide()
        loadImage2()
        razvilka.show()
        homework.show()
        works.show()
        info.show()
def score():
    if bio.clicked:
        hp += 15
    if chemist.clicked:
        hp += 15
    if obg.clicked:
        hp += 15

def loadImage2():
    pixmapimage = QPixmap('puro.png')
    w, h = 100, 100
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)
    #name_start.setAlignment(Qt.AlignRight)
    #name_start.setAlignment(Qt.AlignTop)        

def homeworking():
    razvilka.hide()
    homework.hide()
    works.hide()
    info.hide()

    V_Line.addWidget(russian)
    V2_Line.addWidget(literatur)
    V_Line.addWidget(manth)
    V2_Line.addWidget(geo)
    V_Line.addWidget(chemist)
    V2_Line.addWidget(bio)

    V_Line.addWidget(history)
    V2_Line.addWidget(piple)
    V_Line.addWidget(phisics)
    V2_Line.addWidget(obg)
    V_Line.addWidget(informatik)
    V2_Line.addWidget(eng)

    H_Line.addWidget(next)

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

razvilka = QLabel('Чем сегодня займёмся?')

name_puro = QLineEdit()

start_bottom = QPushButton('START!')
safeandsound = QPushButton('Сохранить')

homework = QPushButton('Домашка')
works = QPushButton('Работы')
info = QPushButton('Инфа о друге')

russian = QCheckBox('Русский')
literatur = QCheckBox('Литра')
manth = QCheckBox('Математика (алгебра/геометрия)')
chemist = QCheckBox('Химия')
bio = QCheckBox('Биология')
history = QCheckBox('История')
piple = QCheckBox('Обществознание')
geo = QCheckBox('География')
phisics = QCheckBox('Физика')
informatik = QCheckBox('Информатика')
eng = QCheckBox('Английский')
obg = QCheckBox('ОБЖ')

next = QPushButton('Закончить')





box_line = QVBoxLayout()
V_Line = QVBoxLayout()
V2_Line = QVBoxLayout()
H_Line = QHBoxLayout()
H2_Line = QHBoxLayout()

# V2_Line.addWidget(purame)
box_line.addWidget(label)


V2_Line.addWidget(pers2, alignment=Qt.AlignBottom)
V2_Line.addWidget(pers)
V2_Line.addWidget(pers3, alignment=Qt.AlignBottom)
V2_Line.addWidget(dude)
V2_Line.addWidget(name_puro, alignment=Qt.AlignBottom)
V2_Line.addWidget(safeandsound)
V2_Line.addWidget(name_start)
V2_Line.addWidget(start_bottom)

V2_Line.addWidget(razvilka)
V2_Line.addWidget(homework)
V2_Line.addWidget(works)
V2_Line.addWidget(info)

H_Line.addLayout(V_Line)
H_Line.addLayout(H2_Line)
H_Line.addLayout(V2_Line)
win.setLayout(H_Line)
win.setLayout(box_line)

homework.clicked.connect(homeworking)
start_bottom.clicked.connect(vstrecha)
safeandsound.clicked.connect(save_name)
safeandsound.clicked.connect(perfect)

razvilka.setAlignment(Qt.AlignCenter)


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
razvilka.setFont(font)







razvilka.hide()
homework.hide()
works.hide()
info.hide()
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
