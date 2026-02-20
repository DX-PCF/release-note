
# Title: February 18, 2026 
Link: https://docs.cloud.google.com/release-notes#February_18_2026<br>
Google Cloud リリースノート調査結果をご報告いたします。

---
# Cloud SQL for PostgreSQL

## Deprecated
原文: Control of MCP use with organization policies is deprecated.
After March 17, 2026, organization policies that use the
`gcp.managed.allowedMCPServices` constraint won't work,
and you can control MCP use with IAM deny policies.
For more information about controlling MCP use, see
[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

説明：2026年3月17日以降、組織ポリシーで `gcp.managed.allowedMCPServices` 制約を使用したMCP (Managed Control Plane) の使用制御が廃止されます。今後は、IAM deny ポリシーを使用してMCPの使用を制御することが推奨されます。

影響有無：**要確認 (将来的な影響あり)**
現在 `gcp.managed.allowedMCPServices` 組織ポリシーを使用している場合に影響があります。使用している場合でも、2026年3月17日までは現在の設定が機能しますが、それ以降は機能しなくなります。

対処方法：
*   現在 `gcp.managed.allowedMCPServices` 組織ポリシーを使用しているか確認してください。
*   使用している場合は、2026年3月17日までにIAM deny ポリシーへの移行計画を立ててください。
*   詳細については、[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam) を参照し、移行手順を確認してください。

用語説明：
*   **MCP (Managed Control Plane)**: クラウドサービスの一部としてGoogleによって管理されるコントロールプレーン。ユーザーは基盤となるインフラストラクチャの管理から解放され、サービスの利用に集中できます。
*   **組織ポリシー (Organization Policies)**: Google Cloudリソース全体で特定のリソース構成を強制できるサービス。セキュリティ、規制遵守、コスト管理などの目的で利用されます。
*   **IAM deny ポリシー (IAM deny policies)**: 特定のプリンシパルが特定のリソースに対して特定のアクションを実行することを明示的に拒否するIAMポリシーの機能。従来のIAM許可ポリシーよりも優先されます。

## Change
原文: After March 17, 2026, when you enable the Cloud SQL Admin API
(`sqladmin.googleapis.com`)`, the Cloud SQL remote MCP server is
enabled automatically.
The Cloud SQL remote MCP server is in [Preview](https://cloud.google.com/products/#product-launch-stages).

説明：2026年3月17日以降、Cloud SQL Admin API (`sqladmin.googleapis.com`) を有効にすると、Cloud SQL のリモートMCPサーバーが自動的に有効になります。この機能は現在プレビュー段階です。

影響有無：**影響なし (現状はプレビュー機能のため)**
Cloud SQL Admin API は通常使用されているAPIですが、自動有効化が始まるのは2026年3月17日以降です。また、リモートMCPサーバー機能自体が現在プレビュー段階であるため、本番環境への即時影響はありません。

対処方法：現時点での直接的な対応は不要です。将来的にリモートMCPサーバーがGA（一般提供）になった際に、その機能と影響について再評価してください。

用語説明：
*   **Cloud SQL Admin API**: Cloud SQLインスタンスの作成、管理、設定変更などを行うためのAPI。ほとんどのCloud SQL操作はこのAPIを通じて行われます。
*   **プレビュー (Preview)**: Google Cloudの製品ライフサイクルにおけるフェーズの一つ。機能が公開されているが、まだ開発中であり、将来変更される可能性があることを示します。本番環境での使用は推奨されません。

---
# Cloud Service Mesh

## Announcement
原文: CNI and managed data plane controller version 1.23.6-asm.28 is rolling out to all
release channels.
While the managed data plane automatically updates Envoy Proxies by restarting
workloads, you must manually restart any StatefulSets and Jobs.
This patch includes the fix for the following CVEs:
| Name | CNI | MDPC | Severity |
| --- | --- | --- | --- |
| CVE-2017-11164 | Yes | Yes | High (7.5) |
| CVE-2022-27943 | Yes | Yes | Medium (5.5) |
| CVE-2022-41409 | Yes | Yes | High (7.5) |
| CVE-2022-4899 | Yes | Yes | High (7.5) |
| CVE-2023-29383 | Yes | Yes | Low (3.3) |
| CVE-2023-34969 | Yes | Yes | Medium (6.5) |
| CVE-2023-50495 | Yes | Yes | Medium (6.5) |
| CVE-2023-7008 | Yes | Yes | Medium (5.9) |
| CVE-2024-41996 | Yes | Yes | High (7.5) |
| CVE-2025-8114 | Yes | Yes | Medium (4.7) |
| CVE-2025-9086 | Yes | Yes | High (7.5) |

説明：Cloud Service Mesh (Anthos Service Mesh) のCNI (Container Network Interface) とマネージドデータプレーンコントローラーがバージョン1.23.6-asm.28へアップデートされます。マネージドデータプレーンはワークロードを再起動することでEnvoyプロキシを自動的に更新しますが、StatefulSetsとJobsについては手動での再起動が必要です。このパッチには、複数のCVE（共通脆弱性識別子）に対するセキュリティ修正（High Severityを含む）が含まれています。

影響有無：**影響あり (セキュリティ修正、手動作業が必要な場合あり)**
Cloud Service Meshを利用していない場合は影響ありません。利用している場合、セキュリティ修正が適用されるため推奨されるアップデートです。StatefulSetsやJobsを使用している場合、Envoyプロキシの更新を反映させるために手動での再起動が必要です。

対処方法：
*   現在Cloud Service Mesh（Anthos Service Mesh）を利用しているかどうか確認してください。
*   利用している場合は、リリースチャンネルに応じて順次アップデートが適用されます。
*   **StatefulSets** や **Jobs** をデプロイしている場合は、アップデート適用後にEnvoyプロキシの更新を反映させるため、それらのワークロードを再起動してください。
*   含まれるCVEsはHigh Severityのものも含まれているため、セキュリティ向上の観点から速やかに対応を検討してください。

用語説明：
*   **Cloud Service Mesh (Anthos Service Mesh)**: Google Cloudが提供するフルマネージドのサービスメッシュ。トラフィック管理、セキュリティ、観測性などの機能を提供し、マイクロサービスアプリケーションの運用を簡素化します。
*   **CNI (Container Network Interface)**: コンテナとネットワークスタックを接続するための仕様。Kubernetesクラスタ内のポッドがネットワークと通信するために使用されます。
*   **マネージドデータプレーン (Managed Data Plane)**: ユーザーがデータプレーンの管理から解放され、Google CloudがEnvoyプロキシなどのデータプレーンコンポーネントのライフサイクルを管理するサービスメッシュの運用モデル。
*   **Envoy Proxy**: サービスメッシュのサイドカープロキシとして広く利用される高性能なL7プロキシ。サービス間の通信を中継し、トラフィック管理、ロードバランシング、セキュリティ、観測性などを実現します。
*   **StatefulSet**: KubernetesのワークロードAPIオブジェクトの一つ。永続ストレージや特定のネットワークIDが必要なステートフルなアプリケーション（データベースなど）を管理するために使用されます。
*   **Jobs**: KubernetesのワークロードAPIオブジェクトの一つ。指定された数のPodを完了するまで実行し、成功したことを保証します。バッチ処理や一度限りのタスクに適しています。
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されているソフトウェアのセキュリティ脆弱性に対して割り当てられる一意の識別子。

---
# Google Cloud Armor

## Change
原文: Cloud Armor preconfigured WAF rules support for inspection up to the first 64 kB (either 8 kB, 16 kB, 32 kB, 48 kB, or 64 kB) of the request body content  is Generally Available.
[preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules)
[request body content](https://docs.cloud.google.com/armor/docs/security-policy-overview#request-body)

説明：Google Cloud Armor の事前構成済みWAFルールにおける、リクエストボディコンテンツの先頭64KBまでの検査サポートがGA（一般提供）になりました。これにより、リクエストボディの検査深度を8KB、16KB、32KB、48KB、64KBの中から選択できるようになります。

影響有無：**影響なし (機能強化、既存設定への影響なし)**
これは機能の追加および強化であり、既存のCloud Armor設定に直接的な影響はありません。WAFルールによるリクエストボディの検査深度をより深く設定できるようになり、セキュリティを強化する選択肢が増えます。

対処方法：現時点で特別な対応は不要です。より深いリクエストボディ検査が必要な場合は、既存のCloud Armorセキュリティポリシーの設定を変更して、検査深度を64KBまで拡張することを検討してください。

用語説明：
*   **Google Cloud Armor**: Google Cloudの分散型サービス拒否（DDoS）攻撃保護およびWebアプリケーションファイアウォール（WAF）サービス。アプリケーションを一般的なウェブベースの攻撃から保護します。
*   **事前構成済みWAFルール (preconfigured WAF rules)**: Google Cloud Armorが提供する、一般的なWeb攻撃パターン（例: SQLインジェクション、クロスサイトスクリプティング）を検出するために事前に定義されたルールセット。
*   **GA (Generally Available)**: Google Cloudの製品ライフサイクルにおけるフェーズの一つ。機能が安定しており、GoogleのSLA（サービスレベルアグリーメント）によってサポートされ、本番環境での使用が推奨されることを示します。

---
# Google Kubernetes Engine

## Security
原文: Multiple security vulnerabilities have been identified in the OpenSSL library.
The most significant finding is CVE-2025-15467, a critical vulnerability that
might allow for remote code execution (RCE) or denial of service (DoS) attacks
via network-based vectors.
For more information, see the
[GCP-2026-006 security bulletin](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2026-006-gke).

説明：OpenSSLライブラリに複数のセキュリティ脆弱性が特定されました。最も重大なものはCVE-2025-15467で、これはリモートコード実行（RCE）やサービス拒否（DoS）攻撃を引き起こす可能性のあるクリティカルな脆弱性です。詳細については、GCP-2026-006セキュリティ速報を参照してください。

影響有無：**影響あり (重大なセキュリティ脆弱性)**
Google Kubernetes Engine (GKE) を利用している場合、基盤となるOpenSSLライブラリの脆弱性であるため、GKEクラスタやノードイメージに影響を与える可能性があります。Googleによって修正が提供されるため、クラスタの自動アップグレードまたは手動アップグレードを通じてパッチが適用されると予想されます。

対処方法：
*   現在Google Kubernetes Engine (GKE) を利用しているかどうか確認してください。
*   利用している場合、GKEクラスタが自動アップグレードの対象となっているか確認し、定期的なアップグレードウィンドウが設定されていることを推奨します。
*   手動アップグレードを行っている場合は、Googleから提供されるセキュリティパッチを含む新しいGKEバージョンへの速やかなアップグレードを計画してください。
*   詳細については、[GCP-2026-006 security bulletin](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2026-006-gke) を確認し、推奨される対応措置に従ってください。

用語説明：
*   **OpenSSL**: SSL/TLSプロトコルの実装を提供するオープンソースの暗号ライブラリ。多くのアプリケーションやシステムで暗号化通信のために使用されています。
*   **RCE (Remote Code Execution)**: 攻撃者がリモートから標的のシステム上で任意のコードを実行できる脆弱性。非常に危険な脆弱性の一つです。
*   **DoS (Denial of Service) 攻撃**: サービスを意図的に利用不能にする攻撃。正当なユーザーがサービスを利用できなくなります。
*   **GCP security bulletin**: Google Cloudが公開するセキュリティ脆弱性に関する公式速報。特定の脆弱性の詳細、影響、および推奨される対策が記載されています。
# Title: February 17, 2026 
Link: https://docs.cloud.google.com/release-notes#February_17_2026<br>
Google Cloudのリリースノートに関する調査結果を以下にご報告します。
今回のリリースノートは、主に「Model Context Protocol (MCP)」に関連する内容で構成されています。MCPは、生成AIエージェントがGoogle Cloudデータベースと連携する際に使用されるプロトコルであり、セキュリティ強化と管理方法の変更が中心となります。

現在ご利用中のGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) については、今回のリリースノートに直接的な変更は含まれていません。しかし、Composerのワークフロー内でAlloyDB, BigQuery, Cloud SQL, Compute Engine, Firestore, GKE, Spannerといったサービスを利用している場合、これらのサービスに対する変更が間接的に影響する可能性があります。特に、2026年3月17日以降の「MCPサーバーの自動有効化」や「組織ポリシーの非推奨化」は、将来的な運用やセキュリティポリシーに影響を与える可能性がありますので、各サービスの項をご確認ください。

---

# AlloyDB for PostgreSQL
## Announcement
原文: New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see Best practices for securing agent interactions with Model Context Protocol.
[Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/alloydb/docs/ai/secure-agent-interactions-mcp)

説明：
生成AIエージェントがModel Context Protocol (MCP) を使用してGoogle Cloudデータベースと連携する際のセキュリティに関する新しいベストプラクティスが公開されました。このガイドは、最小権限の原則、ネイティブなデータベース制御、セキュアなエージェント設計といった主要なセキュリティ対策を網羅しており、より安全なAIアプリケーション構築に役立ちます。

影響有無：
影響なし。これはセキュリティに関する推奨事項であり、既存のAlloyDB for PostgreSQLの運用に直接的な変更や影響を与えるものではありません。

対処方法：
現在の運用に緊急の対処は不要です。将来的に生成AIエージェントとAlloyDB for PostgreSQLを連携させるシステムを設計・構築する際に、セキュリティ設計の参照情報として活用することを推奨します。

用語説明：
*   **Model Context Protocol (MCP)**: 生成AIエージェントがGoogle Cloud上のデータベースと安全に相互作用するためのプロトコル。AIモデルがデータベースから情報を取得したり、データベースに書き込んだりする際の通信を定義します。
*   **最小権限の原則 (Least Privilege)**: システムの利用者やプロセスが、その業務を遂行するために必要最小限の権限のみを持つべきであるというセキュリティ原則。
*   **ネイティブなデータベース制御 (Native Database Controls)**: データベースシステム自体が提供するアクセス制御、監査ログ、暗号化などのセキュリティ機能。

---

# BigQuery
## Deprecated
原文: Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices constraint` won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM deny policies.
[Control MCP use with IAM deny policies](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

説明：
BigQueryにおけるModel Context Protocol (MCP) の利用制御に関して、組織ポリシー `gcp.managed.allowedMCPServices` を用いた方法は非推奨となります。2026年3月17日以降、この組織ポリシーは機能しなくなり、今後はIAM拒否ポリシー (IAM deny policies) を使用してMCPの利用を制御することになります。

影響有無：
現時点での直接的な影響はありません。しかし、BigQueryでMCPの利用を組織ポリシー `gcp.managed.allowedMCPServices` によって制御している場合、2026年3月17日以降はそのポリシーが無効になります。このため、将来的にIAM拒否ポリシーへの移行計画が必要となります。

対処方法：
現在、組織ポリシー `gcp.managed.allowedMCPServices` を利用してBigQueryにおけるMCPの使用を制御している場合は、2026年3月17日までにIAM拒否ポリシーへの移行計画を策定し、実施することを推奨します。新規にMCPの利用を制御する場合は、IAM拒否ポリシーの利用を検討してください。

用語説明：
*   **組織ポリシー (Organization Policies)**: Google Cloudリソースの構成を組織レベルで一元的に制御するためのサービス。特定の制約 (Constraints) を設定することで、リソースの作成や変更に関するルールを強制できます。
*   **IAM拒否ポリシー (IAM Deny Policies)**: 特定のプリンシパル（ユーザー、サービスアカウントなど）に対して、特定のアクションを明示的に禁止するIAMポリシー。許可ポリシー（Allow Policy）よりも優先されるため、より厳格なアクセス制御が可能です。
*   **Constraint**: 組織ポリシーで適用する制約のID。ここでは `gcp.managed.allowedMCPServices` が該当します。

---

## Change
原文: After March 17, 2026, when you enable BigQuery, the BigQuery MCP server is automatically enabled.

説明：
2026年3月17日以降、BigQueryサービスを有効化する際に、BigQuery Model Context Protocol (MCP) サーバーが自動的に有効化されるようになります。

影響有無：
現時点での直接的な影響はありません。2026年3月17日以降にBigQueryを新規に有効化したり、既存のプロジェクトでBigQueryが自動的に有効化されるような処理を行う場合に影響が出ます。MCPサーバーが自動的に有効化されることで、意図しないリソース消費や、セキュリティポリシー（もしMCPの利用を明示的に禁止している場合）との整合性に注意が必要です。

対処方法：
現在のBigQueryの運用に緊急の対処は不要です。2026年3月17日以降にBigQueryをプロビジョニングする際は、MCPサーバーが自動的に有効化されることを認識し、関連するセキュリティ設定や課金への影響を評価してください。もしMCPの利用を厳格に制御したい場合は、上記で説明されたIAM拒否ポリシーの導入を検討してください。

---

# Cloud SQL for PostgreSQL
## Announcement
原文: New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see Best practices for securing agent interactions with Model Context Protocol.
[Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/sql/docs/postgres/secure-agent-interactions-mcp)

説明：
生成AIエージェントがModel Context Protocol (MCP) を使用してGoogle Cloudデータベースと連携する際のセキュリティに関する新しいベストプラクティスが公開されました。このガイドは、最小権限の原則、ネイティブなデータベース制御、セキュアなエージェント設計といった主要なセキュリティ対策を網羅しており、より安全なAIアプリケーション構築に役立ちます。

影響有無：
影響なし。これはセキュリティに関する推奨事項であり、既存のCloud SQL for PostgreSQLの運用に直接的な変更や影響を与えるものではありません。

対処方法：
現在の運用に緊急の対処は不要です。将来的に生成AIエージェントとCloud SQL for PostgreSQLを連携させるシステムを設計・構築する際に、セキュリティ設計の参照情報として活用することを推奨します。

---

# Compute Engine
## Change
原文: After March 17, 2026, when you enable Compute Engine, the Compute Engine MCP server is automatically enabled.

説明：
2026年3月17日以降、Compute Engineサービスを有効化する際に、Compute Engine Model Context Protocol (MCP) サーバーが自動的に有効化されるようになります。

影響有無：
現時点での直接的な影響はありません。2026年3月17日以降にCompute Engineを新規に有効化したり、既存のプロジェクトでCompute Engineが自動的に有効化されるような処理を行う場合に影響が出ます。MCPサーバーが自動的に有効化されることで、意図しないリソース消費や、セキュリティポリシー（もしMCPの利用を明示的に禁止している場合）との整合性に注意が必要です。

対処方法：
現在のCompute Engineの運用に緊急の対処は不要です。2026年3月17日以降にCompute Engineをプロビジョニングする際は、MCPサーバーが自動的に有効化されることを認識し、関連するセキュリティ設定や課金への影響を評価してください。もしMCPの利用を厳格に制御したい場合は、後述のIAM拒否ポリシーの導入を検討してください。

---

## Deprecated
原文: Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM.
[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

説明：
Compute EngineにおけるModel Context Protocol (MCP) の利用制御に関して、組織ポリシー `gcp.managed.allowedMCPServices` を用いた方法は非推奨となります。2026年3月17日以降、この組織ポリシーは機能しなくなり、今後はIAM拒否ポリシー (IAM deny policies) を使用してMCPの利用を制御することになります。

影響有無：
現時点での直接的な影響はありません。しかし、Compute EngineでMCPの利用を組織ポリシー `gcp.managed.allowedMCPServices` によって制御している場合、2026年3月17日以降はそのポリシーが無効になります。このため、将来的にIAM拒否ポリシーへの移行計画が必要となります。

対処方法：
現在、組織ポリシー `gcp.managed.allowedMCPServices` を利用してCompute EngineにおけるMCPの使用を制御している場合は、2026年3月17日までにIAM拒否ポリシーへの移行計画を策定し、実施することを推奨します。新規にMCPの利用を制御する場合は、IAM拒否ポリシーの利用を検討してください。

---

# Firestore
## Announcement
原文: New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see Best practices for securing agent interactions with Model Context Protocol.
[Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/firestore/native/docs/secure-agent-interactions-mcp)

説明：
生成AIエージェントがModel Context Protocol (MCP) を使用してGoogle Cloudデータベースと連携する際のセキュリティに関する新しいベストプラクティスが公開されました。このガイドは、最小権限の原則、ネイティブなデータベース制御、セキュアなエージェント設計といった主要なセキュリティ対策を網羅しており、より安全なAIアプリケーション構築に役立ちます。

影響有無：
影響なし。これはセキュリティに関する推奨事項であり、既存のFirestoreの運用に直接的な変更や影響を与えるものではありません。

対処方法：
現在の運用に緊急の対処は不要です。将来的に生成AIエージェントとFirestoreを連携させるシステムを設計・構築する際に、セキュリティ設計の参照情報として活用することを推奨します。

---

## Deprecated
原文: Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM.
[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

説明：
FirestoreにおけるModel Context Protocol (MCP) の利用制御に関して、組織ポリシー `gcp.managed.allowedMCPServices` を用いた方法は非推奨となります。2026年3月17日以降、この組織ポリシーは機能しなくなり、今後はIAM拒否ポリシー (IAM deny policies) を使用してMCPの利用を制御することになります。

影響有無：
現時点での直接的な影響はありません。しかし、FirestoreでMCPの利用を組織ポリシー `gcp.managed.allowedMCPServices` によって制御している場合、2026年3月17日以降はそのポリシーが無効になります。このため、将来的にIAM拒否ポリシーへの移行計画が必要となります。

対処方法：
現在、組織ポリシー `gcp.managed.allowedMCPServices` を利用してFirestoreにおけるMCPの使用を制御している場合は、2026年3月17日までにIAM拒否ポリシーへの移行計画を策定し、実施することを推奨します。新規にMCPの利用を制御する場合は、IAM拒否ポリシーの利用を検討してください。

---

## Change
原文: After March 17, 2026, when you enable Firestore, the Firestore MCP server is automatically enabled.

説明：
2026年3月17日以降、Firestoreサービスを有効化する際に、Firestore Model Context Protocol (MCP) サーバーが自動的に有効化されるようになります。

影響有無：
現時点での直接的な影響はありません。2026年3月17日以降にFirestoreを新規に有効化したり、既存のプロジェクトでFirestoreが自動的に有効化されるような処理を行う場合に影響が出ます。MCPサーバーが自動的に有効化されることで、意図しないリソース消費や、セキュリティポリシー（もしMCPの利用を明示的に禁止している場合）との整合性に注意が必要です。

対処方法：
現在のFirestoreの運用に緊急の対処は不要です。2026年3月17日以降にFirestoreをプロビジョニングする際は、MCPサーバーが自動的に有効化されることを認識し、関連するセキュリティ設定や課金への影響を評価してください。もしMCPの利用を厳格に制御したい場合は、上記で説明されたIAM拒否ポリシーの導入を検討してください。

---

# Google Kubernetes Engine
## Deprecated
原文: Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM.
[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

説明：
Google Kubernetes Engine (GKE) におけるModel Context Protocol (MCP) の利用制御に関して、組織ポリシー `gcp.managed.allowedMCPServices` を用いた方法は非推奨となります。2026年3月17日以降、この組織ポリシーは機能しなくなり、今後はIAM拒否ポリシー (IAM deny policies) を使用してMCPの利用を制御することになります。

影響有無：
現時点での直接的な影響はありません。しかし、GKEでMCPの利用を組織ポリシー `gcp.managed.allowedMCPServices` によって制御している場合、2026年3月17日以降はそのポリシーが無効になります。このため、将来的にIAM拒否ポリシーへの移行計画が必要となります。

対処方法：
現在、組織ポリシー `gcp.managed.allowedMCPServices` を利用してGKEにおけるMCPの使用を制御している場合は、2026年3月17日までにIAM拒否ポリシーへの移行計画を策定し、実施することを推奨します。新規にMCPの利用を制御する場合は、IAM拒否ポリシーの利用を検討してください。

---

## Change
原文: After March 17, 2026, when you enable GKE, the GKE MCP server is automatically enabled.

説明：
2026年3月17日以降、Google Kubernetes Engine (GKE) サービスを有効化する際に、GKE Model Context Protocol (MCP) サーバーが自動的に有効化されるようになります。

影響有無：
現時点での直接的な影響はありません。2026年3月17日以降にGKEを新規に有効化したり、既存のプロジェクトでGKEが自動的に有効化されるような処理を行う場合に影響が出ます。MCPサーバーが自動的に有効化されることで、意図しないリソース消費や、セキュリティポリシー（もしMCPの利用を明示的に禁止している場合）との整合性に注意が必要です。

対処方法：
現在のGKEの運用に緊急の対処は不要です。2026年3月17日以降にGKEをプロビジョニングする際は、MCPサーバーが自動的に有効化されることを認識し、関連するセキュリティ設定や課金への影響を評価してください。もしMCPの利用を厳格に制御したい場合は、上記で説明されたIAM拒否ポリシーの導入を検討してください。

---

# Spanner
## Announcement
原文: New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see Best practices for securing agent interactions with Model Context Protocol. This feature is in Preview.
[Preview](https://cloud.google.com/products/#product-launch-stages)

説明：
生成AIエージェントがModel Context Protocol (MCP) を使用してGoogle Cloudデータベースと連携する際のセキュリティに関する新しいベストプラクティスが公開されました。このガイドは、最小権限の原則、ネイティブなデータベース制御、セキュアなエージェント設計といった主要なセキュリティ対策を網羅しており、より安全なAIアプリケーション構築に役立ちます。この機能は現在プレビュー版です。

影響有無：
影響なし。これはセキュリティに関する推奨事項であり、既存のSpannerの運用に直接的な変更や影響を与えるものではありません。ただし、言及されているMCP連携機能自体がプレビュー段階であることに留意が必要です。

対処方法：
現在の運用に緊急の対処は不要です。将来的に生成AIエージェントとSpannerを連携させるシステムを設計・構築する際に、セキュリティ設計の参照情報として活用することを推奨します。プレビュー機能であるため、本番環境での利用には慎重な評価と検証が必要です。

用語説明：
*   **プレビュー (Preview)**: Google Cloudのプロダクトのリリースステージの一つ。一般提供 (GA: General Availability) の前に提供される機能で、フィードバック収集を目的としています。本番環境での使用は推奨されません。

---
# Title: February 16, 2026 
Link: https://docs.cloud.google.com/release-notes#February_16_2026<br>
Google Cloud インフラエンジニアとして、Google Cloud Composer のリリースノートに基づき、お客様の構築済みサービスへの影響を調査し、以下の通りご報告いたします。

現在ご利用中の環境: **Google Cloud Composer 2 (Composer version 2.7.1、Airflow version 2.7.3)**

---

# Cloud Composer

## Change

原文:
```
 New Airflow builds
are available in Cloud Composer 3:

[Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
- composer-3-airflow-3.1.0-build.9
- composer-3-airflow-2.10.5-build.26 (default)
- composer-3-airflow-2.9.3-build.46

[composer-3-airflow-3.1.0-build.9](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-0-build-9)
[composer-3-airflow-2.10.5-build.26](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-26)
[composer-3-airflow-2.9.3-build.46](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-46)
```
説明:
Cloud Composer 3環境向けに、最新のAirflowビルドバージョンが新たに提供開始されました。これには、Airflow 3.1.0、2.10.5 (デフォルト)、および2.9.3が含まれます。

影響有無:
**影響なし**。
お客様の環境はCloud Composer 2 (Composer version 2.7.1)であるため、Cloud Composer 3に関するこの更新は直接的な影響を及ぼしません。

対処方法:
なし。

用語説明:
*   **Airflow ビルド**: Apache Airflowの特定のバージョンと、Google Cloud Composerが提供する基盤イメージや追加パッケージを組み合わせたCloud Composerの環境パッケージのことです。
*   **Cloud Composer 3**: Cloud Composerの主要なメジャーバージョンであり、Cloud Composer 2とは異なるアーキテクチャや機能セットを持つ場合があります。

---

## Change

原文:
```
 New images
are available in Cloud Composer 2:

[images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
- composer-2.16.4-airflow-2.10.5 (default)
- composer-2.16.4-airflow-2.9.3

[composer-2.16.4-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-16-4-airflow-2-10-5)
[composer-2.16.4-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-16-4-airflow-2-9-3)
```
説明:
Cloud Composer 2環境向けに、新しいイメージバージョン `composer-2.16.4-airflow-2.10.5` (デフォルト) および `composer-2.16.4-airflow-2.9.3` が利用可能になりました。これらのイメージには、最新のセキュリティパッチや機能改善が含まれている可能性があります。

影響有無:
**間接的な影響あり。**
お客様の現在のComposerバージョンは `2.7.1` (Airflow `2.7.3`) であり、新たに提供されたのは `2.16.4` です。この変更自体が自動的に環境をアップグレードすることはありませんが、現在のバージョンが古いことを示唆しています。
新しいデフォルトイメージ (`composer-2.16.4-airflow-2.10.5`) は、Airflow 2.10.5 を含んでおり、お客様のAirflowバージョン `2.7.3` よりも新しいです。これは、新機能やバグ修正が含まれる一方で、Airflowのマイナーバージョンアップに伴うDAG互換性や動作変更の可能性を考慮する必要があります。

対処方法:
直ちの対応は不要ですが、現在の環境 (`composer-2.7.1-airflow-2.7.3`) は比較的古いバージョンであるため、セキュリティ、パフォーマンス、および機能の観点から、将来的なアップグレード計画を検討することを強く推奨します。
1.  **アップグレード計画の立案**: `composer-2.16.4-airflow-2.10.5` などの新しいバージョンへのアップグレード計画を立ててください。
2.  **DAGの互換性テスト**: アップグレード先のAirflowバージョン (`2.10.5` または `2.9.3`) において、既存のDAG (Directed Acyclic Graph) が問題なく動作するかどうかを、ステージング環境などで十分にテストしてください。特にカスタムプラグインやPythonパッケージを利用している場合は注意が必要です。
3.  **リリースノートの確認**: アップグレード対象バージョンのリリースノート (Cloud ComposerとAirflowの両方) を詳細に確認し、非互換性のある変更点や推奨される移行手順を把握してください。

用語説明:
*   **Cloud Composer イメージ**: Google Cloud Composer環境を構成する際に使用される仮想マシンイメージのことで、特定のCloud ComposerバージョンとApache Airflowバージョン、OS、必要なライブラリやツールが含まれています。
*   **DAG (Directed Acyclic Graph)**: Apache Airflowにおいて、データ処理パイプラインのタスクとその依存関係を定義するPythonスクリプトファイルのことです。

---

## Deprecated

原文:
```
 The following Cloud Composer versions and builds have reached their
end of support period:
composer-3-airflow-2.9.3-build.15 and composer-2.11.2-*.

[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support)
```
説明:
特定のCloud Composerバージョン、具体的には `composer-3-airflow-2.9.3-build.15` および `composer-2.11.2-*` の全ビルドがサポート終了期間に達しました。これは、これらのバージョンに対する公式サポート（セキュリティアップデート、バグ修正、技術サポートなど）が提供されなくなることを意味します。

影響有無:
**直接的な影響の可能性と間接的な影響あり。**
お客様の環境はCloud Composer 2 (Composer version 2.7.1)です。サポート終了対象の一つである `composer-2.11.2-*` は、お客様の現在のバージョン `2.7.1` よりも新しいバージョンです。このことから、お客様の `composer-2.7.1` も既にサポート終了している、あるいはサポート終了が非常に近い状態である可能性が極めて高いです。
サポート終了したバージョンを継続して使用することは、以下のようなリスクを伴います。
*   **セキュリティ脆弱性**: 既知のセキュリティ脆弱性が修正されないまま残る可能性があります。
*   **運用リスク**: 問題発生時にGoogle Cloudからの公式サポートやパッチが提供されません。
*   **機能の制限**: 最新のGoogle Cloudサービスや機能との連携が困難になる場合があります。

対処方法:
**緊急の対応が必要です。**
1.  **現状のサポート状況の確認**: Google Cloud Composerの公式ドキュメント（[Cloud Composer バージョン管理の概要](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support)）を参照し、お客様の `composer-2.7.1` の正確なサポート終了日を確認してください。
2.  **迅速なアップグレード計画**: 現在のバージョンがサポート終了している、または終了間近である場合、速やかにサポート対象の最新バージョン（例: 前述の `composer-2.16.4-airflow-2.10.5`）へのアップグレード計画を立案し、実行してください。
3.  **リスク評価**: アップグレードが完了するまでの間、サポート対象外の環境で運用し続けることによるセキュリティおよび運用上のリスクを評価し、必要に応じて一時的な緩和策を講じてください。

用語説明:
*   **サポート終了 (End of Support Period)**: プロダクトやサービスの特定のバージョンに対して、ベンダーからの公式な技術サポート、バグ修正、セキュリティパッチの提供が終了する期間のことです。この期間を過ぎたバージョンは、リスクを伴いながら運用することになります。
*   **バージョン管理**: ソフトウェアやサービスのライフサイクルにおいて、バージョン番号付け、新機能の追加、バグ修正、セキュリティアップデート、およびサポートポリシーを定義するプロセスです。