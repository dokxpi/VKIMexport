import re
import os
import json
import urllib.request
import urllib.error

import lxml.html
import requests


LOGIN = '380636418552'  # Логин от вашего аккаунта
PASSWORD = 'AcYsYc'  # Пароль от аккаунта
DIALOG_ID = '69828681'  # ID чата или диалога
PATH = 'C:/dialog'  # Полный путь к папке куда нужно сохранить фотографии 


def auth(login, password):
    """
    Авторизация на сайте
    """
    data_auth = {
        'act': 'login',
        'role': 'al_frame',
        'q': '1',
        'al_frame': '1',
        'expire': '',
        'captcha_sid': '',
        'captcha_key': '',
        '_origin': 'https://vk.com',
        'email': login,
        'pass': password
    }

    requests_auth = requests.post('https://login.vk.com/?act=login', data=data_auth)
    if 'parent.onLoginDone' in requests_auth.text:
        return requests_auth.cookies
    else:
        print('Ошибка авторизации')
        exit(1)


def parse_response(cookies, dialog_id):
    """
    Вытаскиваем из ответа сервера смещение и данные о ссылках
    """
    all_urls = []

    # offset - текущее смешение count - максимальное значение смещения
    offset = {'count': 10000, 'offset': 0}  # Начальные значения

    data_request = {
        'act': 'show',
        'al': '1',
        'loc': 'al_im.php',
        'w': 'history{}_photo'.format(dialog_id),
        'offset': 0,
        'part': 1
    }

    while offset['offset'] < offset['count']:
        data_request['offset'] = offset['offset']
        content = requests.post('https://vk.com/wkview.php', cookies=cookies, params=data_request).text

        # Получаем значение смещения
        indexes = slice(*re.search('\{"count":.+?,"offset":.+?\}', content).span())
        offset = {key: int(value) for key, value in json.loads(content[indexes]).items()}

        # Извлекаем ссылки
        all_urls.extend(get_urls(content))

    return all_urls


def get_urls(data):
    """
    Подправляем ответ сервера и извлекаем ссылки на фото
    """
    compiled_urls = []

    # Заменяем экранированные последовательности и знак комментария, чтобы парсить html
    data = data.replace('&quot;', "'").replace('<!--', '')

    parsing = lxml.html.fromstring(data)
    for i in parsing.cssselect('a'):
        # Извлекаем атрибут onclick и разбираем его содержимое, а так же приводим полученные данные к правильному json
        find = re.search("{'base'.*\]}", i.get('onclick')).group().replace("'", '"')
        url_data = json.loads(find)

        # Собираем url
        if 'z_' in url_data.keys():
            compiled_urls.append('{}{}.jpg'.format(url_data['base'], url_data['z_'][0]))
        else:
            compiled_urls.append('{}{}.jpg'.format(url_data['base'], url_data['x_'][0]))

    return compiled_urls


def download_img(urls, path):
    """
    Скачивает картинки в указанное место
    """
    error = []
    all_files = len(urls)
    for count, url in enumerate(urls):
        try:
            urllib.request.urlretrieve(url, os.path.join(path, url.split('/')[-1]))
        except urllib.error.HTTPError:
            error.append(url)
        print('\rСкачано {}/{} файлов'.format(count + 1, all_files), end='')
    return error

if __name__ == '__main__':
    cookies = auth(LOGIN, PASSWORD)
    urls = parse_response(cookies, DIALOG_ID)
    error = download_img(urls, PATH)

    if error:
        print('\n Возникли ошибки при скачивании: ')
        for i in error:
            print(i)
