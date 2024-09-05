def get_human_development_stages():

  stages = []

  while True:

    stage = input("Введите следующий этап развития человека (или 'стоп' для завершения): ")
    stages.append(stage)

    if stage.lower() == 'homo sapiens sapiens':
      break

  print("Этапы развития человека: ", end="")
  print(*stages, sep=" => ")

if __name__ == "__main__":
  get_human_development_stages()