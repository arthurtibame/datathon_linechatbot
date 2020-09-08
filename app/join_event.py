from app import app,  handler, line_bot_api

from linebot.models.events import JoinEvent, FollowEvent

from linebot.models import (
    TextSendMessage, TextMessage
)
from utils.events_tool import event2json, timestamp2date
@handler.add(FollowEvent)
def handle_join(event):
    newcoming_text = "謝謝邀請我這個機器來至此群組！！我會盡力為大家服務的～"
    dictEvent=event2json(event)
    userId=dictEvent["source"]["userId"]
    timestamp = dictEvent["timestamp"]    
    print(type(timestamp))
    
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=userId)
    )


    print("userId: ", userId,timestamp)

    