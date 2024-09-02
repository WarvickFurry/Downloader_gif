import sys
import json
import os
from datetime import datetime, timedelta

from PySide6.QtWidgets import QDialog, QApplication, QMessageBox, QListWidgetItem, QAbstractItemView, QLineEdit
from PySide6.QtCore import Slot, Signal, Qt

from SQLite import db_init
from json_updater import JSONUpdater


from ui.settings.settings_dialog import Ui_Dialog_settings
#from custom_widgets import CustomWidgets

class Dialog_settings(QDialog):
    get_signal = Signal(int)
    save_button_signal = Signal(str)
    def __init__(self, parent=None):
        super(Dialog_settings, self).__init__(parent)

        self.db = db_init() #  init DB
        self.updater = JSONUpdater("config.json")

        self.ui = Ui_Dialog_settings()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        #if not os.path.exists("config.json"):
        self.default_settings()
        self.load_settings()

        self.blur()

        self.ui.auto_swap_tab_checkBox.stateChanged.connect(self.save_checkbox)
        self.ui.auto_swap_time_data_checkBox.stateChanged.connect(self.save_checkbox)
        self.ui.notifications_checkBox.stateChanged.connect(self.save_checkbox)
        self.ui.infoBox_checkBox.stateChanged.connect(self.save_checkbox)


        self.ui.soun_end_download_checkBox.stateChanged.connect(self.save_checkbox)
        self.ui.blur_token_checkBox.stateChanged.connect(self.save_checkbox)
        self.ui.blur_token_checkBox.stateChanged.connect(self.blur)




        self.ui.autosave_tab_settings_checkBox.stateChanged.connect(self.save_checkbox)
        self.ui.autosave_tab_minewindow_checkBox.stateChanged.connect(self.save_checkbox)
        self.ui.autosave_keep_checkBox.stateChanged.connect(self.save_checkbox)

        self.ui.spinBox.valueChanged.connect(self.auto_save_spinbox)
        self.ui.spinBox.valueChanged.connect(self.on_spinbox_value_changed)



        self.ui.save_setings.clicked.connect(self.save_settings)
        self.ui.save_setings.clicked.connect(self.emit_signal_save_button)
        self.ui.clear_pole_pushButton.clicked.connect(self.clear_pole)

################################__DB__######################################

        if self.ui.autosave_tab_settings_checkBox.isChecked():
            self.ui.tabWidget.currentChanged.connect(self.save_cur_index)

            #load settings
            saved_index = self.db.load_setting("tab_index")
            if saved_index is not None:
                self.ui.tabWidget.setCurrentIndex(int(saved_index))


    def save_cur_index(self,index):
        self.db.save_setting("tab_index",index)

########################### ОЗУ ###########################################






######################################################################

        # код добавления виджета
    #     self.ui.add_list_button.clicked.connect(self.add_widget)
    #     self.ui.clear_list_button.clicked.connect(self.clear_widget)
    #     self.my_widget_dict: dict[int, QListWidgetItem] = {}
    #     self.my_id_counter = 0
    #     self.signal_save_value = False
    #
    #     self.ui.tags_listWidget.setDragDropMode(QAbstractItemView.InternalMove)
    #     self.ui.tags_listWidget.currentRowChanged.connect(self.update_label)
    #     self.ui.tags_listWidget.model().rowsMoved.connect(self.update_indexes)
    #
    #
    #
    def clear_pole(self):
        self.ui.token_lineEdit.setText("")
        self.ui.token_group_lineEdit.setText("")
        self.ui.id_group_lineEdit.setText("")
        config = self.load_data_from_json()
        config["settings"]["user_token"] = self.ui.token_lineEdit.text()
        config["settings"]["group_token"] = self.ui.token_group_lineEdit.text()
        config["settings"]["id"] = self.ui.id_group_lineEdit.text()
        self.write_data_to_json(config)
    def emit_signal_save_button(self):
        self.save_button_signal.emit("clicked")
    def on_spinbox_value_changed(self, value):
        # Испускаем сигнал с новым значением spinbox
        self.get_signal.emit(value)
    #
    # @Slot()
    # def add_widget(self):
    #     widget = CustomWidgets(self.my_id_counter)
    #     my_item = QListWidgetItem(self.ui.tags_listWidget)
    #     my_item.setSizeHint(widget.sizeHint())
    #     self.my_widget_dict[widget.my_id] = my_item
    #     self.ui.tags_listWidget.addItem(my_item)
    #     self.ui.tags_listWidget.setItemWidget(my_item, widget)
    #     widget.delete.connect(self.delete_widget)
    #     self.my_id_counter += 1
    #
    # @Slot()
    # def clear_widget(self):
    #     self.ui.tags_listWidget.clear()
    #     self.my_widget_dict.clear()
    #     self.my_id_counter = 0
    #     self.update_label()
    #
    # @Slot()
    # def delete_widget(self):
    #     widget = self.sender()
    #     my_item = self.my_widget_dict[widget.my_id]
    #     self.ui.tags_listWidget.takeItem(self.ui.tags_listWidget.row(my_item))
    #     del self.my_widget_dict[widget.my_id]
    #     self.update_indexes()
    #
    # @Slot()
    # def update_label(self):
    #     current_row = self.ui.tags_listWidget.currentRow()
    #     self.ui.label_2.setText(f"Current Index: {current_row}")
    #
    # @Slot()
    # def update_indexes(self):
    #     for index in range(self.ui.tags_listWidget.count()):
    #         item = self.ui.tags_listWidget.item(index)
    #         widget = self.ui.tags_listWidget.itemWidget(item)
    #         if widget:
    #             widget.set_index(index)
    #     self.update_label()

    ##########################

    def blur(self):
        if self.ui.blur_token_checkBox.isChecked():
            self.ui.token_lineEdit.setEchoMode(QLineEdit.Password)
            self.ui.token_group_lineEdit.setEchoMode(QLineEdit.Password)
            self.ui.id_group_lineEdit.setEchoMode(QLineEdit.Password)
        else:
            self.ui.token_lineEdit.setEchoMode(QLineEdit.Normal)
            self.ui.token_group_lineEdit.setEchoMode(QLineEdit.Normal)
            self.ui.id_group_lineEdit.setEchoMode(QLineEdit.Normal)


    ###########################

    def default_settings(self):
        config = {
            "settings": {
                "user_token": "",
                "group_token": "",
                "id": "",
                "hour_add": 0,
                "auto_swap_tab_checkBox": True,
                "auto_swap_time_data_checkBox": True,
                "blur_token_checkBox": False,
                "notifications_checkBox": False,
                "sound_end_download_checkBox": True,
                "infoBox_checkBox": False,
                "autosave_tab_settings": False,
                "autosave_tab_minewindow": False,
                "autosave_keep": False
            },
            "combobox": {
                "0": "11:00",
                "1": "13:00",
                "2": "15:00",
                "3": "17:00",
                "4": "19:00",
                "5": "21:00",
                "6": "23:00",
                "7": "01:00"
            }
        }
        self.updater.update_json_file(config)





    def load_data_from_json(self):
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
                return config
        except FileNotFoundError:
            print("Файл не найден.")
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
        except Exception as e:
            print(f"Произошла другая ошибка: {e}")
        return {}

    def write_data_to_json(self, config):
        with open('config.json', 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=4)

    def load_settings(self):
        config = self.load_data_from_json()
        self.ui.token_lineEdit.setText(config["settings"]["user_token"])
        self.ui.token_group_lineEdit.setText(config["settings"]["group_token"])
        self.ui.id_group_lineEdit.setText(config["settings"]["id"])
        self.ui.auto_swap_tab_checkBox.setChecked(config["settings"]["auto_swap_tab_checkBox"])
        self.ui.auto_swap_time_data_checkBox.setChecked(config["settings"]["auto_swap_time_data_checkBox"])
        self.ui.blur_token_checkBox.setChecked(config["settings"]["blur_token_checkBox"])
        self.ui.notifications_checkBox.setChecked(config["settings"]["notifications_checkBox"])
        self.ui.soun_end_download_checkBox.setChecked(config["settings"]["sound_end_download_checkBox"])
        self.ui.infoBox_checkBox.setChecked(config["settings"]["infoBox_checkBox"])
        self.ui.spinBox.setValue(int(config["settings"]["hour_add"]))
        #auto save checkbox in db
        self.ui.autosave_tab_settings_checkBox.setChecked(config["settings"]["autosave_tab_settings"])
        self.ui.autosave_tab_minewindow_checkBox.setChecked(config["settings"]["autosave_tab_minewindow"])
        self.ui.autosave_keep_checkBox.setChecked(config["settings"]["autosave_keep"])


    def save_settings(self):
        config = self.load_data_from_json()
        config["settings"]["user_token"] = self.ui.token_lineEdit.text()
        config["settings"]["group_token"] = self.ui.token_group_lineEdit.text()
        config["settings"]["id"] = self.ui.id_group_lineEdit.text()
        self.write_data_to_json(config)
        QMessageBox.information(self, "Информация!", "Настройки сохранены!")


    def save_checkbox(self):
        config = self.load_data_from_json()
        config["settings"]["auto_swap_tab_checkBox"] = self.ui.auto_swap_tab_checkBox.isChecked()
        config["settings"]["auto_swap_time_data_checkBox"] = self.ui.auto_swap_time_data_checkBox.isChecked()
        config["settings"]["blur_token_checkBox"] = self.ui.blur_token_checkBox.isChecked()
        config["settings"]["notifications_checkBox"] = self.ui.soun_end_download_checkBox.isChecked()
        config["settings"]["sound_end_download_checkBox"] = self.ui.notifications_checkBox.isChecked()
        config["settings"]["infoBox_checkBox"] = self.ui.infoBox_checkBox.isChecked()
        config["settings"]["autosave_tab_settings"] = self.ui.autosave_tab_settings_checkBox.isChecked()
        config["settings"]["autosave_tab_minewindow"] = self.ui.autosave_tab_minewindow_checkBox.isChecked()
        config["settings"]["autosave_keep"] = self.ui.autosave_keep_checkBox.isChecked()
        self.write_data_to_json(config)

    def auto_save_spinbox(self):
        config1 = {
            "combobox": {
                "0": "11:00",
                "1": "13:00",
                "2": "15:00",
                "3": "17:00",
                "4": "19:00",
                "5": "21:00",
                "6": "23:00",
                "7": "01:00"
            }
        }
        config = self.load_data_from_json()
        config["settings"]["hour_add"] = self.ui.spinBox.value()
        hour_add = self.ui.spinBox.value()
        delta = timedelta(hours=hour_add)
        for key in config1['combobox']:
            default_time = datetime.strptime(config1['combobox'][key], "%H:%M")
            current_time = datetime.combine(datetime.today(), default_time.time())
            adjusted_time = current_time + delta
            config['combobox'][key] = adjusted_time.strftime("%H:%M")

        self.write_data_to_json(config)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dialog_settings()
    window.show()
    sys.exit(app.exec())
