import os
from pathlib import Path


def init_notes_dir():
    """
    Створює папку `notes`, якщо вона ще не існує.
    """
    subfolders = os.listdir('./')
    print(subfolders)
    
    if 'notes' not in subfolders:
        os.mkdir('notes/')
    
    

def add_note(title: str, content: str):
    """
    Додає нову нотатку з вказаним заголовком і текстом.
    Ім'я файлу формується з title (пробіли → '_').
    """
    file_name = title.replace(' ', '_')
    
    with open('./notes/' + file_name, 'w') as f:
        f.write(content)
    


def list_notes() -> list:
    """
    Повертає список усіх нотаток у папці `notes`.
    """
    subnotes = os.listdir('./notes/')
    print('\r\nFound the following notes: ', subnotes)
    return subnotes


def read_note(filename: str) -> str:
    """
    Читає вміст вказаної нотатки.
    """
    example = open(filename, "r")
    read_example = example.read()
    example.close()
    print(read_example)


def edit_note(filename: str, new_content: str, append: bool = True):
    """
    Редагує нотатку:
    - append=True → додає текст у кінець файлу
    - append=False → перезаписує весь файл
    """
    file_mode = "a" if append == True else "w"
    with open(filename, file_mode) as f:
        f.write(new_content)

    


def delete_note(filename: str):
    """
    Видаляє вказану нотатку.
    """
    pass


def search_notes(keyword: str) -> list:
    """
    Шукає всі нотатки, де зустрічається keyword.
    Повертає список файлів.
    """
    pass

