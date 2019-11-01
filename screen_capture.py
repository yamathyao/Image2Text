from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QGuiApplication, QColor, QPen, QPainter
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, qAbs, QRect


class CaptureScreen(QWidget):
    """
    截屏： 使用时仅需直接new一个该实例即可出现全屏的截屏画面
    """
    load_pix_map = None
    screen_width = None
    screen_height = None
    is_mouse_pressed = None
    begin_pos = None
    end_pos = None
    capture_pix_map = None
    painter = QPainter()
    signal_complete_capture = pyqtSignal(QPixmap)

    def __init__(self):
        QWidget.__init__(self)
        self.init_window()
        self.load_background_pix_map()
        self.setCursor(Qt.CrossCursor)
        self.show()

    def init_window(self):
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowState(Qt.WindowActive | Qt.WindowFullScreen)

    def load_background_pix_map(self):
        # 截下当前屏幕的图像
        self.load_pix_map = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
        self.screen_width = self.load_pix_map.width()
        self.screen_height = self.load_pix_map.height()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.is_mouse_pressed = True
            self.begin_pos = event.pos()
        if event.button() == Qt.RightButton:
            self.close()
        return QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.is_mouse_pressed is True:
            self.end_pos = event.pos()
            self.update()
        return QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.end_pos = event.pos()
        self.is_mouse_pressed = False
        return QWidget.mouseReleaseEvent(self, event)

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.capture_pix_map is not None:
            self.signal_complete_capture.emit(self.capture_pix_map)
            self.close()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        self.painter.begin(self)
        shadow_color = QColor(0, 0, 0, 100)  # 阴影颜色设置
        self.painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine, Qt.FlatCap))  # 设置画笔
        self.painter.drawPixmap(0, 0, self.load_pix_map)  # 将背景图片画到窗体上
        self.painter.fillRect(self.load_pix_map.rect(), shadow_color)  # 画影罩效果
        if self.is_mouse_pressed:
            selected_rect = self.get_rect(self.begin_pos, self.end_pos)
            self.capture_pix_map = self.load_pix_map.copy(selected_rect)
            self.painter.drawPixmap(selected_rect.topLeft(), self.capture_pix_map)
            self.painter.drawRect(selected_rect)
        self.painter.end()  # 重绘结束

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.signal_complete_capture.emit(self.capture_pix_map)
            self.close()

    def get_rect(self, begin_point, end_point):
        width = qAbs(begin_point.x() - end_point.x())
        height = qAbs(begin_point.y() - end_point.y())
        x = begin_point.x() if begin_point.x() < end_point.x() else end_point.x()
        y = begin_point.y() if begin_point.y() < end_point.y() else end_point.y()
        select_rect = QRect(x, y, width, height)
        # 避免高或宽为零时拷贝截图有误
        # 以QQ截图为例，高或宽为零时默认为2
        if select_rect.width() == 0:
            select_rect.setWidth(1)
        if select_rect.height() == 0:
            select_rect.setHeight(1)
        return select_rect
