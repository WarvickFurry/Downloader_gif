import json

class JSONUpdater:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data_from_json(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def write_data_to_json(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def merge_dicts(self, target, source):
        for key, value in source.items():
            if isinstance(value, dict) and key in target:
                self.merge_dicts(target[key], value)
            elif key not in target:
                target[key] = value

    def data_is_new(self, existing_data, new_data):
        """
        Проверяет, есть ли новые данные, которые нужно добавить.
        Возвращает True, если данные новые и их нужно добавить, иначе False.
        """
        for key, value in new_data.items():
            if key not in existing_data:
                return True
            if isinstance(value, dict) and isinstance(existing_data[key], dict):
                if self.data_is_new(existing_data[key], value):
                    return True
            elif existing_data[key] != value:
                return True
        return False

    def update_json_file(self, new_data):
        # Шаг 1: Прочитать существующий JSON файл
        try:
            data = self.load_data_from_json()
        except FileNotFoundError:
            data = {}

        # Шаг 2: Проверить, есть ли новые данные
        if self.data_is_new(data, new_data):
            # Шаг 3: Добавить только новые данные
            self.merge_dicts(data, new_data)

            # Шаг 4: Сохранить обновленный JSON обратно в файл
            self.write_data_to_json(data)
            print("JSON файл был обновлен.")
        else:
            print("Новых данных нет. JSON файл не был обновлен.")
