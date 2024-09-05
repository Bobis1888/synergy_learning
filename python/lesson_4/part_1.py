def compress_spaces(text):
  return ' '.join(text.split())

text = "  Hello,            world!  I'm        Software       Developer        "
result = compress_spaces(text)
print(result)