# pyqt-chat-widget
PyQt widget for chatting app

## Requirements
* PyQt5

## How to Use
### By Cloning
1. git clone ~
2. python sample.py
### By pip
* python -m pip install pyqt-chat-widget

## Detailed Description
This is very basic chat widget which looks like this

![image](https://user-images.githubusercontent.com/55078043/216797180-84841611-7d57-42e2-9b1c-8219657859c8.png)

If you want to change the style of widgets, check out `ChatBrowser`, `Prompt` class in "chatWidget.py".

## Code Sample (for installing the package with pip)

```python
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QGuiApplication, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget

from pyqt_chat_widget.chatWidget import Prompt, ChatBrowser

# HighDPI support, for better quality overall
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

QApplication.setFont(QFont('Arial', 12))  # to be more visible


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('PyQt Chat Widget Example')
        self.__prompt = Prompt()
        self.__textEdit = self.__prompt.getTextEdit()
        self.__textEdit.setPlaceholderText('Write some text...')
        self.__textEdit.returnPressed.connect(self.__chat)
        self.__browser = ChatBrowser()
        lay = QVBoxLayout()
        lay.addWidget(self.__browser)
        lay.addWidget(self.__prompt)
        lay.setSpacing(0)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)
        self.resize(600, 400)

        self.__browser.showText('Hello!', True)
        self.__browser.showText('Hello! How may i help you?', False)

    def __chat(self):
        self.__browser.showText(self.__textEdit.text(), True)
        self.__browser.showText(f'You said "{self.__textEdit.text()}"', False)
        self.__textEdit.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
```

## TODO list
* show the profile icon
