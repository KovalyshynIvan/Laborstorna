def count_words(text):
    words = text.split()
    return len(words)

# Введення тексту від користувача
user_text = input("Введіть текст: ")

# Рахування слів у введеному тексті
word_count = count_words(user_text)

# Виведення результату,Цей код виводить на екран повідомлення, яке містить кількість слів у тексті.
# При цьому використовується метод форматування рядків за допомогою методу format.
print("Кількість слів у тексті: {}".format(word_count))