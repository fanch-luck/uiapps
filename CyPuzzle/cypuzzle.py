#!usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: cypuzzle
# Author:    fan20200225
# Date:      2020/3/21 0021
# -----------------------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QWidget
from PIL import Image


class CyPuzzle(QWidget):
    """超越拼图"""
    def __init__(self):
        super(CyPuzzle, self).__init__()
        self.resize(450, 800)
        self.lB = QtWidgets.QLabel()

        self.lB.resize(450, 800)
        self.lB.setText("lBbbbbbbbbbbbbbbbbbbbbbbbbnnnnnnnnnnnnnnnnnnnnnnnnb")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lB)
        self.setLayout(layout)
        # self.pB1 = QtWidgets.QPushButton(self)
        # self.pB1.setText("pB1")
        # self.pB1.setGeometry(0, 0, 100, 100)
        # self.pB2 = QtWidgets.QPushButton(self)
        # self.pB2.setText("pB2")
        # self.pB2.setGeometry(200, 0, 100, 100)
        self.was_block_clicked = False  # 标记是否有方块被选中
        self.temp_block = None

        self.photopath = "ycy.jpg"
        self.photo = None  # 拼图照片
        self.howmanyblocks = 1  # 拼图难度（分成多少块，默认是1）

        self.select_photo(self.photopath)

    def select_photo(self, photopath):
        """选择图片"""
        big_img = Image.open(photopath)
        x, y = big_img.size
        img = big_img.resize((450, int(450 * y / x)), Image.ANTIALIAS)
        qimg = img.toqimage()

        pixmap = QtGui.QPixmap("ycy.jpg")
        self.lB.setPixmap(pixmap)
        # palette = QtGui.QPalette()
        # palette.setBrush(self.backgroundRole(), QtGui.QBrush(pixmap))
        # self.setPalette(palette)


    def layout_blocks(self, howmanyblocks):
        """"布局拼块"""
        pass

    def map_blocks(self):
        """给拼块贴图"""
        pass

    def start_puzzle(self):
        """开始拼图"""
        pass

    def swich_block(self, block):
        """前后分别点击的拼块进行对调，完成一次拼图动作"""
        if not self.was_block_clicked:
            self.was_block_clicked = True
            self.temp_block = block
            print("1")
        else:
            x = self.temp_block.x()
            y = self.temp_block.y()
            self.temp_block.move(block.x(), block.y())
            block.move(x, y)
            self.was_block_clicked = False
            self.temp_block = None
            print("2")

    def click_block(self):
        """
        第一块被选中
        第二块被点击，交换两个方块位置, 之后复位方块状态为未选中
        """
        self.pB1.clicked.connect(lambda: self.swich_block(self.pB1))
        self.pB2.clicked.connect(lambda: self.swich_block(self.pB2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cyp = CyPuzzle()
    cyp.show()
    # cyp.click_block()
    sys.exit(app.exec_())
    # def open_photo():
    #     big_img = Image.open("ycy.png")
    #     x, y = big_img.size
    #     img = big_img.resize((450, int(450 * y / x)), Image.ANTIALIAS)
    #     img.save('ycy-2.png', 'png')
    # open_photo()
