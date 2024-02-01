from decouple import config

config.read_dotenv('../config/.env')

TOKEN = config('TOKEN', default='MTIwMDA1NjQxMzcwNDE3OTc2Mg.GNl2Vk.oGeiRiTvZ6pi8R89oKGUx751XIRADkfdOKbfMo')
PREFIX = config('PREFIX', default='/')