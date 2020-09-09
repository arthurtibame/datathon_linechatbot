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
from app.utils.events_tool import logs_handler
config = configparser.ConfigParser()
config.read("./app/utils/configure.ini")

app = Flask(__name__)

line_bot_api = LineBotApi(config.get('LINE', 'CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(config.get('LINE','CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    logs_handler(body)
    # app.logger.info(body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

from linebot.models import (
    RichMenuArea, RichMenu, RichMenuBounds, RichMenuSize, LocationAction, 
    MessageAction, URIAction

)

rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=2500, height=1686),
    selected=False,
    name="test20",
    chat_bar_text="Menu",
    areas=[
        RichMenuArea(
            bounds=RichMenuBounds(x=721, y=0, width=1038, height=576),
            action=MessageAction(label='None1', text="尚未開發")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=1767, y=0, width=733, height=690),
            action=MessageAction(label='None2', text="尚未開發")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=1097, width=869, height=589),
            action=URIAction(label='github', uri="https://github.com/arthurtibame")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=716, height=801),
            action=URIAction(label='Linkedin', uri="https://www.linkedin.com/in/shuli-lin-1679a9152/")
        ),

        RichMenuArea(
            bounds=RichMenuBounds(x=1653, y=1101, width=847, height=595),
            action=URIAction(label='Reference', uri="https://github.com/line/line-bot-sdk-python")
        ),
        RichMenuArea(
            bounds=RichMenuBounds(x=736, y=594, width=1017, height=476),
            action=URIAction(label='Datathon', uri="https://2020datathon.wixsite.com/hack")
        )
    ]
)
rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
# print(rich_menu_id)

with open("./static/image/04.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image(rich_menu_id,  "image/png", f)
line_bot_api.set_default_rich_menu(rich_menu_id)    
print("done!")    

from app.controller import reply_msg, join_event,rich_menu, quick_reply_msg, location_msg