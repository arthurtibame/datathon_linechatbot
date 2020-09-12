import requests


def flooding_town():
    town_codes = list()
    res = requests.get("http://fhy.wra.gov.tw/WraApi/v1/Rain/Warning?$top=100")
    res_json = res.json()
    town_codes= [f["TownCode"] for f in res_json]     
    return town_codes



if __name__ == "__main__":
    print(flooding_town())
