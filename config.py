import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID","23024283" ))  
API_HASH = os.getenv("API_HASH", "658d604b76eb60d7c99596b7440f90af")

# Bot Token / String Session
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING1 = os.getenv("STRING_SESSION", "")

# Database
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://telegramescrower_db_user:EoWsXsfXtJrMb5GC@dkdk.sprm6ke.mongodb.net/?retryWrites=true&w=majority&appName=Dkdk")

# Owner / Admin
OWNER_ID = int(os.getenv("OWNER_ID", "7804917014"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "CertifiedSexer")

# Support / Updates
SUPPORT_GRP = os.getenv("SUPPORT_GRP", "Zenxode")
UPDATE_CHNL = os.getenv("UPDATE_CHNL", "UrTGmarket")