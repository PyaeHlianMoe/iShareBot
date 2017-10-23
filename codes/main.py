import time
import telepot
import re
import requests
import glob, os
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

################################
# Set 3 boolean variables (upload, regex_check and download).
#     We will set these three boolean variables to detect what's the option that user choose.
#         upload        - Upload switch
#         download      - Download switch
#         regex_check   - Regular expression switch
################################
upload = False
regex_check = False
download = False


# Custom message to display the user
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
Our bot will help you in finding the image by searching with #hashtags
>> #cz1001#lab. Don't worry, we will show the description of the image too.
"""

# Custom keyboard to display the user
weclome_keyboardLayout = [
    [KeyboardButton(text='Upload'), KeyboardButton(text='Download')]
]
welcome_keyboard_markup = ReplyKeyboardMarkup(keyboard=weclome_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)

################################
# Name
#     MainHandler
# Version
#     1.0
# Created Date
#     10/24/2017
# Purpose
#     Perform the Logic Handling when there is an message from user
# Inputs
#     Pass the message from user as an input. This message will pass to the function as JSON object
# Exception
#     Exception handling doesn't require because it will keep repeating the user to choose the correct option
################################
def mainHandler(msg):
    global upload, download, regex_check, hashTag
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if (content_type == 'text'):
        if (msg['text'] == 'Upload'):
            #print(chat_id)
            bot.sendMessage(chat_id, upload_message)
            upload = True
        elif (msg['text'] == 'Download'):
            bot.sendMessage(chat_id, download_message)
            download = True
        elif (upload == True):
            if (re.match("^(#[A-Za-z]{2}\d{4})(#lab|#lec|#tut)#", msg['text'])):
                hashTag = msg['text']
                bot.sendMessage(chat_id, "Please upload a screenshot!")
                regex_check = True
            else:
                bot.sendMessage(chat_id, "You have used the wrong input")
        elif (download == True):
            downloadHandler(msg, chat_id)
            bot.sendMessage(chat_id,welcome_message, reply_markup=welcome_keyboard_markup)
        else:
            bot.sendMessage(chat_id,welcome_message, reply_markup=welcome_keyboard_markup)
            upload = False
            download = False
            regex_check = False
        
    elif (content_type == 'photo'):
        if (regex_check == True and upload == True):
            uploadHandler(msg, hashTag + msg['caption'] if 'caption' in msg else hashTag, chat_id)
        else:
            upload = False
            download = False
            regex_check = False
        bot.sendMessage(chat_id, welcome_message, reply_markup=welcome_keyboard_markup)
    else:
        bot.sendMessage(chat_id, error_message, reply_markup=welcome_keyboard_markup)
        

################################
# Name
#     UploadHandler
# Version
#     1.0
# Created Date
#     10/24/2017
# Purpose
#     Download the image to the filesystem and rename the filename in below format
#     (UserName_#moduleCode#content#description_date.jpg)
# Inputs
#     Pass the message from user as an input. This message will pass to the function as JSON object
# Exception
#     Exception handling doesn't require because it will keep repeating the user to choose the correct option
################################
def uploadHandler(msg, hashTag, chat_id):
    file_id = msg['photo'][-1]['file_id']
    userName = msg['chat']['username']
    date = str(msg['date'])
    
    if 'Files' in os.getcwd():
        bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    elif 'Files' in os.listdir():
        os.chdir('./Files/')
        bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    else:
        os.chdir('../Files/')
        bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    bot.sendMessage(chat_id, "Photo(s) have been uploaded successfully!")    
    #download_file(file_id, chat_id, userName, date, hashTag)

#def download_file(file_id, chat_id, userName, date, hashTag):
    #if 'Files' in os.getcwd():
        #bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
        ##
    #elif 'Files' in os.listdir():
        #os.chdir('./Files/')
        #bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    #else:
        #os.chdir('../Files/')
        #bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    #bot.sendMessage(chat_id, "Photo(s) have been uploaded successfully!")


################################
# Name
#     DownloadHandler
# Version
#     1.0
# Created Date
#     10/24/2017
# Purpose
#     Perform the Logic Handling when there is an message from user
# Inputs
#      Pass the message from user as an input. This message will pass to the function as JSON object
# Exception
#      Exception handling doesn't require because it will keep repeating the user to choose the correct option
################################
def downloadHandler(msg, chat_id):
    data = msg['text']
    
    if 'Files' in os.getcwd():
        get_file(data, msg, chat_id)
    elif 'Files' in os.listdir():
        os.chdir('./Files/')
        get_file(data, msg, chat_id)
    else:
        os.chdir('../Files/')
        get_file(data, msg, chat_id)

def get_file(data, msg, chat_id):
    url = 'https://api.telegram.org/bot473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ/sendPhoto?chat_id=' + str(chat_id)
    for file in glob.glob("*" + data + "*.*"):
        files = {'photo': open(file, 'rb')}
        captions = {'caption': ''.join(caption) for caption in re.compile('(#[A-Za-z]{2}\d{4})(#lab|#lec|#tut)(#.*)_').findall(file)}
        requests.post(url, files=files, data=captions)
    
bot = telepot.Bot('473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ')
MessageLoop(bot, mainHandler).run_as_thread()

# Keep the program running.
while 1:
    time.sleep(10)
