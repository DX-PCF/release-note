
# Title: April 22, 2026 
Link: https://docs.cloud.google.com/release-notes#April_22_2026<br>
Google Cloudインフラエンジニアとして、ご依頼のリリースノートを基に、構築済みのサービスへの影響調査結果をご報告いたします。

## BigQuery

### Announcement
原文: Dataproc is now called Managed Service for Apache Spark. The names for associated API, client
library, CLI, and Identity and Access Management (IAM) resources remain unchanged.
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview)
説明：
Dataprocのサービス名称が「Managed Service for Apache Spark」に変更されました。これに伴うAPI、クライアントライブラリ、CLI、IAMリソースの名称には変更はありません。
影響有無：
影響なし。これは名称変更のみのアナウンスであり、既存のワークロードや設定に直接的な変更は必要ありません。API名やリソース名に変更がないため、既存のコードやスクリプトへの影響もありません。
対処方法：
なし。変更された名称を認識しておくのみで問題ありません。
用語説明：
*   **Dataproc / Managed Service for Apache Spark**: Apache Spark、Hadoopなどのオープンソースのデータ処理フレームワークをマネージドサービスとして提供するGoogle Cloudのサービス。名称変更により、Sparkに特化したマネージドサービスであることを強調しています。
*   **API (Application Programming Interface)**: プログラムが他のソフトウェアと対話するためのインターフェースの集合です。
*   **CLI (Command Line Interface)**: コマンドラインからサービスを操作するためのツールです。
*   **IAM (Identity and Access Management)**: Google Cloudリソースへのアクセス権限を管理するためのサービスです。

### Announcement
原文: BigLake is now called Google Cloud Lakehouse.
BigLake metastore is now called the Lakehouse runtime
catalog. The names for associated APIs, client
libraries, CLI commands, and Identity and Access Management (IAM) remain
unchanged and still reference BigLake.
[Google Cloud Lakehouse](https://docs.cloud.google.com/biglake/docs/introduction)
[Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/about-blms)
説明：
BigLakeのサービス名称が「Google Cloud Lakehouse」に、BigLake metastoreが「Lakehouse runtime catalog」に変更されました。関連するAPI、クライアントライブラリ、CLI、IAMリソースの名称は変更されず、引き続き「BigLake」を参照します。
影響有無：
影響なし。これは名称変更のみのアナウンスであり、既存のデータレイクハウス環境の利用方法や構成に直接的な変更は必要ありません。API名などに変更がないため、既存のコードやスクリプトへの影響もありません。
対処方法：
なし。変更された名称を認識しておくのみで問題ありません。
用語説明：
*   **BigLake / Google Cloud Lakehouse**: BigQueryやCloud Storageなどのデータソースを統合し、統一されたアクセスとガバナンスを提供するGoogle Cloudのデータレイクハウスプラットフォームです。
*   **BigLake metastore / Lakehouse runtime catalog**: Google Cloud Lakehouseにおいて、Cloud Storageなどに格納されたデータに対するスキーマ情報などのメタデータを管理するコンポーネントです。

### Announcement
原文: Dataplex Universal Catalog is now called Knowledge
Catalog. The API, client library, CLI, and
Identity and Access Management (IAM) names remain unchanged. For more
information, see Knowledge Catalog overview.
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction)
[Knowledge Catalog overview](https://docs.cloud.google.com/dataplex/docs/introduction)
説明：
Dataplex Universal Catalogの名称が「Knowledge Catalog」に変更されました。API、クライアントライブラリ、CLI、IAMリソースの名称は変更されません。
影響有無：
影響なし。これは名称変更のみのアナウンスであり、既存のデータカタログの利用方法や構成に直接的な変更は必要ありません。API名などに変更がないため、既存のコードやスクリプトへの影響もありません。
対処方法：
なし。変更された名称を認識しておくのみで問題ありません。
用語説明：
*   **Dataplex Universal Catalog / Knowledge Catalog**: Google Cloud Dataplexのコンポーネントで、組織全体の様々なデータソースのメタデータを一元的に管理し、検索可能にするデータカタログ機能です。

### Announcement
原文: Looker Studio is now called Data Studio.
The website and endpoint change from `lookerstudio.google.com` to
`datastudio.google.com`. You do not need to update your reports for this change,
as Data Studio automatically redirects to the new domain. However,
if your company uses proxies to restrict access to external sites, your IT
administrator needs to add the new domain to your access control list (ACL).
The names for associated API, client library, CLI, and Identity and Access
Management (IAM) resources remain unchanged. For more information, see Data Studio returns as new home for Data Cloud
assets.
[Data Studio](https://docs.cloud.google.com/data-studio)
[Data Studio returns as new home for Data Cloud assets](https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio)
説明：
Looker Studioのサービス名称が「Data Studio」に変更されました。それに伴い、ウェブサイトおよびエンドポイントのドメインが `lookerstudio.google.com` から `datastudio.google.com` に変更されます。既存のレポートの更新は不要で、新しいドメインに自動的にリダイレクトされます。ただし、企業内でプロキシを用いて外部サイトへのアクセスを制限している場合、IT管理者は新しいドメインをアクセス制御リスト（ACL）に追加する必要があります。API、クライアントライブラリ、CLI、IAMリソースの名称は変更されません。
影響有無：
軽微な影響あり。
*   既存のレポートは自動的に新しいドメインにリダイレクトされるため、機能的な影響は基本的にありません。
*   社内のネットワーク設定（プロキシ、ファイアウォールなど）で外部ドメインのアクセス制限を実施している場合、新しいドメイン `datastudio.google.com` を許可リストに追加する作業が必要になります。
対処方法：
*   社内ネットワークでプロキシやファイアウォールによる外部サイトへのアクセス制限を行っている場合は、IT部門に連絡し、`datastudio.google.com` をアクセス制御リスト（ACL）に追加するよう依頼してください。
用語説明：
*   **Looker Studio / Data Studio**: Googleが提供する無料のデータ可視化およびレポート作成ツールです。様々なデータソースに接続し、インタラクティブなダッシュボードやレポートを作成できます。
*   **ACL (Access Control List)**: ネットワークやシステムにおいて、特定のユーザーやグループが特定のリソースに対してどのようなアクセス権を持つかを定義するリストです。

## Google Kubernetes Engine

### Change
原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
説明：
GKEクラスターの新しいバージョンが、新規クラスターの作成、および既存クラスターのコントロールプレーンとノードの手動アップグレードで利用可能になりました。
影響有無：
間接的な影響あり。
*   現在ご利用のGoogle Cloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3) はGKE上に構築されています。Composerはマネージドサービスであり、基盤となるGKEクラスターのバージョンアップはGoogle Cloudによって管理されます。
*   GKEのバージョンアップは、通常、新機能の追加、パフォーマンスの向上、セキュリティ修正を含みます。そのため、基盤の安定性とセキュリティが向上する点でプラスの影響があります。
*   Composerの自動アップグレード機能が有効になっている場合、Google Cloudが互換性を考慮しつつ、これらの新しいGKEバージョン範囲内で基盤クラスターのバージョンアップを自動的に行います。
対処方法：
*   直接的な対応は不要ですが、Composer環境のアップグレードポリシー（自動アップグレードチャネルの選択など）が適切に設定されていることを確認してください。
*   GKEのバージョンアップに起因するComposerの挙動変更がないか、Composerのリリースノートや互換性マトリックスを定期的に確認することが推奨されます。

### Security
原文: This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:
(以下、GKEバージョンとCOSバージョンの対応表とリンク)
説明：
このリリースには、セキュリティ修正を含む更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらのCOSイメージには、前回のGKEリリース以降にリリースされたすべてのCOSバージョンからのセキュリティ修正が累積的に適用されています。
影響有無：
プラスの影響あり。
*   GKEクラスターの基盤となるOS（Container-Optimized OS）にセキュリティ修正が適用されるため、既存のGKEクラスターおよびComposer2環境のセキュリティ体制が向上します。
*   GKEの自動アップグレードが有効な場合、これらのセキュリティ修正を含むバージョンに自動的に更新されます。
対処方法：
*   GKEクラスターの自動アップグレードが有効になっていることを確認し、これらのセキュリティ修正が適切に適用されるようにしてください。
*   手動アップグレード運用の場合、セキュリティ向上のため、アップグレード計画にこれらのバージョンを含めることを検討してください。
用語説明：
*   **Container-Optimized OS (COS)**: Google Cloudでコンテナワークロードを実行するために最適化されたGoogle製のLinuxベースのオペレーティングシステムです。セキュリティ、信頼性、パフォーマンスに優れています。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
There are no new releases in the Stable channel.
説明：
新しいGKEバージョンが、リリースノート公開時点ですべてのGoogle Cloudゾーンで利用可能になっているとは限らず、展開には数日かかる場合があるという注意喚起です。また、Stableチャネルには新しいリリースはありません。
影響有無：
軽微な影響あり。
*   新しいGKEバージョンへのアップグレードを検討している場合、現時点ではそのバージョンが利用可能でない可能性があります。
*   Composer2環境でGKEのStableチャネルが利用されている場合、今回の更新では基盤のGKEバージョンに新しい変更はありません。
対処方法：
*   特定のGKEバージョンへのアップグレードが必要な場合は、GKEコンソールや`gcloud`コマンドで利用可能なバージョンを確認してから実行してください。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Regular channel:
- 1.32.13-gke.1258000
- 1.33.10-gke.1115000
- 1.34.6-gke.1154000
- 1.35.3-gke.1234000
(リンクは省略)
説明：
新しいGKEバージョンが、リリースノート公開時点ですべてのGoogle Cloudゾーンで利用可能になっているとは限らず、展開には数日かかる場合があるという注意喚起です。以下のGKEバージョンがRegularチャネルで利用可能になりました。
影響有無：
間接的な影響あり。
*   GKEクラスターがRegularチャネルを利用している場合、これらの新しいバージョンに順次自動アップグレードされる可能性があります。
*   Composer2環境の基盤GKEがRegularチャネルを利用している場合、GKEのバージョンがこれらの新しいバージョンに更新される可能性があります。
対処方法：
*   Regularチャネルを利用しているGKEクラスター、またはComposer2環境の基盤GKEがRegularチャネルを利用している場合、これらのバージョンへのアップグレードが予定されることを認識しておいてください。
*   Composerのアップグレードポリシーにおいて、テスト環境で互換性確認を行うことが推奨されます。
用語説明：
*   **Regular channel**: GKEのアップグレードチャネルの一つで、新機能と安定性のバランスが取れたバージョンが提供されます。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Rapid channel:
- 1.32.13-gke.1362000
- 1.33.11-gke.1013000
- 1.34.6-gke.1307000
- 1.35.3-gke.1522000
(リンクは省略)
説明：
新しいGKEバージョンが、リリースノート公開時点ですべてのGoogle Cloudゾーンで利用可能になっているとは限らず、展開には数日かかる場合があるという注意喚起です。以下のGKEバージョンがRapidチャネルで利用可能になりました。
影響有無：
間接的な影響あり。
*   GKEクラスターがRapidチャネルを利用している場合、これらの新しいバージョンに順次自動アップグレードされる可能性があります。
*   Composer2環境の基盤GKEがRapidチャネルを利用している場合、GKEのバージョンがこれらの新しいバージョンに更新される可能性があります。
対処方法：
*   Rapidチャネルを利用しているGKEクラスター、またはComposer2環境の基盤GKEがRapidチャネルを利用している場合、これらのバージョンへのアップグレードが予定されることを認識しておいてください。
*   Rapidチャネルは最も早く新バージョンが提供されるため、本番環境での利用にはより慎重なテストと検証が必要です。Composerのアップグレードポリシーにおいて、テスト環境で互換性確認を綿密に行うことが推奨されます。
用語説明：
*   **Rapid channel**: GKEのアップグレードチャネルの一つで、最新の機能や修正が最も早く提供されます。

### Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- The following versions are now available:
- 1.32.13-gke.1362000
- 1.33.11-gke.1013000
- 1.34.6-gke.1307000
- 1.35.3-gke.1522000
- The following node versions are now available:
-
# Title: April 20, 2026 
Link: https://docs.cloud.google.com/release-notes#April_20_2026<br>
はい、Google Cloudのリリースノートに基づき、各製品への影響調査と回答を以下にまとめます。

---

# AlloyDB for PostgreSQL

## Issue
**原文:** `ChatGPT users aren't able to list or use the AlloyDB toolset provided by the AlloyDB remote MCP server.`

**説明:**
このリリースノートは、AlloyDB for PostgreSQLとChatGPTの連携に関する既知の問題をアナウンスしています。具体的には、ChatGPTのユーザーが、AlloyDBのリモートMCP (Multi-Cloud Platform) サーバーが提供するAlloyDBのツールセットを一覧表示したり、利用したりできないという問題が発生していることを示しています。これは、AlloyDBとChatGPTの特定の連携機能が期待通りに動作しないことを意味します。

**影響有無:**
**限定的な影響**

*   **影響を受ける可能性のある利用者:** AlloyDB for PostgreSQLを利用しており、かつAlloyDBのツールセットをChatGPTを介して（例えば、ChatGPTプラグインやChatGPTを組み込んだアプリケーションなど）利用しているユーザーのみが影響を受けます。
*   **影響を受けない利用者:** 通常のAlloyDBユーザーや、ChatGPTとの連携を行っていないユーザー、あるいはChatGPT経由でAlloyDBツールセットを利用するユースケースがないユーザーには直接的な影響はありません。現在のところ、多くのAlloyDB利用者がこの連携を利用している可能性は低いため、影響は限定的と判断されます。

**対処方法:**
*   もし、AlloyDBとChatGPTの連携を通じてツールセットを利用している場合、現状ではこの機能は正常に動作しません。Google Cloudからの公式な修正アナウンスを待つ必要があります。
*   当面の間、AlloyDBのツールセットを利用する際は、ChatGPTを介さずに、直接的な管理コンソール、`gcloud` CLI、またはアプリケーションからアクセス・操作することを検討してください。

**用語説明:**
*   **AlloyDB for PostgreSQL:** Google Cloudが提供する、フルマネージドでPostgreSQL互換の高性能なリレーショナルデータベースサービスです。
*   **ChatGPT:** OpenAIが開発した大規模言語モデル（LLM）で、対話形式で自然言語処理を行うことができます。
*   **MCP Server (Multi-Cloud Platform Server):** この文脈では、AlloyDBが外部サービス（ここではChatGPT）と連携するために提供する、バックエンドのコンポーネントまたはサービスエンドポイントの一部を指している可能性があります。
*   **AlloyDB toolset:** AlloyDBインスタンスの管理、監視、操作に使用される一連のツールや機能群を指します。

---

# BigQuery

## Change
**原文:** `Starting July 25, 2026, the BigQuery Data Transfer Service for Facebook Ads connector will update the data type mapping for the ActionValue field in the AdInsightsActions report from INT to FLOAT.`

**[BigQuery Data Transfer Service for Facebook Ads connector](https://cloud.google.com/bigquery/docs/facebook-ads-transfer)**

**説明:**
このリリースノートは、BigQuery Data Transfer Serviceにおける将来の変更をアナウンスしています。2026年7月25日より、BigQuery Data Transfer ServiceのFacebook広告コネクタを使用して転送される`AdInsightsActions`レポート内の`ActionValue`フィールドのデータ型が、現在の`INT`（整数）から`FLOAT`（浮動小数点数）に変更されます。これはデータ型の仕様変更であり、ダウンストリームでのデータ利用に影響を与える可能性があります。

**影響有無:**
**中程度の潜在的影響（ただし、実施までに時間的猶予あり）**

*   **影響を受ける利用者:**
    *   BigQuery Data Transfer Serviceを利用してFacebook広告のデータをBigQueryに転送しており、特に`AdInsightsActions`レポートの`ActionValue`フィールドを利用しているユーザー。
    *   このフィールドを基にした既存のBigQueryクエリ、ビュー、テーブルスキーマ定義、またはBigQueryからデータを取り込むダウンストリームのシステム（例: BIツール、データウェアハウス、データ分析アプリケーション、ETL/ELTパイプラインなど）は影響を受ける可能性があります。
*   **具体的な影響:**
    *   `INT`から`FLOAT`への変更は、一般的に数値の表現範囲が広がり、小数点以下の値も扱えるようになるため、データ損失のリスクは低いですが、以下の点に注意が必要です。
        *   **スキーマ変更:** BigQueryテーブルのスキーマは自動的に更新される可能性がありますが、もし明示的にスキーマを定義している場合は確認が必要です。
        *   **クエリの動作:** `ActionValue`フィールドに対する既存のクエリ（特に型キャスト、比較演算、集計関数）は、結果の精度や動作に微細な影響を与える可能性があります。
        *   **ダウンストリームシステムへの影響:** 浮動小数点数を扱えない、または厳密な整数型を期待しているシステムでは、データ取り込みエラーや計算結果の差異が発生する可能性があります。
        *   **パフォーマンス:** データ型の変更がパフォーマンスに与える影響は通常小さいですが、大規模なデータセットで頻繁に利用される場合は監視が必要です。

**対処方法:**
この変更は2026年7月25日と、約2年間の猶予があります。以下の対応を計画的に実施してください。

1.  **影響範囲の特定:** 現在、BigQuery Data Transfer Service for Facebook Adsコネクタを利用しているか、および`AdInsightsActions`レポートの`ActionValue`フィールドがどこでどのように利用されているかを特定します。
2.  **ダウンストリームシステムの評価:** `ActionValue`フィールドを参照している全てのBigQueryクエリ、ビュー、およびBigQueryからデータを取り込むBIツール、ETL/ELTパイプライン、アプリケーションなどで、データ型変更によって影響を受ける可能性がある箇所を洗い出します。
3.  **改修計画の立案:** 2026年7月25日までに、上記で特定された影響箇所に対して、`FLOAT`型への変更に対応するための改修計画（例: クエリの修正、スキーマの調整、ダウンストリームシステムのデータ型対応）を立案します。
4.  **テスト環境での検証:** 変更が適用される前に、テスト環境で変更をシミュレートし、既存のデータ処理が正常に機能するかどうかを十分に検証することを強く推奨します。
5.  **公式ドキュメントの確認:** BigQuery Data Transfer Service for Facebook Adsコネクタの公式ドキュメント（上記リンク）や関連するリリースノートを定期的に確認し、追加情報がないか注意を払ってください。

**用語説明:**
*   **BigQuery Data Transfer Service:** Google Cloudが提供するフルマネージドなサービスで、SaaSアプリケーション（Salesforce, Google Adsなど）やその他のデータソースからBigQueryへデータを自動的にロードします。
*   **Facebook Ads connector:** BigQuery Data Transfer Serviceの一機能で、Facebook広告プラットフォームのデータをBigQueryに定期的に自動転送するためのコネクタです。
*   **`AdInsightsActions` report:** Facebook広告のパフォーマンスレポートの一つで、広告に対するアクション（クリック、コンバージョンなど）に関する詳細なインサイトを提供します。
*   **`ActionValue` field:** `AdInsightsActions`レポート内の特定のフィールドで、アクションに関連する数値（例: コンバージョン値、単価など）を表します。
*   **`INT` (Integer):** 整数値を格納するためのデータ型です。
*   **`FLOAT` (Floating-point number):** 浮動小数点数（小数点以下の値を含む数値）を格納するためのデータ型です。

---

# Cloud Logging

## Libraries
## Go
**原文:** `[v1.16.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.15.0...logging/v1.16.0)`

**説明:**
このリリースノートは、Google Cloud LoggingのGoクライアントライブラリがバージョンv1.16.0に更新されたことを示しています。提供されたリンクは、GitHub上で前バージョンv1.15.0からの変更差分を示しており、どのような修正や機能追加、改善が行われたかを確認できます。通常、ライブラリのバージョンアップは、バグ修正、パフォーマンス改善、新機能のサポート、セキュリティアップデートなどが含まれます。

**影響有無:**
**限定的な影響（Go言語でCloud Logging APIを利用している場合のみ）**

*   **影響を受ける利用者:** Go言語でアプリケーションを開発しており、その中でGoogle Cloud LoggingのGoクライアントライブラリを利用してログをCloud Loggingに送信したり、Cloud Logging APIを操作したりしている場合に影響があります。
*   **Google Cloud Composer:** Google Cloud Composerは主にPythonベースであるため（AirflowもPythonで記述されています）、Cloud LoggingのGoクライアントライブラリの更新は直接的な影響を与えません。
*   **一般的なライブラリ更新の影響:**
    *   **非破壊的変更の場合:** 既存のコードに影響なく、バグ修正やパフォーマンス改善の恩恵を受けられる可能性があります。
    *   **破壊的変更 (Breaking Change) の場合:** 非常に稀ですが、もし破壊的変更が含まれている場合は、コードの修正が必要になる可能性があります。リリースノートのリンク先で変更ログを確認することが重要です。

**対処方法:**
1.  **利用状況の確認:** 自社のGo言語で開発されたアプリケーションで、Google Cloud LoggingのGoクライアントライブラリが使用されているか、またそのバージョンを確認します。
2.  **変更ログの確認:** 提供されたGitHubのリンク（`https://github.com/googleapis/google-cloud-go/compare/logging/v1.15.0...logging/v1.16.0`）を参照し、v1.16.0での具体的な変更点（バグ修正、新機能、パフォーマンス改善、そして特に破壊的変更の有無）を確認します。
3.  **バージョンアップの検討:** 新しいバージョンにすることで、セキュリティの向上、バグ修正、パフォーマンス改善などの恩恵が受けられる可能性があります。必要に応じて、アプリケーションの依存関係をv1.16.0に更新することを検討してください。
4.  **テストとデプロイ:** バージョンアップを行う際は、必ず開発環境やステージング環境で十分にテストを実施し、既存機能への影響がないことを確認してから本番環境にデプロイしてください。

**用語説明:**
*   **Cloud Logging:** Google Cloudが提供するフルマネージドなロギングサービスで、Google Cloudリソースやアプリケーションからのログを収集、保存、分析、モニタリングします。
*   **Go:** Googleによって開発されたオープンソースのプログラミング言語です。
*   **Client Library:** プログラミング言語ごとに提供されるSDK（Software Development Kit）の一部で、特定のGoogle CloudサービスのAPIと容易にやり取りできるように設計されたコードの集まりです。開発者はこれらのライブラリを使用することで、APIリクエストの詳細を意識することなくサービスを利用できます。