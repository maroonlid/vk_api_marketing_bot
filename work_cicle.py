import vk_api
import time
import random
import requests
import bot_alphabet
from vk_api import VkUpload
import telebot
from telebot import types  # для указание типов
from requests.auth import HTTPProxyAuth
from datetime import datetime, date
import smtplib


def send_to_telegram(message):

    apiToken = '6512588978:AAE_M2JvYUXV8Av0ZOTEd08L804D_9gFhmo'
    chatID = '1215286915'
    chatID1 = '957045238'
    #chatID2 = '1058339360'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL , json={'chat_id': chatID, 'text': message})
        #response = requests.post(apiURL, json={'chat_id': chatID1, 'text': message})
        #response = requests.post(apiURL, json={'chat_id': chatID2, 'text': message})
        #print(response.text)
    except Exception as e:
        return



def get_info():
    print("Input phone number -", end=" ")
    number = input()
    print("Input accaunt password -", end=" ")
    password = input()
    print("Input time range (sec) -", end=" ")
    u_time = int(input())

    return number, password, u_time


def start_spam(number, password, u_time, post_time, run_id, sum_count):
    #s = requests.Session()
    #s.proxies.update({'http': 'http://92.249.13.243:63096:ekuduFMB:z2yZPavt'})

    try:
        vk_session = vk_api.VkApi(number, password, app_id=2685278)
        vk_session.auth()
    except:
        send_to_telegram("Пользователь - " + str(number) + " заблокирован ❌")
        return 0

    send_to_telegram("Авторизован в аккаунте - " + str(number))

    photo_path = bot_alphabet.get_image_path()

    vk = vk_session.get_api()

    upload = VkUpload(vk_session)  # Для загрузки изображений

    # Загрузка картинок на сервера вк и получение их id
    photos = [photo_path]
    try:
        photo_list = upload.photo_wall(photos)
    except:
        send_to_telegram("Пользователь - " + str(number) + " заблокирован ❌")
        return 0

    attachment = ','.join('photo{owner_id}_{id}'.format(**item) for item in photo_list)

    def standart_message(id, caption):
        vk_session.method("wall.post", {
            'owner_id': id,
            'message': caption,
            'attachment': attachment,
        })
        return "<Photo message was uploaded>"

    i = 0
    pause = random.randint(5, 13)

    current_datatime = datetime.now()
    send_to_telegram('--VK_elfbot начал работу--' + "  run_id - " + run_id)
    try:
        vk.wall.post(message='--VK_elfbot начал работу--' + "  run_id - " + run_id)
    except:
        return 0

    count = 0
    cond = True

    while cond:
        current_datatime = datetime.now()
        spam_time_check = True

        if spam_time_check:
            for j in range(len(bot_alphabet.groups_id_list)):
                message_status = bot_alphabet.groups_id_list[j]
                print("id -", bot_alphabet.groups_id_list[j])

                try:
                    print(standart_message(bot_alphabet.groups_id_list[j], bot_alphabet.get_text()))
                    send_to_telegram("id - " + str(bot_alphabet.groups_id_list[j]) + " <Сообщение с фото было опубликовано>")
                    time.sleep(post_time + random.randint(0, 3) + (random.randint(0, 10) / 10))
                except:
                    print("<<ОШИБКА>>")
                    send_to_telegram("<<ОШИБКА>>")

                count += 1
                if count == 95 + random.randint(0, 10):
                    return count
                if count % 10 == 0:
                    post_mess = "<Бот работает. Отправлено сообщений - " + str(count + sum_count) + ">  " + "run_id - " + run_id
                    print("<Бот работает. Отправлено сообщений - " + str(count + sum_count) + ">  " + "run_id - " + run_id)
                    send_to_telegram("<Бот работает. Отправлено сообщений - " + str(count + sum_count) + ">  " + "run_id - " + run_id)
                    #vk.wall.post(message=post_mess)


            if i == pause:
                print("<началась пауза>")
                send_to_telegram("<началась пауза>")
                sleep_time = abs(u_time + random.randint(-10, 10) + (random.randint(0, 10) / 10))
                time.sleep(sleep_time)
                #time.sleep(random.randint(40, 80) + (random.randint(0, 10) / 10))
                pause = random.randint(5, 13)
                i = 0

            i += 1