# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv 



load_dotenv()


class Var(object):

    MULTI_CLIENT = False

    API_ID = int(getenv('API_ID',"26872474"))

    API_HASH = str(getenv('API_HASH',"f8d3a289bf28a13a7159ad0b2ed114e7"))

    BOT_TOKEN = str(getenv('BOT_TOKEN',"6166862817:AAGoryxbujDDODRLrCTO7hJV153fdqbgE2c"))

    SESSION_NAME = str(getenv('SESSION_NAME', 'filetolinkbot'))

    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

    WORKERS = int(getenv('WORKERS', '4'))

    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001850979293'))

    PORT = int(getenv('PORT', 8000))

    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))

    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5211097531").split())  

    LONG_DROPLINK_URL=str(getenv('LONG_DROPLINK_URL',"paisakamalo.in"))

    SHORTENER_API=str(getenv('SHORTENER_API',"9d7e32c571c44b3ee91a814fa25c31e0211f5aeb"))
                          
    NO_PORT = bool(getenv('NO_PORT', False))

    APP_NAME= str(getenv('APP_NAME','fastlink-39f7f5a4099e'))

#    APP_NAME = str(getenv('APP_NAME','filetolinktb.onrender.com')) #@fligher

    OWNER_USERNAME = str(getenv('OWNER_USERNAME',"RBEagle2k"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL',"mongodb+srv://Karnan2k:karnan2k@cluster0.guq8k77.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL',"MainChannal2k"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001850979293")).split())) 
