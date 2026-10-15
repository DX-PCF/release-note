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
