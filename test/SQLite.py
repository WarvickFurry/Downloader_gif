from PySide6.QtSql import QSqlDatabase, QSqlQuery
import sys

class DatabaseManager:
    def __init__(self, dbname="param.db"):
        # Подключаемся к базе данных SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(dbname)

        if not self.db.open():
            print("Ошибка подключения к базе данных!")
            sys.exit(1)
        else:
            print("Успешное подключение к базе данных.")

        # Инициализация таблицы settings
        self.init_settings_table()

    def init_settings_table(self):
        # Создание таблицы settings для хранения параметров
        query = QSqlQuery()
        query.exec("""
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT
            )
        """)

    def save_setting(self, key, value):
        # Сохранение параметра в таблицу settings
        query = QSqlQuery()
        query.prepare("INSERT OR REPLACE INTO settings (key, value) VALUES (:key, :value)")
        query.bindValue(":key", key)
        query.bindValue(":value", value)
        if not query.exec():
            print("Ошибка при сохранении параметра:", query.lastError().text())

    def load_setting(self, key):
        # Загрузка параметра из таблицы settings
        query = QSqlQuery()
        query.prepare("SELECT value FROM settings WHERE key = :key")
        query.bindValue(":key", key)
        if query.exec() and query.next():
            return query.value(0)
        return None





class db_init:
    def __init__(self):
        self.db_manager = DatabaseManager()

        # Восстановление сохранённого индекса вкладки

    def load_setting(self, key):
        saved_index = self.db_manager.load_setting(str(key))
        if saved_index is not None:
            return saved_index



    def save_setting(self,key, index):
        self.db_manager.save_setting(str(key), str(index))


