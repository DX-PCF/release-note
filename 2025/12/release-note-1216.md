
# Title: December 12, 2025 
Link: https://docs.cloud.google.com/release-notes#December_12_2025<br>
## Cloud Composer
### Deprecated
原文: The following Cloud Composer versions and builds have reached their end of support period: composer-3-airflow-2.9.3-build.11, composer-2.10.1-*.
説明: Cloud Composer 3の一部のビルド（`composer-3-airflow-2.9.3-build.11`）と、Cloud Composer 2の特定のバージョン（`composer-2.10.1-*`）がサポート終了期間に到達しました。これは、これらのバージョンに対するGoogle Cloudからの技術サポートやパッチ提供が終了したことを意味します。
影響有無: 直接的な影響はありません。現在利用されているCloud Composer環境は `composer-2.7.1` であり、サポート終了対象のバージョンには該当しません。
対処方法: なし。しかし、利用中のバージョンも将来的にサポート終了となるため、定期的なバージョンアップグレード計画を策定し、サポート期間が終了する前に新しいバージョンへの移行を検討することを推奨します。

### Changed
原文: New Airflow builds are available in Cloud Composer 3: composer-3-airflow-3.1.0-build.6, composer-3-airflow-2.10.5-build.23 (default), composer-3-airflow-2.9.3-build.43
説明: Cloud Composer 3向けに、新しいApache Airflowのビルドイメージがリリースされました。これには、Airflow 3.1.0、2.10.5（デフォルト）、2.9.3をベースとしたイメージが含まれます。
影響有無: 影響はありません。現在利用されている環境はCloud Composer 2であり、この変更はCloud Composer 3ユーザー向けです。
対処方法: なし。

### Fixed
原文: Fixed an issue where the Copy button on the DAG details page in the Airflow UI was copying incorrect content.
説明: Apache Airflow UIのDAG（Directed Acyclic Graph）詳細ページに表示される「Copy」ボタンが、誤った内容をクリップボードにコピーしてしまう不具合が修正されました。
影響有無: 間接的な影響がある可能性があります。現在利用中のAirflow 2.7.3環境でこの不具合が発生していた場合、新しいComposerイメージへのアップグレードによってこの修正が適用される可能性があります。
対処方法: 現在の環境で同様の不具合を経験している場合、後述のCloud Composer 2の新しいイメージへのアップグレードを検討してください。アップグレードにより、この修正が適用される可能性が高まります。

### Changed
原文: New images are available in Cloud Composer 2: composer-2.16.1-airflow-2.10.5 (default), composer-2.16.1-airflow-2.9.3
説明: Cloud Composer 2向けに、新しいバージョンの環境イメージがリリースされました。これには、`composer-2.16.1-airflow-2.10.5`（デフォルト）と `composer-2.16.1-airflow-2.9.3` が含まれます。これらのイメージは、基盤となるOS、Python、およびApache Airflowの新しいバージョンを含んでおり、機能強化、セキュリティパッチ、パフォーマンス改善などが期待されます。
影響有無: 直接的な影響はありません。既存の `composer-2.7.1` 環境は自動的にアップグレードされません。しかし、より新しいバージョンのCloud Composer 2環境が利用可能になったため、セキュリティ、安定性、および機能面でのメリットを享受するために、アップグレードを検討する価値があります。特に、Airflowバージョンが 2.7.3 から 2.10.5 へと大きく更新されるため、Apache Airflow自体の新機能や改善が利用可能になります。
対処方法: 新しいCloud Composer 2イメージへのアップグレードを強く推奨します。アップグレードを実行する前に、以下の手順を確実に実施してください。
1.  **互換性確認:** 現在のDAGsが新しいAirflowバージョン（特に2.10.5）と互換性があるかを検証します。Apache Airflowのメジャーバージョンアップは、後方互換性のない変更を含む場合があります。
2.  **テスト環境での検証:** 本番環境への適用前に、テスト環境で新しいイメージへのアップグレードとDAGの実行検証を徹底的に行います。
3.  **ドキュメント参照:** Google Cloud Composerの公式ドキュメントで、アップグレードパス、手順、および非互換性に関する情報を確認してください。
4.  **メンテナンスウィンドウの確保:** アップグレード作業中にサービス中断が発生する可能性を考慮し、適切なメンテナンスウィンドウを設定します。
用語説明:
*   **Cloud Composer Image:** Cloud Composer環境の基盤となるソフトウェアスタック（オペレーティングシステム、Python、Apache Airflow、およびその他の依存ライブラリ）をパッケージ化したものです。Google Cloudによって管理・提供され、環境の作成や更新時に使用されます。
*   **DAGs (Directed Acyclic Graphs):** Apache Airflowにおけるワークフロー定義のこと。タスクとその依存関係をPythonコードで表現します。

## Cloud Logging
### Changed
原文: The default setting for the time-range selector for the Logs Explorer is now five minutes. The previous default was one hour.
説明: Cloud LoggingのLogs Explorerにおいて、ログを表示する際のデフォルトの時間範囲セレクタが変更されました。これまでは過去1時間のログがデフォルトで表示されていましたが、今回の変更により過去5分間のログがデフォルトで表示されるようになります。
影響有無: 軽微な影響があります。これはユーザーインターフェースのデフォルト設定の変更であり、ログの収集、保存、またはクエリの機能に影響はありません。Logs Explorerで広範な期間のログを調査する際には、手動で時間範囲セレクタを調整する必要があります。
対処方法: なし。Logs Explorerを利用するオペレーションチームや開発者に対して、デフォルトの時間範囲が変更されたことを周知し、必要に応じて時間範囲を調整するよう促してください。

## Compute Engine
### Issue
原文: Workloads on A4 VMs might experience interruptions due to a firmware issue for NVIDIA B200 GPUs. To help prevent the issue, we recommend resetting the GPUs on A4 VMs at least once every 60 days. For more information, see the known issue.
説明: Compute EngineのA4 VMインスタンスにおいて、搭載されているNVIDIA B200 GPUのファームウェアに起因する問題により、ワークロードが中断される可能性があることが報告されました。この問題の発生を防ぐために、A4 VM上のGPUを少なくとも60日ごとにリセットすることが推奨されています。
影響有無: 現在のGoogle Cloud環境でA4 VM（特にNVIDIA B200 GPUを搭載したインスタンス）が利用されていない場合、影響はありません。もしA4 VM（NVIDIA B200 GPU搭載）が利用されている場合は、ワークロードが予期せず中断するリスクがあり、運用上の対応が必要となります。
対処方法:
1.  **環境確認:** 貴社のGoogle Cloud環境内でA4 VM（NVIDIA B200 GPU搭載）がデプロイされているかどうかを確認します。
2.  **運用プロセスの確立:** A4 VMが利用されている場合、GPUのリセット手順を公式ドキュメント（提供された「known issue」リンクを参照）で確認し、それを運用手順に組み込みます。定期的なメンテナンス計画（60日以内）にGPUリセットのタスクを含めることで、ワークロード中断のリスクを低減します。
3.  **ワークロードへの影響評価:** GPUリセットがワークロードに与える影響を評価し、必要に応じてメンテナンスウィンドウを設けるか、フェイルオーバー戦略を検討してください。
用語説明:
*   **A4 VM:** Google Cloud Compute Engineで提供される、NVIDIA社のGPUを搭載した仮想マシンインスタンスのファミリーです。主に機械学習（ML）トレーニング、推論、高性能コンピューティング（HPC）ワークロード向けに設計されています。
*   **NVIDIA B200 GPU:** NVIDIAが開発した、データセンター向け高性能GPUの一種です。特に大規模なAIモデルのトレーニングや推論に特化しており、高い計算能力とメモリ帯域幅を提供します。
*   **ファームウェア (Firmware):** ハードウェアデバイスを制御するために、そのデバイスの不揮発性メモリに組み込まれた低レベルのソフトウェアです。ハードウェアの基本的な機能や動作を定義します。