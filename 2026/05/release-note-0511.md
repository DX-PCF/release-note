
# Title: May 08, 2026 
Link: https://docs.cloud.google.com/release-notes#May_08_2026<br>
# BigQuery
## Announcement
原文: Starting August 11, 2026, the billing label for the BigQuery Data Transfer Service SKU will be updated from `goog-bq-feature-type: DATA_TRANSFER_SERVICE` (uppercase) to `goog-bq-feature-type: data_transfer_service` (lowercase) to provide a more unified and complete view of your costs. This update expands the scope of the label to cover all costs associated with the BigQuery Data Transfer Service, including data transfer orchestration, data load operations, and data merge operations.

To ensure uninterrupted cost visibility, update your billing exports, dashboards, and reporting queries to include both these labels.

説明：
2026年8月11日より、BigQuery Data Transfer Service (BQ DTS) の課金ラベル（SKU billing label）が変更されます。具体的には、現在の`goog-bq-feature-type: DATA_TRANSFER_SERVICE`（大文字）から`goog-bq-feature-type: data_transfer_service`（小文字）へ更新されます。この変更は、BQ DTSに関連するデータ転送オーケストレーション、データロード操作、データマージ操作など、すべてのコストをより統一的かつ包括的に把握できるようにすることを目的としています。

このラベル変更により、既存の課金レポート、ダッシュボード、および費用分析用のクエリは、将来的に適切に機能しなくなる可能性があります。継続的なコストの可視性を確保するためには、変更日までに両方のラベル（新しい小文字と古い大文字）を対象に含めるようにシステムを更新する必要があります。

影響有無：
**影響あり（運用サービスへの直接影響はなし、コスト可視性への影響あり）**
現在、BigQuery Data Transfer Serviceを利用しており、その利用コストをCloud Billing Export経由でBigQueryにエクスポートし、カスタムダッシュボードやレポートツールなどで分析・監視している場合は影響があります。2026年8月11日以降、現在のラベル名のみでフィルタリングや集計を行っている場合、BigQuery Data Transfer Serviceのコストが正しく把握できなくなる可能性があります。
ただし、変更日が2026年8月11日とかなり先であるため、即座の対応は不要です。

対処方法：
2026年8月11日までに、以下の対応を計画・実行してください。
1.  **影響範囲の特定:** BigQuery Data Transfer Serviceのコストを分析・レポートするために、Cloud Billing Exportデータを使用しているすべてのカスタムダッシュボード、BIツール、スクリプト、およびBigQueryクエリを確認してください。
2.  **クエリ/フィルタの更新:** 該当するすべてのクエリやフィルタリング条件を更新し、新しい小文字のラベル (`goog-bq-feature-type: data_transfer_service`) と既存の大文字のラベル (`goog-bq-feature-type: DATA_TRANSFER_SERVICE`) の**両方**を対象に含めるように変更してください。これにより、ラベル変更前後で継続的にすべてのBQ DTS関連コストを追跡できるようになります。
    *   例: フィルタ条件を `WHERE labels."goog-bq-feature-type" IN ('DATA_TRANSFER_SERVICE', 'data_transfer_service')` のように修正します。
3.  **テスト:** 変更前に、テスト環境で新しいクエリやダッシュボードが正しく機能するかどうかを確認してください。

用語説明：
*   **BigQuery Data Transfer Service (BQ DTS):** BigQueryに対して、Google Ads、Google Play、YouTube Analyticsなど様々なSaaSアプリケーションや他のGoogle Cloudプロダクト（Amazon S3など含む）からデータを自動的にスケジュール転送するサービスです。
*   **SKU (Stock Keeping Unit):** 製品やサービスの最小課金単位を指します。Google Cloudの課金では、各リソース（例: VMのCPU時間、ストレージ容量）が特定のSKUに関連付けられています。
*   **Billing Label:** Google Cloudの課金データに付与できるキーバリューペアのタグです。リソースのコストを部門別、プロジェクト別、アプリケーション別などに分類・分析するために使用されます。Cloud Billing Export機能を通じてBigQueryなどにエクスポートされる詳細な課金データに含まれます。
*   **Cloud Billing Export:** Google Cloudの費用データをBigQueryなどのデータウェアハウスに定期的に自動エクスポートする機能です。これにより、ユーザーは独自のツールやクエリを使って詳細なコスト分析を行うことができます。