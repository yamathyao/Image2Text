import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import image2text

WINDOW_TITLE = 'Image2Text'
APP_ICON_URL = './assert/myicon.ico'


def run_with_title_bar():
    app = QApplication(sys.argv)
    image_frame = image2text.Image2Text()
    image_frame.setWindowTitle(WINDOW_TITLE)
    image_frame.setWindowIcon(QIcon(APP_ICON_URL))
    image_frame.mainwidget.setFocus()
    image_frame.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run_with_title_bar()
