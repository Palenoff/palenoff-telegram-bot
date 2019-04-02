import telebot
import responses
import keyboards
import commands
import os

bot = telebot.AsyncTeleBot(os.environ["TOKEN"])
#logging.basicConfig(filename='messages.log')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, "Привет!\nЯ Бот Палёныч!\n" + 
                     "Кирилл решил доверить мне высокую миссию: " + 
                     "представить его как добросовестного сотрудника и хорошего человека!\n" + 
                     "Что ж, надеюсь, я сумею оправдать Ваши ожидания😏\n" + 
                     "Пожелайте мне удачи!🙏", reply_markup=keyboards.start_markup)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.from_user.id,responses.responses["помощь"]["reply"])

@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_message(message.from_user.id,responses.responses["о боте"]["reply"])

def send_message(message, response):
    bot.send_message(message.chat.id,response["reply"],reply_markup=response["markup"])

def handle_command(message,messagetext):
    if messagetext == "помощь":
        handle_help(message)
    elif messagetext == "о боте":
        handle_about(message)
    elif messagetext == "назад":
        handle_back(message)
    else:
        send_message(message,responses.responses[messagetext])


@bot.message_handler(content_types=['text'])
def handle_message(message):
    print("Зарос:")
    print(message.json)
    #logging.debug(datetime.datetime.now())
    #logging.debug(message.json)
    messagetext = message.text.lower()
    if messagetext in responses.responses.keys():
        print("Распознан как Команда: " + messagetext)
        handle_command(message,messagetext)
    else:
        print("Распознан как Текст: " + messagetext)
        reply = commands.parse_text(messagetext)
        if reply is None:
            reply = "На данный момент я не обладаю подобной информацией!\nНо не переживайте!\nВаш вопрос записан в лог, и скоро я узнаю ответ на него!"
            print("Текст не распознан")
            #logging.info(messagetext)
        print("Ответ: " + reply)
        bot.send_message(message.chat.id, reply)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        print("Инлайновый запрос")
        print("Нажата кнопка: " + call.data)
        print("Источник запроса: ")
        print(call.message.json)
        #logging.debug(datetime.datetime.now())
        #logging.debug(call.message.json)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=responses.responses[call.data]["reply"],reply_markup=responses.responses[call.data]["markup"])
            #bot.send_message(chat_id=call.message.chat.id, text="Сообщение отправилось из нормального сообщения об образовании")

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as ex:
        print(ex.args)
        #logging.critical(datetime.datetime.now())
        #logging.critical(ex.args)

#bot.polling(none_stop=True,interval=0)