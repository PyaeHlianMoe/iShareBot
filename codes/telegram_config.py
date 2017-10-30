import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

################################
# Different messages to display user
################################
welcome_message = """
You can either upload or download your study material.
Click on the “Upload” button to upload photo.
Click on the “Download” button to download photo.
"""
upload_message = """
Please enter module code, type of material (of the photo in this format (#CZ1005#tut)

material type – tut (tutorial), lab (laboratory), lec (lecture), exam (past year paper answer)
"""
download_message = """
Please search image by hashtag (#) of module code

valid hashtag:

Module code (e.g. #CZ1005)
Material type (e.g. #tut)

Material type availables for #tut, #lab, #lec, #exam
"""
error_message = "You have entered an invalid option."
## End of custom message


################################
# Use ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton from telepot to display keyboard to user
# Use the ReplyKeyboard for 'Upload/ Download' and InlineKeyboard for 'Module code, Content type and Upload confirmation'
################################
weclome_keyboardLayout = [
    [KeyboardButton(text='Upload'), KeyboardButton(text='Download')]
]
module_code_keyboard_structure = [
    [InlineKeyboardButton(text='CZ1011', callback_data='#cz1011'),InlineKeyboardButton(text='CZ1007', callback_data='#cz1007')],
                   [InlineKeyboardButton(text='CZ1003', callback_data='#cz1003'),InlineKeyboardButton(text='CZ1012', callback_data='#cz1012')],
                   [InlineKeyboardButton(text='CZ1005', callback_data='#cz1005'),InlineKeyboardButton(text='CZ2001', callback_data='#cz2001')],
                   [InlineKeyboardButton(text='CZ1006', callback_data='#cz1006'),InlineKeyboardButton(text='CZ2002', callback_data='#cz2002')],
]
content_type_keyboard_structure = [
    [InlineKeyboardButton(text='Lab', callback_data='#lab'),InlineKeyboardButton(text='Tutorial', callback_data='#tut')],
    [InlineKeyboardButton(text='Lectures', callback_data='#lec'),InlineKeyboardButton(text='ExamPapers', callback_data='#exam')]
]
confirmation_keyboard_structure = [
    [InlineKeyboardButton(text='Yes', callback_data='Yes'), InlineKeyboardButton(text='No', callback_data='No')]
]

""" Set 'one_time_keyboard=True' to hide the 'Upload/ Download' keyboard as soon as it has been used in ReplyKeyboard function """
welcome_keyboard_markup = ReplyKeyboardMarkup(keyboard=weclome_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)
""" Use InlineKeyboard function that is integrated in the message """
module_code_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=module_code_keyboard_structure)
content_type_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=content_type_keyboard_structure)
confirmation_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=confirmation_keyboard_structure)
## End of custom keyboard

""" Set Telegram bot Token key """
bot = telepot.Bot('473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ')