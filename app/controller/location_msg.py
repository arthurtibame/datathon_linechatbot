from app import handler, line_bot_api

from linebot.models.events import (
    LocationMessage
)
from linebot.models import(
    MessageEvent, TextSendMessage
)

@handler.add(MessageEvent, message=LocationMessage)
def location_handler(event):
    print(event.message)
    line_bot_api.reply_message( 
    event.reply_token,
    TextSendMessage(text="收到位置"))

