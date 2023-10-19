"""This file represents a start logic."""
from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

from web import web_driver

parse_router = Router(name='parse')


@parse_router.message(Command(commands='parse'))
async def capcha_handler(message: types.Message):
    """Captcha handler."""

    web_driver.raw_go()
    try:
        print("First attempt...")
        web_driver.parse()
        web_driver.grace_shutdown()
        return await message.answer("First try!")
    except:
        print("First attempt failed. Waiting for captcha")
        try:
            if web_driver.captcha_found():
                cpt = web_driver.captcha()
                cpt.screenshot()
                print("First try")
                f = FSInputFile("test.png")
                return await message.answer_photo(photo=f, caption="captcha detected!")

        except:
            print("something wend super wrong...")
            web_driver.grace_shutdown()
            return
    