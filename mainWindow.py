# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'front.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 698)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mainContentStacked = QStackedWidget(self.centralwidget)
        self.mainContentStacked.setObjectName(u"mainContentStacked")
        self.mainContentStacked.setStyleSheet(u"")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.gridLayout = QGridLayout(self.Home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.all_companies_table = QTableView(self.Home)
        self.all_companies_table.setObjectName(u"all_companies_table")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_companies_table.sizePolicy().hasHeightForWidth())
        self.all_companies_table.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.all_companies_table.setFont(font)
        self.all_companies_table.setStyleSheet(u"")
        self.all_companies_table.setFrameShape(QFrame.Panel)
        self.all_companies_table.setLineWidth(0)
        self.all_companies_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.all_companies_table.setAutoScroll(True)
        self.all_companies_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.all_companies_table, 0, 0, 1, 1, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.Home)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_4 = QCheckBox(self.widget_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.widget_3)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy2.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.widget_3)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy2.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.checkBox_6)


        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)

        self.mainContentStacked.addWidget(self.Home)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_2 = QGridLayout(self.page_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.divInfoTableView = QTableView(self.page_4)
        self.divInfoTableView.setObjectName(u"divInfoTableView")
        self.divInfoTableView.setFont(font)
        self.divInfoTableView.setFrameShape(QFrame.NoFrame)
        self.divInfoTableView.setLineWidth(0)

        self.gridLayout_2.addWidget(self.divInfoTableView, 0, 0, 1, 1, Qt.AlignHCenter)

        self.widget_2 = QWidget(self.page_4)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy2.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.widget_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy2.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.widget_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy2.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.checkBox_2)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.mainContentStacked.addWidget(self.page_4)

        self.gridLayout_3.addWidget(self.mainContentStacked, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 50))
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.gridLayout_3.addWidget(self.widget_4, 1, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainContentStacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

