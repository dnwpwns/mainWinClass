from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog, QApplication
from PyQt6 import uic
import csv

Form, Window = uic.loadUiType("res/fbDialog.ui")

class myWindow:
    def __init__(self):
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

        # Connect signals to slots
        self.form.btnSubmit.clicked.connect(self.save_to_csv)
        self.form.btnSearch.clicked.connect(self.fine_from_csv)
        self.form.btnAddPhoto.clicked.connect(self.add_photo)

    def save_to_csv(self):
        text1 = self.form.lineEdit.text() if self.form.lineEdit.text() else ""
        text2 = self.form.lineEdit_2.text() if self.form.lineEdit_2.text() else ""
        text3 = self.form.lineEdit_3.text() if self.form.lineEdit_3.text() else ""
        with open("add.txt", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([text1, text2, text3])

    def fine_from_csv(self):
        self.form.lineEdit.clear()
        self.form.lineEdit_2.clear()
        self.form.lineEdit_3.clear()
        with open("add.txt", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    self.form.lineEdit.setText(row[0])
                    self.form.lineEdit_2.setText(row[1])
                    self.form.lineEdit_3.setText(row[2])
                    break

    def add_photo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            pixmap = QPixmap(file_path)
            self.form.lblPhoto.setPixmap(pixmap)
            self.form.lblPhoto.setScaledContents(True)
            self.form.lineEdit_3.setText(file_path)
    def lounch(self):
        self.window.show()
if __name__ == "__main__":
    app = QApplication([])
    mw = myWindow()
    mw.window.show()
    app.exec()