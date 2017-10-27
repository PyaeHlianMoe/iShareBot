import os

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
################################
def uploadHandler(msg, hashTag, chat_id):
    file_id = msg['photo'][-1]['file_id']
    userName = msg['chat']['username']
    date = str(msg['date'])
    
    # if 'Files' in os.getcwd():
    #     bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    # elif 'Files' in os.listdir():
    #     os.chdir('./Files/')
    #     bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    # else:
    #     bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    if 'Files' in os.getcwd():
        bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    elif 'Codes' in os.getcwd():
        os.chdir('../Files/')
        bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    else:
        if not (os.path.isexist('./Files')):
            os.makedirs('./Files/')
        os.chdir('./Files')
        bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    bot.sendMessage(chat_id, "Photo(s) have been uploaded successfully!")