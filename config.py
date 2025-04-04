import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7151674132:AAEZXSIktkinA3ZhzyEIqVZ6FuJgM2eMBM4')
    API_ID = int(os.environ.get("API_ID", '24025791'))
    API_HASH = os.environ.get("API_HASH", 'b4980ef76018e77ce8d96cde35451fa9')
    AUTH_USER = os.environ.get('AUTH_USERS','7170328188').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://api.masterapi.tech"
    CREDIT = "ᗅოꪖꫛ"#Here You Can Change with Your Name  or any custom name or title you prefer
