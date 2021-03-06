# Структура проекта

back   - Бэкенд. Написан на nodejs. 
image  - код воркера (python) и dockerfile - все для для сборки docker-образа воркера
order

## back - Бэкенд

Задача бэкена в этой инфраструктуре - раздавать задачи и принимать результаты выполнения этих задач.

Представляет собой простейший веб-сервис, написанный на nodejs и express. 
После запуска принимает запросы по двум адресам: 
- /get_task - возвращает данные для задачи. В нашем примере это json объект вида 
```
  {
    id: 1,
    a: 12,
    b: 8
  }
```
id задачи и два числа. Задача, например - сложить эти числа в сонме.
- /push_result - Прием результата. Принимает любой json. push_result.rest - пример rest запроса, который отправит результат на данный адрес. Можно отправить через любой rest клиент (парочка для примера: [Rest Client для VSCode](https://marketplace.visualstudio.com/items?itemName=humao.rest-client); [insomnia](https://insomnia.rest/)). 


## image - образ воркера

Воркер - та часть системы, которая выполняет задачи на сонме. Представляет собой docker-образ. В нашем случае код написан на python. Образ пушится на hub.docker.com.


## order - Скрипты на создание задачи через sonm-cli

Сначала создается order. Затем после создания сделки создается задача - task.

# Сборка и запуск

## Бэкенд

```sh
npm install   # Установить пакеты
npm start     # запуск. При получении результата сервис пишет его в консоль.
```

## image

Разработка:

```
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Сборка, запуск и публикация образа:

```sh
make build
make run
make push
```
