
# Title: November 24, 2025 
Link: https://docs.cloud.google.com/release-notes#November_24_2025<br>
# Cloud Composer

## Issue

原文:
We discovered an issue that might impact the reporting of metrics in the
following recently released Cloud Composer versions:

- composer-2.15.4-airflow-*
- composer-3-airflow-2.10.5-build.20
- composer-3-airflow-2.9.3-build.40
- composer-3-airflow-3.1.0-build.3

To prevent additional environments from being affected, we have disabled the
ability to upgrade existing environments to these versions and to create new
environments using these versions. If your environment is already using one of
these versions, you can continue to use it as usual. We are working to resolve
the issue for all currently affected environments.

説明：
Cloud Composerにおいて、一部の最新バージョン（`composer-2.15.4-airflow-*`、`composer-3-airflow-2.10.5-build.20`、`composer-3-airflow-2.9.3-build.40`、`composer-3-airflow-3.1.0-build.3`）で、メトリクスレポート機能に影響を及ぼす可能性のある問題が発見されました。

この問題の影響を拡大させないため、Google Cloudは、既存のComposer環境をこれらの問題のあるバージョンへアップグレードすること、およびこれらのバージョンを使用して新規環境を作成することを一時的に無効化しました。

すでにこれらのバージョンを使用している環境については、通常通り継続して使用できます。Google Cloudは現在、影響を受けているすべての環境に対して問題の解決に取り組んでいます。

影響有無：
影響なし。
当社のCloud Composer環境はバージョン `2.7.1` (Airflow version `2.7.3`) を利用しており、リリースノートに記載されている影響を受けるバージョン（`composer-2.15.4-airflow-*`、`composer-3-airflow-*`など）には含まれていません。したがって、直接的な機能への影響やメトリクスレポートの異常は発生していません。

対処方法：
現在のところ、特別な対処は不要です。
将来的にCloud Composer環境のバージョンアップグレードを計画する際は、本リリースノートで言及されている問題のあるバージョンを避け、Google Cloudが問題解決後に提供する安定した最新バージョンへのアップグレードを推奨します。最新のリリースノートを定期的に確認し、今後の修正パッチや安定版のリリースに注意してください。

用語説明：
*   **Cloud Composer**: Google Cloudが提供する、Apache Airflowをフルマネージドで利用できるサービスです。ワークフローのオーケストレーションやスケジューリングを容易にします。
*   **Apache Airflow**: プログラムによってワークフローをオーサリング、スケジューリング、監視するためのオープンソースプラットフォームです。データパイプラインやETL処理の管理によく利用されます。
*   **メトリクスレポート (Metrics Reporting)**: Cloud Composer環境やその上で動作するAirflowタスクのパフォーマンス、リソース使用量、実行状態などの各種測定データを収集し、可視化・監視のために報告する機能です。通常、Cloud Monitoringなどのサービスに送信され、環境の健全性や効率性を把握するために使用されます。
*   **環境のアップグレード (Environment Upgrade)**: Cloud Composer環境のComposerバージョンおよび対応するAirflowバージョンを新しいものに更新するプロセスです。新機能の利用やセキュリティパッチの適用などの目的で行われます。