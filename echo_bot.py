import telebot
from telebot import types
import os


bot = telebot.TeleBot("2086054651:AAF_PuqicSmPFdvWMkFIaSXobKmElwL5A7c", parse_mode=None) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello!!!")

help_cnt = 0
@bot.message_handler(commands=['help'])
def send_welcome(message):
    global help_cnt
    if help_cnt < 1:
        bot.reply_to(message, "Type 'Hi' or anything else")
        help_cnt += 1
    else:
        bot.reply_to(message, "No more help")


@bot.message_handler(commands=['newtodo'])
def create_point(message):
    bot.send_message(message.from_user.id, "one more...")
    bot.send_message(message.from_user.id, "Ok, write")
    bot.register_next_step_handler(message, addtolist)
    
def addtolist(message):
    with open('todolist.txt', 'a') as f:
        print(message.text, file = f)
    bot.send_message(message.from_user.id, "Your list has become longer")

# from new_f import new_funk

@bot.message_handler(commands=['deletepoint'])
def delete_point(message):
    bot.send_message(message.from_user.id, "Congratulations!")
    bot.send_message(message.from_user.id, "What would you like to delete?")
    # new_funk()
    bot.register_next_step_handler(message, delfromlist)
    
def delfromlist(message):
    flag = False
    with open('todolist.txt', 'r') as tdl:
        with open('tmp.txt', 'w') as tmp:
            for line in tdl:
                if line.lstrip('-').strip().lower() != message.text.lstrip('-').strip().lower():
                    tmp.write(line)
                else:
                    flag = True
    os.replace('tmp.txt', 'todolist.txt')
    if flag:
        bot.send_message(message.from_user.id, "Your list has become shorter")
    else:
        bot.send_message(message.from_user.id, "It was not in the list")
    f = open("tmp.txt","w")
    f.close()



@bot.message_handler(commands=['output'])
def output_(message):
    bot.send_message(message.from_user.id, "okey, have a look")
    with open('todolist.txt', 'r') as tdl:
        
        for line in tdl:
            bot.send_message(message.from_user.id, "- "+line)


name = '';
surname = '';
hi_cnt = 1

@bot.message_handler(content_types=['text'])
def start(message):
    global hi_cnt
    if message.text == '/makefriends':
        bot.send_message(message.from_user.id, "Your name?");
        bot.register_next_step_handler(message, get_name)
    elif message.text == "Hi":
        hi_message = " hi" * hi_cnt
        bot.send_message(message.from_user.id, "Hi"+hi_message)
        hi_cnt += 1
    else:
        bot.reply_to(message, message.text+"\n"+"\n"+"if you wanna be friends, type /makefriends")
    

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Surname?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    surname = message.text
    
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, 'Hi, '+name+' '+surname+'!', reply_markup=keyboard)



@bot.message_handler(content_types=['document'])
def handle_text_doc(message):
    bot.reply_to(message, "Here is a document, right?")


bot.infinity_polling()



