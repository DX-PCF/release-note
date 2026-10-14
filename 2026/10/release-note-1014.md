
# Title: October 13, 2026 
Link: https://docs.cloud.google.com/release-notes#October_13_2026<br>
ご提供いただいた情報には、`# Cloud SDK` の `## Breaking` カテゴリに該当する具体的なリリースノートの原文が含まれていません。

リリースノートの原文がないため、変更内容の詳細な説明、お客様の環境への影響有無、具体的な対処方法、および関連する用語の説明を生成することができません。

恐れ入りますが、Cloud SDK の `Breaking` 変更に関するリリースノートの原文をご提供いただけますでしょうか。原文をご提供いただければ、ご要望の形式で回答を作成いたします。
# Title: October 12, 2026 
Link: https://docs.cloud.google.com/release-notes#October_12_2026<br>
Google Cloud インフラエンジニアとして、ご提供いただいたリリースノートに基づき、Cloud Service Mesh の影響について調査結果を報告します。

---

# Cloud Service Mesh

## Announcement

原文: **1.31.1-asm.16 is now available for in-cluster Cloud Service Mesh.**
You can now download 1.31.1-asm.16 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.31.1 subject to the list of supported features.
[Istio 1.31.1](https://istio.io/latest/news/releases/1.31.x/announcing-1.31/)
[supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster)
The following are not supported:
- `PILOT_NODE_UNTAINT_CONTROLLERS_TAINT_NAME`
- `prefix_rewrite` field in `HTTPRedirect`
- `ALLOW_ANY_DYNAMIC_DNS` in `outboundTrafficPolicy`
- `connectionSettings` in `ProxyConfig`
- `defaultTrafficPolicy` in `MeshConfig`
- `zoneAwareLbSetting` in `DestinationRule` and `MeshConfig`
- `trustDomains` and `notTrustDomains` fields in `source` field of `AuthorizationPolicy`
- `fips-140-3` for the `COMPLIANCE_POLICY`
- `PILOT_ENABLE_REMOTE_CREDENTIALS_CONTROLLER`
- External SDS provider for gateways
- `PILOT_AGENT_MERGE_ENVOY_STATS`
- `prometheus.istio.io/scrape-targets`
- `ENVOY_SECURE_METRICS_PORT` and `ENVOY_SECURE_MERGED_METRICS_PORT`
- `istioctl manifest generate` with `-o/--output`
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.31.1-asm.16 uses Envoy v1.39.3.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明:
インクラスタ型Cloud Service Meshの最新バージョン `1.31.1-asm.16` がリリースされました。このバージョンにはIstio 1.31.1の機能が含まれており、Envoyプロキシは `v1.39.3` を使用します。
重要な点として、いくつかの機能がこのバージョンではサポート対象外であることが明記されています。これには、HTTPRedirectの`prefix_rewrite`フィールド、ProxyConfigの`connectionSettings`、MeshConfigの`defaultTrafficPolicy`などが含まれます。

影響有無:
*   **影響あり（要確認）**: 現在Cloud Service Meshをご利用の場合、このバージョンへのアップグレードを検討する際に、既存のIstio設定でサポート対象外となった機能を使用していないか確認が必要です。もし使用している場合、機能の動作変更や設定の再検討が必要になります。
*   **影響なし（ただしメリットあり）**: 現在Cloud Service Meshを導入していない場合や、古いバージョンをご利用の場合、このバージョンを利用することでIstio 1.31.1の新機能や改善の恩恵を受けられます。ただし、上述の非サポート機能に依存する設定は避けるべきです。パフォーマンスや安定性向上も期待できます。

対処方法:
1.  現在利用中のCloud Service Meshのバージョンを確認してください。
2.  `1.31.1-asm.16` へのアップグレードを検討する場合、既存のIstio設定（特に`HTTPRedirect`、`ProxyConfig`、`MeshConfig`、`DestinationRule`、`AuthorizationPolicy`）を確認し、リリースノートに記載されているサポート対象外の機能を使用していないか確認してください。
3.  サポート対象外の機能を使用している場合は、代替手段の検討または設定の変更を計画してください。
4.  アップグレード手順の詳細は、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) ドキュメントを参照し、計画的に実施してください。

## Announcement

原文: **1.30.5-asm.8 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.30.5-asm.8 uses Envoy v1.38.7-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)
This release resolves the security vulnerability listed in Security Bulletin GCP-2026-067.
[GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067)

説明:
インクラスタ型Cloud Service Meshのバージョン `1.30.5-asm.8` がリリースされました。このバージョンはEnvoy `v1.38.7-dev` を使用し、セキュリティ速報 [GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067) で言及されているセキュリティ脆弱性が解決されています。

影響有無:
*   **影響あり（推奨）**: Cloud Service Meshのバージョンが `1.30.5-asm.8` より古い場合、このバージョンにアップグレードすることでセキュリティ脆弱性 [GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067) が修正され、セキュリティ体制が向上します。

対処方法:
1.  現在利用中のCloud Service Meshのバージョンを確認してください。
2.  `1.30.5-asm.8` より古いバージョンをご利用の場合は、速やかにこのバージョンまたはより新しいバージョンへのアップグレードを強く推奨します。
3.  アップグレード手順の詳細は、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) ドキュメントを参照し、計画的に実施してください。

## Fixed

原文: Patch 1.30.5-asm.8 contains the fix for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-18924 | Yes | Yes | No | Yes | Medium (9.1) |
| CVE-2026-82474 | Yes | Yes | No | Yes | Medium (8.5) |
| CVE-2026-82209 | Yes | Yes | No | Yes | Medium (8.2) |
| CVE-2026-84782 | Yes | Yes | No | Yes | High (8.2) |
| CVE-2026-96512 | Yes | Yes | No | Yes | Medium (7.8) |
| CVE-2026-80230 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-13608 | Yes | Yes | No | Yes | Medium (7.4) |
| CVE-2026-15534 | Yes | Yes | No | Yes | Medium (5.7) |
| CVE-2026-19487 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2026-35189 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75805 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75806 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-54872 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-77696 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-0799 | Yes | Yes | No | Yes | Medium (0.0) |
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924) ... (他のCVEリンク省略)

説明:
バージョン `1.30.5-asm.8` には、多数のプラットフォームCVE（共通脆弱性識別子）に対する修正が含まれています。これらの修正は、プロキシ、コントロールプレーン、CNIコンポーネントに影響を与えるものです。特に、SeverityがHigh（8.2）の`CVE-2026-84782`を含む、複数のMediumおよびLowの脆弱性が修正されています。

影響有無:
*   **影響あり（重要）**: 現在 `1.30.5-asm.8` より古いCloud Service Meshのバージョンをご利用の場合、これらのCVEに対する脆弱性が存在する可能性があります。アップグレードすることで、多数のセキュリティリスクが軽減されます。特にHigh Severityの脆弱性修正は、システムのセキュリティ体制を強化するために非常に重要です。

対処方法:
1.  現在利用中のCloud Service Meshのバージョンを確認してください。
2.  `1.30.5-asm.8` より古いバージョンをご利用の場合は、速やかにこのバージョンまたはより新しいバージョンへのアップグレードを強く推奨します。これにより、これらのCVEによって引き起こされる潜在的なセキュリティリスクからシステムを保護できます。
3.  アップグレード手順の詳細は、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) ドキュメントを参照し、計画的に実施してください。

## Announcement

原文: **1.29.8-asm.8 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.29.8-asm.8 uses Envoy v1.37.9-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade)
This release resolves the security vulnerability listed in Security Bulletin GCP-2026-067.
[GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067)

説明:
インクラスタ型Cloud Service Meshのバージョン `1.29.8-asm.8` がリリースされました。このバージョンはEnvoy `v1.37.9-dev` を使用し、セキュリティ速報 [GCP-2026-067](https://cloud.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067) で言及されているセキュリティ脆弱性が解決されています。

影響有無:
*   **影響あり（推奨）**: Cloud Service Meshのバージョンが `1.29.8-asm.8` より古い場合、このバージョンにアップグレードすることでセキュリティ脆弱性 [GCP-2026-067](https://cloud.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067) が修正され、セキュリティ体制が向上します。

対処方法:
1.  現在利用中のCloud Service Meshのバージョンを確認してください。
2.  `1.29.8-asm.8` より古いバージョンをご利用の場合は、速やかにこのバージョンまたはより新しいバージョンへのアップグレードを強く推奨します。
3.  アップグレード手順の詳細は、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade) ドキュメントを参照し、計画的に実施してください。

## Fixed

原文: Patch 1.29.8-asm.8 contains the fix for the following platform CVEs:
(CVEリストは1.30.5-asm.8と同じため省略)

説明:
バージョン `1.29.8-asm.8` には、多数のプラットフォームCVE（共通脆弱性識別子）に対する修正が含まれています。これは `1.30.5-asm.8` と同様のリストであり、特にHigh Severityの`CVE-2026-84782`を含む複数の脆弱性が修正されています。

影響有無:
*   **影響あり（重要）**: 現在 `1.29.8-asm.8` より古いCloud Service Meshのバージョンをご利用の場合、これらのCVEに対する脆弱性が存在する可能性があります。アップグレードすることで、多数のセキュリティリスクが軽減されます。特にHigh Severityの脆弱性修正は、システムのセキュリティ体制を強化するために非常に重要です。

対処方法:
1.  現在利用中のCloud Service Meshのバージョンを確認してください。
2.  `1.29.8-asm.8` より古いバージョンをご利用の場合は、速やかにこのバージョンまたはより新しいバージョンへのアップグレードを強く推奨します。これにより、これらのCVEによって引き起こされる潜在的なセキュリティリスクからシステムを保護できます。
3.  アップグレード手順の詳細は、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade) ドキュメントを参照し、計画的に実施してください。

## Announcement

原文: **1.28.10-asm.49 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.10-asm.49 uses Envoy v1.36.10-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)

説明:
インクラスタ型Cloud Service Meshのバージョン `1.28.10-asm.49` がリリースされました。このバージョンはEnvoy `v1.36.10-dev` を使用しています。

影響有無:
*   **影響なし（ただしメリットあり）**: このアナウンス自体にセキュリティ脆弱性の解決や新機能追加の明示的な記述はありませんが、後述のCVE修正が含まれているため、古いバージョンからのアップグレードは推奨されます。

対処方法:
1.  現在利用中のCloud Service Meshのバージョンを確認してください。
2.  `1.28.10-asm.49` より古いバージョンをご利用の場合は、後述のCVE修正の恩恵を受けるため、このバージョンまたはより新しいバージョンへのアップグレードを検討してください。
3.  アップグレード手順の詳細は、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade) ドキュメントを参照し、計画的に実施してください。

## Fixed

原文: Patch 1.28.10-asm.49 contains the fix for the following platform CVEs:
(CVEリストは1.30.5-asm.8と同じだが、CVE-2026-81870が追加されているため注意)

説明:
バージョン `1.28.10-asm.49` には、多数のプラットフォームCVE（共通脆弱性識別子）に対する修正が含まれています。これには、他のバージョンにも共通するHigh Severityの`CVE-2026-84782`を含む複数の脆弱性だけでなく、`CVE-2026-81870` (Low Severity) も追加で修正されています。

影響有無:
*   **影響あり（重要）**: 現在 `1.28.10-asm.49` より古いCloud Service Meshのバージョンをご利用の場合、これらのCVEに対する脆弱性が存在する可能性があります。アップグレードすることで、多数のセキュリティリスクが軽減されます。特にHigh Severityの脆弱性修正は、システムのセキュリティ体制を強化するために非常に重要です。

対処方法:
1.  現在利用中のCloud Service Meshのバージョンを確認してください。
2.  `1.28.10-asm.49` より古いバージョンをご利用の場合は、速やかにこのバージョンまたはより新しいバージョンへのアップグレードを強く推奨します。これにより、これらのCVEによって引き起こされる潜在的なセキュリティリスクからシステムを保護できます。
3.  アップグレード手順の詳細は、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade) ドキュメントを参照し、計画的に実施してください。

---

### 用語説明

*   **Cloud Service Mesh (Google Cloud)**: Google Cloud上で提供されるマネージドなサービスメッシュプラットフォーム。オープンソースのIstioに基づいており、サービスの接続、監視、セキュリティ保護、ルーティング制御などを可能にします。
*   **Istio**: マイクロサービス間のトラフィックを管理・制御・監視するためのオープンソースのサービスメッシュ実装。サイドカープロキシとしてEnvoyを使用します。
*   **Envoy Proxy**: クラウドネイティブアプリケーション向けに設計された高性能なオープンソースエッジ/サービスプロキシ。Istioのデータプレーンとして、各サービスのトラフィックを仲介します。
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されている既知のサイバーセキュリティの脆弱性や露出に関する識別子。セキュリティ研究者やベンダーが脆弱性を一意に識別し、共有するために使用されます。
*   **Proxy (サイドカープロキシ)**: サービスメッシュにおいて、各アプリケーションコンテナの隣にデプロイされ、そのアプリケーションへの出入りするすべてのネットワークトラフィックを横断的に処理するプロキシのこと。
*   **Control Plane (コントロールプレーン)**: サービスメッシュ全体の振る舞いを設定、管理、制御するコンポーネント群。IstioではPilot, Citadel, Galley, Mixer (現在はIstioに統合) などが該当します。
*   **CNI (Container Network Interface)**: Linuxコンテナのネットワーク接続を設定するための仕様。Kubernetesなどのコンテナオーケストレーションシステムで利用されます。Cloud Service Meshのコンポーネントとしても一部関係します。
*   **Distroless**: Googleが開発した、最小限のLinuxディストリビューション。アプリケーションを実行するために必要なものだけが含まれており、セキュリティとイメージサイズを最適化します。CVEの影響範囲で「Distroless」とあるのは、Distrolessベースのイメージを使用するコンポーネントへの影響を示唆しています。
*   **GCP-2026-067**: Google Cloudが発行したセキュリティ速報の識別子。特定のセキュリティ脆弱性に関する詳細情報を提供し、対処を促すものです。