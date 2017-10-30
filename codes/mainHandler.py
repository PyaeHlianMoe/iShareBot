import time
import telepot
import telegram_config
from uploadHandler import uploadHandler
from downloadHandler import downloadHandler
from telepot.loop import MessageLoop

################################
# Set 4 global variables (2 booleans, 2 strings).
# Boolean variables will to detect the user option.
#   upload                     - To detect when user select upload
#   download                   - To detect when user select download
#   module_code, module_type   - Declare at global namespace for both functions
################################
upload, download = False, False
module_code, module_type = "",""

################################
# Name
#     mainHandler
# Version
#     1.0
# Created Date
#     10/24/2017
# PURPOSE
#     Read the input data from user and call the corresponding procedure to execute
# INPUTS
#     msg - incoming message from user
# PRE CONDITIONS
#     upload, download, module_code and module_type variables must declare under global namespace
# Exception
#     Send message to user when either upload or download fail
#     Developer will receive notification message with exception message and username
################################
def mainHandler(msg):
    #print(msg)
    """
    Declare upload and download as Global variables
    Use telepot.glance to know
        content_type - type of the message (e.g. text, photo, file, etc)
        chat_type    - type of chat room (e.g. private, public)
        chat_id      - unique ID of the user
    """
    global upload, download
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if (content_type == 'text'):
        if (msg['text'] == 'Upload'):
            """ Set 'upload=True' and send inline keyboard to use to select a module """
            upload = True
            telegram_config.bot.sendMessage(chat_id, "Please select a module", reply_markup=telegram_config.module_code_keyboard_markup)
        elif (msg['text'] == 'Download'):
            download = True
            """ Set 'download=True' and send instructions to user """
            telegram_config.bot.sendMessage(chat_id, telegram_config.download_message)
        elif (download == True):
            try:
                downloadHandler(msg, chat_id)
            except Exception as e:
                """ Send the message to the developer by hardcoding his/ her own chat_id """
                #telegram_config.bot.sendMessage("68380099", "Exception: " + str(e) + "for uploader " + msg['chat']['first_name'])
                telegram_config.bot.sendMessage(chat_id, "***No screenshot found***\n Please try again", reply_markup=telegram_config.welcome_keyboard_markup)
            else:
                """ Repeat the welcome message when download was successful """
                telegram_config.bot.sendMessage(chat_id,telegram_config.welcome_message, reply_markup=telegram_config.welcome_keyboard_markup)
            """ Set back download=False to allow to select other action """
            download = False
        else:
            """
            Send the welcome message when the text isn't download or upload.
            Set back the download, upload to original state to prevent unwanted actions    
            """
            telegram_config.bot.sendMessage(chat_id,telegram_config.welcome_message, reply_markup=telegram_config.welcome_keyboard_markup)
            upload, download = False, False
    elif (content_type == 'photo'):
        if (upload == True and module_code != "" and module_type != ""):
            """ Upload the photo(s) if all the conditions are fulfilled """
            #print(module_code, module_type)
            """ Do try-except-else. Without setting back upload=False will allow multiple photos to upload. """
            try:
                uploadHandler(msg, module_code + module_type + msg['caption'].lower() if 'caption' in msg else module_code + module_type)
            except Exception as e:
                """ Send the message to the developer by hardcoding his/ her own chat_id """
                #telegram_config.bot.sendMessage("68380099", "Exception: " + str(e) + "for uploader " + msg['chat']['first_name'])
                telegram_config.bot.sendMessage(chat_id, "***There is a problem in saving the documents.***\n Please try to upload again!", reply_markup=telegram_config.welcome_keyboard_markup)
            else:
                telegram_config.bot.sendMessage(chat_id, "Photo(s) have been uploaded successfully" + telegram_config.welcome_message, reply_markup=telegram_config.welcome_keyboard_markup)
        else:
            """ Send welcome message if all the conditions aren't fulfilled and set upload=False """
            telegram_config.bot.sendMessage(chat_id,telegram_config.welcome_message, reply_markup=telegram_config.welcome_keyboard_markup)
            upload = False
        """ Set download=False to allow one action at a time """
        download = False
    else:
        telegram_config.bot.sendMessage(chat_id, "You have uploaded a wrong format. Please upload a screenshot.\n Maximum size: 20MB", reply_markup=telegram_config.welcome_keyboard_markup)
## End of mainHandler

################################
# Name
#     module_and_content_callback
# Version
#     1.0
# Created Date
#     10/24/2017
# PURPOSE
#     Get the value from InlineKeyboard and assign them to module_code and module_type variables
# INPUTS
#     msg - incoming message from user via InlineKeyboard
# PRE CONDITIONS
#     upload, download, module_code and module_type variables must declare under global namespace
################################
def module_and_content_callback(msg):
    global module_code, module_type
    
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    #print('Callback Query:', query_id, from_id, query_data)
    
    #print(j[2] for i in telegram_config.module_code_keyboard_structure for j in i])
    """ Check if query_data contains a data from InlineKeyboard """
    if (query_data in [j[2] for i in telegram_config.module_code_keyboard_structure for j in i]):
        """ Assign the data to module_code variables when user select module_code from InlineKeyboard """
        module_code = query_data
        #print(module_code)
        telegram_config.bot.sendMessage(from_id, 'Please select a content type', reply_markup=telegram_config.content_type_keyboard_markup)
    elif (query_data in [j[2] for i in telegram_config.content_type_keyboard_structure for j in i]):
        """ Assign the data to module_type variables when user select content_type from InlineKeyboard """
        module_type = query_data
        #print(module_type)
        """ Send confirmation message to user before uploading photo(s) to filesystem """
        telegram_config.bot.sendMessage(from_id, "You have chosen \nmodule code: " + module_code + "\ncontent type: " + module_type,reply_markup=telegram_config.confirmation_keyboard_markup)
    elif (query_data == 'Yes' and module_code != "" and module_type != ""):
        """ Request user to upload photo(s) after confirmation """
        telegram_config.bot.sendMessage(from_id, "Please attach photo(s)")
    else:
        """ Send welcome message and assign null values to module_code & module_type variables """
        telegram_config.bot.sendMessage(from_id, telegram_config.welcome_message, reply_markup=telegram_config.welcome_keyboard_markup)
        module_type, module_code = "", ""
## End of module_and_content_callback

""" Use MessageLoop function from telepot to keep monitoring the incoming messages """
MessageLoop(telegram_config.bot, {'chat': mainHandler,
                  'callback_query': module_and_content_callback}).run_as_thread()

""" Keep the program running """
while 1:
    time.sleep(10)