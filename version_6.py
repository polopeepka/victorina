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
        ask_two_baby = input('Ты хорошо себя ведешь? - ')
        if ask_two_baby == 'да':
            print('Молодец,так держать!')
            break
        elif ask_two_baby == 'нет':
            print('Я думаю тебе стоит подумать над своим поведением и исправиться ')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')


def baby_questions_three(ask_age):
    while True:
        ask_three_baby = input('Ты любишь гулять на улице? -  - ')
        if ask_three_baby == 'да':
            print('Свежий воздух-это хорошо!')
            break
        elif ask_three_baby == 'нет':
            print('Гулять-весело,но если тебе не нравиться,то можно посидеть дома еще чуток)')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue


def baby_questions_four(ask_age):
    while True:
        ask_four_baby = input('Тебе нравиться слушать музыку? - ')
        if ask_four_baby == 'да':
            print('Я тоже люблю слушать музыку!')
            break
        elif ask_four_baby == 'нет':
            print('Это твое дело,вот я например слушаю музыку,потому что она меня успокаивает.')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue


################################################################################################
def teener_questions_one(ask_age):
    while True:
        ask_one_tener = input('Ты любишь играть в футбол? - ')
        if ask_one_tener == 'да':
            print('Спорт это всегда хорошо!')
            break
        elif ask_one_tener == 'нет':
            print('Может быть тебе нравятся другие игры,я тоже не люблю футюол')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue


def teener_questions_two(ask_age):
    while True:
        ask_two_tener = input('У тебя много друзей? - ')
        if ask_two_tener == 'да':
            print('Отлично,в компании друзей всегда веселей!')
            break
        elif ask_two_tener == 'нет':
            print('Интроверт be like')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue


def teener_questions_three(ask_age):
    while True:
        ask_three_tener = input('У тебя много друзей? - ')
        if ask_three_tener == 'да':
            print('Отлично,в компании друзей всегда веселей!')
            break
        elif ask_three_tener == 'нет':
            print('Интроверт be like')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue



def teener_questions_four(ask_age):
    while True:
        ask_four_tener = input('У тебя есть вторая половинка? - ')
        if ask_four_tener == 'да':
            print(f'wtf bro u are {ask_age} ')
            break
        elif ask_four_tener == 'нет':
            print('Интроверт be like')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue


def adult_questions_one(ask_age):
    while True:
        ask_one_adult = input('У тебя есть машина или другое средство передвижения? - ')
        if ask_one_adult == 'да':
            print('Круто,только не гоняй особо ')
            break
        elif ask_one_adult == 'нет':
            print('Я уверен,что скоро появится')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue


def adult_questions_two(ask_age):
    while True:
        ask_two_adult = input('У тебя есть работа? - ')
        if ask_two_adult == 'да':
            print('как бы не боло тяжело, работать надо')
            break
        elif ask_two_adult == 'нет':
            print('Пора бы и найти работу')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue

def adult_questions_three(ask_age):
    while True:
        ask_three_adult = input('Ты готов к самостоятельной жизни? - ')
        if ask_three_adult == 'да':
            print('Это большая ответственность,но я думаю ты справишься')
            break
        elif ask_three_adult == 'нет':
            print('У тебя осталось не так много времени')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue


def adult_questions_four(ask_age):
    while True:
        ask_four_adult = input('Ты любишь читать? - ')
        if ask_four_adult == 'да':
            print('Это классно,что ты развиваешься')
            break
        elif ask_four_adult == 'нет':
            print('Я тоже не люблю)')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue


##########################################################################################################

print('Эта программа будет задавать вопросы а которые вам нужно ответить,\n'
      'все вопросы будут заданы в зависимости от возраста того человека который ввел ссвой возраст в программе ')
print('Отвечай "да или нет") ')
while True:
    ask_age = int(input('Сколько вам лет? - '))
    if ask_age <= 10:
        duw = input(f"Оу,тебе всего {ask_age}\nты хочешь узнать первый вопрос? - ")
        if duw == 'да':
            print('Отлично!')
            print('Я задам тебе пару вопросов для твоего возраста')
            baby_questions_one(ask_age)
            print('')
            baby_questions_four(ask_age)
            print('')
            dul = input('Тебе понравилось? - ')
            if dul.lower() == 'да':
                print('Отлично,давай продолжим!')
                print('')
                baby_questions_three(ask_age)
                print('')
                print('Это были все мои вопросы,надеюсь тебя все понравилось!')
                break
            elif dul.lower() == 'нет':
                print('Эх, но у меня есть еще один вопрос,посмотри и на него,может тебе понравится')
                print('')
                baby_questions_two(ask_age)
                print('Это были все мои вопросы,надеюсь тебя все понравилось!')
                break
            else:
                print('Ты можешь отвечать только "да или нет"')
                continue

        elif duw == 'нет':
            print('эх,я думал мы подружимся,пока!')
            break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue




    elif ask_age <= 15 and ask_age > 10:
        duw = input(f"Оу,тебе уже {ask_age}\nты хочешь узнать первый вопрос? - ")
        if duw == 'да':
            print('Отлично!')
            print('Я задам тебе пару вопросов для твоего возраста')
            teener_questions_one(ask_age)
            print('')
            teener_questions_four(ask_age)
            print('')
            dul = input('Тебе понравилось? - ')
            if dul.lower() == 'да':
                print('Отлично,давай продолжим!')
                print('')
                teener_questions_three(ask_age)

                print('')
                print('Это были все мои вопросы,надеюсь тебя все понравилось!')
                break
            elif dul.lower() == 'нет':
                print('Эх, но у меня есть еще один вопрос,посмотри и на него,может тебе понравится')
                print('')
                teener_questions_two(ask_age)
                print('Это были все мои вопросы,надеюсь тебя все понравилось!')
                break
            else:
                print('Ты можешь отвечать только "да или нет"')
                continue

    elif ask_age <= 20 and ask_age > 15:
        duw = input(f"Емае,тебе {ask_age}\nты хочешь узнать первый вопрос? - ")
        if duw == 'да':
            print('Отлично!')
            print('Я задам тебе пару вопросов для твоего возраста')
            adult_questions_one(ask_age)
            print('')
            adult_questions_four(ask_age)
            print('')
            dul = input('Тебе понравилось? - ')
            if dul.lower() == 'да':
                print('Отлично,давай продолжим!')
                print('')
                adult_questions_three(ask_age)
                print('')
                print('Это были все мои вопросы,надеюсь тебя все понравилось!')
                break

            elif dul.lower() == 'нет':
                print('Эх, но у меня есть еще один вопрос,посмотри и на него,может тебе понравится')
                print('')
                adult_questions_two(ask_age)
                print('Это были все мои вопросы,надеюсь тебя все понравилось!')
                break
        else:
            print('Ты можешь отвечать только "да или нет"')
            continue












            # dul = input('Тебе понравилось? - ')
            # if dul.lower() == 'да':
            # print('Отлично,давай продолжим!')
            # print('')
            b  # aby_questions_three(ask_age)

            # elif dul.lower() == 'нет':
            # print('Эх, но у меня есть еще несколько вопросов,посмотри и на них,может тебе понравятся они')
            # print('')
            baby_questions_two(ask_age)
        # else:
        # print('Ты можешь отвечать только "да или нет"')
        # continue

        # baby_questions_two(ask_age)
        # baby_questions_three(ask_age)