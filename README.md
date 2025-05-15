# mainWinClass

1. mainwindow 만들기 2.Class 단위로 만들기 3. 몇개의 Class로 만들어진 app

pyQTapp01.py
'''
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("dialog.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
'''

pyQTapp02와 pyQTapp03은 기능을 확장한 것들이다.

### pyQTapp04는 클래스로 만든 것이다.

### 그리고 최종적으로 app.py를 만들었다
이것은 mainwindow를 맨처음 실행 되는 것이다. 여기서 메뉴를 클릭했을 때
위의 pyQTapp04.py가 실행되는 것이다.
