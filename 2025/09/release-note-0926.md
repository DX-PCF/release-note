
# Title: September 25, 2025 
Link: https://cloud.google.com/release-notes#September_25_2025<br>
# Cloud Service Mesh
## 非推奨 (Deprecated)

**原文**:
Support for the following features will end on **March 17, 2027**:

- GKE on AWS
- GKE on Azure
- EKS Attached Clusters on AWS
- Azure Attached Clusters with AKS

[GKE on AWS](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
[GKE on Azure](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
Note that there are no changes to the other features of GKE attached clusters or Google Distributed Cloud (software only or air-gapped).

You must migrate to an alternative service mesh solution or an alternative Istio-based solution using your existing CSM configuration files by March 17, 2027.

**説明**:
Cloud Service Mesh (CSM) において、以下の環境に対するサポートが **2027年3月17日** をもって終了します。

*   GKE on AWS
*   GKE on Azure
*   AWS 上の EKS Attached Clusters
*   AKS を利用した Azure Attached Clusters

GKE attached clustersのその他の機能や、Google Distributed Cloud (ソフトウェアのみまたはエアギャップ環境) の機能には変更はありません。

対象の環境でCloud Service Meshを利用している場合、2027年3月17日までに、代替のサービスメッシュソリューション、または既存のCSM設定ファイルを用いた代替のIstioベースソリューションへの移行を完了する必要があります。

**影響有無**:
現在、GKE on AWS、GKE on Azure、EKS Attached Clusters on AWS、またはAzure Attached Clusters with AKS上でCloud Service Meshをご利用の場合、本アナウンスは重大な影響を及ぼします。
これらの環境を使用していない場合、直接的な影響はありません。
影響の理由は、指定されたマルチクラウド/ハイブリッドクラウド環境におけるCloud Service Meshのサポートが、期日をもって終了するためです。

**対処方法**:
1.  **環境の確認**: 現在利用中のKubernetesクラスターが、GKE on AWS、GKE on Azure、EKS Attached Clusters on AWS、またはAzure Attached Clusters with AKSのいずれかであるかを確認してください。
2.  **移行計画の策定**: 対象環境でCloud Service Meshを利用している場合、2027年3月17日までに代替のサービスメッシュソリューション、または既存のCSM設定ファイルを利用したIstioベースのソリューションへの移行を計画・実行する必要があります。
3.  **関連する非推奨への対応**: GKE on AWS および GKE on Azure 自体も非推奨となり、Google Distributed Cloud Virtual (GDCV) などの他のGoogle Cloudのハイブリッド/マルチクラウドソリューションへの移行が推奨されています。サービスメッシュの移行計画と併せて、基盤となるKubernetes環境の移行計画も検討し、統合的なアプローチを取ることを強く推奨します。
4.  **ドキュメントの参照**: 移行戦略の策定にあたっては、[GKE on AWSの非推奨に関するドキュメント](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) および [GKE on Azureの非推奨に関するドキュメント](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) を参照し、詳細なガイダンスを確認してください。

**用語説明**:
*   **Cloud Service Mesh (CSM)**: Google Cloudが提供するフルマネージドなサービスメッシュソリューションです。オープンソースのIstioをベースにしており、マイクロサービスの可視化、トラフィック管理、セキュリティポリシーの適用、認証・認可などを統合的に行います。
*   **GKE on AWS / GKE on Azure**: Google Kubernetes Engine (GKE) の機能拡張であり、Google CloudコンソールからAWSまたはAzure上にKubernetesクラスターをデプロイ・管理できるようにするサービスです。
*   **Attached Clusters (EKS Attached Clusters on AWS, Azure Attached Clusters with AKS)**: 既存のAmazon Elastic Kubernetes Service (EKS) クラスターやAzure Kubernetes Service (AKS) クラスターをGoogle Cloudに登録し、GKEから管理・監視できるようにする機能です。これにより、Google Cloudの管理プレーンを通じてマルチクラウド環境のKubernetesクラスターを一元的に操作できます。
*   **サービスメッシュ (Service Mesh)**: マイクロサービスアーキテクチャにおいて、サービス間の通信を管理・制御するためのインフラストラクチャ層です。サービスディスカバリ、負荷分散、認証、認可、オブザーバビリティ (可観測性) などの機能を提供し、アプリケーションロジックからこれらの非機能要件を分離します。
*   **Istio**: Google、IBM、Lyftによって開発されたオープンソースのサービスメッシュプラットフォームです。Kubernetesを基盤として、上記のサービスメッシュ機能を提供します。
# Title: September 24, 2025 
Link: https://cloud.google.com/release-notes#September_24_2025<br>
# Identity and Access Management

## Changed
原文: Notification emails for grant activation or denial no longer include approver details.
To view the approver details, navigate to the **IAM & Admin > Privileged Access Manager > Grants** page on the Google Cloud Console.

説明: 特権アクセスの要求（grant activation）が承認または拒否（denial）された際に送付される通知メールから、承認者の詳細情報が含まれなくなりました。承認者の詳細情報を確認する必要がある場合は、Google Cloud Consoleの「IAM と管理」>「Privileged Access Manager」>「Grants」ページに移動して確認してください。

影響有無: 影響あり (限定的)
理由:
Privileged Access Manager (PAM) を利用し、特権アクセスの承認・拒否プロセスにおいて、承認者の詳細を通知メールで確認する運用を行っている場合に影響します。メールから承認者情報が削除されるため、運用フローによっては変更が必要となる可能性があります。ただし、情報はGoogle Cloud Consoleから引き続き確認可能です。

対処方法:
*   特権アクセス要求の承認者情報をメール通知のみで確認している運用がある場合、その運用フローを見直し、Google Cloud Consoleで確認する手順に切り替える必要があります。
*   関係者に対して、承認者情報の確認方法が変更された旨を周知してください。

用語説明:
*   **Identity and Access Management (IAM)**: Google Cloud のリソースに対するアクセス権限を管理するサービスです。誰がどのリソースにどのような操作を許可されるかを定義します。
*   **Privileged Access Manager (PAM)**: Google Cloud での機密性の高いリソースへの特権アクセスを管理、監査、自動化するためのサービスです。一時的かつ時間制限付きのアクセス付与を可能にし、最小権限の原則を強化します。
*   **Grant activation or denial**: PAMにおいて、特定の役割や権限の一時的な付与要求が承認された（activation）か、または拒否された（denial）かを示す状態です。
*   **Approver details**: 特権アクセス要求を承認または拒否したユーザーに関する詳細情報（例: ユーザー名、メールアドレス）です。
# Title: September 23, 2025 
Link: https://cloud.google.com/release-notes#September_23_2025<br>
# Cloud Service Mesh
## Announcement
原文: **1.27.1-asm.2 is now available for in-cluster Cloud Service Mesh.**

 You can now download 1.27.1-asm.2 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.27.1 subject to the list of supported features.

[Istio 1.27.1](https://istio.io/latest/news/releases/1.27.x/announcing-1.27/)
[supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster)
 The following environment variables and annotations are not supported:

- `ENVOY_STATUS_PORT_ENABLE_PROXY_PROTOCOL`
- `PILOT_DNS_CARES_UDP_MAX_QUERIES`
- `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX` and `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX`
- `sidecar.istio.io/bootstrapOverride`

 For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.27.1-asm.2 uses Envoy v 1.35.3-dev.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：
Cloud Service Mesh の新しいバージョン 1.27.1-asm.2 が、インクラスタデプロイメント向けに利用可能になりました。このバージョンは、Istio 1.27.1 の機能を含みますが、特定のサポート機能リストに従います。特に、以下の環境変数とアノテーションはサポートされません: `ENVOY_STATUS_PORT_ENABLE_PROXY_PROTOCOL`、`PILOT_DNS_CARES_UDP_MAX_QUERIES`、`PILOT_IP_AUTOALLOCATE_IPV4_PREFIX`、`PILOT_IP_AUTOALLOCATE_IPV6_PREFIX`、および `sidecar.istio.io/bootstrapOverride`。このCloud Service Meshバージョン 1.27.1-asm.2 は Envoy v1.35.3-dev を使用しています。アップグレードに関する詳細については、提供されているドキュメントを参照してください。

影響有無：
なし。これは新しいバージョンの提供アナウンスであり、既存のCloud Service Mesh環境に自動的に適用される変更ではありません。既存の環境がこのバージョン（1.27.1-asm.2）にまだアップグレードされていない場合、直接的な影響はありません。ただし、将来的にこのバージョンへのアップグレードを計画する場合、または現在すでにこのバージョンを使用している場合は影響があります。特に、上記で挙げられた非サポートの環境変数やアノテーションを既存の構成で使用している場合、アップグレード後にそれらの機能が利用できなくなるか、動作が変更される可能性があります。

対処方法：
現在のCloud Service Meshのバージョンを確認し、もしこのバージョン（1.27.1-asm.2）より古い場合は、直ちに対処する必要はありません。
このバージョンへのアップグレードを計画している場合は、事前に以下の点を評価してください。
1.  [Istio 1.27.1](https://istio.io/latest/news/releases/1.27.x/announcing-1.27/) のリリースノートおよび [Cloud Service Meshのサポートされる機能](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster) ドキュメントを確認し、含まれる新機能や変更点を把握してください。
2.  既存のCloud Service Mesh構成（Pod、Deployment、Serviceなどのマニフェスト）において、リリースノートにリストアップされている非サポートの環境変数やアノテーション（`ENVOY_STATUS_PORT_ENABLE_PROXY_PROTOCOL`, `PILOT_DNS_CARES_UDP_MAX_QUERIES`, `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX`, `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX`, `sidecar.istio.io/bootstrapOverride`）が使用されていないかを確認してください。
3.  もし非サポート項目を使用している場合は、それらの設定を削除するか、代替手段を検討する必要があります。
4.  アップグレード手順については、[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade) ドキュメントを参照し、本番環境に適用する前に十分なテスト環境での検証を実施してください。

用語説明：
*   **Cloud Service Mesh:** Google Cloud が提供する、Istioベースのマネージドなサービスメッシュプラットフォームです。マイクロサービス間のトラフィック管理、セキュリティ、可観測性を実現します。
*   **Istio:** マイクロサービスを接続、監視、保護するためのオープンソースのサービスメッシュプラットフォームです。サービス間の通信を透過的に制御します。
*   **In-cluster Cloud Service Mesh:** Cloud Service Meshのデプロイモードの一つで、Istioのコントロールプレーン（Pilot, Citadelなど）がユーザーのGoogle Kubernetes Engine (GKE) クラスタ内にデプロイされる形式です。
*   **Envoy:** Istioのデータプレーンとして広く利用されている高性能なオープンソースのエッジ/サービスプロキシです。サービス間のすべてのネットワークトラフィックをインターセプトし、ルーティング、負荷分散、認証などを処理します。
*   **環境変数 (Environment Variables) / アノテーション (Annotations):** KubernetesおよびIstioリソースの設定をカスタマイズするための一般的なメカニズムです。環境変数はコンテナのプロセスに直接影響を与え、アノテーションはリソースに追加の非構造化メタデータを提供します。
*   **PILOT_DNS_CARES_UDP_MAX_QUERIES:** Istioの`pilot`コンポーネントにおけるDNS解決に関する設定項目で、UDPでの最大クエリ数を制御する可能性があります。
*   **PILOT_IP_AUTOALLOCATE_IPV4_PREFIX / PILOT_IP_AUTOALLOCATE_IPV6_PREFIX:** `pilot`コンポーネントがIPアドレスを自動的に割り当てる際のIPv4またはIPv6のプレフィックスに関する設定項目です。
*   **sidecar.istio.io/bootstrapOverride:** Istioサイドカープロキシのブートストラップ設定を、カスタム設定で上書きするためのPodアノテーションです。これにより、デフォルトのEnvoyプロキシ設定を詳細に調整できます。
# Title: September 22, 2025 
Link: https://cloud.google.com/release-notes#September_22_2025<br>
# BigQuery
## Changed
原文:
[3.38.0](https://github.com/googleapis/python-bigquery/compare/v3.37.0...v3.38.0)
- Add additional query stats (#2270) (7b1b718)

説明：
`google-cloud-bigquery` Python クライアントライブラリのバージョン 3.38.0 がリリースされました。このバージョンでは、BigQuery のクエリ実行に関する追加の統計情報が利用可能になりました。

影響有無：
軽微な機能追加であり、既存の BigQuery ワークロードや Python コードに直接的な影響はありません。後方互換性のある変更です。

対処方法：
なし。新しいクエリ統計情報を利用したい場合は、`google-cloud-bigquery` ライブラリをこのバージョン以降に更新することを検討してください。

用語説明：
*   **クエリ統計情報 (Query Stats)**: BigQuery がクエリを実行した際に収集する、実行時間、処理されたバイト数、スロット使用量、ステップごとの詳細情報などのデータ。これにより、クエリのパフォーマンスボトルネックの特定や最適化が可能になります。

---

# Cloud Logging
## Announcement
原文:
Cloud Logging has removed the quota for write requests per minute, which has been replaced by volume-based regional quotas. We've also removed the references to August dates for the removal of the old quota from the public documentation. For more information, see Logging API quotas and limits.

[Logging API quotas and limits](https://cloud.google.com/logging/quotas#api-limits)

説明：
Cloud Logging のログ書き込みに関するクォータが変更されました。これまでの「1分あたりの書き込みリクエスト数」の上限が廃止され、「ボリュームベースのリージョン別クォータ」に置き換えられました。また、古いクォータ廃止に関するドキュメント内の、過ぎた日付（8月）の言及が削除されました。

影響有無：
*   **ポジティブな影響**: これまで分間リクエスト数の制限に達していた大規模な書き込みワークロードは、より柔軟なログ取り込みが可能になる可能性があります。リクエスト数ではなくボリュームベースになったことで、多数のリクエストで少量のログを書き込むワークロードが有利になる場合があります。
*   **潜在的な影響**: 新しいボリュームベースのクォータが、既存のログ書き込みパターンにどのように影響するかは評価が必要です。特に、多数のリクエストで大量のログを書き込むワークロードでは、全体のログボリュームが増加し、新たなクォータ制限に抵触する可能性がないか確認が必要です。

対処方法：
1.  Cloud Logging API を利用してログ書き込みを行っている全てのサービスについて、新しい「Logging API quotas and limits」ドキュメントを参照し、現在のログ書き込みパターンが新しいボリュームベースのリージョン別クォータに適合しているかを評価してください。
2.  Google Cloud Monitoring を利用して、Logging API のクォータ使用状況（特にバイト数）を監視し、予期せぬスロットリングや制限が発生していないか継続的に確認することを推奨します。

用語説明：
*   **クォータ (Quota)**: Google Cloud リソースの使用量に設定された上限。サービスを安定稼働させ、過剰なリソース消費を防ぐために設定されます。
*   **ボリュームベースのリージョン別クォータ (Volume-based regional quotas)**: 特定のリージョンにおいて、ログの書き込み量（バイト数）に基づいて設定されるクォータ。従来の API リクエスト数ベースではなく、データ量に基づいているため、一度に大量のログを書き込む場合に有利になることがあります。

---

# Spanner
## Changed
原文:
[3.58.0](https://github.com/googleapis/python-spanner/compare/v3.57.0...v3.58.0)
- **spanner:** Support setting read lock mode (#1404) (ee24c6e)
- Remove Python 3.7 and 3.8 as supported runtimes (#1395) (fc93792)

説明：
`google-cloud-spanner` Python クライアントライブラリのバージョン 3.58.0 がリリースされました。
*   このバージョンでは、Spanner の読み取りロックモードを設定する機能が追加されました。
*   **重要な変更として、Python 3.7 および 3.8 の公式サポートが終了しました。**

影響有無：
*   **読み取りロックモードのサポート追加**: 新機能の追加であり、既存の Spanner ワークロードや Python コードに直接的な影響はありません。
*   **Python 3.7/3.8 のサポート終了**:
    *   現在、当社の Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) は Python 3.8 を基盤として動作しています。
    *   この Spanner ライブラリのバージョン 3.58.0 以降に更新した場合、Composer 環境で利用されている Python 3.8 はサポート対象外となります。
    *   直ちに動作しなくなるわけではありませんが、今後、Python 3.8 環境での動作に関するバグ修正やセキュリティパッチが提供されなくなる可能性があります。これにより、将来的な安定性やセキュリティリスクが発生する可能性があります。

対処方法：
1.  **Python 3.7/3.8 環境での `google-cloud-spanner` 利用**:
    *   Google Cloud Composer 2.7.1 環境で `google-cloud-spanner` ライブラリを利用している場合、現状では Python 3.8 が基盤であるため、このライブラリをバージョン 3.57.x 以前に固定することを強く推奨します。
    *   将来的に `google-cloud-spanner` をバージョンアップする必要がある場合は、Composer 環境自体の Python バージョンを 3.9 以降にアップグレードする必要があります。これには、Composer 環境のバージョンアップが必要となる可能性が高いです。Composer のアップグレードパスと、その際の Airflow 環境への影響を事前に評価してください。
    *   カスタムの Python 環境で Python 3.7/3.8 を利用している場合は、Python 3.9 以降へのアップグレードを計画してください。
2.  **新しい読み取りロックモードの利用**: Spanner の読み取り操作のパフォーマンスやトランザクション分離レベル要件に基づいて、新しい読み取りロックモードの機能を評価し、必要に応じて利用を検討してください。

用語説明：
*   **読み取りロックモード (Read Lock Mode)**: データベーストランザクションにおける読み取り操作のロック戦略。Spanner においては、読み取りの一貫性や分離レベルを制御するために使用されます。これにより、並行性とデータ整合性のバランスを調整します。
*   **サポートランタイム (Supported Runtimes)**: ソフトウェアライブラリやフレームワークが、正常に動作することを保証するプログラミング言語のバージョン。サポートが終了すると、そのバージョンでの動作保証がなくなり、将来のバグ修正や新機能が提供されなくなる可能性があるため、利用継続にはリスクが伴います。