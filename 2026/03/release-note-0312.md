
# Title: March 10, 2026 
Link: https://docs.cloud.google.com/release-notes#March_10_2026<br>
Google Cloud のインフラエンジニアとして、提供されたリリースノートに基づき、構築済みのサービスへの影響有無を調査し、以下に回答します。

---

# Cloud Composer

## Announcement

原文: Cloud Composer 2 environments can no longer be created in Turin (europe-west12). We're switching this region to supporting only Cloud Composer 3 environments.

説明：
Turin (europe-west12) リージョンにおいて、Cloud Composer 2 環境の新規作成が不可能になります。今後は、このリージョンではCloud Composer 3 環境のみがサポートされるようになります。この変更は、当該リージョンにおける将来的なComposer環境のデプロイ戦略に影響を与えます。

影響有無：
**直接的な影響は無し。**
現在ご利用のCloud Composer 2 (Compoer version 2.7.1、Airflow version 2.7.3) 環境がTurin (europe-west12) リージョンに存在する場合でも、既存の環境の運用（実行中のワークフローやデータパイプライン）には直接的な影響はありません。
ただし、将来的にTurin (europe-west12) リージョンでCloud Composer 2環境を新規構築または追加構築する計画がある場合は、当該リージョンでの新規作成が不可能となるため、計画に影響が生じます。

対処方法：
現在運用中のCloud Composer 2環境がTurin (europe-west12) リージョンにない場合、特に対処は不要です。
将来的にTurin (europe-west12) リージョンでCloud Composer環境を新規作成する予定がある場合は、以下のいずれかの対応をご検討ください。

*   **Cloud Composer 3への移行または新規導入の検討**:
    *   Turin (europe-west12) リージョンで新しいComposer環境をデプロイする必要がある場合は、Cloud Composer 3の利用を検討してください。Cloud Composer 3は、Composer 2と比較して基盤となるインフラストラクチャが刷新されており、スケーラビリティ、パフォーマンス、コスト効率の向上が期待されます。
    *   参考ドキュメント: [Cloud Composer 3 の概要](https://cloud.google.com/composer/docs/composer-3/composer-3-overview?hl=ja)
*   **他のサポート対象リージョンの選択**:
    *   引き続きCloud Composer 2環境を新規作成する必要がある場合は、Turin (europe-west12) 以外のCloud Composer 2がサポートされているリージョンを選択してください。
    *   参考ドキュメント: [Cloud Composer のロケーション](https://cloud.google.com/composer/docs/concepts/locations?hl=ja)

用語説明：
*   **Cloud Composer**: Google Cloud が提供する Apache Airflow のフルマネージドサービスです。ユーザーはインフラストラクチャの管理を気にすることなく、データパイプラインやワークフローを効率的にオーケストレーションできます。
*   **Apache Airflow**: プログラムによってワークフローをオーサリング、スケジューリング、監視するためのオープンソースプラットフォームです。主にデータ処理ワークフローのETL（抽出、変換、ロード）に利用されます。
*   **リージョン (Region)**: Google Cloud の物理的なデータセンターの集合体であり、リソースがデプロイされる特定の地理的場所です。`europe-west12` はイタリアのTurinを指すGoogle Cloudのリージョンコードです。
*   **Cloud Composer 2 / Cloud Composer 3**: Cloud Composer のメジャーバージョンです。Composer 3は、Composer 2と比較して基盤となるアーキテクチャが異なり、特にGKE Autopilotの利用やGoogle Cloud Storage FUSEによるパフォーマンス向上が図られています。