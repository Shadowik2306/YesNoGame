import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidgetItem, QDialog, QMainWindow
from PyQt5.QtCore import Qt

from source.ui.main_Ui import *
from source.qt_alg import *


points = 0
IDK = None  # i dont know


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.label.hide()
        self.points.setText(f"Баллов: {points}")
        self.pushButton.clicked.connect(self.check_subj)

    def check_subj(self):
        global IDK
        if real_subj(self.subject_check.text()):
            IDK = self.subject_check.text()
            self.new_window = Game()
            self.new_window.show()
            self.close()
        else:
            if self.label.isVisible():
                IDK = True
                self.new_window = Game()
                self.new_window.show()
                self.close()
            self.label.setVisible(True)
            self.label.setText(" Возможно, предмет не существует в базе данных. Если уверены, нажмите еще раз")


class Game(QWidget, Ui_Form):
    def __init__(self):
        new_game()
        super(Game, self).__init__()
        self.setupUi(self)
        self.chooseQuest()
        self.pushButtonYes.clicked.connect(self.yes_button)
        self.pushButtonNo.clicked.connect(self.no_button)

    def chooseQuest(self):
        user_turn = question()
        if user_turn['is_question']:
            self.questLabel.setText(user_turn['text'])
        else:

            self.pushButtonYes.clicked.connect(self.result)
            self.pushButtonNo.clicked.connect(self.result)
            # self.result(user_turn['text'], user_turn['turns'])
            self.questLabel.setText("Это: " + user_turn['text'])

    def yes_button(self):
        ans_yes()
        self.chooseQuest()

    def no_button(self):
        ans_no()
        self.chooseQuest()

    def result(self):
        global points
        if self.sender().objectName() == 'pushButtonYes':
            points += 10 + (10 - turns) if turns > 10 else 10
        self.new_window = MyWindow()
        self.new_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    sys.exit(app.exec())