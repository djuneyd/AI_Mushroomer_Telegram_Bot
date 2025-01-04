from telebot import TeleBot, types
from config import *
from AI_recognizer.AI_mushroom_recognizer import *
from Third_face_AIs.simple_gpt_yandex import *
import os, cv2

bot = TeleBot(TOKEN)
c1 = types.BotCommand(command='start', description='Start the Bot')
c2 = types.BotCommand(command='recognize', description='Recognize the mushroom')
bot.set_my_commands([c1,c2])

def more_info_markup(mushroom):
    # ask if the user wants to know more about the mushroom
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='More information', callback_data=f'more_info {mushroom}')
    markup.add(item1)
    return markup
    

def process_image(message):
    try:
        # download the image
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        #save the file on a local directory
        with open('image.jpg', 'wb') as f:
            f.write(downloaded_file)
        # load the image and predict the mushroom type
        cv2.imread('image.jpg')
        # animation of tasting
        bot.send_message(message.chat.id, 'Tasting your mushroom...')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAENIk9nOIl57NGge2VPFF3_Yr_6Y_UDWQACMR4AAoH_mUiXf6-WbGZNzDYE')
        result = Mushroom('image.jpg')
        # remove the downloaded file
        os.remove('image.jpg')
        # send the result and ask for more information
        bot.send_message(message.chat.id, f'''The mushroom you sent is a {result[0]}, with a confidence score of {result[1]}%.
It is {result[2]}
If you need more information about it, click the button below.😁''', reply_markup=more_info_markup(result[0]))
    except:
        bot.send_message(message.chat.id, 'I couldn\'t load the image. Please send a proper picture.🙏')
        bot.register_next_step_handler(message, process_image)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.set_chat_menu_button(message.chat.id, types.MenuButtonCommands('commands'))
    # greeting
    bot.send_message(message.chat.id, '''Hello, I'm Mushroomer!👋
I can help you identify and understand various types of mushrooms.🍄
I specialize in 20 types of mushrooms from around the world.🤓''')
    
@bot.message_handler(commands=['recognize'])
def recognize_the_mushroom(message):
    # asking for the image
    bot.send_message(message.chat.id, 'Please, send me a picture of a mushroom.🖼')
    
    # waiting for the image
    bot.register_next_step_handler(message, process_image)

# make a processing of callback data from inline keyboard markup
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if 'more_info' in call.data:
        # delete the markup sent
        call.data = call.data.replace('more_info ', '')
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        # animation of tasting
        bot.send_message(call.message.chat.id, 'Looking for more information...')
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAENIotnOLivH99K8YW5AWC-4rI1cVH0cwACCTUAAk4iWUmsmwAB8lLCDoo2BA')
        # get more information about the mushroom
        more_info = gpt(call.data, server, api_key)
        bot.send_message(call.message.chat.id, f'''More information about {call.data}:
{more_info}''')
    
if __name__ == '__main__':
    bot.infinity_polling()