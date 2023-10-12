from time import sleep

from web.driver import PrigozhinSelenium

bot = PrigozhinSelenium()
bot.raw_go()
try:
    bot.parse()
except:
    try:
        cpt = bot.captcha()
        print("First try")
    except:
        sleep(30)
        cpt = bot.captcha()
        print("Ready! 2nd try")
