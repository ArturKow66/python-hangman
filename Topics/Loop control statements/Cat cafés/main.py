name = ''
cats = 0
max_cats = 0
value_tuple = (name, cats)
values_list = list()

while True:
    value = input()
    value_tuple = value.split(' ')
    if value_tuple[0] == 'MEOW':
        break
    values_list.append(value_tuple)

for cat in values_list:
    if int(cat[1]) > max_cats:
        max_cats = int(cat[1])
        biggest_place = cat

print(biggest_place[0])
