class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Привет! Меня зовут {self.name}, мне {self.age} лет."

    def info(self):
        return f"Имя: {self.name}, возраст: {self.age} , пол: {self.gender}"


class Student(Person):
    def __init__(self, name, age, gender, university):
            super().__init__(name, age, gender)
            self.university = university

    def introduce(self):
            return f"Я студент {self.university}. Меня зовут {self.name} и мне {self.age} лет."
    def info(self):
            return f"{self.name}, {self.age} лет, учусь в {self.university}, пол: {self.gender}"

student = Student("Asman", 21, "man", "Ahjz")
print((student.introduce()))
print(student.info())



# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name    # имя
#         self.age = age      # возраст
#         self.gender = gender  # пол
#
#     def introduce(self):
#         return f"Привет! Меня зовут {self.name}, мне {self.age} лет."
#
#     def info(self):
#         return f"Имя: {self.name}, возраст: {self.age}, пол: {self.gender}"
#
#
# class Student(Person):   # Обязательно после Person!
#     def __init__(self, name, age, gender, university):
#         super().__init__(name, age, gender)
#         self.university = university   # новый атрибут — университет
#
#     # Полиморфизм — переопределяем метод
#     def introduce(self):
#         return f"Я студент {self.university}. Меня зовут {self.name}, и мне {self.age} лет."
#
#     def info(self):
#         return f"{self.name}, {self.age} лет, учусь в {self.university}, пол: {self.gender}"
#
#
# # Проверка
# student = Student("Алина", 20, "женский", "БГУ")
# print(student.introduce())
# print(student.info())
