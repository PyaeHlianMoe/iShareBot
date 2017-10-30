import os
import telegram_config

################################
# Name
#     uploadHandler
# Version
#     1.0
# Created Date
#     10/24/2017
# Purpose
#     Download the image to the filesystem and rename the photo inlcuding username & time with below format
#     Format  - <username>_<#moduleCode#contentType#description>_<telegram_datetime>.jpg
#     Example - PyaeHlianMoe_#cz1011#lab#test_1509375707.jpg
# Inputs
#     msg     - message from user as JSON object
#     hashTag - description from user including module_code and date_time
################################
def uploadHandler(msg, hashTag):
    #print(msg)
    file_id = msg['photo'][-1]['file_id']
    userName = msg['chat']['first_name']
    """Convert the integer data type to string"""
    date = str(msg['date'])
    #print(userName, file_id, date)
    
    """
    Use the download_file function from telepot module to download.
    Save all the photo(s) in 'Files' directory located under root directory
    """
    #print(os.getcwd())
    if 'Files' in os.getcwd():
        telegram_config.bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
    elif 'Codes' in os.getcwd():
        """Check Files directory exist"""
        if not (os.path.exists('../Files/')):
            """Create new directory called Files"""
            os.makedir('../Files/')
        os.chdir('../Files/')
        #print(os.getcwd())
        telegram_config.bot.download_file(file_id, '' + userName + "_" + hashTag + "_" + date + ".jpg")
    else:
        if not (os.path.exists('./Files/')):
            os.makedirs('./Files/')
        os.chdir('./Files')
        #print(os.getcwd())
        telegram_config.bot.download_file(file_id, userName + "_" + hashTag + "_" + date + ".jpg")
## End of uploadHandler