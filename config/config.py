from decouple import config

TOKEN = config('TOKEN')
PREFIX = config('PREFIX' , default='/')