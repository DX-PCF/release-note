
# Title: June 23, 2026 
Link: https://docs.cloud.google.com/release-notes#June_23_2026<br>
## Cloud SDK
### Change
原文: (空)
説明: このリリースノートエントリは、Cloud SDKの変更点について記載されるべき部分ですが、詳細な内容が提供されていません。
影響有無: 原文が提供されていないため、影響の有無を判断できません。
対処方法: Cloud SDKの具体的な変更内容が不明なため、現時点での対処は不要です。定期的にCloud SDKのリリースノートを確認し、利用している機能に影響がないか確認することを推奨します。
用語説明:
*   **Cloud SDK**: Google Cloudの各種サービスをコマンドラインから操作するためのツールセットです。gcloud CLI、gsutil、bqツールなどが含まれます。

---

## Cloud Service Mesh
### Security
原文: **1.29.5-asm.3 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in GCP-2026-040.
[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.29.5-asm.3 uses Envoy v1.37.5-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)
説明: インクラスター（self-managed）版のCloud Service Meshバージョン1.29.5-asm.3がリリースされました。このパッチリリースには、セキュリティ脆弱性「GCP-2026-040」に対する修正が含まれています。このバージョンはEnvoy v1.37.5-devを使用しています。
影響有無: 影響あり。このリリースはセキュリティ修正を含んでいるため、サービス全体のセキュリティ体制を強化するポジティブな影響があります。現在Cloud Service Meshのバージョン1.29.xをインクラスターで運用している場合、この脆弱性の影響を受ける可能性があります。
対処方法: Cloud Service Meshのバージョン1.29.5-asm.3へのアップグレードを強く推奨します。アップグレード手順については、提供されているリンク「Upgrade Cloud Service Mesh」を参照してください。
用語説明:
*   **Cloud Service Mesh**: Google Cloud上で動作する、サービスメッシュ機能を提供するサービスです。オープンソースのIstioをベースにしています。
*   **インクラスター（in-cluster）Cloud Service Mesh**: ユーザー自身がGKEクラスタ内にService Meshのコントロールプレーンをデプロイし、管理する形態です。セルフマネージドとも呼ばれます。
*   **Envoy**: Cloud Service Mesh（Istio）で使用される高性能プロキシで、サイドカーとして各サービスにデプロイされ、トラフィックルーティング、セキュリティ、テレメトリ収集などを行います。
*   **GCP-2026-040**: Google Cloudで発見されたセキュリティ脆弱性の識別子です。詳細については、関連するセキュリティ速報を確認する必要があります。

### Fixed
原文: This patch release also contain the fixes for the following CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-34182 | Yes | Yes | No | Yes | Medium (9.1) |
| CVE-2026-45447 | Yes | Yes | No | Yes | High (8.8) |
| CVE-2026-7383 | Yes | Yes | No | Yes | Low (8.1) |
| CVE-2026-34180 | Yes | Yes | No | Yes | Low (7.5) |
| CVE-2026-45445 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-9076 | Yes | Yes | No | Yes | Low (7.5) |
| CVE-2026-42766 | Yes | Yes | No | Yes | Low (5.9) |
| CVE-2026-42767 | Yes | Yes | No | Yes | Low (5.9) |
| CVE-2026-34743 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-45446 | Yes | Yes | No | Yes | Low (4.8) |
| CVE-2026-42770 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-40226 | Yes | Yes | No | Yes | Medium (0.0) |
説明: このパッチリリースには、上記のCVE（Common Vulnerabilities and Exposures）に対する修正が含まれています。これらの修正は、プロキシ、コントロールプレーン、CNIなどのコンポーネントに影響し、それぞれHigh, Medium, Lowの深刻度を持つ複数の脆弱性を解決します。
影響有無: 影響あり。これらの修正により、Cloud Service Mesh環境のセキュリティが向上します。特にHighおよびMediumの脆弱性は、サービスへの潜在的な攻撃リスクを低減するため、影響はポジティブです。これらのCVEの影響を受けるバージョンのCloud Service Meshを使用している場合、サービスが脆弱な状態である可能性があります。
対処方法: Cloud Service Meshのバージョン1.29.5-asm.3へのアップグレードを強く推奨します。アップグレードにより、これらの脆弱性から保護されます。
用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されているソフトウェアのセキュリティ脆弱性に付けられる識別子です。
*   **Proxy**: この文脈では、主にEnvoyプロキシを指し、データプレーンとして機能します。
*   **Control Plane**: Service Meshの管理を行うコンポーネント群（Istiodなど）を指します。
*   **Distroless**: 最小限の依存関係しか含まないLinuxディストリビューションで構築されたコンテナイメージを指します。
*   **CNI (Container Network Interface)**: コンテナがネットワークと通信するためのプラグイン仕様です。
*   **Severity**: 脆弱性の深刻度を示す尺度です。CVSS (Common Vulnerability Scoring System) スコアに基づいて評価されます。

### Security
原文: **1.28.9-asm.2 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in GCP-2026-040.
[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.9-asm.2 uses Envoy v1.36.9-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)
説明: インクラスター版のCloud Service Meshバージョン1.28.9-asm.2がリリースされました。このパッチリリースには、セキュリティ脆弱性「GCP-2026-040」に対する修正が含まれています。このバージョンはEnvoy v1.36.9-devを使用しています。
影響有無: 影響あり。このリリースはセキュリティ修正を含んでいるため、サービス全体のセキュリティ体制を強化するポジティブな影響があります。現在Cloud Service Meshのバージョン1.28.xをインクラスターで運用している場合、この脆弱性の影響を受ける可能性があります。
対処方法: Cloud Service Meshのバージョン1.28.9-asm.2へのアップグレードを強く推奨します。アップグレード手順については、提供されているリンク「Upgrade Cloud Service Mesh」を参照してください。

### Fixed
原文: This patch release also contain the fixes for the following CVEs:
(上記の1.29.5-asm.3のCVEリストと同一)
説明: このパッチリリースには、上記のCVE（Common Vulnerabilities and Exposures）に対する修正が含まれています。これらの修正は、プロキシ、コントロールプレーン、CNIなどのコンポーネントに影響し、それぞれHigh, Medium, Lowの深刻度を持つ複数の脆弱性を解決します。
影響有無: 影響あり。これらの修正により、Cloud Service Mesh環境のセキュリティが向上します。特にHighおよびMediumの脆弱性は、サービスへの潜在的な攻撃リスクを低減するため、影響はポジティブです。これらのCVEの影響を受けるバージョンのCloud Service Meshを使用している場合、サービスが脆弱な状態である可能性があります。
対処方法: Cloud Service Meshのバージョン1.28.9-asm.2へのアップグレードを強く推奨します。アップグレードにより、これらの脆弱性から保護されます。

### Security
原文: **1.27.9-asm.8 is now available for in-cluster Cloud Service Mesh.**
This patch release contains the fix for the security vulnerability listed in GCP-2026-040.
[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.27.9-asm.8 uses Envoy v1.35.13-dev.
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade)
説明: インクラスター版のCloud Service Meshバージョン1.27.9-asm.8がリリースされました。このパッチリリースには、セキュリティ脆弱性「GCP-2026-040」に対する修正が含まれています。このバージョンはEnvoy v1.35.13-devを使用しています。
影響有無: 影響あり。このリリースはセキュリティ修正を含んでいるため、サービス全体のセキュリティ体制を強化するポジティブな影響があります。現在Cloud Service Meshのバージョン1.27.xをインクラスターで運用している場合、この脆弱性の影響を受ける可能性があります。
対処方法: Cloud Service Meshのバージョン1.27.9-asm.8へのアップグレードを強く推奨します。アップグレード手順については、提供されているリンク「Upgrade Cloud Service Mesh」を参照してください。

### Fixed
原文: This patch release also contain the fixes for the following CVEs:
(上記の1.29.5-asm.3のCVEリストと同一)
説明: このパッチリリースには、上記のCVE（Common Vulnerabilities and Exposures）に対する修正が含まれています。これらの修正は、プロキシ、コントロールプレーン、CNIなどのコンポーネントに影響し、それぞれHigh, Medium, Lowの深刻度を持つ複数の脆弱性を解決します。
影響有無: 影響あり。これらの修正により、Cloud Service Mesh環境のセキュリティが向上します。特にHighおよびMediumの脆弱性は、サービスへの潜在的な攻撃リスクを低減するため、影響はポジティブです。これらのCVEの影響を受けるバージョンのCloud Service Meshを使用している場合、サービスが脆弱な状態である可能性があります。
対処方法: Cloud Service Meshのバージョン1.27.9-asm.8へのアップグレードを強く推奨します。アップグレードにより、これらの脆弱性から保護されます。

### Security
原文: The following images are now rolling out for managed Cloud Service Mesh:
- Sidecar version 1.21.6-asm.38, is rolling out to the rapid release channel.
- Sidecar version 1.20.8-asm.88 is rolling out to the regular release channel.
- Sidecar version 1.19.10-asm.78 is rolling out to the stable release channel.
These patch releases contain the fix for the vulnerability listed in GCP-2026-040.
[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
These rollouts will preempt those previously announced on June 12, 2026.
[June 12, 2026](#June_12_2026)
説明: マネージドCloud Service Meshの以下のサイドカーバージョンが各リリースチャネルに展開されています。
*   Rapidチャネル: 1.21.6-asm.38
*   Regularチャネル: 1.20.8-asm.88
*   Stableチャネル: 1.19.10-asm.78
これらのパッチリリースには、セキュリティ脆弱性「GCP-2026-040」に対する修正が含まれています。この展開は、2026年6月12日に以前発表されたものに優先します。
影響有無: 影響あり。このリリースはセキュリティ修正を含んでいるため、サービス全体のセキュリティ体制を強化するポジティブな影響があります。現在マネージドCloud Service Meshを利用している場合、これらのサイドカーバージョンのいずれかに自動的に更新されることで、この脆弱性から保護されます。
対処方法: マネージドCloud Service Meshは自動的に更新が適用されるため、ユーザー側での手動によるアップグレード作業は基本的に不要です。ただし、GCP-2026-040の脆弱性に関するリスクが懸念される場合は、ご自身の環境のCloud Service Meshのチャネルとバージョンを確認し、これらの修正が適用されていることを確認してください。
用語説明:
*   **マネージドCloud Service Mesh**: Googleがコントロールプレーンを管理するService Meshの形態です。ユーザーはデータプレーン（サイドカー）の管理に注力できます。
*   **リリースチャネル (Release Channel)**: マネージドサービスにおける更新の適用頻度と安定性のレベルを定義するものです。`Rapid` は最新機能が早く提供されるが安定性は低い、`Stable` は安定性が最も高いが機能提供は遅い、`Regular` はその中間です。

---

## Google Kubernetes Engine
### Issue
原文: For GKE cluster version 1.34.1-gke.3899001 (sidecar mounter image version 1.21.9) and later affected versions, Cloud Storage FUSE volumes might fail to mount if the GKE metadata service isn't ready when the Cloud Storage FUSE sidecar initiates.
When this issue occurs, you might see the following error:
Additionally, the `gcsfuse-sidecar` container displays the following error:
**Mitigation**
To resolve this issue, perform one of the following mitigations:
- Upgrade your cluster to one of the following fixed GKE versions:
  - `1.34.8-gke.1218000` or later
  - `1.35.3-gke.2347000` or later
  - `1.36.0-gke.1266000` or later.
- Create an init container in your Pod that validates metadata service availability.
- Manually inject the sidecar to ensure the sidecar is blocked by an init container.
For more information, see the Cloud Storage FUSE CSI driver troubleshooting guide.
[Cloud Storage FUSE CSI driver troubleshooting guide](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md#limitations)
説明: GKEクラスターバージョン1.34.1-gke.3899001（およびそれ以降のバージョン）において、GKEメタデータサービスが準備できていない状態でCloud Storage FUSEサイドカーが起動すると、Cloud Storage FUSEボリュームのマウントに失敗する可能性があります。この問題が発生すると、特定の`gcsfuse-sidecar`コンテナのエラーが表示されます。
解決策として、以下のいずれかが提案されています。
1.  GKEクラスターを修正済みバージョン（1.34.8-gke.1218000以降、1.35.3-gke.2347000以降、1.36.0-gke.1266000以降）にアップグレードする。
2.  Pod内に、メタデータサービスの可用性を検証するinitコンテナを作成する。
3.  サイドカーを手動でインジェクトし、initコンテナによってサイドカーの起動がブロックされるようにする。
影響有無: 影響は限定的です。
ユーザー環境のCloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3) は通常、GKE 1.26.x または 1.27.x ベースで動作するため、本リリースノートに記載されているGKEバージョン（1.34.x以降）よりも古い可能性が高いです。したがって、現時点では直接的な影響はないと考えられます。
ただし、もし利用中のCloud Composer環境がカスタム設定でCloud Storage FUSE CSIドライバーを使用しており、将来的にGKEバージョンが影響範囲（1.34.1-gke.3899001以降）にアップグレードされた場合、この問題が発生する可能性があります。
対処方法:
現時点では直接的な対処は不要です。
将来的にCloud Composer環境のGKEバージョンが1.34.1-gke.3899001以降にアップグレードされ、かつCloud Storage FUSE CSIドライバーを使用している場合に問題が発生した場合は、GKEクラスターの修正済みバージョンへのアップグレードを検討するか、initコンテナの導入、またはサイドカーの手動インジェクトによる回避策を適用してください。
用語説明:
*   **Cloud Storage FUSE**: Google Cloud Storageバケットをファイルシステムとしてマウントできるオープンソースのアダプターです。
*   **GKE Metadata Service**: GKEノード上で実行される内部サービスで、PodのWorkload Identityなど、GKEのメタデータを提供します。
*   **Sidecar**: メインアプリケーションコンテナと一緒にPod内で実行される補助的なコンテナです。ここではCloud Storage FUSEのマウント機能を提供します。
*   **Init Container**: Podのアプリケーションコンテナが起動する前に実行される特別なコンテナです。セットアップや前提条件の確認などに使用されます。

### Issue
原文: In GKE version 1.35 and later, due to faster node startup, workloads that use Dataplane V2 and Workload Identity Federation for GKE to authenticate to Google Cloud APIs might experience transient connectivity timeouts or refused connections to the GKE metadata server immediately following node startup.
[authenticate to Google Cloud APIs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
For recommendations and workarounds if this impacts your workload (for example, if your workload doesn't retry requests until they succeed), see Timeout errors at Pod startup, specifically by deploying an `initContainer`.
[Timeout errors at Pod startup](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication#troubleshoot-timeout)
Alternatively, add any that selects no workloads, such as in a namespace with no workloads—to GKE Dataplane V2, network policy—including one which disables the faster node startup.
Improvements are in progress and coming in a future GKE patch.
[network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)
説明: GKEバージョン1.35以降で、ノードの起動が高速化された結果、Dataplane V2とGKEのWorkload Identity連携を使用してGoogle Cloud APIsへの認証を行うワークロードにおいて、ノード起動直後にGKEメタデータサーバーへの一時的な接続タイムアウトや接続拒否が発生する可能性があります。
推奨される回避策として、Pod起動時に`initContainer`を使用してタイムアウトエラーに対処する方法が挙げられています。また、Dataplane V2のネットワークポリシー（ワークロードを選択しないポリシーでも可）を追加することで、ノードの高速起動を無効化することも可能です。将来的にはGKEパッチで改善される予定です。
影響有無: 影響は限定的です。
ユーザー環境のCloud Composer2 (Composer version 2.7.1, Airflow version 2.7.3) は通常、GKE 1.26.x または 1.27.x ベースで動作するため、本リリースノートに記載されているGKEバージョン（1.35以降）よりも古い可能性が高いです。したがって、現時点では直接的な影響はないと考えられます。
ただし、もし利用中のCloud Composer環境が将来的にGKEバージョン1.35以降にアップグレードされ、かつDataplane V2とWorkload Identity Federation for GKEを組み合わせて使用している場合、この問題が発生する可能性があります。Cloud Composerは通常Workload Identityを使用するため、GKEバージョンが該当すると影響を受ける可能性があります。
対処方法:
現時点では直接的な対処は不要です。
将来的にCloud Composer環境のGKEバージョンが1.35以降にアップグレードされ、この問題が発生した場合は、ワークロードがリトライ処理を行うように修正するか、Podに`initContainer`を導入してメタデータサービスへの接続を待機させる、またはDataplane V2のネットワークポリシーを調整してノードの高速起動を無効化することを検討してください。
用語説明:
*   **Dataplane V2**: GKEのContainer Network Interface (CNI) の一種で、eBPFを活用してネットワークパフォーマンスとセキュリティを向上させます。
*   **Workload Identity Federation for GKE**: GKEのPodがGoogle CloudのサービスアカウントになりすましてGoogle Cloud APIに安全にアクセスするための機能です。
*   **GKE Metadata Server**: GKEノード上で動作し、PodのWorkload Identity認証情報など、GKEクラスター内のメタデータを提供するサービスです。
*   **Init Container**: Podのアプリケーションコンテナが起動する前に実行される特別なコンテナです。ここでは、サービス起動前の前提条件（メタデータサービスへの接続性）を確保するために利用が推奨されます。
*   **Network Policy**: Kubernetesのネットワークトラフィックの許可/拒否ルールを定義する機能です。Dataplane V2はネットワークポリシーの実装を担います。
# Title: June 22, 2026 
Link: https://docs.cloud.google.com/release-notes#June_22_2026<br>
ご担当者様

Google Cloudのリリースノートに基づくサービスへの影響調査結果をご報告いたします。
構築済みのApigee XおよびCloud Loggingサービスについて、最新のリリースノート内容を評価し、影響の有無と推奨される対処方法をまとめました。

---

# Apigee X

## Announcement

原文: On June 22nd, 2026, we released an updated version of Apigee (1-17-0-apigee-10).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明:
Apigeeの新しいバージョン(1-17-0-apigee-10)がリリースされました。リリースノートには2026年6月22日と記載されていますが、このリリースの展開（ロールアウト）は本日より開始されており、すべてのGoogle Cloudゾーンで完了するまでに4営業日以上かかる可能性があります。展開が完了するまでは、お客様のApigeeインスタンスで新しい機能や修正が利用できない場合があります。

影響有無:
影響はありません。Apigee Xはマネージドサービスであり、基盤のアップデートはGoogle Cloud側で自動的に実施されます。お客様側で特別な操作は不要です。展開が完了するまで、一部の最新機能や修正が即時には利用できない可能性がありますが、既存のサービス運用に直接的な影響はありません。

対処方法:
特別な対処は不要です。ロールアウトの完了を待機してください。

用語説明:
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォーム。APIの設計、デプロイ、セキュリティ、監視、分析などを一元的に行います。
*   **ロールアウト (Rollout)**: ソフトウェアやサービスの新しいバージョンを、本番環境に段階的に展開していくプロセス。これにより、影響を最小限に抑えつつ新バージョンへの移行が行われます。

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **519996459** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway to patch the following vulnerabilities: - CVE-2026-27143- CVE-2019-14993- CVE-2021-39155- CVE-2021-39156- CVE-2022-23635- CVE-2026-27140- CVE-2026-27144- CVE-2026-29181- CVE-2026-32280- CVE-2026-32281- CVE-2026-32283- CVE-2026-33811- CVE-2026-33814- CVE-2026-34986- CVE-2026-35469- CVE-2026-39820- CVE-2026-39836- CVE-2026-39883- CVE-2026-4046- CVE-2026-42499- CVE-2026-42501- CVE-2026-42504- CVE-2022-31045- CVE-2026-27145- CVE-2026-32282- CVE-2026-32288- CVE-2026-32289- CVE-2026-39350- CVE-2026-39817- CVE-2026-39819- CVE-2026-39823- CVE-2026-39825- CVE-2026-39826- CVE-2026-41413- CVE-2026-42507- CVE-2026-4437- CVE-2026-4438 |
| **N/A** | **Security fix for Apigee infrastructure.** |
[CVE-2026-27143](https://nvd.nist.gov/vuln/detail/CVE-2026-27143)
[CVE-2019-14993](https://nvd.nist.gov/vuln/detail/CVE-2019-14993)
... (以下、すべてのCVEリンク)

説明:
Apigee ingress gatewayとApigeeインフラストラクチャに対する多数のセキュリティ脆弱性（CVEで識別されるもの）の修正が適用されました。これらの修正により、プラットフォーム全体のセキュリティ体制が強化されます。

影響有無:
影響はありません。これらのセキュリティ修正は、Apigeeサービスのセキュリティを向上させるものであり、お客様の既存のApigeeインスタンスに自動的に適用されます。運用上の変更は必要ありません。

対処方法:
特別な対処は不要です。システムは自動的に更新され、セキュリティが強化されます。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアやハードウェアの既知のセキュリティ脆弱性を識別するための国際的な標準識別子。
*   **Ingress Gateway**: 外部からのAPIトラフィックをApigeeインスタンスにルーティングする入り口となるコンポーネント。このゲートウェイが処理するAPIトラフィックに対してセキュリティ脆弱性がないようにパッチが適用されました。

## Fixed

原文:
| Bug ID | Description |
| --- | --- |
| **515788622** | Upgraded the default outbound TLS protocol from TLSv1.2 to TLSv1.3 on JVMs that support it. Per-proxy `<SSLInfo><Protocols>` settings continue to take precedence, and the new `HTTPClient.outbound.tls.protocol` override lets operators force a specific protocol. |
| **184266748** | Fixed an issue where ApigeeDatastore TLS certificate creation could fail in namespaces with longer names when the certificate common name exceeded the 64-byte limit. |
| **286069772** | Added a per-gateway `proxyProtocol.mode` property (strict, permissive, disable) on Apigee ingress gateway components to opt in to HAProxy PROXY-protocol parsing. The property defaults to disable. |
| **N/A** | Updates to infrastructure and libraries. |

説明:
以下の修正と改善が行われました。
*   **デフォルトのアウトバウンドTLSプロトコルがTLSv1.3にアップグレード**: JVMがサポートする場合、Apigeeからの外部接続のデフォルトTLSプロトコルがTLSv1.2からTLSv1.3に引き上げられました。既存のプロキシごとの`<SSLInfo><Protocols>`設定は引き続き優先され、また`HTTPClient.outbound.tls.protocol`プロパティを使用して特定のプロトコルを強制することも可能です。
*   **ApigeeDatastore TLS証明書作成の不具合修正**: 証明書の共通名が64バイトの制限を超えると、名前の長いネームスペースでのApigeeDatastore TLS証明書作成が失敗する問題が修正されました。
*   **Apigee ingress gatewayにPROXYプロトコルモードの追加**: Apigee ingress gatewayコンポーネントに、HAProxy PROXYプロトコル解析を有効にする`proxyProtocol.mode`プロパティ（`strict`, `permissive`, `disable`）が追加されました。このプロパティのデフォルトは`disable`です。
*   **インフラストラクチャおよびライブラリの更新**: 基盤となるインフラストラクチャおよびライブラリの更新が行われました。

影響有無:
*   **TLSプロトコル**: デフォルトのTLSプロトコルが向上し、セキュリティとパフォーマンスが改善されます。お客様の環境で明示的にTLSv1.2以下のプロトコルバージョンを指定している場合は、その設定が優先されるため影響はありません。デフォルト設定を利用している場合は、より新しいTLSv1.3が使用されるようになりますが、通常は透過的に動作します。
*   **TLS証明書作成不具合**: 特定の条件で発生していたTLS証明書作成の問題が修正されます。影響はポジティブであり、該当する問題に直面していたお客様にとっては運用が改善されます。
*   **PROXYプロトコルモード**: 新しい機能追加です。既存の動作には影響ありません。HAProxyなどでPROXYプロトコルを使用している場合に、その解析を有効にするオプションが提供されました。既存のAPIトラフィックに影響を与えるものではなく、必要に応じて設定を有効にできます。
*   **インフラストラクチャ更新**: サービスの安定性、パフォーマンス、セキュリティが向上します。直接的な運用変更は不要です。

対処方法:
*   **TLSプロトコル**: 通常の運用では特別な対処は不要です。もし、Apigeeから接続する外部サービスがTLSv1.3をサポートしていない場合や、特定のTLSプロトコルバージョンに依存する要件がある場合は、`HTTPClient.outbound.tls.protocol`プロパティまたは`<SSLInfo><Protocols>`設定で明示的にバージョンを指定することを検討してください。本番適用前にテスト環境での確認を推奨します。
*   **TLS証明書作成不具合**: 該当する問題に遭遇していた場合、今後の証明書作成が正常に行われるようになります。特別な対処は不要です。
*   **PROXYプロトコルモード**: HAProxyなどの環境でPROXYプロトコルを利用し、Apigee ingress gatewayでその情報を解析したい場合は、この`proxyProtocol.mode`プロパティを適切に設定することを検討してください。

用語説明:
*   **TLSv1.2 / TLSv1.3 (Transport Layer Security)**: インターネット上での安全な通信を確立するための暗号化プロトコル。TLSv1.3は最新かつ最も安全なバージョンの一つです。
*   **JVM (Java Virtual Machine)**: Javaプログラムを実行するための仮想マシン。
*   **`SSLInfo`**: Apigeeのプロキシ設定において、TLS/SSL接続に関する詳細な設定（プロトコル、鍵、証明書など）を指定するために使用されるXML要素。
*   **PROXYプロトコル**: ロードバランサーやプロキシサーバーがバックエンドサーバーに接続する際に、クライアントの元のIPアドレスやポート番号などの接続情報を伝達するためのプロトコル。

---

# Cloud Logging

## Security

原文: If the parent project for a Cloud Storage bucket changes, a log sink stops routing log entries to that bucket. For more information about error messages and recovery options, see Errors routing to Cloud Storage.
[Errors routing to Cloud Storage](https://docs.google.com/logging/docs/export/troubleshoot#errors_exporting_to_cloud_storage)

説明:
Cloud Storageバケットの親プロジェクトが変更された場合、そのバケットにログエントリをルーティングしているログシンクは、ログのルーティングを停止するようになります。エラーメッセージと復旧オプションに関する詳細情報は、提供されたCloud Loggingのトラブルシューティングドキュメントで確認できます。

影響有無:
影響は限定的です。これは、Cloud Storageバケットの親プロジェクトを変更するという特定の操作を行った場合にのみ発生する挙動です。通常運用でCloud Storageバケットの親プロジェクトを変更しない限り、既存のログシンクの動作に影響はありません。この変更は、ログデータの整合性とセキュリティを維持するためのものです。

対処方法:
通常の運用では特別な対処は不要です。
将来的にCloud Storageバケットの親プロジェクトを変更する計画がある場合は、ログシンクが停止する可能性を考慮し、事前のテストと計画が重要です。ログシンクが停止した場合は、[Errors routing to Cloud Storage](https://docs.google.com/logging/docs/export/troubleshoot#errors_exporting_to_cloud_storage)のドキュメントを参照し、ログシンクの再設定や新規作成などの復旧手順を実行してください。

用語説明:
*   **ログシンク (Log Sink)**: Cloud Loggingの機能で、収集されたログエントリをCloud Storage、BigQuery、Pub/Subなどの他のGoogle Cloudサービスや外部サービスにエクスポート（ルーティング）するための設定です。
*   **Cloud Storageバケット**: Google Cloud Storageサービスで、データ（オブジェクト）を保存するための基本的なコンテナ。
*   **親プロジェクト (Parent Project)**: Google Cloudの組織階層において、特定のGCPリソース（この場合、Cloud Storageバケット）が属する上位のプロジェクト。プロジェクトの移動は、リソースに対する権限や課金、ポリシーの継承に影響を与える可能性があります。

---
本件についてご不明な点がございましたら、お気軽にお問い合わせください。