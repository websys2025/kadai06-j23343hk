# kadai6-2.py

"""
課題6-2：JIRCAS（国際農林水産業研究センター）のイベント情報を取得して表示するプログラム

【参照するオープンデータ】
- データ名：JIRCAS イベント一覧（2024年）
- 提供：国際農林水産業研究センター（JIRCAS）
- URL（エンドポイント）：https://www.jircas.go.jp/ja/event/2024/eventlist.json
- 概要：JIRCASが開催するシンポジウム・講演会などのイベント情報をJSON形式で提供
- 主な項目：イベント名（title）、開催日（date）、リンクURL（path）、概要（description）など
"""

import requests

# JSONデータのURL
URL = "https://www.jircas.go.jp/ja/event/2024/eventlist.json"

# データ取得
response = requests.get(URL)
data = response.json()

# イベントデータのリストを取り出す（"list"キーに格納されている）
events = data.get("list", [])

# 上位5件だけ表示
print("【JIRCASイベント情報 2024年】\n")
for event in events[:5]:
    title = event.get("title", "タイトル不明")
    date = event.get("date", "日付不明")
    path = event.get("path", "#")
    print(f"イベント名：{title}")
    print(f"開催日：{date}")
    print(f"詳細URL：https://www.jircas.go.jp{path}")
    print("-" * 40)
