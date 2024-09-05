def calculate_rectangle_area_and_perimeter(length, width):
  area = length * width
  perimeter = 2 * (length + width)
  return area, perimeter

if __name__ == "__main__":
  length = float(input("Введите длину прямоугольника: "))
  width = float(input("Введите ширину прямоугольника: "))

  area, perimeter = calculate_rectangle_area_and_perimeter(length, width)

  print(f"Площадь прямоугольника: {area}")
  print(f"Периметр прямоугольника: {perimeter}")