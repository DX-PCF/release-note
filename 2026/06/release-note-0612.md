
# Title: June 10, 2026 
Link: https://docs.cloud.google.com/release-notes#June_10_2026<br>
はい、承知いたしました。Google Cloudのリリースノートより、Google Kubernetes Engineに関する変更を調査し、ご提示いただいたフォーマットで回答いたします。

---

# Google Kubernetes Engine

## Deprecated
原文: The configuration option to not enroll your cluster in a release channel (known as *No channel*, formerly as *Static*) is now deprecated, and will be removed on June 14, 2027. For any clusters not enrolled in a release channel, we recommend that you enroll the cluster before this date. After the removal date, GKE will enroll all remaining clusters in the Stable channel. For more information about this deprecation and how you can achieve the same functionality with release channels, see Clusters not enrolled in a release channel.

説明:
Google Kubernetes Engine (GKE) のクラスタ設定において、リリースチャンネルに登録しないオプション（以前は「Static」と呼ばれ、現在は「No channel」として知られているもの）が非推奨となりました。このオプションは2027年6月14日に完全に削除される予定です。
GKEでは、この廃止日までに、現在リリースチャンネルに登録されていないクラスタを何らかのリリースチャンネルに登録することを推奨しています。もし廃止日までに登録が行われない場合、GKEは残りのすべてのクラスタを自動的に「Stable」チャンネルに登録します。
この変更の詳細や、リリースチャンネルを利用して同様の機能を実現する方法については、関連ドキュメントを参照してください。

影響有無:
**影響あり**

*   **影響理由:** 現在運用中のGKEクラスタがリリースチャンネルに登録していない「No channel」または「Static」設定を使用している場合、直接的な影響があります。
    *   2027年6月14日以降、これらのクラスタは自動的に「Stable」チャンネルに強制登録されます。これにより、クラスタのバージョンアップグレードの制御方法が変更され、これまで手動で厳密にバージョン管理をしていた運用に影響を与える可能性があります。
    *   「Stable」チャンネルに登録されることで、GKEが提供する自動アップグレード機能やパッチ適用サイクルに従うことになり、手動でのアップグレード制御の自由度が失われます。
    *   この変更は非互換性のある変更（Breaking Change）ではないものの、運用ポリシーの変更を余儀なくされる可能性があります。

対処方法:
1.  **影響を受けるクラスタの特定:** 現在運用しているGKEクラスタの中で、リリースチャンネルに登録されていない「No channel」または「Static」設定のクラスタがあるかを確認してください。
    *   `gcloud container clusters describe CLUSTER_NAME --zone=COMPUTE_ZONE --project=PROJECT_ID` コマンドなどでクラスタの状態を確認し、`releaseChannel` フィールドが存在しないか、`NONE` となっているクラスタが対象です。
2.  **適切なリリースチャンネルへの移行計画:** 2027年6月14日までに、これらのクラスタをビジネス要件と運用ポリシーに合ったリリースチャンネル（Rapid、Regular、Stable）へ登録することを検討し、計画を立ててください。
    *   **Rapid:** 最新機能やパッチを早期に利用したい場合に適しています。
    *   **Regular:** 最新の安定版リリースと十分なテスト期間を確保したい場合に適しています。
    *   **Stable:** 安定性と長期的なサポートを最も重視する場合に適しています。
    *   Google Cloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3) を使用している場合、Composerの動作安定性を考慮し、GKEのバージョンアップグレードがComposerに与える影響を最小限に抑えるチャンネル（例: StableまたはRegular）を選択することが推奨されます。Composerの対応GKEバージョンも確認してください。
3.  **移行の実施:** 計画に基づき、対象クラスタを新しいリリースチャンネルに登録する作業を実施してください。
    *   `gcloud container clusters update CLUSTER_NAME --release-channel=CHANNEL_NAME --zone=COMPUTE_ZONE --project=PROJECT_ID` コマンドでチャンネルを更新できます。
4.  **移行後の運用確認:** 移行後、クラスタの自動アップグレード動作やアプリケーションへの影響がないかを継続的に監視・確認してください。

用語説明:
*   **リリースチャンネル (Release channel):** GKEクラスタのバージョンアップグレードとパッチ適用を管理する仕組みです。Rapid、Regular、Stableの3つの主要なチャンネルがあり、それぞれ異なるアップグレード頻度と機能提供のタイミングを持ちます。これにより、ユーザーは自動アップグレードの速度と安定性のバランスを選択できます。
*   **No channel (Static):** 以前のGKEクラスタのリリース管理方式で、クラスタをどのリリースチャンネルにも登録せず、ユーザーが手動でGKEバージョンアップグレードのタイミングとバージョンを完全に制御することを可能にしていました。このオプションは現在非推奨であり、将来的に削除されます。
*   **Deprecated (非推奨):** 特定の機能や設定が将来的にサポートされなくなり、最終的には削除されることを示します。通常、代替手段が提供され、ユーザーに移行期間が与えられます。
*   **Stable channel:** リリースチャンネルの一つで、最も安定性が高く、広範囲にテストされたGKEバージョンが提供されます。新しい機能の導入は他のチャンネルよりも遅くなりますが、その分、長期的な安定稼働を重視するワークロードに適しています。
# Title: June 09, 2026 
Link: https://docs.cloud.google.com/release-notes#June_09_2026<br>
はい、承知いたしました。Google Cloudのインフラエンジニアとして、ご提示のリリースノートについて製品ごとに影響有無を調査し、回答例に沿って簡潔にご報告いたします。

---

# Cloud SDK
## Change
原文: (原文が提示されていません。)
説明：Cloud SDKの変更に関するリリースノートですが、具体的な変更内容を示す原文が提供されていないため、詳細を把握できません。
影響有無：原文がないため、特定の影響有無を判断することはできません。
対処方法：具体的な変更内容が不明なため、現時点での対処は不要です。Cloud SDKのバージョンアップを行う際は、リリースノートや変更ログで詳細を確認することを推奨します。

---

# Cloud Service Mesh
## Announcement

 **1.29.4-asm.0 is now available for in-cluster Cloud Service Mesh.**

 原文: 1.29.4-asm.0 is now available for in-cluster Cloud Service Mesh. It includes the features of Istio 1.29.4 subject to the list of supported features. [Istio 1.29.4](https://istio.io/latest/news/releases/1.29.x/announcing-1.29/) [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster) The following environment variables, labels, and annotations are not supported: - `PILOT_IGNORE_RESOURCES` and `PILOT_INCLUDE_RESOURCES` - `RetryIgnorePreviousHosts` - `omit_empty_values` - `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY` - `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` with the value 1 - `PILOT_DNS_JITTER_DURATION` - `PILOT_DNS_JITTER_DURATION` - `ENABLE_NATIVE_SIDECARS` with the value true - `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX` and `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX` - `PILOT_DNS_CARES_UDP_MAX_QUERIES` - `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS` - 'BLOCKED_CIDRS_IN_JWKS_URIS` - `ENABLE_DEBUG_ENDPOINT_AUTH` - `DISABLE_TRACK_REMAINING_CB_METRICS` - `gateway.istio.io/tls-cipher-suites` - `fileFlushMinSizeKB` and `fileFlushInterval` settings in ProxyConfig - `topology.istio.io/locality` - `statsCompression` ProxyConfig option - `proxy.istio.io/config` annotation for metric compression overrides Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported. The formatter option within the `spec.tracing[].customTags` field of the Telemetry custom resource (telemetry.istio.io) is unsupported. The `istiod_remote_cluster_sync_status` Prometheus gauge metric, exposed on the **Istiod control plane metrics endpoint** (port 15014 `/metrics`), is not supported. The following are unsupported for proxyless gRPC clients: - Configuring the `LEAST_REQUEST` load balancing policy within the `spec.trafficPolicy.loadBalancer.simple` field of a **DestinationRule** custom resource (`networking.istio.io`) - Configuring the `http2MaxRequests` circuit breaker within the `spec.trafficPolicy.connectionPool.http.http2MaxRequests` field of a **DestinationRule** custom resource (`networking.istio.io`) Configuring the `LEAST_REQUEST` load balancing policy within the `spec.trafficPolicy.loadBalancer.simple` field of a **DestinationRule** custom resource (`networking.istio.io`) Configuring the `http2MaxRequests` circuit breaker within the `spec.trafficPolicy.connectionPool.http.http2MaxRequests` field of a **DestinationRule** custom resource (`networking.istio.io`) The `ENABLE_AUTO_SNI` flag is still supported to keep aligned with the legacy behavior. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.29.4-asm.0 uses Envoy v1.37.4-dev. [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：インクラスターCloud Service Meshのバージョン1.29.4-asm.0がリリースされました。このバージョンはIstio 1.29.4の機能を基盤としていますが、公式ドキュメントに記載されているサポート対象機能のリストに従います。特に、多くの環境変数、ラベル、アノテーション、一部のIstio実験的機能、Telemetryカスタムリソースの特定のフィールド、Prometheusメトリック、およびProxyless gRPCクライアントの特定のロードバランシングポリシーやサーキットブレーカー設定がサポート対象外であることが明記されています。Envoyのバージョンはv1.37.4-devが使用されます。

影響有無：
*   **ポジティブ**: Istio 1.29.4の機能改善、パフォーマンス向上、セキュリティ修正などの恩恵を受ける可能性があります。
*   **注意/ネガティブ**: 現在インクラスターCloud Service Meshを利用しており、このバージョンへのアップグレードを検討する場合、リストアップされた非サポート項目を使用しているかどうかを確認する必要があります。もし使用している場合、アップグレード時に既存の構成が動作しなくなる可能性や、代替設定への変更が必要となる可能性があります。特に、`PILOT_IGNORE_RESOURCES`や`ENABLE_NATIVE_SIDECARS`など、運用に直接影響する設定が含まれています。

対処方法：
1.  現在インクラスターCloud Service Meshを利用している場合は、本バージョンへのアップグレードを計画します。
2.  既存のCloud Service Mesh構成において、リリースノートに記載されている「サポートされない項目」に該当する環境変数、ラベル、アノテーション、Istio機能、またはProxyless gRPCクライアントの設定が使用されていないか、詳細に確認します。
3.  もし該当する設定が発見された場合、アップグレード前にそれらの設定を削除または代替手段に切り替えることを検討し、非互換性によるサービスへの影響を避けるための対応策を講じます。
4.  本番環境への適用前に、開発・ステージング環境などで十分な互換性テストと動作検証を行います。
5.  アップグレード手順については、提供されている[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)ドキュメントを参照してください。

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するマネージドなIstioサービスであり、マイクロサービスの接続、監視、セキュリティ保護を容易にします。
*   **In-cluster Cloud Service Mesh**: Cloud Service Meshのデプロイメントモデルの一つで、IstioのコントロールプレーンがユーザーのGKEクラスタ内にデプロイされます。
*   **Istio**: オープンソースのサービスメッシュプラットフォームで、トラフィック管理、ポリシー適用、テレメトリー収集などの機能を提供します。
*   **Envoy**: Istioでデータプレーンとして利用される高性能なオープンソースのエッジおよびサービスプロキシです。
*   **Telemetry custom resource**: Istioにおいて、メトリクス、ロギング、トレーシングといったテレメトリー情報を設定するためのCustom Resource Definition (CRD) です。
*   **Prometheus**: オープンソースのモニタリングおよびアラートツールで、時系列データを収集・保存し、クエリや可視化が可能です。
*   **Proxyless gRPC clients**: Envoyサイドカープロキシを介さずに、直接gRPCアプリケーションがサービスメッシュのコントロールプレーンと通信し、ロードバランシングなどの機能を利用するクライアントです。
*   **DestinationRule**: Istioで利用されるCustom Resourceで、特定サービスへのトラフィックのルーティングやポリシー（例：ロードバランシング、サーキットブレーカー）を定義します。
*   **Load balancing policy**: 複数のバックエンドインスタンス間でトラフィックをどのように分散させるかを決定するアルゴリズムです。`LEAST_REQUEST`は、最もリクエスト数が少ないインスタンスにトラフィックを送るポリシーです。
*   **Circuit breaker**: マイクロサービスアーキテクチャにおける障害伝播を防ぐための設計パターンの一つで、閾値を超えたエラーが発生した場合に一時的にサービスへのアクセスを遮断します。

---

# Cloud Service Mesh
## Announcement

 **In-cluster Cloud Service Mesh 1.26 is no longer supported.**

 原文: In-cluster Cloud Service Mesh 1.26 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions. [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

説明：インクラスターCloud Service Meshのバージョン1.26が、正式にサポート対象外となりました。他のバージョンのサポート終了日（End of Life: EOL）については、[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)のドキュメントで確認できます。

影響有無：
*   **直接的**: 現在インクラスターCloud Service Mesh 1.26を使用している場合、このバージョンに対するGoogleからの公式サポート（セキュリティパッチ、バグ修正、技術サポート）が提供されなくなります。これにより、運用上のリスクが大幅に増加します。
*   **間接的**: 他のバージョンのCloud Service Meshを使用している場合でも、サポートポリシーの変更や将来のEOL計画を把握するための重要な情報となります。

対処方法：
1.  現在Cloud Service Mesh 1.26を利用しているお客様は、速やかにサポート対象の最新バージョン（例: 今回アナウンスされた1.29.4-asm.0）へのアップグレードを計画し、実施してください。サポート終了バージョンを使い続けることは、セキュリティリスクや運用上の問題を引き起こす可能性があります。
2.  利用中のCloud Service Meshのバージョンを確認し、[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)ドキュメントを参照して、当該バージョンのサポート終了日を把握してください。計画的なアップグレードサイクルを確立し、EOL前に常にサポート対象バージョンに移行するようにしてください。

用語説明：
*   **EOL (End of Life)**: ソフトウェアや製品のサポートが終了する日付を指します。この日付以降は、ベンダーからのセキュリティアップデート、バグ修正、技術サポートなどが提供されなくなります。

---

# Compute Engine
## Security

 **A vulnerability (CVE-2025-10263) about bypass of translation stages or GPT protections in some Arm core families was discovered and has been addressed.**

 原文: A vulnerability (CVE-2025-10263) about bypass of translation stages or GPT protections in some Arm core families was discovered and has been addressed. For more information, see the GCP-2026-036 security bulletin. [GCP-2026-036 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-036)

説明：一部のArmコアファミリーにおいて、トランスレーションステージまたはGPT（Granule Protection Table）保護をバイパスできる脆弱性（CVE-2025-10263）が発見されました。この脆弱性はGoogle Cloudによって既に修正済みであり、詳細についてはセキュリティ速報GCP-2026-036を参照できます。

影響有無：
*   **ポジティブ**: Google Cloudプラットフォームの基盤で脆弱性への対処が完了しているため、お客様が現在Compute EngineでArmベースのVM（例：Tau T2A）を利用している場合でも、プラットフォームレベルでのセキュリティが確保されており、ユーザー側で追加の対応を行う必要はありません。
*   **ネガティブ**: なし。ユーザーのワークロードやパフォーマンスに直接的な悪影響はありません。

対処方法：
お客様側で直接的に行うべき対処はございません。これはGoogle Cloudがインフラストラクチャレベルで実施したセキュリティ対策であり、お客様のCompute Engineインスタンスは既に保護されています。情報として、[GCP-2026-036 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-036) を確認することをお勧めします。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアのセキュリティ脆弱性を識別するための国際的な識別子です。
*   **Arm core families**: Armアーキテクチャに基づくCPUコアのファミリーを指します。Google Cloudでは、Tau T2AなどのVMインスタンスでArmプロセッサが利用されています。
*   **GPT (Granule Protection Table)**: Armアーキテクチャのメモリ管理ユニット（MMU）の一部であり、メモリ保護やアクセス制御を司るテーブルです。
*   **Security Bulletin**: 特定のセキュリティ脆弱性やその対策に関する公式の情報提供です。
# Title: June 08, 2026 
Link: https://docs.cloud.google.com/release-notes#June_08_2026<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、各製品の変更点、影響有無、対処方法について、専門的な言葉遣いと書式で回答いたします。

---

# Apigee X

## Announcement

原文: On June 8th, 2026, we released an updated version of Apigee (1-17-0-apigee-9).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigeeの新しいバージョン `1-17-0-apigee-9` がリリースされたことをお知らせします。このリリースは順次Google Cloudの全ゾーンに展開されており、完了までには4営業日以上かかる場合があります。お使いのインスタンスに新機能や修正が適用されるのは、このロールアウトが完了した後になります。

影響有無: 直接的な機能変更や停止などの影響はありません。ただし、本リリースに含まれるセキュリティ修正やバグ修正が環境に適用されるまでには、ロールアウト完了を待つ必要があります。

対処方法: 特段の対処は不要です。ロールアウトが完了するまで、最新の機能や修正が利用できない可能性があります。

用語説明:
*   **Rollout (ロールアウト)**: ソフトウェアや機能が、計画的に段階的に展開・導入されるプロセスを指します。

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **514384893** | **Security fix for Apigee.** Hardened the Script policy to block server-side request forgery (SSRF) to link-local addresses. |
| **N/A** | **Security fix for Apigee infrastructure.** |

説明:
*   ApigeeのScriptポリシーのセキュリティが強化され、[Link-localアドレス](https://ja.wikipedia.org/wiki/%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9)への[Server-Side Request Forgery (SSRF)](https://ja.wikipedia.org/wiki/Server-side_request_forgery)攻撃がブロックされるようになりました。
*   Apigeeのインフラストラクチャにおけるセキュリティ修正が適用されました。

影響有無: 影響あり（良い影響）。セキュリティ脆弱性の修正により、Apigee環境の堅牢性が向上します。
*   ID `514384893`: Scriptポリシーを使用して意図的にLink-localアドレス（例: `169.254.x.x`）へのリクエストを行っていた場合、その動作はブロックされます。一般的なAPIプロキシの利用においては影響はありません。
*   ID `N/A`: インフラストラクチャレベルのセキュリティ修正であり、サービス運用に直接的な影響はありません。

対処方法:
*   ID `514384893`: ApigeeのScriptポリシーでLink-localアドレスへのアクセスを必要とするユースケースがあった場合、代替手段の検討が必要です。通常は該当しません。
*   ID `N/A`: 自動的に適用されるため、お客様側での特別な対処は不要です。

用語説明:
*   **Server-Side Request Forgery (SSRF)**: サーバーが提供する機能を利用して、攻撃者がサーバー側から任意のURLにリクエストを送信させる攻撃手法です。これにより、内部ネットワークへのアクセスや機密情報の取得、他のシステムへの攻撃などが可能になる場合があります。
*   **Link-local address**: ホスト間で直接通信するために、ルーターを介さずに自動的に割り当てられるIPアドレスです。IPv4では`169.254.0.0/16`の範囲が用いられます。クラウド環境のメタデータサービスへのアクセスなどにも使用されます。

## Fixed

原文:
| Bug ID | Description |
| --- | --- |
| **512850756** | Added observability metrics for the OpenTelemetry trace export pipeline, reporting spans exported, export latency, batch size, and dropped spans. |
| **515039499** | Fixed an issue where OpenTelemetry trace export over HTTP could fail to authenticate when sent through a forward proxy that requires basic authentication. |

説明:
*   OpenTelemetryトレースのエクスポートパイプラインに、エクスポートされた[Span](https://opentelemetry.io/docs/concepts/signals/traces/#spans)数、エクスポートのレイテンシ、バッチサイズ、ドロップされたSpan数など、[可観測性（Observability）](https://cloud.google.com/architecture/devops/devops-tech-observability)に関する新しい[メトリクス](https://cloud.google.com/monitoring/docs/metrics-introduction)が追加されました。
*   基本認証を必要とする[フォワードプロキシ](https://cloud.google.com/load-balancing/docs/proxy-overview?hl=ja#forward_proxy)経由でOpenTelemetryトレースをHTTPでエクスポートする際に、認証に失敗する可能性があった問題が修正されました。

影響有無: 影響あり（良い影響）。
*   ID `512850756`: OpenTelemetryを利用している場合、トレースエクスポートの監視が強化されます。機能追加であり、既存の動作への悪影響はありません。
*   ID `515039499`: 基本認証を必要とするフォワードプロキシ経由でOpenTelemetryトレースをエクスポートする構成を採用していた環境では、この修正により認証失敗の問題が解消されます。該当しない環境には影響ありません。

対処方法:
*   ID `512850756`: 新しいメトリクスを活用することで、ApigeeのOpenTelemetryトレースエクスポートの状態をより詳細に監視できるようになります。必要に応じて、監視ダッシュボードやアラート設定の見直しを検討してください。必須の対処ではありません。
*   ID `515039499`: 問題が修正されるため、特別な対処は不要です。

用語説明:
*   **OpenTelemetry**: ベンダーに依存しないオープンソースの観測可能性フレームワークです。分散トレース、メトリクス、ログの収集・エクスポートのためのAPI、SDK、ツールを提供します。
*   **Span**: 分散トレースにおける単一の論理的な作業単位（例: API呼び出し、データベースクエリなど）を表します。トレースは複数のSpanで構成されます。
*   **Observability metrics**: システムの内部状態を外部から理解するための測定可能なデータです。パフォーマンス、エラーレート、リソース使用量などが含まれます。
*   **Forward Proxy (フォワードプロキシ)**: クライアントからのリクエストをインターネット上のサーバーに転送するプロキシサーバーです。通常、セキュリティ、キャッシング、トラフィックのルーティングなどの目的で使用されます。
*   **Basic Authentication (基本認証)**: HTTPの認証スキームの一つで、ユーザー名とパスワードをBase64エンコードしてHTTPヘッダに含めて送信する、比較的シンプルな認証方法です。

---

# Cloud Service Mesh

## Security

原文:
**1.28.7-asm.4 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.28.7-asm.4 uses Envoy v1.36.8-dev.

**1.27.9-asm.5 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.5 uses Envoy v1.35.12-dev.

**1.26.8-asm.11 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.11 uses Envoy v1.34.14.

説明:
Cloud Service Meshの複数のバージョン（`1.28.7-asm.4`, `1.27.9-asm.5`, `1.26.8-asm.11`）向けにパッチリリースが提供されました。これらのパッチリリースには、[GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035)で詳細が説明されているセキュリティ脆弱性の修正が含まれています。各バージョンで使用されるEnvoyのバージョンも明記されています。

影響有無: 影響あり（良い影響）。既知のセキュリティ脆弱性が修正されるため、Cloud Service Mesh環境のセキュリティ体制が向上します。利用中のCloud Service Meshのバージョンに応じて、この修正を適用することを強く推奨します。

対処方法:
現在利用しているCloud Service Meshのバージョンを確認し、該当する最新のパッチバージョンへのアップグレードを強く推奨します。アップグレード手順については、各バージョンの公式ドキュメントを参照してください。
*   Cloud Service Meshのアップグレード ([Cloud Service Mesh のアップグレード](https://cloud.google.com/service-mesh/docs/upgrade/upgrade))

用語説明:
*   **Patch release (パッチリリース)**: 既存のソフトウェアバージョンに対して、主にバグ修正やセキュリティ修正を目的とした小規模な更新リリースです。
*   **Security vulnerability (セキュリティ脆弱性)**: ソフトウェアやシステムの設計上の欠陥や実装上の誤りにより、攻撃者によって悪用される可能性のある弱点です。
*   **Envoy**: 高性能なオープンソースのエッジおよびサービスプロキシです。IstioやCloud Service Meshのデータプレーンとして使用されます。

## Announcement

原文: The rollouts previously announced on June 3, 2026 have been stopped. The following release will supersede them and include those patches and the fix for the vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).

説明: 2026年6月3日に発表された以前のCloud Service Meshのロールアウトは停止されました。今回の新しいリリースがそれらに取って代わり、以前のパッチと[GCP-2026-035](https://docs.cloud.com/service-mesh/docs/security-bulletins#gcp-2026-035)で言及されているセキュリティ脆弱性の修正がすべて含まれています。

影響有無: 直接的な影響はありません。以前のロールアウトが停止され、今回のリリースで必要な修正がすべて統合された形で提供されるため、結果的にセキュリティ向上の観点からは良い影響となります。

対処方法: 特段の対処は不要です。上記のセキュリティ修正が適用された最新バージョンへのアップグレードを検討してください。

用語説明:
*   **Supersede (スーパーシード)**: （前のものに）取って代わる、置き換わることを意味します。この文脈では、以前のリリースが新しいリリースによって完全に置き換えられたことを示します。