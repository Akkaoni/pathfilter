import json
import os

# Получаем путь к текущему файлу (config.py)
base_path = os.path.dirname(os.path.abspath(__file__))

# Поднимаемся на уровень выше (в корень проекта) и идем в config/config.json
config_path = os.path.join(base_path, '..', 'config', 'config.json')

default_config_path = os.path.join(base_path, '..', 'config', 'default_config.json')

class config:

    @staticmethod
    def get_config():
        """Получение настроек приложения."""
        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f) 

        return data

    @staticmethod
    def get_language():
        """Получение языка приложения."""
        conf = config.get_config()
        language = conf["language"]
        Lange_path = os.path.join(base_path, '..', 'config', f'Lang{language}.json')
        with open(Lange_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    def set_config(config):
        """Изменение настроек приложения."""
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

    def get_default_config():
        """Получение настроек приложения по default."""
        with open(default_config_path, 'r', encoding='utf-8') as f:
            data = json.load(f) 

        return data
