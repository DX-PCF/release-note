
# Title: May 13, 2026 
Link: https://docs.cloud.google.com/release-notes#May_13_2026<br>
はい、承知いたしました。Google Cloud のリリースノートを元に、Cloud Service Mesh の変更内容について調査し、ご指定の形式で回答します。

---

# Cloud Service Mesh

## Changed (Security)

**原文:**
Proxy version csm_mesh_proxy.20260423_RC03 is rolling out to all Managed Cloud Service Mesh release channels over the next week.

**説明:**
Google Cloud が提供するマネージドサービスメッシュソリューションであるCloud Service Meshにおいて、データプレーンで使用されるプロキシ（Envoyプロキシがベース）のバージョンが `csm_mesh_proxy.20260423_RC03` に更新されます。この新しいプロキシバージョンは、今後1週間をかけて、すべてのマネージドCloud Service Meshのリリースチャネル（例：Stable, Rapidなど）に自動的に展開されます。通常、このようなアップデートには、セキュリティ脆弱性の修正、パフォーマンスの向上、およびバグ修正が含まれます。

**影響有無:**
**影響はありません。**
Cloud Service Meshは「Managed」サービスであり、プロキシの更新はGoogle Cloudによって自動的に行われます。ユーザー側で手動でのバージョンアップ作業や設定変更を行う必要はありません。これらのアップデートは通常、後方互換性が保たれるように設計されており、既存のサービス動作に直接的な影響を与える可能性は非常に低いと考えられます。本リリースはセキュリティ関連の変更であると明記されており、セキュリティ強化が主な目的と推測されます。

**対処方法:**
**特に対処は不要です。**
自動的に適用されるため、ユーザー側での操作は必要ありません。
ただし、万が一の予期せぬ動作に備え、Cloud Service Meshを利用しているアプリケーションの主要なメトリクスやログについて、アップデート展開期間中に軽微な監視を継続することをお勧めします。

**用語説明:**
*   **Cloud Service Mesh**: Google Cloud が提供する、サービス間通信を管理、制御、監視するためのマネージドサービスメッシュソリューションです。オープンソースのIstioをベースにしており、Google Kubernetes Engine (GKE) ワークロードやCompute Engine仮想マシン(VM)で実行されるサービスに対してトラフィック管理、認証、認可、オブザーバビリティ機能を提供します。詳細は[Cloud Service Meshの概要](https://cloud.google.com/service-mesh/docs/overview?hl=ja)を参照してください。
*   **Proxy version**: サービスメッシュのデータプレーンを構成するサイドカープロキシ（通常はEnvoy）のバージョンを指します。このプロキシが各サービスインスタンスにデプロイされ、サービス間のすべてのネットワーク通信を仲介します。
*   **Managed Cloud Service Mesh**: ユーザーがIstioのコントロールプレーンやデータプレーンの基盤インフラの運用（バージョンアップ、パッチ適用、スケーリングなど）を意識することなく、Google Cloudがフルマネージドで提供する運用形態です。これにより、ユーザーはサービスメッシュの恩恵を受けつつ、アプリケーション開発に集中できます。
*   **Release Channels**: ソフトウェアのリリース戦略の一つで、異なる安定性レベルや更新頻度を持つバージョンをユーザーに提供するためのチャネルです。例えば、`Stable`チャネルは最も安定したバージョンを提供し、`Rapid`チャネルはより新しい機能を早く提供する代わりに、安定性が若干低い可能性があります。Cloud Service Meshもこれらのチャネルを通じてプロキシのアップデートが展開されます。
# Title: May 12, 2026 
Link: https://docs.cloud.google.com/release-notes#May_12_2026<br>
Google Cloudのインフラエンジニアとして、ご依頼のリリースノートについて調査いたしました。
構築済みのGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) に直接影響する変更はありませんでしたが、Apigee X、Cloud SQL for PostgreSQL、Compute Engineに関する重要な更新がありましたので、製品ごとに影響と対処方法を以下にまとめます。

---

# Apigee X

## Announcement

原文: On May 12th, 2026, we released an updated version of Apigee (1-17-0-apigee-7).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
2026年5月12日にApigee Xの新しいバージョン（1-17-0-apigee-7）がリリースされました。このリリースの展開（ロールアウト）は、本日開始され、すべてのGoogle Cloudゾーンへの適用が完了するまでに4営業日以上かかる可能性があります。ロールアウトが完了するまで、利用中のApigeeインスタンスには新機能や修正が適用されない場合があります。

影響有無：
影響なし。
Apigee XはGoogle Cloudが提供するフルマネージドサービスであり、バージョンアップはGoogle側で自動的に実施されます。ユーザー側での直接的な操作は不要です。これは今後のサービス改善やセキュリティ強化の基盤となるアナウンスです。

対処方法：
特になし。
ロールアウトの完了を待つことで、自動的に最新バージョンが適用されます。

用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームの最新版。APIの設計、デプロイ、セキュリティ、分析、スートリングなどライフサイクル全体を管理します。
*   **ロールアウト (Rollout)**: ソフトウェアやシステムの新しいバージョンや変更を、段階的または一斉に展開・適用するプロセスを指します。

## Security

原文: | Bug ID | Description |
| --- | --- |
| **511325186, 505460952, 502250074, 491231600, 497357701, 509560467, 496969438, 495897297, 495033618, 511332617, 505183435, 500735547, 500890221** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:  - CVE-2026-42587- CVE-2026-5588- CVE-2026-34480- GHSA-72hv-8253-57qq- CVE-2026-33870- CVE-2026-33871- CVE-2026-35611- CVE-2026-33170- CVE-2026-33169- CVE-2026-33176- CVE-2026-33210- CVE-2026-33186- CVE-2026-42499- CVE-2026-35469- CVE-2026-32281- CVE-2026-27144 |

説明：
Apigeeの基盤における複数のセキュリティ脆弱性が修正されました。これには、以下のCVE（Common Vulnerabilities and Exposures）およびGHSA（GitHub Security Advisory）に関連する修正が含まれます。これらの修正により、Apigee環境のセキュリティ体制が強化されます。

*   [CVE-2026-42587](https://nvd.nist.gov/vuln/detail/CVE-2026-42587)
*   [CVE-2026-5588](https://nvd.nist.gov/vuln/detail/CVE-2026-5588)
*   [CVE-2026-34480](https://nvd.nist.gov/vuln/detail/CVE-2026-34480)
*   [GHSA-72hv-8253-57qq](https://github.com/advisories/GHSA-72hv-8253-57qq)
*   [CVE-2026-33870](https://nvd.nist.gov/vuln/detail/CVE-2026-33870)
*   [CVE-2026-33871](https://nvd.nist.gov/vuln/detail/CVE-2026-33871)
*   [CVE-2026-35611](https://nvd.nist.gov/vuln/detail/CVE-2026-35611)
*   [CVE-2026-33170](https://nvd.nist.gov/vuln/detail/CVE-2026-33170)
*   [CVE-2026-33169](https://nvd.nist.gov/vuln/detail/CVE-2026-33169)
*   [CVE-2026-33176](https://nvd.nist.gov/vuln/detail/CVE-2026-33176)
*   [CVE-2026-33210](https://nvd.nist.gov/vuln/detail/CVE-2026-33210)
*   [CVE-2026-33186](https://nvd.nist.gov/vuln/detail/CVE-2026-33186)
*   [CVE-2026-42499](https://nvd.nist.gov/vuln/detail/CVE-2026-42499)
*   [CVE-2026-35469](https://nvd.nist.gov/vuln/detail/CVE-2026-35469)
*   [CVE-2026-32281](https://nvd.nist.gov/vuln/detail/CVE-2026-32281)
*   [CVE-2026-27144](https://nvd.nist.gov/vuln/detail/CVE-2026-27144)

影響有無：
良い影響。
Apigee Xの基盤におけるセキュリティが向上します。ApigeeはGoogleが管理するサービスであるため、これらのセキュリティパッチは自動的に適用されます。ユーザー側での直接的な対応は不要です。

対処方法：
特になし。
Google Cloudによって自動的にパッチが適用されるため、ユーザー側での追加の対応は不要です。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されているソフトウェアの脆弱性を一意に識別するための共通識別子です。
*   **GHSA (GitHub Security Advisory)**: GitHubが管理するセキュリティアドバイザリデータベースで、主にオープンソースプロジェクトの脆弱性情報を提供します。
*   **Apigeeインフラストラクチャ**: Apigee Xサービスを構成するGoogle Cloud側の基盤となるハードウェア、ソフトウェア、ネットワークなどの全体を指します。

## Fixed

原文: | Bug ID | Description |
| --- | --- |
| **480260846** | Improved XML processing security to prevent external entity injection. |
| **505723451** | Fixed an issue where metadata could be shared across unrelated client sessions. |
| **505645076** | Fixed a security issue in OAuthV2 policy to prevent unauthorized token injection. |
| **503723862** | Fixed a security issue in OAuthV2 policy to prevent unauthorized token injection. |
| **503047744, 410026138, 496021751** | Improved security isolation for PythonScript policy execution. |
| **469694040** | Fixed an issue where custom security policies could intermittently fail to apply, and improved security policy resolution to ensure correct policy selection. |
| **502971220** | Fixed a concurrency issue in streaming response handling to improve stability under high load. |
| **509692565** | Fixed content-length header handling in external processing to prevent incorrect values. |
| **282207038** | Fixed inconsistent timeouts when querying apps by parallelizing credential lookup. |
| **501102321** | Fixed recurring fee calculation in monetization to correctly apply rate plan overrides. |
| **494469747** | Fixed content-length header to reflect actual response body size. |
| **N/A** | Updates to infrastructure and libraries. |

説明：
Apigee Xにおける複数のバグ修正と機能改善が行われました。主な内容は以下の通りです。
*   XML処理における外部エンティティ注入（XXE）攻撃を防ぐためのセキュリティ強化。
*   関連性のないクライアントセッション間でメタデータが共有される問題の修正。
*   OAuthV2ポリシーにおける不正なトークン注入を防ぐためのセキュリティ修正。
*   PythonScriptポリシー実行時のセキュリティ分離の改善。
*   カスタムセキュリティポリシーが断続的に適用に失敗する問題の修正と、ポリシー解決メカニズムの改善。
*   高負荷時のストリーミング応答処理における同時実行性の問題修正による安定性向上。
*   外部処理におけるContent-Lengthヘッダの不正確な値の問題修正。
*   アプリクエリ時の資格情報検索の並列化による、タイムアウトの一貫性の改善。
*   収益化機能における定期課金計算でレートプランの上書きが正しく適用されるよう修正。
*   実際の応答ボディサイズを反映するようにContent-Lengthヘッダを修正。
*   基盤とライブラリの更新。

影響有無：
良い影響。
Apigee Xの安定性、セキュリティ、正確性が向上します。これらの修正はGoogleによって自動的に適用されるため、ユーザー側での追加の対応は不要です。特に、OAuthV2ポリシーやPythonScriptポリシーを使用している場合、セキュリティと信頼性が向上します。

対処方法：
特になし。

用語説明：
*   **OAuthV2 Policy**: ApigeeでAPIへのアクセスを保護するために使用されるポリシーの一つで、OAuth 2.0プロトコルを実装します。
*   **PythonScript Policy**: ApigeeのAPIプロキシ内でPythonスクリプトを実行するためのポリシーで、カスタムロジックや高度な処理を組み込むことができます。
*   **外部エンティティ注入 (XXE)**: XMLパーサーの脆弱性を利用して、外部のエンティティをXMLドキュメントに注入し、機密情報の漏洩やDoS攻撃などを引き起こす攻撃手法です。
*   **Content-Lengthヘッダ**: HTTPレスポンスのボディのサイズ（バイト数）を示すHTTPヘッダです。

---

# Cloud SQL for PostgreSQL

## Change

原文: The command for upgrading Cloud SQL instances to the new network architecture has been re-enabled.
For more information, see Upgrade an instance to the new network architecture.

説明：
Cloud SQL for PostgreSQLインスタンスを、より新しいネットワークアーキテクチャにアップグレードするためのコマンドが再度有効化されました。詳細については、公式ドキュメント「Upgrade an instance to the new network architecture」を参照してください。

影響有無：
影響なし。
これは既存のCloud SQL for PostgreSQLインスタンスに対して、必要に応じて新しいネットワークアーキテクチャへの移行を可能にするための機能の再有効化です。現在のネットワークアーキテクチャで運用を続けている限り、直接的な影響はありません。ただし、将来的にネットワークの最適化や機能拡張を目的として移行を検討する際には、この機能が利用可能になったことは良い影響となります。

対処方法：
新しいネットワークアーキテクチャへの移行を計画している場合のみ、[Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture) のドキュメントを参照し、計画を立てて移行を検討してください。現状維持の場合は、特別な対処は不要です。

用語説明：
*   **Cloud SQL for PostgreSQL**: Google Cloudが提供するフルマネージドなPostgreSQLデータベースサービスです。
*   **ネットワークアーキテクチャ**: クラウドサービスにおけるネットワーク構成、接続性、ルーティング、セキュリティなどの設計や構造を指します。新しいアーキテクチャは通常、パフォーマンス、セキュリティ、スケーラビリティの向上を目指します。

---

# Compute Engine

## Security

原文: A vulnerability in AMD firmware (CVE-2025-61971, CVE-2025-61972, CVE-2024-36315) that could compromise SEV-SNP guests has been addressed.
For more information, see the GCP-2026-031 security bulletin.

説明：
AMDファームウェアに存在する複数の脆弱性（CVE-2025-61971, CVE-2025-61972, CVE-2024-36315）が修正されました。これらの脆弱性は、SEV-SNP（Secure Encrypted Virtualization-Secure Nested Paging）を使用する仮想マシン（ゲスト）を危険にさらす可能性がありました。詳細はセキュリティ速報[GCP-2026-031](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-031)で確認できます。

影響有無：
良い影響。
Compute Engineの基盤となるAMDプロセッサのファームウェアレベルでのセキュリティが強化されました。Google Cloudは、これらの基盤となる脆弱性に対して迅速にパッチを適用するため、ユーザー側での直接的な操作は不要です。SEV-SNPを利用しているワークロードのセキュリティが向上します。

対処方法：
特になし。
Google Cloudのマネージドな対応により、ユーザーは安全な環境を利用できます。

用語説明：
*   **AMD firmware**: AMD製のプロセッサやチップセットに組み込まれた低レベルのソフトウェア（ファームウェア）です。
*   **SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging)**: AMD EPYCプロセッサが提供するセキュリティ機能で、仮想マシン（VM）のメモリを暗号化し、ハイパーバイザや他のVMからの不正アクセスを防ぎ、データの機密性と整合性を保護します。
*   **脆弱性 (Vulnerability)**: システムやソフトウェアの欠陥や弱点で、悪用されるとセキュリティ上の問題を引き起こす可能性があるものです。
*   **セキュリティ速報 (Security Bulletin)**: 特定のセキュリティ脆弱性や修正に関する公式のアナウンスです。

## Security

原文: A vulnerability (CVE-2025-54518) about potential corruption within the micro-operation (OP) cache in Zen 2 microarchitecture processors was discovered and has been addressed.
For more information, see the GCP-2026-032 security bulletin.

説明：
Zen 2マイクロアーキテクチャプロセッサのマイクロオペレーション（OP）キャッシュにおける潜在的な破損に関する脆弱性（CVE-2025-54518）が発見され、修正されました。詳細はセキュリティ速報[GCP-2026-032](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-032)で確認できます。

影響有無：
良い影響。
Compute Engineの基盤となるAMD Zen 2プロセッサのセキュリティが強化されました。Google Cloudは、これらの基盤となる脆弱性に対して迅速にパッチを適用するため、ユーザー側での直接的な操作は不要です。Zen 2ベースのVMインスタンスを利用しているワークロードのセキュリティが向上します。

対処方法：
特になし。
Google Cloudのマネージドな対応により、ユーザーは安全な環境を利用できます。

用語説明：
*   **Zen 2 microarchitecture**: AMDが開発したCPUマイクロアーキテクチャの一つで、Ryzen 3000シリーズやEPYC Romeシリーズなどのプロセッサに採用されています。
*   **マイクロオペレーション (OP) キャッシュ**: CPU内部で命令をより高速に処理するために、デコードされた命令（マイクロオペレーション）を一時的に保存するキャッシュメモリです。
*   **脆弱性 (Vulnerability)**: システムやソフトウェアの欠陥や弱点で、悪用されるとセキュリティ上の問題を引き起こす可能性があるものです。
*   **セキュリティ速報 (Security Bulletin)**: 特定のセキュリティ脆弱性や修正に関する公式のアナウンスです。

---
# Title: May 11, 2026 
Link: https://docs.cloud.google.com/release-notes#May_11_2026<br>
# AlloyDB for PostgreSQL
## Announcement
**原文:** AlloyDB now offers extended support for clusters running major PostgreSQL versions that have reached their end-of-life (EOL) as defined by the PostgreSQL community. Extended support provides an additional three years of support after the end of regular support, giving you more time to plan and perform major version upgrades. For more information, see Extended support for AlloyDB for PostgreSQL.
[Extended support for AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/extended-support)

**説明:**
AlloyDB for PostgreSQLにおいて、PostgreSQLコミュニティによって定義された**EOL (End-of-Life)** に達した主要バージョンを実行しているクラスターに対する**延長サポート**が提供されるようになりました。この延長サポートは、通常のサポートが終了した後、さらに3年間追加でサポートを提供することで、お客様が主要なバージョンアップグレードを計画し、実行するための十分な時間的余裕を与えます。詳細については、提供されたドキュメントリンクを参照してください。

**影響有無:**
影響は**ありません**。
これは、既存のAlloyDB for PostgreSQLユーザーにとって、EOL間近またはすでにEOLを迎えたPostgreSQLバージョンを使用している場合に、バージョンアップグレードの計画と実行により多くの時間を確保できるという**メリットを提供する新機能のアナウンス**です。既存のサービス運用に直接的な破壊的変更やパフォーマンスの低下、予期せぬ料金の増加といった負の影響はありません。

**対処方法:**
このアナウンス自体で、お客様側で直ちに対応が必要なことはありません。
もしお客様のAlloyDB for PostgreSQLインスタンスでEOL間近のPostgreSQLバージョンを利用している場合、この延長サポートを有効活用することで、アップグレード計画をより慎重に、かつ余裕をもって進めることが可能になります。詳細な情報や延長サポートの利用方法、関連する費用については、提供されている公式ドキュメント「[Extended support for AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/extended-support)」をご確認ください。

**用語説明:**
*   **EOL (End-of-Life):** ソフトウェアやハードウェア製品のサポート期間が終了する時点を指します。EOLを迎えると、セキュリティパッチの提供や技術サポートが打ち切られるため、運用上のリスクが増大します。
*   **PostgreSQL community:** オープンソースのリレーショナルデータベースであるPostgreSQLの開発、保守、および普及を担うグローバルなコミュニティです。PostgreSQLの各バージョンのサポート期間やEOLは、このコミュニティによって決定されます。
*   **延長サポート (Extended support):** 通常の製品サポート期間が終了した後も、特定の条件の下で追加のサポート（セキュリティアップデートや技術的な支援など）を提供するサービスです。これにより、ユーザーは新しいバージョンへの移行計画を立てるための猶予期間を得ることができます。
*   **主要バージョンアップグレード (Major version upgrade):** データベースシステムの大きなバージョンアップを指します（例: PostgreSQL 14から15へのアップグレード）。通常、互換性のない変更や新機能の追加が含まれるため、ダウンタイムを伴うことがあり、入念な計画、テスト、移行作業が必要です。