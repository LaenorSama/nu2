# отрабатываем условия
user_answer = input('В каком году родился А.С.Пушкин?')
# переведем ответ в нижний регистр
user_answer = user_answer.lower()
# сделаем список верных ответов
correct_answer = ['1799', 'в 1799',
                  'тысяча семьсот девяносто девять',
                  'одна тысяча семьсот девяносто девять',
                  'тысяча семьсот девяносто девятом'
                  'одна тысяча семьсот девяносто девятом',
                  'в тысяча семьсот девяносто девятом',
                  'в одна тысяча семьсот девяносто девятом']
if user_answer in correct_answer:
    print('Верно')
else:
    print('Неверно')