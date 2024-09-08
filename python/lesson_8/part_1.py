import collections

pets = {}

def create():
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    pet_name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    pets[new_id] = {pet_name: {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}}
    print(f"Питомец с ID {new_id} добавлен.")

def read(pet_id):
    pet_info = get_pet(pet_id)
    if pet_info:
        pet_name = list(pet_info.keys())[0]
        species = pet_info[pet_name]["Вид питомца"]
        age = pet_info[pet_name]["Возраст питомца"]
        owner = pet_info[pet_name]["Имя владельца"]
        print(f"Это {species} по кличке \"{pet_name}\". Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {owner}")
    else:
        print(f"Питомец с ID {pet_id} не найден.")

def update(pet_id):
    pet_info = get_pet(pet_id)
    if pet_info:
        pet_name = list(pet_info.keys())[0]
        new_species = input("Новый вид питомца: ")
        new_age = int(input("Новый возраст питомца: "))
        new_owner = input("Новое имя владельца: ")
        pet_info[pet_name]["Вид питомца"] = new_species
        pet_info[pet_name]["Возраст питомца"] = new_age
        pet_info[pet_name]["Имя владельца"] = new_owner
        print(f"Информация о питомце с ID {pet_id} обновлена.")
    else:
        print(f"Питомец с ID {pet_id} не найден.")

def delete(pet_id):
    if pet_id in pets:
        del pets[pet_id]
        print(f"Питомец с ID {pet_id} удален.")
    else:
        print(f"Питомец с ID {pet_id} не найден.")

def get_pet(pet_id):
    return pets[pet_id] if pet_id in pets else False

def get_suffix(age):

    if age % 10 == 1 and age != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and not 12 <= age <= 14:
        return "года"
    else:
        return "лет"

def pets_list():
    for pet_id, pet_data in pets.items():
        pet_name = list(pet_data.keys())[0]
        print(f"ID: {pet_id}, Питомец: {pet_name}")

while True:
    command = input("Введите команду (create, read, update, delete, list, stop): ")
    if command == 'create':
        create()
    elif command == 'read':
        pet_id = int(input("Введите ID питомца: "))
        read(pet_id)
    elif command == 'update':
        pet_id = int(input("Введите ID питомца: "))
        update(pet_id)
    elif command == 'delete':
        pet_id = int(input("Введите ID питомца: "))
        delete(pet_id)
    elif command == 'list':
        pets_list()
    elif command == 'stop':
        break
    else:
        print("Неизвестная команда.")