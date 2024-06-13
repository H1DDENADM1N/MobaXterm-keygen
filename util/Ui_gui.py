# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_gui(object):
    def setupUi(self, gui):
        if not gui.objectName():
            gui.setObjectName(u"gui")
        gui.resize(379, 268)
        self.centralwidget = QWidget(gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_Name = QLabel(self.centralwidget)
        self.label_Name.setObjectName(u"label_Name")

        self.horizontalLayout_4.addWidget(self.label_Name)

        self.lineEdit_Name = QLineEdit(self.centralwidget)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")
        self.lineEdit_Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Name.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_Name)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_License = QLabel(self.centralwidget)
        self.label_License.setObjectName(u"label_License")

        self.horizontalLayout_3.addWidget(self.label_License)

        self.comboBox_License = QComboBox(self.centralwidget)
        self.comboBox_License.setObjectName(u"comboBox_License")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_License.sizePolicy().hasHeightForWidth())
        self.comboBox_License.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.comboBox_License)

        self.label_Users = QLabel(self.centralwidget)
        self.label_Users.setObjectName(u"label_Users")

        self.horizontalLayout_3.addWidget(self.label_Users)

        self.spinBox_Users = QSpinBox(self.centralwidget)
        self.spinBox_Users.setObjectName(u"spinBox_Users")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBox_Users.sizePolicy().hasHeightForWidth())
        self.spinBox_Users.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.spinBox_Users)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_Version = QLabel(self.centralwidget)
        self.label_Version.setObjectName(u"label_Version")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_Version.sizePolicy().hasHeightForWidth())
        self.label_Version.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_Version)

        self.pushButton_GetVersionfromFile = QPushButton(self.centralwidget)
        self.pushButton_GetVersionfromFile.setObjectName(u"pushButton_GetVersionfromFile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_GetVersionfromFile.sizePolicy().hasHeightForWidth())
        self.pushButton_GetVersionfromFile.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.pushButton_GetVersionfromFile)

        self.label_Major = QLabel(self.centralwidget)
        self.label_Major.setObjectName(u"label_Major")

        self.horizontalLayout_2.addWidget(self.label_Major)

        self.spinBox_Major = QSpinBox(self.centralwidget)
        self.spinBox_Major.setObjectName(u"spinBox_Major")
        sizePolicy1.setHeightForWidth(self.spinBox_Major.sizePolicy().hasHeightForWidth())
        self.spinBox_Major.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.spinBox_Major)

        self.label_Minor = QLabel(self.centralwidget)
        self.label_Minor.setObjectName(u"label_Minor")

        self.horizontalLayout_2.addWidget(self.label_Minor)

        self.spinBox_Minor = QSpinBox(self.centralwidget)
        self.spinBox_Minor.setObjectName(u"spinBox_Minor")
        sizePolicy1.setHeightForWidth(self.spinBox_Minor.sizePolicy().hasHeightForWidth())
        self.spinBox_Minor.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.spinBox_Minor)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_Activate = QPushButton(self.centralwidget)
        self.pushButton_Activate.setObjectName(u"pushButton_Activate")
        sizePolicy3.setHeightForWidth(self.pushButton_Activate.sizePolicy().hasHeightForWidth())
        self.pushButton_Activate.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.pushButton_Activate)


        self.verticalLayout.addLayout(self.horizontalLayout)

        gui.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(gui)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 379, 21))
        gui.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(gui)
        self.statusbar.setObjectName(u"statusbar")
        gui.setStatusBar(self.statusbar)

        self.retranslateUi(gui)

        QMetaObject.connectSlotsByName(gui)
    # setupUi

    def retranslateUi(self, gui):
        gui.setWindowTitle(QCoreApplication.translate("gui", u"MobaXterm Keygen", None))
        self.label_Name.setText(QCoreApplication.translate("gui", u"Name:", None))
        self.lineEdit_Name.setPlaceholderText(QCoreApplication.translate("gui", u"Default Name", None))
        self.label_License.setText(QCoreApplication.translate("gui", u"License:", None))
        self.label_Users.setText(QCoreApplication.translate("gui", u"Users:", None))
        self.label_Version.setText(QCoreApplication.translate("gui", u"Version:", None))
        self.pushButton_GetVersionfromFile.setText(QCoreApplication.translate("gui", u"Get Version from File", None))
        self.label_Major.setText(QCoreApplication.translate("gui", u"Major:", None))
        self.label_Minor.setText(QCoreApplication.translate("gui", u"Minor:", None))
        self.pushButton_Activate.setText(QCoreApplication.translate("gui", u"Activate", None))
    # retranslateUi

