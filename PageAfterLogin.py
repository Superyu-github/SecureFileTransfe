# -*- coding: utf-8 -*-

"""
Module implementing PageAfterLogein.
"""
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem

from Ui_PageAfterLogin import Ui_MainWindow


class PageAfterLogein(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(PageAfterLogein, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)  # 窗口置顶，无边框，在任务栏不显示图标
        self.tableWidget.setColumnCount(3)
        # self.tableWidget.setHorizontalHeaderLabels(['文件名','用户','文件大小'])
        # QTableWidget.resizeColumnsToContents(self.tableWidget)
        # QTableWidget.resizeRowsToContents(self.tableWidget)
        item = QTableWidgetItem("11111111111")
        self.tableWidget.setItem(1,1,item)


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
    def on_pushButton_transfer_clicked(self):
        """
        Slot documentation goes here.
        """
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_transfer.setStyleSheet('''image: url(:/ico/ico/cutbutton.png);
                                                border-radius:30px;
                                                color: rgb(248, 237, 83);''')
        # TODO: 函数对接

    
    @pyqtSlot()
    def on_pushButton_log_clicked(self):
        """
        Slot documentation goes here.
        """
        self.stackedWidget.setCurrentIndex(1)
        # TODO: 函数对接

    
    @pyqtSlot()
    def on_pushButton_info_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_upload_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_download_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = PageAfterLogein()
    ui.show()
    sys.exit(app.exec_())
