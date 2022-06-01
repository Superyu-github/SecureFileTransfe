# -*- coding: utf-8 -*-

"""
Module implementing SeverPage.
"""
from Server import Sever

from Ui_SeverPage import Ui_MainWindow

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

class SeverPage(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SeverPage, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 窗口置顶，无边框，在任务栏不显示图标
        self.sever = Sever()


        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(":/ico/ico/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.setWindowIcon(icon)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        self.sever.connect()
        self.close()
        self.sever.server_listen()

    
    @pyqtSlot()
    def on_pushButton_init_clicked(self):
        """
        Slot documentation goes here.
        """
        self.sever.connect()
        self.close()
        self.sever.create_table()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = SeverPage()
    ui.show()
    sys.exit(app.exec_())
