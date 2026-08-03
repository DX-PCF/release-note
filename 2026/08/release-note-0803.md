
# Title: July 31, 2026 
Link: https://docs.cloud.google.com/release-notes#July_31_2026<br>
# Cloud SQL for PostgreSQL
## Change
原文: Starting on August 1, 2026, when you create or clone a Cloud SQL instance
enabled with Private Service Connect, or when you enable Private Service Connect
for an existing instance, then connection reconciliation
behavior is enabled by default and can't be disabled.

[connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation)
 When you remove a project from the list of allowed projects, all existing
Private Service Connect connections from the removed project are immediately
closed (reconciled). This means that applications using Private Service
Connect endpoints in those removed projects can't continue to connect to the
Cloud SQL instance using those endpoints.

 For more information, see Allowed Private Service Connect projects.

[Allowed Private Service Connect projects](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#allowed-psc-projects)

説明:
2026年8月1日以降、Cloud SQL for PostgreSQLインスタンスを作成またはクローンする際にPrivate Service Connect (PSC) を有効にする場合、あるいは既存のインスタンスでPSCを有効にする場合に、「接続調整（connection reconciliation）」の動作がデフォルトで有効になり、無効化できなくなります。

この「接続調整」とは、Private Service Connectで接続が許可されているプロジェクトのリストから特定のプロジェクトを削除した場合に、その削除されたプロジェクトからの既存のPSC接続が即座に切断される機能です。これにより、削除されたプロジェクト内のアプリケーションは、そのPSCエンドポイントを使用してCloud SQLインスタンスに接続し続けることができなくなります。

影響有無:
影響はあります。
現在、Private Service Connect (PSC) を使用してCloud SQL for PostgreSQLインスタンスに接続している場合、または将来的にPSCの利用を計画している場合に影響があります。2026年8月1日以降は、PSCを有効にしたCloud SQL for PostgreSQLインスタンスにおいて、許可されたプロジェクトリストからプロジェクトが削除された際に、そのプロジェクトからの既存のPSC接続が即座に切断される動作が強制されます。

これはセキュリティ強化のための変更ですが、接続が即座に切断されることで、削除されたプロジェクトで稼働するアプリケーションが意図しない接続エラーを発生させる可能性があります。特に、プロジェクトの削除がアプリケーションのダウンタイムに直接影響を与える可能性があるため、PSCの許可プロジェクトリストの管理において、より厳格な運用計画が求められます。

対処方法:
1.  **影響の認識:** 2026年8月1日以降にCloud SQL for PostgreSQLでPSCを新規設定、または既存インスタンスで有効化する際は、この接続調整機能がデフォルトで有効になり、無効化できないことを認識してください。
2.  **運用プロセスの見直し:** PSCの許可プロジェクトリストからプロジェクトを削除した場合、関連するアプリケーションの接続が即座に切断されることを前提とした運用計画を立ててください。
3.  **アプリケーション側の対応確認:** 意図しない切断が発生しないよう、アプリケーション側の接続再試行ロジックやフェイルオーバー戦略が適切に設計されているかを確認してください。プロジェクトの削除は、そのプロジェクト内のアプリケーションにとって一時的な接続中断を引き起こす可能性があるため、この変更による影響を事前に評価することが推奨されます。

用語説明:
*   **Private Service Connect (PSC):** Google Cloudが提供するネットワークサービスで、サービスコンシューマー（サービスを利用する側）が、サービスプロデューサー（サービスを提供する側、この場合はCloud SQL）のサービスにVPCネットワーク経由でプライベートにアクセスすることを可能にします。これにより、インターネット経由での公開を避け、セキュリティを強化できます。
*   **Connection Reconciliation (接続調整):** Private Service Connectにおいて、サービスプロデューサーが公開しているサービスの許可リスト（Allowed Private Service Connect projects）から特定のプロジェクトが削除された際に、その削除されたプロジェクトからの既存のPSC接続を即座に強制終了させる機能です。これにより、不正なアクセスが迅速に遮断されます。
*   **Cloud SQL for PostgreSQL:** Google Cloudが提供する、フルマネージドなPostgreSQLデータベースサービスです。データベースのパッチ適用、バックアップ、レプリケーションなどの運用タスクをGoogle Cloudが管理します。
# Title: July 30, 2026 
Link: https://docs.cloud.google.com/release-notes#July_30_2026<br>
# Google Kubernetes Engine

## Change (GKE バージョンアップデート - No channel (deprecated))
原文:
GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.

- Version 1.35.6-gke.1250000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.33.13-gke.1329000
    - 1.34.9-gke.1655000
    - 1.35.6-gke.1710000
    - 1.36.2-gke.2281000
- The following node versions are now available:
    - 1.30.14-gke.2866000
    - 1.31.14-gke.2456000
    - 1.32.13-gke.2175000
    - 1.33.13-gke.1329000
    - 1.34.9-gke.1655000
    - 1.35.6-gke.1710000
    - 1.36.2-gke.2281000
- The following versions are no longer available:
    - 1.33.12-gke.1165000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.34.8-gke.1126000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.35.6-gke.1049000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.35.6-gke.1638000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.36.0-gke.4447000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.36.0-gke.4681000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.32 to 1.33.13-gke.1101000
        - 1.33 to 1.34.9-gke.1065000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.33 to 1.33.13-gke.1101000
        - 1.34 to 1.34.9-gke.1065000
        - 1.35 to 1.35.6-gke.1250000
        - 1.36 to 1.36.2-gke.1346000

説明:
GKEの「No channel」（特定のリリースチャンネルに属さない、現在非推奨の運用形態）において、利用可能なクラスタバージョンが更新されました。新規クラスタ作成時のデフォルトバージョンが `1.35.6-gke.1250000` に設定されました。また、`1.33.13-gke.1329000`、`1.34.9-gke.1655000`、`1.35.6-gke.1710000`、`1.36.2-gke.2281000` といった新しいGKEクラスタおよびノードバージョンが利用可能になりました。一方で、`1.33.12-gke.1165000` など複数の古いバージョンが非推奨（deprecated）となり、90日以内、またはサポート終了の早い方までに削除される予定です。既存クラスタの自動アップグレードターゲットも更新され、特定のマイナーバージョンからのアップグレードパスが設定されました。
これらのロールアウトは既に進行中であり、すべてのGoogle Cloudゾーンで完了するまでには数日かかる場合があります。

影響有無:
影響あり。
お客様がご利用中のGoogle Cloud Composer 2（バージョン 2.7.1、Airflow 2.7.3）は、内部的にGKEクラスタを使用しています。GKEのバージョンアップは、Composerクラスタの基盤となるGKEバージョンにも適用される可能性があります。Composerクラスタは通常、GKEの`Stable`または`Regular`リリースチャンネルに属しており、「No channel」は現在非推奨の運用形態であるため、お客様のComposer環境に直接このチャンネルの変更が適用されることは稀です。
しかし、GKE全体のバージョン提供状況の変更として、Composerクラスタの将来的な自動アップグレードの方向性や、非推奨となったGKEバージョンを使用している場合のアップグレードの必要性を示唆します。特に、現在利用中のGKEバージョンがリリースノートに記載されている非推奨バージョンに含まれる場合、将来的には自動的にアップグレードが実行されます。
Composerはマネージドサービスであるため、GKEバージョンの互換性はGoogleによって管理されますが、自動アップグレード時には一時的なクラスタの再起動が発生する可能性があります。また、Kubernetesのマイナーバージョンアップに伴い、アプリケーションが非推奨APIを使用している場合、アップグレード後に動作に影響が出る可能性があります。
今回の変更は主にパッチバージョンアップと一部のマイナーバージョンアップ（例: 1.32から1.33、1.33から1.34）が含まれており、一般的な運用においては互換性が維持される見込みですが、非推奨APIの利用状況については確認が必要です。

対処方法:
1.  **現在利用中のGKEバージョン確認**: 現在のComposerクラスタがどのGKEバージョンで稼働しているかを確認してください。GCPコンソールでComposer環境の詳細画面を開くか、`gcloud composer environments describe YOUR_ENVIRONMENT_NAME --location YOUR_LOCATION` コマンドで確認できます。Composer環境のGKEバージョンは、通常Composerのバージョンライフサイクルに沿ってGoogleによって管理されます。
2.  **非推奨バージョン利用時の対応**: もし、お客様がComposer以外でGKEクラスタを直接利用しており、かつ、今回のリリースノートで「deprecated」とされているバージョン（例: 1.33.12-gke.1165000 など）に含まれる場合は、90日以内、またはサポート終了の早い方までに自動アップグレードされるため、事前にワークロードの互換性テストを実施し、必要に応じてアプリケーションの修正を検討してください。Composerクラスタについては、Googleが互換性を確保しながらアップグレードを実施します。
3.  **自動アップグレード計画の確認**: ComposerクラスタはGKEの自動アップグレードに追従します。メンテナンス期間を設定している場合、その期間内にGKEバージョンのアップグレードが実施される可能性があります。アップグレード時の影響（一時的なサービス中断など）を最小限に抑えるため、重要度の低い時間帯にメンテナンス期間を設定することをお勧めします。
4.  **互換性テスト**: 特にマイナーバージョンアップが予定されている場合、アプリケーションが新しいKubernetes APIバージョンと互換性があるか確認するため、ステージング環境などでテストを実施することを強く推奨します。Kubernetesの各マイナーバージョンには非推奨となるAPIが含まれるため、事前に `kubectl convert` や `gke-check-deprecated-apis` ツールなどで非推奨APIの利用状況をチェックすることができます。

用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Composer (Cloud Composer)**: Google Cloudが提供するマネージドApache Airflowサービス。ワークフローのオーケストレーションに使用されます。GKEを基盤として動作します。
*   **リリースチャンネル (Release Channel)**: GKEクラスタのバージョンアップグレード頻度と安定性を示すオプション。`No channel` (deprecated), `Stable`, `Regular`, `Rapid`, `Extended` などがあり、それぞれ異なるアップグレードポリシーとサポート期間を持ちます。Composerは通常`Stable`または`Regular`チャンネルのGKEバージョンに追従します。
*   **デフォルトバージョン**: 新規クラスタ作成時に自動的に選択されるGKEバージョン。
*   **非推奨 (Deprecated)**: 将来的にサポートが終了し、利用できなくなる予定のバージョンや機能。通常、一定の猶予期間が設けられます。非推奨化されたバージョンは、その後のリリースで削除される可能性があります。
*   **自動アップグレードターゲット**: GKEクラスタが自動アップグレードされる際の目標となるバージョン。パッチアップグレード（例: