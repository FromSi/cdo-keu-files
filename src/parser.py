from bs4 import BeautifulSoup
import urllib.request
import requests
import src.helper as helper


def get(url):
    """Получить готовые ссылки на файлы."""

    data = []
    soup = BeautifulSoup(fetch(url), features="html.parser")

    # Получаем элементы <a></a>
    a_list = soup.find_all('a')

    # Если нет файлов, отправляем пустой массив
    if len(a_list) < 1:
        return []

    # Убираем ссылку на родительскую директорию
    del a_list[0]

    for value in a_list:
        # Настраиваем ссылку
        link = f"{url}{value.get('href')}"

        if value.get('href')[-1:] == '/':
            # Если это не файл, а дочерняя директория.
            # Заходим в неё и заходим в рекурсию
            data.extend(get(link))
        else:
            # Отлично! Записываем ссылку подходящего файла в массив
            data.append(link)

    return data


def fetch(url):
    """Сделать запрос и получить html."""

    print(url)

    try:
        # Получаем content с ссылки
        with urllib.request.urlopen(url) as response:
            return response.read()
    except:
        return ''


def media(url):
    """Взять данные по ссылке и записать в файл."""

    print(url)

    # Разбиение делаю для названия файлов
    url_array = url.split('/')
    r = requests.get(url, allow_redirects=True)

    # Сохраняем файл с тестами
    open(f"save/media/file_{url_array[4]}_{url_array[5]}_{url_array[6].split('.')[0]}.txt", 'w') \
        .write(helper.html_to_text(r.content))
