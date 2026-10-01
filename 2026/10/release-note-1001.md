
# Title: September 30, 2026 
Link: https://docs.cloud.google.com/release-notes#September_30_2026<br>
# Cloud Monitoring
## Announcement
原文: The application topology graph is now generally available (GA). This graph helps you to understand relationships between applications, services, and workloads, and shows you traffic flow and incidents in the context of your applications.

説明：
Cloud Monitoring の「アプリケーション トポロジー グラフ」が一般提供（GA）になりました。このグラフは、Google Cloud 上で稼働するアプリケーション、サービス、ワークロード間の関連性や依存関係を視覚的に表示します。これにより、トラフィックの流れや発生しているインシデントをアプリケーション全体のコンテキストで把握し、より迅速な問題特定とトラブルシューティングを支援します。

影響有無：
**影響なし（ポジティブな影響あり）**
この変更は新機能の一般提供開始であり、既存のCloud Monitoringの設定や監視ロジックに直接的な変更を求めるものではありません。既存のシステム運用に悪影響を与えることはありません。むしろ、アプリケーションの構成や関係性の可視化が向上するため、運用における可視性やトラブルシューティング能力の向上に寄与します。

対処方法：
特別な対処は不要です。Cloud Monitoring のコンソールから「アプリケーション トポロジー グラフ」の機能にアクセスし、既存のアプリケーションの依存関係やトラフィックフローの可視化に活用できます。この機能の利用により、アプリケーションの健全性監視や障害発生時の原因特定が効率化される可能性がありますので、積極的な利用を推奨します。

用語説明：
*   **Application topology graph (アプリケーション トポロジー グラフ)**:
    アプリケーションを構成する個々のサービスやワークロード（例えば、GKE上のサービス、Cloud Functions、Cloud Runなど）がどのように相互に連携し、データをやり取りしているかを図式化したものです。これにより、システム全体の構造とデータの流れを一目で把握できます。
*   **Generally available (GA - 一般提供)**:
    Google Cloud プロダクトのライフサイクルにおけるフェーズの一つで、機能が安定しており、本番環境での利用が推奨される状態を指します。通常、GAに達した機能は、サービスレベル契約（SLA）の対象となります。
*   **Cloud Monitoring**:
    Google Cloud が提供するフルマネージドな監視サービスです。Google Cloud リソースだけでなく、オンプレミスやマルチクラウド環境のリソースからの指標、ログ、イベントを収集し、システムパフォーマンス、可用性、健全性を監視・可視化します。
*   **Workload (ワークロード)**:
    特定のタスクを実行するためにリソースを使用するアプリケーションやプロセス群の総称です。例えば、ウェブサーバー、データベース、バッチ処理などがワークロードに該当します。
*   **Incident (インシデント)**:
    システムやサービスに予期せぬ問題が発生し、その機能や可用性が低下または停止した状況を指します。監視ツールは、これらのインシデントを検出し、アラートを発するために使用されます。
# Title: September 29, 2026 
Link: https://docs.cloud.google.com/release-notes#September_29_2026<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、構築済みのサービスへの影響有無について調査し、専門的な言葉遣いと書式設定を用いて回答いたします。

---

# Cloud SDK
## Breaking
原文: (No specific content provided for "Breaking")
説明：このリリースノートでは、Cloud SDKの変更カテゴリとして「Breaking」が示されていますが、具体的な変更内容が記載されていません。通常、Cloud SDKにおける「Breaking Change」は、既存のコマンド、スクリプト、APIの動作に非互換な変更が導入されたことを意味します。これにより、アップグレード後に既存の自動化スクリプトやCI/CDパイプラインなどが機能しなくなる可能性があります。

影響有無：現在の情報では、具体的な変更内容が不明なため、直接的な影響の有無を判断できません。ただし、「Breaking」カテゴリであることから、何らかの非互換性のある変更が含まれている可能性が高いです。

対処方法：
1.  **詳細情報の確認**: Cloud SDKの公式リリースノートや`gcloud components update`コマンド実行時の出力、またはGoogle Cloudの公式ドキュメントで、この「Breaking Change」に関する詳細な情報が後日公開されていないか確認してください。
2.  **テスト環境での検証**: お客様の環境でCloud SDKをCI/CDパイプラインや自動化スクリプトなどで利用している場合、Cloud SDKを本番環境に適用する前に、非本番環境（テスト環境など）で動作検証を実施し、既存のワークフローに影響がないことを確認することを強く推奨します。
3.  **バージョン固定の検討**: 不要な影響を避けるため、CI/CD環境などで使用するCloud SDKのバージョンを明示的に固定し、計画的なアップデートと検証を行う運用を検討してください。

用語説明：
*   **Cloud SDK**: Google Cloud Platformのサービスをコマンドラインから操作するための統合ツールセットです。`gcloud`コマンドラインツール、`gsutil`ユーティリティ、`bq`ユーティリティなどが含まれます。
*   **Breaking Change**: ソフトウェア開発において、API、機能、または動作が変更され、以前のバージョンとの後方互換性が失われる変更のことです。これにより、既存のコードや設定が新しいバージョンでは動作しなくなる可能性があり、修正や適応が必要となる場合があります。

---

# Cloud SQL for PostgreSQL
## Change
原文: You can use the pgAudit extension to prevent string literals that might indicate sensitive information, such as passwords and secrets, from appearing in your log query results. This release provides minor bug fixes to the previous version. This pgAudit extension capability is supported on `[PostgreSQL version].R20260712.01_RC31` or later. For more information, see [Audit for PostgreSQL using pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit).

説明：Cloud SQL for PostgreSQLにおいて、`pgAudit`拡張機能に関する変更が提供されました。このリリースでは、パスワードや秘密情報といった機密性の高い文字列リテラルがデータベースの監査ログクエリ結果に意図せず表示されてしまうのを防ぐための`pgAudit`機能に対し、軽微なバグ修正が適用されました。この改善された`pgAudit`機能は、`[PostgreSQL version].R20260712.01_RC31`以降のPostgreSQLバージョンでサポートされます。

影響有無：
*   **pgAuditを使用している場合**: 影響あり。これは既存の`pgAudit`機能におけるセキュリティおよびロギングの品質を向上させるためのバグ修正です。特に、機密情報がログに記録されるリスクを軽減する効果が期待できます。
*   **pgAuditを使用していない場合**: 直接的な影響はありません。
*   **現在のPostgreSQLバージョン**: お客様のCloud SQL for PostgreSQLインスタンスが`[PostgreSQL version].R20260712.01_RC31`より前のバージョンで`pgAudit`を使用している場合、このバグ修正の恩恵を受けるためにはインスタンスのバージョンアップまたはメンテナンスによるアップデートが必要となる可能性があります。

対処方法：
1.  **バージョン確認**: まず、現在ご利用中のCloud SQL for PostgreSQLインスタンスのPostgreSQLバージョンが`[PostgreSQL version].R20260712.01_RC31`以降であるか確認してください。このバージョン表記は、通常、マイナーバージョンとリリース日付に基づいた内部バージョンを組み合わせたものです（例: `14.5.0.R20260712.01_RC31`）。
2.  **アップデートの適用**:
    *   Cloud SQLインスタンスは通常、メンテナンスウィンドウを通じて自動的に最新のマイナーバージョンにアップデートされます。このバグ修正は、メンテナンスウィンドウ中に自動的に適用される可能性があります。
    *   もし、すぐにこの修正を適用したい場合や、現在のバージョンが古い場合は、Cloud SQLインスタンスの**メンテナンスの構成**を確認し、必要に応じてメンテナンスのスケジューリングを調整するか、手動でのマイナーバージョンアップを検討してください。手動でのバージョンアップは、ダウンタイムを伴う可能性がありますので、事前に十分な計画とテストを行ってください。
3.  **ログ内容の再確認**: アップデート適用後、機密性の高い情報がログに表示されていないことを定期的に確認し、意図した通りの監査ロギングが行われていることを確認してください。

用語説明：
*   **Cloud SQL**: Google Cloudが提供する、フルマネージドなリレーショナルデータベースサービスです。PostgreSQL、MySQL、SQL Serverをサポートしており、データベースのプロビジョニング、パッチ適用、バックアップ、レプリケーションなどを自動的に管理します。
*   **pgAudit**: PostgreSQLの拡張機能の一つで、データベースへのアクセスや操作に関する詳細な監査ログを生成するために使用されます。これにより、セキュリティ要件やコンプライアンス要件を満たすために、誰が、いつ、どのようなSQLクエリを実行したかを追跡できます。
*   **文字列リテラル (String Literal)**: プログラミング言語やデータベースのSQLクエリにおいて、ソースコード中に直接記述される固定の文字列値のことです。例えば、`'password123'`や`'secret_key_abc'`などが文字列リテラルにあたります。
*   **バグ修正 (Bug Fix)**: ソフトウェアの不具合や欠陥（バグ）を特定し、修正するプロセスです。通常、ソフトウェアの安定性、セキュリティ、または機能の正確性を向上させることを目的として行われます。
# Title: September 28, 2026 
Link: https://docs.cloud.google.com/release-notes#September_28_2026<br>
ご担当者様

Google Cloudのリリースノートに関するお問い合わせ、ありがとうございます。
ご連絡いただいたリリースノートについて、構築済みのサービスへの影響有無を調査いたしました。

## Cloud Logging
### Deprecated
原文: The legacy Logging agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the supported alternatives. For more information about this deprecation, see Legacy Monitoring and Logging agents end of support.
[supported alternatives](https://docs.cloud.google.com/logging/docs/agent/index)
[Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/logging-agent)

説明:
レガシーなCloud Loggingエージェントが正式にサポート終了となりました。これに伴い、エージェントの標準メンテナンスおよび通常のバグ修正は停止されます。現在、最新のOps Agentまたは他のサポートされている代替エージェントへの移行が推奨されています。

影響有無:
**影響がある可能性があります。**
*   **レガシーLoggingエージェントを使用している場合**: 運用中のVMインスタンス等でレガシーLoggingエージェントを導入している場合は、今後セキュリティパッチやバグ修正が提供されなくなるため、早急なOps Agentへの移行を推奨します。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響**: Composerはマネージドサービスであり、基盤となるGKEクラスタやVMインスタンスのエージェントはGoogle Cloudが管理しています。そのため、Composer環境自体がこの変更によって直接影響を受けることは通常ありません。しかし、Composer環境に関連するカスタムVM等でレガシーエージェントを使用している場合は影響を受けます。

対処方法:
*   現在利用中のVMインスタンス等でレガシーLoggingエージェントが導入されていないか確認してください。
*   レガシーLoggingエージェントを使用している場合は、[Ops Agent](https://cloud.google.com/monitoring/agents/ops-agent)への移行を計画・実施してください。Ops AgentはLoggingとMonitoringの両方の機能を提供します。

用語説明:
*   **レガシーLoggingエージェント**: 以前のCloud Logging（旧Stackdriver Logging）で利用されていたログ収集エージェント。
*   **Ops Agent**: Cloud MonitoringとCloud Loggingの両方の指標とログを収集するためにGoogle Cloudが推奨する新しい統合エージェント。

### Breaking
原文: Only platform services can write log entries to billing accounts. These logs have names with the format `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`. For more information, see `entries.write`.
[`entries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write)

説明:
課金アカウント（billing account）を対象とするログエントリの書き込みが、Google Cloudのプラットフォームサービスのみに制限されました。`billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`の形式でログ名を指定して、ユーザーが直接課金アカウントにログを書き込むことはできなくなります。

影響有無:
**影響は低いと考えられますが、特殊な構成では影響する可能性があります。**
*   **通常運用の場合**: 一般的なアプリケーションやユーザーが直接`billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`形式のログ名を指定してログを書き込むことは稀であるため、ほとんどの環境では直接的な影響はありません。
*   **カスタム実装の場合**: もし既存のシステムで、特定の目的のためにCloud Logging APIの`entries.write`メソッドを呼び出し、明示的に課金アカウントを対象とするログ名を指定してログを書き込むようなカスタム実装を行っている場合は、エラーが発生する可能性があります。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響**: Composer自体が課金アカウントに直接ログを書き込むことはありません。DAG内でのカスタムスクリプトやオペレータがこのような特殊なログ書き込みを行っていない限り、Composer環境には直接影響はありません。

対処方法:
*   既存のシステムでCloud Logging APIを利用したログ書き込み処理において、`billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`形式のログ名を使用していないか確認してください。
*   もし該当する書き込み処理がある場合は、プロジェクトまたは組織レベルのログシンクを利用してログを集約するか、適切なプロジェクトにログを書き込むようにログ名を変更することを検討してください。

用語説明:
*   **ログエントリ**: Cloud Loggingに記録される個々のログデータ。
*   **課金アカウント (Billing Account)**: Google Cloudの利用料金が請求されるアカウント。
*   **`entries.write`**: Cloud Logging APIのメソッドの一つで、ログエントリをCloud Loggingに書き込むために使用されます。

## Cloud Monitoring
### Deprecated
原文: The legacy Monitoring agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased. We recommend migrating to one of the supported alternatives. For more information about this deprecation, see Legacy Monitoring and Logging agent end of support.
[supported alternatives](https://docs.cloud.google.com/monitoring/agent/index)
[Legacy Monitoring and Logging agent end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/logging-agent)

説明:
レガシーなCloud Monitoringエージェントが正式にサポート終了となりました。これに伴い、エージェントの標準メンテナンスおよび通常のバグ修正は停止されます。現在、最新のOps Agentまたは他のサポートされている代替エージェントへの移行が推奨されています。

影響有無:
**影響がある可能性があります。**
*   **レガシーMonitoringエージェントを使用している場合**: 運用中のVMインスタンス等でレガシーMonitoringエージェントを導入している場合は、今後セキュリティパッチやバグ修正が提供されなくなるため、早急なOps Agentへの移行を推奨します。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響**: Composerはマネージドサービスであり、基盤となるGKEクラスタやVMインスタンスのエージェントはGoogle Cloudが管理しています。そのため、Composer環境自体がこの変更によって直接影響を受けることは通常ありません。しかし、Composer環境に関連するカスタムVM等でレガシーエージェントを使用している場合は影響を受けます。

対処方法:
*   現在利用中のVMインスタンス等でレガシーMonitoringエージェントが導入されていないか確認してください。
*   レガシーMonitoringエージェントを使用している場合は、[Ops Agent](https://cloud.google.com/monitoring/agents/ops-agent)への移行を計画・実施してください。Ops AgentはLoggingとMonitoringの両方の機能を提供します。

用語説明:
*   **レガシーMonitoringエージェント**: 以前のCloud Monitoring（旧Stackdriver Monitoring）で利用されていたメトリック収集エージェント。
*   **Ops Agent**: Cloud MonitoringとCloud Loggingの両方の指標とログを収集するためにGoogle Cloudが推奨する新しい統合エージェント。

## Cloud SQL for PostgreSQL
### Breaking
原文: To improve security, removed the `cloudsql.instances.export` permission from the following roles: Cloud SQL Viewer (`roles/cloudsql.viewer`), Basic Reader (`roles/reader`), Basic Viewer (Legacy) (`roles/viewer`). To retain export capabilities, assign the Cloud SQL Editor (`roles/cloudsql.editor`) role or update custom roles to include the `cloudsql.instances.export` permission. For more information, see Cloud SQL roles.
[Cloud SQL roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles)

説明:
セキュリティ強化のため、Cloud SQLインスタンスのエクスポートを行うための`cloudsql.instances.export`権限が、以下の読み取り専用ロールから削除されました。
*   Cloud SQL Viewer (`roles/cloudsql.viewer`)
*   Basic Reader (`roles/reader`)
*   Basic Viewer (Legacy) (`roles/viewer`)
これらのロールを付与されているユーザーやサービスアカウントがエクスポート機能を引き続き利用するには、Cloud SQL Editor (`roles/cloudsql.editor`) ロールを付与するか、カスタムロールに明示的に`cloudsql.instances.export`権限を追加する必要があります。

影響有無:
**影響がある可能性があります。**
*   **Cloud SQLのエクスポート操作を利用している場合**: 現在、`roles/cloudsql.viewer`、`roles/reader`、`roles/viewer`のいずれかのロールを付与されたユーザーまたはサービスアカウントが、Cloud SQL for PostgreSQLのエクスポート操作（例: データベースのバックアップをCloud Storageにエクスポートするなど）を実行している場合に影響が発生します。これらのロールではエクスポートができなくなります。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響**: Composer環境でCloud SQL for PostgreSQLと連携し、Composerのサービスアカウント（GKEノードサービスアカウントなど）が上記影響を受けるロール（例: `roles/reader`）を付与されており、かつDAG等でCloud SQLのエクスポート操作をトリガーしている場合に影響が発生する可能性があります。Cloud SQLへの一般的な接続やクエリ実行には影響しませんが、エクスポート機能を利用している場合は確認が必要です。

対処方法:
*   Cloud SQL for PostgreSQLインスタンスのエクスポート操作を実行しているユーザーまたはサービスアカウントを確認してください。
*   該当するユーザー/サービスアカウントが、上記の削除対象となったロールを付与されている場合、以下のいずれかの対応を行ってください。
    *   `cloudsql.editor`ロールを付与する。
    *   `cloudsql.instances.export`権限を明示的に含むカスタムIAMロールを定義し、それを付与する。

用語説明:
*   **IAM (Identity and Access Management)**: Google Cloudのアクセス制御システム。誰がどのリソースに対してどのような操作を行えるかを定義します。
*   **ロール (Role)**: 特定のリソースに対する一連の権限をまとめたもの。
*   **権限 (Permission)**: 特定のリソースに対して実行できる個々のアクション（例: `cloudsql.instances.export`）。

## Cloud Service Mesh
### Deprecated
原文: Cloud Service Mesh support for the in-cluster `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, in-cluster control plane components on GKE will not receive updates, security patches, or support from Google Cloud. Cloud Service Mesh with the in-cluster `ISTIOD` control plane on Google Distributed Cloud (software only) continues to be supported as described in Supported platforms. You must migrate your clusters to managed Cloud Service Mesh by March 1, 2028. review the Supported features to confirm feature compatibility, and follow the migration guide to transition to managed Cloud Service Mesh with the `TRAFFIC_DIRECTOR` control plane.
[Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp)
[Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)
[migration guide](https://docs.cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster)
 For more details on the deprecation schedule, see Deprecations.
[Deprecations](https://docs.cloud.google.com/service-mesh/deprecations/)

説明:
GKE (Google Kubernetes Engine) 上で実行されるCloud Service Meshのインクラスター型`ISTIOD`コントロールプレーンのサポートが、2026年9月28日をもって非推奨となり、**2028年3月1日**にサポートが終了します。2028年3月1日以降、GKE上のインクラスターコントロールプレーンコンポーネントはGoogle Cloudからの更新、セキュリティパッチ、サポートを受けられなくなります。ユーザーは2028年3月1日までに、マネージドCloud Service Mesh (TRAFFIC_DIRECTORコントロールプレーン) への移行を完了する必要があります。

影響有無:
**Cloud Service MeshをGKEで利用している場合は影響があります。**
*   **Cloud Service Meshの利用状況**: 現在、GKEクラスタ上でCloud Service Mesh（Istio）をデプロイし、かつそのコントロールプレーンとしてインクラスター型`ISTIOD`を使用している場合に直接的な影響があります。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響**: Composerは内部的にGKEを使用していますが、Composer自身がCloud Service Meshを必須のコンポーネントとして利用することはありません。Composer環境のワークロードをService Mesh配下に置くなどの特殊な構成を行っていない限り、Composer2.7.1には直接的な影響はありません。

対処方法:
*   現在GKE上でCloud Service Meshを利用しており、インクラスター型`ISTIOD`コントロールプレーンを使用しているか確認してください。
*   該当する場合は、[サポートされる機能](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)を確認し、[移行ガイド](https://docs.cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster)に従って、2028年3月1日までにマネージドCloud Service Mesh (TRAFFIC_DIRECTORコントロールプレーン) への移行を計画・実施してください。

用語説明:
*   **Cloud Service Mesh**: Google Cloudのマネージドなサービスメッシュプラットフォーム。マイクロサービス間の通信を管理・可視化・セキュリティ強化する機能を提供します。Istioを基盤としています。
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドなKubernetesサービス。
*   **Istiod**: Istioのコントロールプレーンの中心的なコンポーネント。サービスディスカバリ、コンフィグレーション、証明書管理などを担当します。
*   **インクラスター型コントロールプレーン**: IstioのコントロールプレーンがユーザーのGKEクラスタ内にデプロイされ、ユーザー自身がその管理を行う形式。
*   **マネージドCloud Service Mesh**: Google Cloudがコントロールプレーンを管理する形式。ユーザーはデータプレーンの管理に集中できます。
*   **TRAFFIC_DIRECTOR**: マネージドCloud Service Meshのコントロールプレーンとして利用されるGoogle Cloudのネットワークサービス。

### Deprecated
原文: Cloud Service Mesh support for the managed `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, managed `ISTIOD` control plane components on GKE on Google Cloud will not receive updates, security patches, or support from Google Cloud, and workload sidecars on unmodernized clusters will fail and be unable to receive or send requests. Google Cloud is transitioning managed Cloud Service Mesh with Istio APIs to the `TRAFFIC_DIRECTOR` control plane implementation using Istio APIs. As part of this transition, support will also end for any features that are incompatible with the `TRAFFIC_DIRECTOR` control plane. To continue using managed Cloud Service Mesh on GKE, you must modernize your clusters by March 1, 2028:
- Confirm that you affected.
- Check your compatibility. Review the Supported features to confirm feature compatibility with the `TRAFFIC_DIRECTOR` control plane and evaluate a fleet's compatibility for control plane modernization.
- Plan your modernization following the modernization guide.
[Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)
[evaluate a fleet's compatibility for control plane modernization](https://docs.cloud.google.com/service-mesh/docs/migrate/eligibility)
[modernization guide](https://docs.cloud.google.com/service-mesh/docs/modernization)
 For more details on the transition, see Managed control plane documentation and monitor the release notes for ongoing updates.
[Managed control plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane-overview)
[release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes)

説明:
GKE上のマネージド`ISTIOD`コントロールプレーンを使用するCloud Service Meshのサポートが、2026年9月28日をもって非推奨となり、**2028年3月1日**にサポートが終了します。Google Cloudは、マネージドCloud Service MeshのIstio APIとの連携を`TRAFFIC_DIRECTOR`コントロールプレーンの実装へと移行します。この移行に伴い、`TRAFFIC_DIRECTOR`コントロールプレーンと互換性のない一部の機能のサポートも終了します。引き続きGKEでマネージドCloud Service Meshを利用するには、2028年3月1日までにクラスタのモダナイゼーション（近代化）が必要です。

影響有無:
**Cloud Service MeshをGKEでマネージドIstiodとして利用している場合は影響があります。**
*   **Cloud Service Meshの利用状況**: 現在、GKEクラスタ上でCloud Service Meshをデプロイし、かつそのコントロールプレーンとしてマネージド`ISTIOD`を使用している場合に直接的な影響があります。2028年3月1日以降、未モダナイズのクラスタではワークロードのサイドカーが機能しなくなる可能性があります。
*   **機能互換性**: 現在利用しているCloud Service Meshの機能が`TRAFFIC_DIRECTOR`コントロールプレーンと互換性があるか確認が必要です。互換性がない機能を使用している場合は、代替策を検討する必要があります。
*   **Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響**: Composerは内部的にGKEを使用していますが、Composer自身がCloud Service Meshを必須のコンポーネントとして利用することはありません。Composer環境のワークロードをService Mesh配下に置くなどの特殊な構成を行っていない限り、Composer2.7.1には直接的な影響はありません。

対処方法:
*   現在GKE上でCloud Service Meshを利用しており、マネージド`ISTIOD`コントロールプレーンを使用しているか確認してください。
*   該当する場合は、[サポートされる機能](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)を参照して機能の互換性を確認し、[モダナイゼーションガイド](https://docs.cloud.google.com/service-mesh/docs/modernization)に従って、2028年3月1日までにクラスタのモダナイゼーションを計画・実施してください。

用語説明:
*   **マネージド`ISTIOD`コントロールプレーン**: Google CloudがIstioのコントロールプレーンを管理し、ユーザーはデータプレーン（サイドカープロキシ）の管理に集中できるサービスモデル。今回の変更により、このマネージドコントロールプレーンのバックエンド実装がTRAFFIC_DIRECTORベースに移行します。
*   **サイドカープロキシ (Sidecar Proxy)**: サービスメッシュにおいて、各ワークロード（Pod）に並行してデプロイされるプロキシ。サービス間の通信をインターセプトし、トラフィック管理、セキュリティ、可観測性などの機能を提供します。
*   **モダナイゼーション (Modernization)**: 古いシステムや構成を最新の技術やベストプラクティスに合わせて更新すること。ここでは、Cloud Service Meshのコントロールプレーンの基盤変更に対応するためのクラスタ更新を指します。

---

ご不明な点がございましたら、お気軽にお問い合わせください。