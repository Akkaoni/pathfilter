import tkinter as tk

from init import init
from gui.pages.settings import open_settings_window

def open_settings():
    open_settings_window(main_window)

def run():
    result = init()
    if result == 'NEED_CONFIG':
        open_settings()


# 1. Создаем главное окно
main_window = tk.Tk()
main_window.title("Path Filter")
main_window.geometry("500x150") # Устанавливаем размер окна

btn_settings = tk.Button(main_window, text="Настройки", command=open_settings)
btn_settings.pack(pady=10)

btn_run = tk.Button(main_window, text="Запуск", command=run)
btn_run.pack(pady=10)

# 3. Запускаем цикл обработки событий
main_window.mainloop()