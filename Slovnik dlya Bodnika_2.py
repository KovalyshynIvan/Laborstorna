class Person:
    def __init__(self, name, surname, age, city, nation):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.nation = nation

    def get_attribute(self, attribute):
        return getattr(self, attribute, "Attribute not found")

class Person1(Person):
    pass

class Person2(Person):
    pass

person1 = Person1(name="Ivan", surname="Kovalyshyn", age=16, city="Lviv", nation="Ukrainian")
person2 = Person2(name="Max", surname="Afton", age=16, city="absent", nation="absent")

vocabulary = {"person1": person1, "person2": person2}

while True:
    i = input("What do You want to ask? [name/surname/age/city/nation/exit]")
    if i == "exit":
        print("OK")
        exit()
    else:
        for person_key, person_value in vocabulary.items():
            # Викликаємо метод get_attribute для отримання значення атрибуту
            print(f"{person_key}'s {i}: {person_value.get_attribute(i)}")
