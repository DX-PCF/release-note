`gcloud` コマンドの `--format` と `--filter` オプションを使いこなすための実践的なチートシートです。

---

## 1. `--format` （出力形式の指定）

出力フォーマットの切り替えや、特定フィールドの抽出・整形を行います。

### よく使うフォーマット形式

| フォーマット | 説明 | コマンド例 |
| --- | --- | --- |
| **table** | 表形式（デフォルト） | `--format="table(name, zone, status)"` |
| **json** | JSON形式（プログラミング・スクリプト用） | `--format="json"` |
| **yaml** | YAML形式 | `--format="yaml"` |
| **csv** | CSV形式（ヘッダー付き） | `--format="csv(name, networkInterfaces[0].networkIP)"` |
| **value** | 特定フィールドの値のみ抽出（シェルスクリプト用） | `--format="value(name)"` |
| **text** | キー: 値のリスト形式 | `--format="text"` |

### `--format` のよく使う構文パターン

* **特定の属性だけを表にする（列名のカスタマイズ）**
```bash
gcloud compute instances list \
  --format="table(name:label=NAME, status:label=STATUS, zone.basename():label=ZONE)"

```


* **配列データの先頭要素を取得する**
```bash
gcloud compute instances list \
  --format="value(networkInterfaces[0].networkIP)"

```


* **ネストしたJSONフィールドを展開して取得**
```bash
gcloud container clusters list \
  --format="table(name, currentNodeCount, nodeConfig.machineType)"

```


* **スライス機能（末尾の文字列だけ抽出）**
```bash
# URLパスの最後の要素（ゾーン名など）だけを取得する
gcloud compute instances list \
  --format="value(zone.basename())"

```



---

## 2. `--filter` （データの絞り込み）

クライアント側ではなく、**Google Cloudのサーバー側で検索・フィルタリング**を行って結果を絞り込みます。

### 演算子一覧

| 種類 | 演算子 | 意味 | 例 |
| --- | --- | --- | --- |
| **一致 / 不一致** | `=`, `!=` | 完全一致 / 不一致 | `status=RUNNING` |
| **部分一致** | `:` | 〜を含む（前方/部分一致） | `name:web` |
| **正規表現** | `~` | 正規表現にマッチ | `name~'^prod-.*'` |
| **正規表現不一致** | `!~` | 正規表現にマッチしない | `name!~'test'` |
| **比較** | `<`, `>`, `<=`, `>=` | 数値・日付の比較 | `creationTimestamp < 2026-01-01` |
| **否定** | `NOT` / `-` | 条件の反転 | `NOT status=TERMINATED` |

### `--filter` の実践例

* **単一の条件で絞り込む**
```bash
# 稼働中のVMインスタンスのみ取得
gcloud compute instances list --filter="status=RUNNING"

```


* **複数条件（AND / OR）**
```bash
# asia-northeast1 ゾーンで、かつ RUNNING 状態のインスタンス
gcloud compute instances list \
  --filter="zone:asia-northeast1 AND status=RUNNING"

# 名前に 'web' または 'app' を含むインスタンス
gcloud compute instances list \
  --filter="name:web OR name:app"

```


* **否定（NOT）**
```bash
# 停止中（TERMINATED）以外のインスタンス
gcloud compute instances list --filter="NOT status=TERMINATED"

```


* **キー・バリュー（ラベル）での絞り込み**
```bash
# env=production ラベルが付与されているリソース
gcloud compute instances list --filter="labels.env=production"

```


* **日付での絞り込み**
```bash
# 2026年1月1日以降に作成されたリソース
gcloud compute instances list --filter="creationTimestamp >= 2026-01-01"

```



---

## 3. `--filter` と `--format` の組み合わせ例

実際の運用やスクリプト作成でよく使われる組み合わせ例です。

### 停止中のVMインスタンスの「名前」一覧を取得する（シェルスクリプト用）

```bash
gcloud compute instances list \
  --filter="status=TERMINATED" \
  --format="value(name)"

```

### 外部IPアドレスを持っているVMインスタンスだけを抽出して表形式で出力する

```bash
gcloud compute instances list \
  --filter="networkInterfaces[].accessConfigs[].natIP:*" \
  --format="table(name, zone.basename(), networkInterfaces[0].accessConfigs[0].natIP:label=EXTERNAL_IP)"

```
シェルスクリプトや運用自動化でそのまま使える、`gcloud` の `--filter` / `--format` を活用した実用ワンライナー集です。

---

## 1. 資源の特定と一括操作（ループ・削除）

### 停止中の Compute Engine (VM) の名前一覧を取得して一括削除する

```bash
gcloud compute instances list \
  --filter="status=TERMINATED" \
  --format="value(name)" \
  | xargs -r gcloud compute instances delete --quiet --zone=asia-northeast1-a

```

### 特定ラベルが付いたリソース（例: env=test）をまとめて停止する

```bash
gcloud compute instances list \
  --filter="labels.env=test AND status=RUNNING" \
  --format="value(name, zone.basename())" \
  | while read -r name zone; do
      gcloud compute instances stop "$name" --zone="$zone" --quiet
    done

```

---

## 2. ネットワーク・IPアドレスの抽出

### 外部IPアドレスを持つ全VMの「名前 / 内部IP / 外部IP」をCSV出力する

```bash
gcloud compute instances list \
  --filter="networkInterfaces[].accessConfigs[].natIP:*" \
  --format="csv[no-heading](name, networkInterfaces[0].networkIP, networkInterfaces[0].accessConfigs[0].natIP)"

```

### 未使用（Unattached）の静的外部IPアドレス一覧を取得する

```bash
gcloud compute addresses list \
  --filter="status=RESERVED AND NOT users:*" \
  --format="value(name, address, region.basename())"

```

---

## 3. セキュリティ・IAM・権限の監査

### 指定した権限（例: storage.admin）を持つユーザー/サービスアカウントを抽出する

```bash
gcloud projects get-iam-policy $(gcloud config get-value project) \
  --flatten="bindings[].members" \
  --filter="bindings.role:roles/storage.admin" \
  --format="value(bindings.members)"

```

### 有効化されているサービスアカウントのキー（鍵）一覧と作成日を取得する

```bash
gcloud iam service-accounts keys list \
  --iam-account="MY_SA@$(gcloud config get-value project).iam.gserviceaccount.com" \
  --filter="keyType=USER_MANAGED" \
  --format="table(name.basename():label=KEY_ID, validAfterTime:label=CREATED_AT)"

```

---

## 4. コスト削減・不要リソースの監査

### どのVMにもアタッチされていない「孤立したPersistent Disk」を探す

```bash
gcloud compute disks list \
  --filter="NOT users:*" \
  --format="table(name, sizeGb, zone.basename(), creationTimestamp)"

```

### 30日以上前に作成された古くなったバックアップ（スナップショット）を取得する

```bash
gcloud compute snapshots list \
  --filter="creationTimestamp < 2026-09-21" \
  --format="value(name)"

```

---



# gcloud config configurations チートシート

Google Cloud CLI（`gcloud`）の「構成（Configuration）」は、アカウント、プロジェクト、デフォルトのリージョンやゾーンなどの設定一式に名前を付けて管理する仕組みです。本チートシートでは、環境切り替え（本番/検証/開発）や複数アカウント運用に必須となるコマンドと活用Tipsを整理しています。

---

## 1. コマンドクイックリファレンス

| 操作 | コマンド | 概要 |
| :--- | :--- | :--- |
| **一覧表示** | `gcloud config configurations list` | 既存の構成一覧と現在のアクティブ構成を表示 |
| **新規作成** | `gcloud config configurations create <NAME>` | 新しい構成を作成（作成時に自動アクティブ化） |
| **切り替え** | `gcloud config configurations activate <NAME>` | 指定した構成を有効化 |
| **詳細確認** | `gcloud config configurations describe <NAME>` | 指定した構成の設定プロパティ一覧を表示 |
| **名前変更** | `gcloud config configurations rename <OLD> <NEW>` | 既存の構成名を変更 |
| **削除** | `gcloud config configurations delete <NAME>` | 指定した構成を削除（非アクティブ状態のみ可） |

---

## 2. コマンド詳細と実用例

### 2.1 構成の一覧表示 (`list`)
登録されているすべての構成名、アクティブ状態、関連付けられているアカウント・プロジェクト情報を一覧表示します。

```bash
# 基本の一覧表示
gcloud config configurations list

# テーブル出力のフィルタリング（例: 特定アカウントの構成のみ）
gcloud config configurations list --filter="account:user@example.com"

# アクティブな構成名のみを抽出取得
gcloud config configurations list --filter="is_active=true" --format="value(name)"
```

### 2.2 構成の新規作成 (`create`)
新しい空の構成を作成します。作成が完了すると、自動的にその構成がアクティブになります。

```bash
# 新しい構成を作成（例: pj-prod）
gcloud config configurations create pj-prod

# プロンプトを出さずに作成
gcloud config configurations create pj-dev --quiet
```

### 2.3 構成の有効化・切り替え (`activate`)
作業対象の環境を切り替えます。

```bash
# 指定した構成に切り替え
gcloud config configurations activate pj-prod
```

### 2.4 構成の詳細確認 (`describe`)
特定構成に保存されているプロパティ（`core/project`, `compute/region` など）を確認します。現在アクティブでない構成の内容も参照可能です。

```bash
# 指定した構成の設定値を表示
gcloud config configurations describe pj-prod

# YAML形式で出力（デフォルト）
gcloud config configurations describe pj-prod --format="yaml"
```

### 2.5 構成の名前変更 (`rename`)
既存の構成の識別名を変更します。

```bash
# 古い構成名を新しい名前に変更
gcloud config configurations rename old-name new-name
```

### 2.6 構成の削除 (`delete`)
不要になった構成を削除します。

```bash
# 構成の削除
gcloud config configurations delete old-config

# 複数構成の一括削除
gcloud config configurations delete config-a config-b

# 確認プロンプトをスキップして削除
gcloud config configurations delete old-config --quiet
```

> **注意:** 現在**アクティブになっている構成は直接削除できません**。一度別の構成に `activate` してから削除を実行してください。

---

## 3. 実践ワークフロー：新しい環境セットアップ

新しいプロジェクト環境（例: `my-staging`）を作成し、初期設定を完了させる標準的な流れです。

```bash
# ステップ 1: 新規構成を作成（自動的にアクティブ化されます）
gcloud config configurations create my-staging

# ステップ 2: 認証アカウントを設定（既存ログイン済みアカウントまたは新規ログイン）
gcloud config set account your-name@example.com
# ※ 未ログインの場合は認証を実行: gcloud auth login

# ステップ 3: プロジェクトIDを設定
gcloud config set project my-staging-project-id

# ステップ 4: デフォルトのリージョンとゾーンを設定
gcloud config set compute/region asia-northeast1
gcloud config set compute/zone asia-northeast1-a

# ステップ 5: 設定内容の確認
gcloud config list
```

---

## 4. 応用テクニック・一時的な切り替え

### 4.1 コマンド単発での構成指定 (`--configuration` フラグ)
現在のセッションのアクティブ構成を変更することなく、特定のコマンドだけ別の構成で実行します。

```bash
# アクティブ構成を変更せず、prod環境のComputeインスタンス一覧を取得
gcloud compute instances list --configuration=pj-prod

# 特定の構成のアカウント情報でCloud Storageを確認
gcloud storage ls --configuration=pj-dev
```

### 4.2 ターミナルセッション限定の切り替え (`CLOUDSDK_ACTIVE_CONFIG_NAME`)
環境変数 `CLOUDSDK_ACTIVE_CONFIG_NAME` を設定すると、該当ターミナルウィンドウ内でのみ有効な構成を上書きできます。

```bash
# 現在のシェルセッションのみ構成を固定
export CLOUDSDK_ACTIVE_CONFIG_NAME=pj-prod

# 設定解除（デフォルトのアクティブ構成に戻す）
unset CLOUDSDK_ACTIVE_CONFIG_NAME
```

### 4.3 ディレクトリ連携（`direnv` との組み合わせ）
プロジェクトごとのルートディレクトリに `.envrc` を配置することで、ディレクトリ移動時に自動で `gcloud` の構成を切り替えられます。

```bash
# 対象リポジトリのルートで実行
echo "export CLOUDSDK_ACTIVE_CONFIG_NAME=pj-prod" >> .envrc
direnv allow
```

---

## 5. 現在の状態を確認する補助コマンド

| コマンド | 用途 |
| :--- | :--- |
| `gcloud config list` | 現在有効な構成に設定されている全プロパティを表示 |
| `gcloud config get-value project` | 現在アクティブな構成のプロジェクトIDのみを取得 |
| `gcloud info` | 現在の構成名、SDKのインストール先、設定ファイルのパスなどを包括的に表示 |
| `gcloud auth list` | 認証済みアカウント一覧とアクティブなアカウントを表示 |

---

## 6. 設定ファイルの保存場所と内部仕様

- **設定ファイルの実体パス:**
  - Linux / macOS: `~/.config/gcloud/configurations/config_<NAME>`
  - Windows: `%APPDATA%\gcloud\configurations\config_<NAME>`
- **フォーマット:** INI形式のプレーンテキストファイルとして保存されており、セクション（`[core]`, `[compute]` 等）ごとにキーと値が記録されています。
