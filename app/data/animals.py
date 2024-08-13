import json
from app.data import list_files, open_files

def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal not in animals:
        animals.append(animal)
        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)
        msg = f"Тварину '{animal}' успішно додано."
    else:
        msg = f"Тварина '{animal}' вже є у списку."

    return msg

def cured_animal(animal: str) -> str:
    animals = open_files.get_animals()
    cured_animals = open_files.get_cured_animals()

    if animal in animals:
        animals.remove(animal)
        cured_animals.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        with open(list_files.cured_animals, "w", encoding="utf-8") as file:
            json.dump(cured_animals, file)

        msg = f"Тварину '{animal}' успішно вилікувано."
    else:
        msg = f"Тварина '{animal}' відсутня у списку."

    return msg

def remove_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        animals.remove(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        msg = f"Тварину '{animal}' успішно видалено."
    else:
        msg = f"Тварина '{animal}' відсутня у списку."

    return msg

# class Animal:
#     type = "Animal"

#     def __init__(self, weight: float):
#         print("Call __init__ method")
#         self.weight = weight

#     def eating(self):
#         print(f"{self.type}: Я їм їжу...")
#         self.weight += 0.5

#     def run(self):
#         print(f"{self.type}: Я біжу ->")
#         self.weight -= 0.3


# class Dog(Animal):
#     type = "Dog"

#     def bark(self):
#         print(f"{self.type} say: Bark, bark!")

#     def run(self):
#         print(f"{self.type}: Я біжу ->")
#         self.weight -= 0.4


# class Cat(Animal):
#     type = "Cat"

#     def meow(self):
#         print(f"{self.type} say: Meow...mrrrrrrr")


# class Paw:
#     def eating(self):
#         print("Я лапою їм їжу...")

#     def up(self):
#         print("Я підняв ляпу...")

#     def down(self):
#         print("Я опускаю лапу...")


# class BlackDog(Dog):
#     paw = Paw()


# # dog = Dog(7)
# # cat = Cat(2.6)

# dog = BlackDog(7)
# dog.paw.down()

# dog.bark()
