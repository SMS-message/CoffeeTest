from sys import argv, exit
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        res = cur.execute("""
                                SELECT *
                                  FROM coffee;
                                """)

        self.tableWidget.setColumnCount(7)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


def main() -> None:
    app = QApplication(argv)
    ex = MyWidget()
    ex.show()

    exit(app.exec())


if __name__ == '__main__':
    main()
