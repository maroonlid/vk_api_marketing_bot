import vk_api
from vk_api import VkUpload
from datetime import datetime
import os
import work_cicle
import random
import bot_alphabet
from datetime import datetime, date
import time


#bot.polling(none_stop=True)

print("--Программа начала работу--")
print(" ")

def main():

    sum_count = 0
    cond = True
    u_time = 100
    while cond:
        current_datatime = datetime.now()
        run_id = bot_alphabet.get_line(6) + "_" + str(current_datatime)[:11]

        while True:
            current_datatime = datetime.now()
            if (current_datatime.hour % 2 == 0 and current_datatime.hour > 7):
                if current_datatime.minute < 40:
                    break
            if current_datatime.hour == 16:
                break

        bot_alphabet.list_number, bot_alphabet.list_password = bot_alphabet.map_transl_func()

        try:
            bot_alphabet.list_number.remove('')
        except:
            print("ok")
        print("ok")

        for i in range(len(bot_alphabet.black_number)):
            try:
                bot_alphabet.list_number.remove(bot_alphabet.black_number[i])
            except:
                pass
            try:
                bot_alphabet.list_password.remove(bot_alphabet.black_password[i])
            except:
                pass

        print(bot_alphabet.list_number)
        print(bot_alphabet.list_password)

        print("ok")
        if len(bot_alphabet.list_number) == 0:
            work_cicle.send_to_telegram("--ожидание нового аккаунта--")
            while len(bot_alphabet.list_number) == 0:
                time.sleep(10)
                bot_alphabet.list_number, bot_alphabet.list_password = bot_alphabet.map_transl_func()
                try:
                    bot_alphabet.list_number.remove('')
                except:
                    pass
                print("ok")

                for i in range(len(bot_alphabet.black_number)):
                    try:
                        bot_alphabet.list_number.remove(bot_alphabet.black_number[i])
                    except:
                        pass
                    try:
                        bot_alphabet.list_password.remove(bot_alphabet.black_password[i])
                    except:
                        pass


        acc_index = 0
        print("ok ")
        new_count = work_cicle.start_spam(number=bot_alphabet.list_number[acc_index], password=bot_alphabet.list_password[acc_index], u_time=u_time, post_time=18, run_id=run_id, sum_count=sum_count)
        sum_count += new_count
        bot_alphabet.black_number.append(bot_alphabet.list_number[acc_index])
        bot_alphabet.black_password.append(bot_alphabet.list_password[acc_index])


        work_cicle.send_to_telegram("АККАУНТОВ ОСТАЛОСЬ - " + str(len(bot_alphabet.list_number)))

        print("-" * 24)
        print("АККАУНТОВ ОСТАЛОСЬ - " + str(len(bot_alphabet.list_number)))
        print("-" * 24)
        work_cicle.send_to_telegram("--началась пауза--")
        time.sleep(random.randint(0, 6) + (random.randint(0, 10) / 10))


if __name__ == '__main__':
    main()