def lab1():
    import random
    l = [1, 2, 3, 4, 5]
    a = int(input('Введите число: '))
    if a in l:
        print('Поздравляю, вы угадали число!')
    else:
        print('Нет такого числа!')

lab1()


def lab2():
    list = [1, 1, 2, 3, 4, 5, 5, 6]
    print(*filter(lambda x: list.count(x) > 1, list))

lab2()

def lab3():
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    k = int(input('Введите желаемое число выходных: '))
    v = []
    r = []
    for i in range(0, k):
        v.insert(i, input('Введите выходной: '))
    for i in range(0, len(days)):
        for j in range(0, k):
            if days[i] != v[j]:
                if not days[i] in r:
                    r.append(days[i])
    print('Ваши выходные:', v, 'Кол-во:', k)
    print('Ваши рабочие дни:', r, 'Кол-во:', (7 - k))
lab3()


def lab4():
    import random
    com1 = ['Иванов', "Курицын", "Кораблев", "Алиев", "Венжега", "Лебедев", "Аджаров"]
    com2 = ["Абашин", "Скобиола", "Рямин", "Иванов", "Мацаковский", "Самедов", "Товмасян"]
    com3 = [random.sample(com1, 3) + random.sample(com2, 3)]

    print('Первая группа', *com1)
    print('Вторая группа', *com2)
    print('Спортивная команда ', *com3)

    name = input('Введите фамилию человека: ')
    if name in com3:
        print('Фамилия встречается в списке: ', com3.count('Иванов'))
    else:
        print('Такой фамилии нету в списке, НУЖНО БОЛЬШЕ ТАКИХ, МИЛОРД!')
lab4()






























