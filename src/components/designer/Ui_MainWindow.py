# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/components/designer/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioNavigatorLayout = QtWidgets.QHBoxLayout()
        self.radioNavigatorLayout.setObjectName("radioNavigatorLayout")
        self.verticalLayout.addLayout(self.radioNavigatorLayout)
        self.navButtonsLayout = QtWidgets.QHBoxLayout()
        self.navButtonsLayout.setObjectName("navButtonsLayout")
        self.buttonBackward = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBackward.setObjectName("buttonBackward")
        self.navButtonsLayout.addWidget(self.buttonBackward)
        self.buttonForward = QtWidgets.QPushButton(self.centralwidget)
        self.buttonForward.setObjectName("buttonForward")
        self.navButtonsLayout.addWidget(self.buttonForward)
        self.verticalLayout.addLayout(self.navButtonsLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabImage = QtWidgets.QWidget()
        self.tabImage.setObjectName("tabImage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabImage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelImage = QtWidgets.QLabel(self.tabImage)
        self.labelImage.setObjectName("labelImage")
        self.gridLayout_2.addWidget(self.labelImage, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabImage, "")
        self.tabMetadata = QtWidgets.QWidget()
        self.tabMetadata.setObjectName("tabMetadata")
        self.tabWidget.addTab(self.tabMetadata, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 18))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Viewer"))
        self.buttonBackward.setText(_translate("MainWindow", "Previous"))
        self.buttonForward.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImage), _translate("MainWindow", "Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMetadata), _translate("MainWindow", "Metadata"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
