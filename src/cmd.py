import src.csv as csv
import src.parser as parser
import src.helper as helper


def one():
    """Команда для получения всех ссылок, которые можно скачать в media."""

    print('-------------one-------------')
    print('How many root link to process? [1=100 links, recommend=300 (30k request * 5)]')

    # Количество умножений на число вводимого пользователем.
    # Если пользователь введем 5, то будет умножение на count_links
    # и столько сущностей будет обработанно
    count_links = 100

    # Вводимое число пользователя
    user_input = int(input('>>> '))

    # Базовая ссылка для брутфорсинга
    url = 'http://cdo.keu.kz/content/'

    helper.remove_files('save/db_*')

    # Обработка пользовательского числа. Помогает разделять на временные файлы
    for i in range(1, user_input + 1):
        data = []

        # Запросы на один файл по count_links раз
        for k in range(i * count_links - count_links + 1 if i > 1 else 1, i * count_links + 1):
            # Получение ссылок
            parser_data = parser.get(f"{url}{k}/")

            if parser_data:
                # Если есть ссылки в этом дереве ссылок - мы их записываем
                data.append(parser_data)

        # Записываем результат во временное хранилище
        csv.write_tmp(data, i)

    # Соединение временных данных в один файл csv
    csv.write_merge()

    print('Success!')


def two():
    """Скачиваем данные из bd_test.csv в media."""

    print('-------------two-------------')

    helper.remove_files('save/media/file_*')

    for value in csv.read_tests():
        parser.media(value)

    print('Success!')


def start():
    """Стартовая команда."""

    print('-------------start-------------')
    print('[1] update db.csv')
    print('[2] download files by db.csv (tests)')
    print('[3] exit')

    cmd_list = {
        '1': lambda: one(),
        '2': lambda: two(),
        '3': lambda: exit('End!')
    }

    user_input = input('[1, 2 or 3] >>> ')

    if user_input in cmd_list:
        cmd_list[user_input]()
    else:
        start()
