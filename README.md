# hack_e_dilary

Скрипт предназначен для редактирования бд сайта электронного дневника - https://github.com/devmanorg/e-diary.git

### Как установить

Python3 должен быть уже установлен. 
Чтобы запустить скрипт необходимо положить файл с кодом рядом с manage.py и подключить через import.

### Запуск

Для использования в shell:

* Запустите shell:
```
python manage.py shell
```
* Подключите файл:
```
from script import get_schoolkid, fix_marks, remove_chastisements, create_commendation
```

* Для получения из бд конкретного ученика:
```
child = get_schoolkid('Фамилия Имя')
```
* Для исправления плохих оценок:
```
fix_marks('Фамилия Имя')
```
* Для удаления замечаний:
```
remove_chastisements('Фамилия Имя')
```
* Для создания записи похвалы:
```
create_commendation('Фамилия Имя', 'Название урока')
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).