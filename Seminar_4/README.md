# Dockerfile и слои
### Task
*Необходимо создать Dockerfile, основанный на любом образе (вы в праве выбрать самостоятельно).
В него необходимо поместить приложение, написанное на любом известном вам языке программирования (Python, Java, C, С#, C++).
При запуске контейнера должно запускаться самостоятельно написанное приложение.*
### Ход выполнения
Создание директории под задание:
```bash
nick@Ubuntu:~$ mkdir sem4
nick@Ubuntu:~$ cd sem4/
```
Создание Dockerfile:
```bash
nick@Ubuntu:~/sem4$ nano Dockerfile
```
Dockerfile:
```dockerfile
FROM ubuntu:22.04

RUN apt update && apt install -y python3

WORKDIR /app

COPY app.py /app/

CMD ["python3", "app.py"]
```
Создание docker image:
```bash
nick@Ubuntu:~/sem4$ docker build -t my_application .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  3.072kB
Step 1/5 : FROM ubuntu:22.04
 ---> 7af9ba4f0a47
Step 2/5 : RUN apt update && apt install -y python3
 ---> Using cache
 ---> 357174b1cb12
Step 3/5 : WORKDIR /app
 ---> Using cache
 ---> cc779aae7307
Step 4/5 : COPY app.py /app/
 ---> 535b98480df6
Step 5/5 : CMD ["python3", "app.py"]
 ---> Running in 16baebbf230a
Removing intermediate container 16baebbf230a
 ---> 05c423b519d4
Successfully built 05c423b519d4
Successfully tagged my_application:latest
nick@Ubuntu:~/sem4$ docker images
REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
my_application           latest    05c423b519d4   7 seconds ago    159MB
my-docker-image          latest    5894d532f357   25 minutes ago   159MB
nginx                    latest    2ac752d7aeb1   5 days ago       188MB
ubuntu                   22.04     7af9ba4f0a47   11 days ago      77.9MB
postgres                 latest    d60dc4bd84c0   2 months ago     431MB
ubuntu                   18.04     f9a80a55f492   10 months ago    63.2MB
hello-world              latest    d2c94e258dcb   11 months ago    13.3kB
docker/getting-started   latest    3e4394f6b72f   16 months ago    47MB
```
Запуск docker:
```bash
nick@Ubuntu:~/sem4$ docker run -it my_application

```