from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram import Bot,executor,Dispatcher,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from my_buttons import menu,admins_menu,zat_qosiw_menu


from datas import start_db,add_to_db,show_foods

async def start_bot():
    await start_db()


api = '7937457837:AAETL-AVA3Y594dBoLybIGuV92uYdE_MwBc'
proxy_url = 'http://proxy.server:3128'
bot = Bot(api,proxy=proxy_url)

storage = MemoryStorage()
dp = Dispatcher(bot=bot,storage=storage)

class FoodState(StatesGroup):
    type_of_food = State()
    price = State()
    name = State()
    photo = State()
    ingridients = State()
class RegState():
    name = State()
    phone_num = State()
    #name,phone_num,id, username -> database


admin_id = 5570471897
@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    if admin_id==sms.from_user.id:
        await sms.answer(text='Salem Admin',
                         reply_markup=admins_menu)
    else:
        await sms.answer(text='Assalamu aleykum',
                         
                         reply_markup=menu)
        
#for admin
@dp.message_handler(text='Zat qosiw')
async def start_adding(sms:types.Message):
    if admin_id==sms.from_user.id:
        await sms.answer(text='Tomendegi knopkalardan birin tanlan:',
                         reply_markup=zat_qosiw_menu)
        await FoodState.type_of_food.set()
@dp.message_handler(content_types='text',state=FoodState.type_of_food)
async def send_qosiw(sms:types.Message,state:FSMContext):
    if admin_id==sms.from_user.id:
        async with state.proxy() as foods:
            foods['type']=sms.text
        await sms.answer('Endi bizge cenasin jazin:')
        await FoodState.price.set()
@dp.message_handler(state=FoodState.price)
async def send_price(sms:types.Message,state:FSMContext):
    async with state.proxy() as foods:
        foods['price']=sms.text
    await sms.answer('Endi bizge atin jazin:')
    await FoodState.name.set()

@dp.message_handler(state=FoodState.name)
async def send_price(sms:types.Message,state:FSMContext):
    async with state.proxy() as foods:
        foods['name']=sms.text
    await sms.answer('Endi bizge ingridientin jazin jazin:')
    await FoodState.ingridients.set()

@dp.message_handler(state=FoodState.ingridients)
async def send_price(sms:types.Message,state:FSMContext):
    async with state.proxy() as foods:
        foods['ingridients']=sms.text
    await sms.answer('Endi bizge suwretin jiberin:')
    await FoodState.photo.set()

@dp.message_handler(state=FoodState.photo,content_types='photo')
async def send_price(sms:types.Message,state:FSMContext):
    async with state.proxy() as foods:
        foods['photo']=sms.photo[0]['file_id']
    await sms.answer_photo(
        photo=foods['photo'],
        caption=f'''Tagamnin type : {foods['type']},
Tagamnin cenasi: {foods['price']}''',reply_markup=admins_menu
    )
    await add_to_db(type=foods['type'])
    await state.finish()











if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True,
                           on_startup=start_bot)
