"""
# Name
#     MainHandler.py
# Version
#     1.0
# Created Date
#     10/24/2017
# Purpose
#     Perform the Logic Handling when there is an message from user
"""

import time
import telepot
import re
import requests
import glob, os
import uploadHandler as upload
import downloadHandler as download
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

"""
Set 3 boolean variables (upload, regex_check and download) as a flag.
We will set these three boolean variables to detect what's the user action.
  upload        - Upload switch
  download      - Download switch
  regex_check   - Regular expression switch
"""
upload = False
regex_check = False
download = False


# Custom message to display the user
welcome_message = """
Hey there!! Greetings from the Notes Sharing bot!
We provide you notes shared by your fellow classmates.
Hit the 'Upload or Download'!!!
"""
upload_message = """
Great! Now let's see what you want to upload here.
Before you upload a screenshot, please write the following information (#ModuleCode#lec/Tu/Lab#Description)
>> #cz1001#lec#your_description.
**** Don't forget that you can upload only lec, tut or lab ****
"""
download_message = """
Our bot will help you in finding the image by searching with #hashtags
>> #cz1001#lab. Don't worry, we will show the description of the image too.
"""
error_message = "You have entered an invalid option."

# Custom keyboard to display the user
weclome_keyboardLayout = [
    [KeyboardButton(text='Upload'), KeyboardButton(text='Download')]
]
welcome_keyboard_markup = ReplyKeyboardMarkup(keyboard=weclome_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)

"""
NAME
   MainHandler
PURPOSE
   Read the input data from user and call the corresponding procedure to execute
INPUTS
   msg - incoming message from user
PRE CONDITIONS
   upload, download and regex_check variable must declare under global namespace
Exception
   Exception will happen when the screenshot that user looking isn't available at the server.
"""
def mainHandler(msg):
    global upload, download, regex_check, hashTag
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if (content_type == 'text'):
        if (msg['text'] == 'Upload'):
            #print(chat_id)
            bot.sendMessage(chat_id, upload_message)
            # Need to set upload=True to for user action
            upload = True
        elif (msg['text'] == 'Download'):
            bot.sendMessage(chat_id, download_message)
            download = True
            upload = False
        elif (upload == True):
            if (re.match("^(#[A-Za-z]{2}\d{4})(#lab|#lec|#tut)#", msg['text'])):
                hashTag = msg['text']
                bot.sendMessage(chat_id, "Please upload a screenshot!")
                regex_check = True
            else:
                bot.sendMessage(chat_id, "You have used the wrong input")
        elif (download == True):
            try:
                download.downloadHandler(msg, chat_id)
            except Exception:
                bot.sendMessage(chat_id, "***No screenshot found\n Please try again***")
            else:
                bot.sendMessage(chat_id,welcome_message, reply_markup=welcome_keyboard_markup)
                download = False
        else:
            bot.sendMessage(chat_id,welcome_message, reply_markup=welcome_keyboard_markup)
            upload = False
            download = False
            regex_check = False
        
    elif (content_type == 'photo'):
        if (regex_check == True and upload == True):
            upload.uploadHandler(msg, hashTag + msg['caption'] if 'caption' in msg else hashTag, chat_id)
        else:
            upload = False
            download = False
            regex_check = False
        bot.sendMessage(chat_id, welcome_message, reply_markup=welcome_keyboard_markup)
    else:
        bot.sendMessage(chat_id, error_message, reply_markup=welcome_keyboard_markup)
    
bot = telepot.Bot('473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ')
MessageLoop(bot, mainHandler).run_as_thread()

# Keep the program running.
while 1:
    time.sleep(10)