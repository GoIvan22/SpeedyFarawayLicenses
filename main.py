from tabulate import tabulate
goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
}
store = {
'12345': [
{'quantity': 27, 'price': 42},
],
'23456': [
{'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520},
],
'34567': [
{'quantity': 2, 'price': 1200},
{'quantity': 1, 'price': 1150},
],
'45678': [
{'quantity': 50, 'price': 100},
{'quantity': 12, 'price': 95},
{'quantity': 43, 'price': 97},
],
}

def coast(list):
  all_qua = 0
  all_pr = 0 
  for item in list:
    all_pr += item['quantity'] * item['price']
    all_qua += item['quantity']
  return all_qua, all_pr

new = []
for product, code in goods.items():
  quantity, price = coast(store[code])
  new.append([product, quantity, price])

print(tabulate(new, headers=['Товар',"Количество","Общая стоимость"], tablefmt='psql'))
  
  