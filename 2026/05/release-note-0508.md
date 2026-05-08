
# Title: May 06, 2026 
Link: https://docs.cloud.google.com/release-notes#May_06_2026<br>
# BigQuery
## Breaking
原文: Starting June 1, 2026, due to changes in Google Ads data retention policies, the BigQuery Data Transfer Service connectors for Google Ads, Search Ads 360, and Google Analytics 4 will stop populating data for backfill runs with dates earlier than 37 months from the current date.

[Google Ads](https://docs.cloud.google.com/bigquery/docs/transfer-changes#June01-google-ads)
[Search Ads 360](https://docs.cloud.google.com/bigquery/docs/transfer-changes#June01-search-ads)
[Google Analytics 4](https://docs.cloud.google.com/bigquery/docs/transfer-changes#June01-ga4)
For more information about the changes to the Google Ads data retention policies, see New Data Retention Policy for Google Ads starting June 1, 2026.

[New Data Retention Policy for Google Ads starting June 1, 2026](https://ads-developers.googleblog.com/2026/05/new-data-retention-policy-for-google.html)

説明：Google Adsのデータ保持ポリシー変更に伴い、2026年6月1日以降、BigQuery Data Transfer ServiceのGoogle Ads、Search Ads 360、Google Analytics 4向けコネクタにおいて、現時点から37ヶ月より古い日付のバックフィル実行データは転送されなくなります。
影響有無：なし。
理由：
*   この変更は2026年6月1日以降に適用されるため、現時点での即時的な影響はありません。
*   この変更は、BigQuery Data Transfer Serviceのバックフィル機能を使用して、37ヶ月以上前の過去データをBigQueryに転送する場合にのみ影響します。既存の継続的なデータ転送や、37ヶ月以内のデータのバックフィルには影響ありません。
対処方法：もし将来的に2026年6月1日以降、Google Ads、Search Ads 360、Google Analytics 4から37ヶ月より古い日付の履歴データをBigQueryに転送するバックフィルが必要な場合は、各サービスのAPIなどを利用した別のデータ取得・インポート方法を検討する必要があります。
用語説明：
*   **BigQuery Data Transfer Service:** Google Cloudの様々なデータソース（例: Google Ads、Google Analytics）からBigQueryへデータを自動的に転送・ロードするフルマネージドサービスです。
*   **バックフィル (Backfill):** 通常の定期的なデータ転送スケジュールとは別に、過去の特定の期間に遡ってデータを転送し、不足しているデータを補完する操作を指します。
*   **データ保持ポリシー (Data Retention Policy):** データの保管期間や削除に関するルールを定めたポリシー。

---

# Cloud Composer
## Announcement
原文: Managed Airflow (Gen 2) environments can no longer be created in Johannesburg (africa-south1). We're switching this region to supporting only Managed Airflow (Gen 3) environments. Existing Managed Airflow (Gen 2) environments in this region aren't affected by this change.

説明：ヨハネスブルグ（`africa-south1`）リージョンにおいて、Managed Airflow (Gen 2) 環境の新規作成が不可能になります。このリージョンはManaged Airflow (Gen 3) 環境のみをサポートするよう切り替わります。既存の同リージョンのManaged Airflow (Gen 2) 環境は、この変更の影響を受けません。
影響有無：なし。
理由：
*   当社のCloud Composer環境はComposer version 2.7.1であり、これはManaged Airflow (Gen 2) に分類されます。
*   しかし、当社のデプロイリージョンはヨハネスブルグ（`africa-south1`）ではないため、この新規作成制限は現在の運用に影響しません。
*   既存のManaged Airflow (Gen 2) 環境は影響を受けないと明記されています。
対処方法：なし。ただし、将来的にヨハネスブルグ（`africa-south1`）リージョンで新規のCloud Composer環境（Gen 2）を構築する必要が生じた場合は、Managed Airflow (Gen 3) の使用を検討するか、別のリージョンを選択する必要があります。
用語説明：
*   **Cloud Composer:** Google Cloudが提供するApache Airflowをベースにしたマネージドワークフローオーケストレーションサービスです。
*   **Managed Airflow (Gen 2):** Cloud Composerの第2世代アーキテクチャで、パフォーマンス、スケーラビリティ、コスト効率が向上しています。
*   **Managed Airflow (Gen 3):** Cloud Composerの第3世代アーキテクチャで、Gen 2をさらに改良し、より高いスケーラビリティとリソース効率を提供します。

---

# Google Kubernetes Engine
## Change
原文: GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.

[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明：GKEクラスタの利用可能バージョンが更新され、新しいクラスタの作成および既存クラスタのコントロールプレーンやノードの手動アップグレード用に最新バージョンが提供開始されました。
影響有無：なし。
理由：新しいバージョンが利用可能になったという情報であり、既存クラスタの運用に即座に影響を与えるものではありません。これはGKEの通常のバージョン更新プロセスの一部です。
対処方法：なし。ただし、GKEクラスタの計画的なアップグレードを実施する際に、最新の安定バージョンへの更新を検討してください。

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.

To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:

GKE version
Container-Optimized OS version
Details


1.30.14-gke.2441000
cos-117-18613-534-106
cos-117-18613-534-106 release notes


1.31.14-gke.1850000
cos-117-18613-534-106
cos-117-18613-534-106 release notes


1.32.13-gke.1449000
cos-117-18613-534-106
cos-117-18613-534-106 release notes


1.33.11-gke.1137000
cos-121-18867-381-113
cos-121-18867-381-113 release notes


1.34.7-gke.1321000
cos-125-19216-220-180
cos-125-19216-220-180 release notes


1.35.3-gke.1993000
cos-125-19216-220-180
cos-125-19216-220-180 release notes


1.36.0-gke.1575000
cos-125-19216-220-180
cos-125-19216-220-180 release notes

[cos-117-18613-534-106 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-534-106_)
[cos-117-18613-534-106 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-534-106_)
[cos-117-18613-534-106 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-534-106_)
[cos-121-18867-381-113 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-381-113_)
[cos-125-19216-220-180 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-220-180_)
[cos-125-19216-220-180 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-220-180_)
[cos-125-19216-220-180 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-220-180_)

説明：今回のGKEリリースには、セキュリティ修正が適用されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらのイメージは、前回のGKEリリース以降にリリースされたすべてのCOSバージョンからの累積的なセキュリティ修正を含んでいます。
影響有無：なし（ポジティブな影響）。
理由：セキュリティパッチが含まれたCOSイメージが利用可能になったという情報であり、GKEクラスタのセキュリティ体制が向上します。既存の機能に悪影響を与えるものではありません。
対処方法：GKEクラスタのアップグレード計画に際し、これらのセキュリティ修正が適用されたバージョンへの更新を推奨します。これにより、クラスタのセキュリティが強化されます。
用語説明：
*   **Container-Optimized OS (COS):** Google Cloudが提供する、コンテナの実行に特化し最適化された軽量なLinuxベースのオペレーティングシステムです。セキュリティと信頼性を重視して設計されています。

## Fixed
原文: A fix is available for an issue that caused incomplete file reads and premature end-of-file (EOF) errors when you used the Cloud Storage FUSE CSI driver on ARM64 nodes that use 64 KiB page sizes, such as A4X and A4X Max instances. This issue occurred because the kernel read-ahead mechanism triggered read requests that exceeded the capacity of the Cloud Storage FUSE layer.

To resolve this issue, upgrade your cluster to one of the following versions:

- 1.33.11-gke.1019000 or later
- 1.34.6-gke.1154000 or later
- 1.35.2-gke.1485000 or later

説明：ARM64ノード（64 KiBページサイズを使用するA4XおよびA4X Maxインスタンスなど）でCloud Storage FUSE CSIドライバを使用する際に発生していた、不完全なファイル読み込みおよび予期せぬEOF（End-of-File）エラーの問題に対する修正が提供されました。この問題は、カーネルのリード・アヘッド機構がCloud Storage FUSEレイヤーの容量を超える読み込みリクエストをトリガーしていたために発生していました。
影響有無：なし。
理由：当社のGKEクラスタは、現在ARM64ノードを使用しておらず、かつCloud Storage FUSE CSIドライバも使用していないため、この修正による直接的な影響はありません。
対処方法：もし将来的にARM64ノードを使用し、Cloud Storage FUSE CSIドライバを利用するGKEクラスタを運用する場合には、上記に記載されたバージョン（1.33.11-gke.1019000以降、1.34.6-gke.1154000以降、1.35.2-gke.1485000以降）へクラスタをアップグレードすることを推奨します。
用語説明：
*   **Cloud Storage FUSE CSI driver:** Kubernetesクラスタ内でGoogle Cloud Storageバケットをファイルシステムとしてマウントすることを可能にするContainer Storage Interface (CSI) ドライバです。これにより、アプリケーションは通常のファイルシステム操作でCloud Storageのデータにアクセスできます。
*   **ARM64ノード:** ARMアーキテクチャベースのCPUを搭載したGKEノード。A4XおよびA4X Maxインスタンスなどが該当します。
*   **EOF (End-of-File) エラー:** ファイルの終端に達する前に読み取り操作が終了したことを示すエラーです。

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.34.6-gke.1068000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:

- 1.33.10-gke.1115000
- 1.34.6-gke.1154000
- 1.35.3-gke.1234000

- The following versions are no longer available in the Stable channel:

- 1.32.13-gke.1059000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.32.13-gke.1205000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.33.9-gke.1060000
- 1.34.5-gke.1076000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.2-gke.1269001 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.32 to 1.33.10-gke.1067000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.33 to 1.33.10-gke.1067000
- 1.34 to 1.34.6-gke.1068000
- 1.35 to 1.35.2-gke.1962000

[1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
- 1.33.10-gke.1115000
- 1.34.6-gke.1154000
- 1.35.3-gke.1234000

[1.33.10-gke.1115000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
[1.34.6-gke.1154000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
[1.35.3-gke.1234000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1353)
- 1.32.13-gke.1059000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.32.13-gke.1205000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.33.9-gke.1060000
- 1.34.5-gke.1076000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.2-gke.1269001 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
[deprecated](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support)
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.32 to 1.33.10-gke.1067000

[1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.33 to 1.33.10-gke.1067000
- 1.34 to 1.34.6-gke.1068000
- 1.35 to 1.35.2-gke.1962000

[1.33.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v13310)
[1.34.6-gke.1068000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1346)
[1.35.2-gke.1962000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md#v1352)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)

説明：GKE Stableチャネルにおけるバージョン更新についてのアナウンスです。1.34.6-gke.1068000が新しいデフォルトバージョンとなり、新しい利用可能バージョンが追加されました。同時に、一部のバージョンは非推奨となり、90日以内またはサポート終了時に削除されます。このリリースに伴い、自動アップグレードのターゲットバージョンも更新されました。
影響有無：なし。
理由：GKEのバージョンライフサイクルと自動アップグレードに関する通常の更新であり、既存クラスタの運用に即座に悪影響を与えるものではありません。非推奨バージョンを使用している場合、将来的なアップグレードが必要になる可能性があります。
対処方法：
*   現行のGKEクラスタがStableチャネルを使用しており、かつ非推奨となったバージョンを使用している場合は、今後の自動アップグレードまたは手動アップグレードの計画に含めてください。
*   GKEの自動アップグレードポリシーを理解し、メンテナンスウィンドウや除外設定が適切に構成されていることを確認してください。
用語説明：
*   **GKE リリースチャネル (Release Channels):** GKEクラスタのバージョンアップグレードの頻度と安定性を選択するためのオプション。`Stable`チャネルは最も安定性が高く、更新頻度が低いチャネルです。
*   **非推奨 (Deprecated):** 将来的にサポートが終了し、利用できなくなる予定の機能やバージョンを指します。

## Change
原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.3-gke.1389000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:

- 1.33.11-gke.1013000
- 1.34.6-gke.1307000

- The following versions are no longer available in the Regular channel:

- 1.32.13-gke.1258000
- 1.32.13-gke.1318000
- 1.33.10-gke.1115000
- 1.34.6-gke.1154000
- 1.35.3-gke.1234000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes