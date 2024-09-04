import sys
import os
import os.path
import subprocess
import requests
import json

import vk_api
from datetime import datetime, timedelta, date

from var import tag_sorting
from winsound import SND_ALIAS, PlaySound

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QThread, Signal, QTimer, Qt ,QFile, QTextStream
#from PySide6.QtGui import QMovie

from ui.mine import Ui_MainWindow
from Test import Dialog_settings

from SQLite import db_init


class download_link(QThread):
    finished = Signal()

    def __init__(self, link):
        super().__init__()
        self.sort_system = tag_sorting()
        self.link = link

    def run(self):
        try:
            self.sort_system.download_link_gif(self.link)
        except Exception as e:
            print(f"Error in download_link_gif: {e}")


class DownloadThread(QThread):
    progress = Signal(int)

    def __init__(self, url, filename):
        super().__init__()
        self.url = url
        self.filename = filename

    def run(self):
        try:
            os.makedirs("temp", exist_ok=True)
            filepath = os.path.join("temp", self.filename)

            with open(filepath, 'wb') as f:
                with requests.get(self.url, stream=True) as r:
                    r.raise_for_status()
                    totalsize = int(r.headers.get('content-length', 0))
                    downloaded = 0
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            percent = int(downloaded * 100 / totalsize)
                            self.progress.emit(percent)

            self.finished.emit()

        except requests.RequestException as e:
            print(f"Network error during download: {e}")
        except OSError as e:
            print(f"File operation error: {e}")
        except Exception as e:
            print(f"Unexpected error in DownloadThread: {e}")


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Dialog_settings = Dialog_settings()
        self.source_url = None

        self.load_time_in_set_combobox()
        self.db = db_init()  # init DB




        if not os.path.exists("config.json"):
            self.Dialog_settings.default_settings()

        self.Dialog_settings.get_signal.connect(self.load_time_in_set_combobox)
        self.Dialog_settings.save_button_signal.connect(self.get_id)

        self.ui.download_button.clicked.connect(self.g_link)
        self.ui.test_pushButton.clicked.connect(self.open_temp_folder)
        self.ui.keep.clicked.connect(self.toggle_always_on_top)

        self.Dialog_settings.ui.pushButton_minecraft.clicked.connect(self.set_style)


        self.ui.settings.clicked.connect(self.open_settings)
        self.ui.put_aside_pushButton.clicked.connect(self.posting)
        self.ui.set_date.setDate(date.today())
        self.ui.set_date.setCalendarPopup(True)


        self.ui.label_2.setOpenExternalLinks(True)





        # Переменная для хранения предыдущего выбранного времени
        self.previous_time = None
        # Переменная для отслеживания переключений дней
        self.days_added = 0

        self.ui.lineEdit_.returnPressed.connect(self.g_link)

        self.a = 0

        self.get_id()





##########################__DB__#####################################


        if self.Dialog_settings.ui.autosave_keep_checkBox.isChecked():
            self.ui.keep.clicked.connect(self.save_cur_bool)

            saved_bool = self.db.load_setting("mine_keep_bool")
            if saved_bool is not None:
                self.ui.keep.setChecked(self.str_to_bool("True"))


        if self.Dialog_settings.ui.autosave_tab_minewindow_checkBox.isChecked():
            self.ui.tabWidget.currentChanged.connect(self.save_cur_tab_index)

            saved_index = self.db.load_setting("mine_tab_cur_index")
            if saved_index is not None:
                self.ui.tabWidget.setCurrentIndex(int(saved_index))
        else:
            self.ui.tabWidget.setCurrentIndex(0)

    def str_to_bool(self, s):
        return s.lower() in ('true', '1', 'yes')

    def save_cur_bool(self, s_boolian):
        self.db.save_setting("mine_keep_bool", s_boolian)

    def save_cur_tab_index(self, index):
        self.db.save_setting("mine_tab_cur_index", index)

#################################__Style__#####################################
    def set_style(self):
        self.load_style("ui/style/mine.qss")

    def load_style(self, style_file):
        file = QFile(style_file)
        if not file.open(QFile.ReadOnly | QFile.Text):
            print("Не удалось открыть файл стилей")
            return

        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())



######################################################################



#####################################################################


##################### данные для вк апи ##############################
    def get_id(self):
        config = self.load_data_from_json()
        if config["settings"]["group_token"] != "":
            try:
                self.group_token = config["settings"]["group_token"]
                self.group_id, self.group_screen_name = self.get_group_info()
                config["settings"]["id"] = str(self.group_id)
                self.write_data_to_json(config)
                self.Dialog_settings.load_settings()
            except Exception as e:
                print(f"Error in get_id: {e}")

    def toggle_always_on_top(self):
        try:
            if self.ui.keep.isChecked():
                self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
            else:
                self.setWindowFlag(Qt.WindowStaysOnTopHint, False)
            self.show()
        except Exception as e:
            print(f"Error in toggle_always_on_top: {e}")

    ############# start functions posting ################

    def posting(self):
        try:
            self.schedule_post()
            if self.Dialog_settings.ui.auto_swap_time_data_checkBox.isChecked():
                self.auto_set_data_ttime()
        except Exception as e:
            print(f"Error in posting: {e}")

    ################# start func upload post in usege vk_api ###########################

    def get_group_info(self):
        try:
            # Устанавливаем соединение с VK, используя групповой токен
            vk_session = vk_api.VkApi(token=self.group_token)
            vk = vk_session.get_api()

            # Получаем информацию о группе, используя токен
            group_info = vk.groups.getById()  # Не указываем group_ids, чтобы использовать токен
            if group_info:
                group_id = group_info[0]['id']
                group_screen_name = group_info[0]['screen_name']
                return group_id, group_screen_name
            else:
                raise ValueError("Не удалось получить информацию о группе. Проверьте правильность токена доступа.")
        except vk_api.exceptions.VkApiError as e:
            print(f"VK API error in get_group_info: {e}")
            self.Dialog_settings.clear_pole()
            self.show_warning()
            raise
        except Exception as e:
            print(f"Unexpected error in get_group_info: {e}")
            raise

    def upload_gif_as_document(self):
        try:
            # Устанавливаем соединение с VK с использованием группового токена
            vk_session_group = vk_api.VkApi(token=self.group_token)
            vk_group = vk_session_group.get_api()

            # Получаем сервер для загрузки документа (указываем group_id)
            upload_server = vk_group.docs.getWallUploadServer(group_id=self.group_id)

            # Загружаем файл на сервер
            with open(r"temp\equestria.gif", "rb") as gif_file:
                response = requests.post(upload_server['upload_url'], files={'file': gif_file})
                result = response.json()

            # Проверяем успешность загрузки
            if 'file' not in result:
                raise Exception(f"Ошибка загрузки файла: {result}")

            # Сохраняем документ на сервере ВКонтакте
            saved_doc = vk_group.docs.save(file=result['file'], title="equestria.gif", tags=[])

            # Формируем вложение
            doc = saved_doc['doc']
            attachment = f"doc{doc['owner_id']}_{doc['id']}"
            return attachment

        except vk_api.exceptions.VkApiError as e:
            print(f"VK API error in upload_gif_as_document: {e}")
        except requests.RequestException as e:
            print(f"Network error during GIF upload: {e}")
        except OSError as e:
            print(f"File operation error: {e}")
        except Exception as e:
            print(f"Unexpected error in upload_gif_as_document: {e}")

    def schedule_post(self):
        try:
            # Получаем введенные данные
            selected_date = self.ui.set_date.date().toPython()
            selected_time_str = self.ui.set_time.currentText()
            selected_time = datetime.strptime(selected_time_str, "%H:%M").time()

            # Объединяем дату и время
            selected_datetime = datetime.combine(selected_date, selected_time)
            timestamp = int(selected_datetime.timestamp())

            # Получаем текст с тегами
            tags = self.ui.text_autTags.toPlainText()

            # Устанавливаем соединение с VK с использованием группового токена
            vk_session_group = vk_api.VkApi(token=self.group_token)
            vk_group = vk_session_group.get_api()

            # Загружаем GIF как документ и получаем вложение (используем групповой токен)
            attachment = self.upload_gif_as_document()

            # Формируем текст поста
            post_text = f"{tags}"

            # Публикуем пост с отложенной датой от имени группы с указанием источника
            vk_group.wall.post(
                owner_id=-self.group_id,  # Знак минус перед group_id указывает, что пост идет от имени группы
                from_group=1,  # Публикация от имени группы
                message=post_text,
                attachments=attachment,
                publish_date=timestamp,
                copyright=self.source_url  # Указание на источник поста
            )
            self.ui.text_autTags.setText("")

            self.ui.webEngineView.setUrl("")
            if self.Dialog_settings.ui.notifications_checkBox.isChecked():
                PlaySound("SystemExclamation", SND_ALIAS)

            if self.Dialog_settings.ui.infoBox_checkBox.isChecked():
                QMessageBox.information(self, "Информация!", "Пост отложен!")

        except vk_api.exceptions.VkApiError as e:
            print(f"VK API error in schedule_post: {e}")
        except Exception as e:
            print(f"Unexpected error in schedule_post: {e}")

    ################# end func upload post in usege vk_api ###########################
    def show_warning(self):
        # Создаем экземпляр QMessageBox
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle('Ошибка')
        msg_box.setText('Проверьте правильность токена!')

        # Устанавливаем флаги окна
        msg_box.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        # Добавляем кнопки
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Показ сообщения и обработка ответа
        reply = msg_box.exec()

        if reply == QMessageBox.Ok:
            print("OK button pressed")
        else:
            print("Cancel button pressed")

    def check_time(self):
        try:
            # Получаем выбранное время из combobox
            selected_time_str = self.ui.set_time.currentText()
            selected_time = datetime.strptime(selected_time_str, "%H:%M")

            # Если это не первый выбор, проверяем, нужно ли добавить день
            if self.previous_time is not None:
                if selected_time < self.previous_time:
                    self.days_added += 1
                    new_date = self.ui.set_date.date().toPython() + timedelta(days=1)
                    self.ui.set_date.setDate(new_date)

            # Обновляем предыдущее время
            self.previous_time = selected_time
        except Exception as e:
            print(f"Error in check_time: {e}")

    def auto_set_data_ttime(self):
        try:
            max_size = self.ui.set_time.count()
            self.timebox_index = self.ui.set_time.currentIndex()
            self.set_time()
            if self.timebox_index < max_size - 1:
                self.timebox_index += 1
                if self.timebox_index != max_size:
                    self.ui.set_time.setCurrentIndex(self.timebox_index)
            else:
                self.timebox_index = 0
                self.ui.set_time.setCurrentIndex(self.timebox_index)
            self.check_time()

            if self.Dialog_settings.ui.auto_swap_tab_checkBox.isChecked(): # проверка на состояние чекбокса
                self.ui.tabWidget.setCurrentIndex(0)

        except Exception as e:
            print(f"Error in auto_set_data_ttime: {e}")

    def set_time(self):
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            return current_time
        except Exception as e:
            print(f"Error in set_time: {e}")

    def round_time(self, current_time_str, times):
        try:
            current_time = datetime.strptime(current_time_str, "%H:%M")

            closest_time = None
            min_diff = None

            for time_str in times:
                time_obj = datetime.strptime(time_str, "%H:%M")
                if time_obj < current_time:
                    time_obj += timedelta(days=1)

                diff = (time_obj - current_time).total_seconds()
                if min_diff is None or diff < min_diff:
                    min_diff = diff
                    closest_time = time_str

            return closest_time
        except Exception as e:
            print(f"Error in round_time: {e}")

    def find_serch_time(self):
        try:
            config = self.load_data_from_json()
            times = [config["combobox"][i] for i in config["combobox"]]
            test_times = self.set_time()
            time = self.round_time(test_times, times)
            timebox_index = self.ui.set_time.findText(time)
            self.ui.set_time.setCurrentIndex(timebox_index)
        except Exception as e:
            print(f"Error in find_serch_time: {e}")

    def load_time_in_set_combobox(self):
        try:
            config = self.load_data_from_json()
            for i in config["combobox"]:
                self.ui.set_time.setItemText(int(i), str(config["combobox"][i]))
            self.find_serch_time()
        except Exception as e:
            print(f"Error in load_time_in_set_combobox: {e}")

    ################# end function posting ###########################

    def web_view(self):
        try:
            pass
            #self.ui.webEngineView.setUrl(local_url)
        except Exception as e:
            print(f"Error in web_view: {e}")

    #def movie_start_stop(self):
    #    if self.ui.button_play_pause.isChecked():
    #        self.ui.button_play_pause.setText("Pause")
    #        self.web_view()
    #        self.movie.start()
    #    else:
    #        self.ui.button_play_pause.setText("Play")
    #        self.movie.stop()

    def link(self):
        try:
            file = open("./temp/autTags.txt", 'r')
            for tag in file.read().split(", "):
                self.ui.text_autTags.setText(tag)
            file.close()
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"Error in link: {e}")

    def g_link(self):
        try:
            link = self.ui.lineEdit_.text()
            if link:
                api_url = link.replace("https://derpibooru.org/images/", "https://derpibooru.org/api/v1/json/images/")
                response = requests.get(api_url).json()
                new_url = response['image']['representations']['full']

                self.ui.webEngineView.setUrl(new_url)
                filename = 'equestria.gif'

                self.thread = DownloadThread(new_url, filename)
                self.downloadlink = download_link(link)

                self.thread.progress.connect(self.ui.progressBar.setValue)
                self.thread.finished.connect(self.on_download_finished)

                self.thread.start()
                self.downloadlink.start()

                self.source_url = self.ui.lineEdit_.text()
                self.ui.lineEdit_.setText('')
        except requests.RequestException as e:
            print(f"Network error in g_link: {e}")
        except KeyError as e:
            print(f"Key error in g_link: {e}")
        except Exception as e:
            print(f"Unexpected error in g_link: {e}")

    def on_download_finished(self):
        try:
            def drop():
                self.link()
                self.ui.progressBar.setValue(0)
                if self.Dialog_settings.ui.soun_end_download_checkBox.isChecked():
                    PlaySound("SystemExclamation", SND_ALIAS)
                if self.Dialog_settings.ui.auto_swap_tab_checkBox.isChecked():  # проверка на состояния чекбокса
                    self.ui.tabWidget.setCurrentIndex(2)

            self.a += 1
            if self.a == 2:
                QTimer.singleShot(1000, drop)
                self.a = 0
        except Exception as e:
            print(f"Error in on_download_finished: {e}")

    def open_temp_folder(self):
        try:
            temp_path = os.path.abspath("temp")
            if os.name == 'nt':  # Check if the system is Windows
                os.startfile(temp_path)
            elif os.name == 'posix':  # Check if the system is Unix-based
                subprocess.call(['xdg-open', temp_path])
        except Exception as e:
            print(f"Error in open_temp_folder: {e}")

    def open_settings(self):
        try:
            self.Dialog_settings.exec()
        except Exception as e:
            print(f"Error in open_settings: {e}")

    ############### start json ######################

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
        try:
            with open('config.json', 'w', encoding='utf-8') as file:
                json.dump(config, file, indent=4)
        except Exception as e:
            print(f"Error in write_data_to_json: {e}")

    ################ end json #####################


if __name__ == "__main__":
    try:
        app = QApplication()
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error in main: {e}")
