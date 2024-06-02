import os

import requests
from aiogram import types, Dispatcher


from create_bot import bot


async def doc_set(message: types.Message, **kwargs):
    if message.document.mime_type not in ['text/plain'] or message.document.file_name[-3:] != 'REC':
        await bot.send_message(message.from_user.id, "Неверный формат файла ❌. Загрузите файл в формате .REC!")
        await message.delete()
        return

    if message.document.file_size > 83886080:
        await bot.send_message(message.from_user.id, "Превышен максимально допустимый объем файла ❌")
        await message.delete()
        return

    msg = await bot.send_message(message.from_user.id, "Пожалуйста дождитесь загрузки файла🕒")
    try:
        file_info = await bot.get_file(message.document.file_id)
    except:
        await msg.edit_text("Файл слишком большой, максимально допустимый размер - 20 Мб.")
        await message.delete()
        return

    BOT_TOKEN = os.getenv("TOKEN")
    file_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}'

    # Получение файла
    response = requests.get(file_url, stream=True)
    print(response)

    # Проверка успешности GET-запроса
    if response.status_code == 200:
        files = {'file': ('filename', response.raw)}
        post_response = requests.post("http://v0d14ka.ddns.net:99/", files=files)

        # Проверка успешности POST-запроса
        if post_response.status_code == 200:
            word_url = post_response.json()['word_url']
            dead = post_response.json()['dead']
            get_word_response = requests.get(f"http://v0d14ka.ddns.net:99/{word_url}", stream=True)

            if get_word_response.content is not None:
                await msg.delete()
                await bot.send_document(message.from_user.id, get_word_response.content,
                                        caption=f' {"Патологий не обнаружено." if dead == False else "Обнаружены патологии, обратитесь к врачу"}. Отчет в формате WORD!')
            else:
                await msg.edit_text("Произошла непредвиденная ошибка, повторите попытку позже.")

        else:
            print(f'Ошибка при отправке файла: {post_response.status_code}')
            print(post_response.text)
            await msg.edit_text("Произошла непредвиденная ошибка, повторите попытку позже.")
            return
    else:
        print(f'Ошибка при получении файла: {response.status_code}')
        await msg.edit_text("Произошла непредвиденная ошибка, повторите попытку позже.")
        return

    await message.delete()


def register_handlers_general(_dp: Dispatcher):
    _dp.register_message_handler(doc_set, content_types=['document'], state=None)
