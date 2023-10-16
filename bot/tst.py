from dotenv import load_dotenv

load_dotenv('bot/py.env')
from config import conf

print(conf.bot.token)
