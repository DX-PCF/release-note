
# Title: October 06, 2025 
Link: https://cloud.google.com/release-notes#October_06_2025<br>
# BigQuery
## Announcement
原文:
Starting March 17, 2026, the BigQuery Data Transfer Service will require the
`bigquery.datasets.setIamPolicy` and the `bigquery.datasets.getIamPolicy`
permissions on the target dataset to create or update a transfer configuration.
For more information, see Changes to dataset-level access controls.

[Changes to dataset-level access controls](https://cloud.google.com/bigquery/docs/dataset-access-control)

説明:
2026年3月17日より、BigQuery Data Transfer Service (BQ DTS) を利用して転送設定（transfer configuration）を新規作成または既存の転送設定を更新する際に、対象となるターゲットデータセットに対して `bigquery.datasets.setIamPolicy` および `bigquery.datasets.getIamPolicy` のIAM権限が必要となります。これは、データセットレベルのアクセス制御の変更の一環として導入されるもので、より厳格な権限管理が求められるようになります。

影響有無:
**影響あり**。
現在BigQuery Data Transfer Serviceを利用してデータ転送を行っている場合、または将来的に利用を計画している場合に影響があります。
特に、2026年3月17日以降に既存の転送設定を更新しようとしたり、新しい転送設定を作成しようとしたりする際、BigQuery Data Transfer Serviceを実行するサービスアカウントやユーザーに上記の権限が付与されていないと、操作が失敗します。猶予期間が設けられていますが、事前に対処が必要です。

対処方法:
1.  **権限の確認**: 現在BigQuery Data Transfer Serviceで使用しているサービスアカウント、または転送設定の作成・更新を行うユーザーに対して、転送先のターゲットデータセットに対するIAM権限を確認してください。
2.  **権限の付与**: もし `bigquery.datasets.setIamPolicy` および `bigquery.datasets.getIamPolicy` 権限が付与されていない場合、2026年3月17日までにこれらの権限を追加してください。
    *   これらの権限を含むロールとしては、`roles/bigquery.dataOwner` や `roles/bigquery.admin` などがありますが、最小権限の原則に従い、カスタムロールで必要な権限のみを付与することも検討してください。
3.  **ドキュメント参照**: 詳細は、参照先のドキュメント「[Changes to dataset-level access controls](https://cloud.google.com/bigquery/docs/dataset-access-control)」を確認し、推奨される権限設定ガイドラインに従ってください。

用語説明:
*   **BigQuery Data Transfer Service (BQ DTS)**: 外部SaaSアプリケーション、クラウドストレージ、または他のGoogle CloudサービスからBigQueryへのデータの自動的なロードを管理するサービスです。
*   **転送設定 (transfer configuration)**: BigQuery Data Transfer Serviceにおいて、データ転送元、転送先（ターゲットデータセット）、スケジュール、およびその他の設定を定義するオブジェクトです。
*   **`bigquery.datasets.setIamPolicy`**: 指定されたBigQueryデータセットのIAMポリシーを設定（変更）する権限です。
*   **`bigquery.datasets.getIamPolicy`**: 指定されたBigQueryデータセットのIAMポリシーを取得（参照）する権限です。
*   **IAM (Identity and Access Management)**: Google Cloudリソースへのアクセスをきめ細かく制御するための認証・認可システムです。IAMポリシーは「誰が（プリンシパル）」「どのリソースに対して」「何ができるか（ロール/権限）」を定義します。