from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont

app = QApplication([])
win = QWidget()

# win.move(100,200)
# win.setFixedSize(150, 300)
win.setGeometry(100,200,450,200)
win.setWindowTitle("FIRST APPLICATION")
win.setWindowIcon(QIcon("C:\\Users\\99893\\Desktop\\python_new\\pyqt5\\web.png"))
win.setStyleSheet("background-color:Lightgreen")




lbl = QLabel("salom",win)
# lbl.move(150, 0)
# lbl.setText("Arsenal is champion")
# lbl.setFont(QFont("Times", 20))
lbl.setStyleSheet("""background-color:cyan;
                     color:red;
                     font-size:30px""")


ism=input("Ism kiriting")
familya = input("Familya kiriting")
yosh=input("yosh kiriting")
 
edit = QLineEdit(win)
edit.move(150, 100)
edit.setStyleSheet("background-color: purple; color:white")


def ism1():
    
    lbl.setText(ism)
    edit.clear()

def familya1():
    
    lbl.setText(familya)
    edit.clear()
    
def yosh1():
    
    lbl.setText(yosh)
    edit.clear()
    
    

btn = QPushButton("ism", win)
btn.move(150,50)
btn.clicked.connect(ism1)

btn1 = QPushButton("familya", win)
btn1.move(150,100)
btn1.clicked.connect(familya1)

btn2 = QPushButton("yosh", win)
btn2.move(150,150)
btn2.clicked.connect(yosh1)

win.show()
app.exec_()

