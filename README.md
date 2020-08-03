# Teстовое задание 
Реализация тестового задания по парсингу данных и выводу с помощью Django, Angular.
Ссылка на данные - https://finance.yahoo.com/quote/GOOG/balance-sheet?p=GOOG.
(Balance Sheet)

### Какие модули используются:
- django-cors-headers==3.4.0    `pip install django-cors-headers`
- djangorestframework==3.11.0   `pip install djangorestframework`
- Django==3.0.8                 `pip install Django`
- lxml==4.5.2                   `pip install lxml`
- requests==2.24.0              `pip install requests`
- selenium==3.141.0             `pip install selenium`
- webdriver-manager==3.2.1      `pip install webdriver-manager`
- beautifulsoup4==4.9.1         `pip install beautifulsoup4`
- psycopg2==2.8.5               `pip install psycopg2`
 
 
### Инструкция по запуску:
1. Сделать `pip install` всех модулей выше.
2. В директории client запустить команду `npm install`
3. Запуск сервера Django с директории server: `python manage.py runserver`
4. Запуск клиента Angular с директории client: `ng serve`


Запуск парсера выполняется при каждом запуске сервера, 
но можно и отдельно, командой: `python manage.py parser_data`