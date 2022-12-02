import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class CCC(QWidget):
    def __init__(self):
        super().__init__()

        self.number_of_cookies = 0
        self.cursor_cost = 10
        self.cursor_number = 0
        self.grandma_cost = 100
        self.grandma_number = 0
        self.factory_cost = 10000
        self.factory_number = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_all)
        self.timer.start(1000)

        self.setWindowTitle("Cookie Clicker Clone")

        self.button_for_cookie = QPushButton(f"Click for cookies! You have {self.number_of_cookies} cookies.")
        self.button_for_cursor = QPushButton(
            f"Click to buy cursor for {self.cursor_cost} cookies. You have {self.cursor_number} cursors.")
        self.button_for_grandma = QPushButton(
            f"Click to buy grandma for {self.grandma_cost} cookies. You have {self.grandma_number} grandmas.")
        self.button_for_factory = QPushButton(
            f"Click to buy factory for {self.factory_cost} cookies. You have {self.factory_number} factories.")

        self.button_for_cookie.released.connect(self.add_cookie)
        self.button_for_cursor.released.connect(self.add_cursor)
        self.button_for_grandma.released.connect(self.add_grandma)
        self.button_for_factory.released.connect(self.add_factory)

        self.layout = QGridLayout()
        self.layout.addWidget(self.button_for_cookie, 0, 0)
        self.layout.addWidget(self.button_for_cursor, 0, 1)
        self.layout.addWidget(self.button_for_grandma, 1, 0)
        self.layout.addWidget(self.button_for_factory, 1, 1)
        self.setLayout(self.layout)

    def update_all(self):
        self.update_labels()
        self.number_of_cookies += self.cursor_number + self.grandma_number * 10 + self.factory_number * 1000
        self.timer.start(1000)

    def update_labels(self):
        self.button_for_cookie.setText(f"Click for cookies! You have {self.number_of_cookies} cookies.")
        self.button_for_cursor.setText(
            f"Click to buy cursor for {self.cursor_cost} cookies. You have {self.cursor_number} cursors.")
        self.button_for_grandma.setText(
            f"Click to buy grandma for {self.grandma_cost} cookies. You have {self.grandma_number} grandmas.")
        self.button_for_factory.setText(
            f"Click to buy factory for {self.factory_cost} cookies. You have {self.factory_number} factories.")

    def add_cookie(self):
        self.number_of_cookies += 1
        self.update_labels()

    def add_cursor(self):
        if self.number_of_cookies >= self.cursor_cost:
            self.cursor_number += 1
            self.number_of_cookies -= self.cursor_cost
            self.cursor_cost += 1
            self.update_labels()

    def add_grandma(self):
        if self.number_of_cookies >= self.grandma_cost:
            self.grandma_number += 1
            self.number_of_cookies -= self.grandma_cost
            self.grandma_cost += 10
            self.update_labels()

    def add_factory(self):
        if self.number_of_cookies >= self.factory_cost:
            self.factory_number += 1
            self.number_of_cookies -= self.factory_cost
            self.factory_cost += 1000
            self.update_labels()


app = QApplication(sys.argv)
window = CCC()
window.show()
app.exec()
