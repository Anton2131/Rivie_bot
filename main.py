import telebot
from weather import reply
#Token = 1683166348:AAFQTIehnJ9Ngt52rI7kbH9bQS1XbOECxVU

bot  = telebot.TeleBot('1683166348:AAFQTIehnJ9Ngt52rI7kbH9bQS1XbOECxVU')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Вика', 'Антон', 'Гвен', 'Ривер', 'Погода')

@bot.message_handler(commands=['start', 'help'])
def star_message(message):
    bot.send_message(message.chat.id, 'Привет, я - Иви', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'вика':
        bot.send_message(message.chat.id, 'Вика - это моя мама')
    elif message.text.lower() == 'антон':
        bot.send_message(message.chat.id, 'Антон - мой папа')
    elif message.text.lower() == 'гвен':
        bot.send_message(message.chat.id, 'А Гвени - моя дочка, я ей уши обычно грызу')
    elif message.text.lower() == 'ривер':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAN_YENp55HzH6d7X4Cl_ljOtoBjm2wAAtwHAAJG-6wEBMYgMiaj-t8eBA')
    elif message.text.lower() == 'погода':
        bot.send_message(message.chat.id, reply)
    else:
        bot.send_message(message.chat.id, message.text)
    
@bot.message_handler(content_types=['sticker'])
def answer_sticker(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

'''
@bot.message_handler(content_types=['sticker])
def sticker_info(message):
    bot.send_message(message.chat.id, message.sticker.file_id)
'''

bot.polling()