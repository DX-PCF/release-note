
# Title: July 06, 2026 
Link: https://docs.cloud.google.com/release-notes#July_06_2026<br>
# BigQuery
## Change
**原文:**
 For data transfers from Facebook Ads, support for the `AdInsightsMMM` report has been temporarily disabled. Existing data transfers from Facebook Ads that include the `AdInsightsMMM` report will continue to run, but the transfer won't include data from the `AdInsightsMMM` report.

[data transfers from Facebook Ads](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer)
 This change is due to schema changes in the Facebook Ads API.

 For more information, see July 06, 2026.

[July 06, 2026](https://docs.cloud.google.com/bigquery/docs/transfer-changes#Jul06-fb-ads)

**説明:**
BigQuery Data Transfer ServiceのFacebook Ads転送機能において、`AdInsightsMMM`レポートのデータ転送サポートが一時的に無効化されました。この変更は、Facebook Ads APIのスキーマ変更に起因します。既に設定済みのFacebook Adsからのデータ転送ジョブは継続して実行されますが、`AdInsightsMMM`レポートのデータは転送されなくなります。

**影響有無:**
*   **影響あり**
*   理由: BigQuery Data Transfer Serviceを利用してFacebook Adsから`AdInsightsMMM`レポートのデータをBigQueryに転送し、そのデータを分析やレポート作成に利用している場合、当該レポートのデータが一時的に取得できなくなります。これにより、該当データに依存する分析パイプラインやダッシュボードにデータ欠損や不正確な情報表示が発生する可能性があります。

**対処方法:**
1.  **利用状況の確認**: BigQuery Data Transfer Serviceで設定しているFacebook Ads転送ジョブの中に`AdInsightsMMM`レポートが含まれているか、またそのデータがビジネス上の重要な分析や意思決定に利用されているかを確認してください。
2.  **代替手段の検討**: `AdInsightsMMM`レポートのデータが継続的に必要な場合は、Facebook Ads APIから直接データを取得し、Cloud FunctionsやDataflowなどのカスタムETL（Extract, Transform, Load）プロセスを構築してBigQueryにロードする代替手段の検討が必要です。
3.  **公式アナウンスの監視**: Google CloudおよびFacebook Adsの公式ドキュメントやリリースノートを定期的に確認し、`AdInsightsMMM`レポートのサポート再開時期や恒久的な対応策に関する情報が公開されていないか監視してください。特にリリースノートに記載されている「July 06, 2026」のリンク先で、この変更に関する詳細情報や進捗が公開される可能性があります。

**用語説明:**
*   **BigQuery Data Transfer Service (BigQuery DTS)**: Google Cloudのフルマネージドサービスで、SaaSアプリケーション（例: Facebook Ads, Google Ads）や外部のデータソースからBigQueryへデータを自動的にロードおよび同期する機能を提供します。
*   **Facebook Ads API**: Facebook広告プラットフォームの機能にプログラムからアクセスするためのAPI（Application Programming Interface）です。広告キャンペーンの管理、広告効果のレポート生成、オーディエンスデータの取得などが可能です。
*   **`AdInsightsMMM` Report**: Facebook Ads APIを通じて提供される広告インサイトレポートの一種で、特定の目的（例: メディアミックスモデリング - Media Mix Modeling）のための集計データや詳細データが含まれる可能性があります。
*   **スキーマ変更 (Schema Change)**: データベースやAPIのデータ構造（例: テーブルの列、データ型、JSONのフィールド名や構造）が変更されることです。既存のデータ処理プログラムが変更されたスキーマに対応できない場合、エラーやデータ欠損が発生することがあります。