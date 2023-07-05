
import requests # библиотека для http запросов

key = '6f0c7d1074e54971f1600bf26730c816'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'APPID': key,'q': 'Москва','units': 'metric'}


request = requests.get(url, params=params)

result = request.json()
# print(result)
# print(result['main'])
code = result['cod']

if code != '401':
    if code != '404':
        data = result['main']

        print(f'Температура: {data["temp"]:.1f}\xB0C')

        print('Влажность', data['humidity'],'%')

        print(result['sys']['sunset'])
        raw_time_sunset = result['sys']['sunset']
        # print(datetime.utcfromtimestamp(raw_time_sunset).strftime("%H: %M"))
        print(f'Координаты:{result["coord"]["lon"]},{result["coord"]["lat"]}')
        if result['weather'][0]['main'] == 'Clouds':
                     print('Облачно')

else:
    print('Информации нет')



# import json #Java Script Object Notation
#
#
# with open('pets.json') as pet_file:
#        string = pet_file.read()
#        data = json.loads(string)
#
# for item in data:
#     if type(data[item]) == list:
#         print(item, ','.join(data[item]))
#     elif type(data[item]) == dict:
#         for k, v in data[item].items():
#              print(k,v)
#     else:
#         print(item, data[item])







    # for k, v in item.items():
     # print(k, v)
    # print(item)




# print(type(data['owner']))





















# pets = {
#     'name': 'Charly',
#     'age': 15,
#     'meals': ['Purina', 'Hills'],
#     'owner': {'fname': 'John', 'sname': 'Gates'}
# }
#
# with open('pets.json', 'w') as pet_file:
#     json.dump(pets, pet_file)
#
# # print(pet_file)

















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