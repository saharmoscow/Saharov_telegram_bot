import telebot
bot = telebot.TeleBot('2064427581:AAEW1RqfXbB8b35F9noZ-oxV1o1uIWYlJPU')
@bot.message_handler(content_types=['text'])
def getmessege(message):
    message.text
    if message.text = 'Привет':
        bot.send_message(message.from_user.id, 'Пока.')
    if message.text = 'Пока':
        bot.send_message(message.from_user.id, 'А ну я так и сказал.')
    if message.text = 'Семья':
        bot.send_message(message.from_user.id, 'Ты сказал семья? Нет ничего важнее семьи.')
    
