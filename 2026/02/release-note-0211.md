
# Title: February 09, 2026 
Link: https://docs.cloud.google.com/release-notes#February_09_2026<br>
Google Cloud のインフラエンジニアとして、ご提示いただいたリリースノートについて、構築済みのサービスへの影響有無を調査し、簡潔に回答いたします。

---

# AlloyDB for PostgreSQL
## Fixed
原文: We are announcing the release of support for the AlloyDB language connectors and Auth Proxy with Auto IAM Authentication and managed connection pooling. This feature and the fix for the issue from below is available starting with maintenance version 20260107.02_05. Clusters with a maintenance window that may not have received this release can use self-service maintenance to perform a maintenance update.
[Auto IAM Authentication](https://docs.cloud.google.com/alloydb/docs/connect-iam#automatic)
[self-service maintenance](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance)

説明:
AlloyDB for PostgreSQLにおいて、言語コネクタ、自動IAM認証を伴うAuth Proxy、およびマネージド接続プーリングのサポートがリリースされました。これらの新機能と関連する修正は、メンテナンスバージョン `20260107.02_05` 以降で利用可能です。自動メンテナンスウィンドウでこのリリースが適用されていないクラスタは、セルフサービスメンテナンス機能を使用して手動でアップデートを実行できます。

影響有無: **影響なし (機能追加と改善)**
このリリースは既存の機能に影響を与える非互換性変更ではなく、新しい機能の追加と安定性向上のための修正が含まれています。既存のワークロードに対して直接的な悪影響を及ぼす可能性は低いと考えられます。むしろ、セキュリティ強化（IAM認証）やパフォーマンス効率化（接続プーリング）の恩恵を受ける可能性があります。

対処方法:
*   現在ご利用中のAlloyDBクラスタのメンテナンスバージョンが `20260107.02_05` より古い場合、自動メンテナンスウィンドウでの適用を待つか、これらの新機能を利用したい場合や修正を早期に適用したい場合は、[セルフサービスメンテナンス](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance) を利用して手動でのアップデートを検討してください。
*   Auto IAM Authenticationやマネージド接続プーリングの導入を検討している場合は、このアップデートが前提となります。

用語説明:
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、エンタープライズグレードのマネージドなPostgreSQL互換データベースサービスです。
*   **Auth Proxy**: データベースへの接続を認証・認可するプロキシサービスです。
*   **Auto IAM Authentication**: Google CloudのIdentity and Access Management (IAM) を使用して、データベースユーザーの認証を自動的に行う機能です。セキュリティを向上させ、認証情報の管理を簡素化します。
*   **Managed Connection Pooling**: データベース接続の確立と再利用を効率的に行うための機能で、アプリケーションのパフォーマンス向上に寄与します。
*   **Self-service maintenance**: ユーザーが任意のタイミングで、AlloyDBクラスタのメンテナンスアップデートを手動で実行できる機能です。

---

# Cloud Service Mesh
## Announcement
原文: The following images are now rolling out for managed Cloud Service Mesh:
- 1.21.6-asm.10 is rolling out to the rapid release channel.
- 1.20.8-asm.63 is rolling out to the regular release channel.
- 1.19.10-asm.57 is rolling out to the stable release channel.
These patch releases contain the fixes for the following managed Cloud Service Mesh CVEs:

| CVE | Proxy | Control Plane | CNI | Distroless | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2025-61729 | Yes | Yes | - | Yes | High (7.5) |
| CVE-2025-61727 | Yes | Yes | - | Yes | Medium (6.5) |
| CVE-2024-41996 | Yes | Yes | - | Yes | High (7.5) |
| CVE-2025-9086 | Yes | Yes | - | Yes | High (7.5) |
| CVE-2021-46848 | Yes | Yes | - | Yes | Critical (9.1) |
| CVE-2025-13151 | Yes | Yes | - | Yes | High (7.5) |
| CVE-2025-68973 | Yes | Yes | - | Yes | High (7.8) |
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)
[CVE-2025-61727](https://pkg.go.dev/vuln/GO-2025-4175)
[CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996)
[CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086)
[CVE-2021-46848](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2021-46848)
[CVE-2025-13151](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-13151)
[CVE-2025-68973](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-68973)

説明:
マネージドCloud Service Mesh (Anthos Service Mesh) の新しいイメージバージョンが各リリースチャネル（rapid, regular, stable）で展開されています。これらのパッチリリースには、複数の共通脆弱性識別子 (CVE) に対するセキュリティ修正が含まれており、中程度のものから、重大度「Critical (9.1)」のCVE-2021-46848を含む「High」なものまで多岐にわたります。

影響有無: **影響あり (セキュリティ強化)**
Cloud Service Meshを利用している場合、これらのセキュリティ脆弱性修正が適用されることで、既存のサービスメッシュ環境のセキュリティ体制が大幅に向上します。本リリースはパッチリリースであり、機能変更よりもセキュリティ修正が主目的であるため、既存のワークロードに対する非互換性や機能的な影響は基本的にありません。マネージドサービスであるため、通常は自動的に最新のパッチが適用されるものと推測されます。

対処方法:
*   マネージドCloud Service Meshを利用している場合、通常はGoogle Cloudによって自動的に最新のパッチバージョンに更新されます。ユーザー側での直接的な操作は不要な場合が多いです。
*   ただし、セキュリティパッチが確実に適用されたかを確認するため、定期的にCloud Service Meshのバージョンを確認し、最新の状態が維持されていることを監視することを推奨します。
*   特定のバージョンのまま運用している場合や、自動更新を一時停止している場合は、本リリースに含まれるCriticalおよびHigh severityの脆弱性の内容を確認し、速やかにアップデート計画を立てることを強く推奨します。

用語説明:
*   **Cloud Service Mesh (Anthos Service Mesh)**: Google Cloudが提供するマネージドなIstioベースのサービスメッシュソリューションです。サービスの接続、監視、セキュリティ、信頼性を一元的に管理します。
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアやハードウェアにおける既知のセキュリティ脆弱性に対して割り当てられる、国際的に標準化された識別子です。
*   **Patch Release**: 主にバグ修正やセキュリティ修正を目的とした、小規模なソフトウェアリリースです。
*   **Release Channel (rapid, regular, stable)**: Google CloudのサービスやGKEなどの製品が、新しいバージョンを顧客にリリースする際の提供速度と安定性のレベルを示すチャネルです。
    *   **Rapid**: 最も早く新機能や修正が提供されるが、本番環境での利用は慎重に検討すべき。
    *   **Regular**: バランスの取れたリリースサイクル。ほとんどのユーザーに推奨される。
    *   **Stable**: 最も安定性が高く、長期間運用される環境に適している。
*   **Proxy (サイドカープロキシ)**: サービスメッシュにおいて、アプリケーションコンテナと一緒にデプロイされ、ネットワークトラフィックのルーティング、監視、セキュリティポリシーの適用などを行うコンポーネントです。
*   **Control Plane**: サービスメッシュ全体の管理・制御を行うコンポーネント群で、ポリシーの適用、設定の配布、メッシュ内の通信管理などを担当します。
*   **CNI (Container Network Interface)**: Linuxコンテナのネットワーク構成を行うための標準インターフェースです。
*   **Distroless**: 必要最小限のOSコンポーネントのみを含む、非常に軽量なコンテナイメージのことです。攻撃対象領域を減らし、セキュリティを向上させます。