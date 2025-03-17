from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

##0(1,2)
inline_kb_full_0= InlineKeyboardMarkup(row_width=2)
inline_btn_05 = InlineKeyboardButton('🦸‍♂️ Связь с АрТомом Сендлер-Харди', callback_data='btn05')
inline_btn_06 = InlineKeyboardButton('❓ Вопросики', callback_data='btn06')
inline_kb_full_0.row(inline_btn_06)
inline_kb_full_0.row(inline_btn_05)



##0(1,2)
inline_kb_full_06= InlineKeyboardMarkup(row_width=2)
inline_btn_060 = InlineKeyboardButton('⬅️ назад', callback_data='btn060')
inline_btn_061 = InlineKeyboardButton('1', callback_data='btn061')
inline_btn_062 = InlineKeyboardButton('2', callback_data='btn062')
inline_btn_063 = InlineKeyboardButton('3', callback_data='btn063')
inline_btn_064 = InlineKeyboardButton('4', callback_data='btn064')
inline_btn_065 = InlineKeyboardButton('5', callback_data='btn065')
inline_btn_066 = InlineKeyboardButton('6', callback_data='btn066')
inline_kb_full_06.row(inline_btn_061)
inline_kb_full_06.row(inline_btn_062)
inline_kb_full_06.row(inline_btn_063)
inline_kb_full_06.row(inline_btn_064)
inline_kb_full_06.row(inline_btn_065)
inline_kb_full_06.row(inline_btn_066)
inline_kb_full_06.row(inline_btn_060)


##0(1,2)
inline_kb_full_06b= InlineKeyboardMarkup(row_width=2)
inline_btn_06b1 = InlineKeyboardButton('⬅️ Назад', callback_data='btn06')
inline_kb_full_06b.row(inline_btn_06b1)


##0(1,2)
inline_kb_full_08= InlineKeyboardMarkup(row_width=2)
inline_btn_081 = InlineKeyboardButton('🆗 Отлично', callback_data='btn081')
inline_btn_082 = InlineKeyboardButton('⬅️ Назад', callback_data='btn00')
inline_kb_full_08.row(inline_btn_081)
inline_kb_full_08.row(inline_btn_082)

##0(1,2)
inline_kb_full_082= InlineKeyboardMarkup(row_width=2)
inline_btn_0821 = InlineKeyboardButton('🆗 Записываемся дальше', callback_data='btn0821')
inline_kb_full_082.row(inline_btn_0821)

##0(1,2)
inline_kb_full_083= InlineKeyboardMarkup(row_width=2)
inline_btn_0831 = InlineKeyboardButton('🆗 Записываемся дальше', callback_data='btn0831')
inline_kb_full_083.row(inline_btn_0821)


##0(1,2)
inline_kb_full_0b= InlineKeyboardMarkup(row_width=2)
inline_btn_0b1 = InlineKeyboardButton('⬅️ Назад', callback_data='btn00')
inline_kb_full_0b.row(inline_btn_0b1)


##0(1,2)
inline_kb_full_01= InlineKeyboardMarkup(row_width=2)
inline_btn_010 = InlineKeyboardButton('⬅️ Назад', callback_data='btn00')
inline_btn_011 = InlineKeyboardButton('✈️🌏', callback_data='btn011')
inline_btn_012 = InlineKeyboardButton('🧑‍💼🍽️', callback_data='btn012')
inline_btn_013 = InlineKeyboardButton('🍀🏭', callback_data='btn013')
inline_btn_014 = InlineKeyboardButton('🧑‍🏫🗺️', callback_data='btn014')
inline_kb_full_01.row(inline_btn_011)
inline_kb_full_01.row(inline_btn_012)
##inline_kb_full_01.row(inline_btn_013)
##inline_kb_full_01.row(inline_btn_014)
inline_kb_full_01.row(inline_btn_010)


##0(1,2)
inline_kb_full_01nb= InlineKeyboardMarkup(row_width=2)
inline_btn_01nb1 = InlineKeyboardButton('Спасибо, скорее приду', callback_data='btn01ny')
inline_btn_01nb2 = InlineKeyboardButton('Спасибо, скорее не приду', callback_data='btn01nn')
inline_kb_full_01nb.row(inline_btn_01nb1)
inline_kb_full_01nb.row(inline_btn_01nb2)

##0(1,2)
inline_kb_full_01b= InlineKeyboardMarkup(row_width=2)
inline_btn_01b1 = InlineKeyboardButton('Скорее интересно', callback_data='btn01y')
inline_btn_01b2 = InlineKeyboardButton('Скорее неинтересно', callback_data='btn01n')
inline_kb_full_01b.row(inline_btn_01b1)
inline_kb_full_01b.row(inline_btn_01b2)

##0(1,2)
inline_kb_full_0fb= InlineKeyboardMarkup(row_width=2)
inline_btn_0fb0 = InlineKeyboardButton('🔀 Еще факт!', callback_data='btn03')
inline_btn_0fb1 = InlineKeyboardButton('⬅️ Назад', callback_data='btn00')
inline_kb_full_0fb.row(inline_btn_0fb0)
inline_kb_full_0fb.row(inline_btn_0fb1)


##3(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,!5,16)
inline_kb_full_DL = InlineKeyboardMarkup(row_width=1)
inline_btn_DL0 = InlineKeyboardButton('0', callback_data='btnDL0')
inline_btn_DL1 = InlineKeyboardButton('1', callback_data='btnDL1')
inline_btn_DL2 = InlineKeyboardButton('2', callback_data='btnDL2')
inline_btn_DL3 = InlineKeyboardButton('3', callback_data='btnDL3')
inline_btn_DL4 = InlineKeyboardButton('4', callback_data='btnDL4')
inline_btn_DL5 = InlineKeyboardButton('5', callback_data='btnDL5')
inline_kb_full_DL.row(inline_btn_DL0, inline_btn_DL1, inline_btn_DL2, inline_btn_DL3, inline_btn_DL4, inline_btn_DL5)

inline_kb_full_PDL = InlineKeyboardMarkup(row_width=1)
inline_btn_PDL1 = InlineKeyboardButton('🔙Вернуться в начало', callback_data='btnPDL1')
#inline_btn_PDL2 = InlineKeyboardButton('Вернуться к выбору дней', callback_data='btn2A')
inline_kb_full_PDL.row(inline_btn_PDL1)
#inline_kb_full_PDL.row(inline_btn_PDL2)

##0(1,2)
inline_kb_full_r4c= InlineKeyboardMarkup(row_width=2)
inline_btn_r4c1 = InlineKeyboardButton('Да', callback_data='btnr4c1')
inline_btn_r4c2 = InlineKeyboardButton('Нет', callback_data='btnr4c2')
inline_kb_full_r4c.row(inline_btn_r4c1)
inline_kb_full_r4c.row(inline_btn_r4c2)


##0(1,2)
inline_kb_full_0pb= InlineKeyboardMarkup(row_width=2)
inline_btn_0pb0 = InlineKeyboardButton('🔀 Еще факт!', callback_data='btn09b')
inline_btn_0pb1 = InlineKeyboardButton('⬅️ Назад', callback_data='btn00')
inline_kb_full_0pb.row(inline_btn_0pb0)
inline_kb_full_0pb.row(inline_btn_0pb1)