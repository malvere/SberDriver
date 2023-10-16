import asyncio
from time import sleep

from bot.src.start import start_bot
from web.driver import PrigozhinSelenium

bot = asyncio.run(start_bot())
driver = PrigozhinSelenium()
driver.raw_go()
try:
    driver.parse()
except:
    try:
        cpt = driver.captcha()
        cpt.screenshot()
        print("First try")
        driver.grace_shutdown()
    except:
        sleep(30)
        cpt = driver.captcha()
        cpt.screenshot()
        print("Ready! 2nd try")
        driver.grace_shutdown()
