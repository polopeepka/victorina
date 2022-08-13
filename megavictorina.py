def baby_questions_one(ask_age):
    while True:
        ask_one_baby = input('Тебе нравиться погода на улице? - ')
        if ask_one_baby == 'да':
            print('Хорошая погода-залог хорошего настроения!')
            break
        elif ask_one_baby == 'нет':
            print('Бывает,но не стоит расстраиваться,завтра погода точно будет лучше!')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue

def baby_questions_two(ask_age):
    while True:
        ask_one_baby_two = input('Ты хорошо себя ведешь? - ')
        if ask_one_baby_two == 'да':
            print('Молодец,так держать!')
            break
        elif ask_one_baby_two == 'нет':
            print('Я думаю тебе стоит подумать над своим поведением и исправиться ')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')

print('Эта программа будет задавать вопросы а которые вам нужно ответить,\n'
      'все вопросы будут заданы в зависимости от возраста того человека который ввел ссвой возраст в программе ')
print('Отвечай "да или нет") ')
while True:
    ask_age = int(input('Сколько вам лет? - '))
    if ask_age <= 5:
        baby_questions_one(ask_age)
        baby_questions_two(ask_age)


