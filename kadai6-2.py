# 国際農研　オープンデータ　2024年度　沖縄県でのイベント、シンポジウム
import requests

API_URL = "https://www.jircas.go.jp/ja/event/2024/eventlist.json"

response = requests.get(API_URL)
data = response.json()

for event in data:
    location = event.get("schema:location", {})
    addresses = location.get("schema:address", [])
    
    for addr in addresses:
        if addr.get("schema:addressRegion") == "沖縄県":
            title = event["dc:title"][0]["@value"]
            print(title)
            break