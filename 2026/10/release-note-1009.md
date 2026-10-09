
# Title: October 06, 2026 
Link: https://docs.cloud.google.com/release-notes#October_06_2026<br>
ご担当者様

Google Cloud のリリースノートに基づき、構築済みのサービスへの影響調査結果をご報告いたします。

---

# Cloud SDK
## Breaking
原文: (記載なし)
説明：リリースノートに「Breaking」カテゴリが示されていますが、具体的な変更内容の記載がありません。通常、このセクションには既存の機能との非互換性や破壊的な変更の詳細が記載されます。
影響有無：記載された情報のみでは影響の有無を判断できません。Cloud SDKのバージョンアップグレード時に、利用している機能に影響がないか詳細なリリースノートや公式ドキュメントで確認する必要があります。
対処方法：現時点では具体的な対処は不要です。Cloud SDKをアップグレードする際には、今回の「Breaking」カテゴリに続く詳細情報が公開されているか確認し、ご利用のスクリプトやツールに影響がないか検証してください。
用語説明：
*   **Cloud SDK**: Google Cloud Platformのサービスをコマンドラインから操作するためのツールセットです。`gcloud`コマンドなどが含まれます。
*   **Breaking Change (破壊的変更)**: 既存のコードや設定が変更なしでは動作しなくなるような、後方互換性のない変更を指します。アップグレード時に特別な注意と対応が必要となります。

---

# Google Kubernetes Engine
## Issue
原文: Starting with GKE version 1.36, the default engine for kube-dns is CoreDNS. For Pod IP DNS queries in the `<a-b-c-d>.<namespace>.pod.cluster.local` format, CoreDNS returns NXDOMAIN if the specified `<namespace>` does not exist. The legacy `kubernetes/dns` implementation skipped checking the existence of the namespace provided in the `<namespace>` segment in these queries.

[CoreDNS](https://coredns.io/)
Queries in the `<a-b-c-d>.<namespace>.pod.cluster.local` format are not part of the
Kubernetes DNS specification.
We can't guarantee that uses outside of those specified in the DNS spec will
remain consistent across releases.

[Kubernetes DNS specification](https://github.com/kubernetes/dns/blob/master/docs/specification.md)
Mitigation:

- **Recommended**: Migrate to supported headless Service DNS records
(`<hostname>.<subdomain>.<namespace>.svc.cluster.local`).
- **Workaround**: Ensure the `<namespace>` specified in the DNS query exists in
the cluster.
説明：
GKEバージョン1.36以降、kube-dnsのデフォルトエンジンがCoreDNSに変更されます。この変更により、`<a-b-c-d>.<namespace>.pod.cluster.local`形式のPod IP DNSクエリにおいて、指定された`<namespace>`が存在しない場合にCoreDNSは`NXDOMAIN`（ドメインが存在しない）を返却するようになります。以前の`kubernetes/dns`の実装では、この形式のクエリで`<namespace>`の存在チェックをスキップしていました。

なお、この`<a-b-c-d>.<namespace>.pod.cluster.local`形式のクエリはKubernetesの公式DNS仕様には含まれていないため、将来的なバージョンにおける動作の一貫性は保証されません。
影響有無：**影響を受ける可能性があります。**
*   **理由**: 構築済みのシステム（特にGoogle Cloud Composer 2 (Compoer version 2.7.1, Airflow version 2.7.3) などGKEを基盤とするサービス）内で、PodのIPアドレスを直接参照するような`<a-b-c-d>.<namespace>.pod.cluster.local`形式のDNSクエリを使用しており、かつ、存在しない名前空間を指定してクエリを実行している場合、`NXDOMAIN`が返され、名前解決に失敗する可能性があります。
*   Google Cloud Composerは通常、内部で利用するKubernetesのDNS解決にこのようなPod IP DNSクエリを直接多用することは稀で、通常はService名などを利用するため、直接的な影響は小さいと考えられます。しかし、カスタムのAirflowオペレーターやユーザーが独自にデプロイしたアプリケーションがこの形式のDNSクエリを使用している場合は、動作に影響が出る可能性があります。
対処方法：
1.  **推奨**: Kubernetes DNS仕様に準拠したHeadless Service DNSレコード（例: `<hostname>.<subdomain>.<namespace>.svc.cluster.local`）への移行を検討してください。これが最も堅牢で将来にわたって安定した方法です。
2.  **回避策**: DNSクエリ内で指定する`<namespace>`が、実際にクラスタ内に存在することを確認してください。
3.  既存のワークロードやカスタムアプリケーションで、該当する`<a-b-c-d>.<namespace>.pod.cluster.local`形式のDNSクエリを利用している箇所がないか、コードレビューやログ監視を通じて特定し、必要に応じて修正を計画してください。
用語説明：
*   **Google Kubernetes Engine (GKE)**: Google Cloud上でマネージドKubernetesクラスタを提供するサービスです。
*   **kube-dns**: Kubernetesクラスタ内でDNSサービスを提供するコンポーネントの総称です。PodやServiceの名前解決を行います。
*   **CoreDNS**: Kubernetes 1.13以降でkube-dnsのデフォルトとなったDNSサーバーです。高い柔軟性と拡張性を持っています。
*   **NXDOMAIN**: DNSクエリに対する応答の一つで、「指定されたドメイン名が存在しない」ことを示します。
*   **Pod IP DNSクエリ (`<a-b-c-d>.<namespace>.pod.cluster.local`)**: PodのIPアドレス（例: `10-0-0-1.default.pod.cluster.local`）を元にDNS解決を行うための非標準的な形式です。Kubernetesの公式DNS仕様には含まれていません。
*   **Headless Service**: Kubernetes Serviceの一種で、Cluster IPを持たず、DNSを通じてServiceが管理するPodのIPアドレスを直接公開します。StatefulSetなどで個別のPodのDNSレコードが必要な場合によく利用されます。
*   **Kubernetes DNS specification**: KubernetesにおけるDNSの名前解決に関する公式の仕様書です。これに準拠することで、将来的な互換性を確保できます。
# Title: October 05, 2026 
Link: https://docs.cloud.google.com/release-notes#October_05_2026<br>
以下がGoogle Kubernetes Engineのリリースノートに関する調査結果です。

# Google Kubernetes Engine
## Deprecated
原文: Starting on July 1, 2026, Identity Service for GKE is deprecated in GKE version 1.36 and earlier. This feature is also unavailable in organizations that were created on or after July 1, 2025. GKE version 1.37 and later don't support Identity Service for GKE. Before you upgrade clusters to 1.37 and later, disable this feature and migrate to Workforce Identity Federation. For more information, see Identity Service for GKE deprecation.

説明：
Google Kubernetes Engine (GKE) の「Identity Service for GKE」機能が非推奨 (deprecated) になります。
具体的には以下のスケジュールと制約があります。

*   **非推奨開始日:** 2026年7月1日以降、GKEバージョン1.36以前のクラスタで非推奨となります。
*   **組織作成日による制限:** 2025年7月1日以降に作成されたGoogle Cloud組織では、この機能は利用できません。
*   **GKEバージョン1.37以降のサポート終了:** GKEバージョン1.37以降では「Identity Service for GKE」はサポートされません。
*   **対応必須:** GKEクラスタをバージョン1.37以降にアップグレードする前に、この機能を無効化し、代替機能である「Workforce Identity Federation」へ移行する必要があります。

詳細については、[Identity Service for GKE deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/identity-service) の公式ドキュメントを参照してください。

影響有無：
**影響あり（潜在的）**

*   **現在「Identity Service for GKE」を利用している場合:** サービス継続に直接的な影響があります。GKE 1.37以降へのアップグレードを検討する前に、または2026年7月1日の非推奨化までに、Workforce Identity Federationへの移行計画と実施が必須です。
*   **現在「Identity Service for GKE」を利用していない場合:** 直接的なサービス中断はありませんが、将来的にGKE 1.37以降へのアップグレードを計画している場合、または今後同様の認証基盤を構築する際には、Workforce Identity Federationを利用する必要があります。
*   **GKEバージョン1.36以前をご利用の場合:** 現在は影響ありませんが、将来のアップグレードパスに影響します。

対処方法：
1.  **利用状況の確認:** まず、現在運用中のGKEクラスタで「Identity Service for GKE」機能が利用されているかを確認します。
2.  **利用している場合:**
    *   公式ドキュメント「[Identity Service for GKE deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/identity-service)」を参照し、Workforce Identity Federationへの移行手順を確認・計画します。
    *   GKEクラスタをバージョン1.37以降にアップグレードする前に、必ず移行を完了させてください。
3.  **利用していない場合:**
    *   現状では特別な対応は不要ですが、この非推奨化のアナウンスを今後のGKEアップグレード計画や認証基盤設計の考慮事項として認識しておくことが重要です。

用語説明：
*   **Identity Service for GKE:** GKEクラスタへの認証を外部のIDプロバイダ (SAML、OIDCなど) と統合するための機能です。これにより、既存の企業IDシステムを使ってKubernetesクラスタへのアクセスを管理できます。
*   **Workforce Identity Federation:** Google Cloud全体で、外部のIDプロバイダ（Okta, Azure AD, Ping Identityなど）からのIDをGoogle Cloudリソースへのアクセスに利用できるようにするサービスです。これにより、Google WorkspaceやCloud Identityのユーザーアカウントを作成することなく、従業員やパートナーがGoogle Cloudリソースにアクセスできるようになります。より柔軟でセキュアな認証・認可を実現します。
*   **非推奨 (Deprecated):** 機能がまだ利用可能ではあるものの、開発が停止されており、将来的にサポートが終了する予定であることを意味します。代替手段への移行が強く推奨されます。
*   **GKE (Google Kubernetes Engine):** Google Cloudが提供するマネージドなKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。