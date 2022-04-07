from tocken import token_vk_ms, token_vk_cl
from vk import Vk
from pprint import pprint

token = token_vk_cl
id = '1'

vk = Vk(token)

#получаю информацию о пользователе
res = vk.get_user_info(id)
if res == 'Error':
    print('Завершение работы')
else:
    print('Отслеживание процесса: Данные от ID получены')
    print(res.json())
    age = res.json()['response'][0]['bdate']
    print(f'\nДата рождения - {age}')
    birthday_year = int(age[-4:])
    print(f'Год рождения - {birthday_year}')
    sex = res.json()['response'][0]['sex']
    print(f'Пол - {sex} (1 - женский, 2 - мужской, 0 - пол не указан)')
    city_id = res.json()['response'][0]['city']['id']
    city_name = res.json()['response'][0]['city']['title']
    print(f'Город: номер id - {city_id}, название города - {city_name}')
    relation = res.json()['response'][0]['relation']
    print(f'Семейное положение - {relation} (1 — не женат/не замужем; 2 — есть друг/есть подруга; 3 — помолвлен/помолвлена; 4 — женат/замужем; 5 — всё сложно; '
          f'6 — в активном поиске; 7 — влюблён/влюблена; 8 — в гражданском браке; 0 — не указано.)')

#обработка информации о пользователя
if sex == 2:
    sex_partner = 1
elif sex == 1:
    sex_partner = 2

#выполняю поиск обьекта
res_search = vk.find_user(birthday_year, sex_partner, city_name, relation)

    # result = vk.select_best_foto(res)
    # print(f'Отслеживание процесса: Выбраны {len(result)} фото наилучшего разрешения')
    #pprint(result)
