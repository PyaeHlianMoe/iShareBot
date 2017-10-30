import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

# Custom message to display the user
welcome_message = """
You can either upload or download your study material.
Click on the “Upload” button to upload picture.
Click on the “Download” button to download picture.
"""
upload_message = """
Please enter module code, type of material (of the photo in this format (#CZ1005#tut)

material type – tut (tutorial), lab (laboratory), lec (lecture), exam (past year paper answer)
"""
download_message = """
Please search image by hashtag (#) of module code

valid hashtag:

Module code (e.g. #CZ1005)
material type (e.g. #tut)
"""
error_message = "You have entered an invalid option."

# Custom keyboard to display the user
weclome_keyboardLayout = [
    [KeyboardButton(text='Upload'), KeyboardButton(text='Download')]
]
download_option_keyboardLayout = [
    [KeyboardButton(text='Module Code/ Type'), KeyboardButton(text='HashTag')]
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

welcome_keyboard_markup = ReplyKeyboardMarkup(keyboard=weclome_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)
download_option_keyboard_markup = ReplyKeyboardMarkup(keyboard=download_option_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)
module_code_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=module_code_keyboard_structure)
content_type_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=content_type_keyboard_structure)
confirmation_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=confirmation_keyboard_structure)

bot = telepot.Bot('473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ')