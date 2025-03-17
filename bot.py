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
    quiz1 = State()
    reply1 = State()
    reply2 = State()

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
    
@dp.callback_query_handler(lambda c: c.data == 'btn07', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    userid = callback_query.from_user.id
    filename00l = 'Уссурийск'    
    filenamel = "last%s.txt" % userid 
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filenamel, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"{filename00l}, Начато: {current_time}\n")
    f.close()        
    await bot.send_message(callback_query.from_user.id, 'По ссылке можешь открыть панорамный снимок, сделанный в Уссурийске\nhttps://testingdomain.kz/miost/20230131/ ', reply_markup=kb.inline_kb_full_0b)
    
@dp.callback_query_handler(lambda c: c.data == 'btn08', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
##    await FSMAdmin.record1.set() 
    await bot.answer_callback_query(callback_query.id)
    userid = callback_query.from_user.id
    filename00l = 'Супье0'    
    filenamel = "last%s.txt" % userid 
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filenamel, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"{filename00l}, Начато: {current_time}\n")
    f.close()       
    await bot.send_message(callback_query.from_user.id, "⏳Информация подгружается...⏳")
    ##keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    with urllib.request.urlopen("https://cloud-api.yandex.net/v1/disk/public/resources?public_key=https://disk.yandex.ru/i/KAPAvHqeIN2ETQ") as url:
        data1 = json.loads(url.read().decode())
        jsonData = data1["file"]
        url = jsonData
        fileName2 = 'supe.png'
        req = requests.get(url)
        file = open(fileName2, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()  
    await bot.send_photo(callback_query.from_user.id, photo=open(fileName2, 'rb'))         
    await bot.send_message(callback_query.from_user.id, "Здесь ты можешь записаться на Мастер-класс Февральский супье 11.02", reply_markup=kb.inline_kb_full_08)
    
    
@dp.callback_query_handler(lambda c: c.data == 'btn081', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
##    await FSMAdmin.record2.set() 
    await FSMAdmin.record1.set() 
    await bot.answer_callback_query(callback_query.id)
    userid = callback_query.from_user.id
    filename00l = 'Супье1'    
    filenamel = "last%s.txt" % userid 
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filenamel, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"{filename00l}, Начато: {current_time}\n")
    f.close()         
    await bot.send_message(callback_query.from_user.id, "Напиши в текстовое поле свое имя")
    await bot.send_message(callback_query.from_user.id, "😉")
    await bot.send_message(callback_query.from_user.id, "⬇️")
    
@dp.callback_query_handler(lambda c: c.data == 'btn0821', state=FSMAdmin.record2)
async def process_callback_button1(callback_query: types.CallbackQuery):
 ##   await FSMAdmin.record3.set() 
    await bot.answer_callback_query(callback_query.id)
    userid = callback_query.from_user.id
    filename00l = 'Супье2'    
    filenamel = "last%s.txt" % userid 
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filenamel, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"{filename00l}, Начато: {current_time}\n")
    f.close()         
    await bot.send_message(callback_query.from_user.id, "Напиши в текстовое поле свой номер телефона")
 ##   await bot.send_message(callback_query.from_user.id, "😉")
    await bot.send_message(callback_query.from_user.id, "⬇️")
    
    
@dp.callback_query_handler(lambda c: c.data == 'btn0821', state=FSMAdmin.record3)
async def process_callback_button1(callback_query: types.CallbackQuery):
##    await FSMAdmin.record3.set() 
    await bot.answer_callback_query(callback_query.id)
    userid = callback_query.from_user.id
    filename00l = 'Супье3'    
    filenamel = "last%s.txt" % userid 
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filenamel, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"{filename00l}, Начато: {current_time}\n")
    f.close()         
    await bot.send_message(callback_query.from_user.id, "Произвольно напиши в текстовое поле имена тех, кто будут с тобой в команде. Не более четырех человек!")
 ##   await bot.send_message(callback_query.from_user.id, "😉")
    await bot.send_message(callback_query.from_user.id, "⬇️")

@dp.callback_query_handler(lambda c: c.data == 'btn09', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    userid = callback_query.from_user.id
    filename00l = '2703'    
    filenamel = "last%s.txt" % userid 
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filenamel, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"{filename00l}, Начато: {current_time}\n")
    f.close()        
    await bot.send_message(callback_query.from_user.id, 'Сслыка на презентацию')     
    await bot.send_message(callback_query.from_user.id, 'https://disk.yandex.ru/i/px_mFMX-daHhBA', reply_markup=kb.inline_kb_full_0b)



@dp.callback_query_handler(lambda c: c.data == 'btn09b', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    userid = callback_query.from_user.id
    filename00l = 'Пруд'    
    filenamel = "last%s.txt" % userid 
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filenamel, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%y %H:%M")
    f.write(f"{filename00l}, Начато: {current_time}\n")
    f.close()    
    await bot.send_message(callback_query.from_user.id, random.choice(prud), reply_markup=kb.inline_kb_full_0pb)
    
    
@dp.callback_query_handler(lambda c: c.data == 'btn09d', state="*")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await FSMAdmin.quiz1.set()
    
    filename000l = 'quiz'    
    filename0002 = "numbers.txt"
    ### filename = "%s.txt" % userid 
  ##  f = open(filenamel, 'w')  # open file in append mode
    f = open(filename0002, 'a+')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    f.close()  
    
    await bot.send_message(callback_query.from_user.id, 'Начинаем!')
    await bot.send_message(callback_query.from_user.id, 'Выбери задание')
    await bot.send_message(callback_query.from_user.id, 'Впиши номер -- от 1 до 43')    
    await bot.send_message(callback_query.from_user.id, 'Если какие-то вопросы уже были выбраны, их номера появятся ниже') 

    f = open(filename0002, 'r')
    file_contents = f.read()
    ##with open(filename, encoding='utf-8') as f:
    ##    contents = f.read()
    await bot.send_message(callback_query.from_user.id, f'{file_contents}')  
    await bot.send_message(callback_query.from_user.id, 'Поехали! Вписывай свой номер!')  


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


@dp.message_handler(lambda message: message.text == "privatetext", state="*")
async def any_text_message(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(message.chat.id, f'Введи айди')
    await FSMAdmin.reply1.set()


@dp.message_handler(lambda message: message.text == "restartquiz", state="*")
async def any_text_message(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'w')  # open file in append mode
    f.write('test')
    f.close()



@dp.message_handler(state=FSMAdmin.reply1)
async def any_text_message(message: types.Message):
    # Дополняем исходный текст:
        filename = "reply1.txt"
        f = open(filename, 'w')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
        f.write(f"{message.text}")
        f.close()

        await bot.send_message(message.chat.id, f'Отлично! Теперь текст ответа!')
        await FSMAdmin.reply2.set()
        
        
@dp.message_handler(state=FSMAdmin.reply2)
async def any_text_message(message: types.Message):
        filename = "reply2.txt"
        f = open(filename, 'w')  # open file in append mode
    ##with open(filename, encoding='utf-8', 'w') as f:
    ##f.write('\n' + message.text)
        f.write(f"{message.text}")
        f.close()
        
        filename2 = "reply1.txt"
        f = open(filename2, 'r')
        file_contents2 = f.read()
        ##with open(filename, encoding='utf-8') as f:
        ##    contents = f.read()
        
        filename3 = "reply2.txt"
        f = open(filename3, 'r')
        file_contents3 = f.read()
        ##with open(filename, encoding='utf-8') as f:
        ##    contents = f.read()
        
        await bot.send_message(f'{file_contents2}', f'{file_contents3}')
        await bot.send_message(message.chat.id, f'Отлично! Сообщение отправлено!', reply_markup=kb.inline_kb_full_0)
        await FSMAdmin.record0.set()




@dp.message_handler(lambda message: message.text == "spamtext", state="*")
async def any_text_message(message: types.Message):
    connect = sqlite3.connect('usersf.db')
    cursor = connect.cursor()
    cursor.execute(f'''SELECT id FROM login_id''')
    spam_base = cursor.fetchall()
    for z in range(len(spam_base)):
        await bot.send_message(spam_base[z][0], f'Привет !\n📢Просто хочу напомнить, что завтра мы очень ждем тебя на день открытых дверей Владивостокского государственного университета! \n📍Место - Владивосток, ул. Гоголя, д.41. ⏰время - с 11.00 до 14.00\n🚪Вход со стороны театра «Андеграунд»\n📋В программе дня открытых дверей:\n-	👨👨👧👦Презентация института (директора о специфике обучения, об актуальности специальностей, студенты об учёбе в институте)\n-	🤳 Мастер-классы для абитуриентов \n-	🙂 Общение с приемной комиссией \n-	🤔 Экскурсии по университету и знакомство с нашими студентами\n-	😃 Развлекательная зона \n-	🤝 Знакомство с руководителем института и преподавателями\n-	🏆Розыгрыши призов -  в том числе скидки на обучение!', reply_markup=kb.inline_kb_full_01nb) 


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
   ## await state.finish()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#61 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)

@dp.message_handler(content_types=ContentType.PHOTO, state=FSMAdmin.record61)
async def download_photo(message: types.Message):
    userid = message.chat.id
    fn0p = userid
##    await message.photo[-1].download(destination_dir=f"{userid}")
    id_photo = message.photo[-1].file_id
    await bot.send_message(1049416300, f'#61 {fn0p}')
    await bot.send_photo(1049416300, id_photo)
 ###   await bot.send_message(746493569, f'#скриншот {fn0p}')
 ###   await bot.send_photo(746493569, id_photo)
##    await bot.send_photo(888808670, id_photo)
    await bot.send_message(message.chat.id, 'Фото отправлено!')
    await bot.send_message(message.chat.id, 'Продолжить Комментарий? (например, чтобы добавить текст или еще фото)', reply_markup=kb.inline_kb_full_r4c)


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
   ## await state.finish()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#62 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем!', reply_markup=kb.inline_kb_full_06)

@dp.message_handler(content_types=ContentType.PHOTO, state=FSMAdmin.record62)
async def download_photo(message: types.Message):
    userid = message.chat.id
    fn0p = userid
##    await message.photo[-1].download(destination_dir=f"{userid}")
    id_photo = message.photo[-1].file_id
    await bot.send_message(1049416300, f'#63 {fn0p}')
    await bot.send_photo(1049416300, id_photo)
 ###   await bot.send_message(746493569, f'#скриншот {fn0p}')
 ###   await bot.send_photo(746493569, id_photo)
##    await bot.send_photo(888808670, id_photo)
    await bot.send_message(message.chat.id, 'Фото отправлено!')
    await bot.send_message(message.chat.id, 'Продолжить Комментарий? (например, чтобы добавить текст или еще фото)', reply_markup=kb.inline_kb_full_r4c)

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
   ## await state.finish()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#63 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)

@dp.message_handler(content_types=ContentType.PHOTO, state=FSMAdmin.record63)
async def download_photo(message: types.Message):
    userid = message.chat.id
    fn0p = userid
##    await message.photo[-1].download(destination_dir=f"{userid}")
    id_photo = message.photo[-1].file_id
    await bot.send_message(1049416300, f'#64 {fn0p}')
    await bot.send_photo(1049416300, id_photo)
 ###   await bot.send_message(746493569, f'#скриншот {fn0p}')
 ###   await bot.send_photo(746493569, id_photo)
##    await bot.send_photo(888808670, id_photo)
    await bot.send_message(message.chat.id, 'Фото отправлено!')
    await bot.send_message(message.chat.id, 'Продолжить Комментарий? (например, чтобы добавить текст или еще фото)', reply_markup=kb.inline_kb_full_r4c)



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
   ## await state.finish()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#64 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)

@dp.message_handler(content_types=ContentType.PHOTO, state=FSMAdmin.record64)
async def download_photo(message: types.Message):
    userid = message.chat.id
    fn0p = userid
##    await message.photo[-1].download(destination_dir=f"{userid}")
    id_photo = message.photo[-1].file_id
    await bot.send_message(1049416300, f'#64 {fn0p}')
    await bot.send_photo(1049416300, id_photo)
 ###   await bot.send_message(746493569, f'#скриншот {fn0p}')
 ###   await bot.send_photo(746493569, id_photo)
##    await bot.send_photo(888808670, id_photo)
    await bot.send_message(message.chat.id, 'Фото отправлено!')
    await bot.send_message(message.chat.id, 'Продолжить Комментарий? (например, чтобы добавить текст или еще фото)', reply_markup=kb.inline_kb_full_r4c)







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
   ## await state.finish()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#65 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)

@dp.message_handler(content_types=ContentType.PHOTO, state=FSMAdmin.record65)
async def download_photo(message: types.Message):
    userid = message.chat.id
    fn0p = userid
##    await message.photo[-1].download(destination_dir=f"{userid}")
    id_photo = message.photo[-1].file_id
    await bot.send_message(1049416300, f'#65 {fn0p}')
    await bot.send_photo(1049416300, id_photo)
 ###   await bot.send_message(746493569, f'#скриншот {fn0p}')
 ###   await bot.send_photo(746493569, id_photo)
##    await bot.send_photo(888808670, id_photo)
    await bot.send_message(message.chat.id, 'Фото отправлено!')
    await bot.send_message(message.chat.id, 'Продолжить Комментарий? (например, чтобы добавить текст или еще фото)', reply_markup=kb.inline_kb_full_r4c)




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
   ## await state.finish()
    await bot.send_message(1049416300, fn0)
    await bot.send_message(1049416300, f'#66 {message.text}')
##    await bot.send_message(888808670, message.text)
 ###   await bot.send_message(746493569, fn0)
 ###   await bot.send_message(746493569, f'#фидбэк {message.text}')
    await bot.send_message(message.chat.id, 'Ответ отправлен!')
    await bot.send_message(message.chat.id, 'Продолжаем', reply_markup=kb.inline_kb_full_06)

@dp.message_handler(content_types=ContentType.PHOTO, state=FSMAdmin.record66)
async def download_photo(message: types.Message):
    userid = message.chat.id
    fn0p = userid
##    await message.photo[-1].download(destination_dir=f"{userid}")
    id_photo = message.photo[-1].file_id
    await bot.send_message(1049416300, f'#66 {fn0p}')
    await bot.send_photo(1049416300, id_photo)
 ###   await bot.send_message(746493569, f'#скриншот {fn0p}')
 ###   await bot.send_photo(746493569, id_photo)
##    await bot.send_photo(888808670, id_photo)
    await bot.send_message(message.chat.id, 'Фото отправлено!')
    await bot.send_message(message.chat.id, 'Продолжить Комментарий? (например, чтобы добавить текст или еще фото)', reply_markup=kb.inline_kb_full_r4c)




@dp.message_handler(content_types=ContentType.PHOTO, state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    userid = message.chat.id
    fn0p = userid
##    await message.photo[-1].download(destination_dir=f"{userid}")
    id_photo = message.photo[-1].file_id
    await bot.send_message(1049416300, f'#фидбэк {fn0p}')
    await bot.send_photo(1049416300, id_photo)
 ###   await bot.send_message(746493569, f'#скриншот {fn0p}')
 ###   await bot.send_photo(746493569, id_photo)
##    await bot.send_photo(888808670, id_photo)
    await bot.send_message(message.chat.id, 'Фото отправлено!')
    
    filename = "numbers.txt"    
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, f'{file_contents}')     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "1", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз 1 {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Придумать 5 рифм к слову "пруд"')
 ##   filename = "numbers.txt"    
   
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "2", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, '5 любимых фильмов')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')



@dp.message_handler(lambda message: message.text == "3", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Назвать расписание на следующую неделю')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')



@dp.message_handler(lambda message: message.text == "4", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Вспомнить фамилии всех преподавателей')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')



@dp.message_handler(lambda message: message.text == "5", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Вспомнить название самой первой пары')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "6", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, '5 любимых песен')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "7", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Открыть личный кабинет / показать, что он открыт')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "8", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Каждый урок начинался с вопроса учительницы и этот вопрос знали наизусть даже те, кто ничего другого в английском не знал. Зашифровано оно звучит как «Вопросительное местоимение быть в исполнении какой-либо обязанности в порядке очереди на текущий 24-часовой отрезок времени»? Напишите ответ пятью словами.')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "9", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Не использовать телефон 30 минут!!')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "10", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, '10 раз попрыгать на одной ноге')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "11", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'найти и показать что-то (хорошее!), что напоминает ВВГУ')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "12", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'нарисовать в заметках что-то про ВВГУ')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')

@dp.message_handler(lambda message: message.text == "13", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Назвать три песни Каспийского груза')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "14", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Назвать любую цитату из песен Гио Пика')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "15", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Пройти до конца дня до геометрического тигра и обратно!!!')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "16", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Повторить вслед за онлайн переводчиком на китайском фразу -- "Завтра 16 октября предлагаю тоже поехать на пруды"')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "17", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Спеть / прочитать строчку из песни на английском языке')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')

@dp.message_handler(lambda message: message.text == "18", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Назвать пять поэтов серебряного века')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')

@dp.message_handler(lambda message: message.text == "19", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Сфотаться с кем-нибудь на фоне самой красной машины')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "20", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Задать любому человеку любой вопрос')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "21", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Вспомнить название любых 5 картин')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "22", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Дать определение на английском языке -- что такое "туризм"')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "23", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Дать определение на английском языке -- что такое "педагогика"')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "24", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'назвать одно место во Владивостоке, которое очень хочется посетить')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "25", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'назвать отчество любой одногруппницы или одногруппника')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "26", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Попасть камушком в 5-литровую канистру с 5 метрова')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "27", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Вспомнить 4 имени-отчества преподавателей')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "28", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Назвать три музея г. Владивосток')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "29", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, '3 любимых фильма с Джони Деппом')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "30", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, '3 песни про осень')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "31", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'сбросить в ТГ фотку с любимым мемом')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "32", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'описать любое произведение Гоголя в 3 предложениях')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')

@dp.message_handler(lambda message: message.text == "33", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Перевести на английский слово "мангал"')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "34", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Узнать, сколько стоит горячий чай в любой из точек питания')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "35", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'сделать любое фото и отправить в ТГ')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "36", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Отправить в ТГ одну из последних 10 фото/картинок в телефоне')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "37", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'набрать в одном из мессенджеров "Я" и автоподбором по первому предложению составить фразу из 20 выскакиваемых друг за другом первых слов')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')

@dp.message_handler(lambda message: message.text == "38", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Вспомнить три города, из которых мы поступили.')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "39", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Найти и сфотать на парковке Honda Vezel')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "40", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Говорить только на английском ближайшие 5 минут')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "41", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Назвать / Включить  текущую песню в плеере')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "42", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Назвать самый верхний на данный момент ТГ-канал')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(lambda message: message.text == "43", state=FSMAdmin.quiz1)
async def download_photo(message: types.Message):
    filename = "numbers.txt"
    f = open(filename, 'a+')  # open file in append mode
    f.write('\n' + message.text)
    f.close()
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, 'Сыгранные задания:')
    await bot.send_message(message.chat.id, f'{file_contents}') 
    await bot.send_message(message.chat.id, 'Назвать последний просмотренный / просматриваемый ролик в Ютюбе')
 ##   filename = "numbers.txt"     
    await bot.send_message(message.chat.id, 'Продолжаем!')


@dp.message_handler(state=FSMAdmin.quiz1)
async def any_text_message(message: types.Message):
    fn0p = message.from_user.id
    await bot.send_message(1049416300, f'#квиз {message.text} {fn0p}')
    filename = "numbers.txt"
    f = open(filename, 'r')
    file_contents = f.read()
    f.close()
    await bot.send_message(message.chat.id, f'{file_contents}')
    await bot.send_message(message.chat.id, 'Продолжаем!')

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
        await bot.send_message(message.chat.id, 'Фото отправлено!', reply_markup=kb.inline_kb_full_0b)

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
