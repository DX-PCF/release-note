
# Title: July 08, 2026 
Link: https://docs.cloud.google.com/release-notes#July_08_2026<br>
Google Cloudのリリースノートに基づき、以下の通り影響調査結果をご報告いたします。

---

# Apigee X

## Security

原文: An Improper Input Validation vulnerability in BigQuery DAO in Google Cloud Apigee versions prior to 2026-06-12 on Google Cloud Platform allowed an authenticated attacker to exfiltrate cross-tenant data.

This vulnerability was patched on 12 June 2026 on the Apigee Servers, and no customer action is needed. Apigee hybrid was not affected.

For more information, see CVE-2026-12879.

説明：
Google Cloud Apigeeの2026年6月12日以前のバージョンにおいて、BigQuery DAOに不適切な入力検証の脆弱性（CVE-2026-12879）が存在しました。これにより、認証された攻撃者がクロステナントのデータを不正に引き出す可能性がありました。
この脆弱性は、2026年6月12日にApigeeサーバー側で修正パッチが適用済みであり、お客様側での追加の対応は不要です。Apigee hybridはこの脆弱性の影響を受けません。

影響有無：
**なし**
Google Cloud側で脆弱性に対するパッチが適用されており、お客様側で特別なアクションは求められていません。Apigee hybridをご利用の場合も影響はありません。

対処方法：
**不要**

用語説明：
*   **Apigee X**: Google Cloudが提供するフルマネージドなAPI管理プラットフォームです。APIの設計、セキュリティ、デプロイ、監視、スケーリングを支援します。
*   **BigQuery DAO (Data Access Object)**: BigQueryのデータにアクセスするための抽象化されたインターフェースやコンポーネントを指します。Apigeeが内部でBigQueryと連携する際に使用される可能性があります。
*   **Improper Input Validation (不適切な入力検証)**: ソフトウェアがユーザーや外部からの入力を適切に検証しないことで発生する脆弱性です。これにより、悪意のあるデータが処理され、予期しない動作やセキュリティ上の問題（例: データ漏洩、コード実行）を引き起こす可能性があります。
*   **Cross-tenant data exfiltration (クロステナントデータ抜き出し)**: マルチテナント環境において、あるテナント（顧客）のデータが、別のテナントから不正にアクセスされたり、外部に持ち出されたりすることです。
*   **CVE (Common Vulnerabilities and Exposures)**: 広く知られている情報セキュリティの脆弱性と露出を識別するためのリストと識別子（ID）です。セキュリティアドバイザリなどで参照され、脆弱性の特定に役立ちます。

---

# BigQuery

## Change

原文: An updated version of the Simba ODBC driver for BigQuery is now available.

[Simba ODBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_odbc_driver)

説明：
BigQueryに接続するためのSimba ODBCドライバーの更新バージョンが公開されました。このドライバーは、Microsoft Excel、Tableau、Power BIなどの様々なBIツールやアプリケーションからBigQueryデータにアクセスするために使用されます。

影響有無：
**一部あり**
直接的なサービスへの影響や既存機能の破壊的な変更はありません。しかし、BigQueryに外部アプリケーションからODBCドライバー経由で接続している環境においては、新しいドライバーへのアップデートを検討するメリットがあります。これには、パフォーマンスの向上、バグ修正、新しい機能のサポートなどが含まれる可能性があります。
なお、Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) は、BigQueryとの連携に主にPythonクライアントライブラリやAirflowのBigQuery Hookを使用するため、このODBCドライバーの更新による直接的な影響は基本的にありません。ODBCドライバーをカスタムで利用するようなAirflowタスクを実装している場合は影響がある可能性があります。

対処方法：
BigQueryにSimba ODBCドライバー経由で接続しているシステムをご利用の場合、以下を推奨します。

1.  **アップグレードの検討**: 新しいドライバーは、機能強化、パフォーマンス改善、またはバグ修正を含んでいる可能性があるため、アップグレードを検討してください。
2.  **互換性テスト**: アップグレードを行う前に、テスト環境で新しいドライバーの互換性と安定性を十分に検証してください。既存のアプリケーションやクエリに予期せぬ影響がないことを確認することが重要です。
3.  **定期的な確認**: 現在のドライバーで問題なく稼働している場合でも、セキュリティ修正やパフォーマンス改善のために、定期的に最新版のドライバーを確認することを推奨します。

用語説明：
*   **BigQuery**: Google Cloudが提供する、フルマネージドでペタバイト規模のデータをSQLで分析できるエンタープライズデータウェアハウスサービスです。
*   **ODBC (Open Database Connectivity)**: さまざまなデータベースにアクセスするための標準的なプログラミングインターフェース（API）です。これにより、アプリケーションは特定のデータベースシステムに依存することなく、汎用的な方法でデータに接続・操作できます。
*   **Simba ODBC driver for BigQuery**: Simba Technologies社が開発・提供している、BigQueryにODBC経由で接続するためのソフトウェアドライバーです。多くのサードパーティ製BIツールや分析ツールがBigQueryへの接続にこのドライバーを利用しています。
# Title: July 07, 2026 
Link: https://docs.cloud.google.com/release-notes#July_07_2026<br>
## Cloud SDK
### Change
原文: (本文が提供されていません)
説明: リリースノートの本文が提供されていないため、具体的な変更内容は不明です。
影響有無: 変更内容が不明のため、現在のサービス構成への影響有無は判断できません。
対処方法: リリースノートの本文が明確になった場合、改めて影響調査と必要な対処方法を検討します。
用語説明:
*   **Cloud SDK**: Google Cloud Platformのサービスを管理・操作するためのコマンドラインツール (gcloud CLI)、クライアントライブラリ、エミュレータなどが含まれる統合開発環境キットです。

---

## Google Kubernetes Engine
### Change
原文: For GKE Standard clusters, the maximum number of nodes that you can upgrade simultaneously by using surge upgrades (`maxSurge` + `maxUnavailable`) is now 100. Each of these settings can be set as high as 100, but their sum can be no higher than 100. For more information, see Surge upgrades.
[Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge)
説明: GKE Standard クラスタにおいて、ノードプールのサージアップグレード（Surge upgrades）時に同時にアップグレードできるノードの最大数が100に変更されました。これは、`maxSurge` (一時的に追加されるノード数) と `maxUnavailable` (一時的に利用不可となるノード数) の合計が100を超えることはできないことを意味します。個々の設定値（`maxSurge`または`maxUnavailable`）は最大100まで設定可能ですが、それらの合計が100を超えることはできません。
影響有無: **影響あり**
理由:
この変更は、大規模なGKE Standardクラスタでノードプールアップグレードを行う際の動作に影響を与える可能性があります。
*   既存のノードプール設定で`maxSurge`と`maxUnavailable`の合計が100を超えている場合、この設定は無効になるか、エラーとなる可能性があります。
*   これまで100を超えるノードを同時にサージアップグレードしていた運用をしている場合、アップグレードの戦略を見直す必要があります。
*   通常、小規模なクラスタや、`maxSurge`+`maxUnavailable`の合計が少ないデフォルト設定を使用している場合は、直接的な影響は少ないと考えられます。しかし、上限値が設定された（または変更された）という事実自体が、将来的な拡張性やアップグレード計画に影響を与える可能性があります。
対処方法:
1.  **既存設定の確認**: 現在運用中のGKE Standardクラスタのノードプールアップグレード設定（`maxSurge`と`maxUnavailable`の値）を確認してください。
    *   `gcloud container node-pools describe [NODE_POOL_NAME] --cluster=[CLUSTER_NAME] --zone=[ZONE]` コマンドなどで確認可能です。
2.  **設定値の調整**: もし`maxSurge`と`maxUnavailable`の合計が100を超えている場合、合計が100以下になるように設定値を調整してください。アップグレードの速度とサービスの可用性のバランスを考慮して適切な値を設定します。
3.  **今後のアップグレード計画**: 大規模なノードプールを運用している場合、この新しい上限値を考慮に入れたアップグレード計画を立ててください。必要に応じて、アップグレードを複数回に分割するなどの戦略を検討します。
用語説明:
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するマネージドなKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、スケーリング、管理を容易にします。
*   **GKE Standardクラスタ**: GKEの提供するクラスタモードの一つで、ノード（VMインスタンス）のプロビジョニングやパッチ適用、管理などをユーザーがより詳細に制御できます。対照的に、Autopilotクラスタではノード管理がGKEによって完全に自動化されます。
*   **サージアップグレード (Surge upgrades)**: GKEのノードプールをアップグレードする戦略の一つです。新しいバージョンのノードを既存のノードに「追加」し、新しいノードにワークロードを移行させてから古いノードを削除することで、アップグレード中のサービス中断を最小限に抑えます。
*   **`maxSurge`**: サージアップグレード中に、ノードプールが一時的に通常のサイズを超えて追加プロビジョニングできるノードの最大数を指定します。例えば`maxSurge=5`の場合、通常100ノードのノードプールが一時的に105ノードになる可能性があります。
*   **`maxUnavailable`**: サージアップグレード中に、同時に利用不可となることを許容するノードの最大数を指定します。この数を超えてノードが利用不可能になることはありません。サービスの可用性を維持するために、この値を適切に設定する必要があります。
# Title: July 06, 2026 
Link: https://docs.cloud.google.com/release-notes#July_06_2026<br>
# BigQuery

## Change
原文: For data transfers from Facebook Ads, support for the `AdInsightsMMM` report has been temporarily disabled. Existing data transfers from Facebook Ads that include the `AdInsightsMMM` report will continue to run, but the transfer won't include data from the `AdInsightsMMM` report. This change is due to schema changes in the Facebook Ads API.

説明:
BigQuery Data Transfer Service を使用して Facebook Ads からデータを転送する場合、`AdInsightsMMM` レポートのサポートが一時的に無効化されました。既に設定されている Facebook Ads からのデータ転送で `AdInsightsMMM` レポートが含まれている場合、転送ジョブ自体は引き続き実行されますが、`AdInsightsMMM` レポートのデータは転送されなくなります。この変更は、Facebook Ads API のスキーマ変更に起因するものです。

影響有無:
影響あり。
Facebook Ads から `AdInsightsMMM` レポートのデータを BigQuery に転送し、そのデータに依存する分析やレポート、ダッシュボードを運用している場合、データが一時的に欠損するため影響を受けます。`AdInsightsMMM` レポートを使用していない場合は影響ありません。

対処方法:
1.  **影響範囲の確認**: BigQuery Data Transfer Service で Facebook Ads からの転送設定を確認し、`AdInsightsMMM` レポートを利用しているかを確認してください。
2.  **代替手段の検討**:
    *   `AdInsightsMMM` レポートのデータが必須の場合、Facebook Ads API から直接データを取得し、BigQuery に手動またはカスタムスクリプトでロードすることを検討してください。
    *   他の利用可能な Facebook Ads レポートで必要なデータが代替可能かどうかを評価してください。
3.  **ダウンストリームへの影響確認**: `AdInsightsMMM` レポートのデータを使用している全てのレポート、ダッシュボード、分析プロセス、機械学習モデルなどについて、データ欠損による影響がないか確認し、必要に応じて対応計画を立ててください。
4.  **Google Cloudのアップデートを監視**: この変更は「一時的」とされているため、Google Cloud からのサポート再開に関するアナウンスを継続的に監視してください。

用語説明:
*   **BigQuery Data Transfer Service**: BigQuery にデータを自動的に取り込むためのサービスです。SaaS アプリケーション（例: Google Ads, Facebook Ads）やクラウドストレージなど、さまざまなデータソースから定期的にデータを転送できます。
*   **Facebook Ads API**: Facebook広告プラットフォームのデータ（キャンペーン情報、パフォーマンス指標など）にプログラムからアクセスし、操作するためのインターフェースです。
*   **`AdInsightsMMM` report**: Facebook広告のインサイトデータに関する特定のレポートタイプを指します。MMM は Marketing Mix Modeling など、特定の分析目的で使用される指標セットに関連する可能性が高いです。