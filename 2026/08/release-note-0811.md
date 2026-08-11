
# Title: August 07, 2026 
Link: https://docs.cloud.google.com/release-notes#August_07_2026<br>
# Cloud SQL for PostgreSQL
## Change
原文: Newly created instances configured with high availability (HA) now have Knowledge Catalog (formerly Dataplex Universal Catalog) enabled by default. Cloud SQL for PostgreSQL instances running on PostgreSQL version 14.0 or later send updates and metadata to Knowledge Catalog in near real-time. You can either verify enablement or disable the feature using the Google Cloud console. For more information, see Near real-time.

説明:
高可用性 (HA) 構成で**新規作成される** Cloud SQL for PostgreSQL インスタンスにおいて、Knowledge Catalog (旧称 Dataplex Universal Catalog) との連携機能がデフォルトで有効になる変更です。
この変更により、PostgreSQL バージョン 14.0 以降で稼働する対象インスタンスは、データベースの更新やメタデータを Knowledge Catalog にほぼリアルタイムで送信するようになります。
この機能は Google Cloud Console から有効化されているかを確認したり、無効化したりすることが可能です。

影響有無:
**既存のサービスへの直接的な影響はありません。**
この変更は「新規作成される」インスタンスにのみ適用されるため、既存の Cloud SQL for PostgreSQL インスタンスの動作には影響しません。
ただし、今後高可用性 (HA) 構成の Cloud SQL for PostgreSQL インスタンス (PostgreSQL バージョン 14.0 以降) を新規作成する場合、Knowledge Catalog との連携がデフォルトで有効となるため、この機能を意図しない場合は考慮が必要です。

対処方法:
特別な対処は不要です。
今後、高可用性 (HA) 構成の Cloud SQL for PostgreSQL インスタンスを新規作成する際に、Knowledge Catalog との連携が不要な場合は、インスタンス作成時または作成後に Google Cloud Console から手動で無効化する設定を行ってください。

用語説明:
*   **High Availability (HA)**: 高可用性。システムの一部に障害が発生した場合でも、サービスの中断を最小限に抑え、継続して利用できるようにする設計や構成のことです。Cloud SQL では、フェイルオーバーインスタンスを自動的に用意することでHAを実現します。
*   **Knowledge Catalog (旧 Dataplex Universal Catalog)**: Google Cloud のデータ管理サービスである Dataplex の一部として提供される、データ資産のメタデータ管理機能です。データベースのテーブルやスキーマなどの情報をカタログ化し、データの発見性やガバナンスを向上させることを目的としています。
*   **Metadata**: データに関するデータのことです。例えば、データベースの文脈では、テーブル名、カラム名、データ型、インデックス、制約などの構造情報や、最終更新日時、所有者などの管理情報が含まれます。
*   **Dataplex**: Google Cloud におけるデータレイク、データウェアハウス、データマートなどの多様なデータソースを統合し、データガバナンス、管理、分析を容易にするための包括的なサービスです。