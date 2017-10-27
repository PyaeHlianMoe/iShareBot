import os

################################
# Name
#     DownloadHandler
# Version
#     1.0
# Created Date
#     10/24/2017
# Purpose
#     Get the requested photo(s) from server and then send it to the specific user based on chat_id
# Inputs
#     msg - represent the information from user regarding the 'description' of the photo(s)
#     chat_id - unique_ID of the requested user so that API can send photo to the requestor
# Exception
#     
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