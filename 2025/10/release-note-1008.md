
# Title: October 06, 2025 
Link: https://cloud.google.com/release-notes#October_06_2025<br>
# BigQuery
## Announcement
原文: Starting March 17, 2026, the BigQuery Data Transfer Service will require the `bigquery.datasets.setIamPolicy` and the `bigquery.datasets.getIamPolicy` permissions on the target dataset to create or update a transfer configuration. For more information, see [Changes to dataset-level access controls](https://cloud.google.com/bigquery/docs/dataset-access-control).

説明: 2026年3月17日以降、BigQuery Data Transfer Service (BQ DTS) を利用して転送設定を新規作成または更新する際に、ターゲットとなるBigQueryデータセットに対して `bigquery.datasets.setIamPolicy` および `bigquery.datasets.getIamPolicy` のIAM権限が必要となります。この変更は、データセットレベルのアクセス制御に関するものです。

影響有無: **将来的な影響あり**。
現在BQ DTSを利用しており、そのサービスアカウントやユーザーにターゲットデータセットに対する上記のIAM権限が明示的に付与されていない場合、2026年3月17日以降は転送設定の作成や更新ができなくなります。既存の転送設定の実行自体には直接影響はありませんが、更新が必要になった際に問題が発生する可能性があります。

対処方法:
1.  **既存のBQ DTS転送設定の確認**: 現在運用中のBQ DTS転送設定で使用されているサービスアカウントまたはユーザーを特定します。
2.  **IAM権限の確認**: 特定したサービスアカウントまたはユーザーが、転送先のターゲットデータセットに対して `bigquery.datasets.setIamPolicy` と `bigquery.datasets.getIamPolicy` の権限を保持しているかを確認します。これらの権限は、例えば `roles/bigquery.dataEditor` のような役割に含まれています。
3.  **権限の追加**: もし上記の権限が不足している場合、2026年3月17日までに、当該サービスアカウントまたはユーザーにターゲットデータセットに対するこれらの権限を付与する計画を立ててください。最小権限の原則に基づき、カスタムロールでこれらの権限のみを付与することも検討してください。
4.  **新規作成時の考慮**: 将来的に新しいBQ DTS転送設定を作成する際には、必ずこれらの権限が付与されていることを確認するプロセスを導入してください。

用語説明:
*   **BigQuery Data Transfer Service (BQ DTS)**: Google Cloud内外のさまざまなデータソース（Google Ads、YouTube、Cloud Storageなど）からBigQueryへデータを自動的にロード・管理するサービスです。
*   **IAM (Identity and Access Management)**: Google Cloudリソースへのアクセスをきめ細かく制御するための仕組みです。誰が（Principal）、どのリソースに対して（Resource）、どのような操作を（Role/Permission）行えるかを定義します。
*   **`bigquery.datasets.setIamPolicy`**: 指定されたデータセットのIAMポリシーを設定する権限です。これにより、データセットへのアクセス権限を変更できます。
*   **`bigquery.datasets.getIamPolicy`**: 指定されたデータセットのIAMポリシーを取得する権限です。データセットの現在のアクセス権限を確認するために必要です。
*   **ターゲットデータセット**: BigQuery Data Transfer Serviceによってデータが転送され、格納される最終的なBigQueryデータセットを指します。