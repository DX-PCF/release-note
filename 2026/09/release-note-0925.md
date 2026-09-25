
# Title: September 23, 2026 
Link: https://docs.cloud.google.com/release-notes#September_23_2026<br>
Google Cloud リリースノートについて、構築済みのGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響を調査し、以下の通り回答します。

---

# Cloud Service Mesh

## Announcement

原文: **1.30.4-asm.14 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.30.4-asm.14 uses Envoy v1.38.5-dev.

説明:
Cloud Service Mesh (Anthos Service Mesh) のバージョン `1.30.4-asm.14` が新たに利用可能になりました。このバージョンはEnvoy `v1.38.5-dev` を使用しており、アップグレードに関する詳細ドキュメントへのリンクも提供されています。

影響有無: なし。
理由: Google Cloud Composer は Anthos Service Mesh をそのコンポーネントとして直接利用しておらず、また、構築済みの Composer 環境に明示的に Service Mesh をデプロイしていないため、本アナウンスによる直接的な影響はありません。

対処方法: なし。

## Fixed

原文: Patch 1.30.4-asm.14 contains the fix for the following platform CVEs:
(CVEテーブル省略)

説明:
Cloud Service Mesh のバージョン `1.30.4-asm.14` には、多数のプラットフォーム共通脆弱性識別子 (CVE) に対するセキュリティ修正が含まれています。これらの修正には、Severityが「High」または「Medium」の脆弱性も含まれます。

影響有無: なし。
理由: 上記のAnnouncementと同様に、Google Cloud Composer は Anthos Service Mesh を直接利用していないため、本セキュリティ修正による直接的な影響はありません。

対処方法: なし。

---

## Announcement

原文: **1.29.7-asm.18 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.29.7-asm.18 uses Envoy v1.37.6.

説明:
Cloud Service Mesh のバージョン `1.29.7-asm.18` が新たに利用可能になりました。このバージョンはEnvoy `v1.37.6` を使用しており、アップグレードに関する詳細ドキュメントへのリンクも提供されています。

影響有無: なし。
理由: Google Cloud Composer は Anthos Service Mesh をそのコンポーネントとして直接利用しておらず、また、構築済みの Composer 環境に明示的に Service Mesh をデプロイしていないため、本アナウンスによる直接的な影響はありません。

対処方法: なし。

## Fixed

原文: Patch 1.29.7-asm.18 contains the fix for the following platform CVEs:
(CVEテーブル省略)

説明:
Cloud Service Mesh のバージョン `1.29.7-asm.18` には、多数のプラットフォーム CVE に対するセキュリティ修正が含まれています。これらの修正には、Severityが「High」または「Medium」の脆弱性も含まれます。

影響有無: なし。
理由: 上記のAnnouncementと同様に、Google Cloud Composer は Anthos Service Mesh を直接利用していないため、本セキュリティ修正による直接的な影響はありません。

対処方法: なし。

---

## Announcement

原文: **1.28.10-asm.40 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.10-asm.40 uses Envoy v1.36.10-dev.

説明:
Cloud Service Mesh のバージョン `1.28.10-asm.40` が新たに利用可能になりました。このバージョンはEnvoy `v1.36.10-dev` を使用しており、アップグレードに関する詳細ドキュメントへのリンクも提供されています。

影響有無: なし。
理由: Google Cloud Composer は Anthos Service Mesh をそのコンポーネントとして直接利用しておらず、また、構築済みの Composer 環境に明示的に Service Mesh をデプロイしていないため、本アナウンスによる直接的な影響はありません。

対処方法: なし。

## Fixed

原文: Patch 1.28.10-asm.40 contains the fix for the following platform CVEs:
(CVEテーブル省略)

説明:
Cloud Service Mesh のバージョン `1.28.10-asm.40` には、多数のプラットフォーム CVE に対するセキュリティ修正が含まれています。これらの修正には、Severityが「High」または「Medium」の脆弱性も含まれます。

影響有無: なし。
理由: 上記のAnnouncementと同様に、Google Cloud Composer は Anthos Service Mesh を直接利用していないため、本セキュリティ修正による直接的な影響はありません。

対処方法: なし。

---

# Google Kubernetes Engine

## Change

原文: GKE cluster versions have been updated.
**New versions available for upgrades and new clusters.**
The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.

説明:
Google Kubernetes Engine (GKE) のクラスターバージョンが更新され、新しいバージョンが新規クラスター作成および既存クラスターのコントロールプレーン・ノードアップグレード用に利用可能になりました。GKEのバージョン管理とアップグレードに関する詳細ドキュメントが参照されています。

影響有無: なし。
理由: Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) は、[公式ドキュメント](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions#google_kubernetes_engine_versions)によると、GKE 1.25、1.26、1.27、1.28、1.29 をサポートしています。今回のリリースノートに記載されているGKEバージョンは 1.31、1.32、1.33、1.34、1.35、1.36、1.38 (preview) であり、Composer 2.7.1 が現在サポートしているGKEバージョン範囲外です。そのため、既存のComposer 2.7.1 環境が自動的にこれらの新しいGKEバージョンにアップグレードされることはありません。

対処方法: なし。
補足: 将来的にComposerのバージョンアップを検討する際には、新しいGKEバージョンへの対応状況を確認する必要があります。

## No channel (deprecated)

原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.8-gke.1225000 is now the default version for cluster creation.
- The following versions are now available:
    - 1.34.11-gke.1209000
    - 1.35.8-gke.1626000
    - 1.36.4-gke.1495000
- The following node versions are now available:
    - 1.31.14-gke.2759000
    - 1.32.13-gke.2504000
    - 1.33.13-gke.1721000
    - 1.34.11-gke.1209000
    - 1.35.8-gke.1626000
    - 1.36.4-gke.1495000
- The following versions are no longer available:
    - 1.34.10-gke.1236000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.35.7-gke.1222000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
    - 1.36.4-gke.1082000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
        - 1.33 to 1.34.11-gke.1044000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
        - 1.34 to 1.34.11-gke.1044000

説明:
GKEの「No channel」 (特定のリリースチャネルに属さない、あるいは明示されていないバージョン) におけるクラスターバージョンの更新情報です。新規クラスター作成のデフォルトバージョンが `1.35.8-gke.1225000` になりました。利用可能な新しいGKEバージョンと、ノードバージョンがリストアップされています。また、いくつかのGKEバージョン (`1.34.10-gke.1236000`, `1.35.7-gke.1222000`, `1.36.4-gke.1082000`) が非推奨となり、90日以内またはサポート終了日までに削除されることが示されています。さらに、自動アップグレードターゲットが変更され、メンテナンス除外や非推奨APIがない場合に、指定されたマイナーバージョンやパッチバージョンへのアップグレードが推奨されます。

影響有無: なし。
理由: Composer 2.7.1 がサポートするGKEバージョンは 1.25〜1.29 です。本セクションで言及されているGKEバージョン (1.3x系) はComposer 2.7.1 のサポート対象外であるため、既存のComposer環境に直接的な影響はありません。また、非推奨となったGKEバージョンも、Composer 2.7.1では使用されていないため、対応の必要はありません。

対処方法: なし。

## Security

原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release.
To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. The following table includes links to the release notes for each updated Container-Optimized OS image:
(COSバージョンテーブル省略)

説明:
このGKEリリースには、セキュリティ修正が適用されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらのCOSイメージは、前回のGKEリリース以降にリリースされたすべてのCOSバージョンのセキュリティ修正を累積的に含んでいます。

影響有無: なし (セキュリティ向上という点で間接的なメリットあり)。
理由: Composer 2.7.1がサポートするGKEバージョンとは異なる新しいGKEバージョンにCOSイメージの更新が適用されているため、Composer 2.7.1環境のGKEノードOSが直ちに更新されるわけではありません。しかし、GKEノードの基盤となるOSのセキュリティが強化されることは、GKEサービス全体のセキュリティ体制向上に寄与します。Composer環境はマネージドGKEクラスタ上で動作するため、Google Cloud側でのGKE基盤のセキュリティ強化は、間接的にComposer環境のセキュリティ向上につながります。

対処方法: なし。

## Change (Stable channel)

原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.34.10-gke.1328000 is now available in the Stable channel.
- Version 1.34.10-gke.1236000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.

説明:
GKEのStableチャネルにおけるクラスターバージョンが更新されました。バージョン `1.34.10-gke.1328000` が利用可能になり、`1.34.10-gke.1236000` が非推奨となり90日以内またはサポート終了までに削除される予定です。

影響有無: なし。
理由: Composer 2.7.1 がサポートするGKEバージョンは 1.25〜1.29 であり、Stableチャネルで提供される 1.34.x 系GKEバージョンはサポート対象外です。

対処方法: なし。

## Change (Regular channel)

原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.35.8-gke.1225000 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
    - 1.34.11-gke.1056000
    - 1.35.8-gke.1380000
    - 1.36.4-gke.1247000
- The following versions are no longer available in the Regular channel:
    - 1.34.10-gke.1328000
    - 1.35.8-gke.1036000
    - 1.36.4-gke.1082000 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new
# Title: September 22, 2026 
Link: https://docs.cloud.google.com/release-notes#September_22_2026<br>
ご担当者様

Google Cloudのリリースノートに関する調査結果をご報告いたします。

---

# Cloud SDK
## Breaking
原文: (原文が提供されていません)
説明：Cloud SDKのBreaking Changeに関するアナウンスですが、詳細な変更内容が提供されていないため、具体的な説明はできません。
影響有無：変更内容が不明なため、影響の有無を判断できません。
対処方法：Google Cloud SDKの最新リリースノートや公式ドキュメントで、このBreaking Changeに関する詳細情報が公開されていないか継続的に確認してください。
用語説明：
*   **Breaking Change**: 既存のコードや設定に互換性のない変更をもたらす変更。通常、アップグレード時に修正作業が必要となります。

---

# Compute Engine
## Deprecated
原文: As of September 15, 2026, NVIDIA P100 (`nvidia-tesla-p100` and `nvidia-tesla-p100-vws`) GPUs have reached end of support (EOS) and are shut down. You can no longer create, launch, or access Compute Engine instances or other Google Cloud resources that use NVIDIA P100 GPUs. For information about migrating your workloads to supported GPU alternatives such as the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series, see NVIDIA P100 end of support.
[NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos)
説明：NVIDIA P100 GPU (nvidia-tesla-p100 および nvidia-tesla-p100-vws) は、2026年9月15日にサポート終了 (End of Support: EOS) となり、既にシャットダウンされています。この日付以降、NVIDIA P100 GPUを使用するCompute Engineインスタンスやその他のGoogle Cloudリソースの新規作成、起動、既存リソースへのアクセスは不可能となっています。代替として、G2 (NVIDIA L4) やG4 (NVIDIA RTX PRO 6000) マシンシリーズへのワークロードの移行が推奨されています。
影響有無：
*   **影響あり**: もし現在、貴社環境でNVIDIA P100 GPUを利用しているCompute Engineインスタンスや関連リソースが存在する場合、それらは既に利用できなくなっているため、業務に重大な影響が発生しています。
*   **影響なし**: NVIDIA P100 GPUを利用していない場合は、直接的な影響はありません。
対処方法：
*   現在NVIDIA P100 GPUを使用している場合は、直ちにワークロードをG2 (NVIDIA L4) またはG4 (NVIDIA RTX PRO 6000) など、サポートされているGPUモデルへ移行してください。
*   移行の詳細については、提供されたドキュメント「[NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos)」を参照してください。
用語説明：
*   **GPU (Graphics Processing Unit)**: 画像処理や並列計算に特化したプロセッサ。AI/ML、HPC (High-Performance Computing) などのワークロードで利用されます。
*   **End of Support (EOS)**: 製品やサービスに対するベンダーからの公式サポートが終了すること。通常、バグ修正、セキュリティパッチ、技術サポートなどが提供されなくなります。
*   **Compute Engine**: Google Cloudが提供するIaaS (Infrastructure as a Service) で、仮想マシン (VM) を提供するサービスです。
*   **G2 (NVIDIA L4) / G4 (NVIDIA RTX PRO 6000)**: Compute Engineで利用可能な、より新しい世代の高性能GPUタイプです。

## Deprecated
原文: NVIDIA T4 (`nvidia-tesla-t4` and `nvidia-tesla-t4-vws`) and NVIDIA P4 (`nvidia-tesla-p4` and `nvidia-tesla-p4-vws`) GPUs are deprecated and will reach end of support (EOS) on August 1, 2027. After August 1, 2027, you won't be able to create, launch, or access Compute Engine instances or other Google Cloud resources that run NVIDIA T4 or P4 GPUs. In addition, you can no longer purchase or renew 3-year committed use discounts (CUDs) for NVIDIA T4 or P4 GPUs. To transition your workloads to supported GPU models such as the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series before the EOS date, see NVIDIA T4 end of support and NVIDIA P4 end of support.
[NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos)
[NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos)
説明：NVIDIA T4 GPU (nvidia-tesla-t4 および nvidia-tesla-t4-vws) および NVIDIA P4 GPU (nvidia-tesla-p4 および nvidia-tesla-p4-vws) が非推奨となり、2027年8月1日にサポート終了 (EOS) となります。この日付以降、これらのGPUを使用するCompute Engineインスタンスやその他のGoogle Cloudリソースの新規作成、起動、既存リソースへのアクセスができなくなります。また、NVIDIA T4またはP4 GPUに対する3年間のコミットメント利用割引 (CUD) の新規購入または更新は既にできなくなっています。EOS日までに、G2 (NVIDIA L4) やG4 (NVIDIA RTX PRO 6000) など、サポートされているGPUモデルへのワークロードの移行が推奨されています。
影響有無：
*   **影響あり**: もし現在、貴社環境でNVIDIA T4またはP4 GPUを利用しているCompute Engineインスタンスや関連リソースが存在する場合、2027年8月1日までに移行計画を立て、実行する必要があります。また、GPU関連のコミットメント利用割引 (CUD) を利用している場合、更新ができないためコストに影響が出る可能性があります。
*   **影響なし**: NVIDIA T4またはP4 GPUを利用していない場合は、直接的な影響はありません。
対処方法：
*   現在NVIDIA T4またはP4 GPUを使用している場合は、2027年8月1日のEOS日までに、ワークロードをG2 (NVIDIA L4) またはG4 (NVIDIA RTX PRO 6000) など、サポートされているGPUモデルへ移行する計画を策定し、実行してください。
*   コミットメント利用割引 (CUD) の契約状況を確認し、必要に応じて新しいGPUモデルのCUDへの切り替えや、料金体系の見直しを検討してください。
*   移行の詳細については、提供されたドキュメント「[NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos)」および「[NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos)」を参照してください。
用語説明：
*   **Deprecated (非推奨)**: 将来的にサポートが終了する予定であるか、より新しい代替手段が存在するため、新規利用を推奨しない状態です。既存の利用者は移行を検討する必要があります。
*   **Committed Use Discounts (CUDs)**: 特定のGoogle Cloudリソース（この場合はGPU）を1年間または3年間継続して使用することをコミットすることで、オンデマンド料金よりも大幅な割引を受けられる料金プランです。
*   **G2 (NVIDIA L4) / G4 (NVIDIA RTX PRO 6000)**: Compute Engineで利用可能な、より新しい世代の高性能GPUタイプです。
# Title: September 21, 2026 
Link: https://docs.cloud.google.com/release-notes#September_21_2026<br>
はい、承知いたしました。Google CloudのApigee Xに関するリリースノートについて、インフラエンジニアの視点から分析し、ご指定の書式で回答いたします。

---

# Apigee X

## Announcement

原文: On September 21st, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
[configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)
If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-4**, your instance will be updated to **1-18-0-apigee-4** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.
Note: Instances that meet either of the following two criteria will not be updated:
- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.
[Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues)
[Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)
For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.
[Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance)
[Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)

説明：
2026年9月21日より、メンテナンスウィンドウを設定しているApigeeインスタンスに対するメンテナンスアップデートが開始されました。
インスタンスのバージョンが `1-18-0-apigee-4` 未満の場合、今後7〜21日以内にこのバージョンに更新されます。アップグレード予定日を記載した通知が、今後2営業日以内に送信される予定です。
ただし、以下のいずれかの条件に該当するインスタンスは更新されません。
*   既知の問題 445936920 に記載されているDNS設定ミスがあるインスタンス。
*   2025年10月16日付のApigeeリリースノートに記載されている、削除されたApigee Java Libraryを使用しているインスタンス。

影響有無：
**影響あり（要確認）**
*   **機能変更**: 既存インスタンスが指定バージョンに自動的に更新されるため、バージョンアップに伴う変更（新機能、バグ修正、潜在的な非互換性）が発生します。
*   **計画性**: メンテナンスウィンドウを設定している場合でも、Google Cloudによって計画された更新が実施されます。予期せぬ機能動作の変化や、旧バージョンへの依存性がある場合に影響を受ける可能性があります。

対処方法：
1.  **インスタンスバージョンの確認**: 現在ご利用中のApigeeインスタンスのバージョンを確認してください。
2.  **メンテナンスウィンドウ設定の確認**: 現在メンテナンスウィンドウを設定しているか確認してください。
3.  **アップグレード通知の確認**: バージョンが `1-18-0-apigee-4` 未満で、かつメンテナンスウィンドウを設定している場合、Google Cloudから送信されるアップグレード予定日の通知を確認し、計画を立てる準備をしてください。
4.  **互換性検証**: アップグレード前に、既存のAPIプロキシやカスタムスクリプト（特にJava Calloutなど）が `1-18-0-apigee-4` で正常に動作するかどうか、可能な限りテスト環境で検証することを強く推奨します。特に、2025年10月16日のリリースノートで削除されたJava Libraryを使用していないか確認してください。
5.  **更新対象外条件の確認と対応**: もしご利用中のインスタンスがDNS設定ミスや削除されたJava Libraryの使用により更新対象外となっている場合、これらを修正することを検討してください。これにより、将来的なセキュリティ修正や機能改善が適用されるようになります。

用語説明：
*   **Apigee**: Google Cloudが提供するAPI管理プラットフォームです。APIの設計、セキュアな公開、分析、モニタリングなどを一元的に行います。
*   **メンテナンスウィンドウ**: Google Cloudサービスがメンテナンスのために一時的にサービスが停止または影響を受ける期間です。ユーザーは自身のワークロードへの影響を最小限にするため、特定の時間帯を指定できます。
*   **Apigee Java Library**: ApigeeのカスタムポリシーなどでJavaコードを記述する際に使用されるライブラリ群です。
*   **DNS misconfiguration (DNS設定ミス)**: ドメインネームシステム（DNS）の設定に誤りがある状態を指します。これにより、Apigeeインスタンスへのトラフィックルーティングなどに問題が生じる可能性があります。

---

## Announcement

原文: On September 21st, 2026, we released an updated version of Apigee (1-18-0-apigee-5).
> **Note:** Rollouts of this release began today and can take four or more business days to be completed across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.

説明：
2026年9月21日に、Apigeeの新しいバージョン `1-18-0-apigee-5` がリリースされました。
このリリースのロールアウト（展開）は、全Google Cloudゾーンで完了するまでに4営業日以上かかる場合があります。ロールアウトが完了するまで、お使いのインスタンスで新機能や修正が利用できない可能性があります。

影響有無：
**影響なし（情報提供）**
*   **機能追加/変更**: 新しいバージョンがリリースされ、これにはバグ修正やセキュリティパッチが含まれます（詳細は後続の「Security」および「Fixed」セクションに記載）。
*   **展開期間**: ロールアウトが段階的に行われるため、すぐに全機能が利用可能になるわけではありません。

対処方法：
特段の対処は不要ですが、ご自身のApigeeインスタンスがこのバージョンに更新されたか、またそれに伴う改善点（後述のセキュリティ修正やバグ修正）が適用されたことを認識しておくことが推奨されます。ロールアウトが完了するまでは、最新の機能や修正が利用できない可能性があることを考慮に入れてください。

用語説明：
*   **ロールアウト (Rollout)**: ソフトウェアやシステムの新しいバージョンを、全てのリソースに対して一度に適用するのではなく、段階的かつ計画的に展開していくプロセスです。これにより、リスクを最小限に抑え、問題が発生した場合に速やかに対応できます。

---

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **560130499** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy. |
| **547681234** | **Security fix for Apigee.** Patched CVE-2026-69247 by upgrading a third-party library used by the Apigee model-security engine. |
| **556568593** | **Security fix for Apigee.** Patched CVE-2026-84304 by upgrading gRPC. |
| **N/A** | **Security fix for Apigee infrastructure.** |
[CVE-2026-69247](https://nvd.nist.gov/vuln/detail/CVE-2026-69247)
[CVE-2026-84304](https://nvd.nist.gov/vuln/detail/CVE-2026-84304)

説明：
以下のセキュリティ修正がApigeeに適用されました。
*   **Java Callout policy のセキュリティ修正**: Java Calloutポリシーにおけるセキュリティ上の脆弱性が修正されました。
*   **CVE-2026-69247 へのパッチ**: Apigeeのモデルセキュリティエンジンで使用されるサードパーティライブラリをアップグレードすることで、共通脆弱性識別子（CVE）CVE-2026-69247に関連する脆弱性が修正されました。
*   **CVE-2026-84304 へのパッチ**: gRPCをアップグレードすることで、CVE-2026-84304に関連する脆弱性が修正されました。
*   **Apigee インフラストラクチャのセキュリティ修正**: Apigeeの基盤インフラストラクチャにおけるセキュリティ修正が行われました。

影響有無：
**影響あり（ポジティブな影響）**
*   **セキュリティ体制の向上**: 複数のセキュリティ脆弱性が修正されたため、Apigee環境の全体的なセキュリティ体制が強化されます。特にJava Calloutポリシーを使用している環境では、そのセキュリティが向上します。
*   **脆弱性対応**: 既知のCVEに対応したことで、潜在的な攻撃リスクが低減します。

対処方法：
これらのセキュリティ修正は、Apigeeのバージョンアップデートの一環として自動的に適用されます。ユーザー側で特別な対処は不要ですが、よりセキュアな環境でApigeeを利用できることを認識しておくことが重要です。もしJava Calloutポリシーを広範に利用している場合は、修正によって予期せぬ動作変更がないか、軽いリグレッションテストを実施することを検討しても良いでしょう。

用語説明：
*   **Java Callout policy**: ApigeeのAPIプロキシフロー内で、カスタムのビジネスロジックをJavaで記述し実行するためのポリシーです。
*   **CVE (Common Vulnerabilities and Exposures)**: 公に知られているサイバーセキュリティの脆弱性や露出に一意の識別番号を付与し、リスト化しているデータベースです。
*   **gRPC**: Googleが開発した、高性能なオープンソースのリモートプロシージャコール（RPC）フレームワークです。

---

## Fixed

原文:
| Bug ID | Description |
| --- | --- |
| **559009293** | Fixed elevated OAuth and VerifyAPIKey latency and Cassandra read load for AppGroup apps by caching the AppGroup entity in the Message Processor runtime, matching Developer-app behavior. |
| **558888960** | Fixed distributed tracing so that the target URL is included as a span attribute in all scenarios. |
| **556750755** | Fixed EventFlow (Server-Sent Events) dropping or truncating events that follow a large (greater than 16 KB) event under load on the http-adaptor data path. |
| **553931019** | The MCP tools/list method now aggregates tools across all approved API products. |
| **531783017** | Implemented the `<Enforce>true</Enforce>` element of SSLInfo for a Syslog endpoint, so that the syslog target's TLS server identity is verified. |
| **554114419** | Policies can now change request pseudo-headers (for example, :path and :authority) when HTTP/2 is in use. |
| **548763108** | Blocked outbound HTTP from the Message Processor to Kubernetes-internal targets. |
| **513032450** | Restored a 15-second TCP keep-alive on the Apigee Connect control-plane connection so that a silently dropped connection recovers in seconds rather than approximately two hours. |
| **N/A** | Updates to infrastructure and libraries. |

説明：
以下の複数のバグ修正および改善が行われました。
*   **OAuth / VerifyAPIKey レイテンシ改善**: AppGroupアプリケーションにおけるOAuthおよびVerifyAPIKeyのレイテンシ上昇とCassandraのリード負荷増大の問題が修正されました。これは、Message ProcessorランタイムでAppGroupエンティティをキャッシュすることで、Developer-appの動作と同様に改善されました。
*   **分散トレーシングの改善**: 全てのシナリオにおいて、分散トレーシングのスパン属性にターゲットURLが含まれるようになりました。
*   **EventFlow (Server-Sent Events) の修正**: HTTPアダプターのデータパスにおいて、大きなイベント（16KB以上）の後に続くイベントが負荷時に失われたり途中で切れたりするEventFlow (Server-Sent Events) の問題が修正されました。
*   **MCP `tools/list` メソッドの改善**: MCPの `tools/list` メソッドが、承認済みの全てのAPI製品を横断してツールを集約するようになりました。
*   **SyslogエンドポイントのTLS検証強制**: Syslogエンドポイントに対してSSLInfoの `<Enforce>true</Enforce>` 要素が実装され、syslogターゲットのTLSサーバーのIDが検証されるようになりました。
*   **HTTP/2 におけるポリシーによる疑似ヘッダー変更**: HTTP/2が使用されている場合、ポリシーがリクエストの疑似ヘッダー（例: `:path`, `:authority`）を変更できるようになりました。
*   **Message Processor から Kubernetes 内部ターゲットへの HTTP アウトバウンドブロック**: Message ProcessorからKubernetes内部ターゲットへのHTTPアウトバウンド通信がブロックされました。
*   **Apigee Connect TCP keep-alive の復元**: Apigee Connectのコントロールプレーン接続において15秒のTCP keep-aliveが復元されました。これにより、サイレントに切断された接続が約2時間ではなく数秒で回復するようになりました。
*   **インフラストラクチャおよびライブラリの更新**: 基盤インフラストラクチャと使用ライブラリの更新が行われました。

影響有無：
**影響あり（ポジティブな影響が主、一部要確認）**
*   **パフォーマンス向上**: OAuth/VerifyAPIKeyのレイテンシ改善、EventFlowのイベント損失解消、Apigee Connectの接続回復性向上などにより、全体的なパフォーマンスと信頼性が向上します。
*   **機能の正確性向上**: 分散トレーシングのデータ充実化、MCPツールリストの改善、SyslogのTLS検証強制などにより、モニタリングや管理機能の正確性が向上します。
*   **新機能**: HTTP/2におけるポリシーによる疑似ヘッダー変更は、特定のHTTP/2ベースのルーティングや変換ロジックを実装する上で新たな柔軟性を提供します。
*   **セキュリティ/ネットワーク制限**: 「Message Processor から Kubernetes 内部ターゲットへの HTTP アウトバウンドブロック」は、セキュリティ強化のための変更です。もし既存のワークロードで、意図的にMessage ProcessorからKubernetes内部のサービスへHTTP通信を行っていた場合、この変更により通信がブロックされるため、**影響があります（Breaking Changeの可能性）**。通常はこのような直接通信は不要ですが、特殊な構成を取っている場合は注意が必要です。

対処方法：
*   これらの修正はApigeeのバージョンアップデートに伴い自動的に適用されるため、ユーザー側での直接的な作業は不要です。
*   ただし、「Message Processor から Kubernetes 内部ターゲットへの HTTP アウトバウンドブロック」に関して、もし既存のシステムでそのような特殊な通信経路を利用していた場合は、通信がブロックされるため、この変更による影響がないか確認し、必要に応じて代替の通信方法（例えば、Service Calloutポリシー経由での適切なターゲットサービスへのルーティングなど）を検討してください。
*   修正された問題（例：OAuthレイテンシ、EventFlowのイベント損失）に過去に直面していた場合、修正が適用された後に問題が改善されているか確認することを推奨します。
*   HTTP/2におけるポリシーによる疑似ヘッダー変更の新しい機能に興味がある場合は、その利用を検討してください。

用語説明：
*   **OAuth**: Open Authorizationの略で、ユーザーの認証情報を共有することなく、特定のリソースへのアクセスを認可するための標準的なプロトコルです。
*   **VerifyAPIKey policy**: Apigeeで受信したリクエストのAPIキーが有効であるか、そしてそのAPIキーに関連付けられたアプリケーションがAPIにアクセスする権限を持っているかを確認するためのポリシーです。
*   **Message Processor**: Apigeeランタイムの主要コンポーネントの一つで、APIプロキシを介してAPIトラフィックを処理し、ポリシーを実行する役割を担います。
*   **AppGroup**: Apigeeにおいて、複数の開発者アプリケーションを論理的にグループ化する機能です。
*   **Cassandra**: Apache Cassandraのことで、スケーラブルで高性能な分散型NoSQLデータベースシステムです。Apigee内部のデータストアとして利用されます。
*   **分散トレーシング (Distributed Tracing)**: マイクロサービスアーキテクチャのような分散システムにおいて、単一のリクエストが複数のサービスを横断する際の処理経路と、各サービスでの処理時間などを可視化する技術です。
*   **スパン属性 (Span Attribute)**: 分散トレーシングにおいて、個々の操作単位である「スパン」に追加されるメタデータです。これにより、その操作に関する詳細情報（例：URL、エラーコードなど）を記録できます。
*   **EventFlow (Server-Sent Events, SSE)**: HTTP接続を介して、サーバーからクライアントへ一方的にリアルタイムのイベント（データ更新など）をプッシュするための技術です。
*   **MCP (Management Plane)**: Apigeeの管理プレーンを指します。APIのデプロイ、設定、ユーザー管理、分析データの収集など、APIプラットフォーム全体の管理機能を提供します。
*   **Syslog**: ネットワーク上のデバイスからシステムログメッセージを収集・転送するための標準プロトコルです。
*   **TLS (Transport Layer Security)**: インターネット上でデータを安全に通信するための暗号化プロトコルで、SSLの後継にあたります。
*   **疑似ヘッダー (Pseudo-headers)**: HTTP/2プロトコルで導入された特殊なヘッダーフィールドです。これらは従来のHTTP/1.xのステータスラインやリクエストラインの情報をヘッダー形式で表現します（例: `:method`, `:path`, `:authority`）。
*   **Kubernetes-internal targets**: Kubernetesクラスタ内部で動作しているサービスやポッドのアドレスを指します。通常、クラスタ内部の通信に利用されます。
*   **Apigee Connect**: ハイブリッド環境のApigeeにおいて、Google Cloud上の管理プレーンと、オンプレミスや他のクラウド環境にデプロイされたラン