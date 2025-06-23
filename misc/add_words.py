from db.russian_words import words
"""
Вспомогательный скрипт для добавления слов из текстового файла в словарь
"""

with open('../db/russian_nouns.txt', 'r', encoding='utf-8') as file_in:
    for line in file_in:
        word = line.rstrip()
        if len(set(word)) == len(word):
            words.setdefault(len(word),set()).add(word)
print(words)
with open('../db/russian_words.py', 'w', encoding='utf-8') as file_out:
    file_out.write(f"words = {words}")