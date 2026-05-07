
class SetupFolders:
    def __init__(self, config, file_list):
        # Чтобы переменные были доступны в других методах, 
        # их нужно привязывать к экземпляру через 'self'
        self.config = config
        self.file_list = file_list
        
        # Создаем множества (set) для быстрой проверки вхождений
        self.folder_names_to_find = {folder["name"] for folder in config} 
        self.file_set = set(file_list)  

    def find_missing_folders(self):
        """Возвращает список папок, которые есть в конфиге, но отсутствуют на диске."""
        # Используем self.file_set вместо списка для ускорения работы (O(1) вместо O(n))
        missing_folders = [name for name in self.folder_names_to_find if name not in self.file_set]
        return missing_folders
    
    def found_in_folders(self): 
        """Возвращает список папок, которые успешно найдены в обоих источниках."""
        # Метод intersection (пересечение) идеально подходит для поиска общих элементов
        found_folders = list(self.folder_names_to_find.intersection(self.file_set))
        return found_folders