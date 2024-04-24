# Введение в Docker
## Task
1) Запустить контейнер с БД, отличной от mariaDB, используя инструкции на сайте: https://hub.docker.com/
2) Добавить в контейнер hostname такой же, как hostname системы через переменную
3) Заполнить БД данными через консоль
4) Запустить phpmyadmin (в контейнере) и через веб проверить, что все введенные данные доступны

## Ход выполнения
Устанавливаем postgresql:
```bash
nick@Ubuntu2204: $ sudo apt install postgresql
```
Запускаем контейнер docker:
```bash
nick@Ubuntu2204: $ docker container run --name="postgres" -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root postgres:9.6.24
```
БД PostgreSQL стандартно запускается на порте 5432. В случае, если при запуске docker-а появляется ошибка
`Error starting userland proxy: listen tcp4 0.0.0.0:5432: bind: address already in use` означающая, что порт 5432 занят, следует его освободить:
```bash
nick@Ubuntu2204: $ sudo fuser -k 5432/tcp
```