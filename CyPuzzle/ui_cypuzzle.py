# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cypuzzle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cyPuzzle(object):
    def setupUi(self, cyPuzzle):
        cyPuzzle.setObjectName("cyPuzzle")
        cyPuzzle.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(cyPuzzle)
        self.centralwidget.setObjectName("centralwidget")
        self.pb1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb1.setGeometry(QtCore.QRect(20, 10, 181, 151))
        self.pb1.setObjectName("pb1")
        self.pb2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb2.setGeometry(QtCore.QRect(220, 10, 181, 151))
        self.pb2.setObjectName("pb2")
        cyPuzzle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cyPuzzle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        cyPuzzle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cyPuzzle)
        self.statusbar.setObjectName("statusbar")
        cyPuzzle.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(cyPuzzle)
        QtCore.QMetaObject.connectSlotsByName(cyPuzzle)

    def retranslateUi(self, cyPuzzle):
        _translate = QtCore.QCoreApplication.translate
        cyPuzzle.setWindowTitle(_translate("cyPuzzle", "CY拼图"))
        self.pb1.setText(_translate("cyPuzzle", "PB1"))
        self.pb2.setText(_translate("cyPuzzle", "PB2"))
        self.menu.setTitle(_translate("cyPuzzle", "文件"))
        self.menu_2.setTitle(_translate("cyPuzzle", "选项"))
        self.menu_3.setTitle(_translate("cyPuzzle", "帮助"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cyPuzzle = QtWidgets.QMainWindow()
    ui = Ui_cyPuzzle()
    ui.setupUi(cyPuzzle)
    cyPuzzle.show()
    sys.exit(app.exec_())
