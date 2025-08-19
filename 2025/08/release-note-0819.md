
# Title: August 15, 2025 
Link: https://cloud.google.com/release-notes#August_15_2025<br>
# Cloud SQL for PostgreSQL
## Deprecated
原文: You can no longer set a deny maintenance period for instances that are running a maintenance version older than 12 months. To update your instance, perform self-service maintenance or wait until the next maintenance window to update your instance automatically. For more information about maintenance, see Maintenance updates on Cloud SQL instances.

説明：Cloud SQL for PostgreSQLにおいて、12ヶ月以上前のメンテナンスバージョンで動作しているインスタンスに対し、ユーザーがメンテナンス拒否期間（deny maintenance period）を設定する機能が廃止されました。この変更により、古いメンテナンスバージョンのインスタンスは強制的にメンテナンスが実施されるようになり、最新の状態に保たれることが促進されます。インスタンスを更新するためには、自己サービスメンテナンスを実行するか、次回のメンテナンスウィンドウでの自動更新を待つ必要があります。

影響有無：**影響は低い**。
理由：ご利用中のGoogle Cloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3) は、そのバックエンドデータベースとしてCloud SQL for PostgreSQLを利用する可能性があります。しかし、このCloud SQLインスタンスはGoogle Cloudによって管理されており、ユーザーが直接メンテナンス拒否期間 (`deny maintenance period`) を設定する運用は通常想定されていません。したがって、この機能の廃止が直接的な運用に影響を与えることはありません。Google CloudはComposerサービス全体のSLAを維持するために、バックエンドのCloud SQLインスタンスも適切に管理・メンテナンスしています。

対処方法：現在のところ、お客様側での直接的な対処は不要です。Cloud Composer2のバックエンドCloud SQLインスタンスのメンテナンスはGoogle Cloudが責任を持って実施します。

用語説明：
*   **メンテナンスバージョン**: Cloud SQLインスタンスに適用される、基盤となるデータベースソフトウェア（PostgreSQL）のマイナーバージョン、オペレーティングシステム、セキュリティパッチなどのバージョンを指します。
*   **メンテナンス拒否期間 (Deny Maintenance Period)**: Cloud SQLのユーザーが、特定の期間（例：繁忙期など）にメンテナンス作業が実行されないように設定できる機能です。これにより、ワークロードへの影響を最小限に抑えることができます。
*   **自己サービスメンテナンス (Self-service maintenance)**: ユーザーが任意のタイミングでCloud SQLインスタンスのメンテナンスアップデートを手動で開始できる機能です。計画的なダウンタイムを柔軟に管理したい場合に利用されます。