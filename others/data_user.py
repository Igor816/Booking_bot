from aiogram.fsm.context import FSMContext
# from aiogram.types import CallbackQuery
from others.requests import Requests


# async def add_db_prise_service(state: FSMContext, requests: Requests):#call: CallbackQuery,
#     data = state.get_data()
#     # db_time = call.data.split('=')[1].split('|')[0]
#     # db_date = call.data.split('=')[1].split('|')[1]
#     db_time = data["state_time"]
#     db_date = data["state_date"] 
#     db_price = data["price"]
#     dp_service = data["state_service"]
#     dp_add_serv = data["state_add_service"]

    
#     total_price = int(db_price)
#     text_add_serv = [dp_service]
#     for el_data in dp_add_serv:
#         for key, value in el_data.items():
#             text_add_serv.append(key)
#             total_price += int(value)
    
#     await requests.db_service_price(text_add_serv, total_price, db_date, db_time)

async def paste_data_db(state: FSMContext, requests: Requests):
    data = await state.get_data()
    data_needed = data['state_date']
    time_needed = data['state_time']
    service = data['state_service']
    price = data['price']
    dp_add_serv = data['state_add_service']
    
    total_price = int(price) 
    add_service = [service]
            
    for el_data in dp_add_serv:
        for key, value in el_data.items():
            add_service.append(key) 
            total_price += int(value)
    
    result_serv = ", ".join(add_service)
    
    await requests.db_service_price(result_serv, total_price, data_needed, time_needed)


async def get_data_state(state: FSMContext):
    data = await state.get_data()
    data_needed = data['state_date']
    time_needed = data['state_time']
    service = data['state_service']
    price = data['price']
    
    text_user = f"Выбранная дата: {data_needed},\r\nВыбранное время: {time_needed},\
    \r\nВаша стрижка: {service} {price}\r\n"
    total_price = int(price) 
    
    if "state_add_service" in data:
        dict_data = data["state_add_service"]
        text_user += "\r\nСопутствуещие услуги: "            
        for el_data in dict_data:
            for key, value in el_data.items():
                text_user += f"\r\n{key} {value}$" 
                total_price += int(value)
        text_user += f"\r\n\r\nСумма к оплате: {total_price}$"
    return text_user






async def get_data_for_admin(state: FSMContext):
    data = await state.get_data()
    data_needed = data['state_date']
    time_needed = data['state_time']
    service = data['state_service']
    price = data['price']
    
    name = data['state_name']
    # phone = data['state_get_phone']
    phone2 = data['hand_enter_number']
    
    text_user = f"Требуется подтверждение.\n"\
                f"Имя: {name},\r\nТелефон: {phone2},\n"\
                f"Дата: {data_needed},\r\nВремя: {time_needed},\r\n"\
                f"Cтрижка: {service} {price}\r\n$"
    
    total_price = int(price) 
    
    if "state_add_service" in data:
        dict_data = data["state_add_service"]
        
        text_user += "\r\nСопутствуещие услуги: "            
    
        for el_data in dict_data:
            for key, value in el_data.items():
                text_user += f"\r\n{key} {value}$" 
                total_price += int(value)

        text_user += f"\r\n\r\nСумма к оплате: {total_price}$"
    
    return text_user


