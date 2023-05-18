def magic(string):
  dt = {}
  for i in string:
    if i in string:
      dt[i] = 'count(string[i])'

  return dt


text = input('введите текст ')
x = magic(text)
print(x)
