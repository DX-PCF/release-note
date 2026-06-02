## 2. パラメータ対応表

同じ設定項目を同じ行に配置し、それぞれの指定方法、説明、およびデフォルト値をマッピングしています。

| 項目名 / パラメータ論理名 | gcloud CLI 引数・フラグ | Terraform 引数（`google_scc_mute_config`） | 必須 / 任意 | デフォルト値 (gcloud / Terraform) | 説明・仕様 |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **ミュート設定ID** | `CONFIG_ID`<br>*(位置引数)* | `mute_config_id` | **必須** | - / - | ミュート設定の一意の識別子。親リソース（プロジェクト等）内で一意である必要があります。半角英数字とハイフン（`-`）を使用し、1〜63文字で構成します。 |
| **親リソース（適用スコープ）** | `--parent=PARENT_ID` | `parent` | **必須** | - / - | ミュート設定を適用するリソースの階層構造パス。以下のいずれかの形式で指定します。<br>・`projects/{project_id}`<br>・`folders/{folder_id}`<br>・`organizations/{organization_id}` |
| **フィルター条件** | `--filter="FILTER"` | `filter` | **必須** | - / - | 自動ミュートの対象とする検出結果（Findings）を絞り込むためのクエリ式。<br>例: `category="OPEN_FIREWALL" AND severity="LOW"` |
| **説明** | `--description="TEXT"` | `description` | 任意 | `null` / `null` | ミュート設定に関する説明文（管理用のメモなど）。最大1,024文字まで入力可能。 |
| **ミュートタイプ** | `--type=MUTE_TYPE` | `type` | 任意 | **`STATIC`** / **`DYNAMIC`**<br>*(※差異あり、詳細は後述)* | ミュート状態の更新挙動を指定します。<br>・`STATIC`: 設定作成時に一致した検出結果のみがミュートされ、その後の状態変更は追従しません。<br>・`DYNAMIC`: 検出結果の新規発生やアップデート時に、フィルター条件に合致するかどうかで自動追従（動的適用）します。<br>・その他の値: `MUTE_CONFIG_TYPE_UNSPECIFIED` |
| **有効期限** | `--expiry-time=TIMESTAMP` | `expiry_time` | 任意 | `null` / `null` | ミュート設定の有効期限（`DYNAMIC`タイプのみ指定可能）。RFC3339 UTC 形式（例: `2215-02-03T15:01:23Z`）で指定します。期限が切れると、該当する検出結果のミュートが自動的に解除されます。 |
| **データ保管ロケーション** | `--location=LOCATION` | *(未サポート)*<br>*(※詳細は後述)* | gcloudは**必須**<br>*(デフォルト値あり)* | **`global`** / - | SCCのロケーション（データレジデンシー）を指定します。通常は `global` ですが、データ所在地の規制がある場合は `us`、`eu` などのリージョンを指定します。 |

---

## 3. 設計・実装上の重要ポイント（注意書き）

> [!IMPORTANT]
> **1. ミュートタイプ（type）のデフォルト値の食い違いに注意**
> *   **gcloud CLI**: 指定しない場合、デフォルトで **`STATIC`** になります。
> *   **Terraform**: 指定しない場合、デフォルトで **`DYNAMIC`** になります。
> *   **影響**: 両者で挙動を統一したい場合は、省略せずに必ず明示的に `type = "DYNAMIC"` または `"STATIC"` と記述することを推奨します。

> [!NOTE]
> **2. Terraformにおけるロケーション（location）の扱いについて**
> *   Terraformの標準リソース `google_scc_mute_config` (v1 API準拠) は、グローバルまたは親リソース直下に作成されるため、`location` 引数を持ちません。
> *   SCC v2 API（マルチリージョンデータレジデンシー対応等）を利用して特定のロケーションに制限したい場合は、Terraformでは `google_scc_v2_organization_mute_config` や `google_scc_v2_project_mute_config` などの **v2専用リソース** を使用する必要があります。

---

## 4. 参考：自動生成・出力（Computed）パラメータ

Terraform実行後、または `gcloud scc muteconfigs describe` 実行時にAPIから返却される「読み取り専用」のパラメータ一覧です。

| gcloud CLI レスポンス属性 | Terraform 属性名 | 説明 |
| :--- | :--- | :--- |
| `name` | `id` / `name` | ミュート設定のフルリソース名（フォーマット: `organizations/{org}/muteConfigs/{id}` など） |
| `createTime` | `create_time` | ミュート設定が作成された時間（RFC3339形式のタイムスタンプ） |
| `updateTime` | `update_time` | ミュート設定が最後に更新された時間 |
| `mostRecentEditor` | `most_recent_editor` | ミュート設定を最後に作成・更新したユーザー（またはサービスアカウント）のメールアドレス |

---

## 5. 実装・適用例（コードスニペット）

パラメータシートを元にした、全く同じ設定内容となる `gcloud` コマンドと `Terraform` 定義の対比サンプルです。

### 設定要件
*   **ID:** `custom-high-severity-mute`
*   **適用対象:** プロジェクト `my-awesome-project-id`
*   **フィルター:** 重要度（Severity）が `LOW` の脆弱性（Vulnerability）を自動ミュート
*   **タイプ:** 動的適用（`DYNAMIC`）

### A. gcloud CLI コマンド例
```bash
gcloud scc muteconfigs create "custom-high-severity-mute" \
    --parent="projects/my-awesome-project-id" \
    --location="global" \
    --filter="severity=\"LOW\" AND class=\"VULNERABILITY\"" \
    --description="Low severity vulnerabilities are automatically muted" \
    --type="DYNAMIC"
```

### B. Terraform HCL 定義例
```hcl
# Terraform Google Provider 6.26.0
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.26.0"
    }
  }
}

resource "google_scc_mute_config" "low_severity_mute" {
  mute_config_id = "custom-high-severity-mute"
  parent         = "projects/my-awesome-project-id"
  filter         = "severity=\"LOW\" AND class=\"VULNERABILITY\""
  description    = "Low severity vulnerabilities are automatically muted"
  type           = "DYNAMIC"
}
```

---

このテンプレートをそのままExcel、Markdown設計書、Confluence、またはスプレッドシートにコピーしてご活用ください。
=========================================
Terraformコードのモジュール化を前提とし、パラメータ情報を **YAMLファイル** で一元管理・分離するエンタープライズ向けの構成（設計・コードテンプレート）を作成しました。

この構成を採用することで、インフラエンジニア以外のメンバーでもYAMLファイルを編集するだけで安全にミュート設定を追加・変更できるようになります。

---

## 1. ディレクトリ構成
推奨されるファイル配置です。再利用可能な子モジュール（`modules/scc_mute_config`）と、環境ごとの設定を行うルートモジュールに分離しています。

```text
.
├── main.tf                    # ルートモジュール（YAMLロードとモジュール呼び出し）
├── scc_mute_configs.yaml      # パラメータ管理YAMLファイル（本体）
└── modules/
    └── scc_mute_config/       # 子モジュール（カプセル化されたリソース定義）
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

---

## 2. YAMLパラメータ定義ファイル (`scc_mute_configs.yaml`)
ミュート設定一覧を配列で定義します。プロジェクト単位だけでなく、組織（Organization）やフォルダ単位の設定、`STATIC` と `DYNAMIC` の使い分けなども直感的に記述可能です。

```yaml
# Security Command Center ミュート設定パラメータ定義
mute_configs:
  # 例1: プロジェクト単位の動的ミュート（推奨される一般的な構成）
  - mute_config_id: "proj-low-severity-vuln-mute"
    parent: "projects/my-awesome-project-id"
    filter: "severity = \"LOW\" AND class = \"VULNERABILITY\""
    description: "Low severity vulnerabilities are automatically muted for security noise reduction."
    type: "DYNAMIC"
    expiry_time: null # 無期限

  # 例2: 組織（Organization）単位での静的ミュート（一時的なミュートなどに利用）
  - mute_config_id: "org-noisy-service-account-mute"
    parent: "organizations/123456789012"
    filter: "category = \"UNUSED_SERVICE_ACCOUNT\""
    description: "Mute unused service account alerts at organization level"
    type: "STATIC"
    expiry_time: null

  # 例3: 有効期限付きの動的ミュート（特定の検証用プロジェクト等）
  - mute_config_id: "proj-temp-validation-mute"
    parent: "projects/sandbox-project-123"
    filter: "resource.name : \"sandbox-vms\""
    description: "Temporary mute for validation VMs until expiration date"
    type: "DYNAMIC"
    expiry_time: "2026-12-31T23:59:59Z" # RFC3339 形式
```

---

## 3. ルートモジュール実装

### `main.tf`
YAMLファイルを `yamldecode` で解析し、`for_each` でループを回してモジュールを呼び出します。これにより、YAMLにレコードを追加するだけで自動的にリソースがプロビジョニングされます。

```hcl
# 1. YAMLファイルを読み込み、Terraform内のローカル変数に格納
locals {
  yaml_raw_data = yamldecode(file("${path.module}/scc_mute_configs.yaml"))

  # 重複排除とループ用のMapオブジェクトへ変換（キーを mute_config_id に設定）
  mute_configs_map = {
    for config in local.yaml_raw_data.mute_configs : config.mute_config_id => config
  }
}

# 2. 子モジュールをループで呼び出し
module "scc_mute_configs" {
  source   = "./modules/scc_mute_config"
  for_each = local.mute_configs_map

  mute_config_id = each.value.mute_config_id
  parent         = each.value.parent
  filter         = each.value.filter
  description    = lookup(each.value, "description", null)
  type           = lookup(each.value, "type", "DYNAMIC")     # デフォルトは DYNAMIC
  expiry_time    = lookup(each.value, "expiry_time", null)   # 未指定またはnullの場合は無視される
}
```

---

## 4. 子モジュール（再利用部品）の実装

### `modules/scc_mute_config/main.tf`
GCPリソースの定義実体です。この中で、パラメータの型変換やリソース作成ロジックを担保します。

```hcl
resource "google_scc_mute_config" "this" {
  mute_config_id = var.mute_config_id
  parent         = var.parent
  filter         = var.filter
  description    = var.description
  type           = var.type
  expiry_time    = var.expiry_time
}
```

### `modules/scc_mute_config/variables.tf`
モジュールのインターフェース（変数定義）です。型制約（`validation`など）を追加することで、YAML側の記述誤りをデプロイ前にキャッチできます。

```hcl
variable "mute_config_id" {
  type        = string
  description = "Security Command Center内のミュート設定の一意なID"
}

variable "parent" {
  type        = string
  description = "ミュート設定を紐付けるリソースのパス (organizations/X, folders/X, projects/X)"
}

variable "filter" {
  type        = string
  description = "ミュート対象を判定するSCCのクエリ式"
}

variable "description" {
  type        = string
  default     = null
  description = "ミュート設定の説明文"
}

variable "type" {
  type        = string
  default     = "DYNAMIC"
  description = "ミュート挙動タイプ (STATIC もしくは DYNAMIC)"

  validation {
    condition     = contains(["STATIC", "DYNAMIC", "MUTE_CONFIG_TYPE_UNSPECIFIED"], var.type)
    error_message = "typeパラメータは 'STATIC', 'DYNAMIC' のいずれかである必要があります。"
  }
}

variable "expiry_time" {
  type        = string
  default     = null
  description = "ミュート設定の有効期限を表すタイムスタンプ (RFC3339 形式、例: 2026-12-31T23:59:59Z)"
}
```

### `modules/scc_mute_config/outputs.tf`
呼び出し元のルートモジュール（あるいはCI/CDパイプライン）で結果を確認するための出力定義です。

```hcl
output "id" {
  value       = google_scc_mute_config.this.id
  description = "作成されたミュート設定のID"
}

output "name" {
  value       = google_scc_mute_config.this.name
  description = "作成されたミュート設定のフルリソース名"
}

output "create_time" {
  value       = google_scc_mute_config.this.create_time
  description = "ミュート設定の作成日時"
}
```

---

## 5. この設計のメリット
1. **設定（YAML）と実装（Terraform）の完全な分離:**
   ユーザーや運用担当者はTerraformの文法（HCL）を深く知らなくても、`scc_mute_configs.yaml` を変更するだけでルールの追加・削除が行えます。
2. **安全性の向上 (`validation` ブロック):**
   子モジュール側の `variables.tf` で `type` に不適切な値（例: タイポした `DYNAMIK` など）が入った場合、Terraformの実行前ステージ（`plan`）で即座にエラーになり安全にガードされます。
3. **拡張性（DRY原則の準拠）:**
   親（`parent`）がプロジェクトだったり、組織だったりする複数の設定群を、単一のコードブロック（`for_each`）で美しく効率的に処理できます。

Searched web: ""google_scc_v2_project_mute_config" terraform"
Searched web: ""google_scc_v2_project_mute_config" site:registry.terraform.io/providers/hashicorp/google"
Searched web: ""google_scc_v2_project_mute_config" terraform "Arguments Reference""
Searched web: ""google_scc_v2_project_mute_config" terraform parent format"
Searched web: ""google_scc_v2_project_mute_config" terraform "type""
Searched web: ""google_scc_v2_project_mute_config" terraform "expiry_time""
Searched web: ""google_scc_v2_project_mute_config" terraform expiry_time"
Searched web: "site:github.com/hashicorp/terraform-provider-google "google_scc_v2_project_mute_config""
Searched web: ""google_scc_v2_project_mute_config" site:registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_project_mute_config"
Searched web: "site:registry.terraform.io/providers/hashicorp/google "google_scc_v2_project_mute_config" "parent""

はい、**`google_scc_mute_config`（v1/レガシーAPI準拠）**から、最新の**`google_scc_v2_project_mute_config`（v2 API準拠）**に変更する場合、**いくつかの重要な仕様変更とそれに伴うコードの修正が発生します。**

以下に、具体的な変更点と、先ほど作成したYAMLおよびモジュール構成に対する修正内容を整理しました。

---

## 1. 主な仕様変更点（v1 vs v2）

もっとも大きな違いは、**「リソースの単一化（v1）」から「適用階層ごとのリソース分離（v2）」**への移行と、**「データ所在ロケーション（Location）の明示的指定」**です。

| 項目 | 変更前（v1: `google_scc_mute_config`） | 変更後（v2: `google_scc_v2_project_mute_config`） |
| :--- | :--- | :--- |
| **リソース名** | `google_scc_mute_config` | `google_scc_v2_project_mute_config` |
| **適用範囲 (Scope)** | 組織、フォルダ、プロジェクト全てを単一リソースでカバー可能。 | **プロジェクト専用**リソース。<br>※組織（`organizations`）は `google_scc_v2_organization_mute_config`、フォルダ（`folders`）は `google_scc_v2_folder_mute_config` と別リソースになります。 |
| **`parent` のフォーマット** | `projects/{project_id}` | `projects/{project_id}/locations/{location}` <br>*(例: `projects/my-project/locations/global`)* |
| **ロケーション指定** | サポートなし（グローバル暗黙） | **必須**（親リソースのパスの一部としてロケーションを指定します。通常は `global`） |

---

## 2. これまでに作成した資料（構成・コード）への具体的な影響と修正内容

モジュール化とYAML設計を導入しているため、影響箇所は局所化されますが、以下の修正が必要です。

### ① YAMLパラメータファイル (`scc_mute_configs.yaml`) の修正
`parent` の書き方を **ロケーション（`locations/global` など）を含む形式**にアップデートする必要があります。

```yaml
# scc_mute_configs.yaml
mute_configs:
  # 変更前 (v1): "projects/my-awesome-project-id"
  # 変更後 (v2): 末尾に "/locations/global" を追加
  - mute_config_id: "proj-low-severity-vuln-mute"
    parent: "projects/my-awesome-project-id/locations/global"
    filter: "severity = \"LOW\" AND class = \"VULNERABILITY\""
    description: "Low severity vulnerabilities are automatically muted for security noise reduction."
    type: "DYNAMIC"
    expiry_time: null

  # 【注意】組織（organizations）宛ての設定
  # google_scc_v2_project_mute_config は「プロジェクト専用」のため、組織用のレコードは
  # このモジュールのループから除外するか、組織用別モジュールに分離する必要があります。
```

---

### ② 子モジュール (`modules/scc_mute_config/main.tf`) の修正
リソースブロックの宣言を **v2プロジェクト用** に書き換えます。

```hcl
# modules/scc_mute_config/main.tf

# 変更後: v2 リソース名に修正
resource "google_scc_v2_project_mute_config" "this" {
  mute_config_id = var.mute_config_id
  parent         = var.parent  # 入力される値は "projects/.../locations/..."
  filter         = var.filter
  description    = var.description
  type           = var.type
  expiry_time    = var.expiry_time
}
```

---

### ③ 子モジュール変数定義 (`modules/scc_mute_config/variables.tf`) の修正
`parent` 変数の説明（`description`）や、必要であれば値のバリデーション定義（正規表現による `/locations/` の確認）を修正します。

```hcl
# modules/scc_mute_config/variables.tf

variable "parent" {
  type        = string
  description = "ミュート設定を紐付けるプロジェクトパス。フォーマット: projects/{project_id}/locations/{location_id}"

  # 簡易的なフォーマットチェックを追加可能（オプション）
  validation {
    condition     = can(regex("^projects/[a-z0-9-]+/locations/[a-z0-9-]+$", var.parent))
    error_message = "parentは 'projects/{project_id}/locations/{location_id}' の形式で指定する必要があります。"
  }
}
```

---

## 3. まとめ：変更が発生する理由と設計上のメリット

> [!IMPORTANT]
> **移行の最大のポイント**
> `google_scc_v2_project_mute_config` に切り替えることで、これまでの汎用的なモジュールから **「プロジェクトレベル専用のミュート設定モジュール」** に役割が明確化（特化）されます。

もしプロジェクトだけでなく、**組織（Organization）レベル**や**フォルダ（Folder）レベル**でのミュート設定もYAMLで一元管理したい場合は、ルートモジュール（`main.tf`）側で、YAMLから読み込んだデータの `parent` プレフィックス（`projects/`、`organizations/`、`folders/`）に応じて呼び出すモジュールを分岐させる（または、YAMLの配列をスコープごとに分ける）設計へのアップデートを設計を追加設計することで、美しく拡張が対応が最も美しい設計にアップデートすると、さらに美しいアーキテクチャになります。

====
