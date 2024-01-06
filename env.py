import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "28542813").strip()
API_HASH = os.getenv("API_HASH", "02ce7c339f7776844ff4ab03da338ccd").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6796476756:AAGvgQXojSoDdWFYj_AoPO1wSgn-Jfg9-x8").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://yashsing2008:12345678yash@cluster0.j8n5cqz.mongodb.net/?retryWrites=true&w=majority").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/YS_SUPPORT_CHAT")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
