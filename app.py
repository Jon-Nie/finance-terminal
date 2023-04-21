import sys
from PySide2.QtCore import QRect
from PySide2.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QMainWindow
)
from PySide2.QtGui import QFontDatabase
from core.topbar import TopBar
from core.sidebar import SideBar
from core.content import Content

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        QFontDatabase.addApplicationFont("fonts/Roboto-Medium.ttf")
        self.setWindowTitle("Finance Terminal")
        self.setGeometry(QRect(160, 60, 1600, 900))

        self.central = QFrame()
        self.setCentralWidget(self.central)

        self.topbar = TopBar()
        self.sidebar = SideBar()
        self.content = Content()

        self.layout = QGridLayout(self.central)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.topbar, 0, 0, 1, 2)
        self.layout.addWidget(self.sidebar, 1, 0, 1, 1)
        self.layout.addWidget(self.content, 1, 1, 1, 1)

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())