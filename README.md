# Короткое Ссылочное Пространство Bitly и Счетчик Кликов

Этот скрипт на Python взаимодействует с API Bitly для выполнения двух основных функций:
1. Сокращение длинных URL с помощью сервиса Bitly.
2. Получение и отображение статистики кликов для ссылок Bitly.

## Предварительные требования
- Python 3.x
- Подключение к интернету
- Учетная запись Bitly с токеном доступа

## Настройка
1. Убедитесь, что у вас установлен Python на вашей системе.
2. Получите токен доступа от Bitly, зарегистрировавшись и создав ключ API.
3. Определите переменную с именем `access_token` в этом файле и присвойте ей ваш токен доступа.

## Установка
Внешние библиотеки прописаны в requirements.txt.

## Использование
1. Запустите скрипт.
2. Введите URL, который вы хотите сократить или проверить статистику кликов, когда будет запрос.
3. Если URL допустим, он будет сокращен с помощью Bitly. Если это уже ссылка Bitly, ее статистика кликов будет отображена.

## Функции
- `shorten_link(token, url)`: Сокращает указанный URL с использованием API Bitly.
- `count_clicks(token, url)`: Получает статистику кликов для ссылки Bitly.
- `is_bitlink(token, url)`: Проверяет, является ли указанный URL ссылкой Bitly.

## Примечание
- Этот скрипт зависит от API Bitly, поэтому для его эффективного использования требуется подключение к интернету.
- Убедитесь, что вы соблюдаете условия использования и политику использования API Bitly при использовании этого скрипта.