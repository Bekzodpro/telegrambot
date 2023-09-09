import logging
from aiogram import Bot, Dispatcher, executor, types
# Initialize bot and dispatcher
from aiogram import types

from loader import dp
@dp.message_handler(commands=['start', 'help',"1","2","3",'4',"5",'6',"7",'8',"9",'0'])
async def send_welcome(message: types.Message):
    keys = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
    keys.add(
        types.KeyboardButton(text="⌨️ tez klaviyatura ro`yxati ⌨️"),
        types.KeyboardButton(text="🎮 Grafik dizayner uchun o`yinlar 🎮"),
        types.KeyboardButton(text="🐭 sichqoncha ishlamaganda 🐭"),
        types.KeyboardButton(text="wordda Muhammad(s.a.v) ismlarini arabcha yozish ﷺ"),        
        types.KeyboardButton(text="🤖Bot haqida bilib olish🤖"),
        types.KeyboardButton(text="🤨O`zingiz haqida bilib olish🤨")

    )
    await message.reply("""Salom """,reply_markup=keys)




@dp.message_handler(text="⌨️ tez klaviyatura ro`yxati ⌨️")
async def klavatura(message:types.Message):
    await message.answer("""🟦Windows 10 operatsion tizimida eng ko'p ishlatiladigan tezkor tugmalar ro'yxati

| #klaviatura | #tugma | #tezkor |

ALT + F4   —   Faol dasturlarni ishini to'xtatadi;
ALT + Tab   —  Oynadan oynaga ko'chish;
ALT + Shift   —   Tilni almashtirish;
ALT + Enter  —   Cвoйcтвa ni ochish;

Ctrl + S   —   Saqlash;
Ctrl + C   —   Nusxa olish;
Ctrl + X   —   Kesib olish;
Ctrl + V   —  Qo'yish;
Ctrl + Z   —   Amallarni ortga qaytarish;
Ctrl + Y   —   Qaytarilgan amallarni oldinga o'tkazish;
Ctrl + W   —   Oynani yopish;
Ctrl + A   —   Hammasini belgilash;
Ctrl + P   —   Chop etish;
Ctrl + Shift + Esc  —   Vazifa menejeri(Диспетчер задач);

Пуск -> Win

Win + E   —   Этот компьютер ni ochish;
Win + R   — Dasturlarni tezkor ishga tushirish oynasi;
Win + D   —   Barcha oynalarni teskari o'girish;
Win + Tab   —   Faol oynalarni ko'rish;
Win + P   —   Ekranni loyihalash;
Win + I   —   Kompyuter sozlamalariga o'tish;
Win + M   —   Barcha oynalarni vazifalar paneliga tushirish;
Win + S   —   Qidiruv tizimi;
Win + Space(Probel)   —   Tilni almashtirish;
Win + PrtSc   —   Ekranni rasmga olish;
Win + L   —   Kompyuter foydalanuvchisi almashtirish;
Win + U   —   Ekran sozlamalariga kirish;
Win + Pause-Break   —   Kompyuter haqida ma'lumot;


Ctrl + T   —   Yangi tab ochish;
Ctrl + W   —   Ochiq tabni yopish;
Ctrl + Shift + T   —   Yopilgan tablarni qayta ochish;
Shift + Esc   —   Vazifa menejeri(Диспетчер задач);
Alt + F4   —   To'liq yopish;
Ctrl + R | F5 | Ctrl + F5   —   Sahifani yangilash;
Ctrl + Shift + A   —   Tablar ichidan qidirish;
Ctrl + N   —  Yangi oyna ochish;
Ctrl + J   —   Yuklamalar jadvali;
Ctrl + H   —   Tarix;
Ctrl + F   —  Sahifa ichidan qidirish;
Ctrl + S   — Sahifani saqlab olish;
Ctrl + Shift + Delete   —   Tarixni tozalash""")
    
@dp.message_handler(text="🎮 Grafik dizayner uchun o`yinlar 🎮")
async def dizayn(message:types.Message):
    await message.answer("""🎯 Grafik Dizaynerlar uchun foydali o'yinlar:

1. https://bezier.method.ac/
2. https://type.method.ac/
3. https://shape.method.ac/
4. https://color.method.ac/
5. http://kolor.moro.es/
""")
    
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def getphot(message:types.Message):
    await message.answer("Photo yaxshi chiqmagan")

@dp.message_handler(content_types=types.ContentType.AUDIO)
async def getphot(message:types.Message):              
    await message.answer("bu yaxshi qo`shiq")              

@dp.message_handler(content_types=types.ContentType.STICKER)
async def getphot(message:types.Message):              
    await message.answer("bu stiker menga yoqdi.👍👌")  

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def getphot(message:types.Message):              
    await message.answer("bu yaxshi dieo emas ekan 🤔😕")  

@dp.message_handler(content_types=types.ContentType.GROUP_CHAT_CREATED)
async def getphot(message:types.Message):              
    await message.answer("bu guruh unchalik yaxshi emas ekan chunki unda hech kim yozmaydi😠")           

@dp.message_handler(text="🐭 sichqoncha ishlamaganda 🐭")
async def dizayn(message:types.Message):
    await message.answer("""Sichqonchangiz ishlamay qoldimi? Unda klaviaturangizdan sichqoncha o'rnida foydalaning! 

⌨️ Buning uchun Alt + Shift + Num Lock tugmalarini bosing. Sizga tasdiqlash oynasi ochiladi. Yes-ni bosing va ana endi klaviatura tugmalari yordamida kursorni boshqaring! (eng chekkadagi raqamlarni bosing!)""")

@dp.message_handler(text="wordda Muhammad(s.a.v) ismlarini arabcha yozish ﷺ")
async def bot_layfhak(message:types.Message):
    await message.answer(" word dasturida (fdfa)-ni yazib (Alt + x)-tugmasini bosing va Muhammad(s.a.v) ismlarini arabchada yozilgani hosil bo`ladi!")    

@dp.message_handler(text="🤨O`zingiz haqida bilib olish🤨")
async def bot_uzi(message:types.Message):
    await message.answer("⛔❌kechirasiz sizda bunaqa funksiya ishlamaydi!❌⛔")

@dp.message_handler(text="🤖Bot haqida bilib olish🤖")
async def bot_haqida(message:types.Message):
    await message.answer("Bu bot yaxshi bot.Bot hali yangi bo`lganligi uchun hali funlsiyalari ko`p emas! ")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("""Iltimos tugmalardan birini tanlang!
Yoki (rasm, stiker, audio, video, telegramdagi chat)-lardan birini yuboring!""")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
