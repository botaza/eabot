import asyncio
import logging
import datetime
import requests
import sqlite3
import urllib.request
import json
import re
import os
import random

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher


from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.contrib.fsm_storage.redis import RedisStorage2

from datetime import datetime

from config import TOKEN
import keyboards as kb
##import pandas as pd



##logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
##level=logging.INFO)

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

f = open('prud.txt', 'r', encoding='UTF-8')
prud = f.read().split('\n')
f.close()


storage = MemoryStorage()
bot = Bot(token=TOKEN)

##admins_id = [1049416300]

dp = Dispatcher(bot, storage=storage)

class FSMAdmin(StatesGroup):
    main = State()
    record0 = State()
    record1 = State()
    record2 = State()
    record3 = State()
    record61 = State()
    record62 = State()
    record63 = State()
    record64 = State()
    record65 = State()
    record66 = State()

######### общее #########

##now = datetime.now()
##current_time = now.strftime("%d/%m/%y %H:%M")

#########

##blacklist = [10494163009, 1049416300]

blacklist = [10494163009, 5947512949]

##updater = [1049416300, 308971677]
updater = 1049416300

@dp.message_handler(commands=['start'], state="*")
async def process_start_command2(message: types.Message):
##await bot.send_photo(message.from_user.id, photo = GREETER)
 logging.info('Начало лога:')
 logging.info('Подключается к боту (id -- username -- firstname  -- lastname):')
 #logging.info(message.chat.phone_number)
 logging.info(message.chat.id)
 logging.info(message.chat.username)
 logging.info(message.chat.first_name)
 logging.info(message.chat.last_name)
 now0 = datetime.now()
 current_time0 = now0.strftime("%d/%m/%y %H:%M")
 connect = sqlite3.connect('usersf.db')
 cursor = connect.cursor()
 cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
    id INTEGER,
    username INTEGER,
    firstname INTEGER,
    lastname INTEGER,
    current_time0 INTEGER
 )""")

 connect.commit()
 people_id = message.chat.id
 cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
 checkdata = cursor.fetchone()
 if checkdata is None:
  user_id = [message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name, current_time0]
  cursor.execute("INSERT INTO login_id VALUES(?,?,?,?,?);", user_id)
  connect.commit()
 else:
  pass
 
 if message.from_user.id in blacklist:
   await message.reply("ты не можешь использовать бот...(")
 else:
  await bot.send_message(message.chat.id, f'Hello {message.chat.first_name} !')
  await bot.send_message(message.chat.id, 'This bot is for Эльмира.. чтобы надежнее, технологичнее, молодежнее... ')
  await bot.send_message(message.chat.id, 'Загружаю обложку... ')
  with urllib.request.urlopen("https://cloud-api.yandex.net/v1/disk/public/resources?public_key=https://disk.yandex.ru/i/KfxWLzfBi3ZQxg") as url:
        data0 = json.loads(url.read().decode())
        jsonData = data0["file"]
        url = jsonData
        fileName1 = 'Note.jpg'
        req = requests.get(url)
        file = open(fileName1, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()
  await bot.send_photo(message.from_user.id, photo=open(fileName1, 'rb')) 
  await FSMAdmin.record0.set()
  await bot.send_message(message.chat.id, 'Что я умею?', reply_markup=kb.inline_kb_full_0)

@dp.callback_query_handler(lambda c: c.data == 'btn060', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Продолжаем знакомиться!', reply_markup=kb.inline_kb_full_0)


   
   
@dp.callback_query_handler(lambda c: c.data == 'btn05', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    userid = callback_query.from_user.id
    filename00l = 'Связь с сотрудником'    
    filenamel = "last%s.txt" % userid 
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filenamel, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"{filename00l}, Начато: {current_time}\n")
    f.close()        
    await callback_query.message.delete()
   ## await bot.send_photo(callback_query.from_user.id, photo = CONTACT)
   ## await bot.send_message(callback_query.from_user.id, 'при возникновении технических проблем пиши +79241311138')
    await bot.send_message(callback_query.from_user.id, 'Коучинг, айти решения, шутки из Плюшек, встречи в Океане  [+79241311138](tg://user?id=1049416300)', reply_markup=kb.inline_kb_full_0, parse_mode=ParseMode.MARKDOWN)

    
@dp.callback_query_handler(lambda c: c.data == 'btn06', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выбери вопрос!', reply_markup=kb.inline_kb_full_06)

@dp.callback_query_handler(lambda c: c.data == 'btn061', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await FSMAdmin.record61.set()
    await bot.send_message(callback_query.from_user.id, 'Любимая строчка из Круга или Меладзе')

@dp.callback_query_handler(lambda c: c.data == 'btn062', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await FSMAdmin.record62.set()
    await bot.send_message(callback_query.from_user.id, 'Идеальный ужин? Идеальный перекус в кафе?')

@dp.callback_query_handler(lambda c: c.data == 'btn063', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await FSMAdmin.record63.set()
    await bot.send_message(callback_query.from_user.id, 'Любимые места в ВЛД и Приморье?')

@dp.callback_query_handler(lambda c: c.data == 'btn064', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await FSMAdmin.record64.set()
    await bot.send_message(callback_query.from_user.id, 'Любимые цветы?')


@dp.callback_query_handler(lambda c: c.data == 'btn065', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await FSMAdmin.record65.set()
    await bot.send_message(callback_query.from_user.id, 'Рандомные 5 вещей которые нравятся?')
    

@dp.callback_query_handler(lambda c: c.data == 'btn066', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await FSMAdmin.record66.set()
    await bot.send_message(callback_query.from_user.id, '5 ред-флагов?')
    


@dp.message_handler(content_types=ContentType.STICKER, state="*")
async def unknown_message(msg: types.Message):
     if message.from_user.id in blacklist:
        await message.reply("ты не можешь использовать бот...(")
     else:
        message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        italic('\nЯ просто напомню,'), 'что есть',
                        code('команда'), '/start')
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=ContentType.DOCUMENT, state="*")
async def unknown_message(msg: types.Message):
     if message.from_user.id in blacklist:
        await message.reply("ты не можешь использовать бот...(")
     else:
        message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        italic('\nЯ просто напомню,'), 'что есть',
                        code('команда'), '/start')
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=ContentType.VIDEO, state="*")
async def unknown_message(msg: types.Message):
     if message.from_user.id in blacklist:
        await message.reply("ты не можешь использовать бот...(")
     else:
        message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        italic('\nЯ просто напомню,'), 'что есть',
                        code('команда'), '/start')
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)







@dp.message_handler(state=FSMAdmin.record61)
async def any_text_message(message: types.Message):
    # Дополняем исходный текст:
    userid = message.from_user.id
    ##print (userid)
    fn0 = userid
    filename = "%s.txt" % userid
    f = open(filename, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"#фидбэк {message.text}, записано: {current_time}\n")
    f.close()
   ## await message.delete()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#61 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)
    await FSMAdmin.main.set()



@dp.message_handler(state=FSMAdmin.record62)
async def any_text_message(message: types.Message):
    # Дополняем исходный текст:
    userid = message.from_user.id
    ##print (userid)
    fn0 = userid
    filename = "%s.txt" % userid
    f = open(filename, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"#фидбэк {message.text}, записано: {current_time}\n")
    f.close()
   ## await message.delete()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#62 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем!', reply_markup=kb.inline_kb_full_06)
    await FSMAdmin.main.set()


@dp.message_handler(state=FSMAdmin.record63)
async def any_text_message(message: types.Message):
    # Дополняем исходный текст:
    userid = message.from_user.id
    ##print (userid)
    fn0 = userid
    filename = "%s.txt" % userid
    f = open(filename, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"#фидбэк {message.text}, записано: {current_time}\n")
    f.close()
   ## await message.delete()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#63 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем!', reply_markup=kb.inline_kb_full_06)
    await FSMAdmin.main.set()




@dp.message_handler(state=FSMAdmin.record64)
async def any_text_message(message: types.Message):
    # Дополняем исходный текст:
    userid = message.from_user.id
    ##print (userid)
    fn0 = userid
    filename = "%s.txt" % userid
    f = open(filename, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"#фидбэк {message.text}, записано: {current_time}\n")
    f.close()
   ## await message.delete()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#64 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)
    await FSMAdmin.main.set()



@dp.message_handler(state=FSMAdmin.record65)
async def any_text_message(message: types.Message):
    # Дополняем исходный текст:
    userid = message.from_user.id
    ##print (userid)
    fn0 = userid
    filename = "%s.txt" % userid
    f = open(filename, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"#фидбэк {message.text}, записано: {current_time}\n")
    f.close()
   ## await message.delete()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#65 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)
    await FSMAdmin.main.set()




@dp.message_handler(state=FSMAdmin.record66)
async def any_text_message(message: types.Message):
    # Дополняем исходный текст:
    userid = message.from_user.id
    ##print (userid)
    fn0 = userid
    filename = "%s.txt" % userid
    f = open(filename, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"#фидбэк {message.text}, записано: {current_time}\n")
    f.close()
   ## await message.delete()
 ##   await state.finish()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#66 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)
    await FSMAdmin.main.set()





@dp.message_handler(content_types=["photo"], state="*")
async def download_photo(message: types.Message):
     if message.from_user.id in blacklist:
        await message.reply("ты не можешь использовать бот...(")
     else:
        userid = message.chat.id
        fn0p = userid
##    await message.photo[-1].download(destination_dir=f"{userid}")
        id_photo = message.photo[-1].file_id
        await bot.send_message(1049416300, f'#скриншот {fn0p}')
        await bot.send_photo(1049416300, id_photo)
 ###   await bot.send_message(746493569, f'#скриншот {fn0p}')
 ###   await bot.send_photo(746493569, id_photo)
##    await bot.send_photo(888808670, id_photo)
        await bot.send_message(message.chat.id, 'Фото отправлено!', reply_markup=kb.inline_kb_full_0)

##@dp.message_handler(lambda message: message.text == "синхрофазотрон")
##async def any_text_message(message: types.Message):

##    userid = message.from_user.id
##    fn0 = userid    

##    filename = "%s.txt" % userid
##    f = open(filename, 'a+')  # open file in append mode

##    now = datetime.now()
##    current_time = now.strftime("%d/%m/%y %H:%M")
##    f.write(f"#профориент {message.text}, записано: {current_time}\n")

##    await bot.send_message(1049416300, fn0)
##    await bot.send_message(1049416300, f'#профориент {message.text}')
##    await bot.send_message(message.chat.id, f'Верный ответ!', reply_markup=kb.inline_kb_full_06b)


##@dp.message_handler(lambda message: '~' in message.text)
##async def any_text_message(message: types.Message):

##    userid = message.from_user.id
##    fn0 = userid    

##    filename = "%s.txt" % userid
##    f = open(filename, 'a+')  # open file in append mode

##    now = datetime.now()
##    current_time = now.strftime("%d/%m/%y %H:%M")
##    f.write(f"#профориент {message.text}, записано: {current_time}\n")
##    f.close()

##    await bot.send_message(1049416300, fn0)
##    await bot.send_message(1049416300, f'#профориент {message.text}')
##    await bot.send_message(message.chat.id, f'Отлично! Запись сделана!', reply_markup=kb.inline_kb_full_0b)









@dp.message_handler(lambda message: message.text == "^")
async def any_text_message(message: types.Message):
##    await bot.send_message(5710506417, f'Ссылка на фото')
    await bot.send_message(1049416300, f'Ссылка на фото')  
    await bot.send_message(5710506417, f'Ссылка на фото') 
    await bot.send_message(1049416300, f'https://drive.google.com/file/d/1CyvPxiJSiY_2ZgesbZjsj4ITHUAriLbl/view?usp=share_link')   
    await bot.send_message(5710506417, f'https://drive.google.com/file/d/1CyvPxiJSiY_2ZgesbZjsj4ITHUAriLbl/view?usp=share_link') 
    await bot.send_message(1049416300, f'Ссылка на видео') 
    await bot.send_message(5710506417, f'Ссылка на видео')
    await bot.send_message(1049416300, f'https://drive.google.com/file/d/1h0k8Mff8RMsIms_m23VI3IxpN-ltJ0zK/view?usp=share_link')
    await bot.send_message(5710506417, f'https://drive.google.com/file/d/1h0k8Mff8RMsIms_m23VI3IxpN-ltJ0zK/view?usp=share_link')
    await bot.send_message(1049416300, f'Ссылка на AR-страницу') 
    await bot.send_message(5710506417, f'Ссылка на AR-страницу') 
    await bot.send_message(1049416300, f'https://testingdomain.kz/miost/230303/') 
    await bot.send_message(5710506417, f'https://testingdomain.kz/miost/230303/') 
    await bot.send_message(1049416300, f'Напишите в бот, как скачаете. И я удалю фото и видео из облака') 
    await bot.send_message(5710506417, f'Напишите в бот, как скачаете. И я удалю фото и видео из облака') 
 


##@dp.message_handler(lambda message: message.text == "*")
##async def any_text_message(message: types.Message):

##    userid = message.from_user.id

##    filename = "%s.txt" % userid
##    f = open(filename, 'r')
##    file_contents = f.read()

##    await bot.send_message(message.chat.id, f'{file_contents}')

##    await bot.send_message(message.chat.id, f'Отлично! Журнал показн', reply_markup=kb.inline_kb_full_0b)


    
    
@dp.message_handler(state=FSMAdmin.record1)
async def any_text_message(message: types.Message):
     if message.from_user.id in blacklist:
        await message.reply("ты не можешь использовать бот...(")
     else:
    # Дополняем исходный текст:
   ## await message.delete()
   ## await state.finish()
        userid = message.from_user.id
        fn0 = userid
        await FSMAdmin.record2.set() 
        await bot.send_message(1049416300, fn0)
        await bot.send_message(1049416300, f'#record1 {message.text}')
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#record1 {message.text}')
##    await bot.send_message(888808670, message.text)
    ##await bot.send_message(message.chat.id, f'Имя записано! Нажимай кнопку ОК и продолжим!', reply_markup=kb.inline_kb_full_082)
        await bot.send_message(message.chat.id, f'Имя записано!')
        await bot.send_message(message.chat.id, "Напиши в текстовое поле свой номер телефона")
 ##   await bot.send_message(callback_query.from_user.id, "😉")
        await bot.send_message(message.chat.id, "⬇️")
    
@dp.message_handler(state=FSMAdmin.record2)
async def any_text_message(message: types.Message):
     if message.from_user.id in blacklist:
        await message.reply("ты не можешь использовать бот...(")
     else:
    # Дополняем исходный текст:
   ## await message.delete()
   ## await state.finish()
        userid = message.from_user.id
        fn0 = userid
        await FSMAdmin.record3.set() 
        await bot.send_message(1049416300, fn0)
        await bot.send_message(1049416300, f'#record2 {message.text}')
##    await bot.send_message(888808670, message.text)
##    await bot.send_message(message.chat.id, f'Телефон записан! Нажимай кнопку ОК и продолжим!', reply_markup=kb.inline_kb_full_083)
        await bot.send_message(message.chat.id, f'Телефон записан!')
        await bot.send_message(message.chat.id, "Произвольно напиши в текстовое поле имена тех, кто будут с тобой в команде. Не более четырех человек!")
 ##   await bot.send_message(callback_query.from_user.id, "😉")
        await bot.send_message(message.chat.id, "⬇️")


    
@dp.message_handler(state=FSMAdmin.record3)
async def any_text_message(message: types.Message):
    # Дополняем исходный текст:
   ## await message.delete()
   ## await state.finish()
    userid = message.from_user.id
    fn0 = userid
    await FSMAdmin.main.set() 
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#record3 {message.text}')
##    await bot.send_message(888808670, message.text)
    await bot.send_message(message.chat.id, f'Записал! Мы обязательно с тобой свяжемся!', reply_markup=kb.inline_kb_full_0)

@dp.message_handler(content_types=ContentType.CONTACT, is_sender_contact=True)
async def contact_handler(message):

     if message.from_user.id in blacklist:
        await message.reply("ты не можешь использовать бот...(")
     else:
##async def process_callback_button1(callback_query: types.CallbackQuery):
##   await bot.answer_callback_query(callback_query.id)

        userid = message.from_user.id
    ##print (userid)
        filename = "phone%s.txt" % userid
        f = open(filename, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
        now = datetime.now()
        current_time = now.strftime("%d/%m/%y %H:%M")
        f.write(f"{message.contact.phone_number}, записано: {current_time}\n")
        f.close()
   ## await FSMAdmin.star.set()
   ## await message.delete()
   ## await state.finish()    
 ##  print(message.contact.phone_number) 
 ##   await FSMAdmin.passw.set()  

        filename = "last%s.txt" % userid
        f = open(filename, 'r')
        last_line = f.readlines()[-1]
        ##file_contents = f.read()
       
    ##with open(filename, encoding='utf-8') as f:
    ##    contents = f.read()
    ##await bot.send_message(message.chat.id, f'{file_contents}')
        if os.stat(filename).st_size == 0:

    ##    await bot.send_message(message.chat.id, f'День, из которого ты вышел: {last_line}')
            await bot.send_message(message.chat.id, f'Журнал пустой')
    ##else:
    ##await FSMAdmin.tilda.set()
    ##await bot.send_message(message.chat.id, f'Если сверху появился журнал, какую строчку удалить?')
    ##     await bot.send_message(message.chat.id, f'Журнал пустой')

        await bot.send_message(1049416300, f'#запись {last_line} {userid}') 
        await bot.send_message(message.chat.id, "Твой номер успешно получен", reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(message.chat.id, "Мы свяжемся в ближайшее время", reply_markup=kb.inline_kb_full_0b) 

@dp.message_handler(content_types=ContentType.CONTACT, is_sender_contact=False)
async def contact_handler(message):
    await bot.send_message(message.chat.id, "Это не твой номер")

@dp.message_handler(state="*")
async def any_text_message(message: types.Message):
     if message.from_user.id in blacklist:
        await message.reply("ты не можешь использовать бот...(")
     else:
    # Дополняем исходный текст:
        userid = message.from_user.id
    ##print (userid)
        fn0 = userid
        filename = "%s.txt" % userid
        f = open(filename, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
        now = datetime.now()
        current_time = now.strftime("%d/%m/%y %H:%M")
        f.write(f"#фидбэк {message.text}, записано: {current_time}\n")
        f.close()
   ## await message.delete()
   ## await state.finish()
        await bot.send_message(1049416300, fn0)
        await bot.send_message(1049416300, f'#фидбэк {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
        await bot.send_message(message.chat.id, f'Отлично! Сообщение записано!', reply_markup=kb.inline_kb_full_0b)

    

if __name__ == '__main__':
    executor.start_polling(dp)
