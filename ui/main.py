# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import numpy as np
import copy

MAIN_FILE_PATH = os.path.dirname(os.path.abspath(__file__))

class Ui_MainWindow(object):
    def __init__(self):
        self.main_img = cv2.imread(os.path.join(MAIN_FILE_PATH, './resource/no_signal.jpg')) if \
            os.path.isfile(os.path.join(MAIN_FILE_PATH, './resource/no_signal.jpg')) else \
            np.zeros((900, 900, 3), dtype=np.uint8)
        self.show_img = copy.deepcopy(self.main_img)
        # self.load_img()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(500, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_20 = QtWidgets.QLabel(self.widget_6)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.widget_5)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.label_19 = QtWidgets.QLabel(self.widget_5)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(self.widget_6)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.radioButton_1_1 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_1_1.setText("")
        self.radioButton_1_1.setObjectName("radioButton_1_1")
        self.horizontalLayout_5.addWidget(self.radioButton_1_1)
        self.radioButton_1_2 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_1_2.setText("")
        self.radioButton_1_2.setObjectName("radioButton_1_2")
        self.horizontalLayout_5.addWidget(self.radioButton_1_2)
        self.radioButton_1_3 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_1_3.setText("")
        self.radioButton_1_3.setObjectName("radioButton_1_3")
        self.horizontalLayout_5.addWidget(self.radioButton_1_3)
        self.radioButton_1_4 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_1_4.setText("")
        self.radioButton_1_4.setObjectName("radioButton_1_4")
        self.horizontalLayout_5.addWidget(self.radioButton_1_4)
        self.radioButton_1_5 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_1_5.setText("")
        self.radioButton_1_5.setObjectName("radioButton_1_5")
        self.horizontalLayout_5.addWidget(self.radioButton_1_5)
        self.radioButton_1_6 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_1_6.setText("")
        self.radioButton_1_6.setObjectName("radioButton_1_6")
        self.horizontalLayout_5.addWidget(self.radioButton_1_6)
        self.radioButton_1_7 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_1_7.setText("")
        self.radioButton_1_7.setObjectName("radioButton_1_7")
        self.horizontalLayout_5.addWidget(self.radioButton_1_7)
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_6)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.radioButton_2_1 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_2_1.setText("")
        self.radioButton_2_1.setObjectName("radioButton_2_1")
        self.horizontalLayout_6.addWidget(self.radioButton_2_1)
        self.radioButton_2_2 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_2_2.setText("")
        self.radioButton_2_2.setObjectName("radioButton_2_2")
        self.horizontalLayout_6.addWidget(self.radioButton_2_2)
        self.radioButton_2_3 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_2_3.setText("")
        self.radioButton_2_3.setObjectName("radioButton_2_3")
        self.horizontalLayout_6.addWidget(self.radioButton_2_3)
        self.radioButton_2_4 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_2_4.setText("")
        self.radioButton_2_4.setObjectName("radioButton_2_4")
        self.horizontalLayout_6.addWidget(self.radioButton_2_4)
        self.radioButton_2_5 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_2_5.setText("")
        self.radioButton_2_5.setObjectName("radioButton_2_5")
        self.horizontalLayout_6.addWidget(self.radioButton_2_5)
        self.radioButton_2_6 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_2_6.setText("")
        self.radioButton_2_6.setObjectName("radioButton_2_6")
        self.horizontalLayout_6.addWidget(self.radioButton_2_6)
        self.radioButton_2_7 = QtWidgets.QRadioButton(self.widget_4)
        self.radioButton_2_7.setText("")
        self.radioButton_2_7.setObjectName("radioButton_2_7")
        self.horizontalLayout_6.addWidget(self.radioButton_2_7)
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.radioButton_3_1 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_3_1.setText("")
        self.radioButton_3_1.setObjectName("radioButton_3_1")
        self.horizontalLayout_4.addWidget(self.radioButton_3_1)
        self.radioButton_3_2 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_3_2.setText("")
        self.radioButton_3_2.setObjectName("radioButton_3_2")
        self.horizontalLayout_4.addWidget(self.radioButton_3_2)
        self.radioButton_3_3 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_3_3.setText("")
        self.radioButton_3_3.setObjectName("radioButton_3_3")
        self.horizontalLayout_4.addWidget(self.radioButton_3_3)
        self.radioButton_3_4 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_3_4.setText("")
        self.radioButton_3_4.setObjectName("radioButton_3_4")
        self.horizontalLayout_4.addWidget(self.radioButton_3_4)
        self.radioButton_3_5 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_3_5.setText("")
        self.radioButton_3_5.setObjectName("radioButton_3_5")
        self.horizontalLayout_4.addWidget(self.radioButton_3_5)
        self.radioButton_3_6 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_3_6.setText("")
        self.radioButton_3_6.setObjectName("radioButton_3_6")
        self.horizontalLayout_4.addWidget(self.radioButton_3_6)
        self.radioButton_3_7 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_3_7.setText("")
        self.radioButton_3_7.setObjectName("radioButton_3_7")
        self.horizontalLayout_4.addWidget(self.radioButton_3_7)
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.widget_6)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.radioButton_4_1 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4_1.setText("")
        self.radioButton_4_1.setObjectName("radioButton_4_1")
        self.horizontalLayout_3.addWidget(self.radioButton_4_1)
        self.radioButton_4_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4_2.setText("")
        self.radioButton_4_2.setObjectName("radioButton_4_2")
        self.horizontalLayout_3.addWidget(self.radioButton_4_2)
        self.radioButton_4_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4_3.setText("")
        self.radioButton_4_3.setObjectName("radioButton_4_3")
        self.horizontalLayout_3.addWidget(self.radioButton_4_3)
        self.radioButton_4_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4_4.setText("")
        self.radioButton_4_4.setObjectName("radioButton_4_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4_4)
        self.radioButton_4_5 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4_5.setText("")
        self.radioButton_4_5.setObjectName("radioButton_4_5")
        self.horizontalLayout_3.addWidget(self.radioButton_4_5)
        self.radioButton_4_6 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4_6.setText("")
        self.radioButton_4_6.setObjectName("radioButton_4_6")
        self.horizontalLayout_3.addWidget(self.radioButton_4_6)
        self.radioButton_4_7 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4_7.setText("")
        self.radioButton_4_7.setObjectName("radioButton_4_7")
        self.horizontalLayout_3.addWidget(self.radioButton_4_7)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.verticalLayout.addWidget(self.widget)
        self.label = QtWidgets.QLabel(self.widget_6)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.widget_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.label_20.setText(_translate("MainWindow", "ABCDEFG"))
        self.label_18.setText(_translate("MainWindow", "      "))
        self.label_3.setText(_translate("MainWindow", "-3"))
        self.label_4.setText(_translate("MainWindow", "-2"))
        self.label_5.setText(_translate("MainWindow", "-1"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "1"))
        self.label_8.setText(_translate("MainWindow", "2"))
        self.label_9.setText(_translate("MainWindow", "3"))
        self.label_19.setText(_translate("MainWindow", "      "))
        self.label_10.setText(_translate("MainWindow", "1-1"))
        self.label_11.setText(_translate("MainWindow", "1_2"))
        self.label_12.setText(_translate("MainWindow", "2_1"))
        self.label_13.setText(_translate("MainWindow", "2_2"))
        self.label_14.setText(_translate("MainWindow", "3_1"))
        self.label_15.setText(_translate("MainWindow", "3_2"))
        self.label_16.setText(_translate("MainWindow", "4_1"))
        self.label_17.setText(_translate("MainWindow", "4_2"))
        self.label.setText(_translate("MainWindow", "XXXX/XXXXX"))

class MainWindow(QtWidgets.QMainWindow):
    resized = QtCore.pyqtSignal()  # 窗口缩放信号
    showTextSignal = QtCore.pyqtSignal(str)  # 文字修改信号

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.resized.connect(self.resize_func)

    # def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
    #     """
    #     重载resize事件
    #     :param a0:
    #     :return:
    #     """
    #     self.resized.emit()
    #     return super(MainWindow, self).resizeEvent(a0)

    # def resize_func(self):
    #     self.ui.refresh_img(result_json=self.ui.result_json)

    # def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
    #     """
    #     重载close事件
    #     :param a0:
    #     :return:
    #     """
    #     if self.ui.pushButton_Disconnect.isEnabled():
    #         self.ui.disconnect_click()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())