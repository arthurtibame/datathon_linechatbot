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
    
    addr_transferred = addr_transfer(language=user.language, addr=event.message.address) 
    
    user.address = event.message.address
    user.city = addr_transferred[0]
    user.town = addr_transferred[1]
    user.longitude =  event.message.longitude
    user.latitude = event.message.latitude    
    db.session.commit()
    return "updated location"
    
def addr_transfer(language, addr):
    if language == "en":
        addr_transferred = en_addr_transfer(addr)
        return addr_transferred
    else: 
        addr_transferred = zh_addr_transfer(addr)
        return addr_transferred

def en_addr_transfer(addr):
    """[summary]

    Args:
        addr (String): [user address]

    Returns:
        [list]: [town, city]
    """
    tmp_list = addr.split(",")       
    tmp_list = [f.strip() for f in tmp_list[-3:-1]]
    city = city2code_en(tmp_list[1])
    print(city, tmp_list)
    
    return [tmp_list[0], city]

def zh_addr_transfer(addr):
    city = addr[5:8]
    chk_district = addr[8:]
    sep_words = ["區", "鄉", "鎮", "市"]
    town=""
    for counter in range(len(chk_district)):
        if chk_district[counter] in sep_words:
            town = chk_district[:counter+1]
    return [city, town]

def city2code_en(city):
    import json
    with open("./app/utils/city_codes.json", mode="r", encoding="utf8") as json_file:
        data = json.load(json_file)
    for json in data:
        if city == json["CityName_En"]:
            return json["CityCode"]