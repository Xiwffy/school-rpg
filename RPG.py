from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QListWidget, QInputDialog, QGroupBox,QLineEdit, QRadioButton, QCheckBox
from PyQt5.QtCore import Qt
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
from time import *
global hp, sheld, brain, talking, poison, world_edu, final

hp = 0
sheld = 0
brain = 0
talking = 0
poison = 0
world_edu = 0

final = 0
lvl = 0

klass = False
sam = False
check = False
ctrl = False
ex = False

russian = False
litra = False
matimatik = False
geografi = False
himic = False
biologi = False
istoria = False
obshestvo = False
fisic = False
python_cool = False
fabric = False
obege = False

name = 'start name'

def vstrecha():
    # print(start_bottom.text())
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
    infourok.setText(f'Ваша статистика:\nУровень: {lvl}\n\nЗдоровье: {hp}\nЗащита: {sheld}\nРазум: {brain}\nКрасноречие: {talking}\nОбществознание: {world_edu}\nЗельеварение: {poison}\n\n\nВсего очков: {final}')
    # final = 0

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
    if final >= 405 * 4:
        lvl += 1
        show_lvl.setText(f"Ваш уровень: {lvl}")
    if final >= 405 * 8:
        lvl += 1
        show_lvl.setText(f"Ваш уровень: {lvl}")
    if final >= 405 * 10:
        lvl += 1
        show_lvl.setText(f"Ваш уровень: {lvl}")
    
    back.show()
    now.show()
    show_lvl.show()
    V2_Line.addWidget(back)
    V_Line.addWidget(now)
    V_Line.addWidget(show_lvl)
    now.setAlignment(Qt.AlignCenter)
    infourok.setText(f'Ваша статистика:\nУровень: {lvl}\n\nЗдоровье: {hp}\nЗащита: {sheld}\nРазум: {brain}\nКрасноречие: {talking}\nОбществознание: {world_edu}\nЗельеварение: {poison}\n\n\nВсего очков: {final}')

def sexyback():
    back.hide()
    now.hide()
    show_lvl.hide()

    show_main()
    loadImage2()
    

def show_main():
    global animka
    razvilka.show()
    homework.show()
    works.show()
    info.show()
    loadImage2()
    animka = False


def hide_main():
    razvilka.hide()
    homework.hide()
    works.hide()
    info.hide()

def popa():
    show_main()
    wasd.hide()
    infourok.hide()

def loadImage2():
    pixmapimage = QPixmap('puro.png')
    w, h = 100, 100
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)
    #name_start.setAlignment(Qt.AlignRight)
    #name_start.setAlignment(Qt.AlignTop)    
    
def loadImage_read():
    pixmapimage = QPixmap('puro read.png')
    w, h = 100, 100
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)

def loadImage_hape():
    pixmapimage = QPixmap('hape puro.png')
    w, h = 100, 100
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)

def loadImage_well():
    pixmapimage = QPixmap('well puro.png')
    w, h = 100, 100
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)

def loadImage_gret():
    pixmapimage = QPixmap('great puro.png')
    w, h = 100, 100
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)

def loadImage_bad():
    pixmapimage = QPixmap('sad puro.png')
    w, h = 100, 100
    pixmapimage = pixmapimage.scaled(w, h)
    name_start.setPixmap(pixmapimage)

# def frame1():
#     pixmapimage = QPixmap('eppy 1.png')
#     w, h = 100, 100
#     pixmapimage = pixmapimage.scaled(w, h)
#     name_start.setPixmap(pixmapimage)

# def frame2():
#     pixmapimage = QPixmap('eppy 2.png')
#     w, h = 100, 100
#     pixmapimage = pixmapimage.scaled(w, h)
#     name_start.setPixmap(pixmapimage)

# def frame3():
#     pixmapimage = QPixmap('eppy 3.png')
#     w, h = 100, 100
#     pixmapimage = pixmapimage.scaled(w, h)
#     name_start.setPixmap(pixmapimage)

# def frame4():
#     pixmapimage = QPixmap('eppy 4.png')
#     w, h = 100, 100
#     pixmapimage = pixmapimage.scaled(w, h)
#     name_start.setPixmap(pixmapimage)

# def frame5():
#     pixmapimage = QPixmap('eppy 5.png')
#     w, h = 100, 100
#     pixmapimage = pixmapimage.scaled(w, h)
#     name_start.setPixmap(pixmapimage)

# def frame6():
#     pixmapimage = QPixmap('eppy 6.png')
#     w, h = 100, 100
#     pixmapimage = pixmapimage.scaled(w, h)
#     name_start.setPixmap(pixmapimage)

# # def animation():
# #     # global animka
# #     # while animka != False:
# #     frame1()
# #     sleep(1)
# #     frame2()
# #     sleep(1)
# #     frame3()
# #     sleep(1)
# #     frame4()
# #     sleep(1)
# #     frame5()
# #     sleep(1)
# #     frame6()

def homeworking():
    russian.setChecked(False)
    literatur.setChecked(False)
    manth.setChecked(False)
    geo.setChecked(False)
    chemist.setChecked(False)
    bio.setChecked(False)
    history.setChecked(False)
    piple.setChecked(False)
    phisics.setChecked(False)
    informatik.setChecked(False)
    eng.setChecked(False)
    obg.setChecked(False)
    
    razvilka.hide()
    homework.hide()
    works.hide()
    info.hide()

    russian.show()
    literatur.show()
    manth.show()
    geo.show()
    chemist.show()
    bio.show()
    history.show()
    piple.show()
    phisics.show() 
    informatik.show() 
    eng.show() 
    obg.show()
    next.show()


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

def work():
    hide_main()
    H2_Line.addWidget(type_work)

    type_work.show()
    klass_work.show()
    sam_work.show()
    check_work.show()
    ctrl_work.show()
    exam.show()
    lesson.show()

    V2_Line.addWidget(klass_work)
    V2_Line.addWidget(sam_work)
    V2_Line.addWidget(check_work)
    V2_Line.addWidget(ctrl_work)
    V2_Line.addWidget(exam)
    H2_Line.addWidget(lesson)

def choose():
    global klass, sam, check, ctrl, ex
    type_work.hide()
    klass_work.hide()
    sam_work.hide()
    check_work.hide()
    ctrl_work.hide()
    exam.hide()
    lesson.hide()

    if klass_work.isChecked():
        klass = True
    if sam_work.isChecked():
        sam = True
    if check_work.isChecked():
        check = True
    if ctrl_work.isChecked():
        ctrl = True
    if exam.isChecked():
        ex = True

    subject.show()
    russian_bottom.show()
    literatur_bottom.show()
    manth_bottom.show()
    geo_bottom.show()
    chemist_bottom.show()
    bio_bottom.show()
    history_bottom.show()
    piple_bottom.show()
    phisics_bottom.show() 
    informatik_bottom.show() 
    eng_bottom.show() 
    obg_bottom.show()
    btn_mark.show()
    H2_Line.addWidget(subject)
    
    V_Line.addWidget(russian_bottom)
    V2_Line.addWidget(literatur_bottom)
    V_Line.addWidget(manth_bottom)
    V2_Line.addWidget(geo_bottom)
    V_Line.addWidget(chemist_bottom)
    V2_Line.addWidget(bio_bottom)

    V_Line.addWidget(history_bottom)
    V2_Line.addWidget(piple_bottom)
    V_Line.addWidget(phisics_bottom)
    V2_Line.addWidget(obg_bottom)
    V_Line.addWidget(informatik_bottom)
    V2_Line.addWidget(eng_bottom)
    H_Line.addWidget(btn_mark)
    subject.setAlignment(Qt.AlignCenter)

def marks():
    global russian, litra, matimatik, geografi, himic, biologi, istoria, obshestvo, fisic, python_cool, fabric, obege
    # best_mark.setChecked(False)
    # well_mark.setChecked(False)
    # good_mark.setChecked(False)
    # bad_mark.setChecked(False)
    # bottom_final.setChecked(False)
    if russian_bottom.isChecked():
        russian = True
    if literatur_bottom.isChecked():
        litra = True
    if manth_bottom.isChecked():
        matimatik = True
    if geo_bottom.isChecked():
        geografi  = True
    if chemist_bottom.isChecked():
        himic = True
    if bio_bottom.isChecked():
        biologi  = True
    if history_bottom.isChecked():
        istoria = True
    if piple_bottom.isChecked():
        obshestvo = True
    if phisics_bottom.isChecked():
        fisic = True
    if informatik_bottom.isChecked():
        python_cool = True
    if eng_bottom.isChecked():
        fabric = True
    if obg_bottom.isChecked():
        obege = True

    subject.hide()
    russian_bottom.hide()
    literatur_bottom.hide()
    manth_bottom.hide()
    geo_bottom.hide()
    chemist_bottom.hide()
    bio_bottom.hide()
    history_bottom.hide()
    piple_bottom.hide()
    phisics_bottom.hide() 
    informatik_bottom.hide() 
    eng_bottom.hide() 
    obg_bottom.hide()
    btn_mark.hide()
    
    what_mark.show()
    best_mark.show()
    well_mark.show()
    good_mark.show()
    bad_mark.show()
    bottom_final.show()


    H2_Line.addWidget(what_mark)
    V2_Line.addWidget(best_mark)
    V2_Line.addWidget(well_mark)
    V2_Line.addWidget(good_mark)
    V2_Line.addWidget(bad_mark)
    H_Line.addWidget(bottom_final)


def kys_back():
    show_main()

    what_mark.hide()
    kys.hide()

def score_mark():
    global hp, sheld, brain, talking, poison, world_edu, final, lvl
    global klass, sam, check, ctrl, ex, russian, litra, matimatik, geografi, himic, biologi, istoria, obshestvo, fisic, python_cool, fabric, obege
    what_mark.setText('Хорошая работа!')
    best_mark.hide()
    well_mark.hide()
    good_mark.hide()
    bad_mark.hide()
    bottom_final.hide()

    kys.show()
    H_Line.addWidget(kys)
    
    #КЛАССНАЯ ЧЕТВЁРКА
    if russian and russian and well_mark.isChecked():
        talking += 70
        world_edu += 50
        
        final += 120
    if klass and litra and well_mark.isChecked():
        brain += 45
        talking += 25
        world_edu += 25

        final += 95
    if klass and matimatik and well_mark.isChecked():
        brain += 20

        final += 20
    if klass and geografi and well_mark.isChecked():
        brain += 20
        world_edu += 25

        final += 45
    if klass and himic and well_mark.isChecked():
        poison += 25
        hp += 25

        final += 50
    if klass and biologi and well_mark.isChecked():
        hp += 25
        sheld += 25

        final += 50
    if klass and istoria and well_mark.isChecked():
        world_edu += 25
        talking += 25

        final += 50
    if klass and obshestvo and well_mark.isChecked():
        hp += 20
        brain += 25
        world_edu += 25
        talking += 20

        final += 90
    if klass and fisic and well_mark.isChecked():
        brain += 30

        final += 30
    if klass and python_cool and well_mark.isChecked():
        sheld += 40
        brain += 20

        final += 60
    if klass and fabric and well_mark.isChecked():
        talking += 55

        final += 55
    if klass and obege and well_mark.isChecked():
        world_edu += 20
        sheld += 25
        hp += 25

        final += 70
    ##КЛАССНАЯ ПЯТЁРКА

    if klass and russian and best_mark.isChecked():
        talking += 85
        world_edu += 75

        final += 160
    if klass and litra and best_mark.isChecked():
        brain += 70
        talking += 50
        world_edu += 50

        final += 170
    if klass and matimatik and best_mark.isChecked():
        brain += 45

        final += 45
    if klass and geografi and best_mark.isChecked():
        brain += 45
        world_edu += 50

        final += 95
    if klass and himic and best_mark.isChecked():
        poison += 50
        hp += 50

        final += 100
    if klass and biologi and best_mark.isChecked():
        hp += 50
        sheld += 50

        final += 100
    if klass and istoria and best_mark.isChecked():
        world_edu += 50
        talking += 50

        final += 100
    if klass and obshestvo and best_mark.isChecked():
        hp += 45
        brain += 50
        world_edu += 50
        talking += 45

        final += 190
    if klass and fisic and best_mark.isChecked():
        brain += 55

        final += 55
    if klass and python_cool and best_mark.isChecked():
        sheld += 65
        brain += 45

        final += 110
    if klass and fabric and best_mark.isChecked():
        talking += 80

        final += 80
    if klass and obege and best_mark.isChecked():
        world_edu += 45
        sheld += 50
        hp += 50

        final += 145
    #КЛАССНАЯ ТРОЙКА

    if klass and russian and good_mark.isChecked():
        talking += 55
        world_edu += 35

        final += 90
    if klass and litra and good_mark.isChecked():
        brain += 30
        talking += 10
        world_edu += 10

        final += 50
    if klass and matimatik and good_mark.isChecked():
        brain += 10

        final += 10
    if klass and geografi and good_mark.isChecked():
        brain += 10
        world_edu += 10

        final += 20
    if klass and himic and good_mark.isChecked():
        poison += 10
        hp += 10

        final += 20
    if klass and biologi and good_mark.isChecked():
        hp += 10
        sheld += 10

        final += 20
    if klass and istoria and good_mark.isChecked():
        world_edu += 10
        talking += 10

        final += 20
    if klass and obshestvo and good_mark.isChecked():
        hp += 10
        brain += 10
        world_edu += 10
        talking += 10

        final += 40
    if klass and fisic and good_mark.isChecked():
        brain += 15

        final += 15
    if klass and python_cool and good_mark.isChecked():
        sheld += 25
        brain += 10

        final += 35
    if klass and fabric and good_mark.isChecked():
        talking += 40

        final += 40
    if klass and obege and good_mark.isChecked():
        world_edu += 10
        sheld += 10
        hp += 10

        final += 30

    #КЛАССНАЯ ПАРАША

    if klass and russian and bad_mark.isChecked():
        talking -= 30
        world_edu -= 15

        final -= 45
    if klass and litra and bad_mark.isChecked():
        brain -= 15
        talking -= 10
        world_edu -= 10

        final -= 45
    if klass and matimatik and bad_mark.isChecked():
        brain -= 10

        final -= 10
    if klass and geografi and bad_mark.isChecked():
        brain -= 10
        world_edu -= 10

        final -= 20
    if klass and himic and bad_mark.isChecked():
        poison -= 10
        hp -= 10

        final -= 20
    if klass and biologi and bad_mark.isChecked():
        hp -= 10
        sheld -= 10

        final -= 20
    if klass and istoria and bad_mark.isChecked():
        world_edu -= 10
        talking -= 10
        final -= 20
    if klass and obshestvo and bad_mark.isChecked():
        hp -= 10
        brain -= 10
        world_edu -= 10
        talking -= 10

        final -= 40
    if klass and fisic and bad_mark.isChecked():
        brain -= 15

        final -= 15
    if klass and python_cool and bad_mark.isChecked():
        sheld -= 15
        brain -= 10

        final -= 25                                             
    if klass and fabric and bad_mark.isChecked():
        talking -= 20

        final -= 20
    if klass and obege and bad_mark.isChecked():
        world_edu -= 10
        sheld -= 10
        hp -= 10
        final -= 30

    if sam:
        if russian and well_mark.isChecked():
            talking += 70 + 15
            world_edu += 50 + 15
            final += (70 + 15) + (50 + 15)
        if litra and well_mark.isChecked():
            brain += 45 + 15
            talking += 25 + 15
            world_edu += 25 + 15
            final += (45 + 15) + (25 + 15) + (25 + 15)
        if matimatik and well_mark.isChecked():
            brain += 20 + 15
            final += 20 + 15
        if geografi and well_mark.isChecked():
            brain += 20 + 15
            world_edu += 25 + 15
            final += (20 + 15) + (25 + 15)
        if himic and well_mark.isChecked():
            poison += 25 + 15
            hp += 25 + 15
            final += (25 + 15) + (25 + 15)
        if biologi and well_mark.isChecked():
            hp += 25 + 15
            sheld += 25 + 15
            final += (25 + 15) + (25 + 15)
        if istoria and well_mark.isChecked():
            world_edu += 25 + 15
            talking += 25 + 15
            final += (25 + 15) + (25 + 15)
        if obshestvo and well_mark.isChecked():
            hp += 20 + 15
            brain += 25 + 15
            world_edu += 25 + 15
            talking += 20 + 15
            final += (20 + 15) + (25 + 15) + (25 + 15) + (20 + 15)
        if fisic and well_mark.isChecked():
            brain += 30 + 15
            final += 30 + 15
        if python_cool and well_mark.isChecked():
            sheld += 40 + 15
            brain += 20 + 15
            final += (40 + 15) + (20 + 15)
        if fabric and well_mark.isChecked():
            talking += 55 + 15
            final += 55 + 15
        if obege and well_mark.isChecked():
            world_edu += 20 + 15
            sheld += 25 + 15
            hp += 25 + 15
            final += (20 + 15) + (25 + 15) + (25 + 15)

        # КЛАССНАЯ ПЯТЁРКА
        if russian and best_mark.isChecked():
            talking += 85 + 15
            world_edu += 75 + 15
            final += (85 + 15) + (75 + 15)
        if litra and best_mark.isChecked():
            brain += 70 + 15
            talking += 50 + 15
            world_edu += 50 + 15
            final += (70 + 15) + (50 + 15) + (50 + 15)
        if matimatik and best_mark.isChecked():
            brain += 45 + 15
            final += 45 + 15
        if geografi and best_mark.isChecked():
            brain += 45 + 15
            world_edu += 50 + 15
            final += (45 + 15) + (50 + 15)
        if himic and best_mark.isChecked():
            poison += 50 + 15
            hp += 50 + 15
            final += (50 + 15) + (50 + 15)
        if biologi and best_mark.isChecked():
            hp += 50 + 15
            sheld += 50 + 15
            final += (50 + 15) + (50 + 15)
        if istoria and best_mark.isChecked():
            world_edu += 50 + 15
            talking += 50 + 15
            final += (50 + 15) + (50 + 15)
        if obshestvo and best_mark.isChecked():
            hp += 45 + 15
            brain += 50 + 15
            world_edu += 50 + 15
            talking += 45 + 15
            final += (45 + 15) + (50 + 15) + (50 + 15) + (45 + 15)
        if fisic and best_mark.isChecked():
            brain += 55 + 15
            final += 55 + 15
        if python_cool and best_mark.isChecked():
            sheld += 65 + 15
            brain += 45 + 15
            final += (65 + 15) + (45 + 15)
        if fabric and best_mark.isChecked():
            talking += 80 + 15
            final += 80 + 15
        if obege and best_mark.isChecked():
            world_edu += 45 + 15
            sheld += 50 + 15
            hp += 50 + 15
            final += (45 + 15) + (50 + 15) + (50 + 15)

        # КЛАССНАЯ ТРОЙКА
        if russian and good_mark.isChecked():
            talking += 55 + 15
            world_edu += 35 + 15
            final += (55 + 15) + (35 + 15)
        if litra and good_mark.isChecked():
            brain += 30 + 15
            talking += 10 + 15
            world_edu += 10 + 15
            final += (30 + 15) + (10 + 15) + (10 + 15)
        if matimatik and good_mark.isChecked():
            brain += 10 + 15
            final += 10 + 15
        if geografi and good_mark.isChecked():
            brain += 10 + 15
            world_edu += 10 + 15
            final += (10 + 15) + (10 + 15)
        if himic and good_mark.isChecked():
            poison += 10 + 15
            hp += 10 + 15
            final += (10 + 15) + (10 + 15)
        if biologi and good_mark.isChecked():
            hp += 10 + 15
            sheld += 10 + 15
            final += (10 + 15) + (10 + 15)
        if istoria and good_mark.isChecked():
            world_edu += 10 + 15
            talking += 10 + 15
            final += (10 + 15) + (10 + 15)
        if obshestvo and good_mark.isChecked():
            hp += 10 + 15
            brain += 10 + 15
            world_edu += 10 + 15
            talking += 10 + 15
            final += (10 + 15) + (10 + 15) + (10 + 15) + (10 + 15)
        if fisic and good_mark.isChecked():
            brain += 15 + 15
            final += 15 + 15
        if python_cool and good_mark.isChecked():
            sheld += 25 + 15
            brain += 10 + 15
            final += (25 + 15) + (10 + 15)
        if fabric and good_mark.isChecked():
            talking += 40 + 15
            final += 40 + 15
        if obege and good_mark.isChecked():
            world_edu += 10 + 15
            sheld += 10 + 15
            hp += 10 + 15
            final += (10 + 15) + (10 + 15) + (10 + 15)

        # КЛАССНАЯ ПАРАША
        if russian and bad_mark.isChecked():
            talking -= 30
            world_edu -= 15
            final -= 30 + 15
        if litra and bad_mark.isChecked():
            brain -= 15
            talking -= 10
            world_edu -= 10
            final -= 15 + 10 + 10
        if matimatik and bad_mark.isChecked():
            brain -= 10
            final -= 10
        if geografi and bad_mark.isChecked():
            brain -= 10
            world_edu -= 10
            final -= 10 + 10
        if himic and bad_mark.isChecked():
            poison -= 10
            hp -= 10
            final -= 10 + 10
        if biologi and bad_mark.isChecked():
            hp -= 10
            sheld -= 10
            final -= 10 + 10
        if istoria and bad_mark.isChecked():
            world_edu -= 10
            talking -= 10
            final -= 10 + 10
        if obshestvo and bad_mark.isChecked():
            hp -= 10
            brain -= 10
            world_edu -= 10
            talking -= 10
            final -= 10 + 10 + 10 + 10
        if fisic and bad_mark.isChecked():
            brain -= 15
            final -= 15
        if python_cool and bad_mark.isChecked():
            sheld -= 15
            brain -= 10
            final -= 15 + 10
        if fabric and bad_mark.isChecked():
            talking -= 20
            final -= 20
        if obege and bad_mark.isChecked():
            world_edu -= 10
            sheld -= 10
            hp -= 10
            final -= 10 + 10 + 10
    

    if check:
        if russian and well_mark.isChecked():
            talking += 70 + 30
            world_edu += 50 + 30
            final += (70 + 30) + (50 + 30)
        if litra and well_mark.isChecked():
            brain += 45 + 30
            talking += 25 + 30
            world_edu += 25 + 30
            final += (45 + 30) + (25 + 30) + (25 + 30)
        if matimatik and well_mark.isChecked():
            brain += 20 + 30
            final += 20 + 30
        if geografi and well_mark.isChecked():
            brain += 20 + 30
            world_edu += 25 + 30
            final += (20 + 30) + (25 + 30)
        if himic and well_mark.isChecked():
            poison += 25 + 30
            hp += 25 + 30
            final += (25 + 30) + (25 + 30)
        if biologi and well_mark.isChecked():
            hp += 25 + 30
            sheld += 25 + 30
            final += (25 + 30) + (25 + 30)
        if istoria and well_mark.isChecked():
            world_edu += 25 + 30
            talking += 25 + 30
            final += (25 + 30) + (25 + 30)
        if obshestvo and well_mark.isChecked():
            hp += 20 + 30
            brain += 25 + 30
            world_edu += 25 + 30
            talking += 20 + 30
            final += (20 + 30) + (25 + 30) + (25 + 30) + (20 + 30)
        if fisic and well_mark.isChecked():
            brain += 30 + 30
            final += 30 + 30
        if python_cool and well_mark.isChecked():
            sheld += 40 + 30
            brain += 20 + 30
            final += (40 + 30) + (20 + 30)
        if fabric and well_mark.isChecked():
            talking += 55 + 30
            final += 55 + 30
        if obege and well_mark.isChecked():
            world_edu += 20 + 30
            sheld += 25 + 30
            hp += 25 + 30
            final += (20 + 30) + (25 + 30) + (25 + 30)

        # КЛАССНАЯ ПЯТЁРКА
        if russian and best_mark.isChecked():
            talking += 85 + 30
            world_edu += 75 + 30
            final += (85 + 30) + (75 + 30)
        if litra and best_mark.isChecked():
            brain += 70 + 30
            talking += 50 + 30
            world_edu += 50 + 30
            final += (70 + 30) + (50 + 30) + (50 + 30)
        if matimatik and best_mark.isChecked():
            brain += 45 + 30
            final += 45 + 30
        if geografi and best_mark.isChecked():
            brain += 45 + 30
            world_edu += 50 + 30
            final += (45 + 30) + (50 + 30)
        if himic and best_mark.isChecked():
            poison += 50 + 30
            hp += 50 + 30
            final += (50 + 30) + (50 + 30)
        if biologi and best_mark.isChecked():
            hp += 50 + 30
            sheld += 50 + 30
            final += (50 + 30) + (50 + 30)
        if istoria and best_mark.isChecked():
            world_edu += 50 + 30
            talking += 50 + 30
            final += (50 + 30) + (50 + 30)
        if obshestvo and best_mark.isChecked():
            hp += 45 + 30
            brain += 50 + 30
            world_edu += 50 + 30
            talking += 45 + 30
            final += (45 + 30) + (50 + 30) + (50 + 30) + (45 + 30)
        if fisic and best_mark.isChecked():
            brain += 55 + 30
            final += 55 + 30
        if python_cool and best_mark.isChecked():
            sheld += 65 + 30
            brain += 45 + 30
            final += (65 + 30) + (45 + 30)
        if fabric and best_mark.isChecked():
            talking += 80 + 30
            final += 80 + 30
        if obege and best_mark.isChecked():
            world_edu += 45 + 30
            sheld += 50 + 30
            hp += 50 + 30
            final += (45 + 30) + (50 + 30) + (50 + 30)

        # КЛАССНАЯ ТРОЙКА
        if russian and good_mark.isChecked():
            talking += 55 + 30
            world_edu += 35 + 30
            final += (55 + 30) + (35 + 30)
        if litra and good_mark.isChecked():
            brain += 30 + 30
            talking += 10 + 30
            world_edu += 10 + 30
            final += (30 + 30) + (10 + 30) + (10 + 30)
        if matimatik and good_mark.isChecked():
            brain += 10 + 30
            final += 10 + 30
        if geografi and good_mark.isChecked():
            brain += 10 + 30
            world_edu += 10 + 30
            final += (10 + 30) + (10 + 30)
        if himic and good_mark.isChecked():
            poison += 10 + 30
            hp += 10 + 30
            final += (10 + 30) + (10 + 30)
        if biologi and good_mark.isChecked():
            hp += 10 + 30
            sheld += 10 + 30
            final += (10 + 30) + (10 + 30)
        if istoria and good_mark.isChecked():
            world_edu += 10 + 30
            talking += 10 + 30
            final += (10 + 30) + (10 + 30)
        if obshestvo and good_mark.isChecked():
            hp += 10 + 30
            brain += 10 + 30
            world_edu += 10 + 30
            talking += 10 + 30
            final += (10 + 30) + (10 + 30) + (10 + 30) + (10 + 30)
        if fisic and good_mark.isChecked():
            brain += 15 + 30
            final += 15 + 30
        if python_cool and good_mark.isChecked():
            sheld += 25 + 30
            brain += 10 + 30
            final += (25 + 30) + (10 + 30)
        if fabric and good_mark.isChecked():
            talking += 40 + 30
            final += 40 + 30
        if obege and good_mark.isChecked():
            world_edu += 10 + 30
            sheld += 10 + 30
            hp += 10 + 30
            final += (10 + 30) + (10 + 30) + (10 + 30)

        # КЛАССНАЯ ПАРАША
        if russian and bad_mark.isChecked():
            talking -= 30
            world_edu -= 15
            final -= 30 + 15
        if litra and bad_mark.isChecked():
            brain -= 15
            talking -= 10
            world_edu -= 10
            final -= 15 + 10 + 10
        if matimatik and bad_mark.isChecked():
            brain -= 10
            final -= 10
        if geografi and bad_mark.isChecked():
            brain -= 10
            world_edu -= 10
            final -= 10 + 10
        if himic and bad_mark.isChecked():
            poison -= 10
            hp -= 10
            final -= 10 + 10
        if biologi and bad_mark.isChecked():
            hp -= 10
            sheld -= 10
            final -= 10 + 10
        if istoria and bad_mark.isChecked():
            world_edu -= 10
            talking -= 10
            final -= 10 + 10
        if obshestvo and bad_mark.isChecked():
            hp -= 10
            brain -= 10
            world_edu -= 10
            talking -= 10
            final -= 10 + 10 + 10 + 10
        if fisic and bad_mark.isChecked():
            brain -= 15
            final -= 15
        if python_cool and bad_mark.isChecked():
            sheld -= 15
            brain -= 10
            final -= 15 + 10
        if fabric and bad_mark.isChecked():
            talking -= 20
            final -= 20
        if obege and bad_mark.isChecked():
            world_edu -= 10
            sheld -= 10
            hp -= 10
            final -= 10 + 10 + 10







    if ctrl:
        if russian and well_mark.isChecked():
            talking += 70 + 50
            world_edu += 50 + 50
            final += (70 + 50) + (50 + 50)
        if litra and well_mark.isChecked():
            brain += 45 + 50
            talking += 25 + 50
            world_edu += 25 + 50
            final += (45 + 50) + (25 + 50) + (25 + 50)
        if matimatik and well_mark.isChecked():
            brain += 20 + 50
            final += 20 + 50
        if geografi and well_mark.isChecked():
            brain += 20 + 50
            world_edu += 25 + 50
            final += (20 + 50) + (25 + 50)
        if himic and well_mark.isChecked():
            poison += 25 + 50
            hp += 25 + 50
            final += (25 + 50) + (25 + 50)
        if biologi and well_mark.isChecked():
            hp += 25 + 50
            sheld += 25 + 50
            final += (25 + 50) + (25 + 50)
        if istoria and well_mark.isChecked():
            world_edu += 25 + 50
            talking += 25 + 50
            final += (25 + 50) + (25 + 50)
        if obshestvo and well_mark.isChecked():
            hp += 20 + 50
            brain += 25 + 50
            world_edu += 25 + 50
            talking += 20 + 50
            final += (20 + 50) + (25 + 50) + (25 + 50) + (20 + 50)
        if fisic and well_mark.isChecked():
            brain += 30 + 50
            final += 30 + 50
        if python_cool and well_mark.isChecked():
            sheld += 40 + 50
            brain += 20 + 50
            final += (40 + 50) + (20 + 50)
        if fabric and well_mark.isChecked():
            talking += 55 + 50
            final += 55 + 50
        if obege and well_mark.isChecked():
            world_edu += 20 + 50
            sheld += 25 + 50
            hp += 25 + 50
            final += (20 + 50) + (25 + 50) + (25 + 50)

        # КЛАССНАЯ ПЯТЁРКА
        if russian and best_mark.isChecked():
            talking += 85 + 50
            world_edu += 75 + 50
            final += (85 + 50) + (75 + 50)
        if litra and best_mark.isChecked():
            brain += 70 + 50
            talking += 50 + 50
            world_edu += 50 + 50
            final += (70 + 50) + (50 + 50) + (50 + 50)
        if matimatik and best_mark.isChecked():
            brain += 45 + 50
            final += 45 + 50
        if geografi and best_mark.isChecked():
            brain += 45 + 50
            world_edu += 50 + 50
            final += (45 + 50) + (50 + 50)
        if himic and best_mark.isChecked():
            poison += 50 + 50
            hp += 50 + 50
            final += (50 + 50) + (50 + 50)
        if biologi and best_mark.isChecked():
            hp += 50 + 50
            sheld += 50 + 50
            final += (50 + 50) + (50 + 50)
        if istoria and best_mark.isChecked():
            world_edu += 50 + 50
            talking += 50 + 50
            final += (50 + 50) + (50 + 50)
        if obshestvo and best_mark.isChecked():
            hp += 45 + 50
            brain += 50 + 50
            world_edu += 50 + 50
            talking += 45 + 50
            final += (45 + 50) + (50 + 50) + (50 + 50) + (45 + 50)
        if fisic and best_mark.isChecked():
            brain += 55 + 50
            final += 55 + 50
        if python_cool and best_mark.isChecked():
            sheld += 65 + 50
            brain += 45 + 50
            final += (65 + 50) + (45 + 50)
        if fabric and best_mark.isChecked():
            talking += 80 + 50
            final += 80 + 50
        if obege and best_mark.isChecked():
            world_edu += 45 + 50
            sheld += 50 + 50
            hp += 50 + 50
            final += (45 + 50) + (50 + 50) + (50 + 50)

        # КЛАССНАЯ ТРОЙКА
        if russian and good_mark.isChecked():
            talking += 55 + 50
            world_edu += 35 + 50
            final += (55 + 50) + (35 + 50)
        if litra and good_mark.isChecked():
            brain += 30 + 50
            talking += 10 + 50
            world_edu += 10 + 50
            final += (30 + 50) + (10 + 50) + (10 + 50)
        if matimatik and good_mark.isChecked():
            brain += 10 + 50
            final += 10 + 50
        if geografi and good_mark.isChecked():
            brain += 10 + 50
            world_edu += 10 + 50
            final += (10 + 50) + (10 + 50)
        if himic and good_mark.isChecked():
            poison += 10 + 50
            hp += 10 + 50
            final += (10 + 50) + (10 + 50)
        if biologi and good_mark.isChecked():
            hp += 10 + 50
            sheld += 10 + 50
            final += (10 + 50) + (10 + 50)
        if istoria and good_mark.isChecked():
            world_edu += 10 + 50
            talking += 10 + 50
            final += (10 + 50) + (10 + 50)
        if obshestvo and good_mark.isChecked():
            hp += 10 + 50
            brain += 10 + 50
            world_edu += 10 + 50
            talking += 10 + 50
            final += (10 + 50) + (10 + 50) + (10 + 50) + (10 + 50)
        if fisic and good_mark.isChecked():
            brain += 15 + 50
            final += 15 + 50
        if python_cool and good_mark.isChecked():
            sheld += 25 + 50
            brain += 10 + 50
            final += (25 + 50) + (10 + 50)
        if fabric and good_mark.isChecked():
            talking += 40 + 50
            final += 40 + 50
        if obege and good_mark.isChecked():
            world_edu += 10 + 50
            sheld += 10 + 50
            hp += 10 + 50
            final += (10 + 50) + (10 + 50) + (10 + 50)

        # КЛАССНАЯ ПАРАША
        if russian and bad_mark.isChecked():
            talking -= 30
            world_edu -= 15
            final -= 30 + 15
        if litra and bad_mark.isChecked():
            brain -= 15
            talking -= 10
            world_edu -= 10
            final -= 15 + 10 + 10
        if matimatik and bad_mark.isChecked():
            brain -= 10
            final -= 10
        if geografi and bad_mark.isChecked():
            brain -= 10
            world_edu -= 10
            final -= 10 + 10
        if himic and bad_mark.isChecked():
            poison -= 10
            hp -= 10
            final -= 10 + 10
        if biologi and bad_mark.isChecked():
            hp -= 10
            sheld -= 10
            final -= 10 + 10
        if istoria and bad_mark.isChecked():
            world_edu -= 10
            talking -= 10
            final -= 10 + 10
        if obshestvo and bad_mark.isChecked():
            hp -= 10
            brain -= 10
            world_edu -= 10
            talking -= 10
            final -= 10 + 10 + 10 + 10
        if fisic and bad_mark.isChecked():
            brain -= 15
            final -= 15
        if python_cool and bad_mark.isChecked():
            sheld -= 15
            brain -= 10
            final -= 15 + 10
        if fabric and bad_mark.isChecked():
            talking -= 20
            final -= 20
        if obege and bad_mark.isChecked():
            world_edu -= 10
            sheld -= 10
            hp -= 10
            final -= 10 + 10 + 10
        
    
    if ex:
        if russian and well_mark.isChecked():
            talking += 70 + 130
            world_edu += 50 + 130
            final += (70 + 130) + (50 + 130)
        if litra and well_mark.isChecked():
            brain += 45 + 130
            talking += 25 + 130
            world_edu += 25 + 130
            final += (45 + 130) + (25 + 130) + (25 + 130)
        if matimatik and well_mark.isChecked():
            brain += 20 + 130
            final += 20 + 130
        if geografi and well_mark.isChecked():
            brain += 20 + 130
            world_edu += 25 + 130
            final += (20 + 130) + (25 + 130)
        if himic and well_mark.isChecked():
            poison += 25 + 130
            hp += 25 + 130
            final += (25 + 130) + (25 + 130)
        if biologi and well_mark.isChecked():
            hp += 25 + 130
            sheld += 25 + 130
            final += (25 + 130) + (25 + 130)
        if istoria and well_mark.isChecked():
            world_edu += 25 + 130
            talking += 25 + 130
            final += (25 + 130) + (25 + 130)
        if obshestvo and well_mark.isChecked():
            hp += 20 + 130
            brain += 25 + 130
            world_edu += 25 + 130
            talking += 20 + 130
            final += (20 + 130) + (25 + 130) + (25 + 130) + (20 + 130)
        if fisic and well_mark.isChecked():
            brain += 30 + 130
            final += 30 + 130
        if python_cool and well_mark.isChecked():
            sheld += 40 + 130
            brain += 20 + 130
            final += (40 + 130) + (20 + 130)
        if fabric and well_mark.isChecked():
            talking += 55 + 130
            final += 55 + 130
        if obege and well_mark.isChecked():
            world_edu += 20 + 130
            sheld += 25 + 130
            hp += 25 + 130
            final += (20 + 130) + (25 + 130) + (25 + 130)

        # КЛАССНАЯ ПЯТЁРКА
        if russian and best_mark.isChecked():
            talking += 85 + 130
            world_edu += 75 + 130
            final += (85 + 130) + (75 + 130)
        if litra and best_mark.isChecked():
            brain += 70 + 130
            talking += 50 + 130
            world_edu += 50 + 130
            final += (70 + 130) + (50 + 130) + (50 + 130)
        if matimatik and best_mark.isChecked():
            brain += 45 + 130
            final += 45 + 130
        if geografi and best_mark.isChecked():
            brain += 45 + 130
            world_edu += 50 + 130
            final += (45 + 130) + (50 + 130)
        if himic and best_mark.isChecked():
            poison += 50 + 130
            hp += 50 + 130
            final += (50 + 130) + (50 + 130)
        if biologi and best_mark.isChecked():
            hp += 50 + 130
            sheld += 50 + 130
            final += (50 + 130) + (50 + 130)
        if istoria and best_mark.isChecked():
            world_edu += 50 + 130
            talking += 50 + 130
            final += (50 + 130) + (50 + 130)
        if obshestvo and best_mark.isChecked():
            hp += 45 + 130
            brain += 50 + 130
            world_edu += 50 + 130
            talking += 45 + 130
            final += (45 + 130) + (50 + 130) + (50 + 130) + (45 + 130)
        if fisic and best_mark.isChecked():
            brain += 55 + 130
            final += 55 + 130
        if python_cool and best_mark.isChecked():
            sheld += 65 + 130
            brain += 45 + 130
            final += (65 + 130) + (45 + 130)
        if fabric and best_mark.isChecked():
            talking += 80 + 130
            final += 80 + 130
        if obege and best_mark.isChecked():
            world_edu += 45 + 130
            sheld += 50 + 130
            hp += 50 + 130
            final += (45 + 130) + (50 + 130) + (50 + 130)

        # КЛАССНАЯ ТРОЙКА
        if russian and good_mark.isChecked():
            talking += 55 + 130
            world_edu += 35 + 130
            final += (55 + 130) + (35 + 130)
        if litra and good_mark.isChecked():
            brain += 30 + 130
            talking += 10 + 130
            world_edu += 10 + 130
            final += (30 + 130) + (10 + 130) + (10 + 130)
        if matimatik and good_mark.isChecked():
            brain += 10 + 130
            final += 10 + 130
        if geografi and good_mark.isChecked():
            brain += 10 + 130
            world_edu += 10 + 130
            final += (10 + 130) + (10 + 130)
        if himic and good_mark.isChecked():
            poison += 10 + 130
            hp += 10 + 130
            final += (10 + 130) + (10 + 130)
        if biologi and good_mark.isChecked():
            hp += 10 + 130
            sheld += 10 + 130
            final += (10 + 130) + (10 + 130)
        if istoria and good_mark.isChecked():
            world_edu += 10 + 130
            talking += 10 + 130
            final += (10 + 130) + (10 + 130)
        if obshestvo and good_mark.isChecked():
            hp += 10 + 130
            brain += 10 + 130
            world_edu += 10 + 130
            talking += 10 + 130
            final += (10 + 130) + (10 + 130) + (10 + 130) + (10 + 130)
        if fisic and good_mark.isChecked():
            brain += 15 + 130
            final += 15 + 130
        if python_cool and good_mark.isChecked():
            sheld += 25 + 130
            brain += 10 + 130
            final += (25 + 130) + (10 + 130)
        if fabric and good_mark.isChecked():
            talking += 40 + 130
            final += 40 + 130
        if obege and good_mark.isChecked():
            world_edu += 10 + 130
            sheld += 10 + 130
            hp += 10 + 130
            final += (10 + 130) + (10 + 130) + (10 + 130)

        # КЛАССНАЯ ПАРАША
        if russian and bad_mark.isChecked():
            talking -= 30
            world_edu -= 15
            final -= 30 + 15
        if litra and bad_mark.isChecked():
            brain -= 15
            talking -= 10
            world_edu -= 10
            final -= 15 + 10 + 10
        if matimatik and bad_mark.isChecked():
            brain -= 10
            final -= 10
        if geografi and bad_mark.isChecked():
            brain -= 10
            world_edu -= 10
            final -= 10 + 10
        if himic and bad_mark.isChecked():
            poison -= 10
            hp -= 10
            final -= 10 + 10
        if biologi and bad_mark.isChecked():
            hp -= 10
            sheld -= 10
            final -= 10 + 10
        if istoria and bad_mark.isChecked():
            world_edu -= 10
            talking -= 10
            final -= 10 + 10
        if obshestvo and bad_mark.isChecked():
            hp -= 10
            brain -= 10
            world_edu -= 10
            talking -= 10
            final -= 10 + 10 + 10 + 10
        if fisic and bad_mark.isChecked():
            brain -= 15
            final -= 15
        if python_cool and bad_mark.isChecked():
            sheld -= 15
            brain -= 10
            final -= 15 + 10
        if fabric and bad_mark.isChecked():
            talking -= 20
            final -= 20
        if obege and bad_mark.isChecked():
            world_edu -= 10
            sheld -= 10
            hp -= 10
            final -= 10 + 10 + 10
    
    if best_mark.isChecked():
        loadImage_hape()
    if well_mark.isChecked():
        loadImage_well()
    if good_mark.isChecked():
        loadImage_gret()
    if bad_mark.isChecked():
        loadImage_bad()
    infourok.setText(f'Ваша статистика:\nУровень: {lvl}\n\nЗдоровье: {hp}\nЗащита: {sheld}\nРазум: {brain}\nКрасноречие: {talking}\nОбществознание: {world_edu}\nЗельеварение: {poison}\n\n\nВсего очков: {final}')

def deanon():
    hide_main()
    infourok.show()
    wasd.show()
    H2_Line.addWidget(infourok)
    V2_Line.addWidget(wasd)
    loadImage_read()
    
        

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
    
    # print(name)

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

wasd = QPushButton('Вернуться в меню')

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

type_work = QLabel('Какая именно работа?')

klass_work = QRadioButton('Классная работа')
sam_work = QRadioButton('Самостоятельная работа')
check_work = QRadioButton('Проверочная работа')
ctrl_work = QRadioButton('Контрольная работа')
exam = QRadioButton('Экзамен')
lesson = QPushButton('Далее')

subject = QLabel('По какому предмету?')

russian_bottom = QRadioButton('Русский')
literatur_bottom = QRadioButton('Литра')
manth_bottom = QRadioButton('Математика (алгебра/геометрия)')
chemist_bottom = QRadioButton('Химия')
bio_bottom = QRadioButton('Биология')
history_bottom = QRadioButton('История')
piple_bottom = QRadioButton('Обществознание')
geo_bottom = QRadioButton('География')
phisics_bottom = QRadioButton('Физика')
informatik_bottom = QRadioButton('Информатика')
eng_bottom = QRadioButton('Английский')
obg_bottom = QRadioButton('ОБЖ')
btn_mark = QPushButton('Далее')

what_mark = QLabel('На какую оценку?')

best_mark = QRadioButton('5')
well_mark = QRadioButton('4')
good_mark = QRadioButton('3')
bad_mark = QRadioButton('2')

bottom_final = QPushButton('Закончить')

now = QLabel(f"За домашку вы получили: {final} очков!!!")
show_lvl = QLabel(f"Ваш уровень: {lvl}")

kys = QPushButton('Вернуться')

infourok = QLabel(f'Ваша статистика:\nУровень: {lvl}\n\nЗдоровье: {hp}\nЗащита: {sheld}\nРазум: {brain}\nКрасноречие: {talking}\nОбществознание: {world_edu}\nЗельеварение: {poison}\n\n\nВсего очков: {final}')

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
works.clicked.connect(work)
bottom_final.clicked.connect(score_mark)
kys.clicked.connect(kys_back)
info.clicked.connect(deanon)
wasd.clicked.connect(popa)


lesson.clicked.connect(choose)

btn_mark.clicked.connect(marks)


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
type_work.setFont(font)
subject.setFont(font)
what_mark.setFont(font)
best_mark.setFont(font)
well_mark.setFont(font)
good_mark.setFont(font)
bad_mark.setFont(font)
infourok.setFont(font)

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
