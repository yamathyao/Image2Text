from PyQt5 import QtCore, QtWidgets


class UiImage2textWidget(object):
    def setup_ui(self, image2text_widget):
        self.pushButtonCapture = QtWidgets.QPushButton(image2text_widget)
        self.pushButtonOpen = QtWidgets.QPushButton(image2text_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.textEdit = QtWidgets.QTextEdit(image2text_widget)
        self.verticalLayout = QtWidgets.QVBoxLayout(image2text_widget)
        image2text_widget.setObjectName('image2textWidget')
        image2text_widget.resize(611, 330)
        self.verticalLayout.setObjectName('verticalLayout')
        self.textEdit.setObjectName('textEdit')
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.pushButtonOpen.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonOpen.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonOpen.setObjectName('pushButtonOpen')
        self.horizontalLayout.addWidget(self.pushButtonOpen)
        self.pushButtonCapture.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonCapture.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonCapture.setObjectName('pushButtonCapture')
        self.horizontalLayout.addWidget(self.pushButtonCapture)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.translate_ui(image2text_widget)
        QtCore.QMetaObject.connectSlotsByName(image2text_widget)

    def translate_ui(self, image2text_widget):
        _translate = QtCore.QCoreApplication.translate
        image2text_widget.setWindowTitle(_translate('image2text_widget', 'Form'))
        self.pushButtonOpen.setText(_translate('image2text_widget', 'Open'))
        self.pushButtonCapture.setText(_translate('image2text_widget', 'cap'))
