from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

#Читаем токен из файла token.txt и записываем в переменную.
with open('token.txt', 'r') as f:
    BOT_TOKEN=f.read()

#Инициализируем бота и диспетчера.
bot=Bot(BOT_TOKEN)
dp=Dispatcher()

#Реализуем хэндлер на комманду /start
@dp.message(Command(commands=['start']))
async def process_command_start(message:Message):
    await message.answer('Привет. Меня зовут Эхо-Бот и я повторю всё что ты напишешь.')

#Реализуем хэндлер на комманду /help
@dp.message(Command(commands=['help']))
async def process_command_help(message:Message):
    await message.answer('Я повторяю всё что ты пишешь.')

#Реализуем хэндлер на любые сообщения
@dp.message()
async def process_echo(message:Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except:
        await message.answer('Данный хэндлер не может быть обработан.')


if __name__=='__main__':
    dp.run_polling(bot)