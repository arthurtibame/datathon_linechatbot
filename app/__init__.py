import json
from flask import Flask, request
from flask import request, abort
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.models import (
    RichMenuArea, RichMenu, RichMenuBounds, RichMenuSize, LocationAction

)

import configparser
import os
from flask_sqlalchemy import SQLAlchemy 
from app.utils.events_tool import logs_handler
config = configparser.ConfigParser()
config.read("./app/utils/configure.ini")

app = Flask(__name__)
app.config.from_object('app.utils.setting')     #模块下的setting文件名，不用加py后缀 
app.config.from_envvar('FLASKR_SETTINGS', silent=True)   #环境变量，指向配置文件setting的路径
app.config['SQLALCHEMY_DATABASE_URL'] = "mysql://arthurtibame:Mbb67594@35.201.161.222/datathon"

line_bot_api = LineBotApi(config.get('LINE', 'CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(config.get('LINE','CHANNEL_SECRET'))
db = SQLAlchemy(app)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    logs_handler(body, line_bot_api)
    # app.logger.info(body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

from app.model import user_model, log_model
from app.service import user_service, log_service, flooding_service

from app.message import (
    reply_msg, join_event_msg, quick_reply_msg, location_msg, image_msg,
    video_msg
)

from app.rich_menu import (
    rich_menu
)

from app.utils import (
    events_tool, kafka_logs
)