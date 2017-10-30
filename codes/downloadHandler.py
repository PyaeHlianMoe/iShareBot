import os
import requests
import glob, os
import re

################################
# Name
#     downloadHandler
# Version
#     1.0
# Created Date
#     10/24/2017
# Purpose
#     Get the requested photo(s) from server and then send it to the specific user based on chat_id
# Inputs
#     msg     - represent the information from user regarding the 'description' of the photo(s)
#     chat_id - unique ID of the requestor so that API can send photo to the requestor
################################
def downloadHandler(msg, chat_id):
    """Convert the text message to small letter"""
    data = msg['text'].lower()
    #print(data)
    
    """
    Change directory to 'Files' and called the 'get_files' procedure.
    'get_files' procedure will send the photo(s) to the requestor using POST method
    """
    if 'Files' in os.getcwd():
        getFile(data, chat_id)
    elif 'Files' in os.listdir():
        os.chdir('./Files/')
        getFile(data, chat_id)
    else:
        os.chdir('../Files/')
        getFile(data, chat_id)
## End of downloadHandler


################################
# Name
#     getFile
# Version
#     1.0
# Created Date
#     10/24/2017
# Purpose
#     Send the photo to the requestor with caption through Telegram API using POST method
# Inputs
#     chat_id - unique ID of the requestor so that API can send photo to the requestor
#     data    - input text value from requestor
################################
def getFile(data, chat_id):
    API_url = 'https://api.telegram.org/bot473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ/sendPhoto?chat_id=' + str(chat_id)
    """ Use glob (filename pattern matching) to find files with Wildcard (*) """
    for file in glob.glob("*" + data + "*.*"):
        #print(file)
        files = {'photo': open(file, 'rb')}
        """ Filter username and datetime from filename by using Regular Expression """
        #print([caption for caption in re.compile('(#[A-Za-z]{2}\d{4})(#lab|#lec|#tut)|(#.*)_').findall(file)])
        captions = {'caption': ''.join(caption) for caption in re.compile('(#[A-Za-z]{2}\d{4})(#lab|#lec|#tut)|(#.*)_').findall(file)}
        """ Use POST request method to send the data to the requestor """
        requests.post(API_url, files=files, data=captions)
## End of getFile procedure