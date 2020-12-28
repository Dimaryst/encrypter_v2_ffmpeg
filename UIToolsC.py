# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI-Tools.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

font = QtGui.QFont()
font.setFamily("Courier New")
font.setPointSize(10)


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 250)
        MainWindow.setMinimumSize(QtCore.QSize(400, 250))
        MainWindow.setMaximumSize(QtCore.QSize(420, 250))
        MainWindow.setFont(font)
        MainWindow.setWhatsThis("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.select_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_file_button.setObjectName("select_file")
        self.gridLayout.addWidget(self.select_file_button, 0, 0, 1, 1)
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setObjectName("run_button")
        self.gridLayout.addWidget(self.run_button, 0, 1, 1, 2)
        self.command_selector = QtWidgets.QComboBox(self.centralwidget)
        self.command_selector.setCurrentText("")
        self.command_selector.setObjectName("command_selector")
        self.gridLayout.addWidget(self.command_selector, 1, 0, 1, 2)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.terminal = QtWidgets.QListWidget(self.centralwidget)
        self.terminal.setObjectName("terminal")
        self.verticalLayout.addWidget(self.terminal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 420, 22))
        self.menuBar.setObjectName("menuBar")
        self.help_menu = QtWidgets.QMenu(self.menuBar)
        self.help_menu.setObjectName("help_menu")
        self.help_menu.setFont(font)
        MainWindow.setMenuBar(self.menuBar)
        self.help_info = QtWidgets.QAction(MainWindow)
        self.help_info.setObjectName("help_info")
        self.commands_edit = QtWidgets.QAction(MainWindow)
        self.commands_edit.setObjectName("commands_edit")
        self.action_ffmpeg = QtWidgets.QAction(MainWindow)
        self.action_ffmpeg.setObjectName("action_ffmpeg")
        self.help_menu.addAction(self.action_ffmpeg)
        self.help_menu.addAction(self.commands_edit)
        self.help_menu.addAction(self.help_info)
        self.menuBar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tool for FFmpeg"))
        self.select_file_button.setText(_translate("MainWindow", "Выбрать видео... "))
        self.run_button.setText(_translate("MainWindow", "Запустить..."))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.help_menu.setTitle(_translate("MainWindow", "Настройки"))
        self.help_info.setText(_translate("MainWindow", "Справка"))
        self.commands_edit.setText(_translate("MainWindow", "Команды для ffmpeg..."))
        self.action_ffmpeg.setText(_translate("MainWindow", "Изменить путь к ffmpeg..."))
