def get_pet_info():
  pet_type = input("Введите вид питомца: ")
  age = int(input("Введите возраст питомца: "))
  nickname = input("Введите кличку питомца: ")

  print(f"Это {pet_type} по кличке \"{nickname}\". Возраст: {age} года.")

if __name__ == "__main__":
  get_pet_info()