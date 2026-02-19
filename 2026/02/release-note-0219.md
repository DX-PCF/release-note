
# Title: February 18, 2026 
Link: https://docs.cloud.google.com/release-notes#February_18_2026<br>
Google Cloudインフラエンジニアとして、リリースノートの各項目について影響調査を実施しました。

---

# Cloud SQL for PostgreSQL

## Deprecated

**原文:**
`Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the gcp.managed.allowedMCPServices constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM.`

[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

**説明:**
Google CloudにおけるMCP (Managed Control Plane) の利用を制御する組織ポリシーのうち、`gcp.managed.allowedMCPServices` 制約を用いた方法が非推奨となります。2026年3月17日以降、この組織ポリシーは機能しなくなり、MCPの利用制御にはIAM拒否ポリシー (`IAM deny policies`) を使用する必要があります。

**影響有無:**
**影響あり（将来的な対応が必要）**
現在、組織ポリシーの `gcp.managed.allowedMCPServices` 制約を使用してMCPの利用を制限している環境に影響があります。期日が2026年3月17日と設定されているため、直ちの運用影響はありませんが、期日までにIAM拒否ポリシーへの移行計画を立案・実行する必要があります。

**対処方法:**
1.  現在、お客様のGoogle Cloud組織で `gcp.managed.allowedMCPServices` 組織ポリシーが設定されているかを確認してください。
2.  もし設定されている場合は、2026年3月17日までに、IAM拒否ポリシーを利用したMCP利用制御への移行計画を策定・実施してください。
3.  詳細な移行手順については、提供された「Control MCP use with IAM」ドキュメントを参照してください。

**用語説明:**
*   **MCP (Managed Control Plane):** Google Cloudが提供するマネージドサービスのバックエンドで動作する制御プレーンです。サービスのプロビジョニング、スケーリング、管理を自動化するためにGoogleが内部的に利用するコンポーネントです。
*   **組織ポリシー (Organization Policy):** Google Cloud組織全体に適用される制約を定義し、リソースのデプロイや設定を管理者が統制するための機能です。
*   **IAM拒否ポリシー (IAM deny policies):** IAM (Identity and Access Management) の機能拡張で、特定のプリンシパル（ユーザー、サービスアカウントなど）が特定のリソースに対して特定のアクションを行うことを明示的に「拒否」するポリシーです。許可ポリシーよりも優先されます。

---

## Change

**原文:**
`After March 17, 2026, when you enable the Cloud SQL Admin API (sqladmin.googleapis.com), the Cloud SQL remote MCP server is enabled automatically. The Cloud SQL remote MCP server is in Preview.`

[Preview](https://cloud.google.com/products/#product-launch-stages)

**説明:**
2026年3月17日以降、Cloud SQL Admin API (`sqladmin.googleapis.com`) を有効化すると、Cloud SQLのリモートMCPサーバーが自動的に有効になるように変更されます。このリモートMCPサーバー機能は現在「プレビュー」段階です。

**影響有無:**
**影響なし（機能追加、ただしプレビュー段階）**
これはCloud SQL Admin API有効化時の動作に関する変更であり、既存のCloud SQLインスタンスの運用に直接的な影響はありません。リモートMCPサーバーの自動有効化は、Google Cloudのバックエンドインフラストラクチャに関する変更であり、通常はユーザーが意識する必要はありません。ただし、現在プレビュー段階の機能であるため、本番環境での利用については注意が必要です。

**対処方法:**
*   特に対処は不要です。この変更は、将来的にCloud SQLサービスを管理する際のバックエンド動作に関するものです。
*   「プレビュー」段階の機能であるため、この変更による追加機能や挙動について、今後GA (Generally Available) になった際の動向を注視してください。

**用語説明:**
*   **Cloud SQL Admin API:** プログラムやコマンドラインを通じてCloud SQLインスタンスの作成、構成、管理を行うためのAPI (Application Programming Interface) です。
*   **リモートMCPサーバー:** Cloud SQLのバックエンドで動作し、サービスの安定性や新機能の提供を支えるMCPの一機能と推測されます。ユーザーが直接操作するものではありません。
*   **プレビュー (Preview):** Google Cloud製品のライフサイクル段階の一つで、機能が開発中であり、将来的に変更される可能性があることを示します。本番環境での利用は推奨されない場合があります。

---

# Google Cloud Armor

## Change

**原文:**
`Cloud Armor preconfigured WAF rules support for inspection up to the first 64 kB (either 8 kB, 16 kB, 32 kB, 48 kB, or 64 kB) of the request body content is Generally Available.`

[preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules)
[request body content](https://docs.cloud.com/armor/docs/security-policy-overview#request-body)

**説明:**
Google Cloud Armorの事前構成済みWAF (Web Application Firewall) ルールにおいて、リクエストボディコンテンツの検査サイズが最大64KB（8KB、16KB、32KB、48KB、または64KBのいずれか）までサポートされる機能が、正式版（GA: Generally Available）として提供開始されました。

**影響有無:**
**影響なし（機能強化、ポジティブな影響の可能性）**
これは既存のCloud Armor機能の検査能力が向上し、GAになったというアナウンスです。既存のCloud Armorポリシーの動作に非互換な変更はありません。
*   **ポジティブな影響:** より大きなリクエストボディに含まれる可能性のある攻撃（例: ファイルアップロードによるマルウェア、大型のSQLインジェクションやXSSペイロードなど）に対して、事前構成済みWAFルールでより詳細な検査が可能になります。

**対処方法:**
*   特に対処は不要です。
*   もし、これまで大きなリクエストボディの検査が制限されていたためにカスタムルールなどで対応していた場合は、この機能を利用して事前構成済みWAFルールでの保護を強化することを検討できます。
*   Cloud Armorポリシーのチューニングを検討する際は、提供されたドキュメント「preconfigured WAF rules」および「request body content」を参照してください。

**用語説明:**
*   **Google Cloud Armor:** Google CloudのDDoS対策およびWAFサービスです。アプリケーションをDDoS攻撃やOWASP Top 10などの一般的なウェブ脆弱性から保護します。
*   **事前構成済みWAFルール (Preconfigured WAF rules):** Google Cloud Armorが提供する、OWASP ModSecurity Core Rule Set (CRS) に基づくなどの標準的なWAFルールセットです。ユーザーはこれらのルールを簡単に有効化して利用できます。
*   **リクエストボディ (Request body content):** HTTPリクエストの一部で、通常はPOSTやPUTメソッドで送信されるデータが含まれる部分です。Webアプリケーションへの入力データとして利用されます。
*   **GA (Generally Available):** Google Cloud製品のライフサイクル段階の一つで、機能が安定しており、本番環境での利用が推奨される状態です。

---

# Google Kubernetes Engine

## Security

**原文:**
`Multiple security vulnerabilities have been identified in the OpenSSL library. The most significant finding is CVE-2025-15467, a critical vulnerability that might allow for remote code execution (RCE) or denial of service (DoS) attacks via network-based vectors. For more information, see the GCP-2026-006 security bulletin.`

[GCP-2026-006 security bulletin](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2026-006-gke)

**説明:**
OpenSSLライブラリに複数のセキュリティ脆弱性が発見されました。特に重要なのは「クリティカル」と評価されているCVE-2025-15467で、ネットワーク経由でリモートコード実行 (RCE) やサービス拒否 (DoS) 攻撃を許す可能性があります。

**影響有無:**
**影響あり（セキュリティリスク、対応必須）**
Google Kubernetes Engine (GKE) が内部的に利用しているOpenSSLライブラリの脆弱性であり、GKEクラスターのセキュリティに直接的な影響を及ぼす可能性があります。「クリティカル」な脆弱性であるため、速やかな対応が推奨されます。

**対処方法:**
1.  提供されている「GCP-2026-006 security bulletin」を直ちに確認し、詳細な情報（影響範囲、修正バージョン、推奨されるアクションなど）を入手してください。
2.  通常、このようなGKEの基盤ライブラリに関する脆弱性は、GKEのコントロールプレーンおよびノードイメージのセキュリティパッチ適用によって修正されます。
3.  ご利用のGKEクラスターのバージョンが影響を受けるか確認し、必要に応じてGKEクラスターのアップグレード（特にノードプールの再作成を含む）を速やかに計画・実行してください。GKEの自動アップグレードが有効になっている場合でも、セキュリティ速報で推奨されるアクションを確認し、緊急性に応じて手動での介入を検討してください。

**用語説明:**
*   **OpenSSL:** SSL/TLSプロトコルの実装を提供するオープンソースの暗号化ライブラリです。多くのソフトウェアやシステムでセキュアな通信を実現するために広く利用されています。
*   **CVE (Common Vulnerabilities and Exposures):** 既知の公開されている情報セキュリティの脆弱性や露出を一意に識別するための国際的な標準識別子システムです。
*   **リモートコード実行 (RCE: Remote Code Execution):** 攻撃者がターゲットシステム上で任意のコードをリモートから実行できる脆弱性です。最も危険な脆弱性の一つとされています。
*   **サービス拒否 (DoS: Denial of Service):** 攻撃者が正当なユーザーがサービスやリソースを利用できないようにする攻撃です。システムやネットワークを過負荷にしたり、クラッシュさせたりすることで引き起こされます。
*   **セキュリティ速報 (Security bulletin):** ベンダー（この場合はGoogle Cloud）が製品のセキュリティ脆弱性について公開する公式通知です。脆弱性の詳細、影響、修正方法、推奨される対策などが記載されます。
# Title: February 17, 2026 
Link: https://docs.cloud.google.com/release-notes#February_17_2026<br>
以下に、Google Cloudのリリースノートを元に、構築済みのサービスへの影響有無を調査し、簡潔に回答します。

---

# AlloyDB for PostgreSQL

## Announcement

原文: New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see Best practices for securing agent interactions with Model Context Protocol.

[Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/alloydb/docs/ai/secure-agent-interactions-mcp)

説明：
AlloyDB for PostgreSQLにおいて、Model Context Protocol (MCP) を使用して生成AIエージェントとの安全なやり取りを行うための新しいベストプラクティスが公開されました。このガイダンスには、最小権限の原則、ネイティブデータベース制御、セキュアなエージェント設計といった主要なセキュリティ対策が含まれており、より安全なAIアプリケーション構築に役立つ情報が提供されています。

影響有無：
**影響なし**
これは既存のサービス構成や動作に直接的な変更を加えるものではなく、生成AIエージェントをAlloyDBと連携させる際のセキュリティ設計に関する新しいガイダンスの提供です。

対処方法：
なし。将来的に生成AIエージェントとAlloyDBの連携を検討する際に、本ベストプラクティスを参照し、セキュリティ設計に役立てることを推奨します。

用語説明：
*   **Model Context Protocol (MCP)**: 生成AIエージェントがGoogle Cloudサービスと安全にやり取りを行うためのプロトコルです。
*   **生成AIエージェント (Generative AI Agents)**: 生成AIモデルを活用し、特定のタスクを実行したり、ユーザーと対話したりするソフトウェアエージェントを指します。

---

# BigQuery

## Deprecated

原文: Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM deny policies.

[Control MCP use with IAM deny policies](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

説明：
BigQueryにおけるModel Context Protocol (MCP) の利用を制御するための組織ポリシー（`gcp.managed.allowedMCPServices` 制約）が非推奨になります。2026年3月17日以降、この組織ポリシーは機能しなくなり、MCPの利用制御はIAM拒否ポリシーに移行する必要があります。

影響有無：
**影響あり（Breaking Changeの可能性）**
現在、`gcp.managed.allowedMCPServices` 組織ポリシー制約を使用してMCPの利用を制御している場合、2026年3月17日以降は当該ポリシーが機能しなくなるため、サービスへの影響が発生する可能性があります。MCPの利用を厳密に制御する必要がある環境では、IAM拒否ポリシーへの移行が必須となります。

対処方法：
`gcp.managed.allowedMCPServices` 組織ポリシー制約を利用してBigQueryにおけるMCP利用を制御している場合、2026年3月17日までにIAM拒否ポリシーへの移行計画を策定し、実行してください。移行手順については、提供されたリンク先のドキュメント「Control MCP use with IAM deny policies」を参照してください。

用語説明：
*   **組織ポリシー (Organization Policies)**: Google Cloudリソースの構成と動作を組織全体で制御するためのルールセットです。特定のAPI、サービス、またはリソースの挙動を制限するために使用されます。
*   **`gcp.managed.allowedMCPServices` 制約**: 特定のGoogle CloudサービスにおけるModel Context Protocol (MCP) の利用を許可するかどうかを制御するための組織ポリシー制約です。
*   **IAM拒否ポリシー (IAM Deny Policies)**: Identity and Access Management (IAM) の機能の一つで、特定のアクションを明示的に禁止することができます。許可ポリシーよりも優先され、アクセスを確実に拒否するために使用されます。

## Change

原文: After March 17, 2026, when you enable BigQuery, the BigQuery MCP server is automatically enabled.

説明：
2026年3月17日以降、BigQueryを有効にする際に、BigQuery Model Context Protocol (MCP) サーバーが自動的に有効になるように変更されます。

影響有無：
**影響なし（将来的な動作変更）**
既存のBigQueryプロジェクトがこの変更によって直ちに影響を受けることはありません。しかし、2026年3月17日以降に新規でBigQueryを有効化する場合や、何らかの理由でBigQueryの再有効化が必要になった場合に、MCPサーバーが意図せず自動で有効化される可能性があります。もしMCPサーバーの自動有効化を避けたい場合は、上記のIAM拒否ポリシーでの制御を検討する必要があります。

対処方法：
直ちに対処は不要です。2026年3月17日以降にBigQueryの新規有効化や再有効化を行う際、MCPサーバーの自動有効化が組織のセキュリティポリシーと競合しないか確認してください。必要に応じて、IAM拒否ポリシーによるMCP利用の明示的な制御を検討してください。

---

# Cloud SQL for PostgreSQL

## Announcement

原文: New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see Best practices for securing agent interactions with Model Context Protocol.

[Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/sql/docs/postgres/secure-agent-interactions-mcp)

説明：
Cloud SQL for PostgreSQLにおいて、Model Context Protocol (MCP) を使用して生成AIエージェントとの安全なやり取りを行うための新しいベストプラクティスが公開されました。このガイダンスには、最小権限の原則、ネイティブデータベース制御、セキュアなエージェント設計といった主要なセキュリティ対策が含まれており、より安全なAIアプリケーション構築に役立つ情報が提供されています。

影響有無：
**影響なし**
これは既存のサービス構成や動作に直接的な変更を加えるものではなく、生成AIエージェントをCloud SQL for PostgreSQLと連携させる際のセキュリティ設計に関する新しいガイダンスの提供です。

対処方法：
なし。将来的に生成AIエージェントとCloud SQL for PostgreSQLの連携を検討する際に、本ベストプラクティスを参照し、セキュリティ設計に役立てることを推奨します。

---

# Compute Engine

## Change

原文: After March 17, 2026, when you enable Compute Engine, the Compute Engine MCP server is automatically enabled.

説明：
2026年3月17日以降、Compute Engineを有効にする際に、Compute Engine Model Context Protocol (MCP) サーバーが自動的に有効になるように変更されます。

影響有無：
**影響なし（将来的な動作変更）**
既存のCompute Engineプロジェクトがこの変更によって直ちに影響を受けることはありません。しかし、2026年3月17日以降に新規でCompute Engineを有効化する場合や、何らかの理由でCompute Engineの再有効化が必要になった場合に、MCPサーバーが意図せず自動で有効化される可能性があります。

対処方法：
直ちに対処は不要です。2026年3月17日以降にCompute Engineの新規有効化や再有効化を行う際、MCPサーバーの自動有効化が組織のセキュリティポリシーと競合しないか確認してください。必要に応じて、IAM拒否ポリシーによるMCP利用の明示的な制御を検討してください。

## Deprecated

原文: Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM.

[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

説明：
Compute EngineにおけるModel Context Protocol (MCP) の利用を制御するための組織ポリシー（`gcp.managed.allowedMCPServices` 制約）が非推奨になります。2026年3月17日以降、この組織ポリシーは機能しなくなり、MCPの利用制御はIAM拒否ポリシーに移行する必要があります。

影響有無：
**影響あり（Breaking Changeの可能性）**
現在、`gcp.managed.allowedMCPServices` 組織ポリシー制約を使用してMCPの利用を制御している場合、2026年3月17日以降は当該ポリシーが機能しなくなるため、サービスへの影響が発生する可能性があります。MCPの利用を厳密に制御する必要がある環境では、IAM拒否ポリシーへの移行が必須となります。

対処方法：
`gcp.managed.allowedMCPServices` 組織ポリシー制約を利用してCompute EngineにおけるMCP利用を制御している場合、2026年3月17日までにIAM拒否ポリシーへの移行計画を策定し、実行してください。移行手順については、提供されたリンク先のドキュメント「Control MCP use with IAM」を参照してください。

---

# Firestore

## Announcement

原文: New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see Best practices for securing agent interactions with Model Context Protocol.

[Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/firestore/native/docs/secure-agent-interactions-mcp)

説明：
Firestoreにおいて、Model Context Protocol (MCP) を使用して生成AIエージェントとの安全なやり取りを行うための新しいベストプラクティスが公開されました。このガイダンスには、最小権限の原則、ネイティブデータベース制御、セキュアなエージェント設計といった主要なセキュリティ対策が含まれており、より安全なAIアプリケーション構築に役立つ情報が提供されています。

影響有無：
**影響なし**
これは既存のサービス構成や動作に直接的な変更を加えるものではなく、生成AIエージェントをFirestoreと連携させる際のセキュリティ設計に関する新しいガイダンスの提供です。

対処方法：
なし。将来的に生成AIエージェントとFirestoreの連携を検討する際に、本ベストプラクティスを参照し、セキュリティ設計に役立てることを推奨します。

## Deprecated

原文: Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM.

[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

説明：
FirestoreにおけるModel Context Protocol (MCP) の利用を制御するための組織ポリシー（`gcp.managed.allowedMCPServices` 制約）が非推奨になります。2026年3月17日以降、この組織ポリシーは機能しなくなり、MCPの利用制御はIAM拒否ポリシーに移行する必要があります。

影響有無：
**影響あり（Breaking Changeの可能性）**
現在、`gcp.managed.allowedMCPServices` 組織ポリシー制約を使用してMCPの利用を制御している場合、2026年3月17日以降は当該ポリシーが機能しなくなるため、サービスへの影響が発生する可能性があります。MCPの利用を厳密に制御する必要がある環境では、IAM拒否ポリシーへの移行が必須となります。

対処方法：
`gcp.managed.allowedMCPServices` 組織ポリシー制約を利用してFirestoreにおけるMCP利用を制御している場合、2026年3月17日までにIAM拒否ポリシーへの移行計画を策定し、実行してください。移行手順については、提供されたリンク先のドキュメント「Control MCP use with IAM」を参照してください。

## Change

原文: After March 17, 2026, when you enable Firestore, the Firestore MCP server is automatically enabled.

説明：
2026年3月17日以降、Firestoreを有効にする際に、Firestore Model Context Protocol (MCP) サーバーが自動的に有効になるように変更されます。

影響有無：
**影響なし（将来的な動作変更）**
既存のFirestoreプロジェクトがこの変更によって直ちに影響を受けることはありません。しかし、2026年3月17日以降に新規でFirestoreを有効化する場合や、何らかの理由でFirestoreの再有効化が必要になった場合に、MCPサーバーが意図せず自動で有効化される可能性があります。

対処方法：
直ちに対処は不要です。2026年3月17日以降にFirestoreの新規有効化や再有効化を行う際、MCPサーバーの自動有効化が組織のセキュリティポリシーと競合しないか確認してください。必要に応じて、IAM拒否ポリシーによるMCP利用の明示的な制御を検討してください。

---

# Google Kubernetes Engine

## Deprecated

原文: Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see Control MCP use with IAM.

[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

説明：
Google Kubernetes Engine (GKE) におけるModel Context Protocol (MCP) の利用を制御するための組織ポリシー（`gcp.managed.allowedMCPServices` 制約）が非推奨になります。2026年3月17日以降、この組織ポリシーは機能しなくなり、MCPの利用制御はIAM拒否ポリシーに移行する必要があります。

影響有無：
**影響あり（Breaking Changeの可能性）**
現在、`gcp.managed.allowedMCPServices` 組織ポリシー制約を使用してMCPの利用を制御している場合、2026年3月17日以降は当該ポリシーが機能しなくなるため、サービスへの影響が発生する可能性があります。MCPの利用を厳密に制御する必要がある環境では、IAM拒否ポリシーへの移行が必須となります。

対処方法：
`gcp.managed.allowedMCPServices` 組織ポリシー制約を利用してGKEにおけるMCP利用を制御している場合、2026年3月17日までにIAM拒否ポリシーへの移行計画を策定し、実行してください。移行手順については、提供されたリンク先のドキュメント「Control MCP use with IAM」を参照してください。

## Change

原文: After March 17, 2026, when you enable GKE, the GKE MCP server is automatically enabled.

説明：
2026年3月17日以降、Google Kubernetes Engine (GKE) を有効にする際に、GKE Model Context Protocol (MCP) サーバーが自動的に有効になるように変更されます。

影響有無：
**影響なし（将来的な動作変更）**
既存のGKEクラスタがこの変更によって直ちに影響を受けることはありません。しかし、2026年3月17日以降に新規でGKEを有効化する場合や、何らかの理由でGKEの再有効化が必要になった場合に、MCPサーバーが意図せず自動で有効化される可能性があります。

対処方法：
直ちに対処は不要です。2026年3月17日以降にGKEの新規有効化や再有効化を行う際、MCPサーバーの自動有効化が組織のセキュリティポリシーと競合しないか確認してください。必要に応じて、IAM拒否ポリシーによるMCP利用の明示的な制御を検討してください。

---

# Spanner

## Announcement

原文: New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see Best practices for securing agent interactions with Model Context Protocol. This feature is in Preview.

[Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/spanner/docs/secure-agent-interactions-mcp)

説明：
Spannerにおいて、Model Context Protocol (MCP) を使用して生成AIエージェントとの安全なやり取りを行うための新しいベストプラクティスが公開されました。このガイダンスには、最小権限の原則、ネイティブデータベース制御、セキュアなエージェント設計といった主要なセキュリティ対策が含まれており、より安全なAIアプリケーション構築に役立つ情報が提供されています。なお、この機能はプレビュー段階です。

影響有無：
**影響なし**
これは既存のサービス構成や動作に直接的な変更を加えるものではなく、生成AIエージェントをSpannerと連携させる際のセキュリティ設計に関する新しいガイダンスの提供です。プレビュー機能であるため、本番環境での利用は推奨されません。

対処方法：
なし。将来的に生成AIエージェントとSpannerの連携を検討する際に、本ベストプラクティスを参照し、セキュリティ設計に役立てることを推奨します。プレビュー機能であるため、正式リリース前の本番環境への導入は避けてください。

---
# Title: February 16, 2026 
Link: https://docs.cloud.google.com/release-notes#February_16_2026<br>
Google Cloudのリリースノート調査結果をご報告いたします。

---

# Cloud Composer

## Change
原文: New Airflow builds are available in Cloud Composer 3:
[Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
- composer-3-airflow-3.1.0-build.9
- composer-3-airflow-2.10.5-build.26 (default)
- composer-3-airflow-2.9.3-build.46

[composer-3-airflow-3.1.0-build.9](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-0-build-9)
[composer-3-airflow-2.10.5-build.26](https://cloud.google.com/composer/docs/versions-packages#composer-2-10-5)
[composer-3-airflow-2.9.3-build.46](https://cloud.google.com/composer/docs/versions-packages#composer-2-9-3)

説明：Cloud Composer 3環境向けに、新しいAirflowビルドイメージ（Airflow 3.1.0、2.10.5、2.9.3）が利用可能になったことが発表されました。特に`composer-3-airflow-2.10.5-build.26`がデフォルトとして設定されています。

影響有無：**影響なし**
理由：現在ご利用の環境はCloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3)であるため、Cloud Composer 3向けのアナウンスは直接的な影響を与えません。

対処方法：不要です。将来的にCloud Composer 3への移行を検討する際に、これらの新しいビルドオプションが選択肢となります。

用語説明：
*   **Airflow build**: Apache Airflowの特定バージョンと、Google Cloud Composerが提供する基盤インフラ（OS、Pythonパッケージなど）を組み合わせた、あらかじめ構築されたイメージのこと。Cloud Composer環境を作成または更新する際に選択できます。

---

## Change
原文: New images are available in Cloud Composer 2:
[images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
- composer-2.16.4-airflow-2.10.5 (default)
- composer-2.16.4-airflow-2.9.3

[composer-2.16.4-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-16-4-airflow-2-10-5)
[composer-2.16.4-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-16-4-airflow-2-9-3)

説明：Cloud Composer 2環境向けに、新しいイメージ（`composer-2.16.4-airflow-2.10.5` および `composer-2.16.4-airflow-2.9.3`）が利用可能になったことが発表されました。`composer-2.16.4-airflow-2.10.5`がデフォルトのイメージとなります。

影響有無：**間接的な影響あり**
理由：現在ご利用の環境はCloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3)であり、リリースされた新しいイメージバージョン（Composer 2.16.4）は、現在の環境よりも新しいバージョンです。このアナウンスにより、新しい機能の利用、パフォーマンスの向上、セキュリティパッチの適用などの恩恵を受けるためのアップグレードパスが提供されました。既存の環境が自動的に変更されることはありませんが、中長期的な運用計画においてアップグレードの検討が必要となります。Airflowのバージョンも2.7.3から2.10.5へ更新されるため、DAGの互換性確認が重要です。

対処方法：
1.  **即時対応は不要です。** 現在のComposer環境が停止したり、機能が損なわれることはありません。
2.  **アップグレード計画の検討：** 新しいイメージへのアップグレードを検討してください。アップグレードにより、Airflowの最新機能、パフォーマンス改善、セキュリティ強化の恩恵を受けられます。
3.  **互換性検証の実施：** アップグレードに際しては、Airflowのバージョンが2.7.3から2.10.5（または2.9.3）に上がるため、既存のDAGやカスタムプラグインが新しいAirflowバージョンと互換性があるか、十分な検証を計画してください。特に、非推奨になった機能や変更されたAPIがないかを確認が必要です。
4.  **Google Cloud公式ドキュメントの参照：** アップグレード手順、注意点、Airflowの変更点については、Google CloudのComposerドキュメントおよびApache Airflowのリリースノートを詳細に確認してください。

用語説明：
*   **Composer Image**: Cloud Composer環境の基盤となるOS、Apache Airflowのバージョン、関連するPythonパッケージなどが一式含まれたテンプレートのようなものです。これを選択して環境を作成または更新します。
*   **DAG (Directed Acyclic Graph)**: Apache Airflowにおいてワークフローを定義するPythonスクリプトのこと。タスクとその実行順序、依存関係を表現します。

---

## Deprecated
原文: The following Cloud Composer versions and builds have reached their end of support period: composer-3-airflow-2.9.3-build.15 and composer-2.11.2-*.

[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support)

説明：以下のCloud Composerのバージョンとビルドがサポート終了期間に達したことが発表されました。
*   `composer-3-airflow-2.9.3-build.15`
*   `composer-2.11.2-*` (Cloud Composer 2.11.2の全てのビルド)

影響有無：**影響なし**
理由：現在ご利用の環境はCloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3)であり、サポート終了対象リストに含まれていません。

対処方法：現在の環境に対して直接的な対処は不要です。しかし、Cloud Composerのバージョンにはライフサイクルがあり、現在ご利用の2.7.1バージョンも将来的にサポート終了となる可能性があるため、定期的なバージョンアップ計画の重要性を再認識してください。

用語説明：
*   **サポート終了 (End of Support)**: 特定のソフトウェアバージョンや製品が、開発元からの技術サポート、セキュリティアップデート、バグ修正の提供を終了する期間を指します。サポートが終了したバージョンを使い続けると、セキュリティリスクや不具合が発生しても対応が困難になる可能性があります。
*   **Composer version**: Cloud Composerサービス自体が持つバージョン体系。これはApache Airflowのバージョンとは別に、Google Cloudが提供する管理機能やインフラストラクチャのバージョンを示します。