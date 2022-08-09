# Завдання 1
# Файл: popularity.py Оцінка: 60

# Створіть функцію def popularity(text) яка приймає текст text і повертає унікальний массив строк відсортований за популярністью.

# Уявіть що вам надсилають текст роману чи вірша і хочуть побачити найбільш популярні слова які зустрічаються у цьому тексті.

# Для початку ви повинні розбити текст на слова. Слова розділені звичайними пробілами.
# В тексті не будуть використовуватись точки або коми.
# Регістр слів не повинен мати значення. Тобто 'Apple' і 'aPPle' - одне слово.
# При формуванні результуючого массива слово повинно бути конвертовано в нижній регістр(lovercase).
# Сортування повинно бути виконано від найпопулярніших слів до найменш популярних.
# Якщо слова мають однакову популярність, сортування повинно бути виконано за абеткою.
# Приклади:


def popularity(text):
    # регістр(lovercase).
    lower_text = text.lower()
    words_arr = lower_text.split(' ')
    words_counter = dict()
    for word in words_arr:
        if word in words_counter:
            words_counter[word] += 1
        else:
            words_counter[word] = 1

    # def get_second_key(item):
    #     return item[1]

    # def get_first_key(item):
    #     return item[0]

    # words_counter.items()  # -> [(apple, 1), (kiwi, 1), (pineapple, 1)]

    # sorted_by_words = sorted(words_counter.items(), key=lambda item: item[0])

    # sorted_by_popularity = sorted(sorted_by_word, key=get_second_key,



print(popularity('apple kiwi pineapple kiwi apple kiwi')) -> ['kiwi', 'apple', 'pineapple']
print(popularity('aPPle pine Apple kiwi Apple kiwi')) -> ['apple', 'kiwi', 'pine']
print(popularity('aPPle pine Apple kiwi Apple kiwi')) -> ['apple', 'kiwi', 'pine']
print(popularity('aab aaa aac aab aac aaa x')) -> ['aaa', 'aab', 'aac', 'x']
