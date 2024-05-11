# Docker Compose и Docker Swarm
## Task

### Задание 1:
1) Создать сервис, состоящий из 2 различных контейнеров: 1 - веб, 2 - БД
2) Далее необходимо создать 3 сервиса в каждом окружении (dev, prod, lab)
3) По итогу на каждой ноде должно быть по 2 работающих контейнера
4) Выводы зафиксировать

### Задание 2*:
1) Нужно создать 2 ДК-файла, в которых будут описываться сервисы
2) Повторить задание 1 для двух окружений: lab, dev
3) Обязательно проверить и зафиксировать результаты, чтобы можно было выслать преподавателю для проверки

## Ход выполнения (Задание №1)

![Docker](/Seminar_5/source/img1.png)  
![Docker](/Seminar_5/source/img2.png)  
![Docker](/Seminar_5/source/img3.png)  
![Docker](/Seminar_5/source/img5.png)  
![Docker](/Seminar_5/source/img6.png)  
![Docker](/Seminar_5/source/img7.png)  
![Docker](/Seminar_5/source/img8.png)  
![Docker](/Seminar_5/source/img9.png)  
![Docker](/Seminar_5/source/img10.png)  
![Docker](/Seminar_5/source/img11.png)  
![Docker](/Seminar_5/source/img12.png)  
![Docker](/Seminar_5/source/img13.png)  
![Docker](/Seminar_5/source/img14.png)  

## Ход выполнения (Задание №2)
Создаем 2 Dockerfile-а:
```dockerfile
version: '3.10.6'

services:

    db:
        image: mariadb:10.10.2
        restart: always
        environment: 
            MYSQL_ROOT_PASSWORD: '12345'
            
    adminer:
        image: adminer:4.8.1
        restart: always
        ports: 6080:8000
```
```dockerfile
version: '3.9'

services:

    db:
        image: mysql
        restart: always
        environment: 
            MYSQL_ROOT_PASSWORD: '12345'
            
    phpmyadmin:
        image: phpmyadmin/phpmyadmin
        restart: always
        ports: 80:80
        environment: 
            MYSQL_ROOT_PASSWORD: '12345'           

```
Компилируем NODE:  
![Docker](/Seminar_5/source/img15.png)  
Проверяем:  
![Docker](/Seminar_5/source/img16.png)  
![Docker](/Seminar_5/source/img17.png)    
Получаем ошибку: "версия данного файла не поддерживается", продолжаем делать, как делали на семинаре. Запускаем первый Dockerfile:  
![Docker](/Seminar_5/source/img18.png)    
Проверяем:  
![Docker](/Seminar_5/source/img19.png)  
![Docker](/Seminar_5/source/img20.png)  
Запускаем второй Dockerfile:  
![Docker](/Seminar_5/source/img21.png)  
![Docker](/Seminar_5/source/img22.png)    
Воспользуемся функционалом Docker Swarm и создадим дубликат одного и того же образа:  
![Docker](/Seminar_5/source/img23.png)  
![Docker](/Seminar_5/source/img24.png)    
Аналогично можем проделать с другими образами, далее повязать их сетью и получить полные дубликаты: БД + WEB