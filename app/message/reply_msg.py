from app import handler, line_bot_api

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "否, 下次再傳送":
        line_bot_api.reply_message( 
            event.reply_token,
            TextSendMessage(text="謝謝您, 隨時歡迎更新位置"))
