from flask import Flask, request

from flask import request, abort
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot import (
    LineBotApi, WebhookHandler
)
import configparser
config = configparser.ConfigParser()
config.read("./utils/configure.ini")

app = Flask(__name__)

line_bot_api = LineBotApi(config.get('LINE', 'CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(config.get('LINE','CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

from app import reply_msg, join_event