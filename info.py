# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import dns.resolver
import re
from os import environ

# --- DNS FIX FOR MONGODB ---
# This forces the bot to use Google DNS (8.8.8.8) to resolve your MongoDB cluster.
# This prevents the "DNS query name does not exist" error on Render.
try:
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = ['8.8.8.8']
except Exception as e:
    print(f"DNS Resolver error: {e}")

from Script import script 

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'cinebot')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Pictures for Start Message
PICS = (environ.get('PICS', 'AgACAgUAAxkBAAICuGht-6GMOH1PNyf31mjemh8PCzcYAALPxDEbEDJwV5LouvHkzjTeAAgBAAMCAAN4AAceBA')).split()

# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7204704497').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '7204704497').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002737880991'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002829192804').split()]
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002829192804')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# Force Subscribe Settings
REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False))
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False))
auth_channel = environ.get('AUTH_CHANNEL', '-1002804738225')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# Support and Request Channels
reqst_channel = environ.get('REQST_CHANNEL', '-1002412902656')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002412902656')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# --- MONGO DB CONFIGURATION (FIXED) ---
# We use the 'Standard' URI format to avoid DNS resolution issues on Render.
DEFAULT_URI = "mongodb://vishnusaketh07:cinebot@cluster0-shard-00-00.bdifagm.mongodb.net:27017,cluster0-shard-00-01.bdifagm.mongodb.net:27017,cluster0-shard-00-02.bdifagm.mongodb.net:27017/?ssl=true&replicaSet=atlas-m0z6v5-shard-0&authSource=admin&retryWrites=true&w=majority"

DATABASE_URI = environ.get('DATABASE_URI', DEFAULT_URI)
DATABASE_NAME = environ.get('DATABASE_NAME', "cinebot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Luffycollection')

MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', False))

# Logic to prevent empty URI crashes
if not MULTIPLE_DATABASE:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = environ.get('O_DB_URI', DATABASE_URI)
    FILE_DB_URI = environ.get('F_DB_URI', DATABASE_URI)
    SEC_FILE_DB_URI = environ.get('S_DB_URI', DATABASE_URI)

# Premium and Referral Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', False))
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>Premium Plan Details...</b>')

# Clone Information
CLONE_MODE = bool(environ.get('CLONE_MODE', False))
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "")
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '')

# External Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/cinebotofclgrup')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/cineofcl')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/cinebotofclgrup')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/luffydev2k')

# Feature Toggles
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
BUTTON_MODE = bool(environ.get('BUTTON_MODE', True))
MAX_BTN = bool(environ.get('MAX_BTN', True))
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
IMDB = bool(environ.get('IMDB', False))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", False))
SPELL_CHECK_REPLY = bool(environ.get("SPELL_CHECK_REPLY", True))
MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', True))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Token Verification
VERIFY = bool(environ.get('VERIFY', False))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')

# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
TUTORIAL = environ.get('TUTORIAL', '')

# Technical Settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Hello My Dear Friends ❤️')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")

# Filter Options
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = [f"season {i}" for i in range(1, 11)]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = [str(y) for y in range(1990, 2026)]

# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', False))
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")

# Auto Approve & Rename
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False))
RENAME_MODE = bool(environ.get('RENAME_MODE', False))

# Start Command Reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🔥", "😎", "🤩"]

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
