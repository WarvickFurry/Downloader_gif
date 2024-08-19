from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from ui.settings.widget_category import Ui_category_list_widget

class CustomWidgets(QWidget):
    delete = Signal()

    def __init__(self, idw: int, parent=None):
        super(CustomWidgets, self).__init__(parent)
        self.ui = Ui_category_list_widget()
        self.ui.setupUi(self)
        self.my_id = idw
        self.ui.label_2.setText(str(self.my_id))
        self.ui.remove_widget.clicked.connect(self.delete)

    def set_index(self, index):
        self.my_id = index
        self.ui.label_2.setText(str(self.my_id))
