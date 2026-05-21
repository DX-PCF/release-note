import pandas as pd
import os
import re

# Google Cloud CLI リリースノートと設計書(a.txt)を照合し、
# ファイルごとにヒット件数をカウントするスクリプト

# Google Cloud CLI リリースノートと設計書(a.txt)を照合するスクリプト

def extract_tokens_from_file(file_path):
    """
    ファイルからコマンドとフラグを抽出する関数
    """
    tokens = set()
    if not os.path.exists(file_path):
        return tokens

    # 文字コードは UTF-8 を優先し、失敗した場合は Shift-JIS (CP932) で読み込む
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='cp932') as f:
            lines = f.readlines()

    for line in lines:
        # 1. gcloudコマンド部分の抽出
        # "gcloud" ＋ スペース ＋ 英小文字/数字/ハイフンの繰り返しを検索
        match = re.search(r'gcloud\s+([a-z0-9\s-]+)', line, re.IGNORECASE)
        if match:
            raw_cmd_body = match.group(1).strip()
            # 単語ごとに分解して、プレースホルダーや日本語が出てくるまでをコマンドとする
            parts = re.split(r'\s+', raw_cmd_body)
            clean_parts = ["gcloud"]
            for p in parts:
                # フラグ（--）が出てきたらコマンド（位置引数）部分は終了
                if p.startswith('--'):
                    break
                # 英小文字、数字、ハイフン以外の文字（日本語や記号）が含まれたら終了
                if not re.match(r'^[a-z0-9-]+$', p, re.IGNORECASE):
                    break
                clean_parts.append(p)
            
            # gcloud単体ではなく、サブコマンド等が含まれる場合のみ追加
            if len(clean_parts) > 1:
                tokens.add(" ".join(clean_parts))

        # 2. オプションフラグ（--xxx）の抽出
        # -- で始まり、その後に英小文字/数字/ハイフンが続くものをすべて拾う
        flags = re.findall(r'--[a-z0-9-]+', line, re.IGNORECASE)
        for f in flags:
            tokens.add(f)
            
    return tokens

def main():
    # 入出力ファイル名の設定
    target_csv = "release_notes_v3 small.csv"
    input_command_files = ["a.txt"]
    output_csv = "release_notes_impacted.csv"
    
    # リリースノート本文が含まれるカラム名
    content_col = '内容'
    
    # 処理対象CSVの読み込み
    try:
        # Excel対応のため UTF-8 BOM付き (utf-8-sig) を優先
        df = pd.read_csv(target_csv, encoding='utf-8-sig')
    except UnicodeDecodeError:
        # 失敗した場合は CP932 (Shift-JIS) で読み込む
        df = pd.read_csv(target_csv, encoding='cp932')

    if content_col not in df.columns:
        print(f"Error: {content_col} not found")
        return

    # 各コマンド定義ファイル（a.txtなど）をループ処理
    for cmd_file in input_command_files:
        print(f"Processing: {cmd_file}")
        
        # ファイルから検索キーワード（コマンド/フラグ）を抽出
        pure_tokens = extract_tokens_from_file(cmd_file)
        
        if not pure_tokens:
            print(f"No tokens found in {cmd_file}")
            df[cmd_file] = 0
            continue

        print(f"Tokens: {sorted(list(pure_tokens))}")

        # 各行に対してヒット件数をカウントする
        def count_matches(text):
            if pd.isna(text): return 0
            text_str = str(text)
            count = 0
            for token in pure_tokens:
                # 正規表現でキーワードが含まれているか検索
                if re.search(re.escape(token), text_str, re.IGNORECASE):
                    count += 1
            return count

        # ファイル名を列名として追加し、カウント結果を格納
        df[cmd_file] = df[content_col].apply(count_matches)

    # 結果をBOM付きUTF-8で保存
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"Saved: {output_csv}")

if __name__ == "__main__":
    main()
