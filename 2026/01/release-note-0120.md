
# Title: January 19, 2026 
Link: https://docs.cloud.google.com/release-notes#January_19_2026<br>
# BigQuery
## Breaking
原文: Dataform workflows, BigQuery notebooks, pipelines, and data preparations are enforcing strict act-as mode at the project level. To avoid failures and maintain automatic releases, you must use custom service accounts instead of the default Dataform service agent across all repositories. You must also grant the Service Account User role (`roles/iam.serviceAccountUser`) to the default Dataform service agent and relevant principals. For more information and to verify act-as permissions, see [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode).

説明：
Dataformワークフロー、BigQueryノートブック、BigQueryパイプライン、およびデータ準備の機能において、プロジェクトレベルで「厳格なact-asモード（なりすましモード）」が強制されるようになりました。これにより、既存のDataformサービスエージェントの代わりに、カスタムサービスアカウントを使用することが必須となります。また、デフォルトのDataformサービスエージェントと関連するプリンシパルに対して、`Service Account User`ロール（`roles/iam.serviceAccountUser`）を付与する必要があります。この変更は、処理の失敗を防ぎ、自動リリースを継続するために必要です。

影響有無：**あり**
Dataformワークフロー、BigQueryノートブック、パイプライン、またはデータ準備を利用しており、かつデフォルトのDataformサービスエージェントを使用している場合、この変更は既存のワークフローに破壊的な影響を及ぼし、処理が失敗する可能性があります。自動リリースを継続するためには、設定の変更が必須となります。

対処方法：
1.  **利用状況の確認**: 現在、Dataformワークフロー、BigQueryノートブック、パイプライン、データ準備でデフォルトのDataformサービスエージェントを使用しているかを確認してください。
2.  **カスタムサービスアカウントへの移行**: デフォルトのDataformサービスエージェントを使用している場合は、カスタムサービスアカウントを作成し、ワークフローがそのカスタムサービスアカウントを使用するように設定を変更してください。
3.  **IAMロールの付与**: デフォルトのDataformサービスエージェント（`service-<PROJECT_NUMBER>@gcp-sa-dataform.iam.gserviceaccount.com`）および、必要に応じて関連するプリンシパルに対して、`Service Account User`ロール（`roles/iam.serviceAccountUser`）を付与してください。
4.  **詳細の参照**: 変更の具体的な手順と厳格なact-asモードの詳細については、公式ドキュメント「[Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode)」を参照してください。

用語説明：
*   **Dataform**: BigQueryにおけるSQLワークフローの作成、バージョン管理、スケジュール実行、テストなどを行うためのサービス。データ変換パイプラインの構築に利用されます。
*   **BigQuery notebooks**: Jupyterノートブック環境でBigQueryクエリやデータ分析を実行できるサービス。
*   **BigQuery pipelines**: BigQueryのデータ処理ワークフローを構築・オーケストレーションする機能。
*   **data preparations**: BigQueryにおけるデータの準備、変換、およびクレンジングプロセスを指します。
*   **strict act-as mode (厳格なact-asモード)**: サービスアカウントが他のサービスアカウントの権限を借用して（なりすまして）操作を実行する際のセキュリティモデルが強化されたモード。これにより、権限の委譲がより厳密に管理され、不必要な権限の昇格が防止されます。
*   **Dataform service agent**: DataformがGoogle Cloudプロジェクト内のリソース（BigQueryデータセット、Cloud Storageバケットなど）にアクセスするためにGoogleによって管理されるデフォルトのサービスアカウント。通常は`service-<PROJECT_NUMBER>@gcp-sa-dataform.iam.gserviceaccount.com`のような形式です。
*   **Custom service account**: ユーザーがIAMで明示的に作成し、管理するサービスアカウント。特定の権限を細かく設定でき、セキュリティ要件に応じて使い分けることが推奨されます。
*   **Service Account User role (`roles/iam.serviceAccountUser`)**: このIAMロールは、他のサービスアカウントのIDを借用（なりすまし）して、そのサービスアカウントが持つ権限でAPI呼び出しを行うことを許可します。今回の変更では、デフォルトのDataformサービスエージェントが、カスタムサービスアカウントとして動作するためにこのロールが必要となります。