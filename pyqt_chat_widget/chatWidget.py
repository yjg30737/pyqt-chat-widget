from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QWidget, QLabel, QLineEdit, QHBoxLayout


class ChatBrowser(QScrollArea):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        lay = QVBoxLayout()
        lay.setAlignment(Qt.AlignTop)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(lay)
        self.setWidget(widget)
        self.setWidgetResizable(True)

    def showText(self, text, user_f):
        chatLbl = QLabel(text)
        if user_f:
            chatLbl.setStyleSheet('QLabel { padding: 1em }')
            chatLbl.setAlignment(Qt.AlignRight)
        else:
            chatLbl.setStyleSheet('QLabel { background-color: #DDD; padding: 1em }')
            chatLbl.setAlignment(Qt.AlignLeft)
        self.widget().layout().addWidget(chatLbl)


class Prompt(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__lineEdit = QLineEdit()
        self.__lineEdit.setStyleSheet('QLineEdit { border: 1px solid #AAA; padding: 1em }')
        lay = QHBoxLayout()
        lay.addWidget(self.__lineEdit)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def getLineEdit(self):
        return self.__lineEdit


