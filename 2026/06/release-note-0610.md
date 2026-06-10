
# Title: June 09, 2026 
Link: https://docs.cloud.google.com/release-notes#June_09_2026<br>
Google Cloud のリリースノートに基づく影響調査の結果を以下に報告します。

---

# Cloud SDK
## Change
原文: (本文なし)

説明：
Cloud SDK に関する変更アナウンスですが、リリースノートの本文が提供されていないため、具体的な変更内容を特定できません。

影響有無：
本文が提供されていないため、変更の詳細が不明であり、影響の有無を判断できません。

対処方法：
もしこのリリースノートが公式なものであり、本文が本来存在するものであれば、具体的な変更内容を確認するために公式ドキュメントやリリースノートの完全版を参照する必要があります。変更内容が不明なため、現時点での対処は不要です。

---

# Cloud Service Mesh
## Announcement
原文: **1.29.4-asm.0 is now available for in-cluster Cloud Service Mesh.**
You can now download 1.29.4-asm.0 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.29.4 subject to the list of supported features.
[Istio 1.29.4](https://istio.io/latest/news/releases/1.29.x/announcing-1.29/)
[supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster)
The following environment variables, labels, and annotations are not supported:
- `PILOT_IGNORE_RESOURCES` and `PILOT_INCLUDE_RESOURCES`
- `RetryIgnorePreviousHosts`
- `omit_empty_values`
- `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
- `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` with the value 1
- `PILOT_DNS_JITTER_DURATION`
- `PILOT_DNS_JITTER_DURATION`
- `ENABLE_NATIVE_SIDECARS` with the value true
- `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX` and `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX`
- `PILOT_DNS_CARES_UDP_MAX_QUERIES`
- `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`
- 'BLOCKED_CIDRS_IN_JWKS_URIS`
- `ENABLE_DEBUG_ENDPOINT_AUTH`
- `DISABLE_TRACK_REMAINING_CB_METRICS`
- `gateway.istio.io/tls-cipher-suites`
- `fileFlushMinSizeKB` and `fileFlushInterval` settings in ProxyConfig
- `topology.istio.io/locality`
- `statsCompression` ProxyConfig option
- `proxy.istio.io/config` annotation for metric compression overrides

Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported.

The formatter option within the `spec.tracing[].customTags` field of the Telemetry custom resource (telemetry.istio.io) is unsupported.

The `istiod_remote_cluster_sync_status` Prometheus gauge metric, exposed on the **Istiod control plane metrics endpoint** (port 15014 `/metrics`), is not supported.

The following are unsupported for proxyless gRPC clients:
- Configuring the `LEAST_REQUEST` load balancing policy within the `spec.trafficPolicy.loadBalancer.simple` field of a **DestinationRule** custom resource (`networking.istio.io`)
- Configuring the `http2MaxRequests` circuit breaker within the `spec.trafficPolicy.connectionPool.http.http2MaxRequests` field of a **DestinationRule** custom resource (`networking.istio.io`)

Configuring the `LEAST_REQUEST` load balancing policy within the `spec.trafficPolicy.loadBalancer.simple` field of a **DestinationRule** custom resource (`networking.istio.io`)

Configuring the `http2MaxRequests` circuit breaker within the `spec.trafficPolicy.connectionPool.http.http2MaxRequests` field of a **DestinationRule** custom resource (`networking.istio.io`)

The `ENABLE_AUTO_SNI` flag is still supported to keep aligned with the legacy behavior.

For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.29.4-asm.0 uses Envoy v1.37.4-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明：
Cloud Service Mesh の新バージョン `1.29.4-asm.0` が in-cluster デプロイメント向けに利用可能になったことがアナウンスされました。このバージョンは Istio `1.29.4` をベースにしており、Envoy `v1.37.4-dev` を使用しています。
特に重要な点として、このバージョンでは多数の環境変数、ラベル、アノテーション、Istioの実験的機能、特定のテレメトリー設定、Prometheusメトリクス、およびプロキシレスgRPCクライアントの特定の機能（`LEAST_REQUEST`ロードバランシングポリシーや`http2MaxRequests`サーキットブレーカー）が**非サポート**となります。
一方、`ENABLE_AUTO_SNI` フラグは引き続きサポートされます。アップグレードの詳細については、提供されているドキュメントを参照するよう促されています。

影響有無：
*   **直接的な影響**: なし。これは新しいバージョンの提供開始のアナウンスであり、既存の稼働中のCloud Service Mesh環境が自動的にこのバージョンにアップグレードされることはありません。
*   **間接的な影響**: Cloud Service Mesh を利用しており、将来的にこのバージョン (`1.29.4-asm.0`) へのアップグレードを計画している場合、現状のデプロイメントが非サポートとなる機能や設定を使用していないか確認が必須です。もし使用している場合は、アップグレード後にそれらの機能が動作しなくなる可能性があります。

対処方法：
1.  **アップグレード計画の確認**: 現在利用しているCloud Service Meshのバージョンと、`1.29.4-asm.0` へのアップグレード計画の有無を確認します。
2.  **既存設定の評価**: アップグレードを検討する場合、現在のIstio/Cloud Service Meshの設定（Kubernetes Deployment, ConfigMap, DestinationRule, Telemetry CRなど）を詳細にレビューし、リリースノートに明記されている非サポートの環境変数、ラベル、アノテーション、機能が利用されていないかを確認してください。
3.  **非サポート機能の代替策検討**: もし非サポートとなる機能が利用されている場合は、代替機能の有無、設定の変更、またはアップグレード計画の見直しを検討する必要があります。
4.  **ドキュメント参照**: 公式のアップグレードドキュメント (`Upgrade Cloud Service Mesh`) を参照し、推奨されるアップグレード手順と注意点を確認の上、慎重にアップグレード計画を立案・実行してください。

用語説明：
*   **Istio**: サービスメッシュを導入するためのオープンソースプラットフォーム。トラフィック管理、ポリシー適用、テレメトリー収集などの機能を提供します。
*   **in-cluster Cloud Service Mesh**: GKEクラスタ内に直接デプロイされるCloud Service Meshの運用モデル。
*   **Envoy**: Istioのデータプレーンとして機能する高性能なオープンソースのプロキシサーバー。サイドカーとしてアプリケーションコンテナと共にデプロイされ、トラフィックのルーティングやポリシー適用を行います。
*   **DestinationRule**: Istioのカスタムリソースの一つで、サービスへのトラフィックのルーティング方法、ロードバランシングアルゴリズム、サーキットブレーカーなどの動作を定義します。
*   **Telemetry custom resource**: Istioのカスタムリソースの一つで、メトリクス、ロギング、トレーシングなどのテレメトリー収集に関する設定を定義します。
*   **Prometheus gauge metric**: Prometheusが収集するメトリクスの一種で、現在の値（例: キューのサイズや温度）を示すメトリクスタイプです。
*   **proxyless gRPC clients**: 通常のサイドカープロキシ（Envoyなど）を介さずに、直接Istioコントロールプレーンと通信するgRPCクライアント。

---

# Cloud Service Mesh
## Announcement
原文: In-cluster Cloud Service Mesh 1.26 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.
[Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

説明：
in-cluster Cloud Service Mesh のバージョン `1.26` のサポートが終了したことがアナウンスされました。他のバージョンのサポート終了日を確認するためには、関連する「Supported versions」ドキュメントを参照するよう促されています。

影響有無：
*   **直接的な影響**: 現在、in-cluster Cloud Service Mesh バージョン `1.26` を利用している場合、重大な影響があります。サポートが終了したため、セキュリティパッチ、バグ修正、および技術サポートが今後提供されなくなります。これにより、運用リスクやセキュリティリスクが増大します。
*   **間接的な影響**: 1.26以外のバージョンを使用している場合は直接的な影響はありませんが、利用中のバージョンのサポート状況を定期的に確認することの重要性を示唆しています。

対処方法：
1.  **バージョン確認**: 現在のCloud Service Meshのバージョンが `1.26` であるかを確認してください。
2.  **直ちにアップグレード計画**: もしバージョンが `1.26` であった場合、直ちにサポートされている最新バージョン（例: 上記アナウンスされた `1.29.4-asm.0` など）へのアップグレード計画を立案・実行する必要があります。
3.  **アップグレード時の考慮事項**: アップグレード時には、新しいバージョンで非推奨または非サポートとなる機能や設定変更がないか、事前に確認し、既存の設定が適切に動作するように調整する必要があります。アップグレードガイドラインを厳守し、十分なテストを実施してください。

用語説明：
*   **EOL (End-of-Life)**: 製品またはサービスのライフサイクルにおける最終段階で、通常はサポート、アップデート、修正が提供されなくなる日付を指します。

---

# Compute Engine
## Security
原文: A vulnerability (CVE-2025-10263) about bypass of translation stages or GPT protections in some Arm core families was discovered and has been addressed.
For more information, see the GCP-2026-036 security bulletin.
[GCP-2026-036 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-036)

説明：
一部のArmコアファミリーにおける、メモリ変換ステージまたはGPT (General Purpose Translation) 保護のバイパスに関する脆弱性 (`CVE-2025-10263`) が発見されましたが、Google Cloud側で既に対処済みであることがアナウンスされました。詳細はGCPセキュリティ速報 `GCP-2026-036` を参照するよう促されています。

影響有無：
*   **直接的な影響**: なし。この脆弱性はGoogle Cloudの基盤レベルで修正が適用されており、ユーザー側でCompute Engineインスタンスに対して直接的なアクション（例: パッチ適用、設定変更）を行う必要はありません。
*   **間接的な影響**: Google Cloudのインフラストラクチャにおけるセキュリティが強化されたことを意味します。ユーザーはより安全な環境でCompute Engineインスタンスを運用できます。

対処方法：
ユーザー側で実施すべき直接的な対処はありません。Google Cloudが提供するインフラレベルのセキュリティ対策によって、この脆弱性から保護されています。
しかし、これはOSやアプリケーションレベルの脆弱性対策とは別であるため、引き続き利用中のOSやアプリケーションのセキュリティパッチ適用、脆弱性管理は継続して実施することが重要です。GCPセキュリティ速報は定期的に確認し、自身の環境に関連する情報に注意を払うことを推奨します。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 共通脆弱性識別子。公開されている既知のサイバーセキュリティ脆弱性を一意に識別するための国際標準の識別子です。
*   **Arm core families**: Arm社が設計するCPUアーキテクチャのファミリー。スマートフォン、IoTデバイス、サーバーなど、広範囲なデバイスで使用されています。
*   **Translation stages / GPT protections**: Armアーキテクチャのメモリ管理ユニット (MMU) におけるページテーブル変換ステージや、汎用変換（General Purpose Translation: GPT）に関連する保護機構を指します。これらの機構は、メモリへの不正アクセスを防ぎ、システムの安定性とセキュリティを確保するために重要です。
# Title: June 08, 2026 
Link: https://docs.cloud.google.com/release-notes#June_08_2026<br>
Google Cloudインフラエンジニアとして、ご提示いただいたリリースノートについて、構築済みのサービスへの影響有無を調査いたしました。

---

# Apigee X

## Announcement
原文: On June 8th, 2026, we released an updated version of Apigee (1-17-0-apigee-9).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.
説明: Apigee Xの新しいバージョン `1-17-0-apigee-9` が2026年6月8日にリリースされました。このロールアウトは本日（リリースノート発行日）開始され、全てのGoogle Cloudゾーンでの完了には4営業日以上かかる可能性があります。ロールアウトが完了するまでは、ご利用のインスタンスで新機能や修正が利用できない場合があります。
影響有無: **有**。 ApigeeサービスはGoogle Cloudによって自動的に最新バージョンにアップデートされます。このロールアウト期間中は、新バージョンが適用されていないインスタンスと混在する可能性があるため、サービスの一貫性に影響がないか監視することが推奨されます。ただし、お客様側での積極的な操作は不要です。
対処方法: 特段の操作は不要です。ロールアウト期間中に特定の機能の動作確認を行う場合は、インスタンスのバージョンが更新されているかを確認することを推奨します。
用語説明:
*   **ロールアウト (Rollout)**: ソフトウェアや機能が段階的に展開され、全てのユーザーやシステムに適用されるプロセスです。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **514384893** | **Security fix for Apigee.** Hardened the Script policy to block server-side request forgery (SSRF) to link-local addresses. |
説明: ApigeeのScriptポリシーにおいて、サーバーサイドリクエストフォージェリ（SSRF）攻撃を防ぐためのセキュリティ強化が実施されました。具体的には、リンクローカルアドレス（例: メタデータサーバーアドレス）へのリクエストがブロックされるよう、ポリシーが強化されました。
影響有無: **有**。セキュリティ強化のため、既存のScriptポリシーで意図的にリンクローカルアドレスへのリクエストを行っている場合、その動作に影響が出る可能性があります。しかし、通常はこのようなリクエストはセキュリティリスクとなるため、多くの場合はポジティブな影響（セキュリティ向上）となります。
対処方法: ご利用のApigee Scriptポリシーにおいて、リンクローカルアドレス（例: `169.254.169.254` のCompute Engineメタデータサービスなど）へのリクエストを明示的に行っている場合は、動作確認を実施し、必要に応じて代替手段の検討やポリシーの修正を検討してください。
用語説明:
*   **サーバーサイドリクエストフォージェリ (SSRF)**: 攻撃者がサーバーをだまして、攻撃者が制御できない内部リソース（例: イントラネット内のサーバー、クラウドのメタデータサービスなど）にリクエストを送信させる攻撃手法です。
*   **リンクローカルアドレス**: 同じネットワークセグメント内でのみ有効なIPアドレス範囲です。IPv4では `169.254.0.0/16` が代表的です。Google CloudのCompute Engineのメタデータサーバーは、この範囲の `169.254.169.254` でアクセスされます。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **N/A** | **Security fix for Apigee infrastructure.** |
説明: Apigeeの基盤インフラストラクチャに対するセキュリティ修正が適用されました。具体的な内容は非公開ですが、Apigeeサービスを支える基盤のセキュリティが強化されたことを意味します。
影響有無: **無**。ユーザーが直接操作する部分ではなく、Google Cloudが管理するApigeeサービス基盤のセキュリティ強化であるため、既存のサービス動作に直接的な影響はありません。セキュリティが向上するというポジティブな影響が期待されます。
対処方法: 不要です。
用語説明:
*   **インフラストラクチャ**: コンピューティング、ストレージ、ネットワークなどのITサービスを支える基盤となるハードウェアおよびソフトウェア構成全体を指します。

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **512850756** | Added observability metrics for the OpenTelemetry trace export pipeline, reporting spans exported, export latency, batch size, and dropped spans. |
説明: OpenTelemetryトレースエクスポートパイプラインに、新たな可観測性メトリクスが追加されました。これにより、エクスポートされたスパンの数、エクスポートの遅延、バッチサイズ、および破棄されたスパンに関する詳細な情報がレポートされるようになります。
影響有無: **無**。機能追加であり、既存の動作に影響を与えるものではありません。OpenTelemetryを利用している場合、トレーシングの状況をより詳細に把握できるようになるため、モニタリングの向上が期待されます。
対処方法: 不要です。追加されたメトリクスを活用したい場合は、Cloud Monitoringなどのモニタリングシステムでの表示設定を確認してください。
用語説明:
*   **OpenTelemetry**: 分散トレーシング、メトリクス、ロギングなどのオブザーバビリティデータを収集・エクスポートするためのオープンソースフレームワークです。
*   **トレース (Trace)**: 分散システムにおける単一のリクエストのライフサイクル全体を追跡するためのデータセットです。
*   **スパン (Span)**: トレース内で実行される単一の操作または処理ステップを表すデータの単位です。
*   **可観測性メトリクス (Observability Metrics)**: システムの内部状態やパフォーマンスを推測・監視するために収集される測定値の集合です。

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **515039499** | Fixed an issue where OpenTelemetry trace export over HTTP could fail to authenticate when sent through a forward proxy that requires basic authentication. |
説明: HTTP経由でOpenTelemetryトレースをエクスポートする際に、基本認証を必要とするフォワードプロキシを経由した場合に認証が失敗する問題が修正されました。
影響有無: **無**。バグ修正であり、OpenTelemetryトレースエクスポートをフォワードプロキシ経由で基本認証を利用して行っていた場合に発生していた特定の認証問題が解消されます。これに該当しない環境では影響はありません。
対処方法: 不要です。もし該当する環境でこれまで認証エラーに遭遇していた場合は、今回の修正によって問題が解消されている可能性がありますので、改めて動作確認を行うことを推奨します。
用語説明:
*   **フォワードプロキシ (Forward Proxy)**: クライアントからのリクエストを仲介し、代理でインターネット上のリソースにアクセスするサーバーです。通常、社内ネットワークから外部へのアクセス制御やキャッシュのために使用されます。
*   **基本認証 (Basic Authentication)**: HTTPにおいて、ユーザー名とパスワードをBase64エンコードしてAuthorizationヘッダーに含める、最も基本的な認証方式です。

---

# Cloud Service Mesh

## Security
原文: **1.28.7-asm.4 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.28.7-asm.4 uses Envoy v1.36.8-dev.
説明: クラスタ内Cloud Service Mesh向けにバージョン `1.28.7-asm.4` がリリースされました。このパッチリリースには、セキュリティ脆弱性 `GCP-2026-035` の修正が含まれています。このバージョンではEnvoy `v1.36.8-dev` が使用されています。
影響有無: **有**。セキュリティ脆弱性の修正が含まれるため、このバージョン系統（1.28系）をご利用の場合、このバージョンへのアップグレードを強く推奨します。アップグレードにより、既存のCloud Service Meshの動作環境が変更される可能性があります。
対処方法: Cloud Service Meshのアップグレード手順に従い、本バージョン(`1.28.7-asm.4`)へのアップグレードを計画・実施してください。アップグレード前に、リリースノートおよび関連する変更点を確認し、既存のワークロードへの影響を評価することが重要です。
用語説明:
*   **Cloud Service Mesh**: Google Cloudが提供するIstioベースのマネージドサービスメッシュソリューションです。
*   **パッチリリース (Patch Release)**: 主にバグ修正やセキュリティアップデートを含む、既存のソフトウェアバージョンのマイナーアップデートです。
*   **セキュリティ脆弱性**: ソフトウェアの設計上または実装上の欠陥で、攻撃者によって悪用されるとシステムの機密性、完全性、可用性が損なわれる可能性があるものです。
*   **Envoy**: クラウドネイティブなプロキシおよびサービスメッシュのために設計された高性能なオープンソースのエッジ/サービスプロキシです。

## Security
原文: **1.27.9-asm.5 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.5 uses Envoy v1.35.12-dev.
説明: クラスタ内Cloud Service Mesh向けにバージョン `1.27.9-asm.5` がリリースされました。このパッチリリースには、セキュリティ脆弱性 `GCP-2026-035` の修正が含まれています。このバージョンではEnvoy `v1.35.12-dev` が使用されています。
影響有無: **有**。セキュリティ脆弱性の修正が含まれるため、このバージョン系統（1.27系）をご利用の場合、このバージョンへのアップグレードを強く推奨します。アップグレードにより、既存のCloud Service Meshの動作環境が変更される可能性があります。
対処方法: Cloud Service Meshのアップグレード手順に従い、本バージョン(`1.27.9-asm.5`)へのアップグレードを計画・実施してください。アップグレード前に、リリースノートおよび関連する変更点を確認し、既存のワークロードへの影響を評価することが重要です。
用語説明: 上記「Cloud Service Mesh - Security (1.28.7-asm.4)」と同様です。

## Security
原文: **1.26.8-asm.11 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.11 uses Envoy v1.34.14.
説明: クラスタ内Cloud Service Mesh向けにバージョン `1.26.8-asm.11` がリリースされました。このパッチリリースには、セキュリティ脆弱性 `GCP-2026-035` の修正が含まれています。このバージョンではEnvoy `v1.34.14` が使用されています。
影響有無: **有**。セキュリティ脆弱性の修正が含まれるため、このバージョン系統（1.26系）をご利用の場合、このバージョンへのアップグレードを強く推奨します。アップグレードにより、既存のCloud Service Meshの動作環境が変更される可能性があります。
対処方法: Cloud Service Meshのアップグレード手順に従い、本バージョン(`1.26.8-asm.11`)へのアップグレードを計画・実施してください。アップグレード前に、リリースノートおよび関連する変更点を確認し、既存のワークロードへの影響を評価することが重要です。
用語説明: 上記「Cloud Service Mesh - Security (1.28.7-asm.4)」と同様です。

## Announcement
原文: The rollouts previously announced on [June 3, 2026](#June_03_2026) have been stopped. The following release will supersede them and include those patches and the fix for the vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).
説明: 2026年6月3日に以前アナウンスされたロールアウトは停止されました。今回のリリース（上記で説明された各バージョン）がそれらに取って代わり、以前のパッチとセキュリティ脆弱性 `GCP-2026-035` の修正が含まれています。
影響有無: **無**。以前のロールアウトが停止され、今回のリリースに統合されたことを示すアナウンスであり、ユーザーの既存環境に直接的な影響はありません。これは情報の明確化であり、混乱を避けるための措置です。
対処方法: 特段の操作は不要です。最新のセキュリティ修正を含む上記の各パッチリリースへのアップグレードを計画・実施してください。
用語説明:
*   **supersede (取って代わる)**: 以前のものを廃止し、新しいものがその代わりとなることを意味します。

---