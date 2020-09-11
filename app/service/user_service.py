from app import db
from app.model.user_model import User

def check_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return True
    else:
        return False

def create_user(profile, user_id):
    if check_user(user_id) ==False:

        try:
            user_name = profile.display_name
            language = profile.language
            picture_url = profile.picture_url
            status_message = profile.status_message
            new_user = User(user_id=user_id,
                user_name=user_name, 
                language=language, 
                picture_url=picture_url           
            )
            db.session.add(new_user)    
            db.session.commit()
            return True
        except:
            return False
    else:
        return "Exists"

def check_location(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user.address and user.longitude and user.latitude:
        return True
    else:
        return False



def udpate_location(event):           
    user_id = event.source.user_id   
    user = User.query.filter_by(user_id=user_id).first()        
    user.address = event.message.address
    user.longitude =  event.message.longitude
    user.latitude = event.message.latitude    
    db.session.commit()
    return True
    
        