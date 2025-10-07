import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID","23024283" ))  
API_HASH = os.getenv("API_HASH", "658d604b76eb60d7c99596b7440f90af")

# Bot Token / String Session
BOT_TOKEN = os.getenv("BOT_TOKEN", "8068358269:AAEYFDgmPrkdaOlE3MTiOT_VUoB_UuF2Dbk")
STRING1 = os.getenv("STRING_SESSION", "BQCOaU4AHxKOHxR54c_N1V8pqMgd4Xesex7wHRsMB4SBHnzg4X7w_Xqcuhe6x7gxCR7xOhNyvoPDJxVCKiZDftJuEDHxHhCA9MXSrom6tU4qilzYf8IsGckWyCH0PDaola0AH4ZYsK_UUL-P4QYmedr2STDPAYcJ-aCctSWbj50dhyXntIylaq9oTD2SPSVbTzu5kuLYxCFScrXer9CB-vbLYXXNSzCrk5YLrv8vXDNZnLutHTRjBralhI2A_TVjcBOvM1AfJbr98mF5SJ7R7CMqgf3tcDlKHd_jKh40pI-8cmm37C-AMaGNpXu1BPnYR5Svb29m7SAV8wvtlGiYPlP6Ih8raAAAAAHt2Ed2AA")

# Database
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://telegramescrower_db_user:EoWsXsfXtJrMb5GC@dkdk.sprm6ke.mongodb.net/?retryWrites=true&w=majority&appName=Dkdk")

# Owner / Admin
OWNER_ID = int(os.getenv("OWNER_ID", "7804917014"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", " CertifiedSexer")

# Support / Updates
SUPPORT_GRP = os.getenv("SUPPORT_GRP", "Zenxode")
UPDATE_CHNL = os.getenv("UPDATE_CHNL", "UrTGmarket")