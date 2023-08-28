# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\DataTableWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(932, 567)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableColumn_Match = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableColumn_Match.setFont(font)
        self.tableColumn_Match.setStyleSheet("#tableColumn_Match{\n"
"    border:1px solid #000;\n"
"    padding:10px;\n"
"}")
        self.tableColumn_Match.setAlignment(QtCore.Qt.AlignCenter)
        self.tableColumn_Match.setObjectName("tableColumn_Match")
        self.gridLayout.addWidget(self.tableColumn_Match, 0, 1, 1, 1)
        self.tableColumn_Time = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableColumn_Time.setFont(font)
        self.tableColumn_Time.setStyleSheet("#tableColumn_Time{\n"
"    border:1px solid #000;\n"
"    padding:10px;\n"
"}")
        self.tableColumn_Time.setAlignment(QtCore.Qt.AlignCenter)
        self.tableColumn_Time.setObjectName("tableColumn_Time")
        self.gridLayout.addWidget(self.tableColumn_Time, 0, 2, 1, 1)
        self.tableColumn_No = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableColumn_No.setFont(font)
        self.tableColumn_No.setStyleSheet("#tableColumn_No{\n"
"    border:1px solid #000;\n"
"    padding:10px;\n"
"}")
        self.tableColumn_No.setAlignment(QtCore.Qt.AlignCenter)
        self.tableColumn_No.setObjectName("tableColumn_No")
        self.gridLayout.addWidget(self.tableColumn_No, 0, 0, 1, 1)
        self.tableColumn_Platform = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableColumn_Platform.setFont(font)
        self.tableColumn_Platform.setStyleSheet("#tableColumn_Platform{\n"
"    border:1px solid #000;\n"
"    padding:10px;\n"
"}")
        self.tableColumn_Platform.setAlignment(QtCore.Qt.AlignCenter)
        self.tableColumn_Platform.setObjectName("tableColumn_Platform")
        self.gridLayout.addWidget(self.tableColumn_Platform, 0, 3, 1, 1)
        self.tableColumn_Tips = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableColumn_Tips.setFont(font)
        self.tableColumn_Tips.setStyleSheet("#tableColumn_Tips{\n"
"    border:1px solid #000;\n"
"    padding:10px;\n"
"}")
        self.tableColumn_Tips.setAlignment(QtCore.Qt.AlignCenter)
        self.tableColumn_Tips.setObjectName("tableColumn_Tips")
        self.gridLayout.addWidget(self.tableColumn_Tips, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.dataRecordsLayout = QtWidgets.QVBoxLayout()
        self.dataRecordsLayout.setContentsMargins(-1, 20, -1, 20)
        self.dataRecordsLayout.setObjectName("dataRecordsLayout")
        self.gridLayout.addLayout(self.dataRecordsLayout, 1, 0, 1, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableColumn_Match.setText(_translate("Form", "Match"))
        self.tableColumn_Time.setText(_translate("Form", "Time"))
        self.tableColumn_No.setText(_translate("Form", "No."))
        self.tableColumn_Platform.setText(_translate("Form", "Platform"))
        self.tableColumn_Tips.setText(_translate("Form", "Tips"))