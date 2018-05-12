import re

def get_answer(question, answers):
    reg_mask = re.compile('[^а-яА-Я0-9 ]')
    q = reg_mask.sub('', question)
    question_lower = q.lower()
    answer = answers.get(question_lower, ['не понимаю', 0])

    return answer


answers = {'привет': ['И тебе привет!', 0],
           'как дела': ['Норм', 0],
           'пока': ['Пока, пока!', 1],
           'здравствуйте': ['Добрый день!', 0],
           'что делаешь': ['Болтаю с тобой:)', 0],
           'что нового': ['День стал длиннее', 0],
           'до свидания': ['Всего доброго!', 1],
           'не понимаю': ['не понимаю', 0]}
inc = 0
exit_flag = 0
while exit_flag != 1:
    inc = inc + 1
    question = input('человек: ')
    ans = get_answer(question, answers)
    print('машина: ' + ans[0])
    exit_flag = ans[1]
    if inc == 10:
        exit_flag = 1
        print('машина: мне пора!')

