import requests
from bs4 import BeautifulSoup
import csv
import re

def version_to_tuple(version_str):
    """バージョン文字列を比較可能なタプルに変換 (例: '565.0.0' -> (565, 0, 0))"""
    match = re.search(r'(\d+)\.(\d+)\.(\d+)', version_str)
    if match:
        return tuple(map(int, match.groups()))
    return (0, 0, 0)

def classify_content(service_name, content):
    """内容から分類を判定する（先頭動詞重視版）"""
    content_clean = content.strip()
    if not content_clean:
        return "その他"
    
    # 最初の単語を取得
    first_word = content_clean.split()[0].rstrip('.,:;()').lower()
    content_lower = content_clean.lower()
    service_lower = service_name.lower()
    
    # 1. 破壊的変更（カテゴリ名最優先）
    if "breaking changes" in service_lower:
        return "破壊的変更"
    
    # 2. 先頭動詞による判定（最優先のヒューリスティック）
    if first_word in ["fixed", "resolved", "fix", "rebuilt", "rebuilding", "resolved"]:
        return "修正"
    
    if first_word in ["promoted", "promote", "promoting", "promotes"]:
        if "ga" in content_lower or "general availability" in content_lower:
            return "GA昇格"
        if any(kw in content_lower for kw in ["beta", "preview", "alpha"]):
            return "ベータ/プレビュー昇格"
        return "GA昇格"  # デフォルトはGA昇格として扱う
        
    if first_word in ["added", "add", "new", "introduced", "introduces", "available", "support", "supports", "newly"]:
        return "新機能/追加"
        
    if first_word in ["updated", "update", "updates", "improved", "modified", "changed", "renamed", "set", "default", "migrated", "upgraded", "made"]:
        return "変更/改善"
        
    if first_word in ["deprecated", "removed", "deleted", "deprecation", "removal"]:
        return "非推奨/削除"

    # 3. 先頭動詞で判定できなかった場合のキーワード判定（フォールバック）
    if "promoted" in content_lower and (" ga" in content_lower or "general availability" in content_lower):
        return "GA昇格"
    if "promoted" in content_lower and any(kw in content_lower for kw in ["beta", "preview", "alpha"]):
        return "ベータ/プレビュー昇格"
    if any(re.search(rf"\b{kw}\b", content_lower) for kw in ["added", "introduced", "available", "support"]):
        return "新機能/追加"
    if any(re.search(rf"\b{kw}\b", content_lower) for kw in ["fixed", "resolved", "bug"]):
        return "修正"
    if any(re.search(rf"\b{kw}\b", content_lower) for kw in ["deprecated", "removed", "deleted"]):
        return "非推奨/削除"
    if any(re.search(rf"\b{kw}\b", content_lower) for kw in ["updated", "improved", "modified", "changed", "renamed", "set"]):
        return "変更/改善"
    
    return "その他"

def fetch_and_export():
    url = "https://docs.cloud.google.com/sdk/docs/release-notes"
    print(f"URLからデータを取得中: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"データの取得に失敗しました: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    min_version = (408, 0, 0)
    results = []
    
    h2_tags = soup.find_all('h2')
    
    for h2 in h2_tags:
        version_text = h2.get_text(strip=True)
        version_num_match = re.search(r'(\d+\.\d+\.\d+)', version_text)
        if not version_num_match: continue
            
        version_str = version_num_match.group(1)
        if version_to_tuple(version_str) < min_version: continue
            
        current_service = "General"
        node = h2.find_next_sibling()
        
        while node and node.name != 'h2':
            if node.name == 'h3':
                current_service = node.get_text(strip=True)
            elif node.name == 'ul':
                for li in node.find_all('li', recursive=False):
                    # separator=" " を指定してタグ間のテキストが結合されないようにする
                    content = li.get_text(separator=" ", strip=True)
                    # 連続する空白を1つにまとめる
                    content = re.sub(r'\s+', ' ', content)
                    
                    classification = classify_content(current_service, content)
                    results.append([current_service, version_str, classification, content])
            node = node.find_next_sibling()

    filename = 'release_notes_v3.csv'
    try:
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['サービス名', 'バージョン', '分類', '内容'])
            writer.writerows(results)
        print(f"成功: {len(results)} 件のレコードを {filename} に出力しました（先頭動詞重視）。")
    except Exception as e:
        print(f"CSVの書き込みに失敗しました: {e}")

if __name__ == "__main__":
    fetch_and_export()
