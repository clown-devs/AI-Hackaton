import io
import os

import aiohttp
import requests
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.exceptions import MessageCantBeDeleted

from bot.create_bot import bot


class FSMSetDoc(StatesGroup):
    new_value = State()


async def upload(message: types.Message, state: FSMContext):
    try:
        msg = await bot.send_message(message.from_user.id, "Отправьте файл")
        async with state.proxy() as data:
            data['msg'] = msg
            await FSMSetDoc.new_value.set()

        try:
            await message.delete()
        except MessageCantBeDeleted:
            pass
    except:
        pass


async def doc_set(message: types.Message, state: FSMContext, **kwargs):
    async with state.proxy() as data:
        # Забираем необходимую информацию
        msg: types.Message = data["msg"]

        if message.document.mime_type in ['text/plain'] and message.document.file_name[-3:] == 'REC':
            if message.document.file_size < 83886080:
                # Сохраняем файл
                await msg.edit_text("Пожалуйста подождите загрузки файла🕒")
                await state.finish()

                print(message.document.file_id)
                file_info = await bot.get_file(message.document.file_id)

                BOT_TOKEN = os.getenv("TOKEN")
                file_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}'

                # Получение файла
                response = requests.get(file_url, stream=True)
                print(response)

                # Проверка успешности GET-запроса
                if response.status_code == 200:
                    # Отправка файла на ваш сервер
                    files = {'file': ('filename', response.raw)}
                    post_response = requests.post("http://v0d14ka.ddns.net:99/", files=files)
                    print(post_response.json())

                    # Проверка успешности POST-запроса
                    if post_response.status_code == 200:
                        print('Файл успешно отправлен.')
                    else:
                        print(f'Ошибка при отправке файла: {post_response.status_code}')
                        print(post_response.text)
                else:
                    print(f'Ошибка при получении файла: {response.status_code}')

                if response != "error":
                    await msg.edit_text("Файл успешно сохранен!✅")
                else:
                    await msg.edit_text("В данный момент прием работ не принимается")

        else:
            await msg.edit_text("Неверный формат файла❌. Пожалуйста, отправьте файл в формате PDF.")
            await message.delete()
            return

        await message.delete()
        await state.finish()


def register_handlers_general(_dp: Dispatcher):
    _dp.register_message_handler(upload, commands=['file'], state=None)
    _dp.register_message_handler(doc_set, state=FSMSetDoc.new_value, content_types=['document'])
    _dp.register_message_handler(doc_set, commands=['start', 'help'], state=None)
