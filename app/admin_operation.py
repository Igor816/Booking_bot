from aiogram import Router, F,  Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from others.requests import Requests

rot = Router()


@rot.callback_query(F.data.startswith('confirmreserve')| F.data.startswith('canselreserve'))
async def answer_reserve(call: CallbackQuery, requests: Requests, bot: Bot):#, state: FSMContext
    type_answer = call.data.split('=')[0]
    date_answer = call.data.split('=')[1].split('|')[0]
    time_answer = call.data.split('=')[1].split('|')[1]
    id_user_answer = call.data.split('=')[1].split('|')[2]
    text = call.message.text.replace('Требуется подтверждение', ' ')
    
    
    if 'confirmreserve' in type_answer:
        await requests.db_change_statuse('buse', date_answer, time_answer)
        msg_user = f'ВАШ ЗАКАЗ ПОДТВЕРЖДЕН\r\n\r\n{text}' 
        msg_admin = f'ЗАКАЗ ПОДТВЕРЖДЕН\r\n\r\n{text}' 
        await call.message.edit_text(msg_admin, reply_markup=None)
        await bot.send_message(id_user_answer, f'{msg_user}\r\n\r\nМенеджер вам перезвонит!')
    
    else:
        msg_user = f'ВАШ ЗАКАЗ ОТКЛОНЕН\r\n\r\n{text}'
        msg_admin = f'ЗАКАЗ ОТКЛОНЕН\r\n\r\n{text}'   
        await call.message.edit_text(msg_admin, reply_markup=None)
        await bot.send_message(id_user_answer, msg_user)