import pandas as pd
import os
import re

# Google Cloud CLI リリースノートと設計書(a.txt)を照合し、
# ファイルごとにヒット件数をカウントするスクリプト

def extract_token_groups_from_file(file_path):
    """
    ファイルからコマンドとフラグのグループを抽出する関数
    戻り値: list of list (各サブリスト内の全要素がヒットした場合に1カウント)
    """
    token_groups = []
    if not os.path.exists(file_path):
        return token_groups

    # 文字コードは UTF-8 を優先し、失敗した場合は Shift-JIS (CP932) で読み込む
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='cp932') as f:
            lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        current_cmd = None
        # 1. コマンド部分の抽出 (gcloud, gsutil, bq)
        cmd_match = re.search(r'\b(gcloud|gsutil|bq)\s+([a-z0-9\s-]+)', line, re.IGNORECASE)
        if cmd_match:
            base_cmd = cmd_match.group(1).lower()
            raw_cmd_body = cmd_match.group(2).strip()
            parts = re.split(r'\s+', raw_cmd_body)
            clean_parts = [base_cmd]
            for p in parts:
                if p.startswith('-'): break
                if not re.match(r'^[a-z0-9-]+$', p, re.IGNORECASE): break
                clean_parts.append(p)
            current_cmd = " ".join(clean_parts)
            # コマンド単体でのヒットも登録
            token_groups.append([current_cmd])

        # 2. オプションフラグ（--xxx または -x）の抽出
        flags = re.findall(r'(?:\s|^)(--[a-z0-9-]+|-[a-z0-9])', line, re.IGNORECASE)
        for f in flags:
            flag = f.strip()
            if current_cmd:
                # コマンドがある場合は、コマンドとセットで登録
                token_groups.append([current_cmd, flag])
            else:
                # コマンドがない場合は、フラグ単体で登録
                token_groups.append([flag])
            
    # 重複の削除
    unique_groups = []
    seen = set()
    for g in token_groups:
        t = tuple(sorted(g))
        if t not in seen:
            seen.add(t)
            unique_groups.append(g)
            
    return unique_groups

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
        
        # ファイルから検索パターンのグループを抽出
        token_groups = extract_token_groups_from_file(cmd_file)
        
        if not token_groups:
            print(f"No tokens found in {cmd_file}")
            df[cmd_file] = 0
            continue

        print(f"Patterns: {token_groups}")

        # 各行に対してヒット件数をカウントする
        def count_matches(text):
            if pd.isna(text): return 0
            text_str = str(text)
            count = 0
            for group in token_groups:
                # グループ内のすべての要素がテキストに含まれているかチェック
                if all(re.search(re.escape(token), text_str, re.IGNORECASE) for token in group):
                    count += 1
            return count

        # ファイル名を列名として追加し、カウント結果を格納
        df[cmd_file] = df[content_col].apply(count_matches)

    # 結果をBOM付きUTF-8で保存
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"Saved: {output_csv}")

if __name__ == "__main__":
    main()
