
# Title: October 14, 2026 
Link: https://docs.cloud.google.com/release-notes#October_14_2026<br>
Google Cloudのリリースノートに基づき、構築済みのサービスへの影響を調査し、以下の通り回答いたします。

---

# Cloud Load Balancing
## Change
原文: Google-managed public SSL certificates signed by Public Certificate Authority (`pki.goog`) are gradually transitioning from a 90-day validity period to a 45-day validity period to improve security. To align with modern industry-wide security standards and promote shorter certificate lifespans, Google-managed public certificates signed by Public Certificate Authority now rotate more frequently. This proactive rotation enhances the overall security posture of load balancers. Transition requires no manual intervention or configuration changes as Google Cloud automatically manages issuance and renewal for both Certificate Manager and Compute Engine SSL certificates. For more information, see Renew a Google-managed SSL certificate.

説明：Google マネージドのパブリック SSL 証明書（`pki.goog` によって署名されたもの）の有効期間が、セキュリティ強化のため段階的に90日から45日に短縮されます。これは、業界全体のセキュリティ標準に合わせ、証明書のライフスパンを短くすることで、ロードバランサ全体のセキュリティ体制を強化することを目的としています。この変更は、Google Cloud が証明書の発行と更新を自動的に管理するため、お客様による手動での介入や設定変更は不要です。

影響有無：影響なし。
理由：Google Cloud が証明書の発行と更新を完全に自動で管理するため、お客様側での設定変更や手動での対応は一切必要ありません。セキュリティの向上が透過的に適用されます。

対処方法：なし。Google Cloud によって自動的に処理されます。

用語説明：
*   **Google-managed public SSL certificates**: Google Cloudが発行、管理するSSL/TLS証明書で、ユーザーが証明書の発行や更新、失効などを意識する必要がないものです。
*   **Public Certificate Authority (`pki.goog`)**: Googleが運用する公開認証局で、Google Cloudサービスで利用される証明書の署名元となります。
*   **有効期間 (Validity period)**: 証明書が有効である期間を示します。この期間を過ぎると証明書は無効となり、再発行または更新が必要になります。セキュリティ向上のため、有効期間を短くすることが業界で推奨されています。

---

# Google Kubernetes Engine
## Fixed
原文: Fixed an issue in GKE Sandbox where Pods using the Cloud Storage FUSE CSI driver could become indefinitely stuck in a `Terminating` state. To resolve this issue, upgrade your node pools to GKE version 1.37.1-gke.1552000 or later and add the `dev.gvisor.fuse.abort-on-teardown: "true"` annotation to your Pod or Deployment metadata. For more information, see About Cloud Storage FUSE CSI driver for GKE and GKE Known Issues.

説明：GKE Sandbox 環境において、Cloud Storage FUSE CSI ドライバーを使用するPodが `Terminating` (終了中) 状態から抜け出せなくなり、停止してしまう問題が修正されました。この問題を解決するには、ご利用のノードプールをGKEバージョン1.37.1-gke.1552000以降にアップグレードし、さらにPodまたはDeploymentのメタデータに `dev.gvisor.fuse.abort-on-teardown: "true"` アノテーションを追加する必要があります。

影響有無：利用状況によって影響あり。
理由：
*   **影響を受ける可能性あり**: 現在のGKE環境で以下の両方を使用している場合、この問題の影響を受けている可能性があります。
    1.  GKE Sandbox (gVisor) を有効にしている
    2.  Cloud Storage FUSE CSIドライバーを使用しているPodが存在する
    *   さらに、現在のGKEバージョンが1.37.1-gke.1552000より古い場合に、この問題に直面する可能性があります。
*   **影響なし**: 上記のいずれかの条件に該当しない場合（例：GKE Sandboxを使用していない、Cloud Storage FUSE CSIドライバーを使用していない）は、直接的な影響はありません。

対処方法：
1.  **前提確認**: ご利用のGKEクラスタで、GKE Sandboxが有効であり、かつCloud Storage FUSE CSIドライバーを使用しているPodが存在するかを確認してください。
2.  **該当する場合の対処**:
    *   対象のノードプールをGKEバージョン1.37.1-gke.1552000以降にアップグレードしてください。
    *   Cloud Storage FUSE CSIドライバーを使用しているPodまたはDeploymentの定義（YAMLファイル）において、`metadata`セクションに以下の`annotations`を追加してください。
        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: your-deployment-name
        spec:
          template:
            metadata:
              annotations:
                dev.gvisor.fuse.abort-on-teardown: "true" # この行を追加
            spec:
              containers:
              - name: your-container
                # ...
        ```
3.  **該当しない場合**: 特段の対処は不要です。

用語説明：
*   **GKE Sandbox**: Google Kubernetes Engine (GKE) において、Podの分離境界を強化するためのセキュリティ機能です。gVisorというサンドボックス技術を利用し、Pod内のプロセスが基盤のホストOSに与える影響を制限することで、セキュリティを向上させます。
*   **Cloud Storage FUSE CSI driver**: Google Cloud Storage (GCS) のバケットをKubernetes Pod内にファイルシステムとしてマウントするためのCSI (Container Storage Interface) ドライバーです。これにより、アプリケーションはGCSバケットを通常のファイルシステムのように扱うことができます。
*   **Pod `Terminating` state**: Kubernetes Podが終了処理中であることを示す状態です。通常は短時間で完了しますが、問題が発生するとこの状態から抜け出せなくなり、リソースが解放されないことがあります。
*   **ノードプール (Node pool)**: GKEクラスタ内で、同じ設定（マシンタイプ、OSイメージなど）を持つVMインスタンスのグループです。異なるワークロードや要件に応じて複数のノードプールを作成できます。
*   **アノテーション (Annotation)**: Kubernetesオブジェクトに任意の非構造化データを追加するためのキーと値のペアです。ラベルとは異なり、主にツールやライブラリ、ユーザー向けのメタデータとして利用されます。今回はgVisorの特定の挙動を制御するための指示として使用されます。
# Title: October 13, 2026 
Link: https://docs.cloud.google.com/release-notes#October_13_2026<br>
ご提供いただいたリリースノートには、「Cloud SDK」の「Breaking Change」に関する具体的な内容が記載されていません。そのため、現状では詳細な影響評価は困難です。

以下に、現時点で提供されている情報に基づいた回答を示しますが、**具体的な変更内容が公開され次第、改めて詳細な影響評価と対応策の検討が必要となります。**

---

# Cloud SDK
## Breaking
原文: (No specific breaking change details provided in the release notes.)

説明：
Cloud SDKにおいて、非互換性のある変更（Breaking Change）が発生する、または既に発生していることを示すアナウンスです。しかし、今回のリリースノートでは、その具体的な変更内容が提供されていません。

影響有無：
現時点では具体的な変更内容が不明であるため、既存のサービスへの直接的な影響有無は判断できません。しかし、「Breaking Change」は、既存のスクリプト、CI/CDパイプライン、自動化ツール、またはアプリケーションがCloud SDKの特定のバージョンを利用している場合に、予期せぬ動作、機能不全、またはエラーを引き起こす可能性が非常に高いです。

**Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) への影響：**
Cloud Composerは内部でGoogle Cloud SDKを様々な操作に使用しています。もし今回のBreaking Changeが、Composer環境が依存しているCloud SDKの特定のコマンドやライブラリに影響を与える場合、ComposerのDAGの実行、環境の管理操作、またはその他の機能に影響を及ぼす可能性があります。ただし、Composerはマネージドサービスであり、Google側でSDKのバージョン管理や互換性テストを行っているため、直ちに影響が出る可能性は低いですが、今後のComposerのアップデートや、カスタムでSDKを呼び出すDAGを使用している場合には注意が必要です。

対処方法：
1.  **詳細情報の確認:** Cloud SDKの公式リリースノート、Google Cloudのサービスアップデート情報、または関連するドキュメントで、今回のBreaking Changeに関する具体的な詳細が公開されるのを継続的に確認してください。
2.  **影響範囲の特定:** Cloud SDKを利用している既存のスクリプト、CI/CDパイプライン、開発環境、およびGoogle Cloud ComposerのカスタムDAGなどを特定し、変更内容が明らかになった際に影響を受ける可能性のある箇所を把握できるように準備してください。
3.  **テスト計画の準備:** 変更が適用されたCloud SDKのバージョンに対して、既存のワークロードが正常に動作するかを検証するためのテスト計画を準備してください。可能であれば、開発環境やステージング環境で事前にテストを実施することを強く推奨します。
4.  **バージョン固定の検討:** 重大な影響を避けるため、CI/CDパイプラインなどで利用するCloud SDKのバージョンを明示的に固定し、Breaking Changeが発表された際に計画的にバージョンアップを行う運用を検討してください。

用語説明：
*   **Cloud SDK:** Google Cloud Platform のサービスとやり取りするためのコマンドラインツール（`gcloud`）、クライアントライブラリ、およびその他のユーティリティのセットです。開発者や管理者がGoogle Cloudリソースを管理するために広く使用されます。
*   **Breaking Change (非互換性のある変更):** ソフトウェアの新しいバージョンがリリースされた際に、以前のバージョンで動作していたコードや設定が、新しいバージョンでは動作しなくなるような変更のことです。APIのシグネチャ変更、設定ファイルの形式変更、動作の根本的な変更などが含まれ、通常、既存のシステムやアプリケーションの修正が必要になります。
*   **Google Cloud Composer:** Apache Airflow を Google Cloud 上でマネージドサービスとして実行できるサービスです。ワークフローのオーケストレーションに使用され、内部でCloud SDKの機能を利用することがあります。
# Title: October 12, 2026 
Link: https://docs.cloud.google.com/release-notes#October_12_2026<br>
Cloud Service Meshをご利用いただきありがとうございます。リリースノートに基づき、各変更点の影響について調査結果を報告いたします。

# Cloud Service Mesh

## Announcement
原文: **1.31.1-asm.16 is now available for in-cluster Cloud Service Mesh.**
 You can now download 1.31.1-asm.16 for in-cluster Cloud Service Mesh. It includes
the features of Istio 1.31.1 subject to the list of
supported features.

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

 For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh version 1.31.1-asm.16 uses Envoy v1.39.3.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明: クラスタ内Cloud Service Mesh (in-cluster Cloud Service Mesh) の新バージョン `1.31.1-asm.16` が利用可能になりました。このバージョンにはIstio 1.31.1の機能が含まれていますが、特定の機能はCloud Service Meshではサポート対象外となります。アップグレードの詳細と、このバージョンで使用されるEnvoyのバージョン（v1.39.3）についても言及されています。

影響有無: **影響なし（ただし、アップグレードを検討する場合に影響あり）**
このアナウンスは新しいバージョンの提供であり、既存の稼働環境に直接的な影響はありません。ただし、本バージョンへのアップグレードを検討する際には、記載されている「サポート対象外の機能リスト」を詳細に確認する必要があります。現在、これらの機能を使用している場合は、アップグレード後に意図しない挙動や機能の喪失が発生する可能性があります。また、Envoyのバージョンアップ（v1.39.3）に伴う既存設定やカスタムリソースとの互換性も確認が必要です。

対処方法:
1.  **即座の対応は不要**: 現在のCloud Service Meshが正常に稼働している場合、このアナウンスに対する緊急の対応は必要ありません。
2.  **アップグレード計画の検討**: 最新機能の利用や将来的なセキュリティ更新を見据え、本バージョンへのアップグレードを計画する際に以下の点を確認してください。
    *   **サポート対象外機能の確認**: 現在のサービスメッシュ設定で、アナウンスに記載されているサポート対象外機能を使用していないか確認します。使用している場合は、代替機能の有無やアップグレードの要否を検討してください。
    *   **互換性テスト**: アップグレードを行う前に、テスト環境でアプリケーションの互換性、特にEnvoyのバージョンアップによる影響を十分に検証してください。
    *   **アップグレード手順の確認**: 公式ドキュメントの[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)を参照し、適切なアップグレード手順を実施してください。

用語説明:
*   **In-cluster Cloud Service Mesh**: Google Kubernetes Engine (GKE) クラスタ内にサービスメッシュのコントロールプレーンをデプロイして運用するCloud Service Meshのデプロイメントモデルです。
*   **Istio**: オープンソースのサービスメッシュプラットフォームです。Kubernetesを拡張し、トラフィック管理、ポリシー適用、セキュリティ、可観測性などの機能を提供します。
*   **Envoy**: Istioのデータプレーンとして使用される高性能なオープンソースのサービスプロキシです。サービス間のすべてのネットワークトラフィックを処理します。
*   **サポート対象外機能**: Istioの機能のうち、Cloud Service Meshが公式にサポートしない、または制限付きでサポートする機能です。これらの機能を使用すると、予期せぬ動作やサポートの問題が発生する可能性があります。

---

## Announcement
原文: **1.30.5-asm.8 is now available for in-cluster Cloud Service Mesh.**

 For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.30.5-asm.8 uses Envoy v1.38.7-dev.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)
 This release resolves the security vulnerability listed in Security Bulletin
GCP-2026-067.

[GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067)

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
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924)
[CVE-2026-82474](https://nvd.nist.gov/vuln/detail/CVE-2026-82474)
[CVE-2026-82209](https://nvd.nist.gov/vuln/detail/CVE-2026-82209)
[CVE-2026-84782](https://nvd.nist.gov/vuln/detail/CVE-2026-84782)
[CVE-2026-96512](https://nvd.nist.gov/vuln/detail/CVE-2026-96512)
[CVE-2026-80230](https://nvd.nist.gov/vuln/detail/CVE-2026-80230)
[CVE-2026-13608](https://nvd.nist.gov/vuln/detail/CVE-2026-13608)
[CVE-2026-15534](https://nvd.nist.gov/vuln/detail/CVE-2026-15534)
[CVE-2026-19487](https://nvd.nist.gov/vuln/detail/CVE-2026-19487)
[CVE-2026-35189](https://nvd.nist.gov/vuln/detail/CVE-2026-35189)
[CVE-2026-75805](https://nvd.nist.gov/vuln/detail/CVE-2026-75805)
[CVE-2026-75806](https://nvd.nist.gov/vuln/detail/CVE-2026-75806)
[CVE-2026-54872](https://nvd.nist.gov/vuln/detail/CVE-2026-54872)
[CVE-2026-77696](https://nvd.nist.gov/vuln/detail/CVE-2026-77696)
[CVE-2026-0799](https://nvd.nist.gov/vuln/detail/CVE-2026-0799)

説明: クラスタ内Cloud Service Meshのバージョン `1.30.5-asm.8` が利用可能になりました。このリリースは、セキュリティ速報 `GCP-2026-067` に記載されているセキュリティ脆弱性を解決し、多数のCVE（共通脆弱性識別子）に対する修正を含んでいます。このバージョンはEnvoy v1.38.7-devを使用します。

影響有無: **影響あり（セキュリティリスク軽減のためアップグレード推奨）**
本バージョンはセキュリティ脆弱性（GCP-2026-067および複数のCVE）の修正が含まれています。現在のCloud Service Meshが `1.30.5-asm.8` より古いバージョンである場合、これらの脆弱性にさらされている可能性があります。この修正はセキュリティ体制を強化するために重要です。

対処方法:
1.  **アップグレードの検討と計画**: 現在Cloud Service Mesh 1.30.x 系をご利用の場合、セキュリティリスクを軽減するために、本バージョンへのアップグレードを強く推奨します。
2.  **互換性テスト**: アップグレード前に、テスト環境で既存のアプリケーションやサービスメッシュの設定が、本バージョン（特にEnvoy v1.38.7-dev）と互換性があるかを十分に検証してください。
3.  **アップグレード手順の実施**: 公式ドキュメントの[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)を参照し、計画的なアップグレードを実施してください。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアの脆弱性を識別するための共通識別子です。CVEに続く番号は、個々の脆弱性を一意に特定します。
*   **Security Bulletin**: 製品やサービスに関するセキュリティ脆弱性の情報を提供する公式文書です。Google Cloudでは「Security Bulletin GCP-XXXX-XXX」の形式で公開されます。
*   **Proxy**: この文脈では、Envoyプロキシを指します。サービスメッシュのデータプレーンとして動作し、サービス間のトラフィックを仲介します。
*   **Control Plane**: サービスメッシュの管理コンポーネント群を指します（Istioの場合、Pilot, Citadel, Galley, Mixerなど）。
*   **Distroless**: 最小限のランタイム依存関係のみを含むコンテナイメージのことです。セキュリティ脆弱性の表面積を減らす目的で使用されます。
*   **CNI (Container Network Interface)**: Kubernetesなどのコンテナオーケストレーションシステムがネットワークプラグインと通信するための仕様です。

---

## Announcement
原文: **1.29.8-asm.8 is now available for in-cluster Cloud Service Mesh.**

 For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.29.8-asm.8 uses Envoy v1.37.9-dev.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade)
 This release resolves the security vulnerability listed in Security Bulletin
GCP-2026-067.

[GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067)

## Fixed
原文: Patch 1.29.8-asm.8 contains the fix for the following platform CVEs:

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
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924)
[CVE-2026-82474](https://nvd.nist.gov/vuln/detail/CVE-2026-82474)
[CVE-2026-82209](https://nvd.nist.gov/vuln/detail/CVE-2026-82209)
[CVE-2026-84782](https://nvd.nist.gov/vuln/detail/CVE-2026-84782)
[CVE-2026-96512](https://nvd.nist.gov/vuln/detail/CVE-2026-96512)
[CVE-2026-80230](https://nvd.nist.gov/vuln/detail/CVE-2026-80230)
[CVE-2026-13608](https://nvd.nist.gov/vuln/detail/CVE-2026-13608)
[CVE-2026-15534](https://nvd.nist.gov/vuln/detail/CVE-2026-15534)
[CVE-2026-19487](https://nvd.nist.gov/vuln/detail/CVE-2026-19487)
[CVE-2026-35189](https://nvd.nist.gov/vuln/detail/CVE-2026-35189)
[CVE-2026-75805](https://nvd.nist.gov/vuln/detail/CVE-2026-75805)
[CVE-2026-75806](https://nvd.nist.gov/vuln/detail/CVE-2026-75806)
[CVE-2026-54872](https://nvd.nist.gov/vuln/detail/CVE-2026-54872)
[CVE-2026-77696](https://nvd.nist.gov/vuln/detail/CVE-2026-77696)
[CVE-2026-0799](https://nvd.nist.gov/vuln/detail/CVE-2026-0799)

説明: クラスタ内Cloud Service Meshのバージョン `1.29.8-asm.8` が利用可能になりました。このリリースは、セキュリティ速報 `GCP-2026-067` に記載されているセキュリティ脆弱性を解決し、多数のCVEに対する修正を含んでいます。このバージョンはEnvoy v1.37.9-devを使用します。

影響有無: **影響あり（セキュリティリスク軽減のためアップグレード推奨）**
本バージョンはセキュリティ脆弱性（GCP-2026-067および複数のCVE）の修正が含まれています。現在のCloud Service Meshが `1.29.8-asm.8` より古いバージョンである場合、これらの脆弱性にさらされている可能性があります。この修正はセキュリティ体制を強化するために重要です。

対処方法:
1.  **アップグレードの検討と計画**: 現在Cloud Service Mesh 1.29.x 系をご利用の場合、セキュリティリスクを軽減するために、本バージョンへのアップグレードを強く推奨します。
2.  **互換性テスト**: アップグレード前に、テスト環境で既存のアプリケーションやサービスメッシュの設定が、本バージョン（特にEnvoy v1.37.9-dev）と互換性があるかを十分に検証してください。
3.  **アップグレード手順の実施**: 公式ドキュメントの[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade)を参照し、計画的なアップグレードを実施してください。

用語説明:
*   **Severity**: 脆弱性の深刻度を示す指標です。通常、CVSS (Common Vulnerability Scoring System) スコアに基づいてHigh, Medium, Lowなどに分類されます。

---

## Announcement
原文: **1.28.10-asm.49 is now available for in-cluster Cloud Service Mesh.**

 For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.28.10-asm.49 uses Envoy v1.36.10-dev.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)

## Fixed
原文: Patch 1.28.10-asm.49 contains the fix for the following platform CVEs:

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
| CVE-2026-81870 | Yes | Yes | Yes | Yes | Low (2.0) |
| CVE-2026-0799 | Yes | Yes | No | Yes | Medium (0.0) |
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924)
[CVE-2026-82474](https://nvd.nist.gov/vuln/detail/CVE-2026-82474)
[CVE-2026-82209](https://nvd.nist.gov/vuln/detail/CVE-2026-82209)
[CVE-2026-84782](https://nvd.nist.gov/vuln/detail/CVE-2026-84782)
[CVE-2026-96512](https://nvd.nist.gov/vuln/detail/CVE-2026-96512)
[CVE-2026-80230](https://nvd.nist.gov/vuln/detail/CVE-2026-80230)
[CVE-2026-13608](https://nvd.nist.gov/vuln/detail/CVE-2026-13608)
[CVE-2026-15534](https://nvd.nist