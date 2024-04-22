# Механизмы пространства имен

### Task
*Необходимо продемонстрировать изоляцию одного и того же приложения в различных пространствах имен.*

### Ход выполнения

Смена корневого каталога:
```bash
nick@Ubuntu:~$ mkdir sem1
nick@Ubuntu:~$ cd sem1/
nick@Ubuntu:~/sem1$ mkdir bin
nick@Ubuntu:~/sem1$ cp /bin/bash sem1/bin
cp: cannot create regular file 'sem1/bin': No such file or directory
nick@Ubuntu:~/sem1$ ls
bin
nick@Ubuntu:~/sem1$ cp /bin/bash sem1/bin/
cp: cannot create regular file 'sem1/bin/': No such file or directory
nick@Ubuntu:~/sem1$ cp /bin/bash /sem1/bin
cp: cannot create regular file '/sem1/bin': No such file or directory
nick@Ubuntu:~/sem1$ cp /bin/bash ~/sem1/bin
nick@Ubuntu:~/sem1$ ldd /bin/bash
	linux-vdso.so.1 (0x00007fff4770f000)
	libtinfo.so.6 => /lib/x86_64-linux-gnu/libtinfo.so.6 (0x000074b4b6cc1000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x000074b4b6a00000)
	/lib64/ld-linux-x86-64.so.2 (0x000074b4b6e65000)
nick@Ubuntu:~/sem1$ mkdir lib
nick@Ubuntu:~/sem1$ mkdir lib64
nick@Ubuntu:~/sem1$ cp /lib/x86_64-linux-gnu/libtinfo.so.6 ~/sem1/lib
nick@Ubuntu:~/sem1$ cp /lib/x86_64-linux-gnu/libc.so ~/sem1/lib
nick@Ubuntu:~/sem1$ cp /lib/x86_64-linux-gnu/libc.so.6 ~/sem1/lib
nick@Ubuntu:~/sem1$ cp /lib64/ld-linux-x86-64.so.2 ~/sem1/lib64
ick@Ubuntu:~/sem1$ sudo chroot ~/sem1/
bash-5.1#
```
Изоляция файловой системы:
```bash
nick@Ubuntu:~/sem1$ sudo unshare --mount --root=sem1 /bin/zsh
```
Изоляция сетевого пространства имен:
```bash
nick@Ubuntu:~/sem1$ ip a
nick@Ubuntu:~/sem1$ unshare --pid --net --fork --mount-proc /bin/bash
nick@Ubuntu:~/sem1$ ip a
```
Host:
```bash
$ ip netns add testns
ip netns exec testns bash
```
Пространство имен:
```bash
$ ip a
```
Host:
```bash
$ ip link add virt0 type veth peer name virt1
$ ip addr 10.0.0.1/24 dev virt0
$ ip addr add 10.0.0.2/24 dev virt1
$ ip link set virt1 netns testns
```
Пространство имен:
```bash
$ ip addr add 10.0.0.3/24 dev virt1
$ ip link set dev virt1 up
```
Host:
```bash
$ ip link set dev virt0 up
$ ping 10.0.0.3 -c2
```
Пространство имен:
```bash
$ ping 10.0.0.1 -c2
```
