import json #Java Script Object Notation



pets = {
    'name': 'Charly',
    'age': 15,
    'meals': ['Purina', 'Hills'],
    'owner': {'fname': 'John', 'sname': 'Gates'}
}

with open('pets.json', 'w') as pet_file:
    json.dump(pets, pet_file)

# print(pet_file)

















# weekdays = ['Понедельник', 'Вторник','Среда', 'Четверг',
#             'Пятница', 'Суббота', 'Воскресенье']
#
# st = [i for i in range(1, 6)]
#
#
# week_dict = {key: val for key, val in enumerate(weekdays)}
# print(week_dict)
#
# data = json.dumps(week_dict)
# print(data)