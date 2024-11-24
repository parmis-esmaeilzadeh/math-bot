import telebot
from config import API_TOKEN
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(API_TOKEN)


def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton(text="3D VIEW OF STRUCTURE-1 IN GEOGEBRA", callback_data="b1")
    b2 = InlineKeyboardButton(text="DARSNAME VA PORSESHNAME", callback_data="b2")
    b5 = InlineKeyboardButton(text="SECTIONS", callback_data="b5")
    b4 = InlineKeyboardButton(text="GUIDE TO WORKING WITH THE STRUCTURE", callback_data="b4")
    markup.add(b1, b2, b4, b5)

    return markup
def sections():
    markup = InlineKeyboardMarkup(row_width=1)
    bs1 = InlineKeyboardButton(text="TRIANGULAR PRISMS", callback_data="bs1")
    bs2 = InlineKeyboardButton(text="CONES", callback_data="bs2")
    bs3 = InlineKeyboardButton(text="RECTANGULAR PRISMS", callback_data="bs3")
    bs4 = InlineKeyboardButton(text="CYLINDERS", callback_data="bs4")
    bs5 = InlineKeyboardButton(text="RECTANGULAR PYRAMIDS", callback_data="bs5")
    bs6 = InlineKeyboardButton(text="TRIANGULAR PYRAMIDS", callback_data="bs6")
    bs7 = InlineKeyboardButton(text="SPHERES", callback_data="bs7")
    bs8 = InlineKeyboardButton(text="CUBE", callback_data="bs8")
    return_button = InlineKeyboardButton(text="Return", callback_data="return_to_main")
    markup.add(bs1, bs2, bs3, bs4, bs5, bs6, bs7, bs8, return_button)
    return markup

def sub1():
    markup = InlineKeyboardMarkup(row_width=1)
    # dshow = InlineKeyboardButton('Show', callback_data='show')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(return_button)

    return markup


####
def sub2():
    markup = InlineKeyboardMarkup(row_width=1)
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(return_button)
    return markup


###
# def sub3():
#     markup = InlineKeyboardMarkup(row_width=1)
#     return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
#     markup.add(return_button)
#     return markup


###
def sub4():
    markup = InlineKeyboardMarkup(row_width=1)
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(return_button)
    return markup


###
###
#call.data == 'show'
# @bot.callback_query_handler(func=lambda call: True)
#def ssub1(call):
    # bot.send_message(message.chat.id,
    #                  f'you can check the link below for more information\n link : https://www.geogebra.org/classic/we83tkje')
    # message_text = f"you can check the link below for more information\n link : https://www.geogebra.org/classic/we83tkje"
    # bot.send_photo(call.message.chat.id, expert_image, caption=message_text, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'b1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"you can check the link below for more information\n link : https://www.geogebra.org/classic/we83tkje", reply_markup=sub1())
        # if call.data == 'show':
        #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        #                           text="--->", reply_markup=ssub1())

    elif call.data == 'b2':
        a="http://localhost:63342/math_project1/htpart.html?_ijt=4dvadvh3ejf23i50dvvak30bs0"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"copy the link below and paste it at the chrome \n {a}", reply_markup=sub2())
    # elif call.data == 'b3':
    #     bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
    #                           text="b3", reply_markup=sub3())
    elif call.data == 'b4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="With the help of each syringe, you can separate different parts of the cube from each other. \n"
                                   "You can also find the size of the angles, the surface area, or the volume of the section you want in the figure with a protractor, ruler, or...",
                              reply_markup=sub4())
    elif call.data == 'b5':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="choose one of these shapes",reply_markup=sections())
    elif call.data == "bs1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="https://www.geogebra.org/classic/xwGbTuzE",reply_markup=sub2())
    elif call.data == "bs2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="https://www.geogebra.org/classic/gxeyxttc",reply_markup=sub2())
    elif call.data == "bs3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="https://www.geogebra.org/classic/HSgSE469",reply_markup=sub2())
    elif call.data == "bs4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="https://www.geogebra.org/classic/gGb5eNDc",reply_markup=sub2())
    elif call.data == "bs5":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="https://www.geogebra.org/classic/NywUsyXp",reply_markup=sub2())
    elif call.data == "bs6":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="https://www.geogebra.org/classic/P8CyNCPb",reply_markup=sub2())
    elif call.data == "bs7":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="https://www.geogebra.org/classic/ZHaaZ7E4",reply_markup=sub2())
    elif call.data == "bs8":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="https://www.geogebra.org/classic/vb2cxf9r",reply_markup=sub2())
    elif call.data == 'return_to_main':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You are in main menu. Choose an option:", reply_markup=main_menu())


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     f"Welcome to the supplementary part of the decade of mathematics project. 😄 \nSelect the part of the cube you want to view from the options below.",
                     reply_markup=main_menu())


bot.polling()
