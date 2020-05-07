#!usr/bin/env python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# File Name: cypuzzle
# Author:    fan20200225
# Date:      2020/3/21 0021
# -----------------------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMouseEvent
from PyQt5.QtWidgets import QWidget, QMessageBox
from PIL import Image
import time
import random


class CyPuzzle(QWidget):
    """超越拼图"""
    def __init__(self, scale):
        super(CyPuzzle, self).__init__()
        self.scale = scale
        self.resize(*self.scale)
        self.setFixedSize(*self.scale)
        self.setWindowTitle("超越拼图")

        # 创建一个标签作为大图的载体
        # self.lB = QtWidgets.QLabel()
        # self.lB.resize(*self.scale)
        # self.lB.move(0, 0)
        # self.lB.setText("lBbbbbbbbbbbbbbbbbbbbbbbbbnnnnnnnnnnnnnnnnnnnnnnnnb")

        # self.lablayout = QtWidgets.QVBoxLayout()
        # self.lablayout.addWidget(self.lB)
        # self.setLayout(self.lablayout)

        # self.pB1 = QtWidgets.QPushButton(self)
        # self.pB1.setText("pB1")
        # self.pB1.setGeometry(0, 0, 100, 100)
        # self.pB2 = QtWidgets.QPushButton(self)
        # self.pB2.setText("pB2")
        # self.pB2.setGeometry(200, 0, 100, 100)
        self.was_block_clicked = False  # 标记是否有方块被选中
        self.temp_block = None
        self.blockA_clicked = False
        self.blockB_clicked = False
        self.blockA = None
        self.blockB = None

        self.orginalimagepath = None
        self.image = None  # 拼图照片,PIL.Image对象
        self.howmanyblocks = 1  # 拼图难度（分成多少块，默认是1）
        self.blocks = []
        self.block_objnames = []
        self.temp_blocks = []
        self.block_images = []

    def mouseReleaseEvent(self, QMouseEvent):
        """前后分别点击的拼块进行对调，完成一次拼图动作"""
        pos = QMouseEvent.pos()
        for block in self.blocks:
            if block.geometry().contains(pos):
                self.swich_block2(block)
                print(pos)
        if self.blockA_clicked is True and self.blockB_clicked is True:
            # 交换时重复触发(此分支放到方法switch_block2方法下时，出现blockB被重复选中问题)
            self.blockA.setStyleSheet("border:1px solid #96c2f1;background:#eff7ff;")
            x = self.blockA.x()
            y = self.blockA.y()
            objname = self.blockA.objectName()
            self.blockA.move(self.blockB.x(), self.blockB.y())
            self.blockA.setObjectName(self.blockB.objectName())
            self.blockB.move(x, y)
            self.blockB.setObjectName(objname)
            self.blockA_clicked = False
            self.blockB_clicked = False
            self.blockA = None
            self.blockB = None
            # print(self.block_objnames)
            # print([tempblock.objectName() for tempblock in self.temp_blocks])
            if self.block_objnames == [tempblock.objectName() for tempblock in self.temp_blocks]:
                self.pop_message("恭喜你！完美通关！")

    def select_photo(self, originalimagepath):
        """选择图片"""
        self.orginalimagepath = originalimagepath
        self.image = self.init_image(Image.open(self.orginalimagepath), self.scale)
        self.image.save("ycy_widget.png", "png")

        # # 将图片构造成qimage并设置为label图片
        # image = self.image.convert("RGBA")
        # data = image.tobytes("raw", "RGBA")
        # qimg = QtGui.QImage(data, *self.scale, QtGui.QImage.Format_RGBA8888)
        #
        # # 预览图片
        # palette = QtGui.QPalette()
        # pixmap = QtGui.QPixmap.fromImage(qimg)
        # palette.setBrush(self.backgroundRole(), QtGui.QBrush(pixmap))
        # self.setPalette(palette)
        pb = QtWidgets.QLabel(self)

        pb.resize(*self.scale)
        # self.stick_image2(pb, self.image)

        # self.stick_image(self, self.image)
        # pixmap = QtGui.QPixmap(self.originalimagepath)  # 另一种方式
        # self.setPixmap(pixmap)

    def init_image(self, pilimage, scale):
        """按照scale给定的大小比例裁剪并缩放图片"""
        original_img = pilimage
        x, y = original_img.size
        to_x = scale[0]
        to_y = scale[1]
        if x / y > to_x / to_y:
            new_y = y
            new_x = to_x * y / to_y
            img = original_img.crop((int(x / 2 - new_x / 2), 0, int(x / 2 + new_x / 2), new_y))
            img = img.resize((to_x, to_y), Image.ANTIALIAS)
        else:
            new_x = x
            new_y = to_y * x / to_x
            img = original_img.crop((0, int(y / 2 - new_y / 2), new_x, int(y / 2 + new_y / 2)))
            img = img.resize((to_x, to_y), Image.ANTIALIAS)
        return img


    def layout_blocks(self, howmanyblocks: int):
        """"布局拼块"""
        self.howmanyblocks = howmanyblocks
        BLOCK_SCALE = {6: (2, 3), 12: (3, 4), 20: (4, 5), 24: (4, 6), 40: (5, 8)}
        ncol, nrow = BLOCK_SCALE[self.howmanyblocks]
        x, y = self.image.size
        block_x = x // ncol
        block_y = y // nrow
        for i in range(nrow):
            for j in range(ncol):
                pB = QtWidgets.QLabel(self)
                pB.setStyleSheet("border:1px solid #96c2f1;background:#eff7ff;")
                pB.setObjectName("pB_{}{}".format(i, j))
                pB.setGeometry(j*block_x, i*block_y, block_x, block_y)
                img = self.image.crop((j*block_x, i*block_y, j*block_x+block_x, i*block_y+block_y))
                self.blocks.append(pB)
                self.block_images.append(img)
                self.block_objnames.append(pB.objectName())  # 保存原始的block排列顺序
                # img.save("pB_{}{}.png".format(i, j), "png")
                print("=================== pB_{}{} ===================".format(i, j))
                print(j*block_x, i*block_y, block_x, block_y)
                print(j*block_x, i*block_y, j*block_x+block_x, i*block_y+block_y)

        blocks = []
        n = len(self.blocks)
        indexlist = list(range(n))
        random.shuffle(indexlist)

        for i in range(n):
            self.temp_blocks.append(self.blocks[indexlist[i]])
        # print(self.blocks)
        # print(self.temp_blocks)
        for block, img in zip(self.temp_blocks, self.block_images):
            self.stick_image2(block, img)
            time.sleep(0.1)

    # def stick_image(self, widget, image):
    #     """给主窗口或拼块贴图"""
    #     # 将图片构造成qimage并设置为label图片
    #     image = image.convert("RGBA")
    #     data = image.tobytes("raw", "RGBA")
    #     qimg = QtGui.QImage(data, *image.size, QtGui.QImage.Format_RGBA8888)
    #
    #     # 预览图片
    #     palette = QtGui.QPalette()
    #     pixmap = QtGui.QPixmap.fromImage(qimg)
    #     palette.setBrush(widget.backgroundRole(), QtGui.QBrush(pixmap))
    #     widget.setPalette(palette)

    def stick_image2(self, widget, image):
        """给主窗口或拼块贴图"""
        # 将图片构造成qimage并设置为label图片
        image = image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")
        qimg = QtGui.QImage(data, *image.size, QtGui.QImage.Format_RGBA8888)

        # 预览图片
        pixmap = QtGui.QPixmap.fromImage(qimg)
        widget.setPixmap(pixmap)

    def start_puzzle(self):
        """开始拼图"""
        pass

    # def swich_block(self, block):
    #     """
    #     第一块被选中
    #     第二块被点击，交换两个方块位置, 之后复位方块状态为未选中
    #     """
    #     print(block.text())
    #     if not self.was_block_clicked:
    #         self.was_block_clicked = True
    #         self.temp_block = block
    #         self.temp_block.setStyleSheet("border:1px solid #ffcc00;background:#fffff7;")
    #         print("1")
    #     else:
    #         self.temp_block.setStyleSheet("border:1px solid #96c2f1;background:#eff7ff;")
    #         x = self.temp_block.x()
    #         y = self.temp_block.y()
    #
    #         # 交换时重复触发
    #         self.temp_block.move(block.x(), block.y())
    #         block.move(x, y)
    #         self.temp_block = None
    #         self.was_block_clicked = False
    #
    #         print("2")

    def swich_block2(self, block):
        """
        第一块被选中
        第二块被点击，交换两个方块位置, 之后复位方块状态为未选中
        """
        if self.blockA_clicked is False and self.blockB_clicked is False:
            self.blockA = block
            self.blockA_clicked = True
            self.blockA.setStyleSheet("border:1px solid #ffcc00;background:#fffff7;")
            print("1")
        elif self.blockA_clicked is True and self.blockB_clicked is False:
            self.blockB = block
            self.blockB_clicked = True
            print("2")
        else:
            pass

    def pop_message(self, messages):
        msgbox = QMessageBox(self)
        msgbox.information(
            self,
            "提示",
            messages,
            QMessageBox.Yes | QMessageBox.No)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    scr_scale = (450, 800)
    cyp = CyPuzzle(scr_scale)
    cyp.select_photo("ycy.jpg")
    cyp.layout_blocks(40)
    cyp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    #
    # def open_photo(scale):
    #     big_img = Image.open("ycy.jpg")
    #     x, y = big_img.size
    #     to_x = scale[0]
    #     to_y = scale[1]
    #     if x/y > to_x/to_y:
    #         new_y = y
    #         new_x = to_x*y/to_y
    #         img = big_img.crop((int(x/2-new_x/2), 0, int(x/2+new_x/2), new_y))
    #         img = img.resize((to_x, to_y), Image.ANTIALIAS)
    #     else:
    #         new_x = x
    #         new_y = to_y * x / to_x
    #         img = big_img.crop(0, int(y/2 - new_y/2), new_x, int(y/2 + new_y/2))
    #         img = img.resize((to_x, to_y), Image.ANTIALIAS)
    #     img.save('ycy_temp.png', 'png')
    # open_photo((450, 800))
