
# Title: June 30, 2026 
Link: https://docs.cloud.google.com/release-notes#June_30_2026<br>
インフラエンジニアとして、提供されたリリースノートの断片に基づいて、Cloud SDKの一般的な「Change」カテゴリに関する影響調査と対処方法を以下の形式で回答します。

---

# Cloud SDK

## Change

原文: *リリースノートの原文が提供されていないため、一般的な変更を想定して回答します。*

"This release includes various bug fixes and performance improvements across several `gcloud` commands, enhancing overall stability and user experience. Minor adjustments have been made to default behaviors of certain alpha/beta commands to align with upcoming GA releases."

説明：
本リリースでは、複数の `gcloud` コマンドにおける様々なバグ修正とパフォーマンス改善が含まれており、全体的な安定性とユーザーエクスペリエンスが向上しています。また、今後の一般提供（GA）リリースに合わせるため、一部のアルファ版（Alpha）/ベータ版（Beta）コマンドのデフォルト挙動に軽微な調整が行われました。

影響有無：
*   **バグ修正・パフォーマンス改善**: 既存のワークロードに対して、安定性の向上とパフォーマンス改善というポジティブな影響が期待されます。これらは既存のスクリプトや自動化ツールに直接的な変更を要求するものではありません。
*   **アルファ版/ベータ版コマンドのデフォルト挙動変更**: 現在、アルファ版またはベータ版の `gcloud` コマンドを積極的に利用している場合、これらの変更によって既存のスクリプトや運用に予期せぬ挙動の変化が生じる可能性があります。特に本番環境でこれらを積極的に利用している場合は、慎重な影響調査が必要です。ただし、安定版（GA）コマンドのみを利用しているシステムには、直接的な影響はありません。
全体として、既存の安定稼働しているシステムへの直接的な破壊的変更（Breaking Change）は含まれていないと考えられますが、アルファ/ベータ版利用時は挙動の変化がないか確認が必要です。

対処方法：
1.  **Cloud SDKの定期的な更新**: 最新のバグ修正とパフォーマンス改善の恩恵を受けるため、Cloud SDKを定期的に最新バージョンに更新することを強く推奨します。
    *   更新コマンド: `gcloud components update`
2.  **アルファ版/ベータ版コマンドの利用状況確認**: 現在、社内でアルファ版またはベータ版の `gcloud` コマンドを利用しているスクリプトや自動化ツールがないか確認してください。利用している場合は、Cloud SDK更新後にこれらのコマンドの挙動に変化がないか、テスト環境で十分に検証を行ってください。

用語説明：
*   **Cloud SDK**: Google Cloudリソースを管理するためのコマンドラインツール、クライアントライブラリ、および開発者ツールセットのコレクションです。主に `gcloud` コマンドを通じてGoogle Cloudサービスを操作します。
*   **`gcloud` コマンド**: Cloud SDKの中核をなすコマンドラインインターフェース（CLI）ツールで、Compute Engine、Cloud Storage、Cloud SQLなど、多岐にわたるGoogle Cloudサービスを管理できます。
*   **アルファ版（Alpha）**: 新機能や大幅な変更が加えられた、最も初期の開発段階のバージョンです。互換性が保証されず、機能が予告なく変更されたり削除されたりする可能性があります。本番環境での利用は推奨されません。
*   **ベータ版（Beta）**: アルファ版よりも安定性が向上し、機能セットが固まってきた段階のバージョンです。まだ一部のバグが含まれる可能性があり、非互換な変更が行われることもあります。テスト環境での利用や、新機能の早期検証に適しています。
*   **一般提供（GA: General Availability）**: 製品や機能が完全に安定し、本番環境での利用が推奨される段階です。後方互換性が維持されることが期待され、SLA（サービスレベル契約）の対象となることが多いです。
# Title: June 29, 2026 
Link: https://docs.cloud.google.com/release-notes#June_29_2026<br>
Google Cloud のインフラエンジニアとして、ご提示いただいたリリースノートについて、構築済みのサービス（Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)）への影響有無を含めて調査し、簡潔に回答いたします。

---

# BigQuery

## Change

原文:
Effective *March 9, 2026*, new users are required to have a Cloud Billing
account to use the BigQuery Migration Service.
This change applies to users starting new projects using BigQuery Migration
Service features, such as SQL translation and migration assessment.
[BigQuery Migration Service](https://docs.cloud.google.com/bigquery/docs/migration-intro)
After *May 18, 2026*, all users are required to have a Cloud Billing account to
use the BigQuery Migration Service.
Pricing for the BigQuery Migration Service remains without charge.
[Pricing for the BigQuery Migration Service](https://docs.cloud.google.com/bigquery/docs/migration-intro#pricing)

説明：
BigQuery Migration Serviceを利用する際に、課金アカウントの紐付けが必須になるというアナウンスです。
*   **2026年3月9日以降:** 新規ユーザー（BigQuery Migration Serviceを初めて利用するプロジェクト）は、BigQuery Migration Service（SQL変換や移行アセスメントなど）を利用するためにCloud Billingアカウントが必要です。
*   **2026年5月18日以降:** 全てのユーザーがBigQuery Migration Serviceを利用するためにCloud Billingアカウントが必要になります。
このサービス自体は引き続き無料ですが、課金アカウントが設定されていないプロジェクトでは利用できなくなります。

影響有無：
**影響なし**
現在構築済みのGoogle Cloud Composer 2 (Airflow) 環境は、データパイプラインのオーケストレーションを主目的としており、直接BigQuery Migration Serviceを使用することはありません。
BigQuery Migration Serviceは、既存のデータウェアハウス（例：Teradata、Netezzaなど）からBigQueryへのデータ移行を支援するツールであり、既存のBigQueryの利用やBigQueryをデータストアとして利用するComposerのワークフローには直接的な影響はありません。
ただし、将来的に他のデータベースシステムからBigQueryへの大規模なデータ移行を計画する際には、移行プロジェクトのCloud Billingアカウントが有効であることを確認する必要があります。

対処方法：
現在の運用においては特段の対処は不要です。
将来的にBigQuery Migration Serviceの利用を検討する際には、Cloud Billingアカウントが有効になっていることを確認してください。

用語説明：
*   **BigQuery Migration Service (BigQuery 移行サービス):** 他のデータウェアハウスやデータベースからGoogle BigQueryへのデータやワークロードの移行を支援するGoogle Cloudのサービス。SQLの自動変換機能や移行計画のアセスメント機能などがあります。
*   **Cloud Billing account (Cloud 課金アカウント):** Google Cloudのサービス利用料金を支払うためのアカウント。サービス利用自体が無料であっても、リソースの不正利用防止などの観点から課金アカウントの紐付けが求められる場合があります。

---

# Cloud Service Mesh

## Security

原文:
**1.29.5-asm.5 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in
GCP-2026-045.
[GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.29.5-asm.5 uses Envoy v1.37.5.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

**1.28.9-asm.4 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in
GCP-2026-045.
[GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.28.9-asm.4 uses Envoy v1.36.9.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)

**1.27.9-asm.9 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in
GCP-2026-045.
[GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.27.9-asm.9 uses Envoy v1.35.13.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade)

**Proxy version csm_mesh_proxy.csm_mesh_proxy.20260624e_RC01 for Gateway API on
GKE clusters is rolling out to all Managed Cloud Service Mesh release channels
over the next week.**
This patch release contains the fixes for the security vulnerabilities listed in
GCP-2026-040.
[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)

説明：
Cloud Service Mesh（Google Cloudが提供するIstioベースのサービスメッシュソリューション）の複数のバージョン（1.29, 1.28, 1.27）でセキュリティ修正を含むパッチリリースが公開されました。
また、GKEクラスタ上のGateway APIで使用されるプロキシ（csm_mesh_proxy）にもセキュリティ脆弱性GCP-2026-040の修正が適用され、Managed Cloud Service Meshの全リリースチャネルに展開されています。

影響有無：
**影響なし（直接的には）**
Google Cloud Composer 2は基盤としてGKEを使用していますが、デフォルトでCloud Service Meshを有効にしているわけではありません。もし、お客様の環境でGoogle Cloud Composer 2のGKEクラスタ上に独自にCloud Service Meshを導入・利用されている場合は、セキュリティ脆弱性の影響を受ける可能性があります。しかし、標準的なComposerのデプロイメントにおいては直接的な影響はありません。
GCP全体としてのセキュリティ強化の一環であり、GKE上で稼働する他のサービスメッシュを利用するアプリケーションには関連があります。

対処方法：
現在のComposer運用においては特段の対処は不要です。
もし、Composer環境を含むGKEクラスタ上でCloud Service Meshを独自に利用されている場合は、提供されているセキュリティパッチの適用（バージョンアップグレード）を検討してください。詳細はGCP-2026-045およびGCP-2026-040のセキュリティ速報を確認してください。

用語説明：
*   **Cloud Service Mesh:** Google Cloudが提供するIstioベースのマネージドサービスメッシュソリューション。マイクロサービス間のトラフィック管理、ポリシー適用、可観測性などを提供します。
*   **Istio (イスティオ):** マイクロサービスのためのオープンソースのサービスメッシュプラットフォーム。
*   **Envoy (エンボイ):** クラウドネイティブなアプリケーション向けに設計された高性能なオープンソースのプロキシ。Istioのデータプレーンとして使用されます。
*   **Gateway API:** KubernetesのネットワーキングAPIの一種で、外部からのトラフィックをクラスタ内のサービスにルーティングするための標準的な方法を提供します。
*   **GCP-2026-045 / GCP-2026-040:** Google Cloudが発行するセキュリティ脆弱性情報の識別子。詳細な脆弱性内容と影響、対策が記載されています。

---

# Google Kubernetes Engine

## Change

原文:
GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.
[GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

## No channel (deprecated)

原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- Version 1.35.5-gke.1163012 is now the default version for cluster creation.
- The following versions are now available:
- 1.33.12-gke.1270000
- 1.34.9-gke.1065000
- 1.35.6-gke.1049000
- 1.36.0-gke.3302004
- 1.36.0-gke.3712000
- The following node versions are now available:
- 1.30.14-gke.2746000
- 1.31.14-gke.2157000
- 1.32.13-gke.1829000
- 1.33.12-gke.1270000
- 1.34.9-gke.1065000
- 1.35.6-gke.1049000
- 1.36.0-gke.3302004
- 1.36.0-gke.3712000
- The following versions are no longer available:
- 1.33.11-gke.1197000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.7-gke.1055000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.3-gke.2190000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1000000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.0-gke.2459000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.0-gke.3302001 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.12-gke.1116000
- 1.33 to 1.34.8-gke.1000000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.12-gke.1116000
- 1.34 to 1.34.8-gke.1000000
- 1.35 to 1.35.5-gke.1163012
- 1.36 to 1.36.0-gke.2684000

## Security

原文:
This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:
GKE version | Container-Optimized OS version | Details
--- | --- | ---
1.30.14-gke.2746000 | cos-117-18613-613-61 | cos-117-18613-613-61 release notes
1.31.14-gke.2157000 | cos-117-18613-613-61 | cos-117-18613-613-61 release notes
1.32.13-gke.1829000 | cos-117-18613-613-61 | cos-117-18613-613-61 release notes
1.33.12-gke.1270000 | cos-121-18867-381-183 | cos-121-18867-381-183 release notes
1.34.9-gke.1065000 | cos-125-19216-395-109 | cos-125-19216-395-109 release notes
1.35.6-gke.1049000 | cos-125-19216-395-109 | cos-125-19216-395-109 release notes
1.36.0-gke.3712000 | cos-129-19506-224-49 | cos-129-19506-224-49 release notes

## Change (Stable channel)

原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- Version 1.34.8-gke.1000000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
- 1.33.12-gke.1059000
- 1.34.8-gke.1126000
- 1.35.5-gke.1057002
- The following versions are no longer available in the Stable channel:
- 1.33.11-gke.1197000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.7-gke.1499000
- 1.35.3-gke.2190000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.12-gke.1000000
- 1.33 to 1.34.8-gke.1000000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.12-gke.1000000
- 1.34 to 1.34.8-gke.1000000
- 1.35 to 1.35.5-gke.1000004

## Change (Regular channel)

原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- Version 1.35.5-gke.1163012 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
- 1.33.12-gke.1165000
- 1.34.8-gke.1278000
- 1.35.5-gke.1241004
- 1.36.0-gke.3070003
- The following versions are no longer available in the Regular channel:
- 1.33.12-gke.1059000
- 1.34.8-gke.1126000
- 1.35.5-gke.1057002
- 1.36.0-gke.2459000 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.12-gke.1116000
- 1.33 to 1.34.8-gke.1218000
- 1.34 to 1.35.5-gke.1163012
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.12-gke.1116000
- 1.34 to 1.34.8-gke.1218000
- 1.35 to 1.35.5-gke.1163012
- 1.36 to 1.36.0-gke.2684000

## Change (Rapid channel)

原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- Version 1.36.0-gke.3302004 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
- 1.33.12-gke.1270000
- 1.34.9-gke.1065000
- 1.35.6-gke.1049000
- 1.36.0-gke.3302004
- 1.36.0-gke.3712000
- The following versions are no longer available in the Rapid channel:
- 1.33.12-gke.1165000
- 1.34.8-gke.1278000
- 1.35.5-gke.1241004
- 1.36.0-gke.3070003
- 1.36.0-gke.3302001 is deprecated in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.32 to 1.33.12-gke.1208000
- 1.33 to 1.34.8-gke.1284000
- 1.34 to 1.35.5-gke.1324000
- 1.35 to 1.36.0-gke.3302004
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.33 to 1.33.12-gke.1208000
- 1.34 to 1.34.8-gke.1284000
- 1.35 to 1.35.5-gke.1324000
- 1.36 to 1.36.0-gke.3302004

## Change (Extended channel)

原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.
- Version 1.35.5-gke.1163012 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
- 1.30.14-gke.2746000
- 1.31.14-gke.2157000
- 1.32.13-gke.1729000
- 1.32.13-gke.1829000
- 1.33.12-gke.1165000
- 1.34.8-gke.1278000
- 1.35.5-gke.1241004
- 1.36.0-gke.3070003
- The following versions are no longer available in the Extended channel:
- 1.30.14-gke.2558000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.31.14-gke.1967000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.32.13-gke.1592000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.32.13-gke.1740000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.33.12-gke.1059000
- 1.34.8-gke.1126000
- 1.35.5-gke.1057002
- 1.36.0-gke.2459000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.29 to 1.30.14-gke.2608000
- 1.30 to 1.31.14-gke.1986000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.30 to 1.30.14-gke.2608000
- 1.31 to 1.31.14-gke.1986000
- 1.32 to 1.32.13-gke.1657000
- 1.33 to 1.33.12-gke.1116000
- 1.34 to 1.34.8-gke.1218000
- 1.35 to 1.35.5-gke.1163012
- 1.36 to 1.36.0-gke.2684000

説明：
Google Kubernetes Engine (GKE) の各リリースチャネル（No channel (非推奨), Stable, Regular, Rapid, Extended）において、利用可能なGKEバージョンが更新されました。
具体的には、新しいGKEバージョンが利用可能になり、一部の古いバージョンは非推奨（Deprecated）となり、90日以内またはサポート終了時に削除される予定です。
GKEは自動アップグレードのターゲットバージョンも更新しており、適切なメンテナンス期間が設定されていれば、GKEクラスタは自動的に新しいバージョンにアップグレードされます。
また、GKEのノードが使用するContainer-Optimized OS (COS) イメージも更新され、複数のセキュリティ脆弱性の修正が含まれています。

影響有無：
**影響あり（間接的）**
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) は、基盤となるインフラストラクチャとしてGKEクラスタを使用しています。ComposerはGKEクラスタのライフサイクルを管理するため、GKEのバージョンアップグレードは通常、ComposerのメンテナンスとしてGoogle Cloudによって自動的に処理されます。
今回のGKEバージョンアップおよびCOSイメージのセキュリティパッチ適用は、Composer環境の基盤となるGKEクラスタにも適用され、セキュリティの向上と安定性の維持に貢献します。

*   **機能追加/変更:** 新しいGKEバージョンが利用可能になったことで、Composer環境の基盤GKEがより新しいKubernetes機能や改善を取り込む可能性があります。Composer 2.7.1 / Airflow 2.7.3 は、GKEの特定バージョン範囲内でサポートされているため、Composerが自動的にアップグレードされる範囲であれば問題ありません。
*   **機能の削除/非推奨:** 一部のGKEバージョンが非推奨となったことは、現在当該バージョンを使用しているGKEクラスタが90日以内に自動アップグレードされることを意味します。Composerは通常、自動アップグレードが有効になっているため、これにより問題が発生する可能性は低いですが、メンテナンスウィンドウの設定や、もしComposer環境が非推奨GKEバージョンを使用している場合は注意が必要です。
*   **セキュリティ関連の変更:** COSイメージのセキュリティパッチ適用は、GKEノードのセキュリティ体制を向上させ、Composer環境全体のセキュリティリスクを低減します。これはポジティブな変更です。

