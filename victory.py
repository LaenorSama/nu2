# список вопросов
questions = ['В каком году родился Хидэо Кодзима?',
             'В каком году родился Хаяо Миядзаки?',
             'В каком году родился Стив Джобс?',
             'В каком году родился Джон Рональд Руэл Толкин?',
             'В каком году родился Ник Перумов?']
# правильные ответы
answers = [1963, 1941, 1955, 1892, 1963]
# kojima = 1963
# miyazaki = 1941
# jobs = 1955
# tolkien = 1892
# perumov = 1963

# приветствуем игрока и объясняем правила
print('Добро пожаловать в нашу викторину!')
print('ВАЖНО! Ответы писать цифрами!')

# заведем переменную указывающую желает игрок играть или нет
wish_play = 'да'

while wish_play != 'нет':
    # заведем счетчик правильных ответов игрока
    user_score = 0
    # так же счетчик неправильных ответов
    user_fail = 0
    # задаем вопросы
    for i in range(len(questions)):
        print('Вопрос', i + 1)
        user_answer = int(input(questions[i]))
        if user_answer == answers[i]:
            user_score += 1
            print('Верно! :D')
        else:
            user_fail += 1
            print('Неверно! :(')
    # выводим результаты
    print('Верных ответов:', user_score)
    print('Неверных ответов:', user_fail)
    # выводим в %
    print('% верных ответов', user_score / len(questions) * 100)
    print('% неверных ответов', user_fail / len(questions) * 100)
    wish_play = input('Начнем сначала?')
    wish_play = wish_play.lower()