# -*- coding: utf-8 -*-

"""
Module implementing PageAfterLogein.
"""
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QFileDialog

from Ui_PageAfterLogin import Ui_MainWindow
from ClientOperate import Client

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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.client = Client()


    def update_transfer_table(self,checkList):

        total_index = 0
        for file_list in checkList:
            print(file_list)
            for file_index in range(len(file_list["fileName"])):
                fileName = file_list["fileName"][file_index]
                fileSize = file_list["fileSize"][file_index]
                self.tableWidget.setRowCount(total_index+10)
                self.tableWidget.setItem(total_index, 0, QTableWidgetItem(str(total_index+1)))
                self.tableWidget.setItem(total_index, 1, QTableWidgetItem(fileName))
                self.tableWidget.setItem(total_index, 2, QTableWidgetItem(str(fileSize)))
                self.tableWidget.setItem(total_index, 3, QTableWidgetItem(str(file_list["usrName"])))
                self.tableWidget.setItem(total_index, 4, QTableWidgetItem(str(file_list["permission"])))
                total_index += 1

    def change_pushButton_permission_state(self,permission):
        if permission == "public":
            self.pushButton_permission.setText("公有")
            self.pushButton_permission.setStyleSheet('''background-color: rgb(71, 141, 65);
                                                                color: rgb(255, 255, 255);
                                                                border-radius:4px''')
        elif permission == "private":
            self.pushButton_permission.setText("私有")
            self.pushButton_permission.setStyleSheet('''background-color: rgb(197, 68, 72);
                                                                color: rgb(255, 255, 255);
        	                                                    border-radius:4px;''')




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
                                                    color: rgb(248, 237, 83);
                                                    border-radius:0px;
                                                    background-color:rgba(0, 0, 0,0);                                
                                                    ''')
        self.pushButton_log.setStyleSheet('''QPushButton{	
                                                border-radius:0px;
                                                background-color:rgba(0, 0, 0,0);
                                                color: rgb(199, 151, 7);
                                                }
                                                QPushButton:pressed{	
                                                image: url(:/ico/ico/cutbutton.png);
                                                color: rgb(248, 237, 83);
                                                }  ''')
        self.pushButton_info.setStyleSheet('''QPushButton{	
                                                        border-radius:0px;
                                                        background-color:rgba(0, 0, 0,0);
                                                        color: rgb(199, 151, 7);
                                                        }
                                                        QPushButton:pressed{	
                                                        image: url(:/ico/ico/cutbutton.png);
                                                        color: rgb(248, 237, 83);
                                                        }  ''')
        check_list = self.client.check()
        self.update_transfer_table(check_list)
        self.change_pushButton_permission_state(self.client.permission)



    @pyqtSlot()
    def on_pushButton_log_clicked(self):
        """
        Slot documentation goes here.
        """
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_transfer.setStyleSheet('''QPushButton{	
                                                        border-radius:0px;
                                                        background-color:rgba(0, 0, 0,0);
                                                        color: rgb(199, 151, 7);
                                                        }
                                                        QPushButton:pressed{	
                                                        image: url(:/ico/ico/cutbutton.png);
                                                        color: rgb(248, 237, 83);
                                                        }  ''')
        self.pushButton_log.setStyleSheet('''image: url(:/ico/ico/cutbutton.png);
                                                            color: rgb(248, 237, 83);
                                                            border-radius:0px;
                                                            background-color:rgba(0, 0, 0,0);                                
                                                            ''')
        self.pushButton_info.setStyleSheet('''QPushButton{	
                                                                border-radius:0px;
                                                                background-color:rgba(0, 0, 0,0);
                                                                color: rgb(199, 151, 7);
                                                                }
                                                                QPushButton:pressed{	
                                                                image: url(:/ico/ico/cutbutton.png);
                                                                color: rgb(248, 237, 83);
                                                                }  ''')
        self.client.audit()
        f = open("./ClientCache/Serverlog.txt", "r", encoding="utf-8")
        log = f.read()
        f.close()
        self.textBrowser.setText(log)


    @pyqtSlot()
    def on_pushButton_info_clicked(self):
        """
        Slot documentation goes here.
        """
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_transfer.setStyleSheet('''QPushButton{	
                                                                border-radius:0px;
                                                                background-color:rgba(0, 0, 0,0);
                                                                color: rgb(199, 151, 7);
                                                                }
                                                                QPushButton:pressed{	
                                                                image: url(:/ico/ico/cutbutton.png);
                                                                color: rgb(248, 237, 83);
                                                                }  ''')
        self.pushButton_log.setStyleSheet('''QPushButton{	
                                                        border-radius:0px;
                                                        background-color:rgba(0, 0, 0,0);
                                                        color: rgb(199, 151, 7);
                                                        }
                                                        QPushButton:pressed{	
                                                        image: url(:/ico/ico/cutbutton.png);
                                                        color: rgb(248, 237, 83);
                                                        }  ''')
        self.pushButton_info.setStyleSheet('''image: url(:/ico/ico/cutbutton.png);
                                                            color: rgb(248, 237, 83);
                                                            border-radius:0px;
                                                            background-color:rgba(0, 0, 0,0);                                
                                                            ''')



    @pyqtSlot()
    def on_pushButton_upload_clicked(self):
        """
        Slot documentation goes here.
        """
        FileDialog = QFileDialog()
        filePath, _ = FileDialog.getOpenFileName(self, "Choose File", '.', "All Files(*)")

        self.client.upload(filePath,1)
        check_list = self.client.check()
        self.update_transfer_table(check_list)
        self.pushButton_upload.setText("上传成功")
        self.pushButton_upload.setStyleSheet('''QPushButton{	
                                                                                    background-color: rgb(14, 177, 68);
                                                                                    color: rgb(255, 255, 255);
                                                                                }
                                                                                QPushButton:pressed{	
                                                                                    padding-left:5px;
                                                                                    padding-top:5px;
                                                                                }''')





    @pyqtSlot()
    def on_pushButton_download_clicked(self):
        """
        Slot documentation goes here.
        """

        row = self.tableWidget.currentRow()
        filename = self.tableWidget.item(row,1).text()
        username = self.tableWidget.item(row,3).text()

        self.client.download(filename, username)
        self.pushButton_download.setText("下载成功")
        self.pushButton_download.setStyleSheet('''QPushButton{	
                                                                                            background-color: rgb(14, 177, 68);
                                                                                            color: rgb(255, 255, 255);
                                                                                        }
                                                                                        QPushButton:pressed{	
                                                                                            padding-left:5px;
                                                                                            padding-top:5px;
                                                                                        }''')

    
    @pyqtSlot()
    def on_pushButton_permission_clicked(self):
        """
        Slot documentation goes here.
        """
        self.client.permission = self.client.change()
        # print(self.client.permission)
        # self.change_pushButton_permission_state(permission)
        self.on_pushButton_transfer_clicked()
    
    @pyqtSlot()
    def on_centralWidget_destroyed(self):
        """
        Slot documentation goes here.
        """
        self.client.ssock.close()
    
    @pyqtSlot(QModelIndex)
    def on_tableWidget_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        self.pushButton_upload.setText("上传")
        self.pushButton_upload.setStyleSheet('''QPushButton{	
                                                background-color: rgb(207, 44, 24);
                                                color: rgb(255, 255, 255);
                                                }
                                                QPushButton:pressed{	
                                                    padding-left:5px;
                                                    padding-top:5px;
                                                }''')
        self.pushButton_download.setText("下载")
        self.pushButton_download.setStyleSheet('''QPushButton{	
                                                background-color: rgb(207, 44, 24);
                                                color: rgb(255, 255, 255);
                                                }
                                                QPushButton:pressed{	
                                                    padding-left:5px;
                                                    padding-top:5px;
                                                }''')









if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = PageAfterLogein()
    ui.show()
    sys.exit(app.exec_())
