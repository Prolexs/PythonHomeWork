vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

def count_syllables(word):
    syllables = 0
    prev_vowel = False

    for char in word.lower():
        if char in vowels:
            if not prev_vowel:
                syllables += 1
            prev_vowel = True
        else:
            prev_vowel = False

    # Учтем особые случаи
    if word.lower().endswith('е'):
        syllables -= 1
    if word.lower().endswith('ле'):
        syllables += 1

    return syllables

def check_rhythm(poem):
    lines = poem.split(" ")
    syllables = []

    for line in lines:
        words = line.split("-")
        total_syllables = 0

        for word in words:
            total_syllables += count_syllables(word)

        syllables.append(total_syllables)

    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

# Инструкция для пользователя
print("Введите стихотворение Винни-Пуха, разделяя фразы пробелами и слова внутри фраз дефисами.")
print("Например, 'Фраза1-фраза2 фраза3-фраза4-фраза5'.")
print()

# Ввод стихотворения от пользователя
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)




