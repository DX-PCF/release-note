
# Title: June 30, 2026 
Link: https://docs.cloud.google.com/release-notes#June_30_2026<br>
Google Cloud のリリースノートの分析をご依頼いただきありがとうございます。

ご提示いただいた「# Cloud SDK ## Change」の項目について、リリースノートの本文（英語原文）が不足しております。

恐れ入りますが、該当するリリースノートの本文（英語原文）をご提供いただけますでしょうか。原文を拝見でき次第、指定された形式に沿って、説明、影響有無、対処方法、および用語説明を速やかに調査し、ご回答いたします。
# Title: June 29, 2026 
Link: https://docs.cloud.google.com/release-notes#June_29_2026<br>
Google Cloudインフラエンジニアとして、ご提供いただいたリリースノートに基づき、構築済みのサービス（Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)）への影響を調査し、以下の通りご回答いたします。

---

# BigQuery

## Change

原文: Effective *March 9, 2026*, new users are required to have a Cloud Billing
account to use the BigQuery Migration Service.
This change applies to users starting new projects using BigQuery Migration
Service features, such as SQL translation and migration assessment.

[BigQuery Migration Service](https://docs.cloud.google.com/bigquery/docs/migration-intro)
After *May 18, 2026*, all users are required to have a Cloud Billing account to
use the BigQuery Migration Service.

Pricing for the BigQuery Migration Service
remains without charge.

[Pricing for the BigQuery Migration Service](https://docs.cloud.google.com/bigquery/docs/migration-intro#pricing)

説明：
2026年3月9日以降、BigQuery Migration Serviceを新規プロジェクトで利用する際にはCloud Billingアカウントが必須となります。2026年5月18日以降は、既存ユーザーを含む全てのBigQuery Migration Service利用者にCloud Billingアカウントが必須となります。なお、BigQuery Migration Service自体の料金は引き続き無料です。

影響有無：
**影響なし**
理由：現在ご利用のGoogle Cloud Composer2 (Airflow) は、BigQueryのデータウェアハウス移行支援サービスであるBigQuery Migration Serviceを直接利用するものではありません。また、お客様の現行のシステム運用においてBigQuery Migration Serviceを利用する計画がないため、直接的な影響はありません。

対処方法：
特になし。将来的にBigQuery Migration Serviceの利用を検討する際には、Cloud Billingアカウントが必須となる点を考慮してください。

用語説明：
*   **BigQuery Migration Service**: 既存のデータウェアハウス（Teradata, Netezza, Oracleなど）からBigQueryへの移行を支援するサービスです。SQLの自動変換や移行アセスメント機能を提供します。
*   **Cloud Billing Account**: Google Cloudサービスの利用料金を管理・支払うためのアカウントです。各Google CloudプロジェクトはCloud Billingアカウントに紐付けられます。

---

# Cloud Service Mesh

## Security

原文: **1.29.5-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in
GCP-2026-045.

[GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.29.5-asm.5 uses Envoy v1.37.5.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：
Cloud Service Meshのバージョン1.29.5-asm.5がリリースされました。このパッチリリースには、セキュリティ脆弱性GCP-2026-045の修正が含まれています。このバージョンはEnvoy v1.37.5を使用しています。

影響有無：
**影響なし**
理由：Google Cloud Composerはマネージドサービスであり、基盤としてGoogle Kubernetes Engine (GKE) を利用していますが、Cloud Service Mesh（Istioをベースとしたサービスメッシュ）はComposerのAirflow環境に直接組み込まれるコンポーネントではありません。したがって、このセキュリティパッチリリースはComposerの運用に直接影響を与えません。

対処方法：
特になし。ただし、お客様のGKEクラスターでCloud Service Meshを個別に導入している場合は、GCP-2026-045のセキュリティ脆弱性に対応するため、該当するバージョンのCloud Service Meshへのアップグレードを検討してください。

用語説明：
*   **Cloud Service Mesh (CSM)**: Google Cloudが提供する、Istioベースのフルマネージドなサービスメッシュプラットフォームです。マイクロサービス間の通信、トラフィック管理、セキュリティポリシー適用、可観測性などを実現します。
*   **Envoy**: 高性能なオープンソースのL7プロキシおよび通信バスです。Cloud Service Meshのデータプレーンとして、マイクロサービス間の通信を仲介します。

---

## Security

原文: **1.28.9-asm.4 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in
GCP-2026-045.

[GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.28.9-asm.4 uses Envoy v1.36.9.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)

説明：
Cloud Service Meshのバージョン1.28.9-asm.4がリリースされました。このパッチリリースには、セキュリティ脆弱性GCP-2026-045の修正が含まれています。このバージョンはEnvoy v1.36.9を使用しています。

影響有無：
**影響なし**
理由：上記と同様に、Google Cloud ComposerはCloud Service Meshを直接利用しないため、このセキュリティパッチリリースはComposerの運用に直接影響を与えません。

対処方法：
特になし。お客様のGKEクラスターでCloud Service Meshを個別に導入している場合は、GCP-2026-045のセキュリティ脆弱性に対応するため、該当するバージョンのCloud Service Meshへのアップグレードを検討してください。

用語説明：
*   **Cloud Service Mesh (CSM)**: Google Cloudが提供する、Istioベースのフルマネージドなサービスメッシュプラットフォームです。
*   **Envoy**: 高性能なオープンソースのL7プロキシおよび通信バスです。

---

## Security

原文: **1.27.9-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in
GCP-2026-045.

[GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.27.9-asm.9 uses Envoy v1.35.13.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade)

説明：
Cloud Service Meshのバージョン1.27.9-asm.9がリリースされました。このパッチリリースには、セキュリティ脆弱性GCP-2026-045の修正が含まれています。このバージョンはEnvoy v1.35.13を使用しています。

影響有無：
**影響なし**
理由：上記と同様に、Google Cloud ComposerはCloud Service Meshを直接利用しないため、このセキュリティパッチリリースはComposerの運用に直接影響を与えません。

対処方法：
特になし。お客様のGKEクラスターでCloud Service Meshを個別に導入している場合は、GCP-2026-045のセキュリティ脆弱性に対応するため、該当するバージョンのCloud Service Meshへのアップグレードを検討してください。

用語説明：
*   **Cloud Service Mesh (CSM)**: Google Cloudが提供する、Istioベースのフルマネージドなサービスメッシュプラットフォームです。
*   **Envoy**: 高性能なオープンソースのL7プロキシおよび通信バスです。

---

## Security

原文: Proxy version csm_mesh_proxy.csm_mesh_proxy.20260624e_RC01 for Gateway API on
GKE clusters is rolling out to all Managed Cloud Service Mesh release channels
over the next week.

This patch release contains the fixes for the security vulnerabilities listed in
GCP-2026-040.

[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)

説明：
GKEクラスター上のGateway API向けCloud Service Meshのプロキシバージョンcsm_mesh_proxy.csm_mesh_proxy.20260624e_RC01が、今後1週間ですべてのManaged Cloud Service Meshリリースチャネルに展開されます。このパッチリリースには、セキュリティ脆弱性GCP-2026-040の修正が含まれています。

影響有無：
**影響なし**
理由：上記と同様に、Google Cloud ComposerはCloud Service Meshを直接利用しないため、このセキュリティパッチリリースはComposerの運用に直接影響を与えません。

対処方法：
特になし。お客様のGKEクラスターでCloud Service MeshとGateway APIを個別に導入している場合は、GCP-2026-040のセキュリティ脆弱性に対応するため、適用されるプロキシバージョンへのアップデートを確認してください。

用語説明：
*   **Gateway API**: Kubernetesにおける外部トラフィック（Ingress）を管理するための新しい標準APIです。より柔軟で表現力豊かなトラフィックルーティングを提供します。
*   **Managed Cloud Service Mesh**: Googleによって完全に管理されるCloud Service Meshのデプロイメントオプションです。

---

# Google Kubernetes Engine

## Change

原文: GKE cluster versions have been updated.

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

説明：
GKEクラスターのバージョンが更新されました。新しいGKEクラスターの作成や、既存クラスターの手動アップグレード（コントロールプレーンおよびノード）で利用可能なバージョンが追加されています。GKEのバージョン管理とアップグレードに関する詳細情報は、提供されたリンクを参照してください。

影響有無：
**限定的な影響（基盤のセキュリティ向上）**
理由：Google Cloud Composer2はGKE上に構築されたマネージドサービスです。Composer 2.7.1はGKEバージョン1.25.x、1.26.x、1.27.x、1.28.xをサポートしています。今回のリリースノートで言及されているGKEバージョン（1.30.xから1.36.x）は、現在のComposerバージョンがサポートする範囲よりも新しいです。

したがって、お客様のComposer環境が現在のところこれらのGKEバージョンに直接アップグレードされることはありません。Composerはサポート対象のGKEバージョン範囲内でGKEを管理するため、サポート対象外のGKEバージョンに自動的にアップグレードされることはありません。

しかし、GKE基盤のバージョンが定期的に更新され、新しいバージョンが利用可能になることは、将来のComposerバージョンアップグレードや機能改善の基盤となります。

対処方法：
特になし。Composerのマネージドサービスとしての特性上、GKEのバージョンアップはGoogle Cloud側で管理されます。Composerのバージョンアップを検討する際は、最新のComposerバージョンがサポートするGKEバージョン範囲を確認してください。

用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービスです。Kubernetesクラスターのデプロイ、管理、スケーリングを自動化します。
*   **Control Plane**: Kubernetesクラスターを管理するコンポーネント群（APIサーバー、スケジューラー、コントローラーマネージャーなど）の総称です。
*   **Node**: Kubernetesクラスターにおいて、アプリケーション（Pod）が実行される仮想マシンまたは物理マシンです。

---

## No channel (deprecated)

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.5-gke.1163012 is now the default version for cluster creation.
- The following versions are now available:
... (中略) ...
- The following versions are no longer available:

- 1.33.11-gke.1197000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.7-gke.1055000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.3-gke.2190000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1000000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.0-gke.2459000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.0-gke.3302001 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
... (後略) ...

説明：
GKEの「No channel」（特定のリリースチャネルに属さない）におけるバージョン更新情報です。新しいクラスター作成時のデフォルトバージョンが1.35.5-gke.1163012になりました。また、いくつかの新しいバージョンが利用可能になり、同時に複数の古いバージョンが非推奨（deprecated）となりました。非推奨のバージョンは、90日以内、またはサポート終了時に削除されます。

影響有無：
**影響なし**
理由：Google Cloud Composer 2.7.1がサポートするGKEバージョン（1.25.x、1.26.x、1.27.x、1.28.x）は、今回非推奨となったバージョン群（1.33.x以降）とは異なるため、お客様のComposer環境がこれらの非推奨バージョンを使用している可能性は極めて低いです。Composerはサポート対象のGKEバージョン範囲内でGKEを管理します。

対処方法：
特になし。

用語説明：
*   **Deprecated (非推奨)**: その機能やバージョンが将来的に削除されるか、新しいものに置き換えられることを意味します。引き続き使用できますが、新しい利用は推奨されず、将来的な移行計画が必要です。

---

## Security

原文: This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:
... (中略) ...

説明：
今回のGKEリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらのCOSイメージには、前回のGKEリリース以降に公開された全てのCOSバージョンからのセキュリティ修正が累積的に適用されています。各COSイメージで修正された具体的な脆弱性については、提供されたリンクからCOSのリリースノートを参照できます。

影響有無：
**ポジティブな影響（基盤のセキュリティ向上）**
理由：Google Cloud Composerが動作するGKEクラスターのノードは、Container-Optimized OSを使用しています。今回のGKEリリースに含まれるCOSイメージのセキュリティアップデートは、GKEノードのOSレベルでのセキュリティを向上させるものであり、お客様のComposer環境の基盤のセキュリティ体制強化に貢献します。

対処方法：
特になし。このセキュリティアップデートはComposerのマネージドサービスの一部として自動的に適用されます。

用語説明：
*   **Container-Optimized OS (COS)**: Googleが開発した、コンテナ実行に最適化されたChrome OSベースのオペレーティングシステムです。セキュリティ、信頼性、スケーラビリティに優れています。GKEノードのデフォルトOSとして利用されます。

---

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.34.8-gke.1000000 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
... (中略) ...
- The following versions are no longer available in the Stable channel:

- 1.33.11-gke.1197000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.7-gke.1499000
- 1.35.3-gke.2190000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
... (後略) ...

説明：
GKEのStableチャネルにおけるバージョン更新情報です。新しいクラスター作成時のデフォルトバージョンが1.34.8-gke.1000000になりました。Stableチャネルで利用可能な新しいバージョンが追加され、同時に一部の古いバージョンが非推奨となりました。

影響有無：
**影響なし**
理由：Google Cloud Composer 2.7.1がサポートするGKEバージョン（1.25.x、1.26.x、1.27.x、1.28.x）は、今回非推奨となったバージョン群（1.33.x、1.34.x、1.35.x）とは異なるため、お客様のComposer環境がこれらの非推奨バージョンを使用している可能性は極めて低いです。Composerはサポート対象のGKEバージョン範囲内でGKEを管理します。

対処方法：
特になし。

用語説明：
*   **Release Channel (GKE)**: GKEクラスターのアップグレードポリシーを管理するための仕組みです。新しいバージョンの提供頻度と安定性の度合いによって、Rapid、Regular、Stable、Extendedの4つのチャネルがあります。Stableチャネルは安定性を重視し、十分なテスト期間を経たバージョンが提供されます。

---

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.5-gke.1163012 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
... (中略) ...
- The following versions are no longer available in the Regular channel:

- 1.33.12-gke.1059000
- 1.34.8-gke.1126000
- 1.35.5-gke.1057002
- 1.36.0-gke.2459000 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
... (後略) ...

説明：
GKEのRegularチャネルにおけるバージョン更新情報です。新しいクラスター作成時のデフォルトバージョンが1.35.5-gke.1163012になりました。Regularチャネルで利用可能な新しいバージョンが追加され、同時に一部の古いバージョンが非推奨となりました。

影響有無：
**影響なし**
理由：Google Cloud Composer 2.7.1がサポートするGKEバージョン（1.25.x、1.26.x、1.27.x、1.28.x）は、今回非推奨となったバージョン群（1.33.x以降）とは異なるため、お客様のComposer環境がこれらの非推奨バージョンを使用している可能性は極めて低いです。

対処方法：
特になし。

用語説明：
*   **Regular Channel (GKE)**: GKEのリリースチャネルの一つです。Stableチャネルよりも新しい機能を早く利用できますが、Rapidチャネルよりは安定性が高いバランスの取れたチャネルです。

---

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.36.0-gke.3302004 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
... (中略) ...
- The following versions are no longer available in the Rapid channel:

- 1.33.12-gke.1165000
- 1.34.8-gke.1278000
- 1.35.5-gke.1241004
- 1.36.0-gke.3070003
- 1.36.0-gke.3302001 is deprecated in the Rapid channel. This version will be removed in 90 days, or at the end of support, if sooner.
... (後略) ...

説明：
GKEのRapidチャネルにおけるバージョン更新情報です。新しいクラスター作成時のデフォルトバージョンが1.36.0-gke.3302004になりました。Rapidチャネルで利用可能な新しいバージョンが追加され、同時に一部の古いバージョンが非推奨となりました。

影響有無：
**影響なし**
理由：Google Cloud Composer 2.7.1がサポートするGKEバージョン（1.25.x、1.26.x、1.27.x、1.28.x）は、今回非推奨となったバージョン群（1.33.x以降）とは異なるため、お客様のComposer環境がこれらの非推奨バージョンを使用している可能性は極めて低いです。

対処方法：
特になし。

用語説明：
*   **Rapid Channel (GKE)**: GKEのリリースチャネルの一つです。最も早く最新のGKEバージョンが提供されますが、安定性よりも新機能の提供を優先します。

---

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.5-gke.1163012 is now the default version for cluster creation.
- The following versions are now available:
... (中略) ...
- The following node versions are now available:
... (中略) ...
- The following versions are no longer available:

- 1.33.11-gke.1197000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.34.7-gke.1055000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.3-gke.2190000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.5-gke.1000000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.0-gke.2459000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.0-gke.3302001 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
... (後略) ...

説明：
GKEの「No channel」におけるバージョン更新情報です。新しいクラスター作成時のデフォルトバージョンが1.35.5-gke.1163012になりました。新しいコントロールプレーンおよびノードバージョンが利用可能になり、同時に複数の古いバージョンが非推奨となりました。

影響有無：
**影響なし**
理由：上記のGKEバージョン更新と同様に、Composer 2.7.1がサポートするGKEバージョンとは異なるため、直接的な影響はありません。Composerはサポート対象のGKEバージョン範囲内でGKEを管理します。

対処方法：
特になし。

用語説明：
*   **Node Version**: GKEクラスターのワーカーノードが実行するKubernetesのバージョンです。コントロールプレーンのバージョンと互換性のある範囲で選択されます。

---

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.5-gke.1163012 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:
... (中略) ...
- The following versions are no longer available in the Extended channel:

- 1.30.14-gke.2558000 is deprecated in the Extended channel. This version will be removed in 90 days, or at the end of support,