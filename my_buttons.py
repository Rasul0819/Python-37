from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


admins_menu = ReplyKeyboardMarkup(resize_keyboard=True)

admins_menu.add(KeyboardButton('Zat qosiw'),
                KeyboardButton(text='Zakazlar'),
                KeyboardButton(text='Xabar jiberiw'),
                )

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton(text='Menu'),
         KeyboardButton(text='Contacts'),
         KeyboardButton(text='Location'))

zat_qosiw_menu = ReplyKeyboardMarkup(resize_keyboard=True)
zat_qosiw_menu.add(KeyboardButton('Fast food'),
                   KeyboardButton('Hot food'),
                   KeyboardButton('Drinks'))
