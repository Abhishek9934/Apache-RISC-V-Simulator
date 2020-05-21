import PC
import configme
import sys
import Commander_normal
import PipCommander
import Commander
import executed_information
import register_file
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import BASIC_code
#import breeze_resources
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt


from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette

from PyQt5 import QtCore, QtGui, QtWidgets
import error_detector_unit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        configme.breakflag=0
        self.mcgenflag=0
        self.runflag=0
        self.steppointer=int((PC.PC)/4)
        self.inst_num=0
        self.breakpoint=-1
        self.breakpc=-1
        self.endpc=-1
        
        FONT = QtGui.QFont()
        FONT.setPointSize(12)
        FONT3 = QtGui.QFont()
        FONT3.setPointSize(10)
        font2 = QtGui.QFont()
        font2.setPointSize(12)
        font4 = QtGui.QFont()
        font4.setPointSize(11)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1284, 858)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setStyleSheet("background-color:black;")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.panes = QtWidgets.QTabWidget(self.centralwidget)
        self.panes.setEnabled(True)
        self.panes.setDocumentMode(False)
        self.panes.setMovable(False)
        self.panes.setTabBarAutoHide(True)
        self.panes.setObjectName("panes")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.label_44 = QtWidgets.QLabel(self.tab_8)
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.tab_8)
        self.label_42.setObjectName("label_42")
        self.gridLayout_3.addWidget(self.label_42, 0, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.tab_8)
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("../../Pictures/fall-autumn-red-season.jpg"))
        self.label_43.setObjectName("label_43")
        self.gridLayout_3.addWidget(self.label_43, 1, 1, 1, 1)
        
        self.panes.addTab(self.tab_8, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.openfilebutton = QtWidgets.QPushButton(self.tab)
        self.openfilebutton.setObjectName("openfilebutton")

        self.openfilebutton.clicked.connect(self.dialogopener)

        self.gridLayout_2.addWidget(self.openfilebutton, 0, 0, 1, 1)
        self.editor_code = QtWidgets.QTextEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editor_code.sizePolicy().hasHeightForWidth())
        self.editor_code.setSizePolicy(sizePolicy)
        self.editor_code.setObjectName("editor_code")
        self.editor_code.setFont(FONT)
        self.gridLayout_2.addWidget(self.editor_code, 1, 0, 1, 1)
        self.panes.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)
        self.previous = QtWidgets.QPushButton(self.tab_2)
        self.previous.setObjectName("previous")
        self.gridLayout_9.addWidget(self.previous, 0, 7, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.tab_2)
        self.label_39.setObjectName("label_39")
        self.gridLayout_9.addWidget(self.label_39, 3, 0, 1, 1)
        self.run = QtWidgets.QPushButton(self.tab_2)
        self.run.setObjectName("run")
        self.gridLayout_9.addWidget(self.run, 0, 5, 1, 1)
        self.pc_edit = QtWidgets.QLineEdit(self.tab_2)
        self.pc_edit.setObjectName("pc_edit")
        self.pc_edit.setFont(FONT)
        self.gridLayout_9.addWidget(self.pc_edit, 0, 2, 1, 1)
        # self.asciiradiobutton = QtWidgets.QRadioButton(self.tab_2)
        # self.asciiradiobutton.setObjectName("asciiradiobutton")
        # self.gridLayout_9.addWidget(self.asciiradiobutton, 5, 12, 1, 1)
        # self.decimalradiobutton = QtWidgets.QRadioButton(self.tab_2)
        # self.decimalradiobutton.setObjectName("decimalradiobutton")
        # self.gridLayout_9.addWidget(self.decimalradiobutton, 5, 11, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setObjectName("label_41")
        self.gridLayout_9.addWidget(self.label_41, 3, 6, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.tab_2)
        self.label_40.setObjectName("label_40")
        self.gridLayout_9.addWidget(self.label_40, 3, 2, 1, 1)
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.console = QtWidgets.QTextEdit(self.tab_7)
        self.console.setObjectName("console")
        self.console.setFont(FONT)
        self.gridLayout_6.addWidget(self.console, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_7, "")
        self.gridLayout_9.addWidget(self.tabWidget_5, 4, 9, 1, 4)
        self.basic_code = QtWidgets.QTextEdit(self.tab_2)
        self.basic_code.setObjectName("basic_code")
        self.basic_code.setFont(FONT)
        self.gridLayout_9.addWidget(self.basic_code, 4, 0, 1, 8)
        self.reset = QtWidgets.QPushButton(self.tab_2)
        self.reset.setObjectName("reset")
        self.gridLayout_9.addWidget(self.reset, 0, 8, 1, 1)
        self.step = QtWidgets.QPushButton(self.tab_2)
        self.step.setObjectName("step")
        self.gridLayout_9.addWidget(self.step, 0, 6, 1, 1)
        # self.hexradiobutton = QtWidgets.QRadioButton(self.tab_2)
        # self.hexradiobutton.setChecked(True)
        # self.hexradiobutton.setObjectName("hexradiobutton")
        # self.gridLayout_9.addWidget(self.hexradiobutton, 5, 13, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setFixedWidth(515)
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -321, 239, 1478))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.x0 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x0.setObjectName("x0")
        self.x0.setFont(font2)
        self.gridLayout_5.addWidget(self.x0, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)
        self.x1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x1.setObjectName("x1")
        self.x1.setFont(font2)
        self.gridLayout_5.addWidget(self.x1, 1, 1, 1, 1)
        self.x9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x9.setObjectName("x9")
        self.x9.setFont(font2)
        self.gridLayout_5.addWidget(self.x9, 9, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 10, 0, 1, 1)
        self.x10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x10.setObjectName("x10")
        self.x10.setFont(font2)
        self.gridLayout_5.addWidget(self.x10, 10, 1, 1, 1)
        self.x4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x4.setObjectName("x4")
        self.x4.setFont(font2)
        self.gridLayout_5.addWidget(self.x4, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 4, 0, 1, 1)
        self.x6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x6.setObjectName("x6")
        self.x6.setFont(font2)
        self.gridLayout_5.addWidget(self.x6, 6, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 6, 0, 1, 1)
        self.x2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x2.setObjectName("x2")
        self.x2.setFont(font2)
        self.gridLayout_5.addWidget(self.x2, 2, 1, 1, 1)
        self.x5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x5.setObjectName("x5")
        self.x5.setFont(font2)
        self.gridLayout_5.addWidget(self.x5, 5, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 3, 0, 1, 1)
        self.x3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x3.setObjectName("x3")
        self.x3.setFont(font2)
        self.gridLayout_5.addWidget(self.x3, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 5, 0, 1, 1)
        self.x7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x7.setText("")
        self.x7.setObjectName("x7")
        self.x7.setFont(font2)
        self.gridLayout_5.addWidget(self.x7, 7, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 8, 0, 1, 1)
        self.x8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x8.setObjectName("x8")
        self.x8.setFont(font2)
        self.gridLayout_5.addWidget(self.x8, 8, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 11, 0, 1, 1)
        self.x11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x11.setObjectName("x11")
        self.x11.setFont(font2)
        self.gridLayout_5.addWidget(self.x11, 11, 1, 1, 1)
        self.x12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x12.setObjectName("x12")
        self.x12.setFont(font2)
        self.gridLayout_5.addWidget(self.x12, 12, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 13, 0, 1, 1)
        self.x13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x13.setObjectName("x13")
        self.x13.setFont(font2)
        self.gridLayout_5.addWidget(self.x13, 13, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 12, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 14, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 22, 0, 1, 1)
        self.x17 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x17.setObjectName("x17")
        self.x17.setFont(font2)
        self.gridLayout_5.addWidget(self.x17, 17, 1, 1, 1)
        self.x22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x22.setObjectName("x22")
        self.x22.setFont(font2)
        self.gridLayout_5.addWidget(self.x22, 22, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 23, 0, 1, 1)
        self.x24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x24.setObjectName("x24")
        self.x24.setFont(font2)
        self.gridLayout_5.addWidget(self.x24, 24, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 25, 0, 1, 1)
        self.x25 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x25.setObjectName("x25")
        self.x25.setFont(font2)
        self.gridLayout_5.addWidget(self.x25, 25, 1, 1, 1)
        self.x15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x15.setObjectName("x15")
        self.x15.setFont(font2)
        self.gridLayout_5.addWidget(self.x15, 15, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 24, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 18, 0, 1, 1)
        self.x23 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x23.setObjectName("x23")
        self.x23.setFont(font2)
        self.gridLayout_5.addWidget(self.x23, 23, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 26, 0, 1, 1)
        self.x18 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x18.setObjectName("x18")
        self.x18.setFont(font2)
        self.gridLayout_5.addWidget(self.x18, 18, 1, 1, 1)
        self.x20 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x20.setObjectName("x20")
        self.x20.setFont(font2)
        self.gridLayout_5.addWidget(self.x20, 20, 1, 1, 1)
        self.x19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x19.setObjectName("x19")
        self.x19.setFont(font2)
        self.gridLayout_5.addWidget(self.x19, 19, 1, 1, 1)
        self.x26 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x26.setObjectName("x26")
        self.x26.setFont(font2)
        self.gridLayout_5.addWidget(self.x26, 26, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_32, 17, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 15, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 16, 0, 1, 1)
        self.x16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x16.setObjectName("x16")
        self.x16.setFont(font2)
        self.gridLayout_5.addWidget(self.x16, 16, 1, 1, 1)
        self.x14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x14.setObjectName("x14")
        self.x14.setFont(font2)
        self.gridLayout_5.addWidget(self.x14, 14, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 20, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 21, 0, 1, 1)
        self.x21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x21.setObjectName("x21")
        self.x21.setFont(font2)
        self.gridLayout_5.addWidget(self.x21, 21, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 19, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_33, 30, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 28, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName("label_34")
        self.gridLayout_5.addWidget(self.label_34, 31, 0, 1, 1)
        self.x30 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x30.setObjectName("x30")
        self.x30.setFont(font2)
        self.gridLayout_5.addWidget(self.x30, 30, 1, 1, 1)
        self.x29 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x29.setObjectName("x29")
        self.x29.setFont(font2)
        self.gridLayout_5.addWidget(self.x29, 29, 1, 1, 1)
        self.x28 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x28.setObjectName("x28")
        self.x28.setFont(font2)
        self.gridLayout_5.addWidget(self.x28, 28, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 27, 0, 1, 1)
        self.x27 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x27.setObjectName("x27")
        self.x27.setFont(font2)
        self.gridLayout_5.addWidget(self.x27, 27, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 29, 0, 1, 1)
        self.x31 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.x31.setObjectName("x31")
        self.x31.setFont(font2)
        self.gridLayout_5.addWidget(self.x31, 31, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 152, 115))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_8.addWidget(self.line, 1, 0, 1, 6)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName("label_38")
        self.gridLayout_8.addWidget(self.label_38, 0, 5, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName("label_37")
        self.gridLayout_8.addWidget(self.label_37, 0, 4, 1, 1)
        self.address_code = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.address_code.setObjectName("address_code")
        self.address_code.setFont(FONT3)
        self.gridLayout_8.addWidget(self.address_code, 2, 0, 1, 6)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout_8.addWidget(self.label_36, 0, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName("label_35")
        self.gridLayout_8.addWidget(self.label_35, 0, 2, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.addWidget(self.scrollArea_2, 0, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout_9.addWidget(self.tabWidget_2, 0, 13, 5, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 3, 1, 1, 1)
        
        self.stopbutton = QtWidgets.QPushButton(self.tab_2)
        self.stopbutton.setObjectName("stopbutton")
        self.gridLayout_9.addWidget(self.stopbutton, 0, 9, 1, 1)
        self.dumpbutton = QtWidgets.QPushButton(self.tab_2)
        self.dumpbutton.setObjectName("dumpbutton")
        self.gridLayout_9.addWidget(self.dumpbutton, 0, 11, 1, 1)

        self.stopbutton.setText("Stop")
        self.stopbutton.clicked.connect(self.stop)
        self.dumpbutton.setText("Dump")
        self.dumpbutton.clicked.connect(self.dump)

        
        #self.normalExecution = QtWidgets.QRadioButton(self.tab_2)
        #self.normalExecution.setObjectName("normalExecution")
        #self.gridLayout_9.addWidget(self.normalExecution, 5, 3, 1, 1)
        #self.normalExecution.setChecked(True)
        #self.pipeLined = QtWidgets.QRadioButton(self.tab_2)
        #self.pipeLined.setObjectName("pipeLined")
        #self.gridLayout_9.addWidget(self.pipeLined, 5, 4, 1, 1)
        self.panes.addTab(self.tab_2, "")


        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("HEXADECIMAL")
        self.comboBox.addItem("DECIMAL")
        self.comboBox.addItem("ASCII")
        self.gridLayout_9.addWidget(self.comboBox, 5, 13 , 1, 1)

        self.pipelined_tab = QtWidgets.QWidget()
        self.pipelined_tab.setObjectName("pipelined_tab")
        self.cycle = QtWidgets.QLabel(self.pipelined_tab)
        self.cycle.setGeometry(QtCore.QRect(30, 60, 250, 17))
        self.cycle.setObjectName("cycle")
        self.cycle.setFont(font4)
        self.inst = QtWidgets.QLabel(self.pipelined_tab)
        self.inst.setGeometry(QtCore.QRect(30, 30, 250, 17))
        self.inst.setObjectName("inst")
        self.inst.setFont(font4)
        self.cpi = QtWidgets.QLabel(self.pipelined_tab)
        self.cpi.setGeometry(QtCore.QRect(30, 90, 250, 17))
        self.cpi.setObjectName("cpi")
        self.cpi.setFont(font4)
        self.data_transfer = QtWidgets.QLabel(self.pipelined_tab)
        self.data_transfer.setGeometry(QtCore.QRect(30, 120, 291, 17))
        self.data_transfer.setObjectName("data_transfer")
        self.data_transfer.setFont(font4)
        self.alu = QtWidgets.QLabel(self.pipelined_tab)
        self.alu.setGeometry(QtCore.QRect(30, 150, 250, 17))
        self.alu.setObjectName("alu")
        self.alu.setFont(font4)
        self.label_45 = QtWidgets.QLabel(self.pipelined_tab)
        self.label_45.setGeometry(QtCore.QRect(30, 180, 250, 17))
        self.label_45.setObjectName("label_45")
        self.label_45.setFont(font4)
        self.label_46 = QtWidgets.QLabel(self.pipelined_tab)
        self.label_46.setGeometry(QtCore.QRect(30, 210, 250, 17))
        self.label_46.setObjectName("label_46")
        self.label_46.setFont(font4)
        self.label_47 = QtWidgets.QLabel(self.pipelined_tab)
        self.label_47.setGeometry(QtCore.QRect(30, 240, 250, 17))
        self.label_47.setObjectName("label_47")
        self.label_47.setFont(font4)
        self.label_48 = QtWidgets.QLabel(self.pipelined_tab)
        self.label_48.setGeometry(QtCore.QRect(30, 270, 250, 17))
        self.label_48.setObjectName("label_48")
        self.label_48.setFont(font4)
        self.label_49 = QtWidgets.QLabel(self.pipelined_tab)
        self.label_49.setGeometry(QtCore.QRect(30, 300, 250, 17))
        self.label_49.setObjectName("label_49")
        self.label_49.setFont(font4)
        self.label_50 = QtWidgets.QLabel(self.pipelined_tab)
        self.label_50.setGeometry(QtCore.QRect(30, 330, 250, 17))
        self.label_50.setObjectName("label_50")
        self.label_50.setFont(font4)
        self.label_51 = QtWidgets.QLabel(self.pipelined_tab)
        self.label_51.setGeometry(QtCore.QRect(30, 360, 291, 17))
        self.label_51.setObjectName("label_51")
        self.label_51.setFont(font4)
        self.lineEdit = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit.setGeometry(QtCore.QRect(350, 20, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(FONT)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 50, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(FONT)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 80, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(FONT)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 110, 113, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFont(FONT)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 140, 113, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setFont(FONT)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 170, 113, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setFont(FONT)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 200, 113, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setFont(FONT)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(350, 230, 113, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setFont(FONT)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_13.setGeometry(QtCore.QRect(350, 350, 113, 25))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setFont(FONT)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_14.setGeometry(QtCore.QRect(350, 320, 113, 25))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setFont(FONT)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_15.setGeometry(QtCore.QRect(350, 290, 113, 25))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setFont(FONT)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.pipelined_tab)
        self.lineEdit_16.setGeometry(QtCore.QRect(350, 260, 113, 25))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.setFont(FONT)

        self.piptabwidget = QtWidgets.QTabWidget(self.pipelined_tab)
        self.piptabwidget.setGeometry(QtCore.QRect(480, 0,1400, 960))
        self.piptabwidget.setObjectName("piptabwidget")
        self.executed_info_tab = QtWidgets.QWidget()
        self.executed_info_tab.setObjectName("executed_info_tab")
        self.textEdit_2 = QtWidgets.QTextEdit(self.executed_info_tab)
        self.textEdit_2.setGeometry(QtCore.QRect(3, 9, 1375, 850))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(FONT)
        # self.textEdit_2.append(f"Cycle number\t\tFetch\t\tDecode\t\tExecute\t\tMemAccess\t\tWriteBack")
        self.piptabwidget.addTab(self.executed_info_tab, "")
        self.child_tab = QtWidgets.QWidget()
        self.child_tab.setObjectName("child_tab")
        self.textEdit = QtWidgets.QTextEdit(self.child_tab)
        self.textEdit.setGeometry(QtCore.QRect(3, 9, 1375, 850))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(FONT)
        self.piptabwidget.addTab(self.child_tab, "")
        self.panes.addTab(self.pipelined_tab, "")


        self.gridLayout.addWidget(self.panes, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 32))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New_Project = QtWidgets.QAction(MainWindow)
        self.action_New_Project.setObjectName("action_New_Project")
        self.action_Open_Project = QtWidgets.QAction(MainWindow)
        self.action_Open_Project.setObjectName("action_Open_Project")
        self.action_Save_Project = QtWidgets.QAction(MainWindow)
        self.action_Save_Project.setObjectName("action_Save_Project")
        self.action_Close_Project = QtWidgets.QAction(MainWindow)
        self.action_Close_Project.setObjectName("action_Close_Project")
        self.action_Undo = QtWidgets.QAction(MainWindow)
        self.action_Undo.setObjectName("action_Undo")
        self.action_Redo = QtWidgets.QAction(MainWindow)
        self.action_Redo.setObjectName("action_Redo")
        self.action_Cut = QtWidgets.QAction(MainWindow)
        self.action_Cut.setObjectName("action_Cut")
        self.action_Copy = QtWidgets.QAction(MainWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(MainWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Select_All = QtWidgets.QAction(MainWindow)
        self.action_Select_All.setObjectName("action_Select_All")
        self.action_Save_Project_2 = QtWidgets.QAction(MainWindow)
        self.action_Save_Project_2.setObjectName("action_Save_Project_2")
        self.menu_File.addAction(self.action_New_Project)
        self.menu_File.addAction(self.action_Close_Project)
        self.menu_File.addAction(self.action_Save_Project_2)
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addAction(self.action_Select_All)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())

        self.retranslateUi(MainWindow)


        self.panes.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.action_Close_Project.triggered.connect(MainWindow.close)

        self.action_Select_All.triggered.connect(self.editor_code.selectAll)
        self.action_Paste.triggered.connect(self.editor_code.paste)
        self.action_Undo.triggered.connect(self.basic_code.undo)
        self.action_Cut.triggered.connect(self.basic_code.cut)
        self.action_Redo.triggered.connect(self.basic_code.redo)
        self.action_Paste.triggered.connect(self.basic_code.paste)
        self.action_Select_All.triggered.connect(self.basic_code.selectAll)
        self.action_Copy.triggered.connect(self.basic_code.copy)
        self.action_Copy.triggered.connect(self.editor_code.copy)
        self.action_Undo.triggered.connect(self.editor_code.undo)
        self.action_Redo.triggered.connect(self.editor_code.redo)
        self.action_Cut.triggered.connect(self.editor_code.cut)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.run.clicked.connect(self.run_buttonclicked)
        self.reset.clicked.connect(self.RESET_IT)
        self.step.clicked.connect(self.step_buttonclicked)
        self.previous.clicked.connect(self.prev_buttonclicked)
       #self.asciiradiobutton.clicked.connect(self.ascii_clicked)
       #self.hexradiobutton.clicked.connect(self.hex_clicked)
       #self.decimalradiobutton.clicked.connect(self.dec_clicked)

        self.comboBox.activated[str].connect(self.On_activated)
        # self.normalExecution.clicked.connect(self.NORM_EXEC)
        # self.pipeLined.clicked.connect(self.PIP_EXEC)
        self.panes.currentChanged.connect(self.tabchanged)
        self.basic_code.mouseReleaseEvent = self.basiccode_clicked
        self.basiccodecursor=self.basic_code.textCursor()

        self.gif = QtGui.QMovie("test.gif", QtCore.QByteArray()) 
        self.gif.setCacheMode(QtGui.QMovie.CacheAll) 
        self.gif.setSpeed(100)
        self.label_43.setMovie(self.gif)
        self.gif.start()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apache 2.0"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#f57900;\">DEVELOPERS:</span></p><p><span style=\" font-size:12pt; color:#f57900;\">SACSHAM GUPTA,  ABHISHEK KUMAR GUPTA, VUSIRIKALA ABHISHEK,</span></p><p><span style=\" font-size:12pt; color:#f57900;\">STEPHEN SUGUN, TANEESH KAUSHIK</span></p></body></html>"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ce5c00;\">APACHE 2.0</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ce5c00;\">RISC-V PIPELINED SIMULATOR</span></p></body></html>"))
        self.panes.setTabText(self.panes.indexOf(self.tab_8), _translate("MainWindow", "Home"))
        self.openfilebutton.setText(_translate("MainWindow", "OPEN FILE FROM COMPUTER"))
        self.panes.setTabText(self.panes.indexOf(self.tab), _translate("MainWindow", "Editor"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">PC VALUE:</span></p></body></html>"))
        self.previous.setText(_translate("MainWindow", "Previous"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ce5c00;\">     PC</span></p></body></html>"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.pc_edit.setText(_translate("MainWindow", "(Current PC value)"))
        # self.asciiradiobutton.setText(_translate("MainWindow", "ASCII"))
        # self.decimalradiobutton.setText(_translate("MainWindow", "Decimal"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ce5c00;\">MACHINE CODE</span></p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ce5c00;\">BASIC CODE</span></p></body></html>"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_7), _translate("MainWindow", "Console"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.step.setText(_translate("MainWindow", "Step"))
        # self.hexradiobutton.setText(_translate("MainWindow", "Hexadecimal"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">sp(x2)</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">zero</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ra(x1)</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a0(x10)</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t2(x7)</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">tp(x4)</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t1(x6)</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">gp(x3)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t0(x5)</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s0(x8)</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s1(x9)</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a1(x11)</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a3(x13)</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a2(x12)</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a4(x14)</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s6(x22)</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s7(x23)</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s9(x25)</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s8(x24)</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s2(x18)</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">s10(x26)</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a7(x17)</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a5(x15)</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">a6(x16)</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s4(x20)</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s5(x21)</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">s3(x19)</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t5(x30)</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t3(x28)</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t6(x31)</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">s11(x27)</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">t4(x29)</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "REGISTERS"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">+3</span></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">+2</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">Address</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">+1</span></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">+0</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "MEMORY"))
        # self.normalExecution.setText(_translate("MainWindow", "Normal Execution"))
        # self.pipeLined.setText(_translate("MainWindow", "Pipelined Execution"))
        self.panes.setTabText(self.panes.indexOf(self.tab_2), _translate("MainWindow", "StepByStep-Execution"))


        self.cycle.setText(_translate("MainWindow", "Total number of cycles"))
        self.inst.setText(_translate("MainWindow", "Total instructions executed"))
        self.cpi.setText(_translate("MainWindow", "CPI"))
        self.data_transfer.setText(_translate("MainWindow", "Data-transfer instructions executed"))
        self.alu.setText(_translate("MainWindow", "ALU instructions executed"))
        self.label_45.setText(_translate("MainWindow", "Control instructions executed"))
        self.label_46.setText(_translate("MainWindow", "Number of data hazards"))
        self.label_47.setText(_translate("MainWindow", "Number of control hazards"))
        self.label_48.setText(_translate("MainWindow", "Total Stalls in pipeline"))
        self.label_49.setText(_translate("MainWindow", "Stalls due to data hazards"))
        self.label_50.setText(_translate("MainWindow", "Stalls due to control hazards"))
        self.label_51.setText(_translate("MainWindow", "Branch mispredictions"))
        self.piptabwidget.setTabText(self.piptabwidget.indexOf(self.child_tab), _translate("MainWindow", "Branch Info"))
        self.piptabwidget.setTabText(self.piptabwidget.indexOf(self.executed_info_tab), _translate("MainWindow", "Executed Info"))
        self.panes.setTabText(self.panes.indexOf(self.pipelined_tab), _translate("MainWindow", "PipelinedOutput"))


        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.action_New_Project.setText(_translate("MainWindow", "&New Project"))
        self.action_New_Project.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Open_Project.setText(_translate("MainWindow", "&Open Project"))
        self.action_Save_Project.setText(_translate("MainWindow", "&Save Project"))
        self.action_Save_Project.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Close_Project.setText(_translate("MainWindow", "&Close Project"))
        self.action_Undo.setText(_translate("MainWindow", "&Undo"))
        self.action_Undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.action_Redo.setText(_translate("MainWindow", "&Redo"))
        self.action_Redo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.action_Cut.setText(_translate("MainWindow", "&Cut"))
        self.action_Cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_Copy.setText(_translate("MainWindow", "&Copy"))
        self.action_Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_Paste.setText(_translate("MainWindow", "&Paste"))
        self.action_Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_Select_All.setText(_translate("MainWindow", "&Select All"))
        self.action_Select_All.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_Save_Project_2.setText(_translate("MainWindow", "&Save Project"))


    def basiccode_clicked(self, event):
        #self.basic_code.setTextBackgroundColor(QtCore.Qt.red)
        #self.basic_code.setTextBackground(QtCore.Qt.white)
        #self.basic_code.setStyleSheet("background-color:rgb(255, 250, 250);")
        #num_lines=self.basic_code.document().blockCount()-1
        
        if(self.runflag==1):
            return

        visiblecursorpos= event.pos()
        basiccodecursor = self.editor_code.cursorForPosition (visiblecursorpos)
        line= basiccodecursor.blockNumber()
        #print(type(line))
        if(line == int(PC.PC/4)):
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Please Refrain")
            msg.setText("Please do not set the current instruction"+
            "to be executed to be the breakpoint")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
            return
        
        if(line == int(self.breakpc/4)):
            cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(line))
            format=QtGui.QTextBlockFormat()
            format.setBackground(QColor(25, 25, 25))
            cursor.setBlockFormat(format)
            self.breakpc=-1
            return


        for i in range( self.inst_num):
            cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(i))
            format=QtGui.QTextBlockFormat()
            format.setBackground(QColor(25, 25, 25))
            cursor.setBlockFormat(format)

        self.breakpc=line*4
        cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(line))
        format=QtGui.QTextBlockFormat()
        format.setBackground(QColor(255,204,204))
        cursor.setBlockFormat(format)

        cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
        format=QtGui.QTextBlockFormat()
        format.setBackground(QColor(0,255,0))
        cursor.setBlockFormat(format)

        
        #lineblock =basiccodecursor.blockFormat()
        #lineblock.setBackground(QtGui.QBrush(QtCore.Qt.yellow))
        #basiccodecursor.setBlockFormat(lineblock)
        #selection= self.basic_code.ExtraSelection()
        #lineColor = QtGui.QColor(QtCore.Qt.yellow).lighter(160)
        #selection.format.setBackground(lineColor)
        #self.basic_code.setStyleSheet("background-color: rgb(255, 255, 255)")
        return

        
    
    # knob=0
    choice=0
    #def NORM_EXEC(self):
    #    self.knob =0
 
    #def PIP_EXEC(self):
    #    self.knob =1

    # def hex_clicked(self):
    #     if(self.runflag==1):
    #         return
    #     self.choice=0
    #     self.CURRENT_VAL()
    #     #print(self.choice)

    # def dec_clicked(self):
    #     if(self.runflag==1):
    #         return
    #     self.choice=1
    #     self.CURRENT_VAL()
    #     #print(self.choice)
    # def ascii_clicked(self):
    #     if(self.runflag==1):
    #         return
    #     self.choice=2
    #     self.CURRENT_VAL()
    #     #print(self.choice)

    def On_activated(self,text):
        if(self.runflag ==1):
            return
        if text == "HEXADECIMAL":
            self.choice=0

        elif text == "DECIMAL":
            self.choice=1
        else:
            self.choice=2
        self.CURRENT_VAL()    


    def tabchanged(self):
        configme.breakflag=1
        self.runflag=0
        currindex=self.panes.currentIndex()
        if(currindex==2):
            
            editorcodefile=open("codefromeditor.txt", 'w+')
            editorcode=self.editor_code.toPlainText()
            editorcodefile.write(editorcode)
            editorcodefile.close()
            #errormessage, errorline= error_detection.main()
        
            error, errorline = error_detector_unit.main()      # number of line to be colored : errorline, error: msg
            
            error=error.strip()
            num=self.editor_code.document().blockCount()
            if(error!="noerror"):
                self.panes.setCurrentIndex(1)
                
                # for i in range(num):
                #     cursor=QtGui.QTextCursor(self.editor_code.document().findBlockByNumber(i))
                #     format=QtGui.QTextBlockFormat()
                #     format.setBackground(QColor(25,25,25))
                #     cursor.setBlockFormat(format)




                # cursor=QtGui.QTextCursor(self.editor_code.document().findBlockByNumber(errorline))
                # format=QtGui.QTextBlockFormat()
                # format.setBackground(QColor(255,255,204))
                # cursor.setBlockFormat(format)

                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle(f"Error in command {errorline}")
                msg.setText(error)
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.exec_()
                return

            if(error=="noerror"):

                for i in range(num):
                    cursor=QtGui.QTextCursor(self.editor_code.document().findBlockByNumber(i))
                    format=QtGui.QTextBlockFormat()
                    format.setBackground(QColor(25,25,25))
                    cursor.setBlockFormat(format)



            BASIC_code.main()

            parsedfile = open("BasicCode.txt",'r')
            parsedcodelines = parsedfile.readlines()
            #print(parsedcodelines)            
            parsedfile.close()

            





            self.GEN_MC()

            mcfile= open("MachineCode.txt", 'r')
            mc_codelines=mcfile.readlines()
            mcfile.close()
            #print(mc_codelines)

           

            #print(len(mc_codelines))
            #print("len")
            #print(len(mc_codelines))
            if self.basic_code.toPlainText()=="":
                fg=""
                for idf in range(len(mc_codelines)):
                    if mc_codelines[idf] == '\n':
                        fg = mc_codelines[idf + 2:]
                        break

                for i in range(len(parsedcodelines)):
                    x=hex(i*4)


                    y = fg[i].find(' ')
                    y = fg[i][y+1:].rstrip()
                #z=(str(x)+"                                                     "+parsedcodelines[i].rstrip()+"                                                                "+mc_codelines[i+2].rstrip())
                #if len()>12
                    z = "     "+x+"\t\t\t\t"+parsedcodelines[i].rstrip()+"\t\t\t\t"+y
                    self.basic_code.append(z)



            num_lines=self.basic_code.document().blockCount()
            self.inst_num=num_lines
            self.endpc=self.inst_num*4
            self.steppointer=0
            self.breakpoint=-1
            self.breakpc=-1
            

            for i in range(num_lines):
                cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(i))
                format=QtGui.QTextBlockFormat()
                format.setBackground(QColor(25, 25, 25))
                cursor.setBlockFormat(format)


            cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int((PC.PC)/4)))
            format=QtGui.QTextBlockFormat()
            format.setBackground(QColor(204,255,153))
            cursor.setBlockFormat(format)

            #if self.knob==0:
            Commander_normal.initializereg()
            #elif self.knob==1:
            #    PipCommander.initializereg()
            self.CURRENT_VAL()

            file = QtCore.QFile('Memory_file.txt')
            file.open(QtCore.QIODevice.ReadOnly)
            stream = QtCore.QTextStream(file)
            self.address_code.setText(stream.readAll())
            file.close()
            return

        if currindex == 3:
            configme.breakflag = 0
            
            editorcodefile=open("codefromeditor.txt", 'w+')
            editorcode=self.editor_code.toPlainText()
            editorcodefile.write(editorcode)
            editorcodefile.close()
            #errormessage, errorline= error_detection.main()
        
            error, errorline = error_detector_unit.main()      # number of line to be colored : errorline, error: msg
            
            error=error.strip()
            num=self.editor_code.document().blockCount()
            if(error!="noerror"):
                self.panes.setCurrentIndex(1)


                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle(f"Error in command {errorline}")
                msg.setText(error)
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.exec_()
                return

            if(error=="noerror"):

                for i in range(num):
                    cursor=QtGui.QTextCursor(self.editor_code.document().findBlockByNumber(i))
                    format=QtGui.QTextBlockFormat()
                    format.setBackground(QColor(25,25,25))
                    cursor.setBlockFormat(format)



          #  exec(open(r"mcgenerator.py").read())  # generate the machine code into mc file
            BASIC_code.main()
            
            self.GEN_MC()
            PipCommander.run_button()
            self.PIP_OUT()
            return

        if(currindex==1 or currindex==0):
            configme.breakflag=1
            self.runflag=0
            self.console.clear()
            self.basic_code.clear()
           
            self.mcgenflag=0  
            self.runflag=0    
            self.inst_num=0
            self.steppointer=0
            self.breakpoint=-1
            self.RESET_IT()
            
        #palle= self.basic_code.palette();
        #color= QtCore.Qt.green
        #palle.setColor(QtGui.QPalette.base, color)
        #self.basic_code.setPalette(palle);
        return

    def dialogopener(self):
        filename=QtWidgets.QFileDialog.getOpenFileName(None,  'Open File' '/home/COAProject')
        
        if(filename[0]):
            file= open(filename[0], 'r')
            text=file.read()
            self. editor_code.setText(text)
            file.close()
        return

    ########################

    def GEN_MC(self):

         # Click Generate Machine Code Button

        file= open(r"mcgenerator.py",'r')
        mcgen_code=file.read()
        exec(mcgen_code)
        file.close()
        file = QtCore.QFile('Memory_file.txt')
        file.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(file)
        self.address_code.setText(stream.readAll())
        file.close()
        
    
        #file = QtCore.QFile('MachineCode.txt')
        #file.open(QtCore.QIODevice.ReadOnly)
        #stream = QtCore.QTextStream(file)
        #self.machine_code.setText(stream.readAll())
        #file.close()

         
        #file2 = QtCore.QFile('BasicCode.txt')
        #file2.open(QtCore.QIODevice.ReadOnly)
        #stream2 = QtCore.QTextStream(file2)
        #self.basic_code.setText(stream2.readAll())
        #file2.close()

        #if self.knob==0:
        Commander_normal.initializereg()
        #elif self.knob==1:
        #PipCommander.initializereg()
        self.CURRENT_VAL()


    def run_buttonclicked(self):
        
        
        if(self.runflag==1):
            return

        configme.breakflag=0
        
        if(PC.PC==self.endpc):
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Please Refrain")
            msg.setText("ALL INSTRUCTIONS HAVE BEEN RUN")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
            return

        if(self.breakpc==-1):
            
            self.runflag=1
            #runthread=threading.Thread(target=self.RUN_IT)
            #runthread.start()

            self.RUN_IT()
            #print("hskfh")
            #print("aslkfjflsajfaslkfjaslk;fjsalkfjlskfjlskdaf")


            for i in range(self.inst_num):
                cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(i))
                format=QtGui.QTextBlockFormat()
                format.setBackground(QColor(25, 25, 25))
                cursor.setBlockFormat(format)
            self.breakpc=-1

            if(PC.PC<self.endpc):
                cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
                format=QtGui.QTextBlockFormat()
                format.setBackground(QColor(204,255,153))
                cursor.setBlockFormat(format)
                
            self.runflag=0
            
            #return

        elif(self.breakpc!=-1):
            #print("hello")
            self.runflag=1
            while(PC.PC!=self.breakpc and PC.PC!=self.endpc and configme.breakflag==0):
                cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
                format=QtGui.QTextBlockFormat()
                format.setBackground(QColor(25, 25, 25))
                cursor.setBlockFormat(format)
                self.STEP_IT()
                QApplication.processEvents()
                if(PC.PC==self.endpc):
                    break
                cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
                format=QtGui.QTextBlockFormat()
                format.setBackground(QColor(204,255,153))
                cursor.setBlockFormat(format)
                QApplication.processEvents()
            self.breakpc=-1
            self.runflag=0
        file = QtCore.QFile('Console.txt')
        file.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(file)
        self.console.setText(stream.readAll())
        file.close()
            


    def stop(self):
        configme.breakflag=1
        self.runflag=0
        if(PC.PC<self.endpc):
            cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
            format=QtGui.QTextBlockFormat()
            format.setBackground(QColor(204,255,153))
            cursor.setBlockFormat(format)
        return

    def dump(self):
        if(self.runflag==1):
            return
        #print("helo")
        mcfile=open("MachineCode.txt",'r')
        mclines=mcfile.readlines()
        mcfile.close()
        self.console.clear()
        # self.console.append("\n")
        for idf in range(len(mclines)):
            if mclines[idf] == '\n':
                fg = mclines[idf+2:]
                break

        for i in range(self.inst_num):
            self.console.append(fg[i].rstrip())
        return

    def step_buttonclicked(self):
        #if self.knob==1:
        #    return
        if(self.runflag==1):
            return
        # if(self.runflag==1):
        #     msg=QtWidgets.QMessageBox()
        #     msg.setWindowTitle("Jyada Tez Mat chal")
        #     msg.setText("Beta pehle hi saara run kar chuka hoon")
        #     msg.setIcon(QtWidgets.QMessageBox.Critical)
        #     msg.exec_()
        #     return            
        if(PC.PC<self.endpc):
            #print(PC.PC)
            cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
            format=QtGui.QTextBlockFormat()
            format.setBackground(QColor(25, 25, 25))
            cursor.setBlockFormat(format)
            self.STEP_IT()
            if(PC.PC<self.endpc):
                cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
                format=QtGui.QTextBlockFormat()
                format.setBackground(QColor(204,255,153))
                cursor.setBlockFormat(format)

        else:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("PLEASE REFRAIN!")
            msg.setText("All instructions have been executed")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        file = QtCore.QFile('Console.txt')
        file.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(file)
        self.console.setText(stream.readAll())
        file.close()

    def prev_buttonclicked(self):
        #if self.knob ==1:
        #    return
        if(self.runflag==1):
            return
        if(PC.PC==0):
            return
        
        else:
            cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
            format=QtGui.QTextBlockFormat()
            format.setBackground(QColor(25, 25, 25))
            cursor.setBlockFormat(format)
            self.PREV_IT()
            cursor=QtGui.QTextCursor(self.basic_code.document().findBlockByNumber(int(PC.PC/4)))
            format=QtGui.QTextBlockFormat()
            format.setBackground(QColor(255,204,255))
            cursor.setBlockFormat(format)
        file = QtCore.QFile('Console.txt')
        file.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(file)
        self.console.setText(stream.readAll())

        file.close()


    def RUN_IT(self):       # Click Run Button
        #print("in runit")

        #if self.knob==0:
        Commander_normal.run_button()
        #elif self.knob==1:
        #    PipCommander.run_button()
        #    self.PIP_OUT()
        self.CURRENT_VAL()

        file = QtCore.QFile('Memory_file.txt')
        file.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(file)
        self.address_code.setText(stream.readAll())
        file.close()
        self.runflag=0
        return 

    def PIP_OUT(self):
        if self.editor_code.toPlainText() != "":
            self.lineEdit.setText(str(PipCommander.instructions_executed))
            self.lineEdit_2.setText(str(PipCommander.cycles))
            if PipCommander.instructions_executed==0:   ghf=0.0
            elif PipCommander.instructions_executed>0:  ghf="{:.2f}".format(PipCommander.cycles/PipCommander.instructions_executed)
            self.lineEdit_3.setText(str(ghf))
            self.lineEdit_4.setText(str(PipCommander.executed_information.data_transfer_instructs))
            self.lineEdit_5.setText(str(PipCommander.executed_information.alu_instructs))
            self.lineEdit_6.setText(str(PipCommander.executed_information.control_instructs))
            self.lineEdit_7.setText(str(PipCommander.executed_information.data_hazards))
            self.lineEdit_8.setText(str(PipCommander.executed_information.control_hazards))
            self.lineEdit_13.setText(str(PipCommander.executed_information.branch_mispredicts))
            self.lineEdit_14.setText(str(PipCommander.executed_information.stalls_control_hzs))
            self.lineEdit_15.setText(str(PipCommander.executed_information.stalls_data_hazs))
            self.lineEdit_16.setText(str(PipCommander.stalls))
            self.textEdit.setText("We have stored Branch-To Address for conditional as well as unconditional jump\n")
            self.textEdit.append("Branch To Address")
            self.textEdit.append(str(PipCommander.executed_information.branch_child))
            self.textEdit.append("\nBranch Taken  (Final value of 1-bit Branch predictor)")
            self.textEdit.append(str(PipCommander.executed_information.branch_taken))
            self.textEdit.append(f"\n\nRegisters having non-zero value finally:\n")
            for dfhj in range(32):
                if register_file.reg_address_to_value[dfhj]:    self.textEdit.append(f"x{dfhj}: {hex(register_file.reg_address_to_value[dfhj])}")
            self.textEdit.append(f'\n\n')
            file = QtCore.QFile('Memory_file.txt')
            file.open(QtCore.QIODevice.ReadOnly)
            stream = QtCore.QTextStream(file)
            self.textEdit.append(stream.readAll())
            file.close()
            self.textEdit_2.setText(f"Numbers represent: instruction number\n\nCycle number\t\tFetch\t\tDecode\t\tExecute\t\tMemAccess\tWriteBack")

            xf = 0
            xd = -1
            xe = -2
            xm = -3
            xw = -4
            x=0
            for i in executed_information.executed_info:
                x += 1
                if i[0]<0 and x>2:  self.textEdit_2.append(f"{x}\t\t\t--------------------------STALL----------------------------(M-E stall)")
                elif i[1]==-3 and not(23<=i[0]<=26):    self.textEdit_2.append(f"{x}\t\t\t--------------------------STALL----------------------------(E-D/M-D stall)")
                elif i[1]==-3 and 23<=i[0]<=26 and i[3]==-1:    self.textEdit_2.append(f"{x}\t\t\t--------------------------STALL----------------------------(E-D/M-D stall)")
                elif i[1]==-47:     self.textEdit_2.append(f"{x}\t\t\t--------------------------STALL----------------------------(branch-mispredict/cond jump)")
                else:
                    xf += 1
                    xd += 1
                    xe += 1
                    xm += 1
                    xw += 1
                    if xf==1:       self.textEdit_2.append(f"{x}\t\t\t1")
                    elif xd==1:     self.textEdit_2.append(f"{x}\t\t\t2\t\t1")
                    elif xe==1:     self.textEdit_2.append(f"{x}\t\t\t3\t\t2\t\t1")
                    elif xm==1:     self.textEdit_2.append(f"{x}\t\t\t4\t\t3\t\t2\t\t1")
                    elif xw==1:     self.textEdit_2.append(f"{x}\t\t\t5\t\t4\t\t3\t\t2\t\t1")
                    elif xw==PipCommander.instructions_executed:    self.textEdit_2.append(f"{x}\t\t\t\t\t\t\t\t\t\t\t{xw}")
                    elif xm==PipCommander.instructions_executed:    self.textEdit_2.append(f"{x}\t\t\t\t\t\t\t\t\t{xm}\t\t{xw}")
                    elif xe==PipCommander.instructions_executed:    self.textEdit_2.append(f"{x}\t\t\t\t\t\t\t{xe}\t\t{xm}\t\t{xw}")
                    elif xd==PipCommander.instructions_executed:    self.textEdit_2.append(f"{x}\t\t\t\t\t{xd}\t\t{xe}\t\t{xm}\t\t{xw}")
                    else:           self.textEdit_2.append(f"{x}\t\t\t{xf}\t\t{xd}\t\t{xe}\t\t{xm}\t\t{xw}")


        else:
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.textEdit_2.setText(f"Numbers represent: instruction number\n\nCycle number\t\tFetch\t\tDecode\t\tExecute\t\tMemAccess\tWriteBack")
            self.textEdit.setText("We have stored Branch-To Address for conditional as well as unconditional jump\n")
            self.lineEdit.setText("0")
            self.lineEdit_2.setText("0")
            self.lineEdit_3.setText("0.0")
            self.lineEdit_4.setText("0")
            self.lineEdit_5.setText("0")
            self.lineEdit_6.setText("0")
            self.lineEdit_7.setText("0")
            self.lineEdit_8.setText("0")
            self.lineEdit_13.setText("0")
            self.lineEdit_14.setText("0")
            self.lineEdit_15.setText("0")
            self.lineEdit_16.setText("0")


    def CURRENT_VAL(self):
        if self.choice==0:
            self.x0.setText(hex(register_file.load_from_register(0)))
            self.x1.setText(hex(register_file.load_from_register(1)))
            self.x2.setText(hex(register_file.load_from_register(2)))
            self.x3.setText(hex(register_file.load_from_register(3)))
            self.x4.setText(hex(register_file.load_from_register(4)))
            self.x5.setText(hex(register_file.load_from_register(5)))
            self.x6.setText(hex(register_file.load_from_register(6)))
            self.x7.setText(hex(register_file.load_from_register(7)))
            self.x8.setText(hex(register_file.load_from_register(8)))
            self.x9.setText(hex(register_file.load_from_register(9)))
            self.x10.setText(hex(register_file.load_from_register(10)))
            self.x11.setText(hex(register_file.load_from_register(11)))
            self.x12.setText(hex(register_file.load_from_register(12)))
            self.x13.setText(hex(register_file.load_from_register(13)))
            self.x14.setText(hex(register_file.load_from_register(14)))
            self.x15.setText(hex(register_file.load_from_register(15)))
            self.x16.setText(hex(register_file.load_from_register(16)))
            self.x17.setText(hex(register_file.load_from_register(17)))
            self.x18.setText(hex(register_file.load_from_register(18)))
            self.x19.setText(hex(register_file.load_from_register(19)))
            self.x20.setText(hex(register_file.load_from_register(20)))
            self.x21.setText(hex(register_file.load_from_register(21)))
            self.x22.setText(hex(register_file.load_from_register(22)))
            self.x23.setText(hex(register_file.load_from_register(23)))
            self.x24.setText(hex(register_file.load_from_register(24)))
            self.x25.setText(hex(register_file.load_from_register(25)))
            self.x26.setText(hex(register_file.load_from_register(26)))
            self.x27.setText(hex(register_file.load_from_register(27)))
            self.x28.setText(hex(register_file.load_from_register(28)))
            self.x29.setText(hex(register_file.load_from_register(29)))
            self.x30.setText(hex(register_file.load_from_register(30)))
            self.x31.setText(hex(register_file.load_from_register(31)))
            self.pc_edit.setText(hex(PC.PC))
        elif self.choice==1:
            self.x0.setText(str(int  (register_file.load_from_register(0))))
            self.x1.setText(str(int  (register_file.load_from_register(1))))
            self.x2.setText(str(int  (register_file.load_from_register(2))))
            self.x3.setText(str(int  (register_file.load_from_register(3))))
            self.x4.setText(str(int  (register_file.load_from_register(4))))
            self.x5.setText(str(int  (register_file.load_from_register(5))))
            self.x6.setText(str(int  (register_file.load_from_register(6))))
            self.x7.setText(str(int  (register_file.load_from_register(7))))
            self.x8.setText(str(int  (register_file.load_from_register(8))))
            self.x9.setText(str(int  (register_file.load_from_register(9))))
            self.x10.setText(str(int  (register_file.load_from_register(10))))
            self.x11.setText(str(int  (register_file.load_from_register(11))))
            self.x12.setText(str(int  (register_file.load_from_register(12))))
            self.x13.setText(str(int  (register_file.load_from_register(13))))
            self.x14.setText(str(int  (register_file.load_from_register(14))))
            self.x15.setText(str(int  (register_file.load_from_register(15))))
            self.x16.setText(str(int  (register_file.load_from_register(16))))
            self.x17.setText(str(int  (register_file.load_from_register(17))))
            self.x18.setText(str(int  (register_file.load_from_register(18))))
            self.x19.setText(str(int  (register_file.load_from_register(19))))
            self.x20.setText(str(int  (register_file.load_from_register(20))))
            self.x21.setText(str(int  (register_file.load_from_register(21))))
            self.x22.setText(str(int  (register_file.load_from_register(22))))
            self.x23.setText(str(int  (register_file.load_from_register(23))))
            self.x24.setText(str(int  (register_file.load_from_register(24))))
            self.x25.setText(str(int  (register_file.load_from_register(25))))
            self.x26.setText(str(int  (register_file.load_from_register(26))))
            self.x27.setText(str(int  (register_file.load_from_register(27))))
            self.x28.setText(str(int  (register_file.load_from_register(28))))
            self.x29.setText(str(int  (register_file.load_from_register(29))))
            self.x30.setText(str(int  (register_file.load_from_register(30))))
            self.x31.setText(str(int  (register_file.load_from_register(31))))
            self.pc_edit.setText(str(int  (PC.PC)))
        elif self.choice ==2:
            if register_file.load_from_register(0)in range(32,127):
                self.x0.setText(chr(register_file.load_from_register(0)))
            else:           self.x0.setText(hex(register_file.load_from_register(0)))
            if register_file.load_from_register(1)in range(32,127):
                self.x1.setText(chr(register_file.load_from_register(1)))
            else:           self.x1.setText(hex(register_file.load_from_register(1)))
            if register_file.load_from_register(2)in range(32,127):
                self.x2.setText(chr(register_file.load_from_register(2)))
            else:           self.x2.setText(hex(register_file.load_from_register(2)))
            if register_file.load_from_register(3)in range(32,127):
                self.x3.setText(chr(register_file.load_from_register(3)))
            else:           self.x3.setText(hex(register_file.load_from_register(3)))
            if register_file.load_from_register(4)in range(32,127):
                self.x4.setText(chr(register_file.load_from_register(4)))
            else:           self.x4.setText(hex(register_file.load_from_register(4)))
            if register_file.load_from_register(5)in range(32,127):
                self.x5.setText(chr(register_file.load_from_register(5)))
            else:           self.x5.setText(hex(register_file.load_from_register(5)))
            if register_file.load_from_register(6)in range(32,127):
                self.x6.setText(chr(register_file.load_from_register(6)))
            else:           self.x6.setText(hex(register_file.load_from_register(6)))
            if register_file.load_from_register(7)in range(32,127):
                self.x7.setText(chr(register_file.load_from_register(7)))
            else:           self.x7.setText(hex(register_file.load_from_register(7)))
            if register_file.load_from_register(8)in range(32,127):
                self.x8.setText(chr(register_file.load_from_register(8)))
            else:           self.x8.setText(hex(register_file.load_from_register(8)))
            if register_file.load_from_register(9)in range(32,127):
                self.x9.setText(chr(register_file.load_from_register(9)))
            else:           self.x9.setText(hex(register_file.load_from_register(9)))
            if register_file.load_from_register(10)in range(32,127):
                self.x10.setText(chr(register_file.load_from_register(10)))
            else:           self.x10.setText(hex(register_file.load_from_register(10)))
            if register_file.load_from_register(11)in range(32,127):
                self.x11.setText(chr(register_file.load_from_register(11)))
            else:           self.x11.setText(hex(register_file.load_from_register(11)))
            if register_file.load_from_register(12)in range(32,127):
                self.x12.setText(chr(register_file.load_from_register(12)))
            else:           self.x12.setText(hex(register_file.load_from_register(12)))
            if register_file.load_from_register(13)in range(32,127):
                self.x13.setText(chr(register_file.load_from_register(13)))
            else:           self.x13.setText(hex(register_file.load_from_register(13)))
            if register_file.load_from_register(14)in range(32,127):
                self.x14.setText(chr(register_file.load_from_register(14)))
            else:           self.x14.setText(hex(register_file.load_from_register(14)))
            if register_file.load_from_register(15)in range(32,127):
                self.x15.setText(chr(register_file.load_from_register(15)))
            else:           self.x15.setText(hex(register_file.load_from_register(15)))
            if register_file.load_from_register(16)in range(32,127):
                self.x16.setText(chr(register_file.load_from_register(16)))
            else:           self.x16.setText(hex(register_file.load_from_register(16)))
            if register_file.load_from_register(17)in range(32,127):
                self.x17.setText(chr(register_file.load_from_register(17)))
            else:           self.x17.setText(hex(register_file.load_from_register(17)))
            if register_file.load_from_register(18)in range(32,127):
                self.x18.setText(chr(register_file.load_from_register(18)))
            else:           self.x18.setText(hex(register_file.load_from_register(18)))
            if register_file.load_from_register(19)in range(32,127):
                self.x19.setText(chr(register_file.load_from_register(19)))
            else:           self.x19.setText(hex(register_file.load_from_register(19)))
            if register_file.load_from_register(20)in range(32,127):
                self.x20.setText(chr(register_file.load_from_register(20)))
            else:           self.x20.setText(hex(register_file.load_from_register(20)))
            if register_file.load_from_register(21)in range(32,127):
                self.x21.setText(chr(register_file.load_from_register(21)))
            else:           self.x21.setText(hex(register_file.load_from_register(21)))
            if register_file.load_from_register(22)in range(32,127):
                self.x22.setText(chr(register_file.load_from_register(22)))
            else:           self.x22.setText(hex(register_file.load_from_register(22)))
            if register_file.load_from_register(23)in range(32,127):
                self.x23.setText(chr(register_file.load_from_register(23)))
            else:           self.x23.setText(hex(register_file.load_from_register(23)))
            if register_file.load_from_register(24)in range(32,127):
                self.x24.setText(chr(register_file.load_from_register(24)))
            else:           self.x24.setText(hex(register_file.load_from_register(24)))
            if register_file.load_from_register(25)in range(32,127):
                self.x25.setText(chr(register_file.load_from_register(25)))
            else:           self.x25.setText(hex(register_file.load_from_register(25)))
            if register_file.load_from_register(26)in range(32,127):
                self.x26.setText(chr(register_file.load_from_register(26)))
            else:           self.x26.setText(hex(register_file.load_from_register(26)))
            if register_file.load_from_register(27)in range(32,127):
                self.x27.setText(chr(register_file.load_from_register(27)))
            else:           self.x27.setText(hex(register_file.load_from_register(27)))
            if register_file.load_from_register(28)in range(32,127):
                self.x28.setText(chr(register_file.load_from_register(28)))
            else:           self.x28.setText(hex(register_file.load_from_register(28)))
            if register_file.load_from_register(29)in range(32,127):
                self.x29.setText(chr(register_file.load_from_register(29)))
            else:           self.x29.setText(hex(register_file.load_from_register(29)))
            if register_file.load_from_register(30)in range(32,127):
                self.x30.setText(chr(register_file.load_from_register(30)))
            else:           self.x30.setText(hex(register_file.load_from_register(30)))
            if register_file.load_from_register(31)in range(32,127):
                self.x31.setText(chr(register_file.load_from_register(31))) 
            else:           self.x31.setText(hex(register_file.load_from_register(31)))
            self.pc_edit.setText(hex(PC.PC))


    def STEP_IT(self):
        Commander_normal.step_button()
        self.CURRENT_VAL()

        file = QtCore.QFile('Memory_file.txt')
        file.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(file)
        self.address_code.setText(stream.readAll())
        file.close()

    def RESET_IT(self):     # Click Reset Button  Please check once if the reset is fine
        self.runflag=0
        configme.breakflag=1
        #if self.knob ==0:
        Commander_normal.initializereg()
        #elif self.knob ==1:
        #    PipCommander.initializereg()
        self.CURRENT_VAL()

        self.basic_code.clear()
        
        self.console.clear()
        self.address_code.clear()
        PC.PC=0

    def PREV_IT(self):
        Commander_normal.previous_button()
        self.CURRENT_VAL()
        file = QtCore.QFile('Memory_file.txt')
        file.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(file)
        self.address_code.setText(stream.readAll())
        file.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    palette = QtGui.QPalette()
    palette.setColor(QPalette.Window, QColor(0,0,0))
    #palette.setColor(QPalette.Background,QColor(0,0,0))
    palette.setColor(QPalette.WindowText, QColor(0,159,255))        ######
    
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, QColor(255,128,0))
    palette.setColor(QPalette.Button, QColor(0, 0, 0))
    palette.setColor(QPalette.ButtonText,QColor(0,159,255) )        ########
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.showMinimized()
    sys.exit(app.exec_())
