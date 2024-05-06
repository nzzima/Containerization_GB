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
![Docker](/Seminar_5/source/img19.png)  

*Запускаем первый Dockerfile на ManagerNode:*   

![Docker](/Seminar_5/source/img20.png)  
![Docker](/Seminar_5/source/img21.png)  

*Запускаем второй Dickerfile на WorkerNode:*   

![Docker](/Seminar_5/source/img22.png)  
![Docker](/Seminar_5/source/img23.png)  

*Попробуем запустить первый Dockerfile на WorkerNode:*  

![Docker](/Seminar_5/source/img24.png)  

*(Ошибки дублирования не произошло т. к имена image разные)*  

![Docker](/Seminar_5/source/img25.png)  

*Запускаем на ManagerNode второй Dockerfile и получаем четыре работающих контейнера на двух node:*

![Docker](/Seminar_5/source/img26.png)  
![Docker](/Seminar_5/source/img27.png)  

*Тем временем WorkerNode упал:*

![Docker](/Seminar_5/source/img28.png) 

*Создаем "реплики" образов и наблюдаем следующее:*

![Docker](/Seminar_5/source/img29.png) 