# -*- coding: utf-8 -*-

"""
Module implementing PageBeforeLogin.
"""
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from PageAfterLogin import PageAfterLogein
from Ui_PageBeforeLogin import Ui_MainWindow

from ClientOperate import Client

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
        self.client = Client()

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
        self.pushButton_set_s.setText("设置")
        self.pushButton_set_s.setStyleSheet('''QPushButton{	                                                                
                                                                        background-color: rgb(223, 212, 63);
                                                                        color: rgb(0, 0, 0);
                                                                    }
                                                                    QPushButton:pressed{	
                                                                        padding-left:5px;
                                                                        padding-top:5px;
                                                                    }''')
    
    @pyqtSlot()
    def on_pushButton_set_s_clicked(self):
        """
        Slot documentation goes here.
        """
        self.client.ip = self.lineEdit_ip_s.text()
        self.client.port = self.lineEdit_port_s.text()
        self.pushButton_set_s.setText("设置成功")
        self.label_ip.setText(f"{self.client.ip}:{self.client.port}")
        self.pushButton_set_s.setStyleSheet('''QPushButton{	
                                                                            background-color: rgb(14, 177, 68);
                                                                            color: rgb(255, 255, 255);
                                                                        }
                                                                        QPushButton:pressed{	
                                                                            padding-left:5px;
                                                                            padding-top:5px;
                                                                        }''')


    
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
        state = self.client.login(username,password)

        if state :
            if state == "admin":
                PageAfterLogein.label_back.setStyleSheet("image: url(:/ico/ico/redpoint2.png);")
                PageAfterLogein.label_user.setText(self.client.username)
                PageAfterLogein.label_user_identity.setText("管理员")
                PageAfterLogein.label_user.setAlignment(QtCore.Qt.AlignHCenter)
                PageAfterLogein.label_user_identity.setAlignment(QtCore.Qt.AlignCenter)
                PageAfterLogein.verticalLayout_5.layout()
            else:
                PageAfterLogein.label_back.setStyleSheet("image: url(:/ico/ico/bluepoint2.png);")
                PageAfterLogein.label_user.setText(self.client.username)
                PageAfterLogein.label_user_identity.setText("普通用户")
                PageAfterLogein.label_user.setAlignment(QtCore.Qt.AlignHCenter)
                PageAfterLogein.label_user_identity.setAlignment(QtCore.Qt.AlignCenter)

            PageAfterLogein.show()
            self.close()

        else:
            self.pushButton_login_l.setText("登录失败")
            self.pushButton_login_l.setStyleSheet('''QPushButton{	
                                                                    background-color: rgb(207, 44, 24);
                                                                    color: rgb(255, 255, 255);
                                                                }
                                                                QPushButton:pressed{	
                                                                    padding-left:5px;
                                                                    padding-top:5px;
                                                                }''')


    
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
        self.pushButton_register_r.setText("注册")
        self.pushButton_register_r.setStyleSheet('''QPushButton{	                                                                
                                                                        background-color: rgb(223, 212, 63);
                                                                        color: rgb(0, 0, 0);
                                                                    }
                                                                    QPushButton:pressed{	
                                                                        padding-left:5px;
                                                                        padding-top:5px;
                                                                    }''')
    
    @pyqtSlot()
    def on_pushButton_register_r_clicked(self):
        """
        Slot documentation goes here.
        """
        username = self.lineEdit_username_r.text()
        password = self.lineEdit_password_r.text()
        rpassword = self.lineEdit_repassword_r.text()
        state = self.client.register(username,rpassword)
        if state:
            self.pushButton_register_r.setText("注册成功")
            self.pushButton_register_r.setStyleSheet('''QPushButton{	
                                                                    background-color: rgb(14, 177, 68);
                                                                    color: rgb(255, 255, 255);
                                                                }
                                                                QPushButton:pressed{	
                                                                    padding-left:5px;
                                                                    padding-top:5px;
                                                                }''')
        else:
            self.pushButton_register_r.setText("注册失败")
            self.pushButton_register_r.setStyleSheet('''QPushButton{	
                                                                                background-color: rgb(207, 44, 24);
                                                                                color: rgb(255, 255, 255);
                                                                            }
                                                                            QPushButton:pressed{	
                                                                                padding-left:5px;
                                                                                padding-top:5px;
                                                                            }''')

    
    @pyqtSlot(int, int)
    def on_lineEdit_username_r_cursorPositionChanged(self, p0, p1):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        @param p1 DESCRIPTION
        @type int
        """
        self.pushButton_register_r.setText("注册")
        self.pushButton_register_r.setStyleSheet('''QPushButton{	                                                                
                                                                background-color: rgb(223, 212, 63);
                                                                color: rgb(0, 0, 0);
                                                            }
                                                            QPushButton:pressed{	
                                                                padding-left:5px;
                                                                padding-top:5px;
                                                            }''')
    
    @pyqtSlot(int, int)
    def on_lineEdit_password_r_cursorPositionChanged(self, p0, p1):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        @param p1 DESCRIPTION
        @type int
        """
        self.pushButton_register_r.setText("注册")
        self.pushButton_register_r.setStyleSheet('''QPushButton{	                                                                
                                                                background-color: rgb(223, 212, 63);
                                                                color: rgb(0, 0, 0);
                                                            }
                                                            QPushButton:pressed{	
                                                                padding-left:5px;
                                                                padding-top:5px;
                                                            }''')
    
    @pyqtSlot(int, int)
    def on_lineEdit_repassword_r_cursorPositionChanged(self, p0, p1):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        @param p1 DESCRIPTION
        @type int
        """
        self.pushButton_register_r.setText("注册")
        self.pushButton_register_r.setStyleSheet('''QPushButton{	                                                                
                                                                background-color: rgb(223, 212, 63);
                                                                color: rgb(0, 0, 0);
                                                            }
                                                            QPushButton:pressed{	
                                                                padding-left:5px;
                                                                padding-top:5px;
                                                            }''')
    
    @pyqtSlot(int, int)
    def on_lineEdit_username_l_cursorPositionChanged(self, p0, p1):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        @param p1 DESCRIPTION
        @type int
        """
        self.pushButton_login_l.setText("登录")
        self.pushButton_login_l.setStyleSheet('''QPushButton{	                                                                
                                                                background-color: rgb(223, 212, 63);
                                                                color: rgb(0, 0, 0);
                                                            }
                                                            QPushButton:pressed{	
                                                                padding-left:5px;
                                                                padding-top:5px;
                                                            }''')

    
    @pyqtSlot(int, int)
    def on_lineEdit_password_l_cursorPositionChanged(self, p0, p1):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        @param p1 DESCRIPTION
        @type int
        """
        self.pushButton_login_l.setText("登录")
        self.pushButton_login_l.setStyleSheet('''QPushButton{	                                                                
                                                                background-color: rgb(223, 212, 63);
                                                                color: rgb(0, 0, 0);
                                                            }
                                                            QPushButton:pressed{	
                                                                padding-left:5px;
                                                                padding-top:5px;
                                                            }''')
    
    @pyqtSlot()
    def on_pushButton_connectLight_clicked(self):
        """
        Slot documentation goes here.
        """
        connect_sever()
    


def connect_sever():
    try:
        client = Client()

        client.connect_sever()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico/greenpoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PageBeforeLogin.pushButton_connectLight.setIcon(icon)
        PageBeforeLogin.label_ip.setText(f"{client.ip}:{client.port}")
        PageBeforeLogin.label_connect.setText("Connected")

        PageAfterLogein.client = client
        PageBeforeLogin.client = client
        return client

        #建立连接

    except:
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico/redpoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PageBeforeLogin.pushButton_connectLight.setIcon(icon)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    PageBeforeLogin = PageBeforeLogin()

    PageAfterLogein = PageAfterLogein()
    connect_sever()

    PageBeforeLogin.show()
    sys.exit(app.exec_())
