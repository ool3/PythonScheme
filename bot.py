print('Привет!\nНапиши что-нибудь и мы начнём.')
answer = str(input())
while answer != 'пока':
    print('Как дела?')
    answer = input()
    if 'хорошо' in answer or 'отлично' in answer or 'не плохо' in answer:
        print('Отлично!Я рад за тебя.')
    elif 'плохо' in answer or 'так себе' in answer:
        print('Ничего, скоро всё наладиться!')
    print('Вы программист?')
    answer = input()
    if 'да' in answer:
        print('Ура!\nВы можете создать мне друга.')
    elif 'нет' in answer:
        print('Почему бы не попробовать себя в этой профессии?')
    print('Хотели бы вы работать в Яндекс?')
    answer = input()
    if answer == 'да':
        print('Это отличное место работы!')
    elif answer == 'нет':
        print('Хорошо, для вас открыты много других компаний.')
    print('Как вы видёте образ жизни?(сидячий , малоподвижный , активный)')
    answer = input()
    if answer == 'сидячий':
        print('Советую вам пройтись.')
    elif answer == 'малоподвижный':
        print('Сделайте зарядку.')
    elif answer == 'активный':
        print('Вы держите себя в форме!\nТак держать!')
print('Если захочется поговорить, заходи ещё')
