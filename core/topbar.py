from PySide2.QtWidgets import QFrame

class TopBar(QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedHeight(40)
        self.setStyleSheet(
            """
            QFrame {
                background-color: darkgrey
            }
            """
        )