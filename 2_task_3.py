#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = input('Введите месяц, в виде целого числа от 1 до 12: ')
word = words.split(' ')
for i, word in enumerate(word):
    print(i + 1, word[:10])