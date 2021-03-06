# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gravity_calibration.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_gravity_calibration(object):
    def setupUi(self, gravity_calibration):
        gravity_calibration.setObjectName(_fromUtf8("gravity_calibration"))
        gravity_calibration.resize(238, 365)
        self.r_2 = QtGui.QToolBox(gravity_calibration)
        self.r_2.setGeometry(QtCore.QRect(10, 10, 220, 281))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.r_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r_2.setFont(font)
        self.r_2.setObjectName(_fromUtf8("r_2"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 220, 153))
        self.page.setObjectName(_fromUtf8("page"))
        self.but_load_observed = QtGui.QPushButton(self.page)
        self.but_load_observed.setGeometry(QtCore.QRect(10, 110, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_load_observed.setFont(font)
        self.but_load_observed.setObjectName(_fromUtf8("but_load_observed"))
        self.report_observed = QtGui.QTextEdit(self.page)
        self.report_observed.setGeometry(QtCore.QRect(5, 40, 210, 60))
        self.report_observed.setObjectName(_fromUtf8("report_observed"))
        self.lbl_observed = QtGui.QLabel(self.page)
        self.lbl_observed.setGeometry(QtCore.QRect(189, 0, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_observed.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Wingdings 2"))
        font.setPointSize(36)
        self.lbl_observed.setFont(font)
        self.lbl_observed.setPixmap(QtGui.QPixmap(_fromUtf8("../icons/error.png")))
        self.lbl_observed.setObjectName(_fromUtf8("lbl_observed"))
        self.r_2.addItem(self.page, _fromUtf8(""))
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 220, 153))
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.but_load_impedance = QtGui.QPushButton(self.page_4)
        self.but_load_impedance.setGeometry(QtCore.QRect(10, 110, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_load_impedance.setFont(font)
        self.but_load_impedance.setObjectName(_fromUtf8("but_load_impedance"))
        self.report_impedance = QtGui.QTextEdit(self.page_4)
        self.report_impedance.setGeometry(QtCore.QRect(5, 40, 210, 60))
        self.report_impedance.setObjectName(_fromUtf8("report_impedance"))
        self.lbl_imped = QtGui.QLabel(self.page_4)
        self.lbl_imped.setGeometry(QtCore.QRect(189, 0, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_imped.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Wingdings 2"))
        font.setPointSize(36)
        self.lbl_imped.setFont(font)
        self.lbl_imped.setObjectName(_fromUtf8("lbl_imped"))
        self.r_2.addItem(self.page_4, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 220, 153))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.radio_gamma = QtGui.QRadioButton(self.page_2)
        self.radio_gamma.setGeometry(QtCore.QRect(20, 10, 161, 16))
        self.radio_gamma.setObjectName(_fromUtf8("radio_gamma"))
        self.radio_expo = QtGui.QRadioButton(self.page_2)
        self.radio_expo.setGeometry(QtCore.QRect(20, 37, 161, 16))
        self.radio_expo.setObjectName(_fromUtf8("radio_expo"))
        self.radio_power = QtGui.QRadioButton(self.page_2)
        self.radio_power.setGeometry(QtCore.QRect(20, 64, 161, 16))
        self.radio_power.setObjectName(_fromUtf8("radio_power"))
        self.radio_friction = QtGui.QRadioButton(self.page_2)
        self.radio_friction.setGeometry(QtCore.QRect(20, 91, 161, 16))
        self.radio_friction.setObjectName(_fromUtf8("radio_friction"))
        self.lbl_par = QtGui.QLabel(self.page_2)
        self.lbl_par.setGeometry(QtCore.QRect(189, 0, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_par.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Wingdings 2"))
        font.setPointSize(36)
        self.lbl_par.setFont(font)
        self.lbl_par.setObjectName(_fromUtf8("lbl_par"))
        self.r_2.addItem(self.page_2, _fromUtf8(""))
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 220, 153))
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.but_choose_output_name = QtGui.QPushButton(self.page_5)
        self.but_choose_output_name.setGeometry(QtCore.QRect(226, 140, 140, 25))
        self.but_choose_output_name.setObjectName(_fromUtf8("but_choose_output_name"))
        self.report_output = QtGui.QTextEdit(self.page_5)
        self.report_output.setGeometry(QtCore.QRect(5, 40, 210, 60))
        self.report_output.setObjectName(_fromUtf8("report_output"))
        self.but_select_output = QtGui.QPushButton(self.page_5)
        self.but_select_output.setGeometry(QtCore.QRect(10, 110, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_select_output.setFont(font)
        self.but_select_output.setObjectName(_fromUtf8("but_select_output"))
        self.lbl_output = QtGui.QLabel(self.page_5)
        self.lbl_output.setGeometry(QtCore.QRect(189, 0, 31, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lbl_output.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Wingdings 2"))
        font.setPointSize(36)
        self.lbl_output.setFont(font)
        self.lbl_output.setObjectName(_fromUtf8("lbl_output"))
        self.r_2.addItem(self.page_5, _fromUtf8(""))
        self.lbl_funding2 = QtGui.QLabel(gravity_calibration)
        self.lbl_funding2.setGeometry(QtCore.QRect(100, 337, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_funding2.setFont(font)
        self.lbl_funding2.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_funding2.setObjectName(_fromUtf8("lbl_funding2"))
        self.progressbar = QtGui.QProgressBar(gravity_calibration)
        self.progressbar.setEnabled(True)
        self.progressbar.setGeometry(QtCore.QRect(10, 336, 211, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressbar.setPalette(palette)
        self.progressbar.setProperty("value", 0)
        self.progressbar.setTextVisible(True)
        self.progressbar.setObjectName(_fromUtf8("progressbar"))
        self.lbl_funding1 = QtGui.QLabel(gravity_calibration)
        self.lbl_funding1.setGeometry(QtCore.QRect(12, 338, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lbl_funding1.setFont(font)
        self.lbl_funding1.setObjectName(_fromUtf8("lbl_funding1"))
        self.but_calibrate_gravity = QtGui.QPushButton(gravity_calibration)
        self.but_calibrate_gravity.setGeometry(QtCore.QRect(10, 298, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_calibrate_gravity.setFont(font)
        self.but_calibrate_gravity.setObjectName(_fromUtf8("but_calibrate_gravity"))
        self.progressbar.raise_()
        self.r_2.raise_()
        self.lbl_funding2.raise_()
        self.lbl_funding1.raise_()
        self.but_calibrate_gravity.raise_()

        self.retranslateUi(gravity_calibration)
        self.r_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(gravity_calibration)

    def retranslateUi(self, gravity_calibration):
        gravity_calibration.setWindowTitle(_translate("gravity_calibration", "Calibrate gravity model", None))
        self.but_load_observed.setText(_translate("gravity_calibration", "Load observed matrix", None))
        self.report_observed.setHtml(_translate("gravity_calibration", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Natrix: NOT loaded</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Zones: 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Total demand: 0</span></p></body></html>", None))
        self.r_2.setItemText(self.r_2.indexOf(self.page), _translate("gravity_calibration", "Observed Matrix", None))
        self.but_load_impedance.setText(_translate("gravity_calibration", "Impedance matrix", None))
        self.report_impedance.setHtml(_translate("gravity_calibration", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Matrix: NOT loaded</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Dimensions: 0</span></p></body></html>", None))
        self.lbl_imped.setText(_translate("gravity_calibration", "O", None))
        self.r_2.setItemText(self.r_2.indexOf(self.page_4), _translate("gravity_calibration", "Impedance matrix", None))
        self.radio_gamma.setText(_translate("gravity_calibration", "Gamma Function", None))
        self.radio_expo.setText(_translate("gravity_calibration", "Negative Exponential", None))
        self.radio_power.setText(_translate("gravity_calibration", "Inverse Power", None))
        self.radio_friction.setText(_translate("gravity_calibration", "Friction Factors", None))
        self.lbl_par.setText(_translate("gravity_calibration", "O", None))
        self.r_2.setItemText(self.r_2.indexOf(self.page_2), _translate("gravity_calibration", "Model", None))
        self.but_choose_output_name.setText(_translate("gravity_calibration", "Choose Output", None))
        self.report_output.setHtml(_translate("gravity_calibration", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</span></p></body></html>", None))
        self.but_select_output.setText(_translate("gravity_calibration", "Select Output", None))
        self.lbl_output.setText(_translate("gravity_calibration", "O", None))
        self.r_2.setItemText(self.r_2.indexOf(self.page_5), _translate("gravity_calibration", "Outputs", None))
        self.lbl_funding2.setText(_translate("gravity_calibration", " www.ipea.gov.br", None))
        self.lbl_funding1.setText(_translate("gravity_calibration", "Partially funded by", None))
        self.but_calibrate_gravity.setText(_translate("gravity_calibration", "Calibrate Gravity Model", None))

