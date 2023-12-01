def unique_words(text):
    words = text.split()
    unique_set = set(words)
    return list(unique_set)

# Введення тексту від користувача
user_text = input("Введіть текст: ")

# Отримання унікальних слів
unique_word_list = unique_words(user_text)

# Виведення результату
print("Унікальні слова у тексті:", unique_word_list)