
# Title: April 03, 2026 
Link: https://docs.cloud.google.com/release-notes#April_03_2026<br>
Google Cloud インフラエンジニアの立場から、お問い合わせいただいたリリースノートについて影響調査を行いました。

---

# Cloud Logging

## Announcement

**原文:** Cloud Logging adds support for the `ca` multi-region. For a complete list of supported regions, see Supported regions.

[Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions)

**説明:** Google Cloud Loggingにおいて、ログバケットの保存先として新たに `ca` (カナダ) マルチリージョンがサポートされました。これにより、お客様はログデータをカナダ国内の複数の地理的に分散したリージョンに冗長的に保存することが可能になります。

**影響有無:**
*   **影響無し**：これは新しいデータ保存ロケーションの追加であり、既存のログバケット構成や動作に直接的な影響を与える変更ではありません。
*   **メリット**：カナダにおけるデータレジデンシー要件や規制遵守が必要な場合、またはカナダを主要なサービス対象地域とするワークロードにおいて、ログデータをより適切な地理的場所へ配置する選択肢が増えます。

**対処方法:**
*   現在の構成で特段の変更は不要です。
*   今後、新規にログバケットを作成する場合や、既存のログデータを新たな要件に基づいて再配置する場合に、`ca` マルチリージョンを検討対象とすることができます。

**用語説明:**
*   **マルチリージョン (Multi-region)**: Google Cloudのデータストレージにおいて、複数の物理的なリージョン（地域）にわたってデータがレプリケートされ、保存される構成を指します。これにより、単一リージョン障害に対する耐性が向上し、高可用性と低レイテンシを実現しつつ、特定の地理的エリア内でのデータレジデンシー要件を満たすことが可能になります。

---

# Identity and Access Management

## Deprecated

**原文:** Extended attributes for Workforce Identity Federation are deprecated. For group mapping, we recommend using SCIM instead of extended attributes. For more information, see IAM deprecations.

[SCIM](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim)
[IAM deprecations](https://docs.cloud.google.com/iam/docs/deprecations)

**説明:** Identity and Access Management (IAM) の機能である Workforce Identity Federation において、「拡張属性 (Extended attributes)」を利用したグループマッピングの機能が非推奨化されました。Google Cloudは、今後のグループマッピングにはSCIM (System for Cross-domain Identity Management) の利用を推奨しています。

**影響有無:**
*   **影響有り（利用中の場合）**：現在、Workforce Identity Federation で「拡張属性」を使用して外部IDプロバイダ (IdP) からのグループ情報をGoogle Cloudにマッピングしている場合、影響があります。この機能は将来的にサポートが終了する可能性があるため、SCIMベースのグループマッピングへの移行計画が必要です。
*   **影響無し（利用していない場合）**：Workforce Identity Federation を使用していない場合、または「拡張属性」を利用したグループマッピングを行っていない場合は、この変更による影響はありません。

**対処方法:**
1.  **現状確認**: まず、お客様のGoogle Cloud環境でWorkforce Identity Federation を利用しており、「拡張属性」によるグループマッピングが構成されているかを確認してください。
2.  **移行計画**: 「拡張属性」を使用している場合は、SCIMへの移行計画を立ててください。SCIMを利用することで、IDプロビジョニングとグループ同期をより標準的かつ効率的に行うことができます。
3.  **ドキュメント参照**: 移行の詳細や非推奨化に関する具体的なタイムラインは、[IAM deprecations](https://docs.cloud.com/iam/docs/deprecations) のドキュメントで確認し、計画に反映させてください。SCIMへの移行については、[SCIM](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim) のドキュメントを参照してください。

**用語説明:**
*   **Workforce Identity Federation**: Google Cloudが提供する機能で、従業員やパートナーなどの「ワークフォース」ユーザーが、Google Cloudの既存のIDプロバイダ（オンプレミスActive Directory、Okta、Azure ADなど）を通じてGoogle Cloudリソースにアクセスできるようにします。これにより、ID管理を一元化し、セキュリティと運用の効率性を向上させます。
*   **拡張属性 (Extended attributes)**: Workforce Identity Federation において、外部IDプロバイダからのユーザーの属性情報（例：所属グループ、役職など）をGoogle Cloudにマッピングするために使用される機能の一つでした。
*   **SCIM (System for Cross-domain Identity Management)**: 異なるID管理システム（IdPとサービスプロバイダなど）間でユーザーID情報を自動的にプロビジョニングし、同期するための業界標準プロトコルです。これにより、手動でのアカウント作成やグループ同期の手間を削減し、ID情報の一貫性と正確性を保つことができます。
# Title: April 02, 2026 
Link: https://docs.cloud.google.com/release-notes#April_02_2026<br>
ご担当者様

Google Cloudのリリースノートに関するお問い合わせ、ありがとうございます。
ご提供いただいたリリースノートに基づき、構築済みのGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響有無を調査いたしました。

---

# AlloyDB for PostgreSQL
## Change
原文: You can now enable Advanced Query Insights on primary clusters which have secondary clusters configured. Advanced Query Insights is not supported on secondary clusters. If you perform a switchover, you must re-enable Advanced Query Insights on the new primary cluster.
[Advanced Query Insights on primary clusters](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#secondary-cluster-instance)

説明：
AlloyDB for PostgreSQLにおいて、セカンダリクラスタが構成されているプライマリクラスタで「Advanced Query Insights」機能を有効にできるようになりました。この機能はセカンダリクラスタではサポートされません。スイッチオーバーを実行した場合は、新しいプライマリクラスタでAdvanced Query Insightsを再度有効にする必要があります。

影響有無：なし
理由：弊社のシステムではAlloyDB for PostgreSQLは利用しておりません。本変更はAlloyDBの新規機能に関するものであり、既存のワークロードに直接的な影響はありません。

対処方法：不要

用語説明：
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、PostgreSQLと互換性のあるフルマネージドなエンタープライズ向けリレーショナルデータベースサービスです。高性能と高可用性が特徴です。
*   **Advanced Query Insights**: AlloyDBのデータベースパフォーマンス監視ツールで、クエリの実行計画やパフォーマンスに関する詳細な洞察を提供します。
*   **プライマリクラスタ (Primary Cluster)**: データベースシステムにおける書き込み操作を処理するメインのクラスタです。
*   **セカンダリクラスタ (Secondary Cluster)**: プライマリクラスタの読み取りレプリカとして機能し、読み取り操作をオフロードしたり、災害復旧のフェイルオーバーターゲットとして使用されたりするクラスタです。

---

# Apigee X
## Breaking
原文: **Deployment disruption for Apigee Drupal Portal via Google Cloud Marketplace**
Google Cloud Deployment Manager was deprecated as of March 31, 2026. We are currently transitioning the Apigee Drupal Portal Marketplace solution to use Infrastructure Manager. During this transition period, some deployment and management functionalities are unavailable.

**Impact:**
- **New Deployments:** Starting April 1, 2026, attempting to deploy a new Apigee Drupal Portal instance using the "Deploy" button on the Google Cloud Marketplace will fail.
- **Existing Deployments:** Your underlying resources (such as VMs and Cloud SQL databases) are unaffected and will continue to run normally. However, you can no longer use Deployment Manager-based features to manage the deployment via the Marketplace UI or the `gcloud deployment-manager` tool.

**Workaround & Resolution:**
Any configuration changes or management tasks must be performed directly on the individual Google Cloud resources (Compute Engine, Cloud SQL, etc.) rather than through the Marketplace UI.
We are actively working to release the updated Infrastructure Manager-based solution.

説明：
Google Cloud Marketplaceを介してApigee Drupal Portalをデプロイする際に、機能停止が発生する可能性があります。Google Cloud Deployment Managerが2026年3月31日に非推奨となるため、現在Apigee Drupal Portal MarketplaceソリューションをInfrastructure Managerへ移行中です。この移行期間中、一部のデプロイおよび管理機能が利用できません。
影響として、2026年4月1日以降、Google Cloud Marketplaceの「Deploy」ボタンからの新規デプロイは失敗します。既存のデプロイにおいては、基盤となるリソース（VMやCloud SQLデータベースなど）は影響を受けず、引き続き正常に稼働しますが、Marketplace UIや`gcloud deployment-manager`ツールを介した管理機能は利用できなくなります。
回避策として、設定変更や管理タスクは、Marketplace UIを介さず、個別のGoogle Cloudリソース（Compute Engine、Cloud SQLなど）に対して直接実行する必要があります。

影響有無：なし
理由：弊社のシステムではApigee XおよびApigee Drupal Portalは利用しておりません。

対処方法：不要

用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームで、APIの設計、セキュリティ、デプロイ、監視、分析など、ライフサイクル全体を管理します。
*   **Google Cloud Marketplace**: Google Cloud上で利用可能なソフトウェアソリューションやサービスを検索、デプロイできるオンラインストアです。
*   **Google Cloud Deployment Manager**: Google Cloudリソースのデプロイと管理を自動化するためのインフラストラクチャ・アズ・コード（IaC）サービスです。テンプレートを使用してリソースを定義し、一貫性のあるデプロイを可能にします。
*   **Infrastructure Manager**: Google Cloudにおける新しいIaCサービスで、Deployment Managerの後継となる機能です。

---

# Cloud Service Mesh
## Announcement
原文: Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see Data plane extensibility with `EnvoyFilter`.
[Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility)
To troubleshoot any issue while configuring, see Resolving data plane extensibility issues.
[Resolving data plane extensibility issues](https://docs.cloud.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility)

説明：
マネージドCloud Service Mesh（`TRAFFIC_DIRECTOR`実装を使用）が、`EnvoyFilter` APIの限定的な実装をサポートするようになりました。これにより、データプレーンの拡張性が向上し、ローカルレートリミットなどの機能を`EnvoyFilter`を使用して実現できるようになります。

影響有無：なし
理由：弊社のGoogle Cloud Composer環境ではCloud Service Meshを直接使用しておりません。本アナウンスは新機能の追加であり、既存のシステムに直接的な影響はありません。

対処方法：不要

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するフルマネージドなサービスメッシュプラットフォームです。サービス間の通信を安全かつ効率的に管理し、トラフィック管理、セキュリティ、可観測性を提供します。
*   **TRAFFIC_DIRECTOR**: Google Cloud Service Meshのデータプレーン実装の一つで、Googleのグローバルインフラストラクチャを活用して、アプリケーションへのトラフィックルーティングと負荷分散を最適化します。
*   **EnvoyFilter API**: Envoyプロキシの動作をカスタムルールで拡張するためのKubernetesリソースです。Envoyのフィルタチェーンにカスタムロジックや機能を挿入するために使用されます。

---

# Google Kubernetes Engine
Google Cloud ComposerはGoogle Kubernetes Engine (GKE) 上で稼働するマネージドサービスであるため、GKEの変更はComposerの基盤に間接的な影響を与える可能性があります。Composer 2.7.1は特定のGKEバージョン範囲をサポートしており、GKEのバージョンアップグレードは通常、Google Cloudによって管理されます。

## Change
原文: GKE cluster versions have been updated. New versions available for upgrades and new clusters. The following versions are now available for new GKE clusters, and for manual control plane upgrades and node upgrades for existing clusters. For more information about versioning and upgrades, see GKE versioning and support and About GKE cluster upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明：
GKEクラスタのバージョンが更新され、新しいバージョンが新規クラスタの作成および既存クラスタのコントロールプレーンとノードの手動アップグレードで利用可能になりました。

影響有無：間接的な影響（ポジティブ）
理由：これは新しいGKEバージョンの提供開始をアナウンスするものであり、既存のComposer環境のGKEクラスタに直ちに自動アップグレードが適用されるわけではありません。Composerの基盤となるGKEはGoogle Cloudによって管理されており、Composerのサポートポリシーとアップグレードスケジュールに従って、将来的にこれらの新しいGKEバージョンにアップグレードされる可能性があります。この変更自体は、GKEの選択肢が増えたことを意味し、セキュリティや安定性の向上が期待できます。

対処方法：
ユーザーが直接GKEクラスタのバージョンアップグレードを行う必要はありません。Composerの自動アップグレードポリシーを把握し、Composerのバージョンアップグレード時にGKEのバージョンも更新されることを認識してください。今後のComposerのリリースノートやGKEのバージョン互換性マトリックスを定期的に確認し、必要に応じてAirflowのDAGsやカスタムプラグインが新しいGKE環境で問題なく動作するか互換性テストを実施することを推奨します。

## Security
原文: This release includes new GKE versions that use updated Container-Optimized OS images. These updated images are cumulative, incorporating security fixes from all Container-Optimized OS versions released since the previous GKE release. To identify the specific vulnerabilities that were resolved in each updated Container-Optimized OS image, see the **Security** release notes for that image. (GKE version table with COS versions and links)

説明：
このGKEリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらの更新されたイメージは累積的であり、前回のGKEリリース以降にリリースされたすべてのCOSバージョンからのセキュリティ修正が組み込まれています。これにより、基盤となるノードのセキュリティが強化されます。

影響有無：間接的な影響（ポジティブ）
理由：Composerの基盤となるGKEノードのOSイメージのセキュリティが強化されます。これにより、システムの全体的なセキュリティ体制が向上します。ユーザー側で直接行うべき対処は通常ありませんが、セキュリティアップデートが適用されることはシステム運用上望ましいことです。

対処方法：
ユーザーが直接行うべき対処はありません。Google CloudによるGKEノードのセキュリティアップデートは自動的に適用されるため、引き続きComposer環境が最新のセキュリティパッチで保護されます。

## Change (Stable, Regular, Rapid, Extended Channels)
原文: **Note**: Your clusters might not have these versions available. Rollouts are already in progress when we publish the release notes, and can take multiple days to complete across all Google Cloud zones.
- The following versions are now available in the Stable channel: (versions listed)
- The following versions are now available in the Regular channel: (versions listed)
- The following versions are now available in the Rapid channel: (versions listed)
- The following versions are now available: (versions listed for control plane)
- The following node versions are now available: (versions listed for nodes)
- The following versions are now available in the Extended channel: (versions listed)

説明：
GKEの各種リリースチャネル（Stable, Regular, Rapid, Extended）および一般的に、新たなGKEバージョン（コントロールプレーンおよびノードバージョン）が利用可能になりました。これらのバージョンは、リリースノート公開時点でロールアウトが進行中であり、全Google Cloudゾーンに展開されるまでに数日かかる場合があります。

影響有無：間接的な影響
理由：これは新しいGKEバージョンが各リリースチャネルで利用可能になったというアナウンスです。ComposerのGKEバージョンはGoogle Cloudによって管理されているため、弊社のComposer環境が自動アップグレードの対象となっている場合、将来的にこれらの新しいGKEバージョンに更新される可能性があります。現在利用中のComposer 2.7.1はGKE 1.30.xまでをサポートしていると考えられるため、1.31.x以降のGKEバージョンへのアップグレードは、Composer自体のメジャー/マイナーバージョンアップグレードに伴うことが多いです。

対処方法：
直ちにユーザー側で必要な対処はありません。Composerのバージョンアップグレード時に、基盤となるGKEバージョンも更新されることを考慮してください。新しいGKEバージョンへの更新が懸念される場合は、ComposerのGKEバージョン互換性に関する公式ドキュメントを定期的に確認し、今後のComposerアップグレード計画に影響がないかを評価することが推奨されます。

用語説明：
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するフルマネージドなKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Google Cloud Composer**: Apache AirflowをGoogle Cloud上で実行するためのフルマネージドサービスです。ワークフローのオーケストレーションに使用されます。
*   **Container-Optimized OS (COS)**: Googleが開発した、コンテナ実行に最適化された軽量なLinuxベースのオペレーティングシステムです。GKEノードのデフォルトOSとして使用されます。
*   **リリースチャネル (Release Channel)**: GKEクラスタがどのバージョンのGKEを受け取るかを制御する設定です。Rapid、Regular、Stable、Extendedなどがあり、それぞれ新しいバージョンの提供頻度と安定性のバランスが異なります。
    *   **Rapid Channel**: 最新機能と修正を最速で受け取るチャネルです。本番環境での利用には慎重な検討が必要です。
    *   **Regular Channel**: 新機能と安定性のバランスが取れたチャネルです。定期的なアップデートが提供されます。
    *   **Stable Channel**: 最も安定性が高く、長期間のサポートが提供されるチャネルです。新しい機能の導入は遅くなります。
    *   **Extended Channel**: 特定のKubernetesバージョンの長期サポートを提供するチャネルです。EOL（End of Life）が迫るバージョン向けです。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタの管理層を構成するコンポーネント群（APIサーバー、スケジューラ、コントローラマネージャーなど）を指します。
*   **ノード (Node)**: Kubernetesクラスタ内のワーカーマシン（VMまたは物理マシン）で、コンテナ化されたアプリケーション（Pod）を実行します。

---