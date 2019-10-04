# отрабатываем условия

# сделаем списки верных ответов
# год
correct_answer_year = ['1799', 'в 1799',
                       'тысяча семьсот девяносто девять',
                       'одна тысяча семьсот девяносто девять',
                       'тысяча семьсот девяносто девятом',
                       'одна тысяча семьсот девяносто девятом',
                       'в тысяча семьсот девяносто девятом',
                       'в одна тысяча семьсот девяносто девятом']
# день
correct_answer_day = ['26 мая',
                      '26.05',
                      'двадцать шестое мая',
                      'двадцать шестого мая']
while 1:
    user_answer_year = input('В каком году родился А.С.Пушкин?')
    # переведем ответ в нижний регистр
    user_answer_year = user_answer_year.lower()
    if user_answer_year in correct_answer_year:
        while 1:
            user_answer_day = input('А в какой день?')
            # переведем ответ в нижний регистр
            user_answer_day = user_answer_day.lower()
            if user_answer_day in correct_answer_day:
                print('Верно')
                break
            else:
                print('Неверно. Попробуй еще раз.')
        break
    else:
        print('Неверно. Попробуй еще раз.')