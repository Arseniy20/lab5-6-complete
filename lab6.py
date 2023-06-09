

def lab1():
    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                      "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                      "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава",
                      "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                      "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(countries_dict)
    cap = str(input("Введите страну: "))
    print(countries_dict[str(cap)])
    for i in sorted(countries_dict):
        print(i, "-", countries_dict[i])
lab1()


def lab2():
    a = input('Введите слово: ').upper()
    points = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10}
    score = 0

    for letter in a:
        score += points.get(letter, 0)

    print("Стоимость ", a, ":", score)
lab2()

def lab3():
    stud = {"Петров": {"Английский", "Китайский"},
            "Иванов": {"Китайский"},
            "Кашин": {"Французский", "Итальянский"},
            "Махичев": {"Испанский"},
            "Лопухов": {"Итальянский", "Испанский"},
            "Селюнина": {"Японский"}}
    language = []
    for i in stud.values():
        for j in i:
            language.append(j)
    language = list(set(language))
    language.sort()
    chinese = []
    for key, value in stud.items():
        if "Китайский" in value:
            chinese.append(key)
    print(*language)
    print(*chinese)

lab3()