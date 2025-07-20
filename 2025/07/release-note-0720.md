
# Title: July 16, 2025 
Link: https://cloud.google.com/release-notes#July_16_2025<br>
# Cloud Service Mesh
## Announcement
原文: **1.26.0-asm.11 is now available for in-cluster Cloud Service Mesh.**
 You can now download 1.26.0-asm.11 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.26.0 subject to the list of supported features.
[Istio 1.26.0](https://istio.io/latest/news/releases/1.26.x/announcing-1.26/)
[supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster)
 The following environment variables and annotations are not supported:

- `ENABLE_GATEWAY_API_MANUAL_DEPLOYMENT`
- `RETRY_IGNORE_PREVIOUS_HOSTS`
- `ENABLE_CLUSTER_TRUST_BUNDLE_API`
- `OMIT_EMPTY_VALUES`
- `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
- `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` with the value 1
- Referencing ConfigMaps in a DestinationRule with TLS mode set to SIMPLE mode is not supported

 The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with the legacy behavior.

 For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.26.0-asm.11 uses Envoy v1.34.2-dev.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)
説明: Cloud Service Mesh の新しいバージョン `1.26.0-asm.11` が利用可能になりました。このバージョンには Istio 1.26.0 の機能が含まれていますが、一部の環境変数、アノテーション、および `DestinationRule` における `SIMPLE` モードでの `ConfigMap` 参照はサポートされません。また、`ENABLE_AUTO_SNI` フラグは引き続きサポートされます。
影響有無: 現在 `1.26.0-asm.11` よりも古いバージョンの Cloud Service Mesh を利用している場合、アップグレードを検討すべきです。特に、サポート対象外となった環境変数、アノテーション、または `DestinationRule` での `ConfigMap` 参照を使用している場合は、アップグレードによって既存の構成に影響が出る可能性があります。
対処方法: アップグレードを計画し、事前にサポート対象外となった機能（環境変数、アノテーション、DestinationRuleでのConfigMap参照）が現在の環境で利用されていないか確認してください。利用されている場合は、代替手段への移行を検討してください。
用語説明:
*   **Cloud Service Mesh**: Google Cloudが提供するマネージドなサービスメッシュソリューションで、オープンソースのIstioをベースにしています。
*   **Istio**: マイクロサービス間のトラフィック管理、セキュリティ、可観測性を提供するオープンソースのサービスメッシュプラットフォームです。
*   **Envoy**: Istioで使用される高性能なプロキシで、サービスメッシュ内のすべてのインバウンドおよびアウトバウンドトラフィックを仲介します。
*   **環境変数 (Environment Variables)**: プログラムの実行環境に設定される動的な名前付きの値です。
*   **アノテーション (Annotations)**: Kubernetesリソースに付加するメタデータで、非識別的な情報を保持します。
*   **DestinationRule**: Istioで、特定のサービスへのトラフィックのルーティング方法やポリシー（ロードバランシング、コネクションプール、TLS設定など）を定義するリソースです。
*   **TLSモード**: Transport Layer Security (TLS) の接続モード（例: `SIMPLE` はクライアントが証明書を提示しない一方向TLS）。
*   **ConfigMap**: Kubernetesで、アプリケーションが利用する設定データをキーバリューペアとして保存するためのリソースです。

## Announcement
原文: In-cluster Cloud Service Mesh 1.23 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.
[Supported versions](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)
説明: Cloud Service Mesh のバージョン `1.23` のサポートが終了しました。
影響有無: 現在 Cloud Service Mesh バージョン `1.23` を利用している場合、ベンダーサポート（セキュリティパッチ、バグ修正、技術サポートなど）が提供されなくなるため、早急にサポートされているバージョンへのアップグレードが必要です。
対処方法: サポートされている最新バージョンへのアップグレードを直ちに計画し、実行してください。
用語説明:
*   **サポート終了 (End-of-Life, EOL)**: 製品やバージョンのライフサイクルが終了し、ベンダーからの公式サポート（セキュリティアップデート、バグ修正、技術サポートなど）が提供されなくなる状態を指します。

## Announcement
原文: **1.25.3-asm.11 is now available for in-cluster Cloud Service Mesh.**
 You can now download 1.25.3-asm.11 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.25.3 subject to the list of supported features. Cloud Service Mesh version 1.25.3-asm.11 uses envoy v1.33.4-dev.
[Istio 1.25.3](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.3/)
[supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster)
 For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh.
[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade)
説明: Cloud Service Mesh の新しいバージョン `1.25.3-asm.11` が利用可能になりました。このバージョンには Istio 1.25.3 の機能が含まれ、Envoy v1.33.4-dev を使用しています。
影響有無: 現在 `1.25.3-asm.11` よりも古いバージョンの Cloud Service Mesh を利用している場合、アップグレードを検討すべきです。アップグレードにより、Istio 1.25.3で導入された新機能や改善、セキュリティ修正の恩恵を受けることができます。
対処方法: アップグレードを計画し、リリースノートとサポート対象機能を確認した上で適用してください。
用語説明:
*   **Istio**: 前述参照。
*   **Envoy**: 前述参照。

## Announcement
原文: **1.24.6-asm.9 is now available for in-cluster Cloud Service Mesh.**
 You can now download 1.24.6-asm.9 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.24.6 subject to the list of supported features. Cloud Service Mesh version 1.24.6-asm.9 uses envoy v1.32.7-dev.
[Istio 1.24.6](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.6/)
[supported features](https://cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster)
 For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh.
[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade)
説明: Cloud Service Mesh の新しいバージョン `1.24.6-asm.9` が利用可能になりました。このバージョンには Istio 1.24.6 の機能が含まれ、Envoy v1.32.7-dev を使用しています。
影響有無: 現在 `1.24.6-asm.9` よりも古いバージョンの Cloud Service Mesh を利用している場合、アップグレードを検討すべきです。アップグレードにより、Istio 1.24.6で導入された新機能や改善、セキュリティ修正の恩恵を受けることができます。
対処方法: アップグレードを計画し、リリースノートとサポート対象機能を確認した上で適用してください。
用語説明:
*   **Istio**: 前述参照。
*   **Envoy**: 前述参照。

# Google Kubernetes Engine
## Changed
原文: GKE cluster versions have been updated.
 **New versions available for upgrades and new clusters.**
 The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see GKE versioning and support
and Upgrades.
[GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
[Upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
説明: GKEクラスタのバージョンが更新され、新しいKubernetesバージョンが新規クラスタの作成および既存クラスタのコントロールプレーンとノードのアップグレードで利用可能になりました。
影響有無: 直接的な影響はありません。既存のGKEクラスタは自動的にアップグレードされるわけではありませんが、最新のバージョンを利用することで、新機能、セキュリティパッチ、パフォーマンス改善の恩恵を受けることができます。Google Cloud Composer 2はGKE上で動作するため、GKEの基盤バージョンを最新に保つことは、Composer環境の安定性とセキュリティにも寄与します。ただし、ComposerがサポートするGKEバージョン範囲を確認し、互換性を維持する必要があります。
対処方法: GKEクラスタのアップグレード計画を立て、テスト環境で十分な検証を行った上で本番環境に適用することを推奨します。Google Cloud Composerのドキュメントを参照し、ComposerがサポートするGKEバージョンとの互換性を確認してください。
用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービスです。
*   **Kubernetes**: コンテナ化されたワークロードとサービスを管理するためのオープンソースのオーケストレーションシステムです。
*   **コントロールプレーン**: Kubernetesクラスタの管理層で、APIサーバー、スケジューラー、コントローラーマネージャーなどが含まれます。
*   **ノード**: コンテナ化されたアプリケーションを実行するワーカーマシン（VMまたは物理マシン）です。

## Changed
原文: To enable upcoming support for mTLS and client certificates, Google Front Ends
(GFEs) that power GKE DNS-based control plane public endpoints will add client
certificate requests during the TLS handshake. Requests are already incorporated
into GKE DNS-based control plane public endpoints where hostnames end with
`us-central1.gke.goog`. For all other GKE DNS-based control plane public
endpoints, this will roll out between August 18, 2025 and August 22, 2025.

 Until mTLS and client certificate configuration options are available, the
following details apply:

- A client certificate request in a TLS handshake *doesn't* mean that `kubectl`
(or other compatible clients) must provide a client certificate. Client
certificates are neither mandatory nor configurable.
- TLS libraries in current operating systems send a "no client certificate"
response to the public endpoint's client certificate request.
- GKE DNS-based control plane public endpoints will **not** enforce client
certificates or mTLS requirements until a future announcement about
configuration options.

 If you use an intermediate proxy between `kubectl` (or other compatible
clients) and a GKE DNS-based control plane public endpoint, ensure that it fully
adheres to
Section 7.4.4 of RFC 5246,
Section 4.4.2 of RFC 8446,
or
Section 4.4.2.4 of RFC 8446.
説明: 将来的なmTLSおよびクライアント証明書のサポート準備として、GKEのDNSベースのコントロールプレーン公開エンドポイント（`us-central1.gke.goog` で終わるホスト名のエンドポイントは既に、その他のエンドポイントは2025年8月18日〜22日の間に順次）が、TLSハンドシェイク時にクライアント証明書のリクエストを追加するようになります。現時点ではクライアント証明書の提供は必須ではなく、設定オプションが利用可能になるまでは強制されません。
影響有無:
*   **直接的な影響は低い**: 現時点ではクライアント証明書の提示は強制されないため、通常の `kubectl` や互換クライアントの動作には影響しません。
*   **間接的な影響**: `kubectl` とGKEコントロールプレーンの間に中間プロキシ（例：セキュリティアプライアンス、カスタムロードバランサー）を使用している場合、そのプロキシがRFCで定義されているTLSプロトコル（特にクライアント証明書要求のハンドリング）に完全に準拠しているか確認する必要があります。準拠していない場合、将来的に問題が発生する可能性があります。
対処方法:
*   中間プロキシを使用している場合は、プロキシがTLSハンドシェイクのクライアント証明書要求処理に関してRFC 5246 Section 7.4.4、RFC 8446 Section 4.4.2、またはRFC 8446 Section 4.4.2.4に準拠していることを確認してください。
*   今後のmTLSおよびクライアント証明書の設定オプションに関するアナウンスに注意を払ってください。
用語説明:
*   **mTLS (mutual TLS)**: クライアントとサーバーの両方が証明書を提示し、相互に認証を行うTLSの形態です。
*   **クライアント証明書**: クライアントが自身の身元をサーバーに証明するために提示するデジタル証明書です。
*   **TLSハンドシェイク**: クライアントとサーバーがセキュアな通信を開始する前に、暗号化パラメータや認証を行う一連のプロセスです。
*   **Google Front Ends (GFEs)**: Googleのグローバルネットワークエッジに配置されたプロキシサーバー群で、Googleのサービスへのトラフィックを処理します。
*   **RFC (Request for Comments)**: インターネット技術の標準を定義する文書群です。

## Changed
原文: (2025-R30) Version updates
> **Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

- The following versions are now available in the Extended channel:

- 1.28.15-gke.2475000
- 1.29.15-gke.1639000
- 1.30.12-gke.1333000
- 1.31.10-gke.1021000
- 1.32.6-gke.1013000
- 1.33.2-gke.1111000
説明: GKE Extendedチャネルで、以下の新しいKubernetesバージョンが利用可能になりました。
影響有無: 直接的な影響はありません。これらのバージョンはアップグレード時に選択できるようになったものであり、既存のクラスタに自動的に適用されるわけではありません。Extendedチャネルを使用しているクラスタは、新しいバージョンへのアップグレードを検討することで、セキュリティパッチや改善の恩恵を受けられます。Google Cloud Composer 2はGKE上で動作するため、GKEの基盤バージョンを最新に保つことは、Composer環境の安定性とセキュリティにも寄与しますが、ComposerがサポートするGKEバージョン範囲と互換性を確認する必要があります。
対処方法: 現在GKEクラスタでExtendedチャネルを利用している場合、これらの新しいバージョンへのアップグレードを計画し、テスト環境で十分な検証を行った上で本番環境に適用してください。Google Cloud Composerのサポートドキュメントで互換性を確認してください。
用語説明:
*   **リリースチャネル**: GKEのバージョンアップグレードの頻度や安定性レベルを制御する設定です（例：Extended, Rapid, Regular, Stable）。Extendedチャネルは長期的な安定性を重視し、リリースサイクルが長めです。

## Changed
原文: (2025-R30) Version updates
> **Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

- The following versions are now available:

- 1.30.12-gke.1372000
- 1.31.10-gke.1067000
- 1.32.6-gke.1060000
- 1.33.2-gke.1384000

- The following node versions are now available:

- 1.28.15-gke.2475000
- 1.29.15-gke.1639000
- 1.30.12-gke.1372000
- 1.31.10-gke.1067000
- 1.32.6-gke.1060000
- 1.33.2-gke.1384000
説明: GKEで、以下の新しいKubernetesバージョン（コントロールプレーンとノード）が利用可能になりました。
影響有無: 直接的な影響はありません。これらのバージョンはアップグレード時に選択できるようになったものであり、既存のクラスタに自動的に適用されるわけではありません。新しいバージョンへのアップグレードを検討することで、セキュリティパッチや改善の恩恵を受けられます。Google Cloud Composer 2はGKE上で動作するため、GKEの基盤バージョンを最新に保つことは、Composer環境の安定性とセキュリティにも寄与しますが、ComposerがサポートするGKEバージョン範囲と互換性を確認する必要があります。
対処方法: 現在GKEクラスタを利用している場合、これらの新しいバージョンへのアップグレードを計画し、テスト環境で十分な検証を行った上で本番環境に適用してください。Google Cloud Composerのサポートドキュメントで互換性を確認してください。

## Changed
原文: (2025-R30) Version updates
> **Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

- The following versions are now available in the Rapid channel:

- 1.30.12-gke.1372000
- 1.31.10-gke.1067000
- 1.32.6-gke.1060000
- 1.33.2-gke.1384000
説明: GKE Rapidチャネルで、以下の新しいKubernetesバージョンが利用可能になりました。
影響有無: 直接的な影響はありません。これらのバージョンはアップグレード時に選択できるようになったものであり、既存のクラスタに自動的に適用されるわけではありません。Rapidチャネルを使用しているクラスタは、新しいバージョンへのアップグレードを検討することで、最新の機能や改善を早期に利用できます。Google Cloud Composer 2はGKE上で動作するため、GKEの基盤バージョンを最新に保つことは、Composer環境の安定性とセキュリティにも寄与しますが、ComposerがサポートするGKEバージョン範囲と互換性を確認する必要があります。
対処方法: 現在GKEクラスタでRapidチャネルを利用している場合、これらの新しいバージョンへのアップグレードを計画し、テスト環境で十分な検証を行った上で本番環境に適用してください。Google Cloud Composerのサポートドキュメントで互換性を確認してください。
用語説明:
*   **リリースチャネル**: 前述参照。Rapidチャネルは最新の機能や改善をいち早く提供しますが、リリース頻度が高く、比較的新しい機能が含まれるため、十分なテストが必要です。

## Changed
原文: (2025-R30) Version updates
> **Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

- The following versions are now available in the Regular channel:

- 1.30.12-gke.1333000
- 1.31.10-gke.1021000
- 1.32.6-gke.1013000
- 1.33.2-gke.1111000
説明: GKE Regularチャネルで、以下の新しいKubernetesバージョンが利用可能になりました。
影響有無: 直接的な影響はありません。これらのバージョンはアップグレード時に選択できるようになったものであり、既存のクラスタに自動的に適用されるわけではありません。Regularチャネルを使用しているクラスタは、新しいバージョンへのアップグレードを検討することで、セキュリティパッチや改善の恩恵を受けられます。Google Cloud Composer 2はGKE上で動作するため、GKEの基盤バージョンを最新に保つことは、Composer環境の安定性とセキュリティ