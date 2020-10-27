import glob
import os
import os.path
from bs4 import BeautifulSoup


def remove_files(path):
    """Удаление файлов."""

    for value in glob.glob(path):
        os.remove(value)


def html_to_text(html):
    """Взял готовое решение для извлечения текста из html"""

    soup = BeautifulSoup(html, "html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    return '\n'.join(chunk for chunk in chunks if chunk)


def is_not_file(path):
    """Проверка файла."""

    return not os.path.isfile(path)
