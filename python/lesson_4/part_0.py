def is_palindrome(text):
  text = ''.join(filter(str.isalnum, text)).lower()
  return text == text[::-1]

text = input("Введите строку: ")

if is_palindrome(text):
  print("yes")
else:
  print("no")