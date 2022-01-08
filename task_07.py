import re


def combine_anagrams(words_array):
    lst = []  # список для хранения слов в нижнем регистре
    for word in words_array:
        lst.append(word.lower())

    res = []  # итоговый список

    for el in lst:
        text = ' '.join(lst)  # преобразуем список в строку
        match = re.findall(r'\b[' + re.escape(el) + r']*\b',
                           text)  # используем регулярные выражения для поиска анаграмм
        match = list(filter(None, match))  # избавляемся от пустых элементов
        res.append(match)  # добавляем найденные анаграммы в итоговый список
        lst = [x for x in lst if x not in match]  # исключаем из дальнейшего анализа уже найденные анаграммы
    res = list(filter(None, res))  # избавляемся от пустых элементов
    return (res)


# TEST
# combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
