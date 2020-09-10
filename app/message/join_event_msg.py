from app import handler, line_bot_api
from app.message import quick_reply_msg

from linebot.models.events import JoinEvent, FollowEvent

from linebot.models import (
    TextSendMessage, TextMessage, QuickReply, QuickReplyButton, MessageAction, LocationAction
)
from app.utils.events_tool import event2json, datetime_now

@handler.add(FollowEvent)
def handle_join(event):    
    dictEvent=event2json(event)
    userId=dictEvent["source"]["userId"]
    now_time = datetime_now()
        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='請問您居住哪裡',
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=MessageAction(label="label", text="text")),
                    QuickReplyButton(action=MessageAction(label="label", text="text")),
                    QuickReplyButton(action=LocationAction(label="label1"))
                ],
            )
        )
    )
  

    