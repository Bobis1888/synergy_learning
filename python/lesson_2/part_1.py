def count_vowels_and_consonants(word):
  vowels = 'aeiou'
  vowel_counts = {vowel: word.count(vowel) for vowel in vowels}
  consonants_count = len(word) - sum(vowel_counts.values())

  if not any(vowel_counts.values()):
    return False

  return vowel_counts, consonants_count

if __name__ == "__main__":
  word = input("Введите слово: ")
  result = count_vowels_and_consonants(word)

  if result is False:
    print("В слове нет ни одной из указанных гласных.")
  else:
    vowel_counts, consonants_count = result
    print("Количество гласных букв:")
    for vowel, count in vowel_counts.items():
      print(f"{vowel}: {count}")
    print(f"Количество согласных букв: {consonants_count}")