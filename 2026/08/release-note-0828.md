
# Title: August 27, 2026 
Link: https://docs.cloud.google.com/release-notes#August_27_2026<br>
Google Cloud のリリースノートに基づき、各製品への影響調査と対処方法を以下にまとめます。

---

# Cloud SQL for PostgreSQL

## Change
**原文:** The rollout of the following extension upgrades is complete:
- `pg_partman` is upgraded from 5.2.4 to 5.4.3.
- `pgfincore` is upgraded from 1.3.1 to 1.4.
- `pgvector` is upgraded from 0.8.1 to 0.8.5.
For more information, see Configure PostgreSQL extensions.

**説明:** Cloud SQL for PostgreSQLで利用可能な3つの拡張機能（`pg_partman`, `pgfincore`, `pgvector`）が新しいバージョンにアップグレードされました。これらのアップグレードの展開が完了したことを示しています。

**影響有無:**
*   **影響あり:** Cloud SQL for PostgreSQLインスタンスでこれらの拡張機能を既に利用している場合、拡張機能のバージョンが自動的にアップグレードされる可能性があります。これにより、新機能の利用、パフォーマンスの改善、または稀に互換性に関する変更が発生する可能性があります。特に`pg_partman`や`pgvector`はデータ操作やクエリの挙動に影響を与える可能性があるため、影響を評価する必要があります。
*   **影響なし:** これらの拡張機能を利用していない場合、直接的な影響はありません。

**対処方法:**
1.  **利用状況の確認:** まず、現在利用しているCloud SQL for PostgreSQLインスタンスで、`pg_partman`, `pgfincore`, `pgvector`のいずれかの拡張機能が有効になっているかを確認します。
2.  **テスト環境での検証:** これらの拡張機能を利用している場合は、本番環境に適用される前に、アップグレードされたバージョンでの動作に問題がないか、既存のワークロードやアプリケーションで影響がないかをステージング環境やテスト環境で十分に検証することを推奨します。
3.  **ドキュメントの確認:** 各拡張機能の新しいバージョンでの変更点（非互換な変更や新機能など）について、公式ドキュメントやリリースノートを参照し、必要に応じてアプリケーション側の調整を検討します。特に`pg_partman`はパーティション管理、`pgvector`はベクトル検索の挙動に影響を与える可能性があります。

**用語説明:**
*   **拡張機能 (Extension):** PostgreSQLの機能を拡張するためのモジュール。特定の機能やデータ型を追加したり、パフォーマンスを改善したりするために利用されます。
*   **`pg_partman`:** PostgreSQLのテーブルパーティション管理を自動化し、簡素化するための拡張機能。大量のデータを扱うテーブルのパフォーマンスと管理性を向上させます。
*   **`pgfincore`:** PostgreSQLがOSのファイルシステムキャッシュの状態を調査したり、明示的にデータをキャッシュにロードしたりする機能を提供する拡張機能。I/Oパフォーマンスの最適化に役立ちます。
*   **`pgvector`:** PostgreSQLでベクトル埋め込みデータ（Vector Embeddings）を効率的に保存し、ベクトル類似性検索（Vector Similarity Search）を実行するための拡張機能。AI/機械学習アプリケーション、特に大規模言語モデル（LLM）との連携で頻繁に利用されます。

---

# Cloud Service Mesh

## Security
**原文:** The following images are now rolling out for managed Cloud Service Mesh:
- 1.21.6-asm.71 is rolling out to the rapid release channel.
- 1.20.8-asm.119 is rolling out to the regular release channel.
- 1.19.10-asm.109 is rolling out to the stable release channel.
These versions resolve the security vulnerabilities listed in Security Bulletin GCP-2026-057.

**説明:** マネージドCloud Service Mesh (ASM) の各リリースチャネル（rapid, regular, stable）向けに、セキュリティ修正を含む新しいバージョンのイメージが展開されています。これらのバージョンは、セキュリティ速報GCP-2026-057で公開されたセキュリティ脆弱性に対処します。

**影響有無:**
*   **影響あり（ポジティブ）:** マネージドCloud Service Meshを利用している場合、基盤となるコンポーネント（Istioコントロールプレーンなど）が自動的にアップデートされ、報告されているセキュリティ脆弱性が修正されます。これにより、サービスメッシュのセキュリティ体制が強化されます。
*   **影響なし（運用面）:** マネージドサービスであるため、ユーザー側で明示的なアップグレード操作は不要であり、運用上の直接的な影響はほとんどありません。

**対処方法:**
1.  **ユーザー側の操作不要:** マネージドCloud Service MeshはGoogleによって管理・アップデートされるため、ユーザー側で特に必要な操作はありません。
2.  **セキュリティ速報の確認:** 参照されているセキュリティ速報「GCP-2026-057」の内容を確認し、修正された脆弱性が自身のワークロードに与える潜在的な影響を理解しておくことを推奨します。
3.  **監視の継続:** アップデートが適用される際、既存のアプリケーションに予期せぬ影響がないか、サービスメッシュのメトリクスやログを継続的に監視することを推奨します。万一問題が発生した場合は、Google Cloudサポートに連絡してください。

**用語説明:**
*   **Cloud Service Mesh (ASM):** Google Cloudが提供するフルマネージドなサービスメッシュソリューション。オープンソースのIstioをベースにしており、マイクロサービス間のトラフィック管理、セキュリティ（mTLSなど）、オブザーバビリティ（トレース、メトリクス）を強化します。
*   **マネージドCloud Service Mesh:** ユーザーがIstioコントロールプレーンの管理（デプロイ、アップグレード、スケーリング）をGoogleに任せ、データプレーン（Envoyプロキシ）のみを管理するデプロイモデル。運用負担が軽減されます。
*   **リリースチャネル (Release Channel):** Google Cloudのプロダクト（GKEやCloud Service Meshなど）で、バージョンの更新頻度と安定性を選択するメカニズム。`rapid`（最新機能、頻繁な更新）、`regular`（バランス型）、`stable`（最も安定性重視）などがあります。
*   **セキュリティ脆弱性 (Security Vulnerability):** ソフトウェアやシステムに存在する、悪意のある第三者によって悪用される可能性のある欠陥や弱点。
*   **セキュリティ速報 (Security Bulletin):** Google Cloudが公開する、特定のセキュリティ脆弱性とその修正に関する公式通知。重要なセキュリティ情報が記載されています。

---
# Title: August 26, 2026 
Link: https://docs.cloud.google.com/release-notes#August_26_2026<br>
Google Cloud リリースノートに関する影響調査結果を報告いたします。

---

# BigQuery
## Security
原文: An Improper Input Validation vulnerability was discovered in the JDBC driver in BigQuery Data Transfer Service versions prior to May 1, 2026. An authenticated attacker could use crafted JDBC connection string parameters to achieve remote code execution in the connector container and escalate privileges in the tenant project. For more information, see the GCP-2026-056 security bulletin.
説明：BigQuery Data Transfer ServiceのJDBCドライバーに、入力検証の不備による脆弱性(Improper Input Validation)が発見されました。この脆弱性は、2026年5月1日以前のバージョンに存在します。認証された攻撃者が不正に細工されたJDBC接続文字列パラメータを使用することで、コネクタコンテナ内でリモートコード実行（RCE）を達成し、テナントプロジェクト内で権限昇格が可能となる可能性があります。詳細については、セキュリティ速報[GCP-2026-056](https://docs.cloud.google.com/bigquery/docs/security-bulletins#gcp-2026-056)を参照してください。
影響有無：**影響あり**。BigQuery Data Transfer ServiceのJDBCドライバーを利用している場合、本脆弱性の影響を受けます。特に、外部のデータソースへの接続にJDBCドライバーを使用している場合に、リモートコード実行および権限昇格のリスクがあります。
対処方法：BigQuery Data Transfer ServiceのJDBCドライバーを最新バージョンに更新してください。定期的にセキュリティ速報[GCP-2026-056](https://docs.cloud.google.com/bigquery/docs/security-bulletins#gcp-2026-056)を確認し、推奨される対応を速やかに実施してください。
用語説明：
*   **JDBCドライバー (Java Database Connectivity Driver)**: Javaアプリケーションからデータベースに接続するためのAPIを実装したソフトウェアコンポーネント。
*   **BigQuery Data Transfer Service**: Google SaaSアプリケーションや外部クラウドストレージからBigQueryへのデータ転送を自動化するサービス。
*   **Improper Input Validation**: プログラムがユーザーからの入力を適切に検証しないために発生するセキュリティ脆弱性の一種。
*   **リモートコード実行 (Remote Code Execution, RCE)**: 攻撃者が標的のシステム上で任意のコードをリモートで実行できる脆弱性。
*   **権限昇格 (Privilege Escalation)**: 攻撃者が低い権限から高い権限（例: 一般ユーザーから管理者）を獲得すること。

---

# Cloud Logging
## Change
原文: VM Extension Manager extension policies for the Ops Agent are Generally Available (GA). Extension policies provide zonal and project-wide Ops Agent installation, version upgrades, and configuration management. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).
説明：Ops AgentのVM Extension Manager拡張ポリシーがGA（一般提供）になりました。この機能により、ゾーンおよびプロジェクト全体でOps Agentのインストール、バージョンアップグレード、および構成管理をVM Extension Managerを通じて行うことが可能になります。詳細については、[VM Extension Managerポリシーを使用したOps Agentのインストールと管理](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies)に関するドキュメントを参照してください。
影響有無：**影響なし**。既存のOps Agentの管理方法（例: 手動インストール、スクリプトなど）には直接的な影響はありません。この変更は、Ops Agentのデプロイと管理に利用できる新しい公式ツールが追加されたことを意味します。
対処方法：Ops Agentのデプロイや管理を効率化したい場合、または新しい方法への移行を検討する場合は、VM Extension Managerの利用を評価してください。
用語説明：
*   **Ops Agent**: Google Cloud上のVMインスタンスからログとメトリクスを収集するためのエージェント。Cloud LoggingとCloud Monitoringにデータを送信する。
*   **VM Extension Manager (VMEM)**: Compute Engine VMインスタンス上でエージェントやソフトウェアをインストール・管理するためのGoogle Cloudのサービス。
*   **GA (Generally Available)**: Google Cloudのプロダクトライフサイクルにおける最終段階で、一般利用可能であることを示す。安定しており、本番環境での使用が推奨される。

---

# Cloud Monitoring
## Change
原文: VM Extension Manager extension policies for the Ops Agent are Generally Available (GA). Extension policies provide zonal and project-wide Ops Agent installation, version upgrades, and configuration management. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).
説明：Ops AgentのVM Extension Manager拡張ポリシーがGA（一般提供）になりました。この機能により、ゾーンおよびプロジェクト全体でOps Agentのインストール、バージョンアップグレード、および構成管理をVM Extension Managerを通じて行うことが可能になります。詳細については、[VM Extension Managerポリシーを使用したOps Agentのインストールと管理](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies)に関するドキュメントを参照してください。
影響有無：**影響なし**。既存のOps Agentの管理方法（例: 手動インストール、スクリプトなど）には直接的な影響はありません。この変更は、Ops Agentのデプロイと管理に利用できる新しい公式ツールが追加されたことを意味します。
対処方法：Ops Agentのデプロイや管理を効率化したい場合、または新しい方法への移行を検討する場合は、VM Extension Managerの利用を評価してください。
用語説明：
*   **Ops Agent**: Google Cloud上のVMインスタンスからログとメトリクスを収集するためのエージェント。Cloud LoggingとCloud Monitoringにデータを送信する。
*   **VM Extension Manager (VMEM)**: Compute Engine VMインスタンス上でエージェントやソフトウェアをインストール・管理するためのGoogle Cloudのサービス。
*   **GA (Generally Available)**: Google Cloudのプロダクトライフサイクルにおける最終段階で、一般利用可能であることを示す。安定しており、本番環境での使用が推奨される。

---

# Cloud Service Mesh
## Announcement / Fixed
原文:
**1.29.7-asm.2 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.29.7-asm.2 uses Envoy v1.35.14. This release resolves the security vulnerabilities listed in Security Bulletin [GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).
Patch 1.29.7-asm.2 contains the fix for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| [CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5) |

**1.28.10-asm.24 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.10-asm.24 uses Envoy v1.36.10. This release resolves the security vulnerabilities listed in Security Bulletin [GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).
Patch 1.28.10-asm.24 contains the fix for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| [CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5) |

**1.27.9-asm.34 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.34 uses Envoy v1.35.14. This release resolves the security vulnerabilities listed in Security Bulletin [GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).
Patch 1.27.9-asm.34 contains fixes for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| [CVE-2026-10536](https://ubuntu.com/security/CVE-2026-10536) | Yes | Yes | No | Yes | Low (9.8) |
| [CVE-2026-42151](https://ubuntu.com/security/CVE-2026-42151) | No | No | No | Yes | High (7.5) |
| [CVE-2026-42154](https://ubuntu.com/security/CVE-2026-42154) | No | No | No | Yes | High (7.5) |
| [CVE-2026-40179](https://ubuntu.com/security/CVE-2026-40179) | No | No | No | Yes | Medium (6.1) |
| [CVE-2026-44903](https://ubuntu.com/security/CVE-2026-44903) | No | No | No | Yes | Medium (6.1) |
| [CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5) |

説明：クラスタ内Cloud Service Meshの複数の新しいバージョン（1.29.7-asm.2、1.28.10-asm.24、1.27.9-asm.34）がリリースされました。これらのリリースには、セキュリティ速報[GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057)に記載されているセキュリティ脆弱性に対する修正が含まれています。各バージョンは特定のEnvoyバージョンを使用しており、CVE-2026-5704などのプラットフォームCVEが修正されています。特にバージョン1.27.9-asm.34では複数のCVE（High severityを含む）が修正されています。
影響有無：**影響あり**。Cloud Service Meshを利用している場合、これらのアップデートはセキュリティ強化のため重要です。特に、脆弱性が修正される前のバージョンを使用している場合は、高リスクの脆弱性を含むため、早急なアップグレードを推奨します。
対処方法：
*   現在利用しているCloud Service Meshのバージョンを確認し、該当するバージョンまたはそれ以降のバージョンへのアップグレードを計画してください。
*   アップグレード手順については、公式ドキュメント「[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)」を参照してください。
*   アップグレード前にテスト環境で影響を確認し、計画的に実施してください。
*   セキュリティ速報[GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057)の詳細を確認し、修正された脆弱性の内容を理解してください。
用語説明：
*   **Cloud Service Mesh (Anthos Service Mesh)**: サービスメッシュを導入・管理するためのGoogle Cloudのマネージドサービス。Istioをベースとしている。
*   **Envoy**: クラウドネイティブアプリケーション向けに設計された高性能なオープンソースのエッジ/サービスプロキシ。Cloud Service Meshのデータプレーンとして使用される。
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されているソフトウェアのセキュリティ脆弱性および暴露のリストで、それぞれに識別番号が付与されている。

---

# Google Kubernetes Engine
## Change
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).
（以下、各リリースチャネルにおける詳細なバージョン情報が続く）
説明：GKEクラスタの利用可能なバージョンが更新されました。新しいGKEクラスタの作成、既存クラスタのコントロールプレーンおよびノードの手動アップグレードに、新しいバージョンが利用可能になります。また、各リリースチャネル（Stable, Regular, Rapid, Extendedなど）においても、デフォルトバージョン、利用可能なバージョンが更新され、一部の古いバージョンが非推奨または削除されました。GKEの自動アップグレードターゲットも、これらの新しいバージョンに設定されます。
影響有無：**影響あり**。現在GKEクラスタを運用している場合、以下の影響が考えられます。
*   **自動アップグレード**: GKEが管理する自動アップグレードを利用しているクラスタは、新しいターゲットバージョンに自動的にアップグレードされる可能性があります（メンテナンス期間や除外設定、API非推奨などの影響がない場合）。
*   **手動アップグレード**: 手動でアップグレードを計画している場合、利用可能なバージョンが増えたり、利用できなくなるバージョンがあるため、計画を見直す必要があります。
*   **新規クラスタ作成**: 新規クラスタ作成時のデフォルトバージョンが変更されるため、意図しないバージョンで作成される可能性があります。
*   **Google Cloud Composer 2との関連**: Google Cloud Composer 2 (Compoer version 2.7.1、Airflow version 2.7.3) はGKEクラスタ上で動作するため、GKEのバージョン更新はComposerの安定性や機能に影響を与える可能性があります。特に、ComposerがサポートするGKEバージョン範囲から外れるようなGKEのアップグレードはComposerの動作に問題を引き起こす可能性があるため注意が必要です。
対処方法：
*   現在運用しているGKEクラスタのリリースチャネルとバージョンを確認してください。
*   GKEのバージョン管理ポリシーとサポート期間（[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)）を確認し、非推奨またはサポート終了間近のバージョンを使用していないか確認してください。
*   自動アップグレード設定を確認し、意図しないタイミングでのアップグレードを防ぐために[メンテナンスウィンドウや除外設定](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)を適切に設定してください。
*   新しいGKEバージョンへのアップグレードを計画する際は、アプリケーションの互換性テストを十分に行ってください。
*   **Google Cloud Composer 2を利用している場合**: Composerの[リリースノートやドキュメント](https://cloud.google.com/composer/docs/release-notes)で、サポートされるGKEバージョンを確認し、ComposerのバージョンアップグレードとGKEのバージョンアップグレードの計画を同期させてください。通常、Composerのアップグレードプロセスで基盤となるGKEバージョンも更新されますが、自動アップグレードが予期せぬ挙動をしないか監視が必要です。
用語説明：
*   **GKE (Google Kubernetes Engine)**: Kubernetesクラスタをデプロイ、管理するためのマネージドサービス。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタの管理層。APIサーバー、スケジューラ、コントローラマネージャなどが含まれる。
*   **ノード (Node)**: Kubernetesクラスタのワーカーマシン。Podが実行される場所。
*   **リリースチャネル (Release Channel)**: GKEクラスタのバージョン更新頻度と安定性レベルを選択するオプション（Rapid, Regular, Stable, Extendedなど）。
*   **自動アップグレード (Auto-upgrade)**: GKEがクラスタのコントロールプレーンやノードを自動的に最新のパッチバージョンやマイナーバージョンにアップグレードする機能。
*   **メンテナンスウィンドウ/除外設定 (Maintenance Windows/Exclusions)**: GKEの自動アップグレードが実行される期間を指定したり、特定の期間アップグレードを禁止したりする設定。
*   **非推奨 (Deprecated)**: 将来的にサポートが終了する予定の機能やバージョン。

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image.
説明：今回のGKEリリースには、更新されたContainer-Optimized OS（COS）イメージを使用する新しいGKEバージョンが含まれています。これらのCOSイメージには、前回のGKEリリース以降に公開されたすべてのCOSバージョンからのセキュリティ修正が累積的に適用されています。各COSイメージで解決された特定の脆弱性については、個別のCOSリリースノートのリンクを参照してください。
影響有無：**影響あり**。GKEクラスタのノードイメージにセキュリティ修正が適用されます。これは、GKEクラスタのセキュリティ体制を強化するために重要です。脆弱性が修正される前のCOSイメージを使用しているノードが存在する場合、セキュリティリスクが軽減されます。Google Cloud Composer 2のAirflowワーカーやスケジューラが動作するGKEノードのOSイメージが更新されることを意味し、基盤となるOSレベルのセキュリティが向上します。
対処方法：GKEクラスタのノードが最新のセキュリティパッチが適用されたCOSイメージを使用するように、ノードの自動アップグレードを有効にしておくことを推奨します。手動アップグレードの場合は、計画的にノードのバージョンアップグレードを実施してください。COSイメージの具体的なセキュリティ修正内容に興味がある場合は、記載されているCOSリリースノートのリンクを確認してください。
用語説明：
*   **Container-Optimized OS (COS)**: コンテナの
# Title: August 25, 2026 
Link: https://docs.cloud.google.com/release-notes#August_25_2026<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、構築済みのサービスへの影響有無を調査し、簡潔に回答いたします。

---

# Cloud SDK

## Breaking

原文: (情報なし)

説明：
Cloud SDKに関するBreaking Changeがアナウンスされていますが、詳細な情報が提供されていません。通常、"Breaking Change"は、既存の動作やAPIの仕様が変更され、下位互換性が失われる可能性のある変更を指します。これにより、既存のスクリプト、自動化ツール、またはアプリケーションが正しく動作しなくなる可能性があります。

影響有無：
**不明。** リリースノートに具体的な変更内容が記載されていないため、現在の構成や利用状況への影響を判断することはできません。ただし、Cloud SDKを利用しているすべてのユーザーは、このアナウンスに注意を払う必要があります。

対処方法：
現時点では具体的な対処方法は示されていませんが、以下の対応を推奨します。
*   Google Cloudの公式リリースノートやCloud SDKのドキュメント、GitHubリポジトリなどを定期的に確認し、このBreaking Changeに関する詳細情報が公開されるのを待ってください。
*   Cloud SDKを利用している環境（CI/CDパイプライン、開発環境、スクリプトなど）において、将来的なアップデートの際に互換性テストを実施する計画を立ててください。

用語説明：
*   **Breaking Change:** ソフトウェアやAPIの変更において、以前のバージョンとの下位互換性が失われ、既存のコードや設定が動作しなくなる可能性のある変更を指します。これらの変更は通常、新しい機能の導入や設計の見直し、セキュリティ強化などのために行われますが、ユーザー側での対応（コードの修正、設定の更新など）が必要となります。
*   **Cloud SDK:** Google Cloud Platform のサービスと対話するためのコマンドラインツール（`gcloud` CLI）、クライアントライブラリ、およびローカル開発ツールセットの集合体です。

---

# Google Kubernetes Engine

## Fixed

原文:
Fixed the issue in which GPUDirect-TCPX for `a3-highgpu-8g` machine types was
incompatible with the Linux kernel version that was used by Container-Optimized
OS in GKE version 1.34 and later. To prevent errors, GKE blocked creating or
upgrading node pools that used the `a3-highgpu-8g` machine type to version 1.34
or later. For more information about this issue, see GKE known
issues.

You can now create or upgrade node pools that use the `a3-highgpu-8g` machine
type to any of the following GKE versions. **Automatic upgrades of these node
pools from version 1.33 to version 1.34 or later are no longer blocked.**

- For minor version 1.34, use patch version 1.34.5-gke.1153000 or later.
- For minor version 1.35, use patch version 1.35.2-gke.1485000 or later.
- For minor version 1.36 and later, use any available patch version.

In GKE version 1.34 and later, you must use version 3.1.9 or later of the
GPUDirect-TCPX installer and version 2.0.12 or later of the GPUDirect-TCPX
sidecar. If you previously installed these components, verify that the container
images use these versions or later. **To avoid degraded performance or workload
failures, update your installer and sidecar image versions before the
`a3-highgpu-8g` node pools are manually or automatically upgraded to version
1.34 or later.** These container image versions correspond to the upstream
definitions maintained in the gpudirect-tcpx GitHub
repository.

説明：
このリリースノートは、Google Kubernetes Engine (GKE) における `a3-highgpu-8g` マシンタイプと GPUDirect-TCPX の互換性問題が修正されたことをアナウンスしています。以前は、GKE バージョン 1.34 以降で使用される Container-Optimized OS (COS) のLinuxカーネルバージョンと GPUDirect-TCPX との間に互換性の問題があり、`a3-highgpu-8g` マシンタイプを使用するノードプールを 1.34 以降のGKEバージョンに作成またはアップグレードすることがブロックされていました。

今回の修正により、以下のGKEパッチバージョン以降であれば、`a3-highgpu-8g` を使用するノードプールの作成およびアップグレードが可能になりました。
*   GKE 1.34: パッチバージョン 1.34.5-gke.1153000 以降
*   GKE 1.35: パッチバージョン 1.35.2-gke.1485000 以降
*   GKE 1.36 以降: 利用可能な任意のパッチバージョン

また、バージョン 1.33 から 1.34 以降へのノードプールの自動アップグレードもブロックされなくなりました。

**重要な注意点として、GKE 1.34 以降では、GPUDirect-TCPX インストーラーはバージョン 3.1.9 以降、GPUDirect-TCPX サイドカーはバージョン 2.0.12 以降を使用する必要がある**とされています。パフォーマンスの低下やワークロードの障害を避けるため、ノードプールが GKE 1.34 以降に手動または自動でアップグレードされる前に、これらのコンポーネントのコンテナイメージバージョンを更新することが強く推奨されています。

影響有無：
**影響あり（特定の構成の場合）。**
*   **`a3-highgpu-8g` マシンタイプを現在使用していない場合:** 影響はありません。
*   **`a3-highgpu-8g` マシンタイプを使用しており、かつGKEバージョンが1.33以前の場合:**
    *   これまではGKE 1.34以降へのアップグレードがブロックされていましたが、今回の修正によりアップグレードが可能になります。
    *   ただし、アップグレード前にGPUDirect-TCPXのインストーラーとサイドカーのバージョン要件（3.1.9+ / 2.0.12+）を満たす必要があります。
*   **`a3-highgpu-8g` マシンタイプを使用しており、かつGKEバージョンが1.34以降であるものの、GPUDirect-TCPXを利用していない場合:**
    *   直接的な影響はありませんが、将来的にGPUDirect-TCPXを利用する際にはバージョン要件に注意が必要です。
*   **`a3-highgpu-8g` マシンタイプを使用しており、かつGKEバージョンが1.34以降でGPUDirect-TCPXを利用している場合:**
    *   既にGKE 1.34以降に移行している環境では、今回の修正により安定性が向上する可能性があります。
    *   しかし、使用しているGPUDirect-TCPXのインストーラーとサイドカーのバージョンが指定されたバージョンより古い場合は、パフォーマンス低下やワークロード障害のリスクがあるため、早急な更新が必要です。

対処方法：
1.  **GKEクラスタが `a3-highgpu-8g` マシンタイプを使用しているか確認します。**
2.  **`a3-highgpu-8g` を使用している場合、現在のGKEバージョンを確認します。**
3.  **GKEバージョンが 1.34 未満の場合:**
    *   GKE 1.34 以降へのアップグレードを計画している場合、ノードプールがアップグレードされる前に、使用しているGPUDirect-TCPXインストーラーおよびサイドカーのコンテナイメージバージョンが、それぞれ 3.1.9 以降と 2.0.12 以降であることを確認し、必要に応じて更新してください。
    *   これにより、アップグレードブロックが解除され、またアップグレード後のパフォーマンス問題を防ぐことができます。
4.  **GKEバージョンが 1.34 以降の場合:**
    *   GPUDirect-TCPXインストーラーおよびサイドカーを利用している場合は、それらのコンテナイメージバージョンが 3.1.9 以降と 2.0.12 以降であることを確認してください。
    *   古いバージョンを使用している場合は、パフォーマンス低下やワークロード障害を避けるため、直ちにこれらのコンポーネントを更新してください。
    *   更新方法については、公式のgpudirect-tcpx GitHub repository ([https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/gpudirect-tcpx](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/gpudirect-tcpx)) を参照してください。

用語説明：
*   **`a3-highgpu-8g` マシンタイプ:** Google Cloudで提供されるVMインスタンスのタイプで、NVIDIA H100 GPUを8基搭載しており、特に高性能なAI/MLワークロードやHPC（高性能計算）向けに設計されています。
*   **GPUDirect-TCPX:** NVIDIA GPUDirectテクノロジーの一部で、GPUメモリとネットワークインターフェースカード (NIC) の間でCPUを介さずに直接データを転送することで、GPU間のデータ転送におけるレイテンシを削減し、スループットを向上させる技術です。特に分散型のGPUワークロードで性能を向上させます。
*   **Container-Optimized OS (COS):** Google が最適化およびセキュリティ強化を行った、コンテナの実行に特化したオペレーティングシステムです。GKEノードのデフォルトOSとして利用されます。
*   **GKEノードプール:** GKEクラスタ内で、同じ設定を持つノード（VMインスタンス）のグループを指します。ノードプールは、異なるマシンタイプ、GPU、ディスク、またはOSイメージを持つことができます。
*   **サイドカー (Sidecar Container):** Kubernetesのコンテナパターンの一つで、メインのアプリケーションコンテナの機能を補助するために同じPod内で実行される追加のコンテナを指します。このリリースノートでは、GPUDirect-TCPXの機能を提供する補助的なコンテナを指しています。