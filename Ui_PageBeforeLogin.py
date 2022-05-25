# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'J:\Projects\FileTransferSystem\SecureFileTransfe\PageBeforeLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 330)
        MainWindow.setMinimumSize(QtCore.QSize(430, 330))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(430, 330))
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_top = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setStyleSheet("background-color: rgb(252, 236, 12);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.frame_6 = QtWidgets.QFrame(self.frame_top)
        self.frame_6.setGeometry(QtCore.QRect(330, -10, 71, 41))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"background-color: rgba(255, 255, 255,0);\n"
"boder:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}")
        self.pushButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"background-color: rgba(255, 255, 255,0);\n"
"boder:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}")
        self.pushButton_8.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/ico/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout.addWidget(self.frame_top)
        self.frame_content = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(92)
        sizePolicy.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy)
        self.frame_content.setStyleSheet("background-color: rgb(19, 99, 119);")
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_content)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(30)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.label = QtWidgets.QLabel(self.page_login)
        self.label.setGeometry(QtCore.QRect(20, -10, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(248, 237, 83);")
        self.label.setObjectName("label")
        self.lineEdit_username_l = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_username_l.setGeometry(QtCore.QRect(100, 60, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setUnderline(False)
        self.lineEdit_username_l.setFont(font)
        self.lineEdit_username_l.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit_username_l.setPlaceholderText("")
        self.lineEdit_username_l.setObjectName("lineEdit_username_l")
        self.lineEdit_password_l = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_password_l.setGeometry(QtCore.QRect(100, 110, 221, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.lineEdit_password_l.setFont(font)
        self.lineEdit_password_l.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit_password_l.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_l.setPlaceholderText("")
        self.lineEdit_password_l.setObjectName("lineEdit_password_l")
        self.label_4 = QtWidgets.QLabel(self.page_login)
        self.label_4.setGeometry(QtCore.QRect(50, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_login)
        self.label_5.setGeometry(QtCore.QRect(50, 110, 51, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label_5.setObjectName("label_5")
        self.pushButton_register_l = QtWidgets.QPushButton(self.page_login)
        self.pushButton_register_l.setGeometry(QtCore.QRect(210, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_register_l.setFont(font)
        self.pushButton_register_l.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(223, 212, 63);\n"
"}\n"
"QPushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_register_l.setObjectName("pushButton_register_l")
        self.pushButton_login_l = QtWidgets.QPushButton(self.page_login)
        self.pushButton_login_l.setGeometry(QtCore.QRect(50, 170, 111, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_login_l.setFont(font)
        self.pushButton_login_l.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(223, 212, 63);\n"
"}\n"
"QPushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_login_l.setObjectName("pushButton_login_l")
        self.frame_left = QtWidgets.QFrame(self.page_login)
        self.frame_left.setGeometry(QtCore.QRect(10, 220, 181, 41))
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_left)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_set_l = QtWidgets.QPushButton(self.frame_left)
        self.pushButton_set_l.setStyleSheet("QPushButton{\n"
"background-color: rgba(255, 255, 255,0);\n"
"boder:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}\n"
"")
        self.pushButton_set_l.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/ico/set.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_set_l.setIcon(icon2)
        self.pushButton_set_l.setObjectName("pushButton_set_l")
        self.horizontalLayout_3.addWidget(self.pushButton_set_l)
        self.label_ip = QtWidgets.QLabel(self.frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ip.sizePolicy().hasHeightForWidth())
        self.label_ip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_ip.setFont(font)
        self.label_ip.setStyleSheet("color: rgb(248, 237, 83);")
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout_3.addWidget(self.label_ip)
        self.frame_right = QtWidgets.QFrame(self.page_login)
        self.frame_right.setGeometry(QtCore.QRect(180, 220, 181, 41))
        self.frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")
        self.pushButton_connectLight = QtWidgets.QPushButton(self.frame_right)
        self.pushButton_connectLight.setGeometry(QtCore.QRect(10, 10, 65, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_connectLight.sizePolicy().hasHeightForWidth())
        self.pushButton_connectLight.setSizePolicy(sizePolicy)
        self.pushButton_connectLight.setStyleSheet("QPushButton{\n"
"background-color: rgba(255, 255, 255,0);\n"
"boder:none;\n"
"}\n"
"QPushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_connectLight.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico/ico/redpoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_connectLight.setIcon(icon3)
        self.pushButton_connectLight.setObjectName("pushButton_connectLight")
        self.label_connect = QtWidgets.QLabel(self.frame_right)
        self.label_connect.setGeometry(QtCore.QRect(60, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_connect.setFont(font)
        self.label_connect.setStyleSheet("color: rgb(248, 237, 83);")
        self.label_connect.setObjectName("label_connect")
        self.stackedWidget.addWidget(self.page_login)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.pushButton_return_r = QtWidgets.QPushButton(self.page_register)
        self.pushButton_return_r.setGeometry(QtCore.QRect(220, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_return_r.setFont(font)
        self.pushButton_return_r.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(223, 212, 63);\n"
"}\n"
"QPushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_return_r.setObjectName("pushButton_return_r")
        self.lineEdit_password_r = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_password_r.setGeometry(QtCore.QRect(130, 90, 191, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.lineEdit_password_r.setFont(font)
        self.lineEdit_password_r.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit_password_r.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_r.setPlaceholderText("")
        self.lineEdit_password_r.setObjectName("lineEdit_password_r")
        self.label_username = QtWidgets.QLabel(self.page_register)
        self.label_username.setGeometry(QtCore.QRect(60, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(15)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label_username.setObjectName("label_username")
        self.lineEdit_username_r = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_username_r.setGeometry(QtCore.QRect(130, 40, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setUnderline(False)
        self.lineEdit_username_r.setFont(font)
        self.lineEdit_username_r.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit_username_r.setPlaceholderText("")
        self.lineEdit_username_r.setObjectName("lineEdit_username_r")
        self.label_13 = QtWidgets.QLabel(self.page_register)
        self.label_13.setGeometry(QtCore.QRect(60, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label_13.setObjectName("label_13")
        self.pushButton_register_r = QtWidgets.QPushButton(self.page_register)
        self.pushButton_register_r.setGeometry(QtCore.QRect(60, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_register_r.setFont(font)
        self.pushButton_register_r.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(223, 212, 63);\n"
"}\n"
"QPushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_register_r.setObjectName("pushButton_register_r")
        self.lineEdit_repassword_r = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_repassword_r.setGeometry(QtCore.QRect(160, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.lineEdit_repassword_r.setFont(font)
        self.lineEdit_repassword_r.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit_repassword_r.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_repassword_r.setPlaceholderText("")
        self.lineEdit_repassword_r.setObjectName("lineEdit_repassword_r")
        self.label_14 = QtWidgets.QLabel(self.page_register)
        self.label_14.setGeometry(QtCore.QRect(60, 140, 101, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_register)
        self.label_15.setGeometry(QtCore.QRect(130, -10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(248, 237, 83);")
        self.label_15.setObjectName("label_15")
        self.pushButton_return_r.raise_()
        self.label_username.raise_()
        self.label_13.raise_()
        self.pushButton_register_r.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.lineEdit_username_r.raise_()
        self.lineEdit_password_r.raise_()
        self.lineEdit_repassword_r.raise_()
        self.stackedWidget.addWidget(self.page_register)
        self.page_Setting = QtWidgets.QWidget()
        self.page_Setting.setObjectName("page_Setting")
        self.label_16 = QtWidgets.QLabel(self.page_Setting)
        self.label_16.setGeometry(QtCore.QRect(60, 50, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_Setting)
        self.label_17.setGeometry(QtCore.QRect(130, -10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(248, 237, 83);")
        self.label_17.setObjectName("label_17")
        self.lineEdit_ip_s = QtWidgets.QLineEdit(self.page_Setting)
        self.lineEdit_ip_s.setGeometry(QtCore.QRect(130, 50, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setUnderline(False)
        self.lineEdit_ip_s.setFont(font)
        self.lineEdit_ip_s.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit_ip_s.setPlaceholderText("")
        self.lineEdit_ip_s.setObjectName("lineEdit_ip_s")
        self.lineEdit_port_s = QtWidgets.QLineEdit(self.page_Setting)
        self.lineEdit_port_s.setGeometry(QtCore.QRect(130, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.lineEdit_port_s.setFont(font)
        self.lineEdit_port_s.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.lineEdit_port_s.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_port_s.setPlaceholderText("")
        self.lineEdit_port_s.setObjectName("lineEdit_port_s")
        self.pushButton_return_s = QtWidgets.QPushButton(self.page_Setting)
        self.pushButton_return_s.setGeometry(QtCore.QRect(220, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_return_s.setFont(font)
        self.pushButton_return_s.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(223, 212, 63);\n"
"}\n"
"QPushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_return_s.setObjectName("pushButton_return_s")
        self.label_18 = QtWidgets.QLabel(self.page_Setting)
        self.label_18.setGeometry(QtCore.QRect(60, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0);")
        self.label_18.setObjectName("label_18")
        self.pushButton_set_s = QtWidgets.QPushButton(self.page_Setting)
        self.pushButton_set_s.setGeometry(QtCore.QRect(60, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("851tegakizatsu")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_set_s.setFont(font)
        self.pushButton_set_s.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(223, 212, 63);\n"
"}\n"
"QPushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_set_s.setObjectName("pushButton_set_s")
        self.stackedWidget.addWidget(self.page_Setting)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_content)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_7.clicked.connect(MainWindow.showMinimized)
        self.pushButton_8.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Secure File Transfer"))
        self.label_4.setText(_translate("MainWindow", "账号："))
        self.label_5.setText(_translate("MainWindow", "密码："))
        self.pushButton_register_l.setText(_translate("MainWindow", "注册"))
        self.pushButton_login_l.setText(_translate("MainWindow", "登录"))
        self.label_ip.setText(_translate("MainWindow", "127.0.0.1：6666"))
        self.label_connect.setText(_translate("MainWindow", "Disonnect"))
        self.pushButton_return_r.setText(_translate("MainWindow", "返回"))
        self.label_username.setText(_translate("MainWindow", "用户名："))
        self.label_13.setText(_translate("MainWindow", "密码："))
        self.pushButton_register_r.setText(_translate("MainWindow", "注册"))
        self.label_14.setText(_translate("MainWindow", "确认密码："))
        self.label_15.setText(_translate("MainWindow", "Register"))
        self.label_16.setText(_translate("MainWindow", "IP："))
        self.label_17.setText(_translate("MainWindow", "Setting"))
        self.pushButton_return_s.setText(_translate("MainWindow", "返回"))
        self.label_18.setText(_translate("MainWindow", "Prot："))
        self.pushButton_set_s.setText(_translate("MainWindow", "设定"))
import ico_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
