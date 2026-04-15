
# Title: April 14, 2026 
Link: https://docs.cloud.google.com/release-notes#April_14_2026<br>
はい、Google Cloudのリリースノートを元に、製品への影響調査と回答を作成します。
Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)の利用を考慮しつつ、各リリースノートについて影響有無と対処方法を記載します。

---

# Cloud SQL for PostgreSQL

## Breaking

**原文:**
As of April 10, 2026, you can create, run, and edit Gemini Cloud Assist investigations only if you have a Premium Support contract. You can use Gemini Cloud Assist investigations to monitor and troubleshoot your Cloud SQL instance with AI assistance.
[Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations)
[Premium Support contract](https://cloud.google.com/support/premium)
[monitor and troubleshoot your Cloud SQL instance with AI assistance](https://docs.cloud.com/sql/docs/postgres/monitor-troubleshoot-with-ai)
If you ran an investigation prior to April 10, 2026, then the results of the investigation continue to be available to you in the Google Cloud console.

**説明:**
2026年4月10日以降、Cloud SQLインスタンスのモニタリングとトラブルシューティングにAIアシスタンスを提供する「Gemini Cloud Assist investigations」機能を利用するには、Google Cloudの「Premium Support」契約が必須となります。この日付より前に実行された調査の結果は、引き続きGoogle Cloud Consoleで確認可能です。この変更は、当該機能の利用条件が限定されることを意味します。

**影響有無:**
**影響あり（将来的な潜在的影響）**
現在のGoogle Cloud Composerの運用において、バックエンドとしてCloud SQL for PostgreSQLが使用されている場合、直接的な運用への影響は現時点ではありません。しかし、将来的にCloud SQL for PostgreSQLのパフォーマンス問題やトラブルシューティングのために「Gemini Cloud Assist investigations」の利用を検討する可能性がある場合、2026年4月10日以降はGoogle CloudのPremium Support契約が必須となるため、サポート費用が増加する可能性があります。現在この機能を利用していない場合でも、将来的な機能拡張やトラブルシューティングの手段として、この変更を認識しておく必要があります。

**対処方法:**
1.  **機能の利用計画の確認:** 現在「Gemini Cloud Assist investigations」を利用しているか、または今後利用する計画があるかを確認してください。
2.  **Premium Supportの検討:** もし将来的にこの機能の利用を希望する場合、Premium Support契約の要否およびそのコストについて、組織内で検討を開始してください。
3.  **情報収集:** 提供されているドキュメントリンク（Gemini Cloud Assist investigations、Premium Support contract）を参照し、機能の詳細とサポートプランについて理解を深めてください。

**用語説明:**
*   **Gemini Cloud Assist investigations**: Google CloudのAI技術「Gemini」を活用し、Cloud SQLインスタンスのパフォーマンス問題や潜在的な課題をAIが分析・特定し、解決策を提案する支援機能です。データベースの専門知識がなくても、AIの洞察に基づいて効率的なトラブルシューティングが可能になります。
*   **Premium Support contract**: Google Cloudが提供する最上位のテクニカルサポートプランです。24時間365日の緊急対応、専任のテクニカルアカウントマネージャー (TAM)、プロアクティブなガイダンス、優先的なケースハンドリングなど、高度なサポートサービスが含まれます。通常のサポートプランと比較して費用が高くなります。
*   **Breaking Change**: 既存のシステムやアプリケーションの互換性を損なう変更を指します。通常、上位互換性がなく、ユーザー側での対応やコード変更が必要となる場合があります。本件では、機能の利用条件の変更がこれに該当します。

---

# Compute Engine

## Security

**原文:**
A vulnerability (CVE-2025-54510) about AMD SEV-SNP guest memory integrity has been addressed. For more information, see the GCP-2026-019 security bulletin.
[GCP-2026-019 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-019)

**説明:**
AMD SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging) を利用するゲスト仮想マシンのメモリ整合性に関する脆弱性 (CVE-2025-54510) が修正されました。この修正に関する詳細は、GCP-2026-019セキュリティ速報で確認できます。

**影響有無:**
**影響なし（ポジティブなセキュリティ強化）**
このリリースは、Compute Engineプラットフォームにおけるセキュリティ脆弱性の修正に関するものであり、Google Cloud側で対応が完了しています。ユーザー側で直接的な運用への影響や操作は不要です。むしろ、基盤となるインフラストラクチャのセキュリティが強化されたため、既存のワークロード（Composerインスタンスが稼働するVMなど）の安全性向上が期待できます。

**対処方法:**
通常、ユーザー側での対処は不要です。
しかし、情報セキュリティの観点から、必要に応じて提供されたGCP-2026-019セキュリティ速報を参照し、脆弱性の詳細とGoogle Cloudによる対応状況を確認しておくことを推奨します。特に、高いセキュリティ要件を持つワークロードでAMD SEV-SNP機能を明示的に利用している場合は、この修正がどのように適用されたかを把握しておくことが望ましいです。

**用語説明:**
*   **AMD SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging)**: AMD EPYCプロセッサに搭載されているセキュリティ機能の一つです。仮想マシン（VM）のメモリを暗号化し、ハイパーバイザーや他のVMからVM内の機密データへの不正アクセスを防ぎます。また、ゲストVMのメモリページの整合性を保証することで、より高いセキュリティと隔離性を提供します。
*   **CVE-ID (Common Vulnerabilities and Exposures Identifier)**: 公開されているソフトウェアやハードウェアのセキュリティ脆弱性に割り当てられる共通の識別子です。これにより、脆弱性の情報共有と追跡が容易になります。
*   **セキュリティ速報 (Security Bulletin)**: ソフトウェアベンダーやクラウドプロバイダが、製品やサービスにおけるセキュリティ関連の重要な情報（脆弱性の修正、新しいセキュリティ機能の追加など）をユーザーに通知するために発行する文書です。
# Title: April 13, 2026 
Link: https://docs.cloud.google.com/release-notes#April_13_2026<br>
Google Cloud インフラエンジニアとして、リリースノートに基づくサービスへの影響調査結果を報告します。

---

# Cloud Logging
## Libraries
原文:
[v1.15.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.14.0...logging/v1.15.0)

説明：
Cloud LoggingのGo言語用クライアントライブラリがバージョン1.15.0にアップデートされました。この変更は、`go.mod`や`go.sum`ファイルなどでGoクライアントライブラリの依存関係を管理しているGoアプリケーション開発者に影響します。通常、マイナーバージョンアップでは後方互換性が維持されつつ、機能追加やバグ修正が行われます。

影響有無：
**影響なし（直接的には）**
*   現在、お使いのGoogle Cloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3)はPythonベースであり、Go言語で開発されたアプリケーションではありません。そのため、このGoクライアントライブラリのバージョンアップがComposer環境に直接影響を与えることはありません。
*   ただし、システム内にGo言語で開発され、Cloud Logging APIを直接利用しているカスタムアプリケーションが存在する場合は、このライブラリの更新が影響を及ぼす可能性があります。

対処方法：
Go言語で開発されたカスタムアプリケーションがあり、Cloud Logging Goクライアントライブラリを利用している場合は、以下の対応を検討してください。
1.  **依存関係の確認**: アプリケーションの依存関係（`go.mod`など）で`cloud.google.com/go/logging`が利用されているか確認します。
2.  **更新の検討**: 最新バージョンへの更新を検討し、更新前に十分なテストを実施して互換性を確認してください。
3.  **変更内容の確認**: GitHubの比較リンク（上記原文参照）から、v1.14.0からv1.15.0への具体的な変更内容を確認し、影響の有無を詳細に評価してください。

用語説明：
*   **Go クライアントライブラリ**: Go言語で書かれたアプリケーションがGoogle Cloudの各種サービスと連携するためのSDK（Software Development Kit）の一部。
*   **go.mod / go.sum**: Go言語のモジュールシステムで使用されるファイルで、プロジェクトの依存関係とそのハッシュ値を管理します。

---

# Cloud Service Mesh
## Announcement
原文:
**1.28.5-asm.12 is now available for in-cluster Cloud Service Mesh.**
This patch release contains fixes for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-33186 | Yes | Yes | Yes | Yes | Critical (9.1) |
| CVE-2026-3731 | Yes | Yes | No | Yes | High (7.5) |
| CVE-2026-3784 | Yes | Yes | No | Yes | Medium (6.5) |
| CVE-2026-1965 | Yes | Yes | No | Yes | Medium (6.5) |
| CVE-2026-29111 | Yes | Yes | No | Yes | Medium (5.5) |
| CVE-2026-3783 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2025-0167 | Yes | Yes | No | Yes | Low (3.4) |
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186)
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731)
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784)
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965)
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111)
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783)
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.5-asm.12 uses Envoy 1.36.5-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：
インクラスター型のCloud Service Meshバージョン1.28.5-asm.12がリリースされました。このパッチリリースには、CVE-2026-33186（Critical severity）を含む複数のプラットフォームCVEに対するセキュリティ修正が含まれています。このバージョンでは、Envoyプロキシが1.36.5-devに更新されています。

影響有無：
**影響あり**
*   現在、インクラスター型Cloud Service Meshバージョン1.28.xを使用している場合、または今後このバージョンへの導入を検討している場合、セキュリティ脆弱性の修正が提供されるため影響があります。
*   特にCritical（深刻度9.1）の脆弱性が含まれているため、本バージョンへのアップグレードを強く推奨します。

対処方法：
*   **アップグレードの検討**: 現在、インクラスター型のCloud Service Meshを運用している場合は、[Cloud Service Meshのアップグレード](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)ドキュメントを参照し、早急に1.28.5-asm.12へのアップグレードを計画・実行してください。
*   **環境の確認**: お使いのCloud Service Meshのデプロイタイプ（インクラスター型かマネージド型か）と現在のバージョンを確認してください。

用語説明：
*   **Cloud Service Mesh (ASM)**: Google Cloud上でサービスメッシュ機能を提供するプラットフォームです。マイクロサービス間の通信管理、セキュリティ、可観測性を向上させます。
*   **インクラスター型**: ユーザーのGKEクラスタ内にService Meshのコントロールプレーンがデプロイされる形式です。ユーザーがコントロールプレーンの運用を管理します。
*   **CVE (Common Vulnerabilities and Exposures)**: 一般に公開されている情報セキュリティ脆弱性に対する識別子です。
*   **Severity (深刻度)**: 脆弱性の深刻度を示す指標で、Criticalは最も高い危険度を示します。
*   **Envoy**: Service Meshにおいてデータプレーンを構成する高性能なオープンソースエッジ/サービスプロキシです。

---

## Announcement
原文:
**1.27.8-asm.9 is now available for in-cluster Cloud Service Mesh.**
This patch release contains fixes for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-33186 | Yes | Yes | Yes | Yes | Critical (9.1) |
| CVE-2026-3731 | Yes | Yes | No | Yes | High (7.5) |
| CVE-2026-3784 | Yes | Yes | No | Yes | Medium (6.5) |
| CVE-2026-1965 | Yes | Yes | No | Yes | Medium (6.5) |
| CVE-2026-29111 | Yes | Yes | No | Yes | Medium (5.5) |
| CVE-2026-3783 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2025-0167 | Yes | Yes | No | Yes | Low (3.4) |
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186)
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731)
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784)
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965)
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111)
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783)
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.27.8-asm.9 uses Envoy 1.35.10-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade)

説明：
インクラスター型のCloud Service Meshバージョン1.27.8-asm.9がリリースされました。このパッチリリースには、CVE-2026-33186（Critical severity）を含む複数のプラットフォームCVEに対するセキュリティ修正が含まれています。このバージョンでは、Envoyプロキシが1.35.10-devに更新されています。

影響有無：
**影響あり**
*   現在、インクラスター型Cloud Service Meshバージョン1.27.xを使用している場合、または今後このバージョンへの導入を検討している場合、セキュリティ脆弱性の修正が提供されるため影響があります。
*   特にCritical（深刻度9.1）の脆弱性が含まれているため、本バージョンへのアップグレードを強く推奨します。

対処方法：
*   **アップグレードの検討**: 現在、インクラスター型のCloud Service Meshを運用している場合は、[Cloud Service Meshのアップグレード](https://docs.cloud.com/service-mesh/v1.27/docs/upgrade/upgrade)ドキュメントを参照し、早急に1.27.8-asm.9へのアップグレードを計画・実行してください。
*   **環境の確認**: お使いのCloud Service Meshのデプロイタイプと現在のバージョンを確認してください。

用語説明：
*   **Cloud Service Mesh (ASM)**, **インクラスター型**, **CVE**, **Severity**, **Envoy**: 上記の項目を参照。

---

## Announcement
原文:
The following images are now rolling out for managed Cloud Service Mesh:
- 1.21.6-asm.19 is rolling out to the rapid release channel.
- 1.20.8-asm.73 is rolling out to the regular release channel.
- 1.19.10-asm.66 is rolling out to the stable release channel.
These patch releases contain the fixes for the following CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | MDPC | Severity |
| --- | --- | --- | --- | --- | --- | --- |
| CVE-2022-27943 | Yes | Yes | Yes | No | No | Medium (5.5) |
| CVE-2023-4039 | Yes | Yes | Yes | No | No | Medium (4.8) |
| CVE-2023-4527 | Yes | Yes | Yes | No | No | Medium (6.5) |
| CVE-2023-4806 | Yes | Yes | Yes | No | No | Medium (5.9) |
| CVE-2023-4911 | Yes | Yes | Yes | No | No | High (7.8) |
| CVE-2023-5156 | Yes | Yes | Yes | No | No | High (7.5) |
| CVE-2023-6246 | Yes | Yes | Yes | No | No | High (7.8) |
| CVE-2024-2961 | Yes | Yes | Yes | No | No | High (7.3) |
| CVE-2024-33599 | Yes | Yes | Yes | No | No | High (8.1) |
| CVE-2024-33600 | Yes | Yes | Yes | No | No | Medium (5.9) |
| CVE-2024-33601 | Yes | Yes | Yes | No | No | High (7.3) |
| CVE-2024-33602 | Yes | Yes | Yes | No | No | High (7.4) |
| CVE-2025-0167 | Yes | Yes | No | No | No | Low (3.4) |
| CVE-2025-0395 | Yes | Yes | Yes | Yes | No | Medium (6.2) |
| CVE-2025-15281 | Yes | Yes | Yes | No | No | High (7.5) |
| CVE-2025-4802 | Yes | Yes | Yes | Yes | No | High (7.8) |
| CVE-2025-68972 | Yes | Yes | No | No | No | Medium (4.7) |
| CVE-2025-8058 | Yes | Yes | Yes | No | No | Low (0.0) |
| CVE-2025-8941 | Yes | Yes | No | No | No | Low (0.0) |
| CVE-2026-0861 | Yes | Yes | Yes | No | No | High (8.4) |
| CVE-2026-0915 | Yes | Yes | Yes | No | No | High (7.5) |
| CVE-2026-1965 | Yes | Yes | No | Yes | Yes | Medium (6.5) |
| CVE-2026-29111 | Yes | Yes | No | Yes | Yes | Medium (5.5) |
| CVE-2026-33186 | Yes | Yes | Yes | No | No | Critical (9.1) |
| CVE-2026-3731 | Yes | Yes | No | Yes | Yes | High (7.5) |
| CVE-2026-3783 | Yes | Yes | No | Yes | Yes | Medium (5.3) |
| CVE-2026-3784 | Yes | Yes | No | No | No | Medium (6.5) |
[CVE-2022-27943](https://security-tracker.debian.org/tracker/CVE-2022-27943)
[CVE-2023-4039](https://security-tracker.debian.org/tracker/CVE-2023-4039)
[CVE-2023-4527](https://security-tracker.debian.org/tracker/CVE-2023-4527)
[CVE-2023-4806](https://security-tracker.debian.org/tracker/CVE-2023-4806)
[CVE-2023-4911](https://security-tracker.debian.org/tracker/CVE-2023-4911)
[CVE-2023-5156](https://security-tracker.debian.org/tracker/CVE-2023-5156)
[CVE-2023-6246](https://security-tracker.debian.org/tracker/CVE-2023-6246)
[CVE-2024-2961](https://security-tracker.debian.org/tracker/CVE-2024-2961)
[CVE-2024-33599](https://security-tracker.debian.org/tracker/CVE-2024-33599)
[CVE-2024-33600](https://security-tracker.debian.org/tracker/CVE-2024-33600)
[CVE-2024-33601](https://security-tracker.debian.org/tracker/CVE-2024-33601)
[CVE-2024-33602](https://security-tracker.debian.org/tracker/CVE-2024-33602)
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167)
[CVE-2025-0395](https://security-tracker.debian.org/tracker/CVE-2025-0395)
[CVE-2025-15281](https://security-tracker.debian.org/tracker/CVE-2025-15281)
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802)
[CVE-2025-68972](https://security-tracker.debian.org/tracker/CVE-2025-68972)
[CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058)
[CVE-2025-8941](https://security-tracker.debian.org/tracker/CVE-2025-8941)
[CVE-2026-0861](https://security-tracker.debian.org/tracker/CVE-2026-0861)
[CVE-2026-0915](https://security-tracker.debian.org/tracker/CVE-2026-0915)
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965)
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111)
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186)
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731)
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783)
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784)

説明：
マネージド型のCloud Service Mesh向けに、以下の新しいイメージが各リリースチャネルに展開されています。
*   **Rapidチャンネル**: 1.21.6-asm.19
*   **Regularチャンネル**: 1.20.8-asm.73
*   **Stableチャンネル**: 1.19.10-asm.66
これらのパッチリリースには、CVE-2026-33186（Critical severity）を含む多数のセキュリティ脆弱性修正が含まれています。

影響有無：
**影響あり**
*   現在、マネージド型Cloud Service Meshを利用している場合、これらの新しいイメージの展開によりセキュリティが向上します。
*   利用しているリリースチャネルに応じて、自動的に更新が適用されるため、直接的な手動操作は不要なことが多いですが、更新が完了するまでは脆弱性に曝露される可能性があります。
*   特にCritical（深刻度9.1）の脆弱性が含まれているため、速やかな更新の適用が重要です。

対処方法：
*   **リリースチャネルの確認**: お使いのマネージド型Cloud Service Meshがどのリリースチャネルに登録されているかを確認してください。
*   **自動更新の確認**: マネージド型ASMは通常、Googleによって自動的に更新されますが、更新の進行状況をモニタリングし、対象バージョンへの更新が完了したことを確認してください。
*   **バージョンの確認**: デプロイされているASMのバージョンを確認し、最新のパッチが適用されていることを確認してください。

用語説明：
*   **マネージド型**: GoogleがCloud Service Meshのコントロールプレーンの運用と管理を完全に担当する形式です。ユーザーはデータプレーン（Envoyプロキシ）のみを管理します。
*   **リリースチャネル**: Google Cloudのサービスやプロダクトにおいて、機能更新やパッチリリースの提供速度を制御する仕組みです。通常、Rapid (迅速), Regular (通常), Stable (安定) などのチャネルがあります。

---

## Announcement
原文:
**1.26.8-asm.5 is now available for in-cluster Cloud Service Mesh.**
This patch release contains fixes for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-33186 | Yes | Yes | Yes | Yes | Critical (9.1) |
| CVE-2026-3731 | Yes | Yes | No | Yes | High (7.5) |
| CVE-2026-3784 | Yes | Yes | No | Yes | Medium (6.5) |
| CVE-2026-1965 | Yes | Yes | No | Yes | Medium (6.5) |
| CVE-2026-29111 | Yes | Yes | No | Yes | Medium (5.5) |
| CVE-2026-3783 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2025-68972 | Yes | No | No | Yes | Medium (4.7) |
| CVE-2025-0167 | Yes | Yes | No | Yes | Low (3.4) |
| CVE-2025-8941 | Yes | No | No | Yes | Low (0.0) |
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186)
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731)
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784)
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965)
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111)
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783)
[CVE-2025-68972](https://security-tracker.debian.org/tracker/CVE-2025-68972)
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167)
[CVE-2025-8941](https://security-tracker.debian.org/tracker/CVE-2025-8941)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.26.8-asm.5 uses Envoy 1.34.14-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade)

説明：
インクラスター型のCloud Service Meshバージョン1.26.8-asm.5がリリースされました。このパッチリリースには、CVE-2026-33186（Critical severity）を含む複数のプラットフォームCVEに対するセキュリティ修正が含まれています。このバージョンでは、Envoyプロキシが1.34.14-devに更新されています。

影響有無：
**影響あり**
*   現在、インクラスター型Cloud Service Meshバージョン1.26.xを使用している場合、または今後このバージョンへの導入を検討している場合、セキュリティ脆弱性の修正が提供されるため影響があります。
*   特にCritical（深刻度9.1）の脆弱性が含まれているため、本バージョンへのアップグレードを強く推奨します。

対処方法：
