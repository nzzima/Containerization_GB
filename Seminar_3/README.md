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
![Docker start](/Seminar_3/source/img1.png)
![Docker start](/Seminar_3/source/img2.png)

Далее заходим (в новой консоли) в bash этого контейнера и оттуда в БД:   

![Docker start](/Seminar_3/source/img3.png)

Создаем БД и заполняем ее данными:

![Docker start](/Seminar_3/source/img4.png)
![Docker start](/Seminar_3/source/img5.png)

После этого необходимо запустить pgadmin4 с помощью docker:

![Docker start](/Seminar_3/source/img6.png)

После этого заходим в web pgAdmin4 по адресу `localhost:82/login/`:

![Docker start](/Seminar_3/source/img7.png)

Проходим авторизацию и видим созданную нами БД:

![Docker start](/Seminar_3/source/img8.png)