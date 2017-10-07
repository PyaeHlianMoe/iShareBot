#!/usr/bin/env python3

#import sys
import time
import telepot
#import json
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

welcome_message = "Welcome to iShareBot\nPlease select an option from keyboard"
error_message = "You have enter an invalid option."
weclome_keyboardLayout = [[KeyboardButton(text='/Upload'), KeyboardButton(text='/Download')]]
upload_keyboardLayout = [[KeyboardButton(text=""), KeyboardButton(text="")]]

def main_handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    welcome_keyboard_markup = ReplyKeyboardMarkup(keyboard=weclome_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)
    
    #if content_type == 'text' and msg['text'] != 'Upload':
        #bot.sendMessage(chat_id,welcome_message, reply_markup=welcome_keyboard_markup)
    #elif content_type == 'text' and msg['text'] == 'Upload':
        #upload_handle(msg)
    #else:
        #bot.sendMessage(chat_id, error_message)
    if (content_type == 'text'):
        if (msg['text'] == '/Upload'):
            bot.sendMessage(chat_id, "Please enter a module code")
            bot.sendMessage(chat_id, "Please enter a ")
            upload_handle()
        elif (msg['text'] == '/Download'):
            download_handle(msg)
        else:
            bot.sendMessage(chat_id,welcome_message, reply_markup=welcome_keyboard_markup)

def upload_handle():
    #content_type, chat_type, chat_id = telepot.glance(msg)
    
    #bot.sendMessage(chat_id, "glad to enter")
    
    ## TODO - handle for the upload
    ## Need 3 arguments. Module code, category and datetime
    
    response = bot.getUpdates()
    pprint(response)

def download_handle():
    ## TODO - handle for the download.
    ## 
    print ("Download handle")
    
bot = telepot.Bot('473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ')
MessageLoop(bot, main_handle).run_as_thread()

# Keep the program running.
while 1:
    time.sleep(10)
