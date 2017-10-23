import time
import telepot
import re
import requests
import glob, os
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

upload = False
regex_check = False
download = False

welcome_message = """
Hey there!! Greetings from the Notes Sharing bot!
We provide you notes shared by your fellow classmates.
Hit the 'Upload or Download'!!!
"""
error_message = "You have entered an invalid option."
upload_message = """
Great! Now let's see what you want to upload here.
Before you upload a screenshot, please write the following information (#ModuleCode#lec/Tu/Lab#Description)
>> #cz1001#lec#your_description.
**** Don't forget that you can upload only lec, tut or lab ****
"""
download_message = """
Our bot will help youin finding the image by searching with #hashtags
>> #cz1001#lab. Don't worry, we will show the description of the image too.
"""

weclome_keyboardLayout = [
    [KeyboardButton(text='Upload'), KeyboardButton(text='Download')]
]
welcome_keyboard_markup = ReplyKeyboardMarkup(keyboard=weclome_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)

def mainHandler(msg):
    global upload, download, regex_check, hashTag
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if (content_type == 'text'):
        if (msg['text'] == 'Upload'):
            print(chat_id)
            bot.sendMessage(chat_id, upload_message)
            upload = True
        elif (msg['text'] == 'Download'):
            bot.sendMessage(chat_id, download_message)
            download = True
        elif (upload == True and re.match("^(#[A-Za-z]{2}\d{4})#(lab|lec|tut)#", msg['text'])):
            hashTag = msg['text']
            bot.sendMessage(chat_id, "Please upload a screenshot!")
            regex_check = True
        elif (download == True and re.match("^(#[A-Za-z]{2}\d{4})#(lab|lec|tut)", msg['text'])):
            downloadHandler(msg, chat_id)
        else:
            bot.sendMessage(chat_id,welcome_message, reply_markup=welcome_keyboard_markup)
            upload = False
            download = False
            regex_check = False
            
    elif (content_type == 'photo'):
        if (regex_check == True and upload == True):
            uploadHandler(msg, hashTag)
        else:
            bot.sendMessage(chat_id, welcome_message, reply_markup=welcome_keyboard_markup)
            upload = False
            download = False
            regex_check = False
    else:
        bot.sendMessage(chat_id, error_message)

def uploadHandler(msg, hashTag):
    #print(msg)
    file_id = msg['photo'][0]['file_id']
    file_path = msg['photo'][0]['file_path']
    download_path = "https://api.telegram.org/file/bot473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ/" + file_path
    
    if 'Files' in os.getcwd():
        bot.download_file(file_id, hashTag + ".jpg")
    elif 'Files' in os.listdir():
        os.chdir('./Files/')
        bot.download_file(file_id, hashTag + ".jpg")
    else:
        os.chdir('../Files/')
        bot.download_file(file_id, hashTag + ".jpg")

def downloadHandler(msg, chat_id):
    hashTag = msg['text']
    #print(os.getcwd())
    
    if 'Files' in os.getcwd():
        get_file(hashTag, msg)
    elif 'Files' in os.listdir():
        os.chdir('./Files/')
        get_file(hashTag, msg)
    else:
        os.chdir('../Files/')
        get_file(hashTag, msg)

def get_file(hashTag, msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    url = 'https://api.telegram.org/bot473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ/sendPhoto?chat_id=' + str(chat_id)
    #print(url)
    for file in glob.glob(hashTag + "*.*"):
        #print(file)
        files = {'photo': open(file, 'rb')}
        captions = {'caption': file[12:-4]}
        #print(caption['caption'])
        requests.post(url, files=files, data=captions)
    
bot = telepot.Bot('473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ')
MessageLoop(bot, mainHandler).run_as_thread()

# Keep the program running.
while 1:
    time.sleep(10)
