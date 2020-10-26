import pandas as pd
import glob
import os

# Путь ко всем найденным ссылкам
path_bd_all = 'save/release/bd_all.csv'

# Путь к ссылкам на тесты
path_bd_test = 'save/release/bd_test.csv'


def write_tmp(data, number):
    """Записать данные на время в csv."""

    df = pd.DataFrame(data)
    df.to_csv(f"save/db_{number}.csv", encoding='utf-8', index=False)


def write_merge():
    """Собрать общие данные и отфильтровать данные тестов в отдельный файл csv."""

    files = glob.glob("save/db_*.csv")

    # Убираем пустые csv файлы
    files = list(filter(lambda file: os.stat(file).st_size > 1, files))

    # Получаем все временные csv файлы для соединения
    df = (pd.read_csv(f) for f in files)
    df = pd.concat(df, ignore_index=True)

    # Сохранение всех найденных ссылок
    df.to_csv(path_bd_all, encoding='utf-8', index=False)

    # Сохранение ссылок, где есть только тесты
    df['0'][df['1'].isnull()].to_csv(path_bd_test, encoding='utf-8', index=False)


def read_tests():
    """Получение ссылок в array из csv"""

    df = pd.read_csv(path_bd_test, skipinitialspace=True)
    data = []

    # Перебор ссылок
    for value in df.iterrows():
        data.append(value[1][0])

    return data
