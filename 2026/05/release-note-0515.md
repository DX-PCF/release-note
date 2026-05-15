
# Title: May 14, 2026 
Link: https://docs.cloud.google.com/release-notes#May_14_2026<br>
Google Cloud のインフラエンジニアとして、リリースノートに基づき構築済みのサービスへの影響を調査し、以下の通りご回答いたします。

---

# Cloud Composer

## Fixed
原文:
The `google-api-core` preinstalled package versions from 2.28.0 to 2.30.2 might
cause degraded environment performance, which can result in longer times to
execute a task and longer times to move a task from the queued to the executing
state.

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

We recommend to upgrade your environment to the following versions, which
contain a version of the package where the problem is fixed or isn't present:

- composer-3-airflow-3.1.7-build.7 and later
- composer-3-airflow-2.11.1-build.3 and later
- composer-3-airflow-2.10.5-build.36 and later
- composer-3-airflow-2.9.3-build.54 (contains 2.27.0)
- composer-2.17.0-airflow-2.11.1 and later
- composer-2.17.0-airflow-2.10.5 and later
- composer-2.16.11-airflow-2.11.1 (contains 2.27.0)
- composer-2.16.11-airflow-2.10.5 (contains 2.27.0)
- composer-2.16.11-airflow-2.9.3 (contains 2.27.0)

As a workaround, you can manually install a later version of the
`google-api-core` package to an affected environment by specifying `>=2.30.3`
as the required version.

説明:
Cloud Composer 環境において、プリインストールされている `google-api-core` パッケージのバージョン `2.28.0` から `2.30.2` の範囲でパフォーマンスが低下する可能性があるという問題が報告されました。これにより、Airflow のタスク実行時間や、タスクがキューから実行状態へ移行するまでの時間が長くなる可能性があります。

この問題は、特定のManaged Airflow (Gen 3) および (Gen 2) のビルドバージョンに影響を及ぼします。リリースノートでは影響を受ける具体的なビルドバージョンが列挙されており、問題が修正されたか、影響を受けない `google-api-core` パッケージバージョンを含む推奨アップグレードバージョンも提示されています。

また、ワークアラウンドとして、影響を受ける環境で `google-api-core` パッケージを `>=2.30.3` に手動でインストールすることで問題を回避できることも示されています。

影響有無:
**影響なし**
お客様が現在ご利用の `Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)` は、リリースノートで示されている影響を受けるManaged Airflow (Gen 2) ビルドのバージョン範囲（例: `composer-2.16.x`）に含まれていないため、この問題の直接的な影響は受けません。

対処方法:
現在ご利用のComposerバージョンでは直接的な影響はありません。
将来的にCloud Composer環境をアップグレードする際には、推奨されるComposerバージョン（例: `composer-2.17.0-airflow-2.11.1` 以降など）を選択することで、この問題が再発しないことを確認できます。

用語説明:
*   **`google-api-core`**: Google Cloud の各種 API と通信するために使用されるPythonクライアントライブラリのコア部分です。
*   **Cloud Composer**: Google Cloud 上でマネージドサービスとして提供される Apache Airflow のインスタンスです。ワークフローのオーケストレーションとスケジューリングに使用されます。
*   **Apache Airflow**: プログラマティックにワークフローをオーサリング、スケジューリング、モニタリングするためのオープンソースプラットフォームです。
*   **Managed Airflow (Gen 2/Gen 3)**: Cloud Composerの基盤となるインフラストラクチャのアーキテクチャ世代を指します。Gen 2はCompute Engineベース、Gen 3はGKEベースの新しいアーキテクチャを採用しています。
*   **Task**: Airflow におけるワークフロー（DAG）内の個々の実行可能な単位です。

---

# Spanner

## Announcement
原文:
The Spanner change streams default retention period has been increased from 1 day to 7 days.
This change affects both new and existing change streams that don't have a retention period explicitly set.
You can always specify the retention period through create change stream or alter change stream DDL statements to override the default.

[retention period](https://docs.cloud.google.com/spanner/docs/change-streams#data-retention)
[create change stream](https://docs.cloud.google.com/spanner/docs/change-streams/manage#create)
[alter change stream](https://docs.cloud.google.com/spanner/docs/change-streams/manage#modify)

説明:
Cloud Spanner の Change Streams 機能において、デフォルトのデータ保持期間が従来の1日から7日間に延長されました。この変更は、保持期間が明示的に設定されていない新規作成されるChange Streams、および既存のChange Streamsの両方に適用されます。

もし特定の保持期間を必要とする場合は、`CREATE CHANGE STREAM` または `ALTER CHANGE STREAM` の DDL (Data Definition Language) ステートメントを使用して、明示的に保持期間を指定することで、この新しいデフォルト設定を上書きすることが可能です。

影響有無:
**影響あり（通常はポジティブな影響）**
この変更により、既存のChange Streamsで保持期間を明示的に設定していない場合、自動的にデータ保持期間が1日から7日に延長されます。これは通常、より長期間のデータ変更履歴を利用できるため、システムの柔軟性向上や監査目的でのデータ保持に役立ちます。

しかし、厳密に1日間の保持期間を期待して設計されていたシステムの場合や、Change Streamsによって生成されるログデータのストレージコストを極力抑えたい場合は、意図しないデータ量の増加や、それに伴う微細なストレージコストの増加が発生する可能性があります。

対処方法:
*   **保持期間の延長が望ましい場合**: 特に必要ありません。自動的に7日間に延長されます。
*   **特定の保持期間を設定したい場合**: 現在の運用で1日保持を厳密に要求している、または7日間以外の保持期間を設定したい場合は、`ALTER CHANGE STREAM` DDLステートメントを使用して、既存のChange Streamの保持期間を明示的に指定し直してください。
    例: 保持期間を1日に設定し直す場合
    `ALTER CHANGE STREAM my_change_stream SET (retention_period = '1d');`
    新規にChange Streamを作成する場合は、`CREATE CHANGE STREAM` ステートメントで `retention_period` オプションを指定してください。

用語説明:
*   **Cloud Spanner**: Google Cloud が提供する、グローバル規模で整合性を保ちながらスケーラビリティと可用性を実現するリレーショナルデータベースサービスです。
*   **Change Streams**: Spanner データベース内で行われたデータ変更（挿入、更新、削除）をほぼリアルタイムでキャプチャし、利用可能なストリームとして提供する機能です。データ同期、分析、監査などの用途に利用されます。
*   **Retention Period**: データがシステムに保持される期間を指します。この期間が過ぎると、データは自動的に削除されます。
*   **DDL (Data Definition Language)**: データベースのスキーマやオブジェクト（テーブル、インデックス、ビューなど）の構造を定義したり変更したりするためのSQLステートメントの総称です。`CREATE`, `ALTER`, `DROP` などが含まれます。
# Title: May 13, 2026 
Link: https://docs.cloud.google.com/release-notes#May_13_2026<br>
## Cloud Service Mesh
### Security
原文: Proxy version csm_mesh_proxy.20260423_RC03 is rolling out to all Managed Cloud Service Mesh release channels over the next week.
説明：Cloud Service Mesh のプロキシバージョン `csm_mesh_proxy.20260423_RC03` が、今後1週間かけてすべてのマネージドCloud Service Mesh リリースチャネルに順次展開されます。このアップデートはセキュリティ関連の修正を含む可能性があります。
影響有無：影響なし。マネージドサービスであるため、通常、ユーザー側の操作は不要で、自動的に最新バージョンが適用されます。セキュリティの向上が期待できます。
対処方法：特別な対処は不要です。Cloud Service Meshの機能に影響が出ないか、システムログやモニタリングを通じて異常がないか継続的に確認します。
用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するフルマネージドなサービスメッシュソリューションです。オープンソースのIstioをベースにしており、マイクロサービス間の通信管理、トラフィックルーティング、ポリシー適用、可観測性などを提供します。
*   **Proxy version**: サービスメッシュにおいて、各サービスのサイドカーとしてデプロイされるプロキシ（通常はEnvoy）のバージョンを指します。このプロキシがサービス間の通信を仲介し、トラフィック管理やセキュリティ機能を提供します。

## Google Kubernetes Engine
### Change
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
説明：GKEクラスターのバージョンが更新されました。新しいGKEクラスターの作成、および既存クラスターのコントロールプレーンとノードのアップグレードに、以下の新バージョンが利用可能になります。
GKE version | Container-Optimized OS version | Details
---|---|---
1.30.14-gke.2458000 | cos-117-18613-534-110 | cos-117-18613-534-110 release notes
1.31.14-gke.1868000 | cos-117-18613-534-110 | cos-117-18613-534-110 release notes
1.32.13-gke.1492000 | cos-117-18613-534-110 | cos-117-18613-534-110 release notes
1.33.11-gke.1197000 | cos-121-18867-381-118 | cos-121-18867-381-118 release notes
1.34.7-gke.1499000 | cos-125-19216-220-185 | cos-125-19216-220-185 release notes
1.35.3-gke.2190000 | cos-125-19216-220-185 | cos-125-19216-220-185 release notes
1.36.0-gke.1759000 | cos-beta-129-19506-120-52 | cos-beta-129-19506-120-52 release notes
影響有無：影響なし。
GKEクラスターの新しいバージョンが利用可能になるというアナウンスであり、既存のクラスターが自動的にアップグレードされるわけではありません。また、現在利用中のGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)はGKE 1.20.xから1.29.xをサポートしており、今回のリリースノートに記載されているバージョン（1.30.x以降）は現在のComposerのサポート範囲外です。そのため、直接的な影響はありません。ただし、GKEをComposer以外の用途で利用している場合は、手動アップグレードの選択肢が増えます。
対処方法：特別な対処は不要です。将来的なGKEバージョンのアップグレード計画を立てる際に、これらのバージョンを考慮することができます。
用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Container-Optimized OS (COS)**: Googleが提供する、コンテナの実行に最適化された最小限のオペレーティングシステムです。GKEクラスターのワーカーノードの基盤として使用されます。

### Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the Security release notes for that image.
説明：今回のGKEリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらの更新されたイメージは累積的なもので、前回のGKEリリース以降にリリースされたすべてのCOSバージョンからのセキュリティ修正が組み込まれています。各COSイメージで解決された特定の脆弱性については、当該イメージのセキュリティリリースノートを参照してください。
影響有無：ポジティブな影響。
セキュリティ修正が含まれるため、セキュリティ体制の向上が期待されます。GKEクラスターがアップグレードされる際に、これらのセキュリティ修正が適用されます。現在のComposer環境がこれらのバージョンを直接利用することはありませんが、将来的なGKEバージョンアップ時にはこれらのセキュリティ強化の恩恵を受けることになります。
対処方法：GKEクラスターの自動アップグレード設定（メンテナンスウィンドウ、除外設定など）を確認し、セキュリティ修正が適切に適用されるよう管理します。
用語説明：
*   **Container-Optimized OS (COS)**: （前述参照）
*   **Cumulative security fixes**: 累積的なセキュリティ修正とは、あるバージョンに含まれるセキュリティ修正が、それ以前のすべてのセキュリティ修正を含んでいることを意味します。これにより、最新バージョンにアップグレードするだけで、過去のすべての既知の脆弱性修正が適用されます。

### Change
原文: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.6-gke.1154000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel: 1.33.10-gke.1176000, 1.34.6-gke.1237000, 1.35.3-gke.1234002, 1.35.3-gke.1389000
- The following versions are no longer available in the Stable channel: 1.33.10-gke.1067000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner. 1.34.6-gke.1068000, 1.35.2-gke.1962000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner. 1.35.3-gke.1234000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.32 to 1.33.10-gke.1115000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: 1.33 to 1.33.10-gke.1115000, 1.34 to 1.34.6-gke.1154000, 1.35 to 1.35.3-gke.1234002
説明：GKEのStableチャネルに関する更新情報です。新しいクラスター作成のデフォルトバージョンが `1.34.6-gke.1154000` になりました。Stableチャネルで新たに利用可能になったバージョンと、非推奨または利用不可になったバージョンがリストされています。また、このチャネルのクラスターに対する自動アップグレードのターゲットバージョンが更新されました。
影響有無：間接的な影響。
現在利用中のGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)はGKE 1.20.xから1.29.xをサポートしており、Stableチャネルのこれらの更新バージョン（1.32.x以降）は現在のComposerのサポート範囲外です。そのため、直接Composer環境が自動アップグレードされるなどの影響はありません。
ただし、GKEをComposer以外の用途でStableチャネルで利用している場合は、
*   新規クラスター作成時のデフォルトバージョンが変更されることに留意する必要があります。
*   既存クラスターで非推奨バージョンを使用している場合、90日以内にサポートが終了するため、計画的なアップグレードが必要です。
*   自動アップグレードが有効な場合、メンテナンスウィンドウや除外設定によっては、自動的に新しいターゲットバージョンにアップグレードされる可能性があります。
対処方法：
*   Stableチャネルで運用中の既存GKEクラスターがある場合、現在利用しているバージョンが非推奨リストに含まれていないか確認します。非推奨の場合、90日以内のアップグレードを計画します。
*   自動アップグレード設定（メンテナンスウィンドウ、除外設定など）を確認し、意図しないアップグレードが発生しないよう、また意図したアップグレードが行われるよう管理します。
用語説明：
*   **GKE release channel**: GKEクラスターのバージョン更新の提供頻度と安定性を制御する設定です。`Stable`チャネルは、本番環境に適した、十分にテストされたバージョンを提供します。
*   **Deprecated version**: 非推奨バージョン。そのバージョンのサポートが終了するか、まもなく終了することを意味します。通常、一定期間の猶予期間の後に利用できなくなったり、セキュリティアップデートが提供されなくなったりします。
*   **Auto-upgrade targets**: GKEが自動アップグレードする際の目標となるバージョンです。

### Change
原文: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Regular channel: 1.33.11-gke.1074000, 1.34.7-gke.1055000
- The following versions are no longer available in the Regular channel: 1.33.10-gke.1176000, 1.34.6-gke.1237000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.32 to 1.33.11-gke.1013000, 1.33 to 1.34.6-gke.1307000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: 1.33 to 1.33.11-gke.1013000, 1.34 to 1.34.6-gke.1307000
説明：GKEのRegularチャネルに関する更新情報です。Regularチャネルで新たに利用可能になったバージョンと、利用不可になったバージョンがリストされています。また、このチャネルのクラスターに対する自動アップグレードのターゲットバージョンが更新されました。
影響有無：間接的な影響。
Stableチャネルと同様に、ComposerがサポートするGKEバージョン範囲外の更新であるため、直接的な影響はありません。GKEをComposer以外の用途でRegularチャネルで利用している場合に影響があります。
対処方法：
*   Regularチャネルで運用中の既存GKEクラスターがある場合、現在利用しているバージョンが利用不可リストに含まれていないか確認します。
*   自動アップグレード設定（メンテナンスウィンドウ、除外設定など）を確認し、意図しないアップグレードが発生しないよう、また意図したアップグレードが行われるよう管理します。
用語説明：
*   **Regular channel**: GKEのリリースチャネルの一つで、Stableチャネルより早く新機能が利用可能になる一方、Rapidチャネルよりは安定性を重視します。

### Change
原文: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.3-gke.1993000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel: 1.33.11-gke.1197000, 1.34.7-gke.1499000, 1.35.3-gke.2190000, 1.36.0-gke.1759000
- The following versions are no longer available in the Rapid channel: 1.33.11-gke.1137000 is deprecated in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner. 1.34.7-gke.1321000 is deprecated in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner. 1.35.3-gke.1737000, 1.36.0-gke.1379000
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.34 to 1.35.3-gke.1993000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: 1.35 to 1.35.3-gke.1993000, 1.36 to 1.36.0-gke.1575000
説明：GKEのRapidチャネルに関する更新情報です。新しいクラスター作成のデフォルトバージョンが `1.35.3-gke.1993000` になりました。Rapidチャネルで新たに利用可能になったバージョンと、非推奨または利用不可になったバージョンがリストされています。また、このチャネルのクラスターに対する自動アップグレードのターゲットバージョンが更新されました。
影響有無：間接的な影響。
Stableチャネルと同様に、ComposerがサポートするGKEバージョン範囲外の更新であるため、直接的な影響はありません。GKEをComposer以外の用途でRapidチャネルで利用している場合に影響があります。
対処方法：
*   Rapidチャネルで運用中の既存GKEクラスターがある場合、現在利用しているバージョンが非推奨リストに含まれていないか確認します。非推奨の場合、90日以内のアップグレードを計画します。
*   自動アップグレード設定（メンテナンスウィンドウ、除外設定など）を確認し、意図しないアップグレードが発生しないよう、また意図したアップグレードが行われるよう管理します。
用語説明：
*   **Rapid channel**: GKEのリリースチャネルの一つで、最も早く新機能やバージョン更新が提供されます。最新機能を試したい場合や、開発・テスト環境に適しています。

### Change
原文: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available: 1.33.11-gke.1197000, 1.34.7-gke.1499000, 1.35.3-gke.1234002, 1.35.3-gke.2190000
- The following node versions are now available: 1.30.14-gke.2458000, 1.31.14-gke.1868000, 1.32.13-gke.1492000, 1.33.11-gke.1197000, 1.34.7-gke.1499000, 1.35.3-gke.1234002, 1.35.3-gke.2190000
- The following versions are no longer available: 1.33.9-gke.1060000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner. 1.33.10-gke.1067000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner. 1.33.11-gke.1137000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner. 1.34.7-gke.1321000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner. 1.35.2-gke.1962000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner. 1.35.3-gke.1522000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.32 to 1.33.10-gke.1115000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: 1.33 to 1.33.10-gke.1115000, 1.34 to 1.34.6-gke.1307000
説明：GKEのコントロールプレーンおよびノードバージョンについて、新たに利用可能になったバージョンと、非推奨となったバージョンに関する情報です。複数のバージョンが利用可能になり、同時にいくつかのバージョンが非推奨化されました。また、自動アップグレードのターゲットバージョンも更新されました。
影響有無：間接的な影響。
現在利用中のGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)はGKE 1.20.xから1.29.xをサポートしており、今回利用可能になったGKEバージョン（1.30.x以降）および非推奨になったGKEバージョン（1.33.x以降）は現在のComposerのサポート範囲外です。そのため、直接的な影響はありません。
ただし、GKEをComposer以外の用途で利用している場合は、
*   現在使用しているGKEクラスターのバージョンが非推奨リストに含まれていないか確認が必要です。非推奨になったバージョンは90日以内にサポートが終了するため、計画的なアップグレードが必要です。
*   自動アップグレードが有効なクラスターは、指定された新しいバージョンに自動的に更新される可能性があります。
対処方法：
*   GKEクラスター（Composer以外も含む）のバージョンを定期的に確認し、非推奨バージョンを使用している場合は、90日以内にアップグレードを計画・実施します。
*   自動アップグレード設定（メンテナンスウィンドウ、除外設定など）を確認し、意図しないアップグレードが発生しないよう、また意図したアップグレードが行われるよう管理します。
用語説明：
*   **Node version**: GKEクラスターのワーカーノードが実行するKubernetesおよびその基盤となるOSのバージョンを指します。Podが実際にデプロイされ実行される環境です。
*   **Control plane version**: GKEクラスターのマスターコンポーネント（APIサーバー、スケジューラー、コントローラーマネージャーなど）が実行するKubernetesのバージョンを指します。クラスター全体の管理とオーケストレーションを担います。

### Change
原文: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Extended channel: 1.30.14-gke.2415000, 1.30.14-gke.2458000, 1.31.14-gke.1823000, 1.31.14-gke.1868000, 1.32.13-gke.1492000, 1.33.11-gke.1074000, 1.34.7-gke.1055000
- The following versions are no longer available in the Extended channel: 1.30.14-gke.2369000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner. 1.30.14-gke.2441000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner. 1.31.14-gke.1790000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner. 1.31.14-gke.1850000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
# Title: May 12, 2026 
Link: https://docs.cloud.google.com/release-notes#May_12_2026<br>
以下に、Google Cloudのリリースノートに対する影響調査結果をまとめました。

---

# Apigee X
## Announcement
原文: On May 12th, 2026, we released an updated version of Apigee (1-17-0-apigee-7).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：Apigee Xの新しいバージョン `1-17-0-apigee-7` が2026年5月12日にリリースされました。この更新のロールアウト（段階的展開）は本日開始され、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる可能性があります。ロールアウトが完了するまで、お使いのインスタンスでは新しい機能や修正が利用できない場合があります。

影響有無：影響なし。これは通常のリリースアナウンスメントであり、サービスへの直接的なダウンタイムやお客様側での設定変更を要求するものではありません。Google Cloudによって自動的に適用されるバックエンドの更新です。ただし、新しい機能や修正が利用可能になるまでに時間差があることを認識しておく必要があります。

対処方法：特段の対処は不要です。ロールアウトの完了を待ってください。もし、特定の修正や新機能の利用を急ぐ場合は、数日待ってから利用可能になっているか確認してください。

用語説明：
*   **ロールアウト (Rollout):** ソフトウェアの新しいバージョンや機能が、段階的に展開され、すべてのユーザーやシステムに適用されていくプロセス。

## Security
原文: Security fix for Apigee infrastructure. This addresses the following vulnerabilities: - CVE-2026-42587- CVE-2026-5588- CVE-2026-34480- GHSA-72hv-8253-57qq- CVE-2026-33870- CVE-2026-33871- CVE-2026-35611- CVE-2026-33170- CVE-2026-33169- CVE-2026-33176- CVE-2026-33210- CVE-2026-33186- CVE-2026-42499- CVE-2026-35469- CVE-2026-32281- CVE-2026-27144
[CVE-2026-42587](https://nvd.nist.gov/vuln/detail/CVE-2026-42587), [CVE-2026-5588](https://nvd.nist.gov/vuln/detail/CVE-2026-5588), [CVE-2026-34480](https://nvd.nist.gov/vuln/detail/CVE-2026-34480), [GHSA-72hv-8253-57qq](https://github.com/advisories/GHSA-72hv-8253-57qq), [CVE-2026-33870](https://nvd.nist.gov/vuln/detail/CVE-2026-33870), [CVE-2026-33871](https://nvd.nist.gov/vuln/detail/CVE-2026-33871), [CVE-2026-35611](https://nvd.nist.gov/vuln/detail/CVE-2026-35611), [CVE-2026-33170](https://nvd.nist.gov/vuln/detail/CVE-2026-33170), [CVE-2026-33169](https://nvd.nist.gov/vuln/detail/CVE-2026-33169), [CVE-2026-33176](https://nvd.nist.gov/vuln/detail/CVE-2026-33176), [CVE-2026-33210](https://nvd.nist.gov/vuln/detail/CVE-2026-33210), [CVE-2026-33186](https://nvd.nist.gov/vuln/detail/CVE-2026-33186), [CVE-2026-42499](https://nvd.nist.gov/vuln/detail/CVE-2026-42499), [CVE-2026-35469](https://nvd.nist.gov/vuln/detail/CVE-2026-35469), [CVE-2026-32281](https://nvd.nist.gov/vuln/detail/CVE-2026-32281), [CVE-2026-27144](https://nvd.nist.gov/vuln/detail/CVE-2026-27144)

説明：Apigeeインフラストラクチャにおける複数のセキュリティ脆弱性（上記のリスト）に対する修正が適用されました。これらの脆弱性は、Apigeeの運用基盤に関連するものです。

影響有無：影響なし。これらの修正はApigeeインフラストラクチャの脆弱性に対応するものであり、Google Cloud側で自動的に適用されます。ユーザーが直接対処する必要はありません。むしろ、セキュリティが強化されるため、Apigee環境の安全性が向上します。

対処方法：特段の対処は不要です。Google Cloudによって自動的に脆弱性が修正され、ユーザー環境に反映されます。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures):** 公開されているソフトウェアの脆弱性に対して付与される識別子。
*   **GHSA (GitHub Security Advisory):** GitHubが管理するセキュリティ脆弱性データベースの識別子。
*   **インフラストラクチャ (Infrastructure):** Apigeeサービスを稼働させるための基盤となるシステムやコンポーネント。

## Fixed
原文:
*   **480260846** Improved XML processing security to prevent external entity injection.
*   **510061670, 505723451, 503723862, 503817773** Improved security in OAuthV2 policy.
*   **505645076** Fixed a security issue in OAuthV2 policy to prevent unauthorized token injection.
*   **503047744, 410026138, 496021751** Improved security isolation for PythonScript policy execution.
*   **469694040** Fixed an issue where custom security policies could intermittently fail to apply, and improved security policy resolution to ensure correct policy selection.
*   **502971220** Fixed a concurrency issue to improve stability under high load.
*   **509692565** Fixed content-length header handling in external processing to prevent incorrect values.
*   **282207038** Improved performance while listing apps on scale.
*   **501102321** Fixed recurring fee calculation in monetization to correctly apply rate plan overrides.
*   **449729840, 502604752** Fixed streaming response handling to prevent race conditions in bidirectional flows.
*   **507167063** Fixed preservation of client request IDs during proxy chaining.
*   **507580304** Improved IPv4 address normalization for consistent access control evaluation.
*   **502692267** MCP to handle /.well-known/oauth-protected-resource/mcp resource paths.
*   **430170696** Changed the error response from 500 to 401 for expired consumer keys.
*   **480770263** Fixed SpikeArrest policy to handle edge cases that previously caused 500 errors.
*   **500861814** Gracefully handle connection failures involving the forward proxy, resolving an issue where port exhaustion could trigger aggressive retry storms, excessive CPU usage, and unnecessary scaling.
*   **500313309** Fixed SSE streaming detection logic.
*   **494304819** Hardened message processor management ports by blocking external access to internal management endpoints.
*   **469642464** Improved input validation in AI protection policies to prevent Server-Side Request Forgery.
*   **472526232** Improved SAML assertion validation.
*   **494590020** Added enforcement for product association in OAuthV2 flow. Apps without valid products are now denied.
*   **479288727** Improved performance and reduced redundant work in ingress status watcher.
*   **N/A** Updates to infrastructure and libraries.

説明：
Apigee Xの様々な機能改善とバグ修正が含まれています。主な変更点としては、以下が挙げられます。
*   XML処理、OAuthV2ポリシー、PythonScriptポリシー、カスタムセキュリティポリシーにおけるセキュリティの強化。
*   高負荷時の安定性向上、コンテンツ長ヘッダー処理の修正、大規模なアプリリスト表示時のパフォーマンス向上、収益化機能の計算ロジック修正など、多くのバグ修正と信頼性向上。
*   プロキシチェイニング時のクライアントリクエストIDの維持、IPv4アドレス正規化の改善、フォワードプロキシ関連の接続障害処理の改善など、ネットワークおよびプロキシ機能の堅牢化。
*   期限切れのコンシューマーキーに対するエラーレスポンスが`500`から`401`に変更。
*   OAuthV2フローにおいて、有効な製品に関連付けられていないアプリからのリクエストが拒否されるように、製品関連付けの強制を追加。
*   インフラストラクチャとライブラリの更新。

影響有無：
*   **概ね影響なし（Positive Impact）：** 多くの修正はセキュリティ強化、安定性向上、パフォーマンス改善、バグ修正であり、既存のワークロードにプラスの影響を与えます。これらはGoogle Cloud側で自動的に適用され、お客様側での変更は通常不要です。
*   **一部影響の可能性（要確認）：**
    *   **OAuthV2フローにおける製品関連付けの強制 (`494590020`):** 現在、有効な製品に紐付けられていないアプリでOAuthV2を使用している場合、そのアプリからのリクエストが拒否されるようになります。これは動作変更であり、影響を受ける可能性があります。
    *   **期限切れのコンシューマーキーに対するエラーレスポンスが500から401に変更 (`430170696`):** もしお客様のクライアントアプリケーションがApigee APIからのエラーレスポンスを解析し、期限切れのキーに対してHTTPステータスコード `500` を期待してハンドリングしている場合、この変更により影響を受ける可能性があります。

対処方法：
*   **OAuthV2フローにおける製品関連付けの強制:**
    *   現在OAuthV2を使用しているすべてのアプリケーションについて、Apigeeの管理UIまたはAPIを通じて、適切に製品と関連付けられているかを確認してください。
    *   関連付けられていないアプリが存在する場合は、速やかに該当する製品と関連付けを行ってください。
*   **期限切れのコンシューマーキーに対するエラーレスポンスが500から401に変更:**
    *   Apigee APIからのエラーレスポンスを解析しているクライアントアプリケーションがある場合、HTTPステータスコードが `401` (`Unauthorized`) に変わることを考慮し、必要に応じてエラーハンドリングロジックを更新してください。
*   その他の修正については、特段の対処は不要です。サービスがより安定し、セキュリティが向上することを期待してください。

用語説明：
*   **外部エンティティインジェクション (External Entity Injection):** XMLパーサーが外部から参照されるエンティティを処理する際の脆弱性を悪用し、不正なデータを挿入する攻撃手法。
*   **OAuthV2ポリシー (OAuthV2 Policy):** ApigeeでOAuth 2.0の認証認可フローを実装・管理するためのポリシー。
*   **PythonScriptポリシー (PythonScript Policy):** ApigeeでカスタムのPythonスクリプトを実行するためのポリシー。
*   **並行処理 (Concurrency):** 複数のタスクが同時に（または時間的に重なって）実行されること。
*   **Content-Lengthヘッダー (Content-Length Header):** HTTPレスポンスやリクエストのボディの長さをバイト単位で示すヘッダー。
*   **収益化 (Monetization):** APIの利用に対して課金や収益管理を行うApigeeの機能。
*   **競合状態 (Race Condition):** 複数の処理が同時に実行された際に、実行順序によって結果が予測不能になる状態。
*   **プロキシチェイニング (Proxy Chaining):** 複数のAPIプロキシが連続して呼び出される構成。
*   **MCP (Message Processor):** Apigeeのデータプレーンコンポーネントで、APIプロキシへのリクエストを処理する。
*   **コンシューマーキー (Consumer Key):** APIクライアントを識別するためのキーで、APIキーやOAuthクライアントIDとして使用される。
*   **SpikeArrestポリシー (SpikeArrest Policy):** Apigeeで短期間のトラフィックの急増（スパイク）からバックエンドサービスを保護するためのポリシー。
*   **フォワードプロキシ (Forward Proxy):** クライアントからのリクエストを代理して外部ネットワークに転送するプロキシ。
*   **ポート枯渇 (Port Exhaustion):** クライアントが利用可能な一時的なポートを使い果たし、新しい接続を確立できなくなる状態。
*   **SSE (Server-Sent Events):** サーバーからクライアントへ一方的にデータをプッシュする技術。
*   **Server-Side Request Forgery (SSRF):** サーバーが外部から与えられたURLに対してリクエストを送信する機能を悪用し、攻撃者が意図しない内部リソースなどへのアクセスを強制する攻撃。
*   **SAMLアサーション (SAML Assertion):** SAML (Security Assertion Markup Language) において、認証、属性、認可決定などの情報を含むXMLドキュメント。
*   **イングレスステータスウォッチャー (Ingress Status Watcher):** Apigeeのイングレス（APIトラフィックの入り口）の健全性や状態を監視するコンポーネント。

---

# Cloud SQL for PostgreSQL
## Change
原文: The command for upgrading Cloud SQL instances to the new network architecture has been re-enabled. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture).

説明：Cloud SQL for PostgreSQLインスタンスを新しいネットワークアーキテクチャにアップグレードするためのコマンドが、再度有効になりました。詳細については、公式ドキュメント「Upgrade an instance to the new network architecture」を参照してください。

影響有無：影響なし。これは、お客様がCloud SQL for PostgreSQLインスタンスを新しいネットワークアーキテクチャにアップグレードしたい場合に、手動で実行できるオプションが利用可能になったという情報です。既存のインスタンスに自動的に変更が適用されるものではありません。新しいネットワークアーキテクチャへの移行を検討しているお客様にとっては、選択肢が増えるためプラスの変更です。

対処方法：特段の対処は不要です。現在、Cloud SQL for PostgreSQLインスタンスを利用している場合で、そのネットワークアーキテクチャを新しいものにアップグレードしたい場合に、このコマンドを利用して手動でアップグレードを検討してください。アップグレードの際は、公式ドキュメントを十分に参照し、影響を評価した上で実施してください。

用語説明：
*   **Cloud SQL (Cloud SQL):** Google Cloudが提供するフルマネージドのリレーショナルデータベースサービス。PostgreSQLはその対応データベースの一つ。
*   **ネットワークアーキテクチャ (Network Architecture):** サービス間の通信や接続方法を規定するネットワークの設計。Cloud SQLでは、インスタンスとアプリケーション間の接続方法に関連する。
*   **インスタンス (Instance):** Cloud SQLで作成される、個々のデータベースサーバーの論理的な単位。

---

# Compute Engine

# Title: May 11, 2026 
Link: https://docs.cloud.google.com/release-notes#May_11_2026<br>
# AlloyDB for PostgreSQL

## Announcement

原文: AlloyDB now offers extended support for clusters running major PostgreSQL versions that have reached their end-of-life (EOL) as defined by the PostgreSQL community. Extended support provides an additional three years of support after the end of regular support, giving you more time to plan and perform major version upgrades. For more information, see Extended support for AlloyDB for PostgreSQL.

説明：
AlloyDB for PostgreSQLが、PostgreSQLコミュニティによってサポート終了（EOL）とされたメジャーバージョンに対し、延長サポートを提供するというアナウンスです。この延長サポートにより、通常のサポート期間終了後、さらに3年間サポートが提供されるため、お客様はAlloyDBのメジャーバージョンアップグレードの計画と実行により多くの時間を確保できるようになります。

影響有無：
既存のサービス稼働に直接的な負の影響はありません。むしろ、現在PostgreSQLのEOLバージョンを使用している、または今後EOLを迎えるAlloyDB for PostgreSQLインスタンスをご利用のお客様にとっては、メジャーバージョンアップグレードの計画に猶予が生まれ、システム移行におけるリスクを低減できるというポジティブな影響があります。

対処方法：
必須の対処はありません。
しかしながら、現在AlloyDB for PostgreSQLをご利用中で、PostgreSQLのメジャーバージョンがEOLに近づいている、または既にEOLを迎えている場合は、この延長サポートを考慮して、より計画的かつ柔軟なメジャーバージョンアップグレード戦略を検討することをお勧めします。具体的な延長サポートの内容（料金体系、サポート範囲、制約など）については、提供されている[Extended support for AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/extended-support)のドキュメントを参照し、ご自身の環境に適用可能か確認してください。

用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供するフルマネージドなPostgreSQL互換データベースサービスです。高い可用性、スケーラビリティ、パフォーマンスを特徴とします。
*   **EOL (End-of-Life)**: ソフトウェアやサービスの「サポート終了」を意味します。EOLを迎えたバージョンは通常、セキュリティアップデートやバグ修正が提供されなくなるため、新しいバージョンへの移行が強く推奨されます。
*   **メジャーバージョンアップグレード**: データベースソフトウェアのバージョン番号の大きな変更（例: PostgreSQL 14から15へのアップグレード）を指します。通常、下位互換性がない場合があり、アプリケーションの修正や入念なテストが必要となるため、計画的な対応が求められます。