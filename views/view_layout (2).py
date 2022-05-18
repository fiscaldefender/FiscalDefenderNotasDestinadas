# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\view.layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 509)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../img/logonova_SO_escudo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(".\\../img/barra_superior.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(5, 6, 6, 6)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setMaxVisibleItems(1000)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.gridLayout_7.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(19)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(216, 238, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../img/salvar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 135, 79);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\../img/VisualizarXML_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(1, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setSizeIncrement(QtCore.QSize(2, 0))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.gridLayout_7.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setInputMethodHints(QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(169)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(36)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(21)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_6.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1036, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuConfigura_es = QtWidgets.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        self.menuVisualizar = QtWidgets.QMenu(self.menuConfigura_es)
        self.menuVisualizar.setObjectName("menuVisualizar")
        self.menuTela_Inicial = QtWidgets.QMenu(self.menuBar)
        self.menuTela_Inicial.setObjectName("menuTela_Inicial")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLogs = QtWidgets.QAction(MainWindow)
        self.actionLogs.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\../img/0_SincronismoNovo_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogs.setIcon(icon3)
        self.actionLogs.setObjectName("actionLogs")
        self.actionHome = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\../img/img_Emp_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon4)
        self.actionHome.setObjectName("actionHome")
        self.actionCertificados = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\../img/1448990550_icon-25-key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCertificados.setIcon(icon5)
        self.actionCertificados.setObjectName("actionCertificados")
        self.actionEmpresas = QtWidgets.QAction(MainWindow)
        self.actionEmpresas.setObjectName("actionEmpresas")
        self.menuVisualizar.addAction(self.actionLogs)
        self.menuConfigura_es.addAction(self.menuVisualizar.menuAction())
        self.menuConfigura_es.addAction(self.actionCertificados)
        self.menuConfigura_es.addAction(self.actionEmpresas)
        self.menuTela_Inicial.addAction(self.actionHome)
        self.menuBar.addAction(self.menuConfigura_es.menuAction())
        self.menuBar.addAction(self.menuTela_Inicial.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serviço Notas Destinadas"))
        self.groupBox.setTitle(_translate("MainWindow", "CONFIGURAÇÕES"))
        self.label_2.setText(_translate("MainWindow", "UF ESTADO"))
        self.label_7.setText(_translate("MainWindow", "EMPRESA"))
        self.label.setText(_translate("MainWindow", "CPF/CNPJ"))
        self.label_4.setText(_translate("MainWindow", "SENHA CERTIFICADO"))
        self.label_6.setText(_translate("MainWindow", "Nº SEQUENCIAL UNI"))
        self.label_3.setText(_translate("MainWindow", "URL CERTIFICADO"))
        self.pushButton.setText(_translate("MainWindow", "ENVIAR DADOS"))
        self.pushButton_4.setText(_translate("MainWindow", "CARREGAR CAMPOS"))
        self.pushButton_2.setText(_translate("MainWindow", "FORÇAR CONSULTA"))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID EMPRESA"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "EMPRESA"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CPF/CNPJ"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "UF_ESTADO"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "URL_CERTIFICADO"))
        self.label_5.setText(_translate("MainWindow", "Painel de Logs"))
        self.menuConfigura_es.setTitle(_translate("MainWindow", "Configurações"))
        self.menuVisualizar.setTitle(_translate("MainWindow", "Visualizar"))
        self.menuTela_Inicial.setTitle(_translate("MainWindow", "Tela Inicial"))
        self.actionLogs.setText(_translate("MainWindow", "Logs"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionCertificados.setText(_translate("MainWindow", "Certificados"))
        self.actionEmpresas.setText(_translate("MainWindow", "Empresas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
