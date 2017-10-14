#!/usr/bin/env python3

import time
import telepot
import re
import csv
import urllib.request
import base64
#import xlsxwriter
import os
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

upload = False
regex_check = False

welcome_message = "Welcome to iShareBot\nPlease select an option from keyboard"
error_message = "You have enter an invalid option."
hash_tag_message = "Please enter a hash_tag: (e.g. #cz1001#lec)\nPlease take note that maximum two hash_tags."

weclome_keyboardLayout = [
    [KeyboardButton(text='Upload'), KeyboardButton(text='Download')]
]
welcome_keyboard_markup = ReplyKeyboardMarkup(keyboard=weclome_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)

def mainHandler(msg):
    global upload, download, regex_check, hashTag
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if (content_type == 'text'):
        if (msg['text'] == 'Upload'):
            bot.sendMessage(chat_id, hash_tag_message)
            upload = True
        elif (msg['text'] == 'Download'):
            bot.sendMessage(chat_id, hash_tag_message)
            download = True
        elif (re.match("^(#[A-Za-z]{2}\d{4})#(lab|lec|tut)$", msg['text'])):
            if (upload == True):
                hashTag = msg['text']
                bot.sendMessage(chat_id, "Please upload a screenshot!")
                regex_check = True
            elif (download == True):
                downloadHandler(msg)
            else:
                bot.sendMessage(chat_id, welcome_message, reply_markup=welcome_keyboard_markup)
        else:
            bot.sendMessage(chat_id,welcome_message, reply_markup=welcome_keyboard_markup)
    elif (content_type == 'photo'):
        if (regex_check == True):
            if (upload == True):
                uploadHandler(msg, hashTag)
                #upload = False
                #regex_check = False
            else:
                bot.sendMessage(chat_id, "Please upload a screenshot!!")
        else:
            bot.sendMessage(chat_id, welcome_message)
            #upload = False
            #download = False
        
        upload = False
        download = False
        regex_check = False
    else:
        bot.sendMessage(chat_id, error_message)

def uploadHandler(msg, hashTag):
    file_id = msg['photo'][0]['file_id']
    file_path = msg['photo'][0]['file_path']
    download_path = "https://api.telegram.org/file/bot473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ/" + file_path
    os.chdir('../Files/')
    bot.download_file(file_id, hashTag + ".jpg")

def downloadHandler(msg):
    print ("Download handle")


def save_file(description):
    print("Save the file")







bot = telepot.Bot('473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ')
MessageLoop(bot, mainHandler).run_as_thread()

# Keep the program running.
while 1:
    time.sleep(10)
