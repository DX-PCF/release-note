
# Title: September 01, 2026 
Link: https://docs.cloud.google.com/release-notes#September_01_2026<br>
Google Cloudのリリースノートを元に、構築済みのサービスへの影響調査結果を以下に回答します。

---

# Cloud SDK

## Change

**原文:** (情報なし)

**説明:** リリースノートに原文が提供されていないため、具体的な変更内容を把握できません。

**影響有無:** 原文情報が不足しているため、具体的な影響有無を判断できません。
通常、Cloud SDKの変更は、CI/CDパイプラインや開発環境におけるコマンドライン操作、SDKを利用したスクリプトなどに影響を及ぼす可能性がありますが、デプロイ済みのサービスそのものへの直接的な影響は少ないことが多いです。

**対処方法:** 変更内容が不明なため、具体的な対処方法は提示できません。もしこの項目に詳細情報が追加された場合は、改めて内容を確認し、必要に応じてSDKのバージョンアップ計画やCI/CDパイプラインへの影響を評価してください。

**用語説明:**
*   **Cloud SDK:** Google Cloudサービスとやり取りするためのコマンドラインツール (gcloud CLI)、ライブラリ、ツールセットのコレクション。

---

# Cloud Service Mesh

## Security

**原文:** Managed Cloud Service Mesh will start using proxy version csm_mesh_proxy.20260819_RC00 for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.37. This change is rolling out to all release channels and contains the fix for the managed Cloud Service Mesh security vulnerabilities listed in [GCP-2026-057](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).

**説明:** マネージドCloud Service Meshが、GKEクラスター上のGateway API向けに新しいプロキシバージョン `csm_mesh_proxy.20260819_RC00` (Envoyバージョン1.37相当) の使用を開始します。この変更はすべてのリリースチャネルに順次適用され、[GCP-2026-057](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057) で報告されているマネージドCloud Service Meshのセキュリティ脆弱性に対する修正が含まれています。

**影響有無:**
*   **当社の状況:** 当社がGKEクラスター上でGateway APIを使用し、マネージドCloud Service Meshを積極的に利用している場合、この変更の対象となります。Google Cloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3) は、通常、直接Cloud Service Meshを利用する設定は行いませんが、基盤となるGKEクラスターはGoogleによって管理されており、その一部としてService Meshの機能が展開される可能性はゼロではありません。
*   **影響の性質:** 今回の変更はセキュリティ脆弱性の修正を含むプロキシバージョンの自動更新であり、サービス利用継続性への直接的な悪影響よりも、セキュリティ強化というポジティブな影響が期待されます。非互換性が生じる可能性は低いですが、非常に特定のEnvoyバージョンに依存する構成が存在する場合は注意が必要です。

**対処方法:**
*   **ユーザー側の直接的な操作は不要です。** マネージドサービスであるため、Googleによって自動的にロールアウトされます。
*   ただし、もし貴社でCloud Service MeshをGKEクラスター上でGateway APIと共に利用しており、特定のEnvoyバージョンに強く依存する複雑なトラフィックルーティングやポリシーを設定している場合は、更新後の動作に予期せぬ影響がないか、テスト環境での確認を推奨します。
*   今回の変更はセキュリティ向上を目的としているため、基本的には自動適用を許容し、変更後のシステム動作を注意深く監視してください。

**用語説明:**
*   **Cloud Service Mesh:** Google Cloudが提供するマネージドなサービスメッシュソリューション。Istioをベースにしており、GKEクラスター上のサービス間の通信管理、トラフィックルーティング、セキュリティポリシー適用、可観測性を提供します。
*   **Gateway API:** Kubernetesの標準的なAPIで、クラスター内外のトラフィックルーティングを管理するための高レベルなインターフェースです。Ingress APIの後継として設計されています。
*   **Envoy:** 高性能なオープンソースのプロキシで、Cloud Service Mesh (Istio) のデータプレーンとして機能し、サービス間のトラフィックを処理します。
*   **セキュリティ脆弱性 (GCP-2026-057):** クラウドサービスやソフトウェアにおけるセキュリティ上の欠陥。今回のアップデートでこれらの脆弱性が修正されます。

---

# Google Kubernetes Engine

## Change

**原文:** GKE version 1.35.1-gke.1031000 and later include the following changes to automatically created firewall rules for Services: [automatically created firewall rules for Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws) - Changes the priority of multiple existing firewall rules for Services from `1000` to `999`. - Creates additional firewall rules to deny traffic that is not explicitly allowed by other auto-created firewall rules. If you use custom firewall rules to override GKE firewall rules for Services, these changes might cause unexpected behavior. Before you upgrade your clusters to version 1.35.1-gke.1031000 or later, do the following: - If you have custom firewall rules that allow or deny traffic with a priority of `1000`, change the priority of those rules to a numerically lower value (such as `999` or lower) to maintain their precedence. - Verify that the new auto-created deny rules do not block required traffic for load balancers that use external IP addresses.

**説明:** GKEバージョン1.35.1-gke.1031000以降で、サービス向けに自動作成されるファイアウォールルールに変更が導入されます。具体的には、既存の複数の自動作成ファイアウォールルールの優先度が`1000`から`999`に変更され、さらに、他の自動作成ルールによって明示的に許可されていないトラフィックを拒否する追加のファイアウォールルールが作成されます。
もしカスタムファイアウォールルールを使用してGKEの自動作成ルールを上書きしている場合、これらの変更によって予期せぬ動作が発生する可能性があります。クラスターをバージョン1.35.1-gke.1031000以降にアップグレードする前に、以下の対応が推奨されています。
*   優先度`1000`でトラフィックを許可または拒否するカスタムファイアウォールルールがある場合、それらのルールの優先度を`999`以下の数値に変更し、優先順位を維持する。
*   新しく自動作成されるDenyルールが、外部IPアドレスを使用するロードバランサーに必要なトラフィックをブロックしないことを確認する。

**影響有無:**
*   **当社の状況:** Google Cloud Composer2はGKEクラスター上で稼働しているため、基盤となるGKEバージョンが将来的に1.35.1-gke.1031000以降にアップグレードされることで、この変更の影響を受ける可能性があります。
*   **直接GKEを運用している場合:** もし貴社がGKEクラスターを直接運用しており、特にGKEの自動作成ファイアウォールルールを上書きするようなカスタムファイアウォールルール（特に優先度`1000`のルール）を定義している場合、本変更は**直接的な影響**を与えます。意図しない通信ブロックやサービス停止につながる可能性があります。また、外部IPアドレスを持つロードバランサーを使用している場合も、新しいDenyルールが通信をブロックしないかの確認が必要です。
*   **Composerへの影響:** Composerはマネージドサービスであり、基盤のGKEクラスターの管理はGoogle Cloudが行います。通常、ComposerユーザーがGKEのファイアウォールルールを直接カスタマイズすることは稀ですが、Composer環境から特定の外部サービスへのアクセスなどを目的として、VPCネットワークレベルや既存のGKE自動作成ルールに依存するカスタムファイアウォールルールを適用している場合は、間接的に影響を受ける可能性があります。Google側で互換性が確認された上でバージョンアップが実施されるはずですが、万一、将来的にComposer環境からの外部通信に問題が発生した場合は、このGKEファイアウォールルールの変更が原因である可能性を疑う必要があります。

**対処方法:**
*   **直接GKEを運用している場合:**
    1.  貴社のGKEクラスターがバージョン1.35.1-gke.1031000以降にアップグレードされる前に、現在設定されているカスタムファイアウォールルールを確認してください。
    2.  もし優先度`1000`のカスタムファイアウォールルールが存在し、それがGKEの自動作成ルールよりも優先されるべき設定である場合、そのルールの優先度を`999`以下のより低い数値（優先度が高い）に変更してください。
    3.  外部IPアドレスを使用するロードバランサー（例えば、インターネット向けアプリケーションのService LoadBalancerなど）を利用している場合、新しい自動作成Denyルールがそれらのトラフィックを誤ってブロックしないか、事前に評価またはアップグレード後に綿密な動作確認を実施してください。
*   **Composer環境について:**
    *   Composerの基盤GKEが自動的にバージョンアップされる際に、貴社のAirflowワークフロー（特に外部システムとの連携部分）に問題が発生しないか、継続的に監視してください。
    *   Composerのネットワーク設定で特別なカスタマイズを行っている場合（例: Private IPアクセスや特定のVPC Service Controlsなど）、将来的なGKEバージョンアップに関するGoogle Cloudの公式アナウンスやドキュメントを注視し、互換性の情報を確認することが重要です。

**用語説明:**
*   **ファイアウォールルール:** ネットワークトラフィックの許可・拒否を制御する設定。Google CloudのVPCネットワーク内で、インスタンス間の通信や外部との通信を制御するために使用されます。
*   **優先度 (Priority):** ファイアウォールルールの適用順序を決定する数値。数値が小さいほど優先度が高く、同じトラフィックに複数のルールが一致する場合、優先度の高いルールが適用されます。
*   **Service (Kubernetes):** Kubernetesクラスタ内で実行されている一連のPodへの論理的なアクセスポイントを定義するリソース。外部からのアクセス（LoadBalancer Service）やクラスター内部からのアクセスを可能にします。
*   **ロードバランサー (Load Balancer):** 複数のバックエンド（ここではKubernetes Pod）にネットワークトラフィックを分散させる仕組み。GKEでは、Serviceリソースの種類に応じてGoogle Cloudのロードバランサーが自動的にプロビジョニングされます。
# Title: August 31, 2026 
Link: https://docs.cloud.google.com/release-notes#August_31_2026<br>
Google Cloud のリリースノートに対する影響調査結果を以下に報告いたします。

---

# BigQuery
## Fixed
原文: Support for configuring daily token quotas for BigQuery generative AI functions has been restored.
[configuring daily token quotas](https://docs.cloud.google.com/bigquery/docs/control-genai-costs)

説明：
BigQueryの生成AI機能（BigQuery MLの`GENERATE_TEXT`など、Vertex AIと連携する機能）において、日次トークンクォータを設定する機能が復元されました。以前にこの機能に問題があった可能性がありましたが、今回の修正により正常に設定および適用できるようになりました。これにより、生成AI機能利用時のコスト管理が改善されます。

影響有無：
**影響あり（ポジティブな改善）**
*   **BigQueryの生成AI機能を利用している場合**: 以前、日次トークンクォータの設定に問題があり、意図したコスト制御ができていなかった場合は、今回の修正によってこの機能が正常に動作するようになります。これにより、より効果的なコスト管理とリソース利用の制限が可能になります。
*   **BigQueryの生成AI機能を利用していない場合**: 直接的な影響はありません。

対処方法：
BigQueryの生成AI機能をご利用中で、日次トークンクォータの設定や運用にご関心がある場合は、[公式ドキュメント](https://docs.cloud.google.com/bigquery/docs/control-genai-costs)を参照の上、設定の見直しや適用をご検討ください。特に、これまでのクォータ設定が期待通りに機能していなかった場合は、再確認をお勧めします。

用語説明：
*   **BigQuery generative AI functions**: Google BigQueryが提供する機能で、SQLクエリ内でVertex AIなどの生成AIモデルを利用してテキスト生成や要約といったタスクを実行できるものです。`GENERATE_TEXT`関数などが該当します。
*   **Daily token quotas**: BigQueryの生成AI機能の使用量（トークン数）に対して、1日あたりの上限を設定できる割り当て機能です。これにより、予期せぬ高額な利用料金が発生するのを防ぎ、コストを管理できます。

---

# Cloud Service Mesh
## Announcement
原文: **1.30.4-asm.1 is now available for in-cluster Cloud Service Mesh.**
You can now download 1.30.4-asm.1 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.30.4 subject to the list of supported features.
[Istio 1.30.4](https://istio.io/latest/news/releases/1.30.x/announcing-1.30/)
[supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster)
The following are not supported:
- Failover Priority support for DNS clusters
- `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`
- Multiple `CUSTOM` external authorization providers per workload
- The `DEBUG_ENDPOINT_AUTH_ALLOWED_NAMESPACES` flag
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.30.4-asm.1 uses Envoy v1.38.4-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：
in-cluster Cloud Service Mesh の新バージョン `1.30.4-asm.1` がリリースされました。このバージョンは、Istio 1.30.4 の機能を基盤としていますが、特定の機能（DNSクラスタのフェイルオーバー優先度サポート、`ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`、複数のカスタム外部認可プロバイダ、`DEBUG_ENDPOINT_AUTH_ALLOWED_NAMESPACES`フラグ）はサポート対象外とされています。このバージョンではEnvoy v1.38.4-devが使用されます。

影響有無：
**影響あり（機能追加および潜在的な非互換性）**
*   **新機能の利用**: Istio 1.30.4 で導入された新機能や改善点が利用可能になります。パフォーマンス向上やセキュリティ強化などが期待されます。
*   **アップグレードの検討**: 現在Cloud Service Meshをご利用の場合、この新バージョンへのアップグレードを検討する機会となります。最新の機能やセキュリティパッチを適用するためにはアップグレードが推奨されます。
*   **未サポート機能の確認**: リリースノートに明記されている4つの未サポート機能（"Failover Priority support for DNS clusters", "`ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`", "Multiple `CUSTOM` external authorization providers per workload", "The `DEBUG_ENDPOINT_AUTH_ALLOWED_NAMESPACES` flag"）を現在の環境で利用している、または将来的に利用を計画している場合は、アップグレード前にこれらの機能の代替策を検討するか、アップグレードパスを慎重に評価する必要があります。これらを現在利用している場合、アップグレードは機能の喪失につながります。
*   **Envoyバージョンの変更**: Envoyのバージョンが`v1.38.4-dev`に変更されるため、カスタムフィルタや高度な設定を利用している場合は互換性を確認する必要があります。

対処方法：
Cloud Service Meshをご利用中の場合は、以下の対応をご検討ください。
1.  現在のCloud Service Meshのバージョンと構成を確認してください。
2.  リリースノートに記載されている「未サポート機能」が現在の環境で利用されていないか、または将来の計画に含まれていないかを確認してください。利用している場合は、代替策の検討が必要になります。
3.  [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)ドキュメントを参照し、バージョンアップの手順、注意事項、および潜在的な影響を詳細に確認した上で、計画的にアップグレードを検討・実施してください。

用語説明：
*   **Cloud Service Mesh (in-cluster)**: Google Kubernetes Engine (GKE) クラスタ内で動作するマネージドなIstioサービスメッシュソリューションです。トラフィック管理、セキュリティ、可観測性を提供します。
*   **Istio**: マイクロサービス間のトラフィック管理、セキュリティ、ポリシー適用、可観測性を提供するオープンソースのサービスメッシュプラットフォームです。
*   **Envoy**: Istioがデータプレーンとして使用する高性能なオープンソースのプロキシです。サービスメッシュ内のすべてのネットワークトラフィックを処理します。
*   **Failover Priority support for DNS clusters**: DNSベースのサービスディスカバリにおけるフェイルオーバーの優先順位付けに関する機能。
*   **`ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`**: TLS設定においてワイルドカードホスト名を持つサービスエントリーを許可するかどうかを制御する機能フラグ。
*   **Multiple `CUSTOM` external authorization providers per workload**: ワークロードごとに複数のカスタム外部認可サービスを設定できるようにする機能。
*   **`DEBUG_ENDPOINT_AUTH_ALLOWED_NAMESPACES` flag**: デバッグ目的でエンドポイント認証が許可されるネームスペースを指定するためのフラグ。

---

# Cloud Service Mesh
## Announcement
原文: In-cluster Cloud Service Mesh 1.27 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.
[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

説明：
in-cluster Cloud Service Mesh バージョン 1.27 のサポートが終了したことが発表されました。サポートが終了したバージョンは、今後セキュリティパッチやバグ修正が提供されなくなるため、利用継続にはリスクが伴います。他のバージョンのサポート終了日については、[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)ドキュメントで確認できます。

影響有無：
**影響あり（重大）**
*   **Cloud Service Mesh 1.27 を利用中の場合**: 現在、Cloud Service Mesh 1.27 を運用しているシステムは、サポートが終了した状態となります。これは、新たなセキュリティ脆弱性やバグが発見されても、Google Cloud からの修正が提供されないことを意味し、セキュリティリスクや運用上の問題が顕在化する可能性が非常に高くなります。速やかにサポート対象のバージョンへのアップグレードが必須です。
*   **Cloud Service Mesh 1.27 を利用していない場合**: 直接的な影響はありません。しかし、現在ご利用のバージョンについても、将来的にサポート終了日が設定される可能性があるため、定期的に[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)ドキュメントを確認し、計画的なアップグレードサイクルを維持することが重要です。

対処方法：
1.  **Cloud Service Mesh 1.27 をご利用中の場合**: 最優先で、サポート対象の最新バージョン（例えば、上記の `1.30.4-asm.1` など）へのアップグレードを計画し、実行してください。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)ドキュメントを詳細に参照してください。
2.  **Cloud Service Mesh をご利用中のすべてのユーザー**: 現在ご利用のバージョンのサポート終了日を[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)で確認し、計画的なバージョンアップロードマップを策定・実行することで、常にサポートされた安全な環境を維持してください。

用語説明：
*   **サポート終了 (End-of-Life, EOL)**: ソフトウェアやサービスの特定のバージョンに対して、ベンダーからの公式サポート（バグ修正、セキュリティパッチ、技術サポートなど）が終了すること。EOLを迎えたバージョンを使い続けると、セキュリティリスクやシステム障害のリスクが高まります。
*   **Supported versions**: Google Cloud がサポートを提供しているCloud Service Meshのバージョンのリストおよび、各バージョンのサポート終了日を示すドキュメント。