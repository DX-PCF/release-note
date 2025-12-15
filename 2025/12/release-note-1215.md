
# Title: December 12, 2025 
Link: https://docs.cloud.google.com/release-notes#December_12_2025<br>
Google Cloudのリリースノートに関する調査結果を以下に報告いたします。
現在の環境では、Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3) を利用していることを前提に調査を進めました。

---

# Cloud Composer

## Deprecated
原文: The following Cloud Composer versions and builds have reached their end of support period: composer-3-airflow-2.9.3-build.11, composer-2.10.1-*.
説明: Cloud Composer 3 の `composer-3-airflow-2.9.3-build.11` ビルドと、Cloud Composer 2 の `composer-2.10.1-*` シリーズのバージョンがサポート終了期間に達しました。これらのバージョンを使用している場合は、サポートが提供されなくなるため、より新しいバージョンへの移行を検討する必要があります。
影響有無: 影響なし
理由: 現在利用しているCloud Composerのバージョンは `composer-2.7.1` であり、サポート終了となったバージョン (`composer-3-airflow-2.9.3-build.11` および `composer-2.10.1-*`) には該当しません。
対処方法: 特になし。ただし、将来的に古いバージョンのCloud Composer環境を構築する際には、サポート終了済みのバージョンを選択しないよう注意が必要です。
用語説明:
*   **End of support period (サポート終了期間)**: 製品または特定のバージョンに対して、ベンダーからの技術サポート、セキュリティアップデート、バグ修正などの提供が終了する期間を指します。この期間を過ぎたバージョンは、潜在的なセキュリティリスクや機能不全のリスクが高まります。
*   **Cloud Composer versioning**: Cloud Composerは、`composer-M.m.p-airflow-A.a.b` の形式でバージョン管理されます。`M.m.p` はComposer環境のインフラストラクチャバージョン、`A.a.b` はAirflowのバージョンを示します。

## Changed
原文: New Airflow builds are available in Cloud Composer 3: composer-3-airflow-3.1.0-build.6, composer-3-airflow-2.10.5-build.23 (default), composer-3-airflow-2.9.3-build.43
説明: Cloud Composer 3 環境で利用可能な新しいAirflowビルドがリリースされました。具体的には、Airflow 3.1.0、2.10.5 (デフォルト)、2.9.3 を含むビルドが追加されています。
影響有無: 影響なし
理由: 現在利用しているのはCloud Composer 2環境であり、このアナウンスはCloud Composer 3に特化したものです。
対処方法: 特になし。将来的にCloud Composer 3への移行を検討する際には、これらの新しいAirflowバージョンを選択肢として考慮できます。
用語説明:
*   **Airflow builds**: Apache Airflowの特定バージョンとCloud Composerのインフラストラクチャが組み合わされた、Cloud Composer環境の実行イメージを指します。

## Fixed
原文: Fixed an issue where the Copy button on the DAG details page in the Airflow UI was copying incorrect content.
説明: Airflow UIのDAG詳細ページにある「コピー」ボタンが、誤ったコンテンツをコピーしてしまう不具合が修正されました。
影響有無: 限定的影響あり
理由: 現在利用しているAirflowバージョン (2.7.3) でこの問題が発生している場合、将来のバージョンアップグレードでこの修正が適用される可能性があります。ただし、このリリースノートではどのCloud Composerイメージバージョンから修正が適用されるか明記されていないため、現在の環境で直ちに影響があるわけではありません。現在の利用環境でこの事象に遭遇していない場合は、直接的な影響は軽微です。
対処方法: 現在の環境でこの不具合に遭遇している場合は、Cloud Composer環境のバージョンアップグレードを検討することで、修正が適用される可能性があります。
用語説明:
*   **DAG details page**: Apache AirflowのWeb UI上で、特定のDAG (Directed Acyclic Graph) の詳細情報（タスクの状態、ログ、コードなど）を表示するページです。
*   **Airflow UI**: Apache Airflowが提供する、DAGの管理、タスクの監視、ログの確認などを行うためのWebベースのユーザーインターフェースです。

## Changed
原文: New images are available in Cloud Composer 2: composer-2.16.1-airflow-2.10.5 (default), composer-2.16.1-airflow-2.9.3
説明: Cloud Composer 2 環境で利用可能な新しいイメージがリリースされました。`composer-2.16.1-airflow-2.10.5` がデフォルトとして提供され、`composer-2.16.1-airflow-2.9.3` も利用可能です。これらのイメージは、より新しいAirflowバージョンを含んでいます。
影響有無: 間接的な影響あり
理由: 現在利用しているCloud Composerのバージョンは `2.7.1` であり、リリースされた新しいイメージは `2.16.1` と、かなり新しいバージョンです。この変更は、現在の環境に直接的な影響を与えるものではありませんが、より新しいAirflowバージョンやComposerの改善が利用可能になったことを示します。現在のバージョンは古くなっているため、セキュリティや機能面での改善のためにアップグレードを検討するきっかけとなります。
対処方法: 将来的なCloud Composer環境のバージョンアップグレード計画において、これらの新しいイメージ（特にデフォルトとなっている `composer-2.16.1-airflow-2.10.5`）への移行を検討してください。アップグレード前には、DAGsやカスタムPythonパッケージの互換性テストを十分に行う必要があります。
用語説明:
*   **Cloud Composer images**: Cloud Composer環境を構築するために使用される、特定のCloud ComposerバージョンとAirflowバージョンの組み合わせを含む、事前構築済みの仮想マシンのイメージです。新しいイメージは、新機能、バグ修正、パフォーマンス改善、セキュリティパッチなどを含んでいます。

---

# Cloud Logging

## Changed
原文: The default setting for the time-range selector for the Logs Explorer is now five minutes. The previous default was one hour.
説明: Cloud LoggingのLogs Explorerにおいて、ログ表示のデフォルト時間範囲が1時間から5分に変更されました。
影響有無: 軽微な影響あり
理由: これはLogs ExplorerのUIにおけるデフォルト表示設定の変更であり、ログの収集、保存、クエリ機能自体には影響ありません。UIの使い勝手の一部変更であり、ユーザーは手動で時間範囲を調整できます。
対処方法: 特になし。ユーザーは新しいデフォルトに慣れる必要がありますが、必要に応じて時間範囲セレクターを調整することで、以前と同じようにログを閲覧できます。
用語説明:
*   **Logs Explorer**: Google Cloud LoggingのWeb UIの一部で、プロジェクト内のログエントリを検索、フィルタリング、表示するためのインタラクティブなインターフェースです。
*   **Time-range selector**: Logs Explorerなどのログ表示ツールで、表示するログエントリの時間範囲を指定するためのUIコンポーネントです。

---

# Compute Engine

## Issue
原文: Workloads on A4 VMs might experience interruptions due to a firmware issue for NVIDIA B200 GPUs. To help prevent the issue, we recommend resetting the GPUs on A4 VMs at least once every 60 days. For more information, see the known issue.
説明: NVIDIA B200 GPUを搭載したA4 VMインスタンスで実行されているワークロードが、ファームウェアの問題により中断する可能性があることが確認されました。この問題を回避するため、60日に一度以上の頻度でA4 VM上のGPUをリセットすることが推奨されています。
影響有無: 影響なし
理由: 現在のGoogle Cloud Composer環境は、A4 VMインスタンスやNVIDIA B200 GPUを使用していません。
対処方法: 特になし。もし将来的にA4 VMインスタンス（特にNVIDIA B200 GPU搭載のもの）を利用する予定がある場合は、この既知の問題と推奨される回避策（定期的なGPUリセット）を運用計画に含める必要があります。
用語説明:
*   **A4 VMs**: NVIDIA Tesla A100 GPUを搭載したCompute EngineのVMインスタンスタイプであり、機械学習やHPC (High Performance Computing) ワークロードに適しています。ただし、リリースノートではNVIDIA B200 GPUについて言及されており、これは新しい世代のGPUを指します。
*   **NVIDIA B200 GPUs**: NVIDIAの次世代GPUアーキテクチャであるBlackwellベースのGPUで、高い計算能力を持ち、特にAIワークロード向けに設計されています。
*   **Firmware issue (ファームウェアの問題)**: ハードウェアに組み込まれている低レベルのソフトウェア（ファームウェア）に起因する不具合です。これはハードウェアの動作に直接影響を与える可能性があります。