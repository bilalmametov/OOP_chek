# task1
from datetime import datetime, timedelta

class CreateMixin:
    def create(self, key, todo):
        if key in self.todos:
            return "Задача под таким ключём уже существует"
        else:
            self.todos[key] = todo
            return f"Задача с ключом {key} добавлена"

class DeleteMixin:
    def delete(self, key):
        if key in self.todos:
            task_name = self.todos[key]
            del self.todos[key]
            return f"Удалили задачу '{task_name}'"
        else:
            return "Задачи с таким ключом не существует"

class UpdateMixin:
    def update(self, key, new_value):
        if key in self.todos:
            self.todos[key] = new_value
            return f"Задача с ключом {key} обновлена"
        else:
            return "Задачи с таким ключом не существует"

class ReadMixin:
    def read(self):
        sorted_tasks = sorted(self.todos.items(), key=lambda x: x[0])
        return [f"{key}: {value}" for key, value in sorted_tasks]

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    def __init__(self):
        self.todos = {}

    def set_deadline(self, deadline):
        # Ваш код для вычисления количества дней до дедлайна
        # Здесь можно использовать модуль datetime
        today = datetime.today()
        deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
        days_left = (deadline_date - today).days
        return days_left

# Пример использования
todo_instance = ToDo()
print(todo_instance.set_deadline("31/12/2021"))

todo_instance.create("key1", "Complete assignment")
todo_instance.create("key2", "Prepare for exam")

print(todo_instance.read())

todo_instance.update("key1", "Finish project")
print(todo_instance.read())

print(todo_instance.delete("key2"))
print(todo_instance.read())


# task2
class Person:
    def __init__(self):
        self._name = None
        self._last_name = None
        self._age = None
        self._email = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value


john = Person()


print(f"Name: {john.name}")
print(f"Last Name: {john.last_name}")
print(f"Age: {john.age}")
print(f"Email: {john.email}")

john.name = "John"
john.last_name = "Doe"
john.age = 25
john.email = "john.doe@example.com"


print(f"Name: {john.name}")
print(f"Last Name: {john.last_name}")
print(f"Age: {john.age}")
print(f"Email: {john.email}")

# task3
class Dog:
    def voice(self):
        print("Гав")

class Cat:
    def voice(self):
        print("Мяу")

def to_pet(pet):
    pet.voice()


rex = Dog()
barsik = Cat()

to_pet(barsik)
to_pet(rex)
