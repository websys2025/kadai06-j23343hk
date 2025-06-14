#１日の平均睡眠時間及び睡眠の質の状況（男性・20代）
import requests

APP_ID = "9ad612083d178d86735d5f7005c03821860850ac"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003224282",  #１日の平均睡眠時間及び睡眠の質の状況
    "cdCat01":"160",  #年齢を20代に限定
    "cdCat03":"110",  #性別を男性に限定
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