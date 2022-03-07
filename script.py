from datacenter.models import Schoolkid, Mark, Chastisement, Commendation, Lesson
import Model
import random

COMMENDATIONS = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Так держать!',
        'Ты на верном пути!',
        'Это как раз то, что нужно!',
        'С каждым разом у тебя получается всё лучше!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]

def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Model.MultipleObjectsReturned:
        print('Найдено несколько учеников!')
    except Model.DoesNotExist:
        print('Не найдено ученика с таким именем!')
    else:
        return schoolkid


def fix_marks(name):
    child = get_schoolkid(name)
    if child:
        marks = Mark.objects.filter(schoolkid=child, points__lt=4)
        for mark in  marks:
            mark.points = 5
            mark.save()


def remove_chastisements(name):
    child = get_schoolkid(name)
    if child:
        chastisements = Chastisement.objects.filter(schoolkid=child)
        for chastisement in chastisements:
            chastisement.delete()
        print('Удалили замечание из БД')


def create_commendation(name, name_lesson):
    commendation = random.choice(COMMENDATIONS)
    child = get_schoolkid(name)
    if child:
        lesson = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter, subject__title=name_lesson).order_by('-date').first()
        if lesson:
            Commendation.objects.create(text=commendation, created=lesson.date, schoolkid=child, subject=lesson.subject, teacher=lesson.teacher)
