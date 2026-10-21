
# Title: October 20, 2026 
Link: https://docs.cloud.google.com/release-notes#October_20_2026<br>
Google Cloudのリリースノートに関する調査結果を以下に報告します。

---

# Apigee X

## Announcement

原文: On October 20th, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-6**, your instance will be updated to **1-18-0-apigee-6** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will not be updated:

- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.

[configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)
[Known Issue 445936920](https://docs.cloud.com/apigee/docs/release/known-issues)
[Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)
[Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance)
[Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)

説明：
2026年10月20日より、Apigeeインスタンスのメンテナンスアップデートが開始されたことがアナウンスされました。
もしお客様のApigeeインスタンスがメンテナンスウィンドウを設定しており、かつ現在のインスタンスバージョンが `1-18-0-apigee-6` 未満である場合、今後7〜21日以内に自動的に `1-18-0-apigee-6` へアップデートされます。アップグレードの具体的な予定日については、今後2営業日以内に通知が送付されます。

ただし、以下のいずれかの条件に該当するインスタンスは、この自動アップデートの対象外となります。
1.  既知の問題 (Known Issue 445936920) に記載されているようなDNS設定ミスがあるインスタンス。
2.  2025年10月16日付のApigeeリリースノートで削除されたApigee Java Libraryを使用しているインスタンス。

影響有無：
Apigee Xを利用しており、かつメンテナンスウィンドウが設定されているインスタンスで、現行バージョンが `1-18-0-apigee-6` 未満である場合、自動アップデートの対象となり影響があります。
このアップデートは、通常、セキュリティ修正や機能改善を含みますが、APIプロキシの挙動に予期せぬ影響を与えないか確認が必要です。特に、インスタンスがDNS設定ミスを抱えている場合や、非推奨のApigee Java Libraryを使用している場合はアップデートがスキップされるため、その状態が放置されることになります。

対処方法：
1.  **Apigee Xの利用有無の確認**: まず、本システムでApigee Xを利用しているか確認してください。
2.  **メンテナンスウィンドウ設定とバージョン確認**: Apigee Xを利用している場合、インスタンスがメンテナンスウィンドウを設定しているか、また現在のインスタンスバージョンが `1-18-0-apigee-6` 未満であるかを確認してください。
3.  **アップデート対象の場合**: 自動アップデートが実施されるため、アップデート期間中（通知される予定日以降）は、APIプロキシの正常性監視を強化し、必要に応じて回帰テストを実施してください。
4.  **アップデート対象外の場合**:
    *   もしインスタンスがDNS設定ミスを抱えている場合、Known Issue 445936920 を参照し、速やかに問題を修正してください。
    *   削除されたApigee Java Libraryを使用している場合は、代替手段への移行を検討・実施してください。
    これらの条件に該当する場合、自動アップデートが実行されないため、潜在的な脆弱性や機能改善が適用されない可能性があります。
5.  **通知の確認**: 今後2営業日以内に送付されるアップグレード予定日に関する通知を必ず確認し、計画に反映させてください。

用語説明：
*   **Apigee X**: Google Cloudが提供するエンタープライズ向けのAPI管理プラットフォームです。APIのライフサイクル全体（設計、開発、デプロイ、セキュリティ、モニタリング、分析など）を管理します。
*   **メンテナンスウィンドウ (Maintenance Window)**: Google Cloudサービスが計画的なメンテナンス作業を行うために予約する時間帯で、お客様のApigeeインスタンスのアップデートが実行されるタイミングを制御するために利用されます。
*   **インスタンスバージョン**: Apigeeランタイムのソフトウェアバージョンです。新しいバージョンは、機能改善、バグ修正、セキュリティパッチなどが含まれます。
*   **DNS misconfiguration**: ドメインネームシステムの設定誤りのことで、Apigee APIトラフィックのルーティングや名前解決に影響を与える可能性があります。
*   **Apigee Java Library**: Apigeeポリシーやカスタムロジックを実装する際に利用できるJavaベースのライブラリ群です。非推奨または削除されたライブラリは、今後のバージョンでサポートされなくなる可能性があります。

---

# Cloud SDK

## Breaking

原文: (本文なし)

説明：
Cloud SDKに関してBreaking Changeがアナウンスされていますが、具体的な変更内容や影響については記載されていません。通常、Breaking Changeは既存の互換性を損なう変更を指します。

影響有無：
Cloud SDKを使用している場合、このBreaking Changeは既存のスクリプト、CI/CDパイプライン、またはアプリケーション連携に影響を与える可能性があります。しかし、現時点では詳細が不明のため、具体的な影響範囲を特定することはできません。

対処方法：
現時点では具体的な変更内容が不明であるため、直ちに対応が必要なアクションはありません。今後のリリースノートやCloud SDKの公式ドキュメント、GitHubリポジトリなどを継続的に監視し、詳細情報が公開され次第、システムへの影響を評価し、必要に応じて対応計画を策定してください。

用語説明：
*   **Cloud SDK**: Google Cloudのサービスやリソースをコマンドライン（`gcloud`コマンド）やクライアントライブラリを介して操作するためのツールセットです。
*   **Breaking Change**: ソフトウェアの変更において、以前のバージョンとの互換性を失う変更のことです。これにより、既存のコードや設定が動作しなくなる可能性があります。

---

# Google Kubernetes Engine

## Fixed

原文: A security issue in GKE fleet management that could have allowed unauthorized configuration changes to clusters registered to a fleet has been resolved. The fixes are rolled out to all regions, and no action is required.

説明：
GKEフリート管理機能において、フリートに登録されたクラスタへの不正な設定変更を可能にする可能性があったセキュリティ脆弱性が修正されました。この修正はすべてのリージョンに展開済みであり、お客様側での追加対応は不要です。

影響有無：
GKEフリート管理を利用している場合でも、このセキュリティ脆弱性は既に修正され、影響は解消されています。ユーザーによる追加の操作は必要なく、セキュリティ体制が強化されたという点でポジティブな影響です。

対処方法：
不要。

用語説明：
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するマネージドなKubernetesサービスで、コンテナ化されたアプリケーションのデプロイ、スケーリング、管理を容易にします。
*   **GKEフリート管理 (GKE Fleet Management)**: 複数のGKEクラスタを論理的にグループ化し、一元的に管理するための機能です。これにより、ポリシーの適用、リソースの可視化、アプリケーションのデプロイなどを簡素化できます。
*   **セキュリティ脆弱性**: ソフトウェアやシステムの設計上、または実装上の欠陥で、攻撃者によって不正な操作や情報漏洩などの被害を引き起こす可能性のある弱点です。

## Fixed

原文: This is an update to the release note regarding the Cloud Storage FUSE CSI driver issue published on October 2, 2026. This issue has been resolved. You can upgrade your cluster control plane to the following versions to fix the issue for `ubuntu_containerd` and older `cos_containerd` node pools:

- 1.36.5-gke.1032000 or later
- 1.37.1-gke.1552000 or later
- Specific 1.36.4 mitigation patches: 1.36.4-gke.1247001, 1.36.4-gke.1247002, 1.36.4-gke.1391001, 1.36.4-gke.1391003, 1.36.4-gke.1495001, 1.36.4-gke.1495003, 1.36.4-gke.2046001, 1.36.4-gke.2202002

[October 2, 2026](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_02_2026)

説明：
2026年10月2日に公開されたCloud Storage FUSE CSIドライバに関する問題が解決されました。この問題を修正するには、GKEクラスタのコントロールプレーンを、指定された以下のバージョンにアップグレードする必要があります。これは、`ubuntu_containerd` および古い`cos_containerd` ノードプールを使用しているクラスタに適用されます。

*   1.36.5-gke.1032000 以降
*   1.37.1-gke.1552000 以降
*   特定の1.36.4緩和パッチバージョン（例: 1.36.4-gke.1247001 など）

影響有無：
GKEクラスタでCloud Storage FUSE CSIドライバを利用しており、かつノードプールが `ubuntu_containerd` または古い `cos_containerd` イメージを使用している場合、以前の問題の影響を受けていた可能性があります。この修正により、その問題が解消されるため、ポジティブな影響です。ただし、この修正を適用するには、クラスタのコントロールプレーンのバージョンアップグレードが必要となります。

対処方法：
1.  **利用状況の確認**: 構築済みのGKEクラスタでCloud Storage FUSE CSIドライバが利用されているか確認してください。
2.  **ノードプールイメージの確認**: Cloud Storage FUSE CSIドライバを利用している場合、ノードプールが `ubuntu_containerd` または古い `cos_containerd` イメージを使用しているか確認してください。
3.  **GKEバージョンの確認**: 該当するクラスタのコントロールプレーンのGKEバージョンが、上記で提示された修正バージョン（例：1.36.5-gke.1032000以降など）以上であるか確認してください。
4.  **アップグレードの検討**: もしバージョンが古い場合は、影響を解消するために、提示された修正バージョンへのコントロールプレーンのアップグレードを計画し、実行してください。アップグレード前には、開発環境やテスト環境での十分な検証を強く推奨します。

用語説明：
*   **Cloud Storage FUSE CSI driver**: Google Cloud Storage (GCS) バケットをKubernetes PodにファイルシステムとしてマウントするためのContainer Storage Interface (CSI) ドライバです。これにより、コンテナアプリケーションからGCSをローカルファイルシステムのように操作できます。
*   **CSI (Container Storage Interface)**: Kubernetesのようなコンテナオーケストレーションシステムが、様々な外部ストレージシステムと連携するための標準的なインターフェースです。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタを管理する中核コンポーネント群（APIサーバー、スケジューラ、コントローラマネージャなど）のことです。クラスタの状態を維持し、ワークロードを管理します。
*   **ノードプール (Node Pool)**: GKEクラスタ内で、同じ設定（マシンタイプ、OSイメージなど）を持つVMインスタンスのグループです。異なるタイプのワークロードや要件に応じて複数のノードプールを作成できます。
*   **`ubuntu_containerd` / `cos_containerd`**: GKEノードが使用するOSイメージとコンテナランタイムの組み合わせです。`ubuntu_containerd`はUbuntuをベースとし、`cos_containerd`はGoogleのContainer-Optimized OS (COS) をベースとし、いずれもContainerdをコンテナランタイムとして使用します。
# Title: October 19, 2026 
Link: https://docs.cloud.google.com/release-notes#October_19_2026<br>
Google Cloudインフラエンジニアとして、リリースノートに基づき構築済みのサービスへの影響を調査し、簡潔に回答いたします。

---

# Cloud Service Mesh

## Announcement
原文: **1.31.1-asm.19 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.31.1-asm.19 uses Envoy v1.39.3.
This release resolves the security vulnerabilities listed in Security Bulletin GCP-2026-069 (ISTIO-SECURITY-2026-007).

説明: インクラスター型のCloud Service Meshバージョン1.31.1-asm.19がリリースされました。このバージョンはEnvoy v1.39.3を使用しており、セキュリティ速報GCP-2026-069 (ISTIO-SECURITY-2026-007)で報告されているセキュリティ脆弱性を解決しています。

影響有無: 影響あり（ポジティブ）。現在、インクラスター型Cloud Service Meshを利用している場合、セキュリティ脆弱性の修正が含まれるため、システム全体のセキュリティ体制が向上します。

対処方法: 現在利用しているCloud Service Meshのバージョンを確認し、該当する場合は[Cloud Service Meshのアップグレード](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)手順に従い、本バージョンへのアップグレードを検討することを強く推奨します。

## Fixed
原文: Patch 1.31.1-asm.19 contains the fix for the following platform CVEs: GHSA-gcjh-h69q-9w9g | No | Yes | Yes | No | Medium (0.0)

説明: 上記の1.31.1-asm.19パッチリリースには、Control PlaneとDistrolessに影響する中程度の脆弱性GHSA-gcjh-h69q-9w9gの修正が含まれています。

影響有無: 影響あり（ポジティブ）。上記Announcementと関連しており、特定のセキュリティ脆弱性が解決されます。

対処方法: 上記Announcementと同様に、アップグレードを検討することを推奨します。

## Announcement
原文: **1.30.5-asm.11 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.30.5-asm.11 uses Envoy v1.38.7-dev.
This release resolves the security vulnerabilities listed in Security Bulletin GCP-2026-069 (ISTIO-SECURITY-2026-007).

説明: インクラスター型のCloud Service Meshバージョン1.30.5-asm.11がリリースされました。Envoy v1.38.7-devを使用し、GCP-2026-069 (ISTIO-SECURITY-2026-007)で報告されているセキュリティ脆弱性を解決しています。

影響有無: 影響あり（ポジティブ）。現在、インクラスター型Cloud Service Meshを利用している場合、セキュリティ脆弱性の修正が含まれるため、システム全体のセキュリティ体制が向上します。

対処方法: 現在利用しているCloud Service Meshのバージョンを確認し、該当する場合は[Cloud Service Meshのアップグレード](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)手順に従い、本バージョンへのアップグレードを検討することを強く推奨します。

## Announcement
原文: **1.29.8-asm.11 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.29.8-asm.11 uses Envoy v1.37.9-dev.
This release resolves the security vulnerabilities listed in Security Bulletin GCP-2026-069 (ISTIO-SECURITY-2026-007).

説明: インクラスター型のCloud Service Meshバージョン1.29.8-asm.11がリリースされました。Envoy v1.37.9-devを使用し、GCP-2026-069 (ISTIO-SECURITY-2026-007)で報告されているセキュリティ脆弱性を解決しています。

影響有無: 影響あり（ポジティブ）。現在、インクラスター型Cloud Service Meshを利用している場合、セキュリティ脆弱性の修正が含まれるため、システム全体のセキュリティ体制が向上します。

対処方法: 現在利用しているCloud Service Meshのバージョンを確認し、該当する場合は[Cloud Service Meshのアップグレード](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade)手順に従い、本バージョンへのアップグレードを検討することを強く推奨します。

## Announcement
原文: **1.28.10-asm.52 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.10-asm.52 uses Envoy v1.36.10-dev.
This release resolves the security vulnerability listed in Security Bulletin GCP-2026-069 (ISTIO-SECURITY-2026-007).

説明: インクラスター型のCloud Service Meshバージョン1.28.10-asm.52がリリースされました。Envoy v1.36.10-devを使用し、GCP-2026-069 (ISTIO-SECURITY-2026-007)で報告されているセキュリティ脆弱性を解決しています。

影響有無: 影響あり（ポジティブ）。現在、インクラスター型Cloud Service Meshを利用している場合、セキュリティ脆弱性の修正が含まれるため、システム全体のセキュリティ体制が向上します。

対処方法: 現在利用しているCloud Service Meshのバージョンを確認し、該当する場合は[Cloud Service Meshのアップグレード](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)手順に従い、本バージョンへのアップグレードを検討することを強く推奨します。

## Security
原文: The following images are now rolling out for managed Cloud Service Mesh: Sidecar version 1.21.6-asm.93 is rolling out to the rapid release channel. Sidecar version 1.20.8-asm.143 is rolling out to the regular release channel. Sidecar version 1.19.10-asm.132 is rolling out to the stable release channel.
Managed Cloud Service Mesh will start using proxy version `csm_mesh_proxy.20261014_RC00` for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.40. This change is rolling out to all release channels and contains the fix for the managed Cloud Service Mesh security vulnerabilities listed in GCP-2026-069 as well as fixes for the following platform CVEs: (詳細なCVEリスト)

説明: マネージドCloud Service Meshの各リリースチャネル（Rapid, Regular, Stable）で、それぞれサイドカーの新しいバージョンがロールアウトされます。また、Gateway APIを使用しているGKEクラスタでは、プロキシバージョン`csm_mesh_proxy.20261014_RC00` (Envoy v1.40相当)の使用が開始されます。これらの更新には、GCP-2026-069で報告されているものを含む多数のプラットフォームCVEに対するセキュリティ修正が含まれています。

影響有無: 影響あり（ポジティブ）。マネージドCloud Service Meshを利用している場合、これらのセキュリティ修正はGoogleによって自動的に適用されるため、セキュリティ体制が自動的に向上します。手動での操作は不要です。ただし、Gateway APIを使用している場合は、Envoyのバージョンアップに伴う挙動の変化や互換性について確認が推奨されます。

対処方法: マネージドサービスのため、特別な対処は不要です。セキュリティ修正は自動的に適用されます。Gateway APIをご利用の場合は、Envoy v1.40へのバージョンアップに伴い、既存の設定やアプリケーションの動作に影響がないか、事前にテスト環境で確認することを推奨します。

---

# Google Cloud Armor

## Security
原文: Security fixes and enhancements to Cloud Armor preconfigured WAF `v33-stable` rulesets. For more information, see Tuning Google Cloud Armor WAF rules.
The following rulesets have been updated: `sqli-v33-stable`, `xss-v33-stable`, `lfi-v33-stable`, `rfi-v33-stable`, `rce-v33-stable`, `methodenforcement-v33-stable`, `scannerdetection-v33-stable`, `protocolattack-v33-stable`, `php-v33-stable`, `sessionfixation-v33-stable`, `java-v33-stable`, `nodejs-v33-stable`.

説明: Google Cloud ArmorのプリセットWAFルールセット`v33-stable`に対して、セキュリティ修正と機能強化が実施されました。SQLインジェクション、クロスサイトスクリプティングなど、幅広い攻撃タイプに対応するルールセットが更新されています。

影響有無: 影響あり（ポジティブ）。Cloud ArmorのWAF機能を使用している場合、プリセットルールセットの更新が自動的に適用されるため、アプリケーションのセキュリティ保護が強化されます。特別な設定変更は不要です。

対処方法: 特に対処は不要です。これらの更新はCloud Armorサービス側で透過的に適用されます。既存のルールセットの動作に予期せぬ影響がないか、必要に応じて[Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning)を参照し、アプリケーションへの影響を監視することを検討してください。通常、後方互換性は維持されます。

## Security
原文: Security fixes and enhancements to Cloud Armor preconfigured WAF `stable` rulesets for v3.0. For more information, see Tuning Google Cloud Armor WAF rules.
The following rulesets have been updated: `sqli-stable`, `xss-stable`, `lfi-stable`, `rfi-stable`, `rce-stable`, `methodenforcement-stable`, `scannerdetection-stable`, `protocolattack-stable`, `php-stable`, `sessionfixation-stable`.

説明: Google Cloud ArmorのプリセットWAFルールセット`stable` (v3.0用)に対して、セキュリティ修正と機能強化が実施されました。こちらも同様に、様々な攻撃タイプに対応するルールセットが更新されています。

影響有無: 影響あり（ポジティブ）。Cloud ArmorのWAF機能を使用している場合、プリセットルールセットの更新が自動的に適用されるため、アプリケーションのセキュリティ保護が強化されます。特別な設定変更は不要です。

対処方法: 特に対処は不要です。これらの更新はCloud Armorサービス側で透過的に適用されます。既存のルールセットの動作に予期せぬ影響がないか、必要に応じて[Tuning Google Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning)を参照し、アプリケーションへの影響を監視することを検討してください。通常、後方互換性は維持されます。

---

### Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への全体的な影響

Google Cloud Composerは、AirflowをGoogle Cloud上で実行するためのマネージドサービスであり、基盤となるGoogle Kubernetes Engine (GKE) クラスタで動作します。

- **Cloud Service Mesh**: Cloud Composer自体はCloud Service Meshを直接管理したり、密接に統合したりするわけではありません。ただし、もしお客様の環境でCloud Composerが稼働するGKEクラスタに手動でCloud Service Meshを導入している場合、またはGoogle Cloudの基盤サービスの一部として透過的に利用されている場合は、上記セキュリティ修正の恩恵を受けることができます。Cloud Composer 2.7.1の動作に直接的な影響は通常ありませんが、基盤のセキュリティ強化に貢献します。

- **Google Cloud Armor**: Cloud ComposerのAirflow UIやDAGsのウェブサーバーエンドポイントへのアクセスを保護するためにGoogle Cloud Armorを利用している場合、今回のWAFルールセットの更新により、自動的にセキュリティ保護が強化されます。この構成は一般的な利用パターンであり、この場合、セキュリティ面でポジティブな影響があります。

結論として、Cloud Composer 2.7.1, Airflow 2.7.3を利用されている環境において、これらのリリースノートによる**直接的な機能変更や非互換性の影響は確認されません**。しかし、基盤サービスであるCloud Service Meshや、フロントエンド保護として利用される可能性のあるCloud Armorのセキュリティ強化は、間接的にシステム全体のセキュリティ向上に寄与するため、**ポジティブな影響**があると言えます。

---

### 用語説明

*   **Cloud Service Mesh (CSM)**: Google Cloudが提供する、Istioをベースとしたマネージドサービスメッシュです。Kubernetesクラスタ内のサービス間通信の管理、可視化、セキュリティ強化、信頼性向上などを実現します。
*   **In-cluster Cloud Service Mesh**: ユーザーがGoogle Kubernetes Engine (GKE) クラスタ内にIstioコントロールプレーンを自身でデプロイし、その管理も行う形態です。
*   **Managed Cloud Service Mesh**: GoogleがIstioコントロールプレーンの運用と管理を代行する形態です。ユーザーはデータプレーン（サイドカープロキシ）のみを管理します。
*   **Envoy**: Cloud Service Mesh (Istio) のデータプレーンとして使用される、高性能なオープンソースのエッジおよびサービスプロキシです。サービス間のトラフィックをルーティング、制御、監視します。
*   **Security Bulletin (GCP-2026-069, ISTIO-SECURITY-2026-007)**: Google CloudおよびIstioプロジェクトから発行される、特定のセキュリティ脆弱性に関する公式のアナウンスや情報提供文書です。
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアのセキュリティ脆弱性を識別するための国際的な標準識別子です。
*   **WAF (Web Application Firewall)**: ウェブアプリケーションに対する一般的な攻撃（例: SQLインジェクション、クロスサイトスクリプティングなど）から保護するために設計されたファイアウォールです。
*   **Preconfigured WAF rulesets**: Cloud Armorが提供する、一般的なウェブ攻撃パターンを検出・防御するための、あらかじめ定義されたルールセットです。ユーザーはこれらのルールセットを有効にするだけで、基本的な保護を迅速に実装できます。
*   **MDPC (Managed Data Plane Control)**: マネージドCloud Service Meshにおける、データプレーン（Envoyプロキシ）の動作を制御するメカニズムを指します。
*   **CNI (Container Network Interface)**: Linuxコンテナのネットワーク構成に関する仕様と、それに基づくプラグインです。Kubernetesクラスタ内のポッド間通信を実現します。
*   **Gateway API**: Kubernetesにおける次世代のネットワークAPIで、Ingressの進化形として、より柔軟で表現豊かなトラフィックルーティングとネットワーク設定を可能にします。Cloud Service Meshなどのサービスメッシュ環境でも利用が推進されています。