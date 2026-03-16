
# Title: March 12, 2026 
Link: https://docs.cloud.google.com/release-notes#March_12_2026<br>
## BigQuery
### Change
原文: BigQuery advanced runtime is now enabled as the default runtime for all projects.
[BigQuery advanced runtime](https://docs.cloud.google.com/bigquery/docs/advanced-runtime)
説明：BigQueryの高度な実行環境（Advanced Runtime）が、全てのプロジェクトでデフォルトのランタイムとして有効化されました。これにより、クエリの実行が最適化され、パフォーマンスが向上する可能性があります。
影響有無：影響あり。
BigQueryのクエリ実行において、従来のランタイムからAdvanced Runtimeへ切り替わります。これにより、既存のクエリの実行パフォーマンス（処理時間やリソース消費量）が変化する可能性があります。通常はパフォーマンス向上とコスト効率の改善が期待されますが、一部の複雑なクエリでは挙動が変わることも考えられます。
対処方法：特別な対処は通常不要ですが、BigQueryのクエリ実行ログ（Audit Logs）やモニタリング（Cloud Monitoring）を通じて、主要なワークロードの実行パフォーマンスとコストに予期せぬ変化がないか監視することを推奨します。もしパフォーマンスの劣化やコスト増大が見られる場合は、クエリの見直しや必要に応じてGoogle Cloudサポートへの問い合わせを検討してください。
用語説明：
*   **BigQuery advanced runtime**: BigQueryのクエリ実行エンジンにおける、より高度に最適化されたランタイム環境。クエリの並列処理能力やメモリ管理が強化され、大規模なデータ処理において高いパフォーマンスを発揮します。

## Cloud Logging
### Issue
原文: The automatic backfill operation performed on a log bucket that has been upgraded to use Log Analytics has been temporarily paused. To manually initiate the backfill operation, contact Cloud Customer Care.
[Cloud Customer Care](https://docs.cloud.google.com/stackdriver/docs/getting-support)
説明：Log Analyticsを使用するようにアップグレードされたログバケットにおいて、自動バックフィル操作が一時的に停止されています。過去のログデータをLog Analyticsで利用できるようにするためのバックフィルを手動で開始したい場合は、Cloud Customer Careに連絡する必要があります。
影響有無：影響あり。
Log Analyticsにアップグレード済みのログバケットを使用しており、かつ過去のログデータがLog Analyticsで利用可能になっていない場合、そのログデータの分析が自動では進行しません。新規にLog Analyticsを有効化し、過去のログも分析対象としたい場合は影響を受けます。
対処方法：既存のログバケットでLog Analyticsを有効にしており、自動バックフィルが完了していない、または過去のログデータを早急にLog Analyticsで分析する必要がある場合は、Google Cloud Customer Careに連絡し、手動でのバックフィル開始を依頼してください。
用語説明：
*   **Log Analytics**: Cloud Loggingの機能の一つで、ログバケットに保存されたログデータをBigQueryの強力な分析機能を用いてSQLクエリで分析できるようにするものです。
*   **Backfill operation (バックフィル操作)**: データベースやデータウェアハウスにおいて、新しい機能やスキーマ変更が適用された際に、過去のデータを新しい形式や要件に合わせて埋め合わせる（移行する）処理を指します。ここでは、Log Analytics有効化以前のログデータをLog Analyticsでクエリ可能にするための処理を意味します。

## Cloud Storage
### Change
原文: Object uploads that use customer-managed encryption keys (CMEK) now fail if the Cloud Storage service agent lacks the necessary IAM role to decrypt the object. For steps to grant the required role, see Assign a Cloud KMS key to a service agent.
[Assign a Cloud KMS key to a service agent](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access)
説明：顧客管理の暗号鍵（CMEK）を使用してオブジェクトをCloud Storageにアップロードする際、Cloud Storageサービスエージェントに必要な復号化用IAMロールが付与されていない場合、アップロードが失敗するようになりました。
影響有無：影響あり（Breaking Change）。
CMEKを使用してCloud Storageにオブジェクトをアップロードしている場合、Cloud Storageサービスエージェント（`service-<PROJECT_NUMBER>@gs-project-accounts.iam.gserviceaccount.com`）に、CMEKが格納されているCloud KMSキーリングに対する`Cloud KMS 暗号鍵の暗号化/復号化機能のユーザー`ロール（`roles/cloudkms.cryptoKeyEncrypterDecrypter`）が付与されていないと、オブジェクトのアップロードが失敗するようになります。この変更は既存の運用に影響を与える可能性があります。
対処方法：CMEKを使用してCloud Storageにオブジェクトをアップロードする全てのバケットについて、関連するCloud KMSキーのIAMポリシーを確認してください。Cloud Storageサービスエージェントに`roles/cloudkms.cryptoKeyEncrypterDecrypter`ロールが適切に付与されていることを確認し、不足している場合は直ちに付与してください。詳細は提供されたドキュメントリンクを参照してください。
用語説明：
*   **CMEK (Customer-Managed Encryption Keys)**: 顧客がCloud KMSで生成・管理する暗号鍵を使用して、保存データを暗号化する機能です。Google管理の暗号鍵（CMEK-G）やGoogle管理のデフォルト暗号鍵（CMEK-D）よりも、顧客側で暗号鍵のライフサイクルを制御できるため、より高いセキュリティ要件を満たす場合に利用されます。
*   **Cloud Storage service agent**: Google Cloudプロジェクト内でCloud Storageサービスが他のGoogle Cloudサービスと連携するために使用する特別なサービスアカウントです。

## Google Kubernetes Engine
### Change
原文: GKE cluster versions have been updated. **New versions available for upgrades and new clusters.** The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
説明：GKEクラスタの利用可能なバージョンが更新されました。新しいGKEクラスタの作成時や、既存クラスタのコントロールプレーンおよびノードのアップグレードに、これらの新しいバージョンが選択できるようになりました。
影響有無：影響なし。
これはGKEクラスタのバージョンが新しく利用可能になったという情報であり、既存のクラスタが自動的に新しいバージョンにアップグレードされることを意味するものではありません（後述のリリースチャネルによる自動アップグレードは除く）。新規クラスタ作成や手動アップグレードの選択肢が増えるため、直接的な運用への影響はありません。
対処方法：GKEクラスタのアップグレード計画を立てる際に、これらの新しいバージョンを検討することができます。
用語説明：
*   **GKE cluster versions**: Google Kubernetes Engine (GKE) クラスタで利用できるKubernetesのバージョンと、それに含まれるGKE独自のパッチや機能のバージョンです。

### Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:
| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.30.14-gke.2192000 | cos-117-18613-534-15 | cos-117-18613-534-15 release notes |
| 1.31.14-gke.1576000 | cos-117-18613-534-15 | cos-117-18613-534-15 release notes |
| 1.32.13-gke.1059000 | cos-117-18613-534-15 | cos-117-18613-534-15 release notes |
| 1.33.9-gke.1060000 | cos-121-18867-381-14 | cos-121-18867-381-14 release notes |
[cos-117-18613-534-15 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-534-15_)
[cos-121-18867-381-14 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-381-14_)
説明：今回のGKEリリースには、セキュリティ修正が含まれた最新のContainer-Optimized OS (COS) イメージを使用するGKEバージョンが含まれています。これらのCOSイメージには、前回のGKEリリース以降に公開された全てのCOSバージョンのセキュリティ修正が累積的に適用されています。
影響有無：影響なし（セキュリティ向上）。
GKEノードの基盤となるOSイメージがセキュリティ修正を含んだ最新版になるため、ノードのセキュリティ体制が強化されます。既存のワークロードに直接的な影響はありませんが、セキュリティ上のメリットがあります。
対処方法：GKEクラスタの自動アップグレードによって、これらのセキュリティ修正が適用されたCOSイメージがノードに適用されていきます。特別な対処は不要です。
用語説明：
*   **Container-Optimized OS (COS)**: Googleが提供する、コンテナの実行に特化し、セキュリティと信頼性を最適化したGoogle Compute Engineイメージです。GKEノードのOSとして使用されます。

### Change (Stable channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.2392000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel: [...]
- The following versions are no longer available in the Stable channel: [...]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [...]
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明：Stableリリースチャネルにおいて、クラスタ作成のデフォルトバージョン、利用可能になったバージョン、利用不可になったバージョンが更新されました。また、Stableチャネルに属する既存クラスタの自動アップグレードターゲットが変更され、コントロールプレーンおよびノードが新しいバージョンへ自動的にアップグレードされるようになります。
影響有無：影響あり。
*   **自動アップグレード対象のクラスタ**: Stableチャネルを使用しているGKEクラスタは、今回の変更により新しいバージョンへ自動的にアップグレードされる可能性があります。これにより、一時的なダウンタイムや、新しいKubernetesバージョンとの互換性問題が発生しないか確認が必要です。
*   **利用不可になったバージョンを利用中のクラスタ**: リストされた利用不可になったバージョンを現在使用しているStableチャネルのクラスタは、速やかにアップグレードの対象となります。
対処方法：
1.  **GKEクラスタのリリースチャネル確認**: 現在運用中のGKEクラスタがStableチャネルを使用しているか確認してください。
2.  **アップグレード計画の確認**: クラスタのメンテナンスウィンドウと除外期間が適切に設定されているか確認し、意図しないタイミングでのアップグレードを防いでください。
3.  **互換性テスト**: もし可能であれば、アップグレード先のバージョンでアプリケーションの互換性テストを実施することをお勧めします。
4.  **モニタリング**: アップグレード前後でクラスタのパフォーマンスやアプリケーションの稼働状況を注意深くモニタリングしてください。
用語説明：
*   **Stable channel (安定版チャネル)**: GKEのリリースチャネルの一つで、Kubernetesの新しいマイナーバージョンがリリースされた後、十分に安定性が確認されたバージョンを提供するチャネルです。本番環境での利用に適しています。
*   **Auto-upgrade (自動アップグレード)**: GKEクラスタのコントロールプレーンとノードが、選択したリリースチャネルのポリシーに従って自動的に新しいバージョンにアップグレードされる機能です。
*   **Maintenance exclusions (メンテナンス除外期間)**: GKEの自動アップグレードやメンテナンス活動を実行しない期間を設定する機能です。これにより、ビジネスのピーク時などの重要な期間に中断が発生するのを避けることができます。

### Change (Regular channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.4-gke.1047000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel: [...]
- The following versions are no longer available in the Regular channel: [...]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [...]
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明：Regularリリースチャネルにおいて、クラスタ作成のデフォルトバージョン、利用可能になったバージョン、利用不可になったバージョンが更新されました。また、Regularチャネルに属する既存クラスタの自動アップグレードターゲットが変更され、コントロールプレーンおよびノードが新しいバージョンへ自動的にアップグレードされるようになります。
影響有無：影響あり。
*   **自動アップグレード対象のクラスタ**: Regularチャネルを使用しているGKEクラスタは、今回の変更により新しいバージョンへ自動的にアップグレードされる可能性があります。Stableチャネルと同様に、ダウンタイムや互換性問題に注意が必要です。
*   **利用不可になったバージョンを利用中のクラスタ**: リストされた利用不可になったバージョンを現在使用しているRegularチャネルのクラスタは、速やかにアップグレードの対象となります。
対処方法：
1.  **GKEクラスタのリリースチャネル確認**: 現在運用中のGKEクラスタがRegularチャネルを使用しているか確認してください。
2.  **アップグレード計画の確認**: クラスタのメンテナンスウィンドウと除外期間が適切に設定されているか確認し、意図しないタイミングでのアップグレードを防いでください。
3.  **互換性テスト**: もし可能であれば、アップグレード先のバージョンでアプリケーションの互換性テストを実施することをお勧めします。
4.  **モニタリング**: アップグレード前後でクラスタのパフォーマンスやアプリケーションの稼働状況を注意深くモニタリングしてください。
用語説明：
*   **Regular channel (標準チャネル)**: GKEのリリースチャネルの一つで、Stableチャネルよりも早くKubernetesの新しいマイナーバージョンが提供されます。最新機能へのアクセスが早い反面、安定性検証期間が短いため、本番環境での利用には注意が必要です。

### Change (Rapid channel)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Rapid channel: [...]
- The following versions are no longer available in the Rapid channel: [...]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [...]
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明：Rapidリリースチャネルにおいて、利用可能になったバージョンと利用不可になったバージョンが更新されました。また、Rapidチャネルに属する既存クラスタの自動アップグレードターゲットが変更され、コントロールプレーンおよびノードが新しいバージョンへ自動的にアップグレードされるようになります。
影響有無：影響あり。
*   **自動アップグレード対象のクラスタ**: Rapidチャネルを使用しているGKEクラスタは、今回の変更により新しいバージョンへ自動的にアップグレードされる可能性があります。最新機能へのアクセスが早い一方で、互換性に関するテストが十分でない場合があるため、注意が必要です。
*   **利用不可になったバージョンを利用中のクラスタ**: リストされた利用不可になったバージョンを現在使用しているRapidチャネルのクラスタは、速やかにアップグレードの対象となります。
対処方法：
1.  **GKEクラスタのリリースチャネル確認**: 現在運用中のGKEクラスタがRapidチャネルを使用しているか確認してください。
2.  **アップグレード計画の確認**: クラスタのメンテナンスウィンドウと除外期間が適切に設定されているか確認し、意図しないタイミングでのアップグレードを防いでください。
3.  **互換性テスト**: Rapidチャネルは頻繁にバージョンが更新されるため、アプリケーションの互換性テストを継続的に実施することが特に重要です。
4.  **モニタリング**: アップグレード前後でクラスタのパフォーマンスやアプリケーションの稼働状況を注意深くモニタリングしてください。
用語説明：
*   **Rapid channel (速報チャネル)**: GKEのリリースチャネルの一つで、最も早くKubernetesの最新バージョンが提供されます。テストや開発目的での利用に適しており、本番環境での利用には慎重な検討が必要です。

### Change (General updates)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.4-gke.1047000 is now the default version for cluster creation.
- The following versions are now available: [...]
- The following node versions are now available: [...]
- The following versions are no longer available: [...]
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release: [...]
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
説明：クラスタ作成のデフォルトバージョン、利用可能なコントロールプレーンおよびノードのバージョン、そして利用不可になったバージョンが更新されました。また、各リリースチャネルに属するクラスタの自動アップグレードターゲットが変更されました。
影響有無：影響あり。
*   **新規クラスタ作成**: 新しいGKEクラスタを作成する際のデフォルトバージョンが変更されます。
*   **既存クラスタの自動アップグレード**: 利用中のリリースチャネルに応じて、既存のGKEクラスタ（コントロールプレーンおよびノード）が新しいバージョンへ自動的にアップグレードされます。これにより、サービスが一時的に中断する可能性や、新しいKubernetesバージョンとの非互換性によるアプリケーションの不具合発生リスクがあります。
*   **利用不可になったバージョン**: 現在利用不可になったバージョンを使用しているクラスタは、速やかに自動アップグレードの対象となるか、手動でのアップグレードが必要になります。サポート終了が近づいているバージョンの場合は、特に注意が必要です。
*   **Google Cloud Composer 2 (Compoer version 2.7.1、Airflow version 2.7.3)**: Google Cloud ComposerはGKEを基盤としているため、GKEのバージョン更新はComposerの基盤環境に影響を与える可能性があります。Composer 2.7.1/Airflow 2.7.3は一般的にGKE 1.25〜1.27で動作します。今回のリリースノートでアナウンスされたGKEバージョンはこれらよりも新しいため、現在のComposer環境が直接影響を受けることはありません。しかし、将来的なComposerのアップグレードにより、これらの新しいGKEバージョンが基盤として適用される可能性があります。
対処方法：
1.  **GKEクラスタのバージョン管理戦略の確認**: 使用しているGKEクラスタのリリースチャネル（Stable, Regular, Rapidなど）を確認し、自動アップグレードの挙動を理解してください。
2.  **メンテナンスウィンドウと除外期間の設定**: サービス影響を最小限に抑えるため、自動アップグレードが実行される時間帯をコントロールするメンテナンスウィンドウや除外期間を適切に設定してください。
3.  **アプリケーションの互換性検証**: アップグレード前に、可能な限り新しいGKEバージョン環境でアプリケーションの互換性テストを実施し、Breaking Changeがないか確認してください。Kubernetesのマイナーバージョンアップグレードでは、APIの非推奨化や削除、動作変更が含まれることがあります。
4.  **モニタリングとアラート**: アップグレード後もクラスタの状態、アプリケーションのパフォーマンス、エラーレートなどを継続的にモニタリングし、異常があった場合に迅速に対応できるようアラートを設定してください。
用語説明：
*   **Control plane (コントロールプレーン)**: Kubernetesクラスタを管理する主要なコンポーネント群（APIサーバー、スケジューラ、コントローラマネージャなど）で構成されます。
*   **Node (ノード)**: Kubernetesクラスタ内でコンテナ化されたワークロード（Pod）を実行するワーカーマシン（Compute Engine VMインスタンス）です。
*   **Deprecated APIs (非推奨API)**: Kubernetesのバージョンアップグレードに伴い、使用が推奨されなくなるAPIです。通常、次のメジャーバージョンで削除される可能性があるため、事前に代替APIへの移行が必要です。
*   **Maintenance windows (メンテナンスウィンドウ)**: GKEクラスタの自動アップグレードやその他のメンテナンス作業が実行されることを許可する時間帯です。