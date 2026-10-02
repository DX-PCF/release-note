
# Title: October 01, 2026 
Link: https://docs.cloud.google.com/release-notes#October_01_2026<br>
Google Cloudのインフラエンジニアとして、BigQueryに関するリリースノートの調査結果を以下に報告します。

---

# BigQuery
## Change
**原文:** An updated version of the Simba JDBC driver for BigQuery is now available.
[Simba JDBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_jdbc_driver)

**説明:**
BigQueryに接続するためのSimba JDBCドライバの新しいバージョンがリリースされ、利用可能になりました。このドライバは、JavaベースのアプリケーションからBigQueryへのデータアクセスやクエリ実行を行う際に使用されます。通常、ドライバの更新には、パフォーマンスの改善、バグ修正、セキュリティの強化、または新しいBigQuery機能への対応が含まれます。

**影響有無:**
**影響無し**

*   **理由:** このリリースは、既存のBigQueryサービスや、現在利用中のアプリケーションで動作しているSimba JDBCドライバのバージョンに直接的な変更を加えるものではありません。新しいバージョンのドライバは「利用可能になった」ものであり、既存のシステムが自動的に更新されることはありません。したがって、既存のワークロードへの即時かつ強制的な影響はありません。
*   ただし、新機能の利用、パフォーマンス改善、または重要なセキュリティ修正が含まれる可能性があるため、将来的なアップグレードは推奨されます。

**対処方法:**
*   **現在の利用状況の確認:** BigQueryに接続する既存のJavaアプリケーション（例えば、データ統合ツール、BIツール、カスタムアプリケーションなど）が、どのバージョンのSimba JDBCドライバを使用しているかを確認してください。
*   **リリースノートの確認:** 更新されたドライバの具体的な変更点（新機能、パフォーマンス改善、バグ修正、セキュリティパッチ、非互換性情報など）について、Simba Technologiesの公式ドキュメントやGoogle CloudのBigQuery JDBCドライバ関連のドキュメントを参照し、詳細を確認してください。特に、セキュリティ関連の修正が含まれる場合は、早急な更新を検討することが重要です。
*   **アップグレードの検討とテスト:** 新しいドライババージョンへのアップグレードを計画する場合は、必ず開発環境またはステージング環境で十分な機能テストとパフォーマンステストを実施してください。これにより、既存のクエリやデータ連携処理への予期せぬ影響がないことを確認します。

**用語説明:**
*   **JDBC (Java Database Connectivity):** Javaアプリケーションからリレーショナルデータベースに接続するための標準的なAPI仕様です。Javaアプリケーションがデータベースを操作するためのインターフェースを提供します。
*   **Simba JDBC driver:** Simba Technologies社が開発・提供しているJDBCドライバの一つで、BigQueryのようなクラウドデータウェアハウスやNoSQLデータベースへの接続を可能にします。データベース固有のプロトコルをJDBC APIに変換する役割を担います。
*   **BigQuery:** Google Cloudが提供する、フルマネージドでスケーラブルなエンタープライズデータウェアハウスサービスです。大規模なデータセットに対して高速なSQLクエリを実行できます。
# Title: September 30, 2026 
Link: https://docs.cloud.google.com/release-notes#September_30_2026<br>
はい、承知いたしました。Google Cloudのインフラエンジニアとして、指定されたリリースノートに対する影響調査を、専門的な言葉遣いと書式で回答いたします。

---

# Cloud Monitoring
## Announcement
**原文:**
The application topology graph is now generally available (GA). This graph helps you to understand relationships between applications, services, and workloads, and shows you traffic flow and incidents in the context of your applications.

**説明:**
Cloud Monitoringにおける「アプリケーション トポロジー グラフ」が一般提供（GA）されました。この機能は、お客様のアプリケーション、サービス、ワークロード間の関係性を視覚的に理解することを支援し、それらのアプリケーションのコンテキスト内でトラフィックフローや発生したインシデントを表示します。これにより、システムの依存関係や問題発生箇所をより直感的に把握できるようになります。

**影響有無:**
影響なし（ポジティブな影響）。
**理由:**
このアナウンスは、Cloud Monitoringにおける新しい可視化機能が一般提供されたことを示すものであり、既存の監視設定、データ収集、またはワークロードの動作に破壊的な変更や互換性の問題をもたらすものではありません。むしろ、アプリケーションの健全性や依存関係の理解を深めるための機能追加であるため、運用上のメリットをもたらします。

**対処方法:**
緊急の対処は不要です。
Cloud Monitoringコンソールから本機能を利用可能であり、アプリケーションやサービスの可視性向上に役立つため、既存のアプリケーション監視体制において本機能の活用を検討することをお勧めします。必要に応じて、本機能の利用方法をドキュメント([application topology graph](https://docs.cloud.google.com/stackdriver/docs/observability/application-topology))で確認し、ダッシュボードやアラート戦略に組み込むことを検討してください。

**用語説明:**
*   **Application topology graph (アプリケーション トポロジー グラフ):** Cloud Monitoringの機能の一つで、アプリケーション、サービス、ワークロード間の論理的な依存関係、通信経路、およびそれらの間のトラフィックフローを視覚的に表現したグラフです。システムの構造や異常を迅速に把握するのに役立ちます。
*   **Generally Available (GA - 一般提供):** Google Cloud プロダクトのローンチステージの一つで、機能が安定しており、本番環境での利用が推奨される状態を指します。通常、SLA（Service Level Agreement）の対象となり、技術サポートが提供されます。
*   **Cloud Monitoring:** Google Cloudが提供する統合モニタリングサービスで、クラウド上のアプリケーション、インフラストラクチャ、およびサービスから指標、ログ、イベントデータを収集、可視化、分析し、アラートを設定することができます。旧称Stackdriver Monitoring。
# Title: September 29, 2026 
Link: https://docs.cloud.google.com/release-notes#September_29_2026<br>
インフラエンジニアとして、提供されたリリースノートに基づき、既存のサービスへの影響調査結果を報告いたします。

---

# Cloud SDK
## Breaking
原文: `Breaking`
説明：Cloud SDKにおいて、互換性のない変更（Breaking Change）が発生する可能性があることを示唆しています。ただし、具体的な変更内容は本リリースノートでは提示されていません。通常、このような変更は既存のスクリプトや自動化ツールに影響を及ぼす可能性があります。
影響有無：具体的な変更内容が不明のため、直接的な影響の有無を判断できません。
対処方法：
Cloud SDKの利用状況（ローカル開発環境、CI/CDパイプライン、自動化スクリプトなど）を確認し、Cloud SDKの完全なリリースノートを参照して、影響を受ける具体的なAPIやコマンドがないかを確認してください。特にSDKのバージョンアップを計画している場合は、本変更がもたらす影響を事前にテスト環境で検証することを強く推奨します。
用語説明：
*   **Breaking Change (破壊的変更)**: ソフトウェアやAPIの変更において、以前のバージョンとの互換性が失われる変更のこと。これにより、古いバージョンで動作していたコードや設定が新しいバージョンでは動作しなくなる可能性があります。

---

# Cloud SQL for PostgreSQL
## Change
原文: `You can use the pgAudit extension to prevent string literals that might indicate sensitive information, such as passwords and secrets, from appearing in your log query results. This release provides minor bug fixes to the previous version. This pgAudit extension capability is supported on [PostgreSQL version].R20260712.01_RC31 or later. For more information, see Audit for PostgreSQL using pgAudit.`
説明：Cloud SQL for PostgreSQLにおいて、`pgAudit` 拡張機能が改善されました。これにより、パスワードや機密情報を含む可能性のある文字列リテラルがログクエリ結果に表示されるのを防ぐ機能が提供され、以前のバージョンでの軽微なバグ修正も含まれています。この新機能は、特定のPostgreSQLバージョン（`[PostgreSQL version].R20260712.01_RC31`以降）でサポートされます。
影響有無：なし。
既存のCloud SQL for PostgreSQLインスタンスの動作に直接的な変更をもたらすものではありません。これは新しい機能の追加と既存機能のバグ修正であり、自動的に既存インスタンスの動作を変更することはありません。pgAudit拡張機能を利用している、または利用を検討している場合は、セキュリティ面でのメリットを享受できます。
対処方法：
pgAudit拡張機能を利用しており、この機密情報マスキング機能の利用やバグ修正の恩恵を受けたい場合は、既存のCloud SQL for PostgreSQLインスタンスをサポートされるバージョン（`[PostgreSQL version].R20260712.01_RC31`またはそれ以降）に更新することを検討してください。インスタンスのバージョンアップは、事前にテスト環境で互換性や動作検証を行った上で、計画的に実施することを推奨します。
用語説明：
*   **pgAudit**: PostgreSQLの拡張機能の一つで、データベースへのアクセスや変更に関する詳細な監査ログを記録する機能を提供します。これにより、セキュリティコンプライアンスの要件を満たしたり、異常なアクティビティを検出したりすることが可能になります。
*   **文字列リテラル**: プログラミング言語やデータベースクエリにおいて、ソースコード内に直接記述された固定の文字列データ。例: `SELECT * FROM users WHERE username = 'admin'` の `'admin'`。機密情報（パスワードなど）が直接クエリに含まれる場合があるため、ログに出力されるとセキュリティリスクとなることがあります。

---

# Compute Engine
## Announcement
原文: `Interface-based versioning (IBV) for the Compute Engine API is now generally available. IBV lets you call a specific, date-based API version so you can adopt API changes on your own schedule. For more information, see Compute Engine API versioning.`
説明：Compute Engine APIのインターフェースベースのバージョン管理（Interface-based versioning, IBV）が一般提供（GA）されました。この機能により、開発者は日付に基づいて特定のAPIバージョンを呼び出すことができるようになり、APIの変更を自身のスケジュールで適用・管理することが可能になります。
影響有無：なし。
これは新しいAPIバージョン管理機能の提供であり、既存のAPI呼び出しの動作を変更するものではありません。既存のAPI呼び出しは、引き続きデフォルトのバージョンまたはこれまで使用していたバージョンで動作します。
対処方法：
現在Compute Engine APIを利用している場合、直ちに対処は不要です。今後のシステム開発やAPIバージョンアップ計画において、このIBVの仕組みを検討に入れることで、より安定したAPI利用が可能になります。特に大規模なシステムや長期運用が想定されるシステムでは、APIのバージョン固定や計画的なバージョンアップ戦略を検討する際にこの機能を活用できるため、詳細については提供されているドキュメントリンクを参照し、将来的な活用を検討してください。
用語説明：
*   **Interface-based versioning (IBV)**: APIのバージョン管理手法の一つ。APIのURIパスやHTTPヘッダなどでバージョンを指定するのではなく、APIのインターフェース（関数シグネチャやデータ構造）自体に基づいてバージョンを管理し、特定の日付時点のインターフェースに固定して利用できるようにするものです。これにより、APIの変更が頻繁に行われる場合でも、ユーザー側で安定したバージョンを利用し続けることが可能になります。
*   **一般提供 (General Availability - GA)**: ベータ版やプレビュー版ではない、すべての顧客が本番環境で利用できる状態の製品や機能。安定しており、Google Cloudから公式サポートが提供されます。
# Title: September 28, 2026 
Link: https://docs.cloud.google.com/release-notes#September_28_2026<br>
Google Cloudのリリースノートに対する影響調査結果を以下の通りご報告いたします。

---

# Cloud Logging
## Deprecated
原文: The legacy Logging agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the supported alternatives. For more information about this deprecation, see Legacy Monitoring and Logging agents end of support.
[supported alternatives](https://docs.cloud.google.com/logging/docs/agent/index)
[Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/logging-agent)

説明：
レガシーなCloud Loggingエージェントが、正式にサポート終了となりました。これにより、標準的なメンテナンスとバグ修正の提供が停止されます。Google Cloudは、サポートが継続される代替エージェント（Ops Agentなど）への移行を強く推奨しています。

影響有無：
*   **影響あり**: お客様の環境で現在、Google Cloud Compute Engine (またはオンプレミスVM) に手動でインストールされたレガシーなCloud Loggingエージェント（`google-fluentd` や `google-stackdriver-logging`）をご利用の場合、今後セキュリティパッチや重要なバグ修正が提供されなくなるため、早急な移行が必要です。
*   **影響なし**: 最新のOps Agentをご利用の場合、またはGoogle Kubernetes Engine (GKE)、Cloud Run、App Engineなどのマネージドサービスをご利用で、明示的にレガシーエージェントを導入していない場合は、この変更による直接的な影響はありません。Google Cloud Composer2の基盤となるGKEクラスタにおいても、通常はレガシーエージェントは使用されていません。

対処方法：
レガシーなCloud Loggingエージェントをご利用中の場合は、Google Cloudが推奨する新しいOps Agentへの移行を計画し、実施してください。移行手順の詳細については、提供されたリンク先のドキュメント（[supported alternatives](https://docs.cloud.google.com/logging/docs/agent/index)）をご参照ください。

用語説明：
*   **Cloud Loggingエージェント**: Compute EngineなどのVMインスタンスからシステムログやアプリケーションログを収集し、Cloud Loggingサービスに送信するためのソフトウェア。
*   **レガシーエージェント**: 旧来のStackdriver Logging agent (`google-fluentd` for Linux, `google-stackdriver-logging` for Windows) を指します。
*   **Ops Agent**: Google Cloudが推奨する、ログと指標の両方を収集できる統合エージェント。レガシーなStackdriver Monitoring agentとLogging agentの後継です。

---

## Breaking
原文: Only platform services can write log entries to billing accounts. These logs have names with the format `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`. For more information, see `entries.write`.
[`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write)

説明：
セキュリティ強化のため、課金アカウントに関連するログエントリ（フォーマットが `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]` であるログ）への書き込みは、Google Cloudプラットフォームサービスのみに限定されました。これにより、ユーザーやアプリケーションが直接これらの課金アカウントログに書き込むことはできなくなります。

影響有無：
*   **影響あり**: お客様のカスタムアプリケーションやスクリプトが、直接 `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]` の形式で課金アカウントログに書き込みを行うような、非常に特殊な運用をしている場合にのみ影響があります。
*   **影響なし**: 通常のGoogle Cloudの利用においては、アプリケーションログやインフラログはプロジェクトレベルで管理され、課金アカウントログに直接書き込むことはありません。したがって、ほとんどのお客様環境、特にGoogle Cloud Composer2などの標準的な環境では影響はありません。

対処方法：
もしお客様のシステムが、この制限に抵触するような特殊なログ書き込みを行っている場合は、設計を見直し、プロジェクトレベルのログに書き込むように変更するか、別の監査・レポートメカニズムを検討する必要があります。

用語説明：
*   **課金アカウントログ**: Google Cloudにおける課金に関連する操作やイベント（例：予算アラート、課金データのエクスポートなど）のログ。これらは主にGoogle Cloudのプラットフォーム自体によって生成されます。
*   **プラットフォームサービス**: Google Cloudが提供するコアサービス（Compute Engine、Cloud Storage、BigQueryなど）自体を指します。

---

# Cloud Monitoring
## Deprecated
原文: The legacy Monitoring agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the supported alternatives. For more information about this deprecation, see Legacy Monitoring and Logging agent end of support.
[supported alternatives](https://docs.cloud.google.com/monitoring/agent/index)
[Legacy Monitoring and Logging agent end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/logging-agent)

説明：
レガシーなCloud Monitoringエージェントが、正式にサポート終了となりました。これにより、標準的なメンテナンスとバグ修正の提供が停止されます。Google Cloudは、サポートが継続される代替エージェント（Ops Agentなど）への移行を強く推奨しています。

影響有無：
*   **影響あり**: お客様の環境で現在、Google Cloud Compute Engine (またはオンプレミスVM) に手動でインストールされたレガシーなCloud Monitoringエージェント（`collectd` for Linux, `stackdriver-monitoring-agent` for Windows）をご利用の場合、今後セキュリティパッチや重要なバグ修正が提供されなくなるため、早急な移行が必要です。
*   **影響なし**: 最新のOps Agentをご利用の場合、またはGKE、Cloud Run、App Engineなどのマネージドサービスをご利用で、明示的にレガシーエージェントを導入していない場合は、この変更による直接的な影響はありません。Google Cloud Composer2の基盤となるGKEクラスタにおいても、通常はレガシーエージェントは使用されていません。

対処方法：
レガシーなCloud Monitoringエージェントをご利用中の場合は、Google Cloudが推奨する新しいOps Agentへの移行を計画し、実施してください。移行手順の詳細については、提供されたリンク先のドキュメント（[supported alternatives](https://docs.cloud.google.com/monitoring/agent/index)）をご参照ください。

用語説明：
*   **Cloud Monitoringエージェント**: Compute EngineなどのVMインスタンスからシステム指標（CPU使用率、メモリ使用率など）を収集し、Cloud Monitoringサービスに送信するためのソフトウェア。
*   **レガシーエージェント**: 旧来のStackdriver Monitoring agent (`collectd` for Linux, `stackdriver-monitoring-agent` for Windows) を指します。
*   **Ops Agent**: Google Cloudが推奨する、ログと指標の両方を収集できる統合エージェント。レガシーなStackdriver Monitoring agentとLogging agentの後継です。

---

# Cloud SQL for PostgreSQL
## Breaking
原文: To improve security, removed the `cloudsql.instances.export` permission from the following roles:
- Cloud SQL Viewer (`roles/cloudsql.viewer`)
- Basic Reader (`roles/reader`)
- Basic Viewer (Legacy) (`roles/viewer`)
To retain export capabilities, assign the Cloud SQL Editor (`roles/cloudsql.editor`) role or update custom roles to include the `cloudsql.instances.export` permission. For more information, see Cloud SQL roles.
[Cloud SQL roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles)

説明：
セキュリティ強化のため、Cloud SQL for PostgreSQLインスタンスのデータベースエクスポート機能 (`cloudsql.instances.export` 権限) が、以下のIAMロールから削除されました。
*   Cloud SQL Viewer (`roles/cloudsql.viewer`)
*   Basic Reader (`roles/reader`)
*   Basic Viewer (Legacy) (`roles/viewer`)
引き続きエクスポート機能を利用するには、Cloud SQL Editor (`roles/cloudsql.editor`) ロールを付与するか、カスタムロールに `cloudsql.instances.export` 権限を明示的に追加する必要があります。

影響有無：
*   **影響あり**: お客様の環境で、上記のいずれかのIAMロールを付与されたユーザーアカウントまたはサービスアカウントが、Cloud SQL for PostgreSQLのデータベースエクスポート機能（gcloud CLI、Cloud Console、APIなどによるエクスポート操作）を利用している場合、これらの操作が実行できなくなります。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響**: Google Cloud Composer2が直接Cloud SQL for PostgreSQLインスタンスのエクスポート操作を行うことは通常ありません。しかし、もしComposerのDAG内で`GoogleCloudSqlExportOperator`のようなオペレータを使用してCloud SQL for PostgreSQLのデータベースエクスポートタスクを実行しており、かつそのタスクが、上記の権限が削除されたサービスアカウントで実行されている場合は、当該タスクが失敗するようになります。DAGのサービスアカウントの権限を見直す必要があります。

対処方法：
Cloud SQL for PostgreSQLのエクスポート機能を利用しているIAMメンバー（ユーザーまたはサービスアカウント）を特定し、以下のいずれかの対応を実施してください。
1.  当該IAMメンバーに **Cloud SQL Editor (`roles/cloudsql.editor`) ロール**を付与する。
2.  カスタムIAMロールを使用している場合は、そのカスタムロールに **`cloudsql.instances.export` 権限**を明示的に追加する。

用語説明：
*   **IAMロール**: Google CloudのIdentity and Access Management (IAM) における、特定の権限の集合体。ユーザーやサービスアカウントに付与することで、Google Cloudリソースへのアクセスを制御します。
*   **`cloudsql.instances.export` 権限**: Cloud SQLインスタンスのデータをCloud Storageにエクスポートする操作を実行するために必要な権限。
*   **Cloud SQL Viewer (`roles/cloudsql.viewer`)**: Cloud SQLインスタンスの構成やデータを参照できるが、変更はできないロール。
*   **Basic Reader (`roles/reader`)**: プロジェクト内のほとんどのリソースを参照できる広範なロール。

---

# Cloud Service Mesh
## Deprecated
原文: Cloud Service Mesh support for the in-cluster `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, in-cluster control plane components on GKE will not receive updates, security patches, or support from Google Cloud. Cloud Service Mesh with the in-cluster `ISTIOD` control plane on Google Distributed Cloud (software only) continues to be supported as described in Supported platforms. You must migrate your clusters to managed Cloud Service Mesh by March 1, 2028. review the Supported features to confirm feature compatibility, and follow the migration guide to transition to managed Cloud Service Mesh with the `TRAFFIC_DIRECTOR` control plane. For more details on the deprecation schedule, see Deprecations.
[Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp)
[Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)
[migration guide](https://docs.cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster)
[Deprecations](https://docs.cloud.google.com/service-mesh/deprecations/)

説明：
Google Kubernetes Engine (GKE) 上におけるCloud Service Meshの「in-cluster `ISTIOD` コントロールプレーン」のサポートが、2026年9月28日をもって非推奨となり、**2028年3月1日**にサポートが完全に終了します。サポート終了後は、in-clusterコントロールプレーンコンポーネントは更新、セキュリティパッチ、Google Cloudからのサポートを受けられなくなります。**2028年3月1日までに、お客様のクラスタをマネージドCloud Service Mesh（`TRAFFIC_DIRECTOR` コントロールプレーンを使用）へ移行することが必須となります。**

影響有無：
*   **影響あり**: お客様のGKEクラスタで、Cloud Service Meshのin-cluster `ISTIOD` コントロールプレーン（お客様自身がIstioコントロールプレーンをGKEクラスタ内にデプロイ・管理する形式）を利用している場合、2028年3月1日までにマネージドCloud Service Meshへの移行計画を策定し、実行する必要があります。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響**: Google Cloud Composer2の環境自体は直接Cloud Service Meshを利用しません。しかし、Composerが稼働しているGKEクラスタがService Meshを構成している場合、この変更はGKEクラスタ全体の運用に影響を与えます。ComposerのDAGがService Meshの機能（例: Istioのトラフィックルーティングやポリシー）に依存している場合は、移行に伴う影響を詳細に評価する必要があります。

対処方法：
現在in-cluster `ISTIOD` コントロールプレーンを利用している場合は、以下の手順でマネージドCloud Service Mesh（`TRAFFIC_DIRECTOR` コントロールプレーン）への移行を計画・実行してください。
1.  現在使用している機能がマネージドCloud Service Meshでサポートされているか、[Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed) ドキュメントで確認してください。
2.  提供されている[migration guide](https://docs.cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster) に従って、移行計画を立案し、実施してください。

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するマネージドなサービスメッシュソリューションで、オープンソースのIstioをベースにしています。
*   **in-cluster `ISTIOD` コントロールプレーン**: Istioのコントロールプレーンである`ISTIOD`をユーザー自身がGKEクラスタ内にデプロイし、そのライフサイクルを管理する形態。
*   **マネージドCloud Service Mesh**: Google Cloudがコントロールプレーンの管理を行うサービスメッシュの形態。ユーザーはデータプレーン（サイドカープロキシ）のみを管理します。
*   **`TRAFFIC_DIRECTOR` コントロールプレーン**: マネージドCloud Service Meshにおいて、Google Cloudのインフラストラクチャを活用した、よりスケーラブルで可用性の高いコントロールプレーンの実装。

---

## Deprecated
原文: Cloud Service Mesh support for the managed `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, managed `ISTIOD` control plane components on GKE on Google Cloud will not receive updates, security patches, or support from Google Cloud, and workload sidecars on unmodernized clusters will fail and be unable to receive or send requests. Google Cloud is transitioning managed Cloud Service Mesh with Istio APIs to the `TRAFFIC_DIRECTOR` control plane implementation using Istio APIs. As part of this transition, support will also end for any features that are incompatible with the `TRAFFIC_DIRECTOR` control plane. To continue using managed Cloud Service Mesh on GKE, you must modernize your clusters by March 1, 2028: Confirm that you affected. Check your compatibility. Review the Supported features to confirm feature compatibility with the `TRAFFIC_DIRECTOR` control plane and evaluate a fleet's compatibility for control plane modernization. Plan your modernization following the modernization guide. For more details on the transition, see Managed control plane documentation and monitor the release notes for ongoing updates.
[Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)
[evaluate a fleet's compatibility for control plane modernization](https://docs.