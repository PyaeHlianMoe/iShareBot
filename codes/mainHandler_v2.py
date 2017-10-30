import time
import telepot
import telegram_config
from uploadHandler import uploadHandler
from downloadHandler import downloadHandler
from telepot.loop import MessageLoop

upload, download = False, False
module_code, module_type = "",""

def mainHandler(msg):
    global upload, download
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if (content_type == 'text'):
        if (msg['text'] == 'Upload'):
            upload = True
            telegram_config.bot.sendMessage(chat_id, "Please select a module", reply_markup=telegram_config.module_code_keyboard_markup)
        elif (msg['text'] == 'Download'):
            download = True
            telegram_config.bot.sendMessage(chat_id, telegram_config.download_message)
        elif (download == True):
            try:
                downloadHandler(msg, chat_id)
            except Exception as e:
                telegram_config.bot.sendMessage("68380099", str(e) + "for ")
                telegram_config.bot.sendMessage(chat_id, "***No screenshot found***\n Please try again", reply_markup=telegram_config.welcome_keyboard_markup)
            else:
                telegram_config.bot.sendMessage(chat_id,telegram_config.welcome_message, reply_markup=telegram_config.welcome_keyboard_markup)
            download = False
        #elif (msg['text'] == 'Download'):
            #download = True
            #telegram_config.bot.sendMessage(chat_id, "Please select a download option", reply_markup=telegram_config.download_option_keyboard_markup)
        #elif (download == True):
            #if (msg['text'] == 'Module Code/ Type'):
                #print("Do something")
            #else:
                #telegram_config.bot.sendMessage(chat_id, telegram_config.download_message)
        else:
            telegram_config.bot.sendMessage(chat_id,telegram_config.welcome_message, reply_markup=telegram_config.welcome_keyboard_markup)
            upload, download = False, False
    elif (content_type == 'photo'):
        if (upload == True):
            #print(module_code, module_type)
            uploadHandler(msg, module_code + module_type + msg['caption'].lower() if 'caption' in msg else module_code + module_type, chat_id)
        telegram_config.bot.sendMessage(chat_id,telegram_config.welcome_message, reply_markup=telegram_config.welcome_keyboard_markup)
        upload, download = False, False
    else:
        telegram_config.bot.sendMessage(chat_id, telegram_config.error_message, reply_markup=telegram_config.welcome_keyboard_markup)
    
def module_and_content_callback(msg):
    global module_code, module_type
    
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    #print('Callback Query:', query_id, from_id, query_data)
    
    if (query_data in [j[2] for i in telegram_config.module_code_keyboard_structure for j in i]):
        module_code = query_data
        telegram_config.bot.sendMessage(from_id, 'Please select a content', reply_markup=telegram_config.content_type_keyboard_markup)
    else:
        if (upload == True):
            module_type = query_data
            telegram_config.bot.sendMessage(from_id, 'Please upload a screenshot')
        
MessageLoop(telegram_config.bot, {'chat': mainHandler,
                  'callback_query': module_and_content_callback}).run_as_thread()

while 1:
    time.sleep(10)
