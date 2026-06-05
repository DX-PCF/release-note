
# Title: June 03, 2026 
Link: https://docs.cloud.google.com/release-notes#June_03_2026<br>
## Cloud Service Mesh

### Announcement
**原文: 1.28.7-asm.3 is now available for in-cluster Cloud Service Mesh. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.7-asm.3 uses Envoy v1.36.7-dev.**

**説明:**
Cloud Service Mesh の in-cluster デプロイメント向けに、バージョン 1.28.7-asm.3 がリリースされました。このバージョンでは、Envoy プロキシが v1.36.7-dev を使用しています。既存の Cloud Service Mesh 環境をアップグレードする際には、提供されているアップグレードガイドを参照してください。

**影響有無:**
影響なし。
当社の環境では、Google Cloud Composer 2（Composer version 2.7.1、Airflow version 2.7.3）を利用しており、これはGoogleによってマネージドされているサービスです。Cloud Service Mesh の in-cluster デプロイメントは、ユーザー自身が GKE クラスタなどに手動で導入・管理する形態を指します。Composer の基盤となる GKE クラスタは Google が管理しており、これらのバージョンアップやセキュリティパッチの適用は Google 側で実施されるため、お客様側で直接的な対応は不要です。

**対処方法:**
なし。
Google Cloud Composer のようなマネージドサービスを利用している場合、これらのセキュリティアップデートは Google 側で透過的に適用されます。ユーザー側で特別な操作は必要ありません。

### Fixed
**原文: Patch 1.28.7-asm.3 contains fixes for the following platform CVEs: [CVE Table and Links]**

**説明:**
Cloud Service Mesh 1.28.7-asm.3 パッチには、以下のプラットフォーム CVE（共通脆弱性識別子）に対する修正が含まれています。
これらの修正は、Proxy (Envoy)、Control Plane (Istioのコンポーネント)、Distroless (コンテナイメージのベース)、CNI (Container Network Interface) など、サービスメッシュを構成する様々なコンポーネントにおけるセキュリティ脆弱性に対応しています。特に、`CVE-2026-27143` は深刻度 Critical (9.8) と評価されており、非常に重要なセキュリティ修正です。その他にも多数の High (7.5以上) および Medium 以上の脆弱性が修正されています。

**影響有無:**
影響なし。
Google Cloud Composer 2 はマネージドサービスであり、基盤となるインフラストラクチャのセキュリティパッチ適用は Google が行います。これらのセキュリティ修正が適用されることで、Composer 環境のセキュリティ態勢が強化されますが、お客様側で直接的な影響を受けたり、対処が必要になったりすることはありません。

**対処方法:**
なし。
マネージドサービスであるため、ユーザー側での具体的な対処は不要です。Googleによるセキュリティ強化の一環として認識してください。

## Cloud Service Mesh

### Announcement
**原文: 1.27.9-asm.4 is now available for in-cluster Cloud Service Mesh. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.27.9-asm.4 uses Envoy v1.35.10-dev.**

**説明:**
Cloud Service Mesh の in-cluster デプロイメント向けに、バージョン 1.27.9-asm.4 がリリースされました。このバージョンでは、Envoy プロキシが v1.35.10-dev を使用しています。既存の Cloud Service Mesh 環境をアップグレードする際には、提供されているアップグレードガイドを参照してください。

**影響有無:**
影響なし。
前述の1.28.7-asm.3と同様に、Google Cloud Composer 2 はマネージドサービスであり、in-cluster デプロイメントに該当しないため、お客様側で直接的な対応は不要です。

**対処方法:**
なし。

### Fixed
**原文: Patch 1.27.9-asm.4 contains fixes for the following platform CVEs: [CVE Table and Links]**

**説明:**
Cloud Service Mesh 1.27.9-asm.4 パッチには、多数のプラットフォーム CVEに対する修正が含まれています。これには、Critical (9.8) の `CVE-2026-27143` を含む、Proxy, Control Plane, Distroless, CNI などに関する重大な脆弱性修正が含まれます。また、過去の CVE (`CVE-2022-31045`, `CVE-2019-14993` など) に対する修正も含まれています。

**影響有無:**
影響なし。
このパッチも、Composer の基盤となるインフラストラクチャのセキュリティ向上に寄与しますが、お客様側で直接的な対処は不要です。

**対処方法:**
なし。

## Cloud Service Mesh

### Announcement
**原文: The following images are now rolling out for managed Cloud Service Mesh: - 1.21.6-asm.32 is rolling out to the rapid release channel. - The regular release channel is being upgraded from 1.20 to 1.21.6-asm.32. - The stable release channel is being upgraded from 1.19 to 1.20.8-asm.80.**

**説明:**
Cloud Service Mesh のマネージド版において、以下の新しいバージョンイメージが各リリースチャネルに展開されています。
*   **Rapid リリースチャネル**: 1.21.6-asm.32 が提供開始。
*   **Regular リリースチャネル**: 1.20 から 1.21.6-asm.32 へアップグレード中。
*   **Stable リリースチャネル**: 1.19 から 1.20.8-asm.80 へアップグレード中。
これらのアップデートは、Google Cloud が管理するサービスメッシュ環境に対して自動的に適用されるものです。

**影響有無:**
影響なし。
Google Cloud Composer 2 はマネージドサービスであり、基盤のインフラストラクチャにマネージド Cloud Service Mesh が使用されている可能性がありますが、その運用・管理は Google の責任範囲です。ユーザーがこれらのバージョン変更によって直接的な操作を行う必要はありません。ただし、マネージドサービスであるComposer環境の安定性、パフォーマンス、セキュリティに影響を与える可能性があるため、これらの更新はサービス全体の品質向上に寄与すると考えられます。

**対処方法:**
なし。
マネージド Cloud Service Mesh は Google によって自動的にアップデートされます。特別な操作は不要です。

### Fixed
**原文: These patch releases contain the fixes for the following CVEs: [CVE Table and Links]**

**説明:**
上記マネージド Cloud Service Mesh の各バージョンアップにおいて、多数の CVE に対する修正が含まれています。これには、Critical (9.8) の `CVE-2026-27143` を含む、Proxy, Control Plane, Distroless, CNI などに関する重大な脆弱性修正が含まれます。

**影響有無:**
影響なし。
マネージドサービスである Google Cloud Composer 2 の基盤におけるセキュリティ強化として認識されます。ユーザー側のサービス運用に直接的な変更や影響はありません。

**対処方法:**
なし。
Google によるセキュリティ強化として、自動的に適用されます。

---

### 用語説明

*   **Cloud Service Mesh (CSM)**: Google Cloud が提供するマネージドなサービスメッシュプラットフォーム。オープンソースの Istio をベースにしており、マイクロサービス間のトラフィック管理、ポリシー適用、セキュリティ、可観測性などを提供します。
*   **In-cluster Cloud Service Mesh**: ユーザーが自身の GKE (Google Kubernetes Engine) クラスタに Istio/Cloud Service Mesh のコントロールプレーンおよびデータプレーン（Envoy プロキシなど）をデプロイし、管理する形態です。ユーザー自身がバージョンアップや設定変更を行う必要があります。
*   **Managed Cloud Service Mesh**: Google Cloud がコントロールプレーンを完全に管理し、データプレーンはユーザーの GKE クラスタにデプロイされる形態です。コントロールプレーンのアップグレードやパッチ適用は Google が行います。
*   **Envoy**: CNCF (Cloud Native Computing Foundation) プロジェクトの一部である高性能なオープンソースのサービスメッシュプロキシです。Istio/Cloud Service Mesh のデータプレーンとして、サービス間のトラフィックを処理します。
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアのセキュリティ脆弱性を識別するための国際的な標準識別子です。各 CVE には一意の番号が割り当てられ、脆弱性の詳細情報が提供されます。
*   **Severity (深刻度)**: CVE の深刻度を示す評価基準。CVSS (Common Vulnerability Scoring System) スコアに基づいて Critical, High, Medium, Low などに分類されます。スコアが高いほど深刻度が高いことを意味します。
*   **Proxy**: サービスメッシュにおけるサイドカープロキシ（Envoyなど）を指します。各ワークロードのPodにデプロイされ、そのPodへの/からのすべてのネットワークトラフィックを傍受・処理します。
*   **Control Plane**: サービスメッシュの構成、ポリシー、証明書管理など、メッシュ全体の動作を制御するコンポーネント群（IstioのPilot, Citadel, Galley, Mixerなど）を指します。
*   **Distroless**: 最小限のランタイム依存関係しか含まない、非常に軽量なコンテナイメージのことです。攻撃対象領域を減らし、セキュリティを向上させます。
*   **CNI (Container Network Interface)**: Linuxコンテナのネットワーク構成を行うための標準インターフェースです。Kubernetesなどのコンテナオーケストレーションシステムで利用されます。
*   **Google Cloud Composer 2**: Apache Airflow を Google Cloud 上で実行するためのマネージドサービスです。基盤として Google Kubernetes Engine (GKE) が利用されており、インフラストラクチャの管理は Google が行います。ユーザーは Airflow のワークフロー管理に集中できます。
# Title: June 02, 2026 
Link: https://docs.cloud.google.com/release-notes#June_02_2026<br>
はい、承知いたしました。Google Cloud のリリースノートに基づき、構築済みのサービスへの影響を調査し、簡潔に回答いたします。

---

# Apigee X

## Announcement

原文: On June 2nd, 2026, we released an updated version of Apigee Cassandra.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigee X の基盤コンポーネントである Apigee Cassandra の更新版が2026年6月2日にリリースされました。この更新は、本日よりすべてのGoogle Cloudゾーンで順次展開（ロールアウト）されており、完了までに4営業日以上かかる場合があります。このロールアウトが完了するまで、Apigee インスタンスに新しい機能や修正が適用されない可能性があります。

影響有無: **影響あり（軽微）**
Apigee X をご利用中の場合、その基盤である Apigee Cassandra が更新されます。これによりサービスが停止することはありませんが、新しい機能やセキュリティ修正が適用されるまで、Google Cloudが管理するロールアウト期間を待つ必要があります。お客様の運用に直接的な影響を及ぼすものではありませんが、バックエンドインフラストラクチャの更新が行われていることを認識しておく必要があります。

対処方法: 特段、お客様側で実施すべき対処はありません。Google Cloudによって自動的に更新が適用されます。ロールアウト完了まで、新しい機能や修正がインスタンスに反映されない可能性がある点をご留意ください。

用語説明:
*   **Apigee X**: Google Cloudが提供するフルマネージドAPI管理プラットフォームです。APIの設計、セキュアな公開、運用、分析などをサポートします。
*   **Apigee Cassandra**: Apigee X の基盤となるデータストアとして利用される分散型NoSQLデータベースです。API関連のメタデータやランタイムデータなどを格納します。
*   **ロールアウト (Rollout)**: ソフトウェアやサービスの新しいバージョンを、段階的かつ計画的に本番環境に展開していくプロセスを指します。これにより、変更による影響を最小限に抑え、問題が発生した場合に早期に検知・対応できるようにします。

## Security

原文: | Bug ID | Description |
| --- | --- |
| **Apigee Cassandra security update** | **Security fix for Apigee Cassandra infrastructure.** This addresses the following vulnerabilities:- CVE-2026-39820- CVE-2026-42499- CVE-2026-39836- CVE-2026-33814- CVE-2026-42501- CVE-2026-33811- CVE-2026-39825- CVE-2026-39817- CVE-2026-39823- CVE-2026-39819- CVE-2026-39826 |
This addresses the following vulnerabilities:- CVE-2026-39820- CVE-2026-42499- CVE-2026-39836- CVE-2026-33814- CVE-2026-42501- CVE-2026-33811- CVE-2026-39825- CVE-2026-39817- CVE-2026-39823- CVE-2026-39819- CVE-2026-39826

[CVE-2026-39820](https://nvd.nist.gov/vuln/detail/CVE-2026-39820)
[CVE-2026-42499](https://nvd.nist.gov/vuln/detail/CVE-2026-42499)
[CVE-2026-39836](https://nvd.nist.gov/vuln/detail/CVE-2026-39836)
[CVE-2026-33814](https://nvd.nist.gov/vuln/detail/CVE-2026-33814)
[CVE-2026-42501](https://nvd.nist.gov/vuln/detail/CVE-2026-42501)
[CVE-2026-33811](https://nvd.nist.gov/vuln/detail/CVE-2026-33811)
[CVE-2026-39825](https://nvd.nist.gov/vuln/detail/CVE-2026-39825)
[CVE-2026-39817](https://nvd.nist.gov/vuln/detail/CVE-2026-39817)
[CVE-2026-39823](https://nvd.nist.gov/vuln/detail/CVE-2026-39823)
[CVE-2026-39819](https://nvd.nist.gov/vuln/detail/CVE-2026-39819)
[CVE-2026-39826](https://nvd.nist.gov/vuln/detail/CVE-2026-39826)

説明: Apigee Cassandra のインフラストラクチャに対してセキュリティ修正が適用されました。これにより、上記にリストされた複数の共通脆弱性識別子（CVE）で特定された脆弱性が解決されます。これらの脆弱性修正は、Apigee Cassandra の更新と同時に適用されます。

影響有無: **影響あり（ポジティブ）**
Apigee X の基盤インフラストラクチャにおけるセキュリティが強化されます。この修正は、Google Cloudが管理する基盤部分で行われるため、お客様の運用に直接的な影響はありませんが、システムのセキュリティ体制が向上します。

対処方法: 特段、お客様側で実施すべき対処はありません。Google Cloudが自動的に修正を適用します。これにより、お客様のApigee X環境のセキュリティが向上します。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: 共通脆弱性識別子。公開されている情報セキュリティの脆弱性に関する名称と識別子の辞書です。世界中で共有され、脆弱性情報の相互参照を容易にします。
*   **脆弱性**: コンピュータシステムやソフトウェア、ネットワークにおいて、意図しない不正な動作を引き起こす可能性のあるセキュリティ上の欠陥や弱点のことです。

---

# Cloud SDK

## Change

原文: (内容なし)

説明: Cloud SDK の変更カテゴリに、具体的な変更内容が記載されていません。

影響有無: **影響なし**
リリースノートに具体的な変更内容が記載されていないため、この情報からは既存の環境への影響を判断できません。Cloud SDKはGoogle Cloudと対話するためのコマンドラインツールやライブラリ群ですが、今回のリリースノートからは特定の変更がないか、または詳細が省略されています。

対処方法: このリリースノートからは対処すべき事項はありません。もしCloud SDKの利用に問題が発生した場合は、最新のCloud SDKの公式リリースノートを確認するか、必要に応じてCloud SDKのバージョンアップを検討してください。

用語説明:
*   **Cloud SDK**: Google Cloud Platformのサービスをコマンドラインから操作するためのツールセットです。`gcloud`コマンドラインツール、`bq`コマンドラインツール、`gsutil`コマンドラインツールなどを含みます。開発や運用作業に広く利用されます。
# Title: June 01, 2026 
Link: https://docs.cloud.google.com/release-notes#June_01_2026<br>
Google Cloud のリリースノートに基づく調査結果を以下に示します。

---

# BigQuery

## Change

原文:
The Facebook Ads connector for the BigQuery Data Transfer Service now supports data transfers from the following Facebook Ads reports:

- `AdInsightsMMM`
- `Ads`
- `AdCreatives`
- `AdSets`
- `Campaigns`
- `AdImages`
- `AdLabels`
- `Businesses`
- `CustomAudiences`

説明：
BigQuery Data Transfer Service の Facebook Ads コネクタが、新たに複数のFacebook Adsレポートタイプからのデータ転送をサポートするようになりました。これにより、既存の `AdInsights` レポートに加えて、より詳細なキャンペーン、広告セット、クリエイティブ、ビジネス情報、カスタムオーディエンスなどのデータをBigQueryへ自動的に転送し、分析することが可能になります。

影響有無：
**影響なし（機能拡張のため）**
これは既存機能の動作を変更するものではなく、サポートされるレポートタイプを追加する機能拡張です。現在BigQuery Data Transfer ServiceのFacebook Adsコネクタを利用していない場合は、全く影響はありません。すでに利用している場合でも、既存のデータ転送設定には影響がなく、転送が中断されたり、設定変更が強制されたりすることはありません。新たにサポートされたレポートからのデータを取り込みたい場合にのみ、この新機能を利用することが可能です。

対処方法：
特に必要な対処はありません。
もし、新たにサポートされたFacebook Adsレポート（例: `Campaigns`, `AdSets`, `AdCreatives`など）のデータをBigQueryに転送したい場合は、BigQuery Data Transfer Serviceで新しいデータ転送ジョブを作成するか、既存の転送設定を編集して、これらの新しいレポートタイプを選択してください。

用語説明：
*   **BigQuery Data Transfer Service (BQ DTS)**: Google BigQueryへ、外部データソース（SaaSアプリケーション、クラウドストレージ、データウェアハウスなど）からデータを自動的にスケジュール転送するためのサービスです。これにより、ETL（抽出、変換、ロード）プロセスを簡素化し、BigQueryで一元的にデータを分析できます。
*   **Facebook Ads connector**: BQ DTS の機能の一つで、Facebook広告プラットフォームからBigQueryへ広告パフォーマンスデータや関連情報を自動的に取り込むための連携機能です。
*   **Facebook Ads reports**: Facebook広告プラットフォームが提供する各種レポートで、広告キャンペーン、広告セット、広告クリエイティブ、パフォーマンス指標など、広告活動に関する詳細なデータが含まれます。
    *   `AdInsightsMMM`: 広告の測定と最適化に関するインサイトレポート（例: 機械学習モデルを活用したMMM（Marketing Mix Modeling）のためのデータ）。
    *   `Ads`: 個々の広告に関する詳細データ。
    *   `AdCreatives`: 広告に使用されている画像、動画、テキストなどのクリエイティブに関するデータ。
    *   `AdSets`: 広告セット（ターゲットオーディエンス、予算、スケジュールなど）に関するデータ。
    *   `Campaigns`: 広告キャンペーンに関するデータ。
    *   `AdImages`: 広告で使用されている画像アセットに関するデータ。
    *   `AdLabels`: 広告に適用されたラベルに関するデータ。
    *   `Businesses`: Facebookビジネスマネージャで管理されているビジネス情報に関するデータ。
    *   `CustomAudiences`: カスタムオーディエンス（特定のユーザーリスト）に関するデータ。