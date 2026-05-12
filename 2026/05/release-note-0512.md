
# Title: May 11, 2026 
Link: https://docs.cloud.google.com/release-notes#May_11_2026<br>
# AlloyDB for PostgreSQL
## Announcement
原文: AlloyDB now offers extended support for clusters running major PostgreSQL versions that have reached their end-of-life (EOL) as defined by the PostgreSQL community. Extended support provides an additional three years of support after the end of regular support, giving you more time to plan and perform major version upgrades. For more information, see Extended support for AlloyDB for PostgreSQL.

[Extended support for AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/extended-support)

説明：
AlloyDB for PostgreSQLが、PostgreSQLコミュニティでEOL（End-of-Life）に達した主要なPostgreSQLバージョンのクラスターに対して、拡張サポートの提供を開始しました。この拡張サポートにより、通常のサポート終了後さらに3年間、サポートが継続されます。これにより、お客様はメジャーバージョンアップグレードの計画と実施に追加の時間を確保できるようになります。詳細については、提供されたドキュメントを参照してください。

影響有無：
*   **影響あり（ポジティブ）**: 既存のAlloyDBクラスターで、将来的にPostgreSQLのメジャーバージョンがEOLを迎える場合、通常のサポート終了後も3年間追加でサポートが提供されるようになるため、計画的なバージョンアップグレードが可能になります。これにより、サービス運用継続性に対するリスクが軽減され、システムの安定稼働に寄与します。
*   **ネガティブな影響はなし**: 新しいサポートオプションの追加であり、既存の機能や動作を変更するものではないため、既存のサービスに悪影響を与えることはありません。

対処方法：
*   **現在のところ不要**: 今回の発表は、新しいサポートポリシーに関するものであり、即座にシステム構成の変更やアクションが必要となるものではありません。
*   **将来の計画に考慮**: 現在または将来的にEOLを迎えるPostgreSQLバージョンを使用しているAlloyDBクラスターがある場合、この拡張サポートを考慮してメジャーバージョンアップグレードの計画を立てる際に、より柔軟なスケジュールを設定できることを認識しておくと良いでしょう。
*   **ドキュメントの確認**: 詳細はリンク先のドキュメントを参照し、拡張サポートの条件や料金体系（もしあれば）を理解しておくことを推奨します。

用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供するフルマネージドのPostgreSQL互換データベースサービスです。高可用性、パフォーマンス、スケーラビリティが特徴で、トランザクション処理とアナリティクスワークロードの両方に最適化されています。
*   **PostgreSQL EOL (End-of-Life)**: PostgreSQLコミュニティによって定義される、特定のバージョンのPostgreSQLが公式なサポート（バグ修正やセキュリティパッチの提供など）を終了する時点です。EOL後は、そのバージョンに対する公式なアップデートは提供されなくなります。
*   **メジャーバージョンアップグレード**: データベースソフトウェアの主要なバージョン番号の変更を伴うアップグレードです。例えば、PostgreSQL 14からPostgreSQL 15へのアップグレードなど。通常、新機能の追加や互換性のない変更が含まれる可能性があり、計画的な作業が必要です。
*   **拡張サポート (Extended Support)**: 製品の通常のサポート期間が終了した後も、一定期間（この場合は3年間）提供される追加のサポートです。これにより、ユーザーはより長い期間、安心してそのバージョンを使用し続けることができますが、通常は通常のサポートとは異なる条件や料金が適用される場合があります。
# Title: May 08, 2026 
Link: https://docs.cloud.google.com/release-notes#May_08_2026<br>
はい、承知いたしました。Google Cloudのリリースノートについて、製品・アナウンス単位で影響調査を行い、ご指定の形式で回答します。

---

# BigQuery

## Announcement

**原文:**
 Starting August 11, 2026, the billing label for the BigQuery Data Transfer
Service SKU will be updated from `goog-bq-feature-type: DATA_TRANSFER_SERVICE`
(uppercase) to `goog-bq-feature-type: data_transfer_service` (lowercase) to
provide a more unified and complete view of your costs. This update expands the
scope of the label to cover all costs associated with the BigQuery Data Transfer
Service, including data transfer orchestration, data load operations, and data
merge operations.

 To ensure uninterrupted cost visibility, update your billing exports,
dashboards, and reporting queries to include both these labels.

**説明:**
2026年8月11日より、BigQuery Data Transfer Service (BQ DTS) のSKU料金ラベルの表記が変更されるというアナウンスです。具体的には、`goog-bq-feature-type` というラベルキーの値が、現在の「`DATA_TRANSFER_SERVICE`」（大文字）から「`data_transfer_service`」（小文字）に更新されます。
この変更の目的は、BigQuery Data Transfer Serviceに関連する全ての費用（データ転送オーケストレーション、データロード操作、データマージ操作など）をより統一的かつ包括的に把握できるようにすることです。
ユーザーに対しては、コスト可視性を継続的に確保するために、既存の請求データのエクスポート設定、ダッシュボード、およびレポートクエリを、新しいラベル値も考慮するように更新することが推奨されています。

**影響有無:**
**あり**

*   **直接的なサービス動作への影響**: ありません。BigQuery Data Transfer Service自体の機能や動作には影響はありません。
*   **間接的な影響**: BigQueryの課金データをBilling Export等でBigQueryにエクスポートし、そのデータを使ってコスト分析を行っている場合、影響があります。
    *   既存のダッシュボードやレポートクエリが、特定のラベル値（特に`goog-bq-feature-type: DATA_TRANSFER_SERVICE`）をフィルタリング条件としている場合、2026年8月11日以降に発生する新しいラベル値の費用が正しく集計されなくなる可能性があります。
    *   この変更により、BigQuery Data Transfer Serviceに関連する費用（オーケストレーション、データロード、データマージ）が新しいラベルで計上されるようになるため、正確なコスト把握のためには対応が必須となります。

**対処方法:**
2026年8月11日までに、以下の対応を計画・実施してください。

1.  **影響範囲の特定**: 現在、BigQuery Data Transfer Serviceの費用を詳細に分析するために、Billing Exportデータを参照しているカスタムダッシュボード（例: Looker Studio (旧Data Portal)）や、BigQuery上でのSQLクエリによるレポートを特定します。
2.  **クエリ・レポートの修正**: 特定したダッシュボードやレポートクエリにおいて、`goog-bq-feature-type` ラベルの値を参照している箇所を修正します。
    *   **推奨される修正例**: 大文字・小文字両方のラベル値を含むようにフィルタリング条件を変更します。
        *   例: `WHERE labels.key = 'goog-bq-feature-type' AND labels.value IN ('DATA_TRANSFER_SERVICE', 'data_transfer_service')`
    *   より柔軟な対応として、大文字・小文字を区別しない比較を使用することも検討できます（ただし、パフォーマンスやインデックス利用に影響を与える可能性がないか確認が必要です）。
        *   例: `WHERE labels.key = 'goog-bq-feature-type' AND LOWER(labels.value) = 'data_transfer_service'`
3.  **テスト**: 修正後、テスト用のデータや過去のデータを用いて、新しいクエリやダッシュボードが意図した通りに動作し、全ての関連コストを正確に集計できることを確認します。

**用語説明:**
*   **BigQuery Data Transfer Service (BQ DTS)**: Google Cloudのサービスの一つで、様々なソース（Google Ads、Google Analytics、YouTube、Amazon S3など）からBigQueryへデータを自動的にロード・転送するためのサービスです。定期的なデータ転送のスケジュール設定や管理を行います。
*   **SKU (Stock Keeping Unit)**: 在庫管理単位を意味しますが、Google Cloudでは、サービスやリソースの種類に応じた課金項目を識別するための単位として用いられます。例えば、BigQueryのストレージ費用やクエリ費用などがSKUとして識別されます。
*   **Billing Label**: Google Cloudの課金データに付与されるメタデータの一種です。リソースやプロジェクトにユーザーが付与する通常の「ラベル」とは異なり、Billing Labelは特定の機能やサービスに関連する課金データにGoogle Cloud側で自動的に付与される情報です。これにより、詳細な費用分析が可能になります。
*   **Billing Export**: Google Cloudの課金データをBigQueryデータセットに自動的にエクスポートする機能です。これにより、ユーザーはBigQueryの強力なクエリ機能を使って、詳細な課金データを自由に分析し、カスタムレポートやダッシュボードを作成できます。
*   **Cost visibility**: 組織やプロジェクト内で、どのサービスがどれくらいの費用を消費しているかを明確に把握できる状態を指します。費用の透明性とも言われ、予算管理やコスト最適化において非常に重要です。