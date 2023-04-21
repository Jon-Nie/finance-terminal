from PySide2.QtWidgets import QFrame

class SideBar(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumWidth(50)
        self.setMaximumWidth(150)
        self.setStyleSheet(
            """
            QFrame {
                background-color: grey
            }
            """
        )