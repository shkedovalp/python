"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('text3.txt', 'r') as my_file:
    lines = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов'
    for line, count in enumerate(my_file, 1)]
    print(*lines, f'Количество строк - {len(lines)}', sep = "\n")
