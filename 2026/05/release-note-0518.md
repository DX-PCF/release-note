
# Title: May 14, 2026 
Link: https://docs.cloud.google.com/release-notes#May_14_2026<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、構築済みのサービスへの影響有無を調査し、簡潔に回答いたします。

---

# BigQuery
## Issue
原文: Support for the `AI.KEY_DRIVERS` function preview has been temporarily disabled. We are working to restore this feature as soon as possible.
説明: BigQuery MLで提供されていた `AI.KEY_DRIVERS` 関数（プレビュー機能）のサポートが一時的に停止されました。Google社はこの機能の早期復旧に向けて対応を進めています。
影響有無:
*   **影響あり**: 当社のワークロードで `AI.KEY_DRIVERS` 関数を現在利用している場合、一時的にこの関数が利用できなくなり、関連する処理が停止または失敗します。
*   **影響なし**: 当社のワークロードでこの関数を現在利用していない場合、影響はありません。
対処方法:
`AI.KEY_DRIVERS` 関数を利用している場合は、機能が復旧するまで、当該機能に依存するワークロードの実行を一時的に停止するか、代替の分析手段を検討してください。本機能はプレビュー段階のため、本番環境での利用は通常推奨されません。
用語説明:
*   **BigQuery ML**: BigQuery上でSQLクエリを使用して機械学習モデルを作成・実行できる機能です。データの前処理からモデルのトレーニング、評価、デプロイまでをBigQuery内で完結させることができます。
*   **`AI.KEY_DRIVERS` function**: BigQuery MLの機能の一つで、特定のターゲット変数の変化に最も影響を与えた要因（キーインサイト）を特定するために使用される関数です。主に予測分析の結果の解釈に役立ちます。
*   **preview (プレビュー)**: Google Cloudの製品や機能が一般公開（GA: General Availability）される前に、顧客がテストや評価のために利用できる状態を示すものです。プレビュー機能は変更される可能性があり、本番環境での利用は推奨されない場合があります。

---

# Cloud Composer
## Issue
原文: The `google-api-core` preinstalled package versions from 2.28.0 to 2.30.2 might cause degraded environment performance, which can result in longer times to execute a task and longer times to move a task from the queued to the executing state.
Affected Managed Airflow (Gen 3) builds:
- composer-3-airflow-3.1.7-build.0 to composer-3-airflow-3.1.7-build.5
- composer-3-airflow-3.1.0-build.5 to composer-3-airflow-3.1.0-build.10
- composer-3-airflow-2.11.1-build.0
- composer-3-airflow-2.10.5-build.22 to composer-3-airflow-2.10.5-build.33
- composer-3-airflow-2.9.3-build.42 to composer-3-airflow-2.9.3-build.53
Affected Managed Airflow (Gen 2) builds:
- composer-2.16.10-airflow-2.11.1
- composer-2.16.0-airflow-2.10.5 to composer-2.16.10-airflow-2.10.5
- composer-2.16.0-airflow-2.9.3 to composer-2.16.10-airflow-2.9.3
We recommend to upgrade your environment to the following versions, which contain a version of the package where the problem is fixed or isn't present:
- composer-3-airflow-3.1.7-build.7 and later
- composer-3-airflow-2.11.1-build.3 and later
- composer-3-airflow-2.10.5-build.36 and later
- composer-3-airflow-2.9.3-build.54 (contains 2.27.0)
- composer-2.17.0-airflow-2.11.1 and later
- composer-2.17.0-airflow-2.10.5 and later
- composer-2.16.11-airflow-2.11.1 (contains 2.27.0)
- composer-2.16.11-airflow-2.10.5 (contains 2.27.0)
- composer-2.16.11-airflow-2.9.3 (contains 2.27.0)
As a workaround, you can manually install a later version of the `google-api-core` package to an affected environment by specifying `>=2.30.3` as the required version.
説明: Cloud Composer環境にプリインストールされている `google-api-core` パッケージのバージョン 2.28.0 から 2.30.2 に、パフォーマンス低下を引き起こす既知の問題が確認されています。この問題により、Airflowタスクの実行時間が長くなったり、タスクがキューから実行状態へ移行するまでの時間が長くなる可能性があります。影響を受けるComposer (Gen 2およびGen 3) およびAirflowのビルドバージョンが具体的に示されており、問題が修正された新しいバージョンへのアップグレードが推奨されています。一時的な回避策として、`google-api-core` パッケージを手動でバージョン 2.30.3 以降にアップグレードする方法も提供されています。
影響有無:
*   **影響なし**: 当社のCloud Composerバージョンは `Composer 2.7.1, Airflow 2.7.3` です。リリースノートに記載されている影響を受けるManaged Airflow (Gen 2) ビルドの対象バージョンは `composer-2.16.x` と `Airflow 2.9.x, 2.10.x, 2.11.x` であり、当社のバージョンはこの範囲に含まれていないため、直接的な影響はありません。
対処方法:
現状、当社のComposer環境は影響範囲外と判断されるため、特に追加の対処は不要です。ただし、将来Composerのバージョンアップを検討する際には、この問題が解決されているバージョンを選択することを確認してください。
用語説明:
*   **Cloud Composer**: Google Cloud上でApache Airflowをマネージドサービスとして実行するためのプラットフォームです。ワークフローのオーケストレーション、スケジュールされたジョブの管理などに利用されます。
*   **`google-api-core`**: Google CloudのPythonクライアントライブラリ群の基盤となるパッケージです。多くのGoogle CloudサービスとPythonアプリケーション間の連携において中心的な役割を果たします。
*   **Airflow Task**: Apache Airflowのワークフロー（DAG: Directed Acyclic Graph）における最小の実行単位です。各タスクは特定の処理を実行します。

---

# Google Kubernetes Engine
## Change
原文: Container-Optimized OS (COS) milestone 129 and higher no longer include the `kubectl` binary in the `/usr/bin/` directory.
説明: Google Kubernetes Engine (GKE) のノードOSとして使用されるContainer-Optimized OS (COS) のマイルストーン129以降のバージョンでは、`/usr/bin/` ディレクトリに `kubectl` バイナリがデフォルトで含まれなくなりました。
影響有無:
*   **影響なし**: 通常、GKEクラスタの管理や操作は、開発者のローカル環境やCI/CDパイプライン、Cloud Shellなど、クラスタ外部から `kubectl` を実行することが一般的です。そのため、GKEノード上で直接 `kubectl` コマンドを使用することは稀であり、ほとんどの場合、直接的な影響はありません。
*   **影響あり**: 仮に、特定のカスタムスクリプトやアプリケーションがGKEノードの `/usr/bin/` パスに存在する `kubectl` バイナリに依存して実行されている場合、そのスクリプトやアプリケーションが正常に動作しなくなる可能性があります。
対処方法:
GKEノード上で `kubectl` バイナリが必要となる特殊なユースケースがある場合は、以下のいずれかの対応を検討してください。
1.  ノードの起動スクリプトやDaemonSetなどを用いて、必要に応じて `kubectl` バイナリをノードにインストールし、適切なパスに配置する。
2.  `kubectl` の利用をノードの外部（開発者ワークステーション、Cloud Shell、CI/CDツールなど）に限定し、ノード内部からの `kubectl` 利用を避ける運用に切り替える。
一般的なGKE運用においては、この変更による対応は不要なケースがほとんどです。
用語説明:
*   **Container-Optimized OS (COS)**: Googleが開発・提供する、コンテナ実行に特化し、セキュリティと信頼性を重視した軽量なオペレーティングシステムです。GKEノードのデフォルトOSイメージとして利用されます。
*   **`kubectl`**: Kubernetesクラスタをコマンドラインから操作するための公式ツールです。Podのデプロイ、サービスの公開、クラスタ情報の取得など、Kubernetesのあらゆる操作を行います。

---

# Spanner
## Announcement
原文: The Spanner change streams default retention period has been increased from 1 day to 7 days. This change affects both new and existing change streams that don't have a retention period explicitly set. You can always specify the retention period through create change stream or alter change stream DDL statements to override the default.
説明: Cloud Spannerの変更ストリーム機能において、変更データ（イベント）のデフォルト保持期間が、従来の1日から7日に延長されました。この変更は、保持期間が明示的に設定されていない新規作成される変更ストリームだけでなく、既存の変更ストリームにも自動的に適用されます。特定の保持期間を設定したい場合は、`CREATE CHANGE STREAM` または `ALTER CHANGE STREAM` DDLステートメントを使用して明示的に期間を指定することで、この新しいデフォルト設定を上書きすることが可能です。
影響有無:
*   **プラスの影響**:
    *   変更ストリームのデータ保持期間が長くなるため、より長期間の変更履歴が利用可能となり、データ監査、障害復旧時のデータ整合性チェック、リアルタイムデータ連携における過去データの再処理などの柔軟性が向上します。
    *   短期間の停止や遅延が発生しても、変更ストリームのデータがすぐに消える心配が減ります。
*   **マイナスの影響**:
    *   保持期間の延長に伴い、変更ストリームに起因するストレージ消費量が増加する可能性があります。これにより、Spannerのストレージ料金が増加する可能性があります。
    *   特に、変更頻度の高いテーブルに対して変更ストリームを有効にしている場合、ストレージコストへの影響が大きくなる可能性があります。
対処方法:
現在Spannerの変更ストリームを使用しており、ストレージコストの増加を懸念する場合、または特定の保持期間（例えば1日）を維持したい場合は、以下の対応を検討してください。
1.  **既存の変更ストリームの確認**: 現在利用している変更ストリームの保持期間が明示的に設定されているかを確認します。設定されていない場合、自動的に7日に延長されています。
2.  **保持期間の明示的な設定**: ストレージコストを管理したい場合や、アプリケーションの要件で特定の保持期間が必要な場合は、以下のDDLステートメントを使用して、変更ストリームの保持期間を明示的に設定し直してください。
    *   例 (1日に設定し直す場合):
        ```sql
        ALTER CHANGE STREAM my_change_stream SET OPTIONS (retention_period = "1d");
        ```
3.  **新規作成時の考慮**: 今後新しく変更ストリームを作成する際は、デフォルトの7日間の保持期間で問題ないか、または特定の期間を設定する必要があるかを考慮し、必要に応じて `CREATE CHANGE STREAM` ステートメントで `retention_period` オプションを明示的に指定してください。
用語説明:
*   **Cloud Spanner**: Google Cloudが提供する、リレーショナルデータベースの特性とグローバルな分散スケーラビリティ、高可用性を兼ね備えたマネージドデータベースサービスです。
*   **変更ストリーム (Change Streams)**: Spannerデータベース内で発生するデータ変更（挿入、更新、削除）をほぼリアルタイムでキャプチャし、その変更イベントをPub/Subなどの別のサービスへストリーミングするための機能です。データ同期、リアルタイム分析、データ監査などに利用されます。
*   **DDL (Data Definition Language)**: データベースの構造（スキーマ）を定義・変更するためのSQL言語の一部です。`CREATE TABLE` や `ALTER TABLE` などが含まれます。ここでは、変更ストリームの作成や変更を行うための構文を指します。