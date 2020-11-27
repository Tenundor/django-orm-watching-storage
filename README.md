# Пульт охраны банка
<img src="https://dvmn.org/media/lessons/Django_1-st_LVl_003.png" alt="security" width="150"/>

Репозиторий с сайтом для урока «Пишем пульт охранника банка» курса [dvmn.org](https://dvmn.org/modules/)

Сайт выводит список сотрудников банка с активными картами доступа и список тех, кто сейчас находится в хранилище с указанием времени пребывания.

Также сайт позволяет посмотреть историю посещений хранилища для любого выбранного сотрудника. Для каждого посещения выводится дата, время и продолжительность пребывания в хранилище.

Если сотрудник находится в хранилище более часа, система отмечает данный визит как подозрительный.

## Установка и запуск сайта
Скачайте код:
```sh
git clone https://github.com/Tenundor/django-orm-watching-storage
```
[Установите Python](https://www.python.org/)

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте окружение проекта:
- Windows: ``.\venv\Scripts\activate``
- MacOS/Linux: ``source venv/bin/activate``

Перейдите в каталог проекта:
```sh 
cd django-orm-watching-storage
```
Установите зависимости в виртуальное окружение:
```sh 
pip install -r requirements.txt
```
Запустите `main.py`:
```sh
python main.py
```
Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
