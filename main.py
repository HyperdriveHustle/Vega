import os
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from talk_show import Client

"""
Vega Bootstrap

Vega: My first virtual companion


@date: 2023/4/26
@author: Yancy
"""

icon = os.path.join('img/icon.png')


def get_images(pics):
    pic_list = []
    for item in pics:
        img = QImage()
        img.load('img/'+item)
        pic_list.append(img)
    return pic_list


class Vega(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.action = None
        self.index = None
        self.left_click = False
        self.mouse_drag_pos = None

        # 托盘
        quit = QAction("退出", self, triggered=self.quit)
        quit.setIcon(QIcon(icon))
        showing = QAction("现身~", self, triggered=self.showing)
        showing.setIcon(QIcon(icon))

        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(quit)
        self.tray_icon_menu.addAction(showing)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icon))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

        # 配置 Vega
        # 活动窗口: 无边框 + 置顶 + 透明背景
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 无边框 + 窗口置顶
        self.setAttribute(Qt.WA_TranslucentBackground)  # 半透明背景
        self.setAutoFillBackground(True)  # 非自动填充
        self.repaint()
        #
        self.img = QLabel(self)
        self.action_dataset = []
        self.init_data()
        self.set_pic("vega1.png")
        self.resize(128, 128)
        self.show()
        self.runing = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.run_random_actions)
        self.timer.start(500)
        self.random_position()

    def init_data(self):
        imgs = get_images(["vega1b.png", "vega2b.png", "vega1b.png", "vega3b"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega11.png", "vega15.png", "vega16.png", "vega17.png", "vega16.png", "vega17.png", "vega16.png", "vega17.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega54.png", "vega55.png", "vega26.png", "vega27.png", "vega28.png", "vega29.png", "vega26.png", "vega27.png", "vega28.png", "vega29.png", "vega26.png", "vega27.png", "vega28.png", "vega29.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega31.png", "vega32.png", "vega31.png", "vega33.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega18.png", "vega19.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega34b.png", "vega35b.png", "vega34b.png", "vega36b.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega14.png", "vega14.png", "vega52.png", "vega13.png", "vega13.png", "vega13.png", "vega52.png", "vega14.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega42.png", "vega43.png", "vega44.png", "vega45.png", "vega46.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega1.png", "vega38.png", "vega39.png", "vega40.png", "vega41.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega25.png", "vega25.png", "vega53.png", "vega24.png", "vega24.png", "vega24.png", "vega53.png", "vega25.png"])
        self.action_dataset.append(imgs)
        imgs = get_images(["vega20.png", "vega21.png", "vega20.png", "vega21.png", "vega20.png"])
        self.action_dataset.append(imgs)

    def set_pic(self, pic):
        img = QImage()
        img.load('img/'+pic)
        self.img.setPixmap(QPixmap.fromImage(img))

    def run_random_actions(self):
        if not self.runing:
            self.action = random.randint(0, len(self.action_dataset)-1)
            self.index = 0
            self.runing = True
        imgs = self.action_dataset[self.action]
        if self.index >= len(imgs):
            self.index = 0
            self.runing = False
        self.img.setPixmap(QPixmap.fromImage(imgs[self.index]))
        self.index += 1

    def random_position(self):
        screen = QDesktopWidget().screenGeometry()
        vega_window = self.geometry()
        self.move((screen.width()-vega_window.width())*random.random(), (screen.height()-vega_window.height())*random.random())

    def quit(self):
        self.close()
        sys.exit()

    # 通过窗口透明度 显示/隐藏
    def showing(self):
        self.setWindowOpacity(1)

    # 鼠标左键按下时, 宠物将和鼠标位置绑定
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.left_click = True
        self.mouse_drag_pos = event.globalPos() - self.pos()
        event.accept()
        # 拖动时鼠标图形的设置
        self.setCursor(QCursor(Qt.OpenHandCursor))

    # 鼠标移动时调用，实现宠物随鼠标移动
    def mouseMoveEvent(self, event):
        # 如果鼠标左键按下，且处于绑定状态
        if Qt.LeftButton and self.left_click:
            # 宠物随鼠标进行移动
            self.move(event.globalPos() - self.mouse_drag_pos)
        event.accept()

    # 鼠标释放调用，取消绑定
    def mouseReleaseEvent(self, event):
        self.left_click = False
        # 鼠标图形设置为箭头
        self.setCursor(QCursor(Qt.ArrowCursor))

    def enterEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)  # 设置鼠标形状 Qt.ClosedHandCursor 非指向手

    # 右键点击交互
    def contextMenuEvent(self, event):
        # 定义菜单
        menu = QMenu(self)
        # 定义菜单项
        hide = menu.addAction("退下吧~")
        question_answer = menu.addAction("聊聊?")
        menu.addSeparator()
        # quitAction = menu.addAction("退出")

        # 使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action = menu.exec_(self.mapToGlobal(event.pos()))
        # if action == quitAction:
        #     qApp.quit()
        if action == hide:
            self.setWindowOpacity(0)
        if action == question_answer:
            self.client = Client()
            self.client.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = Vega()
    sys.exit(app.exec_())

