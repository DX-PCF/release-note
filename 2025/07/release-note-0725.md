
# Title: July 23, 2025 
Link: https://cloud.google.com/release-notes#July_23_2025<br>
# API Gateway
## Announcement
原文: On July 23, 2025, we released an updated version of API Gateway.
説明：2025年7月23日にAPI Gatewayのアップデート版がリリースされました。
影響有無：直接的な影響はありません。これは単なるリリース告知であり、具体的な機能変更や制約の追加を示すものではないためです。
対処方法：なし。

## Deprecated
原文: **Deprecation of Transport Layer Security (TLS) v1.0 and v1.1 protocols**
API Gateway now enforces TLS v1.2+. You can opt out of enforcing TLS v1.2+ for your API Gateway's new security settings by reaching out to Google Cloud Support to continue using your current protocol.
[Google Cloud Support](https://cloud.google.com/support)
説明：API Gatewayにおいて、セキュリティプロトコルであるTLS v1.0およびv1.1が非推奨となり、TLS v1.2以降が強制されるようになりました。もし現在のプロトコル（TLS v1.0またはv1.1）の使用を継続したい場合は、Google Cloudサポートに連絡することで、TLS v1.2+の強制を一時的にオプトアウトできます。
影響有無：**影響あり。**
API Gatewayを利用しているクライアント（APIを呼び出すアプリケーションなど）がTLS v1.2以上をサポートしていない場合、APIへの接続ができなくなる可能性があります。現在の環境でAPI Gatewayを利用するクライアントがTLS v1.0またはv1.1を使用しているか確認が必要です。
対処方法：
1.  **クライアント側の確認:** API Gatewayを利用している全てのクライアントがTLS v1.2以上に対応しているかを確認してください。
2.  **クライアントの更新:** TLS v1.2以上に対応していないクライアントが存在する場合、それらのクライアントのTLSバージョンをアップグレードしてください。
3.  **緊急時の対応:** クライアント側のアップグレードに時間がかかるなど、緊急で対応が必要な場合は、Google Cloudサポートに連絡し、一時的にTLS v1.2+の強制をオプトアウトすることを検討してください。ただし、これはセキュリティリスクを伴うため、速やかにクライアント側の対応を進めることを強く推奨します。
用語説明：
*   **TLS (Transport Layer Security)**: インターネットなどのネットワーク上でデータを安全にやり取りするための暗号化プロトコルです。ウェブサイトのHTTPS接続などで広く利用されています。
*   **TLS v1.0 / v1.1 / v1.2**: TLSプロトコルのバージョンです。v1.0やv1.1は古いバージョンであり、既知のセキュリティ脆弱性が存在するため、よりセキュアなv1.2以降への移行が推奨されています。

---

# AlloyDB for PostgreSQL
**注記**: 以下のリリースノートは「AlloyDB Omni」に関するものです。マネージドサービスのAlloyDB for PostgreSQLを利用している場合は、これらの変更は直接的な影響はありません。AlloyDB Omniを利用している前提で回答します。

## Announcement
原文: AlloyDB Omni version 16.8.0 is generally available (GA). Version 16.8.0 includes the following features and changes:
[AlloyDB Omni](https://cloud.google.com/alloydb/omni/current/docs)
[GA](https://cloud.google.com/products#product-launch-stages)
- AlloyDB Omni supports PostgreSQL version 16.8.
- AlloyDB Omni supports the `pg_squeeze` extension that addresses table bloat and improves data locality.
- You can set up the columnar engine storage cache on dedicated devices. For more information, see Configure the columnar engine in AlloyDB Omni.
- Improved I/O acceleration due to bug fixes in `libaio`.
- Active Directory authentication integration is generally available (GA), providing robust user authentication for your database clusters. For more information, see Integrate Active Directory with AlloyDB Omni.
- Active Directory group-based authorization is available in Preview, enabling granular permission management based on your Active Directory groups. For more information, see Integrate Active Directory group support with AlloyDB Omni.
説明：AlloyDB Omniのバージョン16.8.0がGA（一般提供）になりました。このバージョンでは、PostgreSQL 16.8のサポート、テーブルの肥大化解消とデータ局所性を改善する`pg_squeeze`拡張機能、専用デバイスでのカラムナーエンジンのストレージキャッシュ設定、`libaio`のバグ修正によるI/O高速化、Active Directory認証統合のGA、Active Directoryグループベース認可のプレビューなどの新機能と改善が含まれています。
影響有無：現在のAlloyDB Omni環境でバージョンアップを検討している場合、新機能の利用が可能になります。既存の構成に対する直接的な互換性問題の報告はありませんが、アップグレードパスや新機能の利用においては検証が必要です。
対処方法：
*   AlloyDB Omni 16.8.0へのアップグレードを検討し、新機能（特に`pg_squeeze`やActive Directory連携など）の利用が現在のワークロードや運用改善に役立つか評価してください。
*   アップグレードを行う際は、公式ドキュメントを参照し、適切な手順とテスト計画を立てて実施してください。
用語説明：
*   **AlloyDB Omni**: Google CloudのAlloyDBの機能性をオンプレミスや他のクラウド環境で利用可能にするソフトウェアです。
*   **GA (General Availability)**: 製品や機能が一般に公開され、本番環境での利用が推奨される状態であることを示します。
*   **`pg_squeeze`**: PostgreSQLの拡張機能の一つで、テーブルの肥大化（bloat）を解消し、データの物理的な配置を最適化することで、データベースのパフォーマンスを向上させます。
*   **カラムナーエンジン**: データを列ごとに格納し、分析クエリの処理性能を向上させるためのデータベースエンジンです。
*   **Active Directory (AD)**: Microsoftが提供するディレクトリサービスで、ネットワーク上のユーザーやコンピューターなどのリソースを一元的に管理します。

## Announcement
原文: AlloyDB Omni version 15.12.0 is generally available (GA). Version 15.12.0 includes the following features and changes:
[AlloyDB Omni](https://cloud.google.com/alloydb/omni/current/docs)
[GA](https://cloud.google.com/products#product-launch-stages)
- AlloyDB Omni supports PostgreSQL version 15.12.
- AlloyDB Omni supports the `pg_squeeze` extension that addresses table bloat and improves data locality.
- You can set up the columnar engine storage cache on dedicated devices. For more information, see Configure the columnar engine in AlloyDB Omni.
説明：AlloyDB Omniのバージョン15.12.0がGA（一般提供）になりました。このバージョンでは、PostgreSQL 15.12のサポート、テーブルの肥大化解消とデータ局所性を改善する`pg_squeeze`拡張機能、専用デバイスでのカラムナーエンジンのストレージキャッシュ設定などの新機能と改善が含まれています。
影響有無：現在のAlloyDB Omni環境でバージョンアップを検討している場合、新機能の利用が可能になります。既存の構成に対する直接的な互換性問題の報告はありませんが、アップグレードパスや新機能の利用においては検証が必要です。
対処方法：
*   AlloyDB Omni 15.12.0へのアップグレードを検討し、新機能の利用が現在のワークロードや運用改善に役立つか評価してください。
*   アップグレードを行う際は、公式ドキュメントを参照し、適切な手順とテスト計画を立てて実施してください。
用語説明：上記AlloyDB Omni 16.8.0のGAアナウンスと同様です。

## Announcement
原文: The AlloyDB Omni Kubernetes operator version 1.5.0 is generally available (GA) and includes the following features and bug fixes:
[AlloyDB Omni Kubernetes operator](/alloydb/omni/current/docs/deploy-kubernetes)
[GA](https://cloud.google.com/products#product-launch-stages)
- You can install the operator using the Operator Lifecycle Manager (OLM) for Kubernetes and OpenShift environments. See "Install the AlloyDB Omni operator" for AlloyDB Omni 15.12.0 and 16.8.0 for details.
- Low downtime, minor version upgrades for a database cluster in a high availability setup are available in Preview. For more information, see "Perform a minor database version upgrade for AlloyDB Omni on Kubernetes" in the documentation for AlloyDB Omni 15.12.0 and 16.8.0.
- Active Directory authentication integration on your Kubernetes-based AlloyDB Omni database cluster is generally available (GA). For more information, see Integrate Active Directory with AlloyDB Omni on Kubernetes.
- Active Directory group-based authorization on your Kubernetes-based AlloyDB Omni database cluster is available in Preview. For more information, see Integrate Active Directory group support on Kubernetes.
- You can configure backups to be taken directly from a standby Kubernetes cluster in a high availability (HA) setup to offload backup operations from your primary instance. See "Backup and restore in Kubernetes" for AlloyDB Omni 15.12.0 and 16.8.0 for details.
- The operator fully automatically replicates replication slots for cross-data-center replication to work with primary database clusters that have high availability (HA) enabled. You still need to make sure you have reliable and low latency network connectivity between the primary and secondary data centers, which is crucial for cross-data-center replication to function effectively. For more information, see "Work with cross-data-center replication" for AlloyDB Omni 15.12.0 and 16.8.0.
- AlloyDB Omni Kubernetes images are now built on Red Hat's Universal Base Image (UBI) 9. For more information, see "Install AlloyDB Omni on Kubernetes" for AlloyDB Omni 15.12.0 and 16.8.0.
- AlloyDB AI requires AlloyDB Omni version 15.5.5 or later.
説明：AlloyDB OmniのKubernetesオペレーターバージョン1.5.0がGA（一般提供）になりました。このバージョンでは、Operator Lifecycle Manager (OLM) を使用したインストール、高可用性(HA)構成での低ダウンタイムなマイナーバージョンアップグレード（プレビュー）、Kubernetes上でのActive Directory認証統合（GA）、ADグループベース認可（プレビュー）、スタンバイクラスタからのバックアップ取得設定、クロスデータセンターレプリケーションにおけるレプリケーションスロットの自動複製、Red Hat Universal Base Image (UBI) 9ベースのコンテナイメージへの変更などの機能強化とバグ修正が含まれます。
影響有無：AlloyDB OmniをKubernetes環境で運用している場合、オペレーターのバージョンアップグレードを検討する必要があるため、**影響あり**。新機能（特にHA構成でのアップグレード、AD連携、スタンバイからのバックアップ）は、運用改善やセキュリティ強化に寄与する可能性があります。ベースイメージがUBI 9に変更されたことで、セキュリティや互換性に関する考慮が必要となる場合があります。
対処方法：
*   AlloyDB OmniをKubernetes環境で運用している場合は、オペレーターのバージョン1.5.0へのアップグレードを検討してください。
*   アップグレード前に、新機能（特にHA構成でのアップグレードやActive Directory連携）の利用可否を評価し、計画に含めてください。
*   公式ドキュメントを参照し、アップグレードパスや手順（特に後述のIssueセクションで言及されているアップグレードパス）を注意深く確認してください。
*   ベースイメージの変更（UBI 9）による潜在的な影響がないか、必要に応じて確認してください。
用語説明：
*   **Kubernetes Operator**: Kubernetes上で複雑なアプリケーションのデプロイ、管理、スケーリング、アップグレードといった運用タスクを自動化するためのソフトウェアです。
*   **Operator Lifecycle Manager (OLM)**: Kubernetesオペレーターのインストール、アップグレード、アクセス管理を簡素化するツールです。
*   **HA (High Availability)**: 高可用性。システムが障害発生時にも継続して稼働し続ける能力を指します。
*   **Red Hat Universal Base Image (UBI)**: Red Hat Enterprise Linux (RHEL) のコンポーネントをベースにしたコンテナイメージで、誰でも自由に利用・再配布が可能です。

## Issue
原文: When upgrading your AlloyDB Omni database clusters, be aware of specific upgrade paths and prerequisites depending on your current `controlPlaneAgentsVersion` and environment:
- If your database cluster's `controlPlaneAgentsVersion` is `1.0.0`, you must first upgrade to `1.1.1` before you upgrade to `1.5.0` or higher. You can directly upgrade database clusters with `controlPlaneAgentsVersion` `1.1.0` or later to `1.5.0`.
- If you use an OpenShift database cluster that runs `controlPlaneAgentsVersion` `1.4.1` or earlier, you must run prerequisite steps before updating to `1.5.0`. For more information, see "Update OpenShift database clusters from version `1.4.1` or earlier" for AlloyDB Omni 15.12.0 and 16.8.0.
説明：AlloyDB Omniデータベースクラスターをアップグレードする際には、現在の`controlPlaneAgentsVersion`と実行環境（OpenShiftかどうか）に応じて、特定のアップグレードパスと前提条件があることに注意が必要です。例えば、`controlPlaneAgentsVersion`が`1.0.0`の場合は、まず`1.1.1`にアップグレードしてから`1.5.0`以上に進む必要があります。また、OpenShift環境で`controlPlaneAgentsVersion`が`1.4.1`以前の場合、`1.5.0`へアップデートする前に特定の事前準備ステップが必要です。
影響有無：AlloyDB Omniを運用しており、Kubernetesオペレーターバージョン1.5.0へのアップグレードを計画している場合、**影響あり**。現在の`controlPlaneAgentsVersion`を確認し、指定されたアップグレードパスと前提条件を遵守しないと、アップグレードが失敗したり、予期せぬ問題が発生する可能性があります。
対処方法：
1.  **現状の確認:** オペレーターのアップグレード前に、現在稼働しているAlloyDB Omniデータベースクラスターの`controlPlaneAgentsVersion`を確認してください。
2.  **公式ドキュメントの参照:** 現在のバージョンと環境に合った、AlloyDB Omni Kubernetesオペレーターの公式アップグレードガイドを参照してください。特にOpenShift環境の場合は、追加の事前準備ステップを確認してください。
3.  **計画的なアップグレード:** 正しいアップグレードパスに従い、必要な事前準備ステップを実行した上で、計画的にアップグレードを実施してください。
用語説明：
*   **`controlPlaneAgentsVersion`**: AlloyDB Omniの内部的なコントロールプレーンエージェントのバージョンを示す識別子です。このバージョンによって、アップグレードの互換性や手順が決定されます。
*   **OpenShift**: Red Hatが提供するKubernetesベースのエンタープライズ向けコンテナプラットフォームです。

---

# Cloud Composer
**現在の環境**: Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3)

## Announcement
原文: If your environment uses `dag-factory` package version 0.22, then you might experience DAG failures in Cloud Composer versions that have `apache-airflow-providers-cncf-kubernetes` package version 10.4.2 or later. At the same time, upgrading the `dag-factory` package to version 0.23 might require you to update your DAG code to make it compatible.
If your environment uses `dag-factory` version 0.22, we recommend to do the following:
- Temporarily postpone upgrading your environment until you're ready to switch to `dag-factory` version 0.23. Last versions of Cloud Composer that support version 0.22 are composer-3-airflow-2.10.5-build.3, composer-3-airflow-2.9.3-build.23, composer-2.13.1-airflow-2.10.5, and composer-2.13.1-airflow-2.9.3 released on May 14, 2025.
- When you are ready to upgrade, update your DAGs for compatibility with 0.23. We recommend to do this in a development environment first. Install `dag-factory` version 0.23, then check that your DAGs are parsed and are working correctly, and update them if needed. After your DAGs are compatible, install `dag-factory` version 0.23 in your production environment and transfer the updated DAGs. Your environment can now be upgraded to a later version of Cloud Composer or Airflow.
- If your environment is already upgraded to a later version of Cloud Composer and you experience problems, then update `dag-factory` to version 0.23 and update your DAGs for compatibility with 0.23.
説明：`dag-factory`パッケージのバージョン0.22を使用している環境では、`apache-airflow-providers-cncf-kubernetes`パッケージバージョン10.4.2以降を含むCloud Composer環境でDAGの実行障害が発生する可能性があります。同時に、`dag-factory`をバージョン0.23にアップグレードする際には、DAGコードの互換性に関する修正が必要になる場合があります。`dag-factory` 0.22を使用している場合は、Composer環境のアップグレードを一時的に延期するか、先に`dag-factory` 0.23へのアップグレードとDAGコードの修正を開発環境で実施することが推奨されます。
影響有無：**現在の環境では直接的な影響はなし。**
*   現在のCloud Composer環境（Composer version 2.7.1, Airflow version 2.7.3）に含まれる`apache-airflow-providers-cncf-kubernetes`のバージョンは`7.8.0`です。これはリリースノートで言及されている`10.4.2`より古いため、直ちにこの互換性問題の影響を受けることはありません。
*   ただし、将来Cloud Composer環境をアップグレードし、`apache-airflow-providers-cncf-kubernetes`のバージョンが`10.4.2`以上になった場合、もし`dag-factory` 0.22を使用していれば問題が発生する可能性があります。
対処方法：
1.  **`dag-factory`の使用状況の確認:** 現在のCloud Composer環境で`dag-factory`パッケージが利用されているか、またそのバージョンが0.22であるかを確認してください。
2.  **将来のアップグレードへの備え:** もし`dag-factory` 0.22を利用している場合は、将来Cloud Composer環境をアップグレードする際に、`apache-airflow-providers-cncf-kubernetes`のバージョンが10.4.2以上になる可能性があることを念頭に置いてください。その際には、`dag-factory`を0.23にアップグレードし、必要に応じてDAGコードを修正する計画を立てる必要があります。
3.  **開発環境での検証:** `dag-factory` 0.23へのアップグレードはDAGコードの変更を伴う可能性があるため、事前に開発環境で十分な検証を行うことを強く推奨します。
用語説明：
*   **DAG (Directed Acyclic Graph)**: Apache Airflowにおいて、実行するタスクとその依存関係を定義するワークフローの構造です。
*   **`dag-factory`**: YAMLなどの設定ファイルからAirflow DAGを動的に生成するためのPythonパッケージです。これにより、コードを書かずにDAGを定義できます。
*   **`apache-airflow-providers-cncf-kubernetes`**: Apache AirflowがKubernetesと連携するための機能（Kubernetes ExecutorやKubernetesPodOperatorなど）を提供するプロバイダーパッケージです。
# Title: July 21, 2025 
Link: https://cloud.google.com/release-notes#July_21_2025<br>
以下に、提供されたリリースノートの製品・アナウンス単位での調査結果を報告します。

# BigQuery

## Libraries (Java Client Library)
### Changed
原文:
```
- **bigquery:** Add OpenTelemetry support to BigQuery rpcs (#3860) (e2d23c1)
- **bigquery:** Add support for custom timezones and timestamps (#3859) (e5467c9)
- Load jobs preserve ascii control characters configuration (#3876) (5cfdf85)
- Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.69.0 (#3870) (a7f1007)
- Update dependency com.google.apis:google-api-services-bigquery to v2-rev20250615-2.0.0 (#3872) (f081589)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 (#3878) (0e971b8)
```
説明:
`google-cloud-bigquery` Javaクライアントライブラリがバージョン `2.53.0` に更新されました。主な変更点は以下の通りです。
*   BigQuery RPCに対するOpenTelemetryのサポートが追加されました。これにより、トレースやメトリクスによるモニタリングの統合が容易になります。
*   カスタムタイムゾーンおよびタイムスタンプのサポートが追加されました。
*   ロードジョブにおいてASCII制御文字を保持する設定が追加されました。
*   内部的な依存ライブラリ（`proto-google-cloud-bigqueryconnection-v1`, `google-api-services-bigquery`, `sdk-platform-java-config`）が更新されました。

影響有無:
影響なし。
これらの変更は、主に新機能の追加および内部依存関係の更新であり、既存のAPIの動作変更や非互換性のある変更（Breaking Change）は含まれていません。既存のアプリケーションコードが自動的に影響を受けることはありません。
Composer 2 (Airflow) はPythonベースであるため、このJavaクライアントライブラリの更新による直接的な影響はありません。

対処方法:
新機能（OpenTelemetry、カスタムタイムゾーン、ASCII制御文字保持）を利用したい場合は、アプリケーションで使用している `google-cloud-bigquery` ライブラリのバージョンを `2.53.0` 以降にアップデートしてください。

用語説明:
*   **OpenTelemetry**: クラウドネイティブなソフトウェアのためのオブザーバビリティフレームワークです。トレース、メトリクス、ログを標準化された方法で収集・エクスポートするためのAPI、SDK、ツールを提供します。
*   **RPC (Remote Procedure Call)**: ネットワーク上の別のコンピュータにあるプログラムのサブルーチンやプロシージャを実行するためのプロトコルです。BigQueryのクライアントライブラリは、内部的にRPCを使用してBigQueryサービスと通信します。

## Libraries (Python Client Library)
### Changed
原文:
```
- Add null_markers property to LoadJobConfig and CSVOptions (#2239) (289446d)
- Add total slot ms to RowIterator (#2233) (d44bf02)
- Add UpdateMode to update_dataset (#2204) (eb9c2af)
- Adds dataset_view parameter to get_dataset method (#2198) (28a5750)
- Adds date_format to load job and external config (#2231) (7d31828)
- Adds datetime_format as an option (#2236) (54d3dc6)
- Adds source_column_match and associated tests (#2227) (6d5d236)
- Adds time_format and timestamp_format and associated tests (#2238) (371ad29)
- Adds time_zone to external config and load job (#2229) (b2300d0)
- Fix rows returned when both start_index and page_size are provided (#2181) (45643a2)
- Make AccessEntry equality consistent with from_api_repr (#2218) (4941de4)
- Update type hints for various BigQuery files (#2206) (b863291)
- Improve clarity of "Output Only" fields in Dataset class (#2201) (bd5aba8)
```
説明:
`google-cloud-bigquery` Pythonクライアントライブラリがバージョン `3.35.0` に更新されました。主な変更点は以下の通りです。
*   **新機能の追加**:
    *   `LoadJobConfig` および `CSVOptions` に `null_markers` プロパティが追加され、ロード時にNULL値として解釈されるマーカーを指定できるようになりました。
    *   `RowIterator` に `total_slot_ms` が追加され、クエリ実行に費やされた合計スロット時間を取得できるようになりました。
    *   `update_dataset` メソッドに `UpdateMode` が追加され、データセットの更新動作をより詳細に制御できるようになりました。
    *   `get_dataset` メソッドに `dataset_view` パラメータが追加されました。
    *   ロードジョブと外部テーブル構成に `date_format`, `datetime_format`, `time_format`, `timestamp_format` が追加され、日付/時刻フォーマットの指定が柔軟になりました。
    *   `source_column_match` オプションが追加されました。
    *   外部テーブル構成とロードジョブに `time_zone` オプションが追加されました。
*   **バグ修正**: `start_index` と `page_size` の両方が指定された場合の行数取得の不具合が修正されました。
*   **改善**: `AccessEntry` の等価性チェックの整合性向上、型ヒントの更新、`Dataset` クラスのフィールド説明の明確化など。

影響有無:
影響なし。
これらの変更は、主に新機能の追加や既存の機能強化、バグ修正、およびドキュメンテーションの改善であり、後方互換性のない変更は含まれていません。既存のアプリケーションコードが自動的に影響を受けることはありません。
Composer 2 (Airflow) では、通常Googleが提供する `google-cloud-bigquery` ライブラリのバージョンがバンドルされていますが、これらの変更は既存のAirflow DAGの動作に直接的な影響を与えるものではありません。特にバグ修正 (`Fix rows returned when both start_index and page_size are provided`) は、該当するケースでコードの動作が改善される可能性があります。

対処方法:
新機能を利用したい場合や、修正されたバグの影響を受けていた場合は、アプリケーション（またはAirflow DAGの依存関係）で使用している `google-cloud-bigquery` ライブラリのバージョンを `3.35.0` 以降にアップデートしてください。Airflow環境で特定バージョンのライブラリを使用したい場合は、DAG内で `pip install` するか、Composer環境のPyPIパッケージを更新することを検討してください。

用語説明:
*   **LoadJobConfig**: BigQueryのロードジョブ（データをBigQueryテーブルにロードする操作）の設定を定義するオブジェクトです。
*   **RowIterator**: BigQueryのクエリ結果を行ごとに反復処理するためのイテレータオブジェクトです。
*   **Dataset**: BigQueryにおけるテーブル、ビューなどのリソースをまとめる論理的なコンテナです。

# Cloud Service Mesh

## Changed
原文:
```
Managed Cloud Service Mesh will start using proxy version `csm_mesh_proxy.20250623b_RC00` for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.35. This change is rolling out to all release channels.
```
説明:
マネージドCloud Service Meshにおいて、GKEクラスター上のGateway APIで使用されるプロキシのバージョンが `csm_mesh_proxy.20250623b_RC00` に更新されます。このプロキシバージョンはEnvoyバージョン1.35に相当します。この変更は全てのリリースチャネルに対して順次適用されます。

影響有無:
影響なし。
本件はマネージドサービスであるCloud Service Meshの内部的なコンポーネント（Envoyプロキシ）のバージョンアップであり、ユーザーが直接構成を変更する必要はありません。Cloud Service Meshを利用しており、GKEクラスターでGateway APIを使用している場合に、内部のEnvoyプロキシが新しいバージョンに更新されます。通常、Envoyのバージョンアップは後方互換性が保たれるように行われます。
当社の環境においてCloud Service MeshをGKEクラスターのGateway APIと組み合わせて利用していない場合、影響はありません。Composer 2 (Airflow) はGKE上で動作しますが、Cloud Service MeshのGateway APIを直接利用している構成ではないため、影響はありません。

対処方法:
特別な対処は不要です。
Cloud Service Meshを利用しており、GKE上のGateway APIと組み合わせて使用している場合は、本変更が適用された後もサービスが正常に動作しているか、モニタリングを通じて確認してください。

用語説明:
*   **Cloud Service Mesh**: Google Cloudが提供するマネージドなサービスメッシュプラットフォームです。サービス間のトラフィック管理、セキュリティ、オブザーバビリティを提供します。Istioをベースとしています。
*   **Gateway API**: KubernetesのネットワーキングAPIの次世代版で、Ingress APIの後継と位置づけられています。より柔軟かつ表現力豊かなトラフィックルーティングとロードバランシングの構成を提供します。
*   **Envoy**: 高性能なオープンソースのプロキシサーバーで、サービスメッシュのデータプレーンとして広く利用されています。トラフィックのルーティング、ロードバランシング、セキュリティポリシーの適用などを行います。

# Pub/Sub

## Libraries (Go Client Library)
### Changed
原文:
```
- **pubsub/v2:** Add MessageTransformationFailureReason to IngestionFailureEvent (208745b)
- **pubsub/v2:** Add new v2 library (#12218) (c798f62)
- **pubsub/v2:** Add SchemaViolationReason to IngestionFailureEvent (d8ae687)
- **pubsub/v2:** Generate renamed go pubsub admin clients (a95a0bf)
- **pubsub/v2:** Release 2.0.0 (#12568) (704efce)
- **pubsub/v2:** Document that the `acknowledge_confirmation` and `modify_ack_deadline_confirmation` fields in message `.google.pubsub.v1.StreamingPullResponse` are not guaranteed to be populated (208745b)
- **pubsub/v2:** Standardize spelling of "acknowledgment" in Pub/Sub protos (d8ae687)
- **pubsub/v2:** Update v2 package docs with migration guide (#12564) (5ef6068)
```
説明:
`pubsub/apiv1` Goクライアントライブラリにおいて、主にv2ライブラリに関する更新がリリースされました。
*   Pub/Sub Goクライアントライブラリの **v2バージョン（`pubsub/v2`）がリリース**されました。
*   `IngestionFailureEvent` に `MessageTransformationFailureReason` および `SchemaViolationReason` が追加されました。
*   `StreamingPullResponse` の `acknowledge_confirmation` と `modify_ack_deadline_confirmation` フィールドが常に設定されるわけではない旨のドキュメントが更新されました。
*   プロトバッファ定義における "acknowledgment" のスペルが標準化されました。

影響有無:
影響なし。
Goクライアントライブラリの更新であり、当社はGo言語を用いたPub/Subクライアントアプリケーションを運用していないため、直接的な影響はありません。Composer 2 (Airflow) はPythonベースであるため、このGoクライアントライブラリの更新による直接的な影響はありません。
もし将来的にGoクライアントライブラリを使用する場合、v2ライブラリへの移行はメジャーバージョンアップであるため、移行ガイド (`MIGRATING.md`) に従ったコードの修正が必要となる可能性があります。

対処方法:
特別な対処は不要です。

用語説明:
*   **IngestionFailureEvent**: Pub/Subでメッセージの取り込み（Ingestion）が失敗した際に発生するイベントです。このイベントには失敗理由が含まれます。
*   **StreamingPullResponse**: Pub/SubのStreamingPull APIで、サブスクリプションからメッセージをストリーミングで受信する際のレスポンスオブジェクトです。

## Libraries (Java Client Library)
### Changed
原文:
```
- Add MessageTransformationFailureReason to IngestionFailureEvent (8271399)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.60.1 (c9ef2cd)
- Update dependency com.google.cloud:google-cloud-bigquery to v2.52.0 (#2467) (fe08a6f)
- Update dependency com.google.cloud:google-cloud-core to v2.58.1 (#2476) (96a2354)
- Update dependency com.google.cloud:google-cloud-storage to v2.53.2 (#2469) (fa51a01)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 (#2477) (e1657cb)
```
説明:
`google-cloud-pubsub` Javaクライアントライブラリがバージョン `1.141.0` に更新されました。
*   `IngestionFailureEvent` に `MessageTransformationFailureReason` が追加されました。
*   内部的な依存ライブラリ（`gapic-generator-java`, `google-cloud-bigquery`, `google-cloud-core`, `google-cloud-storage`, `sdk-platform-java-config`）が更新されました。

影響有無:
影響なし。
これらの変更は、主に新機能の追加および内部依存関係の更新であり、既存のAPIの動作変更や非互換性のある変更（Breaking Change）は含まれていません。既存のアプリケーションコードが自動的に影響を受けることはありません。
Composer 2 (Airflow) はPythonベースであるため、このJavaクライアントライブラリの更新による直接的な影響はありません。

対処方法:
`MessageTransformationFailureReason` を利用してメッセージ変換の失敗理由を詳細に取得したい場合は、アプリケーションで使用している `google-cloud-pubsub` ライブラリのバージョンを `1.141.0` 以降にアップデートしてください。

用語説明:
*   **MessageTransformationFailureReason**: Pub/Subでメッセージが処理される過程で変換（例えば、スキーマによる検証やフォーマット変換など）が失敗した場合の理由を示すフィールドです。