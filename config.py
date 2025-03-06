import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7429048456:AAEH21RqF9AuwkjFl7FcnpGtJd4B2_uTsHk')
    API_ID = int(os.environ.get("API_ID", '22594398'))
    API_HASH = os.environ.get("API_HASH", '3a2408d97d6a222d87766dac2da302df')
    AUTH_USER = os.environ.get('AUTH_USERS','5357048091').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌"#Here You Can Change with Your Name  or any custom name or title you prefer
