
# Title: April 22, 2026 
Link: https://docs.cloud.google.com/release-notes#April_22_2026<br>
# BigQuery

## Announcement

### 原文
Dataproc is now called Managed Service for Apache Spark. The names for associated API, client
library, CLI, and Identity and Access Management (IAM) resources remain unchanged.

[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview)

### 説明
これまで「Dataproc」と呼ばれていたサービスが、「Managed Service for Apache Spark」に名称変更されました。これに伴い、関連するAPI、クライアントライブラリ、CLIコマンド、およびIdentity and Access Management (IAM) リソースの名称に変更はありません。これは主にブランド名の変更であり、既存の機能や操作に変更はありません。

### 影響有無
**影響なし**
既存のワークロードやAPI、CLI、IAM設定に対する直接的な影響はありません。名称変更のみであり、技術的な動作や設定には変更がないためです。

### 対処方法
特段の技術的な対処は不要です。しかし、内部のドキュメント、運用手順書、開発者向けの資料などで「Dataproc」の記述がある場合は、「Managed Service for Apache Spark」への更新を推奨します。

### 用語説明
*   **Managed Service for Apache Spark**: Google Cloud上でApache Sparkワークロードを実行するための、フルマネージドなサービス。

---

## Announcement

### 原文
BigLake is now called Google Cloud Lakehouse.
BigLake metastore is now called the Lakehouse runtime
catalog. The names for associated APIs, client
libraries, CLI commands, and Identity and Access Management (IAM) remain
unchanged and still reference BigLake.

[Google Cloud Lakehouse](https://docs.cloud.google.com/biglake/docs/introduction)
[Lakehouse runtime
catalog](https://docs.cloud.google.com/biglake/docs/about-blms)

### 説明
これまで「BigLake」と呼ばれていたサービスが「Google Cloud Lakehouse」に名称変更され、さらに「BigLake metastore」は「Lakehouse runtime catalog」に名称変更されました。これに伴い、関連するAPI、クライアントライブラリ、CLIコマンド、およびIdentity and Access Management (IAM) リソースの名称に変更はなく、引き続き「BigLake」を参照します。

### 影響有無
**影響なし**
既存のワークロードやAPI、CLI、IAM設定に対する直接的な影響はありません。これはブランド名の変更であり、既存の機能やAPIの参照方法には変更がないためです。

### 対処方法
特段の技術的な対処は不要です。内部ドキュメント、運用手順書、開発者向け資料などで「BigLake」や「BigLake metastore」の記述がある場合は、「Google Cloud Lakehouse」や「Lakehouse runtime catalog」への更新を推奨します。

### 用語説明
*   **Google Cloud Lakehouse**: BigQueryを基盤としたデータレイクとデータウェアハウスの統合プラットフォーム。オープンフォーマットとオープンソースエンジンをサポートし、BigQuery、Spark、Prestoなどから単一のカタログを介してデータにアクセスできる。
*   **Lakehouse runtime catalog**: Google Cloud Lakehouse内でデータセットのメタデータを管理し、各種分析エンジンから利用可能にするカタログサービス。

---

## Announcement

### 原文
Dataplex Universal Catalog is now called Knowledge
Catalog. The API, client library, CLI, and
Identity and Access Management (IAM) names remain unchanged. For more
information, see Knowledge Catalog overview.

[Knowledge
Catalog](https://docs.cloud.google.com/dataplex/docs/introduction)
[Knowledge Catalog overview](https://docs.cloud.com/dataplex/docs/introduction)

### 説明
これまで「Dataplex Universal Catalog」と呼ばれていたサービスが、「Knowledge Catalog」に名称変更されました。これに伴い、関連するAPI、クライアントライブラリ、CLIコマンド、およびIdentity and Access Management (IAM) リソースの名称に変更はありません。

### 影響有無
**影響なし**
既存のワークロードやAPI、CLI、IAM設定に対する直接的な影響はありません。これはブランド名の変更であり、技術的な動作や設定に変更がないためです。

### 対処方法
特段の技術的な対処は不要です。内部ドキュメント、運用手順書、開発者向け資料などで「Dataplex Universal Catalog」の記述がある場合は、「Knowledge Catalog」への更新を推奨します。

### 用語説明
*   **Knowledge Catalog**: Google Cloud Dataplexの一部として提供される、データアセットのメタデータを統合管理するカタログサービス。データディスカバリ、ガバナンス、ライフサイクル管理をサポートする。

---

## Announcement

### 原文
Looker Studio is now called Data Studio.
The website and endpoint change from `lookerstudio.google.com` to
`datastudio.google.com`. You do not need to update your reports for this change,
as Data Studio automatically redirects to the new domain. However,
if your company uses proxies to restrict access to external sites, your IT
administrator needs to add the new domain to your access control list (ACL).
The names for associated API, client library, CLI, and Identity and Access
Management (IAM) resources remain unchanged. For more information, see Data Studio returns as new home for Data Cloud
assets.

[Data Studio](https://docs.cloud.google.com/data-studio)
[Data Studio returns as new home for Data Cloud
assets](https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio)

### 説明
これまで「Looker Studio」と呼ばれていたサービスが、「Data Studio」に名称変更されました。これに伴い、ウェブサイトおよびエンドポイントのドメインが `lookerstudio.google.com` から `datastudio.google.com` に変更されます。既存のレポートは自動的に新しいドメインにリダイレクトされるため、レポートの更新は不要です。関連するAPI、クライアントライブラリ、CLIコマンド、およびIdentity and Access Management (IAM) リソースの名称に変更はありません。

### 影響有無
**一部影響あり**
*   **レポート利用者:** 既存のレポートは自動的に新しいドメインにリダイレクトされるため、レポートの閲覧や操作には直接的な影響はありません。
*   **企業ネットワーク管理者:** 企業内でプロキシやファイアウォールを使用して外部サイトへのアクセスを制限している場合、新しいドメイン (`datastudio.google.com`) へのアクセスを許可するようにACL (Access Control List) の設定変更が必要になる可能性があります。

### 対処方法
*   **ネットワーク管理者向け:** 企業ネットワークでプロキシやファイアウォールを使用している場合は、`datastudio.google.com` へのHTTPS (ポート443) アクセスを許可するようにACLまたはファイアウォールルールを見直し、必要に応じて追加・更新してください。
*   **内部ドキュメントの更新:** 内部で利用している手順書やガイド、トレーニング資料などで「Looker Studio」の記述がある場合は、「Data Studio」への更新を推奨します。

### 用語説明
*   **Data Studio (旧 Looker Studio)**: Google Cloudの無料のレポートおよびデータ可視化ツール。様々なデータソースに接続し、インタラクティブなダッシュボードやレポートを作成できる。
*   **ACL (Access Control List)**: ネットワーク機器やOSなどで、特定のリソースへのアクセスを許可または拒否するためのルールリスト。
# Title: April 20, 2026 
Link: https://docs.cloud.google.com/release-notes#April_20_2026<br>
はい、Google Cloudのリリースノートに基づき、各製品の変更点とお客様のサービスへの影響を調査し、ご回答いたします。

---

# AlloyDB for PostgreSQL

## Issue

原文: `ChatGPT users aren't able to list or use the AlloyDB toolset provided by the AlloyDB remote MCP server.`

説明：
AlloyDB for PostgreSQLにおいて、ChatGPTユーザーがAlloyDBの遠隔MCP (Multi-Cluster PrimaryまたはManagement Plane) サーバーが提供する特定のツールセットを一覧表示したり、使用したりできないという問題が報告されています。これは、ChatGPTとAlloyDBの間の連携機能に関する既知の問題です。

影響有無：
**影響あり。**
もしお客様のサービスで、ChatGPTを介してAlloyDBの特定の管理ツールやユーティリティを利用している場合、これらの機能が一時的に利用できないという直接的な影響があります。AlloyDBサービスそのものの稼働には影響はありませんが、特定の連携シナリオにおけるオペレーションに支障をきたす可能性があります。

対処方法：
現時点では、Google Cloudからの公式な修正パッチや回避策の提供を待つ必要があります。このリリースノートでは具体的な対処方法は示されていません。
もし緊急で当該ツールセットの機能が必要な場合は、ChatGPTを介さずに、AlloyDBの標準的な管理ツールやAPIを直接利用するなどの代替手段を検討してください。

用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、PostgreSQL互換のフルマネージドなエンタープライズ向けデータベースサービスです。高いパフォーマンス、可用性、セキュリティが特徴です。
*   **ChatGPT**: OpenAIによって開発された大規模言語モデルであり、自然言語処理に基づく対話システムです。
*   **AlloyDB toolset**: AlloyDBインスタンスの管理、監視、データ操作などを行うための各種ツールやユーティリティの総称です。
*   **MCP server**: 文脈から「Multi-Cluster Primary server」または「Management Plane server」など、AlloyDBの管理や運用をサポートするバックエンドサーバーの一部を指す可能性があります。

---

# BigQuery

## Change

原文: `Starting July 25, 2026, the BigQuery Data Transfer Service for Facebook Ads connector will update the data type mapping for the ActionValue field in the AdInsightsActions report from INT to FLOAT.`
[BigQuery Data Transfer Service for Facebook Ads connector](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer)

説明：
BigQuery Data Transfer ServiceのFacebook Adsコネクタにおいて、2026年7月25日から、`AdInsightsActions`レポート内の`ActionValue`フィールドのデータ型マッピングが変更されます。現在の`INT`（整数）型から`FLOAT`（浮動小数点数）型へ更新される予定です。

影響有無：
**影響あり。**
お客様のサービスでBigQuery Data Transfer Serviceを利用してFacebook Adsからデータを転送しており、特に`AdInsightsActions`レポートの`ActionValue`フィールドをBigQuery内で利用している場合に影響します。
この変更は、当該フィールドを`INT`型として処理している既存のETL/ELTパイプライン、BigQueryビュー、BIダッシュボード、およびBigQueryからデータを読み込むアプリケーションにデータ型不一致によるエラーや予期せぬ挙動を引き起こす可能性があります。
変更日時はかなり先ですが、計画的な対応が必要となるBreaking Changeです。

対処方法：
2026年7月25日までに、以下の対応を計画的に実施してください。
1.  **影響範囲の特定**: `AdInsightsActions`レポートの`ActionValue`フィールドを参照している全てのBigQueryジョブ、ビュー、BIレポート、および関連するアプリケーションを特定します。
2.  **データ型処理の変更**: 特定した全てのコンポーネントにおいて、`ActionValue`フィールドのデータ型が`FLOAT`に変わることを前提とした処理に修正します。現在`INT`型であることを前提とした型変換、集計関数、比較演算などを見直してください。
3.  **テスト**: 変更を適用する前に、十分なテスト環境で動作検証を行い、データの一貫性や処理の正確性を確認してください。
4.  **ドキュメント更新**: 内部ドキュメントやデータ辞書を更新し、新しいデータ型情報を反映させてください。

用語説明：
*   **BigQuery Data Transfer Service**: Google Cloud BigQueryに、外部データソース（SaaSアプリケーション、データウェアハウスなど）からデータを自動的かつ定期的に転送するためのフルマネージドサービスです。
*   **Facebook Ads connector**: BigQuery Data Transfer Serviceの一種で、Facebook広告プラットフォームから広告キャンペーンのデータやパフォーマンスレポートをBigQueryに自動転送するコネクタです。
*   **AdInsightsActions report**: Facebook広告のレポートの一つで、広告に対するユーザーのアクション（例: クリック、購入、アプリインストールなど）に関する詳細な情報を提供するものです。
*   **ActionValue**: `AdInsightsActions`レポート内の特定のフィールドで、アクションに関連する数値データを示します。
*   **INT**: 整数型（Integer）。
*   **FLOAT**: 浮動小数点数型（Floating-point number）。

---

# Cloud Logging

## Libraries

原文: `[v1.16.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.15.0...logging/v1.16.0)`

説明：
Google Cloud LoggingのGo言語クライアントライブラリが、バージョンv1.15.0からv1.16.0へ更新されたことを示します。提供されているリンクは、GitHubでの前バージョンとの差分を示すもので、通常、バグ修正、パフォーマンス改善、または後方互換性を維持した機能追加などが含まれています。

影響有無：
**直接的なサービスへの影響なし。**
この変更は、お客様がGo言語でCloud Logging APIを利用するアプリケーションを開発・運用している場合にのみ関連します。既存のGoアプリケーションがv1.15.0以前のCloud Loggingライブラリに依存している場合、このリリースノート自体が直ちに影響を与えるものではありません。
しかし、今後ライブラリのバージョンアップを計画する際には、この新しいバージョンを検討する対象となります。一般的に、マイナーバージョンアップでは後方互換性が保たれることが多いですが、念のため差分を確認することが推奨されます。

対処方法：
Go言語でCloud Loggingを利用しているアプリケーションがある場合、以下の対応を検討してください。
1.  **差分確認**: 提供されているGitHubの差分リンク (`https://github.com/googleapis/google-cloud-go/compare/logging/v1.15.0...logging/v1.16.0`) を確認し、v1.16.0に含まれる変更内容（特に非互換性のある変更や、既存コードに影響を与える可能性のある変更）がないか確認します。
2.  **アップグレードの検討**: 新機能の利用やバグ修正の恩恵を受けるために、`go.mod`ファイルを更新してCloud Loggingクライアントライブラリをv1.16.0にアップグレードすることを検討します。
3.  **テスト**: アップグレードを行う際は、開発・テスト環境で十分な動作検証を行い、アプリケーションの安定性に影響がないことを確認してください。

用語説明：
*   **Cloud Logging**: Google Cloudが提供するフルマネージドなログ管理サービス。様々なGoogle Cloudサービスやカスタムアプリケーションからのログを収集、保存、分析、監視できます。
*   **Go**: Googleが開発した、シンプルさ、信頼性、効率性を重視したオープンソースのプログラミング言語です。
*   **Client Library (クライアントライブラリ)**: プログラミング言語（この場合はGo）からGoogle Cloudの各サービスのAPIを容易に呼び出せるようにするためのSDK（Software Development Kit）の一部です。APIとのやり取りを抽象化し、開発を簡素化します。
*   **v1.16.0**: ソフトウェアのバージョン番号。通常「メジャー.マイナー.パッチ」の形式で表され、マイナーバージョン（この場合は16）の更新は、後方互換性を維持しつつ新機能の追加や改善が行われたことを示します（セマンティックバージョニングに従っている場合）。

---