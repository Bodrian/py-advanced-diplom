# https://github.com/netology-code/py-advanced-diplom/blob/new_diplom/group_settings.md - инструкция по созданию групппы
from random import randrange

from tocken import token_vk_ms

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

#token = input('Token: ')
token = token_vk_ms

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")