# count_clicks
Скрипт для сокращения ссылок и подсчета колличества переходов по ним. Работает с исользованием API сервиса сокращения ссылок [Bitly.om](https://bitly.com/).

Для использования скрипта необходимо зарегистрироваться на сервисе и получить токен.


## Необходимое окружение
В папке со скриптом необходимо создать .env файл содержащий токен, полученный на сервисе.
```
BITLY_TOKEN=your_token
```

## Как установить
* Клонируем репозиторий
* Создаем виртуальное окружение
* В корень проекта добавляем .env c требуемыми переменными
* Устанавливаем зависимости
```
pip install -r requirements.txt
```


## Использование
Для запуска скрипта в консоли набираем команду на запуск файла и ссылку
```
python main.py http://your-link.com
```
В ответ будет напечатана сокращенная версия ссылки, если она не сокращалась ранее, либо количесво кликов по ней, если ссылка уже была сокращенаю