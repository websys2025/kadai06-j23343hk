#１日の平均睡眠時間別、睡眠の質の状況 - １日の平均睡眠時間、睡眠の質の状況、年齢階級別、人数、割合 - 総数・男性・女性、20歳以上 

import requests

APP_ID = "9ad612083d178d86735d5f7005c03821860850ac"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003224282",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)