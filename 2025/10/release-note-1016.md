
# Title: October 15, 2025 
Link: https://cloud.google.com/release-notes#October_15_2025<br>
## Cloud Service Mesh

### Announcement
原文: 1.25.5-asm.7 is now available for in-cluster Cloud Service Mesh.
You can now download 1.25.5-asm.7 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.25.5 subject to the list of supported features. Cloud Service Mesh version 1.25.5-asm.7 uses envoy v1.33.10-dev.

[Istio 1.25.5](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.5/)
[supported features](https://cloud.google.com/service-mesh/v1.25/docs/supported-features-in-cluster)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade)

説明: Cloud Service Meshのインクラスターデプロイメント向けに、バージョン1.25.5-asm.7が新たにリリースされました。このバージョンは、Istio 1.25.5の機能を包含し、Envoy v1.33.10-devを基盤としています。

影響有無:
*   **現在Cloud Service Meshを利用していない場合:** 影響なし。
*   **現在Cloud Service Meshを利用しているが、1.25.5-asm.7未満のバージョンを利用している場合:** 影響あり。新機能の利用や、後述のCVE修正の適用を検討できます。メジャーバージョンの変更を伴うため、非互換性のリスクについてはIstioのリリースノートやCloud Service Meshのドキュメントを確認する必要があります。

対処方法:
新機能の利用やセキュリティ修正の適用を検討する場合、計画的に本バージョンへのアップグレードを推奨します。アップグレード前に、公式ドキュメント「Upgrade Cloud Service Mesh」を参照し、互換性や影響範囲を十分に評価してください。

用語説明:
*   **Cloud Service Mesh (CSM):** Google Cloudが提供するフルマネージドなサービスメッシュプラットフォーム。Istioをベースとしており、マイクロサービス間の通信管理、トラフィックルーティング、ポリシー適用、テレメトリ収集などを提供します。
*   **In-cluster deployment:** Cloud Service Meshのコントロールプレーンが、Kubernetesクラスタ内にデプロイされる形式。
*   **Istio:** マイクロサービスを接続、監視、保護するためのオープンソースのサービスメッシュプラットフォーム。
*   **Envoy:** Istioでサイドカープロキシとして使用される高性能なオープンソースエッジ/サービスプロキシ。

### Fixed
原文: 1.25.5-asm.7 includes the fixes for the following CVEs:
| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| CVE-2025-6297 | Yes | Yes | Yes | - |
| CVE-2024-10963 | Yes | Yes | Yes | - |
| CVE-2025-4802 | - | - | - | Yes |
| CVE-2025-8058 | Yes | Yes | Yes | Yes |
[CVE-2025-6297](https://ubuntu.com/security/CVE-2025-6297)
[CVE-2024-10963](https://ubuntu.com/security/CVE-2024-10963)
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802)
[CVE-2025-8058](https://ubuntu.com/security/CVE-2025-8058)

説明: Cloud Service Mesh バージョン1.25.5-asm.7には、複数の共通脆弱性識別子（CVE）に対する修正が含まれています。これらのCVEはプロキシ、コントロールプレーン、CNI、Distrolessイメージの各コンポーネントに影響を与える可能性があります。

影響有無:
*   **現在Cloud Service Meshを利用していない場合:** 影響なし。
*   **現在Cloud Service Meshの1.25.5-asm.7未満のバージョンを利用している場合:** 影響あり。これらのCVEに起因するセキュリティリスクに晒されている可能性があります。

対処方法:
セキュリティリスクを軽減するため、バージョン1.25.5-asm.7またはそれ以降の推奨バージョンへの早期アップグレードを強く推奨します。アップグレード前に、各CVEの内容を確認し、自身の環境への影響度を評価してください。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures):** 公開されているソフトウェアのセキュリティ脆弱性を識別するための国際的な識別子。
*   **Control Plane:** サービスメッシュの動作を制御し、ポリシー適用や設定配布を行うコンポーネント群（IstioではPilot, Citadel, Galleyなど）。
*   **CNI (Container Network Interface):** コンテナネットワーキングのための仕様。Kubernetesクラスタ内でPodのネットワーク設定を行うプラグイン。
*   **Distroless:** 必要最低限のランタイムのみを含む軽量なベースイメージ。セキュリティリスクを減らすために使用される。

### Announcement
原文: 1.26.4-asm.7 is now available for in-cluster Cloud Service Mesh.
You can now download 1.26.4-asm.7 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.26.4 subject to the list of supported features.

[Istio 1.26.4](https://istio.io/latest/news/releases/1.26.x/announcing-1.26.4/)
[supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.26.4-asm.7 uses Envoy v1.34.8-dev.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明: Cloud Service Meshのインクラスターデプロイメント向けに、バージョン1.26.4-asm.7が新たにリリースされました。このバージョンは、Istio 1.26.4の機能を包含し、Envoy v1.34.8-devを基盤としています。

影響有無:
*   **現在Cloud Service Meshを利用していない場合:** 影響なし。
*   **現在Cloud Service Meshを利用しているが、1.26.4-asm.7未満のバージョンを利用している場合:** 影響あり。新機能の利用や、後述のCVE修正の適用を検討できます。

対処方法:
新機能の利用やセキュリティ修正の適用を検討する場合、計画的に本バージョンへのアップグレードを推奨します。アップグレード前に、公式ドキュメント「Upgrade Cloud Service Mesh」を参照し、互換性や影響範囲を十分に評価してください。

### Fixed
原文: 1.26.4-asm.7 includes the fixes for the following CVEs:
| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| CVE-2024-10963 | Yes | Yes | Yes | - |
| CVE-2025-8058 | Yes | Yes | Yes | Yes |
| CVE-2025-4802 | - | - | - | Yes |
[CVE-2024-10963](https://ubuntu.com/security/CVE-2024-10963)
[CVE-2025-8058](https://ubuntu.com/security/CVE-2025-8058)
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802)

説明: Cloud Service Mesh バージョン1.26.4-asm.7には、複数の共通脆弱性識別子（CVE）に対する修正が含まれています。これらのCVEはプロキシ、コントロールプレーン、CNI、Distrolessイメージの各コンポーネントに影響を与える可能性があります。

影響有無:
*   **現在Cloud Service Meshを利用していない場合:** 影響なし。
*   **現在Cloud Service Meshの1.26.4-asm.7未満のバージョンを利用している場合:** 影響あり。これらのCVEに起因するセキュリティリスクに晒されている可能性があります。

対処方法:
セキュリティリスクを軽減するため、バージョン1.26.4-asm.7またはそれ以降の推奨バージョンへの早期アップグレードを強く推奨します。アップグレード前に、各CVEの内容を確認し、自身の環境への影響度を評価してください。

### Announcement
原文: 1.27.1-asm.5 is now available for in-cluster Cloud Service Mesh.
You can now download 1.27.1-asm.5 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.27.1 subject to the list of supported features.

[Istio 1.27.1](https://istio.io/latest/news/releases/1.27.x/announcing-1.27/)
[supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.27.1-asm.5 uses Envoy v1.35.4-dev.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明: Cloud Service Meshのインクラスターデプロイメント向けに、最新バージョンの1.27.1-asm.5が新たにリリースされました。このバージョンは、Istio 1.27.1の機能を包含し、Envoy v1.35.4-devを基盤としています。

影響有無:
*   **現在Cloud Service Meshを利用していない場合:** 影響なし。
*   **現在Cloud Service Meshを利用しているが、1.27.1-asm.5未満のバージョンを利用している場合:** 影響あり。新機能の利用や、後述のCVE修正の適用を検討できます。

対処方法:
新機能の利用やセキュリティ修正の適用を検討する場合、計画的に本バージョンへのアップグレードを推奨します。アップグレード前に、公式ドキュメント「Upgrade Cloud Service Mesh」を参照し、互換性や影響範囲を十分に評価してください。

### Fixed
原文: 1.27.1-asm.5 includes the fixes for the following CVEs:
| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| CVE-2025-6297 | Yes | Yes | Yes | - |
| CVE-2024-10963 | Yes | Yes | Yes | - |
| CVE-2025-9230 | Yes | Yes | Yes | - |
| CVE-2025-8058 | Yes | Yes | Yes | Yes |
| CVE-2025-4802 | - | - | - | Yes |
[CVE-2025-6297](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-6297)
[CVE-2024-10963](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2024-10963)
[CVE-2025-9230](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-9230)
[CVE-2025-8058](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-8058)
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802)

説明: Cloud Service Meshの最新バージョンである1.27.1-asm.5には、複数の共通脆弱性識別子（CVE）に対する修正が含まれています。これらのCVEはプロキシ、コントロールプレーン、CNI、Distrolessイメージの各コンポーネントに影響を与える可能性があります。

影響有無:
*   **現在Cloud Service Meshを利用していない場合:** 影響なし。
*   **現在Cloud Service Meshの1.27.1-asm.5未満のバージョンを利用している場合:** 影響あり。これらのCVEに起因するセキュリティリスクに晒されている可能性があります。

対処方法:
セキュリティリスクを軽減するため、バージョン1.27.1-asm.5またはそれ以降の推奨バージョンへの早期アップグレードを強く推奨します。アップグレード前に、各CVEの内容を確認し、自身の環境への影響度を評価してください。

### Announcement
原文: In-cluster Cloud Service Mesh 1.24 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.

[Supported versions](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

説明: Cloud Service Meshのインクラスターデプロイメント向けバージョン1.24は、サポート対象外となりました。他のバージョンのサポート終了日については、「Supported versions」ドキュメントを参照してください。

影響有無:
*   **現在Cloud Service Meshを利用していない場合:** 影響なし。
*   **現在Cloud Service Meshのバージョン1.24を利用している場合:** 影響大。このバージョンは公式サポートが終了したため、セキュリティパッチやバグ修正が提供されなくなります。これにより、運用リスクが増大します。
*   **現在Cloud Service Meshのバージョン1.24以外のサポート対象バージョンを利用している場合:** 影響なし。ただし、今後のバージョンアップ計画において、サポート期間を考慮する必要があります。

対処方法:
現在Cloud Service Meshバージョン1.24を利用している場合は、速やかにサポートされているバージョン（例: 1.25.5-asm.7, 1.26.4-asm.7, 1.27.1-asm.5など）へのアップグレードを計画・実行してください。アップグレード計画には、互換性テストとロールバック戦略を含める必要があります。
今後のバージョンアップ計画では、サポート対象期間を考慮した上で、定期的なアップグレード戦略を策定することをお勧めします。

用語説明:
*   **サポート終了 (End of Life - EOL):** 特定のソフトウェアバージョンや製品に対して、ベンダーからのサポート（セキュリティアップデート、バグ修正、技術サポートなど）が提供されなくなる状態。EOLになったバージョンを使い続けることは、セキュリティリスクや運用リスクを高めます。
# Title: October 14, 2025 
Link: https://cloud.google.com/release-notes#October_14_2025<br>
Google Cloudのリリースノートを元に、構築済みのサービスへの影響調査結果を以下にご報告いたします。

---

# Apigee X

## Deprecated

原文:
Removal of deprecated Gemini Code Assist `@Apigee` tool.
The Gemini Code Assist `@Apigee` tool is shut down as of October 14, 2025.
See Gemini Code Assist @Apigee tool deprecation for information.
[Gemini Code Assist @Apigee tool deprecation](https://cloud.google.com/apigee/docs/deprecations/apigee-tool)

説明：
ApigeeのGemini Code Assist `@Apigee` ツールが非推奨となり、2025年10月14日にシャットダウンされることが発表されました。このツールは、Apigee APIプロキシなどの開発作業を支援するコード生成・補完機能を提供していました。

影響有無：
影響なし。
理由：現在のサービス構成において、Apigee Xおよび関連するGemini Code Assist `@Apigee` ツールの利用が確認されていないため、直接的な影響はありません。

対処方法：
なし。
もし今後Apigee Xの導入を検討される場合や、現在利用していないが開発プロセスにおいて類似の支援ツールを必要とする場合は、本ツールが廃止されることを考慮し、代替となる開発支援ソリューションの検討が必要です。詳細については、提供されたドキュメントリンクをご確認ください。

用語説明：
*   **Apigee X:** Google Cloudが提供するAPI管理プラットフォーム。APIの設計、デプロイ、セキュリティ、監視、分析などを一元的に行い、APIエコシステムの構築を支援します。
*   **Gemini Code Assist:** Google CloudのAIを活用したコード生成および補完機能の総称。開発者の生産性向上を目的としており、各種開発環境やサービスに統合されています。
*   **Deprecation (非推奨化):** ある機能やプロダクトが将来的にサポート対象外となる、または削除されることを事前に告知するプロセス。利用者には代替手段への移行が推奨されます。

---

# BigQuery

## Announcement

原文:
The BigQuery Data Transfer API (bigquerydatatransfer.googleapis.com) is now enabled by default for every new Google Cloud project. This feature is generally available (GA).
[generally available](https://cloud.google.com/products#product-launch-stages)

説明：
BigQuery Data Transfer API (`bigquerydatatransfer.googleapis.com`) が、新規作成されるすべてのGoogle Cloudプロジェクトでデフォルトで有効化されるようになりました。この機能は一般提供 (GA) されています。

影響有無：
影響なし。
理由：この変更は、新規に作成されるGoogle Cloudプロジェクトにのみ適用されるため、既存のプロジェクトや、現在稼働しているGoogle Cloud Composer2を含むサービスには直接的な影響を与えません。既存のプロジェクトでは、引き続き必要に応じてAPIの有効化・無効化を管理する必要があります。

対処方法：
なし。
新規プロジェクトでBigQuery Data Transfer APIを利用する際には、APIの有効化プロセスが不要になります。セキュリティポリシー上、特定のAPIのデフォルト有効化を避けたい場合は、プロジェクト作成後のAPI管理設定を確認・調整してください。

用語説明：
*   **BigQuery:** Google Cloudが提供する、フルマネージドでペタバイト級のデータ分析が可能なエンタープライズデータウェアハウスサービス。SQLを使用して大規模データセットを高速にクエリできます。
*   **BigQuery Data Transfer API:** BigQueryへのデータロードを自動化・スケジュール化するためのAPI。Google Cloud Storage、Google Ads、Google Analytics、Amazon S3など、さまざまなデータソースからBigQueryへデータを定期的に転送する機能を提供します。
*   **Generally Available (GA):** Google Cloudのプロダクトライフサイクルにおける最終段階の一つ。この段階にあるサービスは、安定性と信頼性が保証され、本番環境での利用が推奨されます。

---

# Google Kubernetes Engine

## Issue

原文:
In GKE versions 1.32.4-gke.1029000 and later, MountVolume calls for network file system (NFS) volumes might fail with the following error: `mount.nfs:rpc.statd is not running but is required for remote locking`.
This failure can occur if a Pod mounting an NFS volume runs on the same node as an NFS server Pod, and the NFS server Pod starts before the client Pod attempts to mount the volume. This scenario causes a conflict over the `rpcbind` service, which prevents the service from starting correctly on the node for the client Pod, leading to the mount failure.
As a workaround, deploy this DaemonSet on all nodes where you mount the NFS volumes.
[this DaemonSet](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/troubleshooting/nfs-mount-workaround/daemonset.yaml)

説明：
GKEのバージョン1.32.4-gke.1029000以降において、NFS (Network File System) ボリュームのマウント時に、`mount.nfs:rpc.statd is not running but is required for remote locking` というエラーが発生し、マウントが失敗する可能性がある問題が報告されています。この問題は、NFSボリュームをマウントするPodとNFSサーバーのPodが同一のノード上で動作し、かつNFSサーバーPodがNFSクライアントPodよりも先に起動した場合に、`rpcbind` サービスの競合が発生することによって引き起こされます。Googleから、この問題に対するワークアラウンドとしてDaemonSetのデプロイが提供されています。

影響有無：
影響なし。
理由：現在の環境では、Google Cloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3) が利用されています。ComposerはGKEを基盤としていますが、NFSボリュームをPodに直接マウントするようなカスタムのストレージ構成は標準的な利用パターンではありません。また、NFSサーバーPodとNFSクライアントPodを同一GKEノード上で実行するシナリオは、現在のワークロード設計には含まれていません。したがって、この問題は現在のサービス運用には影響しません。

対処方法：
なし。
もし将来的にGKEクラスタ上でNFSサーバーとNFSクライアントを同一ノード上で動作させるようなカスタムワークロードをデプロイする可能性がある場合は、このイシューを考慮し、Googleが提供するDaemonSetを適用することを検討してください。DaemonSetは、必要なNFS関連サービスがノード上で正しく起動するよう支援します。

用語説明：
*   **Google Kubernetes Engine (GKE):** Google Cloudが提供する、Kubernetesクラスタをマネージドサービスとしてデプロイ・運用するためのプラットフォーム。コンテナ化されたアプリケーションのデプロイ、スケーリング、管理を自動化します。
*   **NFS (Network File System):** ネットワーク経由でファイルシステムを共有するための分散ファイルシステムプロトコル。Linux/Unix環境で広く利用されています。
*   **Pod:** Kubernetesにおけるデプロイの最小単位。1つ以上のコンテナ、共有ストレージ、ネットワークリソース、およびコンテナ実行方法の仕様をカプセル化します。
*   **rpcbind:** RPC (Remote Procedure Call) サービスが利用可能なポート番号とトランスポートアドレスを管理するサービス。NFSのようなRPCベースのプロトコルで、クライアントがサーバーのRPCサービスを検索するために必要です。
*   **DaemonSet:** Kubernetesのワークロードオブジェクトの一種。指定されたすべてのノード（または一部のノード）でPodのコピーを1つ実行することを保証します。通常、ログコレクターや監視エージェント、または本件のようなノードごとのユーティリティサービスのデプロイに利用されます。