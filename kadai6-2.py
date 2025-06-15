# 国際農研　オープンデータ　2024年度　沖縄県でのイベント、シンポジウム
import requests

#国際農研　オープンデータ　イベント・シンポジウム (json)
API_URL = "https://www.jircas.go.jp/ja/event/2024/eventlist.json"

response = requests.get(API_URL)
data = response.json()

#開催地（addressRegion）の取得
for event in data:
    location = event.get("schema:location", {})
    addresses = location.get("schema:address", [])

#開催地が沖縄県のイベント名の抽出
    for addr in addresses:
        if addr.get("schema:addressRegion") == "沖縄県":
            
#イベント名(title)の表示
            title = event["dc:title"][0]["@value"]
            print(title)