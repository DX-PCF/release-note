
# Title: December 05, 2025 
Link: https://docs.cloud.google.com/release-notes#December_05_2025<br>
## Apigee X
### Announcement
原文: On December 5th, 2025, we released an updated version of Apigee.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.
説明: Apigeeの新しいバージョンが2025年12月5日にリリースされました。このリリースの展開は本日から開始され、全てのGoogle Cloudゾーンに適用が完了するまでに4営業日以上かかる場合があります。展開が完了するまで、インスタンスで新機能や修正が利用できない可能性があります。
影響有無: **影響あり（情報提供）**。新しいバージョンがリリースされたことを示す情報であり、直接的なサービス中断やユーザーアクションは不要ですが、機能や修正が環境に反映されるまで時間がかかる可能性があることを理解しておく必要があります。
対処方法: 特になし。Google Cloud側で自動的にロールアウトが進行します。
用語説明:
*   **ロールアウト (Rollout)**: ソフトウェアやシステムの新しいバージョンを、段階的かつ計画的にデプロイしていくプロセス。

### Security
原文: Bug ID: 388271708, Description: Security fix for Apigee infrastructure. This addresses the following vulnerability:- CVE-2025-13426 Fixed an issue with the JavaCallout policy that could result in remote code execution.
説明: Apigeeのインフラストラクチャにおけるセキュリティ修正が適用されました。これにより、JavaCalloutポリシーにおけるリモートコード実行（RCE）の脆弱性（CVE-2025-13426）が修正されました。
影響有無: **影響あり（セキュリティ改善）**。重大なセキュリティ脆弱性が修正されたため、既存のApigee環境のセキュリティが向上します。JavaCalloutポリシーを使用している場合は特に重要です。
対処方法: 自動的に修正が適用されるため、ユーザー側での具体的な対処は不要です。Apigeeのロールアウトが完了するのを待つことで、この修正が適用されます。
用語説明:
*   **JavaCallout policy**: Apigee APIプロキシ内でカスタムJavaコードを実行するためのポリシー。
*   **リモートコード実行 (Remote Code Execution, RCE)**: 攻撃者が遠隔から任意のコードをシステム上で実行できてしまう、深刻なセキュリティ脆弱性。
*   **CVE-2025-13426**: 共通脆弱性識別子（Common Vulnerabilities and Exposures）番号。特定のセキュリティ脆弱性を国際的に一意に識別するためのID。

## Google Kubernetes Engine
### Changed (Extended channel)
原文:
> **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- Version 1.33.5-gke.1308000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel: 1.28.15-gke.3202000, 1.29.15-gke.2520000, 1.30.14-gke.1760000, 1.31.13-gke.1139000, 1.31.13-gke.1454000, 1.32.9-gke.1239000, 1.32.9-gke.1548000, 1.33.5-gke.1791000, 1.34.1-gke.2909002, 1.34.1-gke.3084002
- The following versions are no longer available in the Extended channel: (多数の旧バージョンが列挙)
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
    - GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades: 1.27 to 1.28.15-gke.3096000, 1.28 to 1.29.15-gke.2380000, 1.29 to 1.30.14-gke.1658000
    - GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades: 1.28 to 1.28.15-gke.3096000, 1.29 to 1.29.15-gke.2380000, 1.30 to 1.30.14-gke.1658000, 1.31 to 1.31.13-gke.1139000, 1.32 to 1.32.9-gke.1239000, 1.33 to 1.33.5-gke.1308000, 1.34 to 1.34.1-gke.2909002
説明: ExtendedチャネルのGKEクラスタにおいて、デフォルトバージョンが`1.33.5-gke.1308000`に更新されました。複数の新しいGKEバージョンが利用可能になり、多数の古いバージョンが利用不可になりました。また、クラスタの自動アップグレードターゲットが更新され、特定のマイナーバージョンおよびパッチバージョンへのアップグレードパスが追加されました。
影響有無: **影響あり**。
    *   Google Cloud Composer 2 は通常GKE Autopilotクラスタを使用しており、GKEバージョンはGoogle Cloudによって自動的に管理・アップグレードされます。
    *   本リリースにより、Composer環境が稼働するGKEクラスタが新しいパッチまたはマイナーバージョンに自動アップグレードされる可能性があります。
    *   特に、マイナーバージョンアップグレード（例: 1.29から1.30へのアップグレード）の場合、Kubernetes APIの変更や非互換性により、デプロイ済みのAirflow DAGsやカスタムプラグインに影響が出る可能性があります。
    *   Composer 2.7.1 (Airflow 2.7.3) は現時点でGKE 1.27.x, 1.28.x, 1.29.x をサポートしています。このリリースに含まれる1.30以上のGKEバージョンへの自動アップグレードパスは、将来的なComposerのバージョンアップを検討するきっかけとなる可能性があります。
対処方法:
    1.  **メンテナンスウィンドウの確認と設定**: GKEの自動アップグレードが業務影響の少ない時間帯に行われるよう、Composer環境のGKEメンテナンスウィンドウを設定しているか確認してください。
    2.  **DAGの互換性確認**: GKEのマイナーバージョンアップグレード（例: 1.29から1.30など）が行われる可能性があるため、Airflow DAGs
# Title: December 04, 2025 
Link: https://docs.cloud.google.com/release-notes#December_04_2025<br>
はい、承知いたしました。Google Cloud のリリースノートに基づき、Cloud Service Meshの変更点について、影響調査と対処方法を専門的な観点から回答いたします。

---

# Cloud Service Mesh

## Announcement

**原文:**
Managed Cloud Service Mesh will start using proxy version
`csm_mesh_proxy.20251121c_RC00` for Gateway API on GKE clusters. This proxy
version maps closest to Envoy version 1.37. This change is rolling out to all
release channels and contains the fix for the managed Cloud Service Mesh
security vulnerability listed in [GCP-2025-073](/service-mesh/docs/security-bulletins#gcp-2025-073).

**説明:**
マネージドのCloud Service Meshにおいて、GKEクラスタ上でGateway APIを使用する際のプロキシバージョンが、`csm_mesh_proxy.20251121c_RC00` に更新されます。このプロキシバージョンは、オープンソースのEnvoyプロキシバージョン1.37に最も近いものとなります。この変更は、すべてのリリースチャネルに対して段階的に展開され、[GCP-2025-073](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073) に記載されている、マネージドCloud Service Meshのセキュリティ脆弱性に対する修正が含まれています。

**影響有無:**
*   **ポジティブな影響**: マネージドサービスとして、GCP-2025-073で開示されたセキュリティ脆弱性に対する修正が自動的に適用されるため、サービスのセキュリティ態勢が向上します。
*   **直接的なユーザーへの影響**: Managed Cloud Service MeshはGoogleによって運用されるため、お客様側での手動によるプロキシバージョンアップグレード作業は不要です。自動的にアップデートが適用されます。
*   **潜在的な間接的な影響**: プロキシ（Envoy）のバージョンアップに伴い、非常に稀ではありますが、既存のEnvoy設定やアプリケーションのトラフィックパターンによっては、互換性の問題や意図しない動作変更が発生する可能性はゼロではありません。しかし、一般的にGoogle Cloudのマネージドサービスは後方互換性を考慮して設計されています。

**対処方法:**
1.  **影響範囲の確認**: お客様のGKEクラスタにおいて、Cloud Service MeshをGateway APIと組み合わせて使用しているか確認してください。
2.  **モニタリングの強化**: プロキシバージョンアップグレードが適用された後、Gateway APIを介したサービス間のトラフィック、ルーティングポリシー、およびアプリケーションのパフォーマンスについて、いつもより注意深くモニタリングを実施してください。異常なトラフィックパターン、エラー率の増加、レイテンシの悪化などがないかを確認することが推奨されます。
3.  **セキュリティ情報の確認**: 修正される脆弱性の内容について、[GCP-2025-073](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073) の詳細を確認し、影響範囲と修正内容を理解しておくことをお勧めします。
4.  **ロールバックの考慮（非推奨）**: 基本的に自動適用されるため、ユーザー側でのロールバックは推奨されませんが、重大な問題が発生した場合は、Google Cloudサポートへの連絡を検討してください。

**用語説明:**
*   **Cloud Service Mesh**: Google Cloudが提供するマネージドなサービスメッシュソリューションです。Istioを基盤としており、GKEクラスタ内のサービス間のトラフィック管理、セキュリティ、可観測性を一元的に提供します。
*   **Gateway API**: KubernetesのネットワークAPIの一種で、Ingress APIの後継として設計されています。より柔軟で表現力豊かなトラフィックルーティング、ポリシー適用、ロードバランシングなどの機能を提供し、GKEを含むKubernetes環境での外部トラフィック管理を強化します。
*   **Envoy**: Cloud Service Meshのデータプレーンとして利用される、高性能なオープンソースのエッジ/サービスプロキシです。サービスメッシュにおいて、各サービスのサイドカープロキシとして動作し、トラフィックのルーティング、負荷分散、セキュリティポリシーの適用、メトリクス収集などを行います。
*   **Proxy version**: サービスメッシュを構成するEnvoyなどのプロキシソフトウェアのバージョンを指します。このバージョンが更新されることで、新機能の追加、パフォーマンスの改善、セキュリティ脆弱性の修正などが適用されます。
*   **Release channels (リリースチャネル)**: GKEクラスタのバージョン管理戦略です。Rapid, Regular, Stableなどのチャネルがあり、新しい機能や修正が段階的にユーザーに提供されます。これにより、安定性と最新機能のバランスを取ることができます。

---