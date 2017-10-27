import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

# Custom message to display the user
welcome_message = """
Hey there!! Greetings from the Notes Sharing bot!
We provide you notes shared by your fellow classmates.
Hit the 'Upload or Download'!!!
"""
upload_message = """
Great! Now let's see what you want to upload here.
Before you upload a screenshot, please write the following information (#ModuleCode#lec/Tu/Lab#Description)
>> #cz1001#lec#your_description.
**** Don't forget that you can upload only lec, tut or lab ****
"""
download_message = """
Type any kind of data you want and our Bot will help you find in the server.
You can find by using hahtags too.
>> #cz1001#lab. Don't worry, we will show the description of the image.
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
    [InlineKeyboardButton(text='CZ1011', callback_data='#CZ1011'),InlineKeyboardButton(text='CZ1007', callback_data='#CZ1007')],
                   [InlineKeyboardButton(text='CZ1003', callback_data='#CZ1003'),InlineKeyboardButton(text='CZ1012', callback_data='#CZ1012')],
                   [InlineKeyboardButton(text='CZ1005', callback_data='#CZ1005'),InlineKeyboardButton(text='CZ2001', callback_data='#CZ2001')],
                   [InlineKeyboardButton(text='CZ1006', callback_data='#CZ1006'),InlineKeyboardButton(text='CZ2002', callback_data='#CZ2002')],
]
content_type_keyboard_structure = [
    [InlineKeyboardButton(text='Lab', callback_data='#lab'),InlineKeyboardButton(text='Tutorial', callback_data='#tut')],
    [InlineKeyboardButton(text='Lectures', callback_data='#lec'),InlineKeyboardButton(text='ExamPapers', callback_data='#exmPa')]
]

welcome_keyboard_markup = ReplyKeyboardMarkup(keyboard=weclome_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)
download_option_keyboard_markup = ReplyKeyboardMarkup(keyboard=download_option_keyboardLayout,resize_keyboard=True,one_time_keyboard=True)
module_code_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=module_code_keyboard_structure)
content_type_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=content_type_keyboard_structure)

bot = telepot.Bot('473082600:AAHyecek_jYWVsVhpyWY7EIs06VtA3dP2tQ')