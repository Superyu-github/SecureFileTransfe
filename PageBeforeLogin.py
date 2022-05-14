# -*- coding: utf-8 -*-

"""
Module implementing PageBeforeLogin.
"""
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from Ui_PageBeforeLogin import Ui_MainWindow


class PageBeforeLogin(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(PageBeforeLogin, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 窗口置顶，无边框，在任务栏不显示图标

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
    def on_pushButton_return_s_clicked(self):
        """
        Slot documentation goes here.
        """
        self.stackedWidget.setCurrentIndex(0)
    
    @pyqtSlot()
    def on_pushButton_set_s_clicked(self):
        """
        Slot documentation goes here.
        """
        ip = self.lineEdit_ip_s
        port = self.lineEdit_port_s
        # TODO: 传入设置函数

    
    @pyqtSlot()
    def on_pushButton_register_l_clicked(self):
        """
        Slot documentation goes here.
        """
        self.stackedWidget.setCurrentIndex(1)
    
    @pyqtSlot()
    def on_pushButton_login_l_clicked(self):
        """
        Slot documentation goes here.
        """
        username = self.lineEdit_username_l.text()
        password = self.lineEdit_password_l.text()
        # TODO: 参数传入登录函数
    
    @pyqtSlot()
    def on_pushButton_set_l_clicked(self):
        """
        Slot documentation goes here.
        """
        self.stackedWidget.setCurrentIndex(2)
    
    @pyqtSlot()
    def on_pushButton_return_r_clicked(self):
        """
        Slot documentation goes here.
        """
        self.stackedWidget.setCurrentIndex(0)
    
    @pyqtSlot()
    def on_pushButton_register_r_clicked(self):
        """
        Slot documentation goes here.
        """
        username = self.lineEdit_username_r.text()
        password = self.lineEdit_password_r.text()
        rpassword = self.lineEdit_rpassword_r.text()
        # TODO: 传入注册函数



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = PageBeforeLogin()
    ui.show()
    sys.exit(app.exec_())
