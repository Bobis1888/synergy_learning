def add_pet(pets):
    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[name] = {
        'Вид питомца': species,
        'Возраст питомца': age,
        'Имя владельца': owner
    }


def get_pet_info(pets, pet_name):
    pet_info = pets[pet_name]
    age = pet_info['Возраст питомца']

    if age % 10 == 1 and age != 11:
        year_word = "год"
    elif 2 <= age % 10 <= 4 and not 12 <= age <= 14:
        year_word = "года"
    else:
        year_word = "лет"

    return f"Это {pet_info['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {age} {year_word}. Имя владельца: {pet_info['Имя владельца']}"


pets = {}

print("Добавьте информацию о питомце")
add_pet(pets)

print("Добавьте информацию о питомце")
add_pet(pets)

name = input("Введите имя питомца для получения информации:")

print(get_pet_info(pets, name))