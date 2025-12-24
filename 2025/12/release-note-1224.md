
# Title: December 23, 2025 
Link: https://docs.cloud.google.com/release-notes#December_23_2025<br>
## Apigee X
### Announcement
**原文:**
On December 23, 2025, we released an updated version of Apigee.

Note: Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

**説明:**
2025年12月23日にApigeeの更新バージョンがリリースされました。ただし、ロールアウトは本日から開始されており、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる可能性があります。ロールアウトが完了するまで、Apigeeのインスタンスでは新機能や修正が利用できない場合があります。

**影響有無:**
**影響はありません。**
リリースノートの日付「December 23, 2025」は未来の日付であり、通常リリースノートには直近のリリース情報が記載されることから、日付の誤植である可能性が高いです。また、「Rollouts of this release began today」とあるため、もしこのリリースが本日行われているとしても、具体的な更新内容（機能追加、変更、削除、セキュリティ、パフォーマンス、料金体系など）が本リリースノートからは不明なため、現時点での直接的な影響は評価できません。Apigee Xをご利用の場合、今後詳細なリリース内容が発表されるまで、現状のサービス運用への影響はありません。

**対処方法:**
*   現時点では、具体的な変更内容が不明なため、特別な対処は不要です。
*   Apigee Xをご利用の場合は、今後公開される詳細なリリースノートやアップデート情報を継続的に確認し、新機能や変更点が既存の構成に影響を与える可能性がある場合に備えて、評価計画を立てることを推奨します。

**用語説明:**
*   **Apigee X:** Google Cloudが提供するAPI管理プラットフォームの最新バージョン。APIの設計、開発、セキュリティ、モニタリング、収益化など、APIライフサイクル全体を管理するための機能を提供します。
*   **ロールアウト (Rollout):** 新しいソフトウェアバージョンや機能が段階的に導入され、利用可能になるプロセスを指します。これにより、変更による影響を最小限に抑えつつ、安定した導入が可能になります。
*   **インスタンス (Instance):** 特定のApigee環境やデプロイメントの単位を指します。

## Cloud Composer
### Issue
**原文:**
Environments with Cloud Composer 2 versions 2.16.0 and 2.16.1 might experience a known issue with the reporting of metrics. You can observe a few skipped data points in the reported metrics and see error messages about the airflow-monitoring pod restarts in the environment logs.

[known issue](https://docs.cloud.google.com/composer/docs/composer-2/known-issues#missing-data-points)

This issue doesn't affect the environment's functionality. The environment is still operational and the environment health and monitoring information is reported correctly. You can ignore the error messages.

**説明:**
Cloud Composer 2のバージョン2.16.0および2.16.1を使用している環境で、メトリクスレポートに既知の問題が発生する可能性があります。具体的には、レポートされるメトリクスで一部のデータポイントがスキップされたり、環境ログに`airflow-monitoring` Podの再起動に関するエラーメッセージが表示されたりすることがあります。
この問題は、環境の機能には影響を与えません。環境は引き続き正常に動作し、環境の健全性や監視情報は正しくレポートされます。表示されるエラーメッセージは無視しても問題ありません。

**影響有無:**
**影響はありません。**
現在のCloud Composerのバージョンが`2.7.1`であるため、このリリースノートで述べられている既知の問題の対象バージョン（`2.16.0`および`2.16.1`）には該当しません。
仮に、対象バージョンを使用していた場合でも、この問題はメトリクスのレポートの一部欠損とログのエラー表示に限定されており、環境の機能自体やAirflowのワークフロー実行には影響がないと明記されています。

**対処方法:**
*   現在のCloud Composerのバージョンが対象外であるため、特別な対処は不要です。
*   将来的にバージョンアップを検討する際には、この既知の問題が修正されたバージョンを選択することをお勧めします。

**用語説明:**
*   **Cloud Composer:** Google Cloud上でフルマネージドなApache Airflow環境を提供するサービスです。ワークフローのオーケストレーションとスケジューリングを容易にします。
*   **Airflow:** プログラマブルにワークフローを定義、スケジュール、監視するためのプラットフォームです。Cloud ComposerはAirflowをベースにしています。
*   **メトリクス (Metrics):** システムのパフォーマンスや健全性を示す数値データです。CPU使用率、メモリ使用量、ディスクI/O、ネットワークトラフィックなどが含まれます。
*   **Pod (ポッド):** Kubernetesにおける最小のデプロイ可能なコンピューティング単位です。1つまたは複数のコンテナ（この場合は`airflow-monitoring`コンテナ）をグループ化して、ストレージやネットワークリソースを共有します。
*   **Operational (オペレーショナル):** システムやサービスが正常に稼働しており、期待される機能を提供している状態を指します。
*   **Environment Health:** Cloud Composer環境全体の健全性を示す情報で、各コンポーネントの状態やリソース利用状況などを含みます。