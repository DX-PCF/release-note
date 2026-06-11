
# Title: June 09, 2026 
Link: https://docs.cloud.google.com/release-notes#June_09_2026<br>
Google Cloudのリリースノートに基づき、各製品に対する影響調査を以下の通り実施しました。

---

# Cloud SDK
## Change
**原文:** (情報が提供されていません)
**説明:** Cloud SDKに関する変更がアナウンスされていますが、具体的な変更内容は提供されたリリースノートのテキストには含まれていません。通常、Cloud SDKの変更は、コマンドラインインターフェース（gcloud CLI）やクライアントライブラリの機能追加、修正、パフォーマンス改善などに関連します。
**影響有無:**
*   **不確定:** 具体的な変更内容が不明であるため、既存のワークロードへの影響有無を判断できません。Cloud SDKを使用するCI/CDパイプラインやスクリプトがある場合、変更内容によっては影響を受ける可能性があります。
*   **Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3):** Composer環境の内部ではCloud SDKが利用されていますが、これはGoogleによってマネージドされているため、ユーザー側で直接的な対処は通常不要です。しかし、Airflow DAGs内で`gcloud`コマンドなどを直接呼び出している場合、変更内容によっては影響が出る可能性もゼロではありません。
**対処方法:**
*   このリリースノートのより詳細な情報が公開された場合、またはCloud SDKのバージョンアップグレードを行う際には、変更履歴（Release Notes for Google Cloud CLI）を確認し、既存のスクリプトやアプリケーションとの互換性を検証することを推奨します。
**用語説明:**
*   **Cloud SDK:** Google Cloudサービスとやり取りするためのコマンドラインツール（`gcloud` CLI）、クライアントライブラリ、およびローカル開発ツールセットを含むソフトウェア開発キットです。

---

# Cloud Service Mesh
## Announcement
**原文:** 1.29.4-asm.0 is now available for in-cluster Cloud Service Mesh. You can now download 1.29.4-asm.0 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.29.4 subject to the list of supported features. [Istio 1.29.4](https://istio.io/latest/news/releases/1.29.x/announcing-1.29/) [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster) The following environment variables, labels, and annotations are not supported: - `PILOT_IGNORE_RESOURCES` and `PILOT_INCLUDE_RESOURCES` - `RetryIgnorePreviousHosts` - `omit_empty_values` - `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY` - `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` with the value 1 - `PILOT_DNS_JITTER_DURATION` - `PILOT_DNS_JITTER_DURATION` - `ENABLE_NATIVE_SIDECARS` with the value true - `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX` and `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX` - `PILOT_DNS_CARES_UDP_MAX_QUERIES` - `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS` - 'BLOCKED_CIDRS_IN_JWKS_URIS` - `ENABLE_DEBUG_ENDPOINT_AUTH` - `DISABLE_TRACK_REMAINING_CB_METRICS` - `gateway.istio.io/tls-cipher-suites` - `fileFlushMinSizeKB` and `fileFlushInterval` settings in ProxyConfig - `topology.istio.io/locality` - `statsCompression` ProxyConfig option - `proxy.istio.io/config` annotation for metric compression overrides Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported. The formatter option within the `spec.tracing[].customTags` field of the Telemetry custom resource (telemetry.istio.io) is unsupported. The `istiod_remote_cluster_sync_status` Prometheus gauge metric, exposed on the **Istiod control plane metrics endpoint** (port 15014 `/metrics`), is not supported. The following are unsupported for proxyless gRPC clients: - Configuring the `LEAST_REQUEST` load balancing policy within the `spec.trafficPolicy.loadBalancer.simple` field of a **DestinationRule** custom resource (`networking.istio.io`) - Configuring the `http2MaxRequests` circuit breaker within the `spec.trafficPolicy.connectionPool.http.http2MaxRequests` field of a **DestinationRule** custom resource (`networking.istio.io`) Configuring the `LEAST_REQUEST` load balancing policy within the `spec.trafficPolicy.loadBalancer.simple` field of a **DestinationRule** custom resource (`networking.istio.io`) Configuring the `http2MaxRequests` circuit breaker within the `spec.trafficPolicy.connectionPool.http.http2MaxRequests` field of a **DestinationRule** custom resource (`networking.istio.io`) The `ENABLE_AUTO_SNI` flag is still supported to keep aligned with the legacy behavior. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.29.4-asm.0 uses Envoy v1.37.4-dev. [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

**説明:** クラスタ内Cloud Service Meshの新しいバージョン1.29.4-asm.0がリリースされました。このバージョンはIstio 1.29.4の機能を基盤としていますが、特定の環境変数、ラベル、アノテーション、Istioの実験的機能、テレメトリーカスタムリソースの一部設定、特定のPrometheusメトリック、およびプロキシレスgRPCクライアントの特定のロードバランシングポリシーやサーキットブレーカー設定はサポート対象外となります。Envoyプロキシのバージョンはv1.37.4-devを使用します。
**影響有無:**
*   **影響あり（アップグレードを検討する場合）:** 現在Cloud Service Meshを使用しており、このバージョンへのアップグレードを計画している場合、既存の構成が新しいバージョンのサポート対象外機能リストに含まれていないか詳細に確認する必要があります。特に、プロキシレスgRPCクライアントを使用している場合は、記載された非サポート機能に依存していないか注意が必要です。
*   **Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3):** Google Cloud Composerは基盤となるGKEクラスタ上で動作しますが、Cloud Service Mesh（ASM）はComposerの必須コンポーネントではありません。もしユーザーがComposer環境のGKEクラスタで明示的にASMを有効化し、管理している場合は影響を受けます。一般的なComposerの利用においては、直接的な影響は低いと考えられますが、カスタムでASMを導入している場合は確認が必要です。
**対処方法:**
*   Cloud Service Meshをこのバージョンにアップグレードする前に、現在使用しているIstio/ASMの設定（環境変数、アノテーション、カスタムリソース定義など）を確認し、リリースノートに記載されている非サポート機能に該当する箇所がないか照合します。
*   非サポート機能を使用している場合は、代替策の検討または機能の調整が必要です。
*   アップグレード手順については、公式ドキュメント「Upgrade Cloud Service Mesh」を参照し、計画的に実施してください。
**用語説明:**
*   **Cloud Service Mesh (ASM):** Google Cloudが提供するマネージドなIstioサービスメッシュプラットフォームです。GKEクラスタ内でマイクロサービス間のトラフィック管理、セキュリティ、可観測性を提供します。
*   **Istio:** オープンソースのサービスメッシュ。マイクロサービスアーキテクチャでサービス間通信の管理、セキュリティ、監視を容易にします。
*   **In-cluster Cloud Service Mesh:** Cloud Service MeshのコントロールプレーンがユーザーのGKEクラスタ内にデプロイされる形態です。
*   **Envoy:** Istioがデータプレーンとして利用する高性能なエッジ/サービスプロキシです。
*   **Telemetry custom resource (telemetry.istio.io):** Istioにおけるテレメトリー（メトリクス、ログ、トレース）設定を定義するカスタムリソース定義（CRD）です。
*   **Prometheus gauge metric:** Prometheus監視システムで利用されるメトリクスタイプの一つで、現在の値を表示します。
*   **Proxyless gRPC clients:** gRPCクライアントがEnvoyプロキシを介さず、直接xDS APIから設定を取得し、ロードバランシングやルーティングを行う形態です。
*   **DestinationRule custom resource (networking.istio.io):** Istioにおけるトラフィックポリシー（ロードバランシング、サーキットブレーカーなど）を定義するカスタムリソース定義（CRD）です。
*   **LEAST_REQUEST load balancing policy:** ロードバランシングポリシーの一つで、最も少ないリクエスト数を処理しているバックエンドインスタンスにトラフィックをルーティングします。
*   **Circuit breaker:** システムの障害伝播を防ぐためのパターン。特定の条件（エラー率、同時接続数など）が満たされた場合に、一時的にリクエストを遮断する仕組みです。

---

# Cloud Service Mesh
## Announcement
**原文:** In-cluster Cloud Service Mesh 1.26 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions. [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

**説明:** クラスタ内Cloud Service Meshのバージョン1.26がサポート対象外となりました。サポートされているバージョンおよび各バージョンのサポート終了日については、Google Cloudの「Supported versions」ドキュメントを参照してください。
**影響有無:**
*   **影響あり（Cloud Service Mesh 1.26を使用している場合）:** 現在Cloud Service Mesh 1.26を使用している場合、このバージョンはもはやサポートされません。これは、セキュリティパッチの提供停止、バグ修正の停止、およびテクニカルサポートの終了を意味します。運用上のリスクやセキュリティ脆弱性の問題に直面する可能性があります。
*   **Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3):** 前述の通り、Composer自体はASMのバージョンを直接管理しません。もしユーザーがComposer環境のGKEクラスタでCloud Service Mesh 1.26を明示的に有効化している場合は、速やかなアップグレードが必要です。
**対処方法:**
*   現在Cloud Service Mesh 1.26を使用している場合は、速やかにサポート対象となっている新しいバージョン（例: 1.29.4-asm.0）へのアップグレードを計画し、実行してください。
*   アップグレードの計画には、新しいバージョンの非サポート機能リストの確認や、サービスへの影響評価を含める必要があります。
*   アップグレード手順については、Google Cloudの公式ドキュメント「Upgrade Cloud Service Mesh」を参照してください。
**用語説明:**
*   **End-of-Life (EOL):** 製品やバージョンのサポートが終了する日付。EOL以降は、セキュリティパッチ、バグ修正、およびテクニカルサポートが通常提供されなくなります。

---

# Compute Engine
## Security
**原文:** A vulnerability (CVE-2025-10263) about bypass of translation stages or GPT protections in some Arm core families was discovered and has been addressed. For more information, see the GCP-2026-036 security bulletin. [GCP-2026-036 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-036)

**説明:** 一部のArmコアファミリーにおいて、翻訳ステージまたはGPT（Granule Protection Table）保護をバイパスする脆弱性（CVE-2025-10263）が発見されましたが、Googleによって既に対処済みであることがアナウンスされています。この脆弱性に関する詳細は、GCP-2026-036セキュリティ速報で確認できます。
**影響有無:**
*   **影響なし（ユーザー側の直接的な対応は不要）:** この脆弱性はGoogle Cloudの基盤インフラストラクチャレベルで修正されており、Compute Engineを利用するユーザー側で直接的な対処は不要です。Googleがサービスプロバイダとして責任を持って修正を適用済みです。
*   **Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3):** Composer環境はCompute Engineインスタンス上で動作するため、基盤となるインフラストラクチャのセキュリティ強化はComposer環境の安定性とセキュリティ向上に寄与します。ユーザー側で特別なアクションは必要ありません。
**対処方法:**
*   Google側で既に修正が適用されているため、ユーザー側で特別な対処は不要です。
*   必要に応じて、GCP-2026-036セキュリティ速報を参照し、脆弱性の内容とGoogleの対応について理解を深めることができます。
**用語説明:**
*   **CVE (Common Vulnerabilities and Exposures):** 脆弱性に関する公開された標準識別子です。
*   **Arm core families:** ARMアーキテクチャに基づくCPUコアのシリーズで、広範囲なデバイスで使用されています。
*   **Translation stages:** CPUが仮想アドレスを物理アドレスに変換するプロセスにおける段階を指します。
*   **GPT (Granule Protection Table):** ARMv9-Aアーキテクチャで導入されたメモリ保護メカニズムで、より詳細な粒度でメモリのアクセス権限を制御します。
*   **Security bulletin:** セキュリティに関する重要な情報（脆弱性やその対策、推奨事項など）を公式に発表する文書です。
# Title: June 08, 2026 
Link: https://docs.cloud.google.com/release-notes#June_08_2026<br>
ご担当者様

Google Cloud のリリースノートに基づき、構築済みのサービスへの影響について調査結果を報告いたします。

---

# Apigee X

## Announcement
原文:
On June 8th, 2026, we released an updated version of Apigee (1-17-0-apigee-9).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
2026年6月8日に、Apigeeの更新バージョン (1-17-0-apigee-9) がリリースされました。このリリースの展開は現在進行中であり、全てのGoogle Cloudゾーンでの完了には4営業日以上かかる可能性があります。展開が完了するまでは、一部の機能や修正が利用できない場合があります。

影響有無：
影響はありません。
Apigee X はGoogle Cloudが提供するフルマネージドサービスであり、この更新はGoogle側で自動的に適用されます。既存のサービス運用に直接的な影響はありませんが、新機能や修正が環境に反映されるまでには時間差が生じる可能性があります。

対処方法：
特別な対処は不要です。展開が完了するまでお待ちください。サービス運用上の注意点として、特定の修正や新機能の利用を急ぐ場合は、展開状況を考慮する必要があります。

用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームの最新バージョン。APIの設計、セキュアな公開、運用、分析などを一元的に行える。
*   **Rollout (展開)**: ソフトウェアの新しいバージョンやパッチを本番環境に段階的に適用していくプロセス。サービスへの影響を最小限に抑えるために、ゾーンごと、リージョンごとに行われることが多い。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **514384893** | **Security fix for Apigee.** Hardened the Script policy to block server-side request forgery (SSRF) to link-local addresses. |
| **N/A** | **Security fix for Apigee infrastructure.** |

説明：
Apigeeのセキュリティ修正が行われました。
*   Bug ID 514384893: Scriptポリシーのセキュリティが強化され、リンクローカルアドレスへのサーバーサイドリクエストフォージェリ（SSRF）攻撃がブロックされるようになりました。
*   Apigeeインフラストラクチャに対するセキュリティ修正も含まれています。

影響有無：
ポジティブな影響があります。
これらの変更はセキュリティ強化であり、既存のApigee環境の脆弱性が改善されます。既存のAPIプロキシやサービスへの直接的な動作変更（Breaking Change）はなく、安全性向上に寄与します。

対処方法：
特別な対処は不要です。これらのセキュリティ修正は自動的に適用されます。

用語説明：
*   **Script policy**: ApigeeのAPIプロキシフロー内でJavaScriptコードを実行するためのポリシー。
*   **Server-Side Request Forgery (SSRF)**: サーバーがユーザーから提供されたURL（または一部）を使用して、内部リソースや外部サービスに対して意図しないリクエストを送信させられてしまう脆弱性。
*   **Link-local addresses**: 特定のローカルネットワークセグメント内でのみ有効なIPアドレス。通常、ルーターを介して他のネットワークセグメントにルーティングされることはない。

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **512850756** | Added observability metrics for the OpenTelemetry trace export pipeline, reporting spans exported, export latency, batch size, and dropped spans. |
| **515039499** | Fixed an issue where OpenTelemetry trace export over HTTP could fail to authenticate when sent through a forward proxy that requires basic authentication. |

説明：
以下の修正が行われました。
*   Bug ID 512850756: OpenTelemetryトレースエクスポートパイプラインに可観測性メトリクスが追加されました。エクスポートされたスパン数、エクスポートレイテンシ、バッチサイズ、ドロップされたスパンがレポートされます。
*   Bug ID 515039499: Basic認証を必要とするフォワードプロキシ経由でHTTP経由のOpenTelemetryトレースエクスポートを行う際に、認証に失敗する可能性があった問題が修正されました。

影響有無：
ApigeeでOpenTelemetryを利用している場合にポジティブな影響があります。
OpenTelemetryを利用していない場合は影響ありません。利用している場合は、トレースエクスポートの可観測性が向上し、認証に関する既知のバグが修正されるため、安定性と監視性が向上します。既存のワークロードに悪影響はありません。

対処方法：
特別な対処は不要です。Apigeeが自動更新されることで、これらの修正が適用されます。OpenTelemetryを利用している場合は、これらの改善を享受できます。

用語説明：
*   **OpenTelemetry**: ベンダーニュートラルなオープンソースプロジェクトで、テレメトリーデータ（メトリクス、ログ、トレース）の収集とエクスポートのためのAPI、SDK、ツールを提供する。
*   **Trace (トレース)**: 分散システムにおける単一のリクエストの実行パスを追跡するデータ構造。マイクロサービス間の呼び出しフローなどを可視化するために使用される。
*   **Span (スパン)**: トレース内の単一の操作（例えば、特定の関数の実行や外部サービスへのRPC呼び出し）を表す単位。
*   **Observability metrics (可観測性メトリクス)**: システムの内部状態を把握するための数値データ。パフォーマンス、リソース使用量、エラー率など。
*   **Forward proxy (フォワードプロキシ)**: クライアントからのリクエストをインターネット上のサーバーに転送するプロキシサーバー。クライアントからのアクセス元を匿名化したり、Webフィルタリングを行うなどの目的で利用される。

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

説明：
Cloud Service Meshの複数のバージョン (1.28.7-asm.4, 1.27.9-asm.5, 1.26.8-asm.11) に対して、セキュリティ脆弱性 [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035) の修正を含むパッチリリースが提供されました。各パッチは、対応するバージョンのEnvoyを使用しています。アップグレードに関する詳細は、提供されたドキュメントを参照してください。

影響有無：
ポジティブな影響があります。
これらのアップデートはセキュリティ脆弱性の修正であるため、既存のCloud Service Mesh環境のセキュリティが向上します。構築済みのサービスへの直接的な悪影響はありません。
ただし、**in-cluster Cloud Service Mesh (Anthos Service Mesh)** を利用している場合、これらのパッチは自動的に適用されない可能性があり、ユーザーが手動でアップグレードする必要がある場合があります。

対処方法：
ご利用のCloud Service Meshのバージョンを確認し、以下の対応を検討してください。
1.  **GCP-2026-035の評価**: まず、[GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035) のセキュリティ情報を確認し、この脆弱性がお客様の環境に与える影響度を評価してください。
2.  **アップグレードの検討**: 現在利用しているCloud Service Meshのバージョン（特にin-cluster版の場合）が、上記パッチリリースで対象となっているバージョン（1.28.x, 1.27.x, 1.26.x）であれば、速やかに当該バージョンへのアップグレードを推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) を参照してください。

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するマネージドサービスメッシュソリューション。サービスの検出、トラフィック管理、セキュリティ、可観測性などを実現する。Anthos Service Mesh (ASM) とも呼ばれる。
*   **in-cluster Cloud Service Mesh**: GKEクラスタ内にコントロールプレーンがデプロイされるタイプのCloud Service Mesh。ユーザーがコントロールプレーンの管理も一部行う必要がある。
*   **Envoy**: サービスメッシュのデータプレーンとして広く利用されている高性能なオープンソースエッジ/サービスプロキシ。

## Announcement
原文:
The rollouts previously announced on [June 3, 2026](#June_03_2026) have been stopped. The following release will supersede them and include those patches and the fix for the vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).

説明：
2026年6月3日に以前発表されたロールアウトは停止され、新しいリリースがそれらに取って代わります。この新しいリリースには、停止されたロールアウトに含まれる予定だったパッチと、セキュリティ脆弱性GCP-2026-035の修正が含まれます。

影響有無：
影響はありません。
これは、以前のリリース計画が変更され、新しいリリースに統合されることの通知です。構築済みのサービス運用に直接的な影響を与えるものではありません。

対処方法：
特別な対処は不要です。新しい統合されたリリースに含まれる修正が適用されるのを待つことになります。

---
**補足事項:**
ご質問にあったGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) については、Apigee XおよびCloud Service Meshとは直接関連するサービスではありません。したがって、今回のリリースノートによる直接的な影響はありません。

以上となります。ご不明な点がございましたら、お気軽にお問い合わせください。