
# Title: October 16, 2025 
Link: https://cloud.google.com/release-notes#October_16_2025<br>
Google Cloudのリリースノートを元に、構築済みのサービスへの影響有無と対処方法について調査結果を報告いたします。

---

# Apigee X

## Announcement
原文: On October 16, 2025, we released an updated version of Apigee (1-16-0-apigee-3).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
Apigeeのバージョン1-16-0-apigee-3がリリースされました。このリリースは2025年10月16日に公開され、Google Cloudの全ゾーンへのロールアウトには4営業日以上かかる可能性があります。ロールアウトが完了するまで、お使いのApigeeインスタンスでは新機能や修正が利用できない場合があります。

影響有無：影響あり
Apigee Xをご利用の場合、自動的に本バージョンへのアップグレードが適用されます。ただし、ロールアウトには時間がかかるため、すぐには新機能や修正が反映されない可能性があります。Google Cloud Composerとは直接関連しないサービスであるため、Composer環境への影響はありません。

対処方法：
特別な対処は不要です。ロールアウトが完了するまでお待ちください。ロールアウト状況については、Apigeeのインスタンスステータスやリリースノートの続報を確認してください。

用語説明：
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォーム。APIの設計、セキュリティ、デプロイ、監視、分析などを一元的に行います。
*   **ロールアウト (Rollout)**: 新しいソフトウェアバージョンや設定を段階的に本番環境に適用していくプロセス。サービスの中断を最小限に抑えながら変更を導入するために用いられます。

## Fixed
### Bug ID: 442501403
原文: Fixed an issue that caused incorrect target latency metrics in Apigee Analytics when a TargetEndpoint is configured with a <LoadBalancer>.

説明：
Apigee Analyticsにおいて、`TargetEndpoint`に`<LoadBalancer>`が設定されている場合に、ターゲットのレイテンシーメトリクスが正しく表示されない問題が修正されました。

影響有無：影響あり（改善）
Apigee Xをご利用で、かつ`TargetEndpoint`でロードバランサー設定を使用している場合、これまで分析データが不正確だった可能性があります。今回の修正により、より正確なレイテンシーデータが取得できるようになり、APIのパフォーマンス監視が改善されます。

対処方法：
特別な対処は不要です。修正が適用され次第、自動的に改善されます。

### Bug ID: 437999897
原文: Reduced the log level for failed geo IP lookups to address excessive log messages for private IP addresses.

説明：
プライベートIPアドレスに対するGeo IPルックアップが失敗した際に発生する過剰なログメッセージを軽減するため、ログレベルが引き下げられました。

影響有無：影響あり（改善）
Apigee Xのログ出力量が削減され、ロギングコストの最適化やログ解析の効率向上が期待できます。

対処方法：
特別な対処は不要です。

### Bug ID: 436323210
原文: Fixed ingress cert keys to allow both `tls.key`/`key` and `tls.crt`/`cert`.

説明：
ApigeeのIngress（APIゲートウェイへの入り口）で使用される証明書キーにおいて、`tls.key`と`key`、`tls.crt`と`cert`の両方のキー形式が許可されるように修正されました。

影響有無：影響なし
既存の証明書設定に影響はなく、Ingress証明書の構成の柔軟性が向上します。

対処方法：
特別な対処は不要です。

### Bug ID: N/A
原文: Updates to security infrastructure and libraries.

説明：
Apigeeの基盤となるセキュリティインフラストラクチャおよびライブラリが更新されました。

影響有無：影響あり（改善）
Apigee環境全体のセキュリティ体制が強化されます。

対処方法：
特別な対処は不要です。

## Security
### Bug ID: 440419558, 433759657
原文: Security fix for Apigee infrastructure. This addresses the following vulnerabilities: - CVE-2025-22868 - CVE-2025-48924 Note: This fix updates a Java library that is included in Apigee. Reliance on Java libraries that are included with Apigee is not supported. Those libraries are for Apigee product functionality only, and there's no guarantee that a library will be available from release to release. For more information, see [Restrictions](https://cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy#Restrictions).

説明：
Apigeeインフラストラクチャに対するセキュリティ修正が適用されました。これにより、以下の2つの共通脆弱性識別子 (CVE) に対応しています。
*   CVE-2025-22868
*   CVE-2025-48924
この修正には、Apigeeに組み込まれているJavaライブラリの更新が含まれます。Apigeeが提供するJavaライブラリへの外部からの依存はサポートされておらず、これらのライブラリはApigee製品機能のみを目的としており、リリース間で利用可能性が保証されない点に注意が必要です。

影響有無：影響あり（改善と注意点）
*   **改善点**: Apigee環境のセキュリティが強化され、既知の脆弱性からの保護が向上します。
*   **注意点**: もしカスタムコード（例: Java Callout）でApigeeに組み込まれたJavaライブラリに直接依存している場合、その使用方法はサポート対象外であり、将来のリリースで互換性が失われるリスクがあります。

対処方法：
*   基本的には自動でセキュリティが強化されるため、特別な対処は不要です。
*   もし、Apigeeのカスタムポリシー（特にJava Callout）で、Apigee内部のJavaライブラリに直接依存している実装がある場合は、Google Cloudが推奨するベストプラクティスに従い、これらの依存関係を見直すことを強く推奨します。通常、Apigeeのポリシーや機能として提供されているものを利用している場合は問題ありません。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されているサイバーセキュリティの脆弱性に関する情報を識別するための国際的な識別子。

---

# Compute Engine

## Changed
原文: Starting with SUSE Linux Enterprise Server (SLES) 16, including variants for SAP, the default file system for the root partition (`/`) is Btrfs changing from the previous default of XFS. For more information, see [File systems in SLES](https://documentation.suse.com/sles/15-SP7/html/SLES-all/cha-filesystems.html#sec-filesystems-major-btrfs-suse) in the SUSE documentation.

説明：
SUSE Linux Enterprise Server (SLES) 16およびそれ以降のバージョン（SAP向けバリアントを含む）において、ルートパーティション (`/`) のデフォルトファイルシステムが、従来のXFSからBtrfsに変更されました。

影響有無：影響なし
*   現在稼働中のCompute Engine VMインスタンスでSLES 15以前のバージョンを使用している場合、既存のファイルシステムには変更はありません。
*   Google Cloud Composer 2は通常、DebianやUbuntuなどのLinuxディストリビューションを基盤としており、SLESは使用されません。そのため、Google Cloud Composer環境への直接的な影響はありません。
*   今後、Compute EngineでSLES 16以降のOSイメージを使用して新規VMインスタンスをデプロイする場合にのみ、この変更が適用されます。

対処方法：
*   もし将来的にCompute EngineでSLES 16以降のVMインスタンスを新規にデプロイする計画がある場合、ルートファイルシステムがBtrfsとなることを認識し、Btrfsの特性（例: スナップショット機能、CoWなど）や運用上の注意点を確認しておくことを推奨します。
*   特定のファイルシステム（例: XFS）を前提としたアプリケーションやスクリプトがある場合は、互換性を事前に確認してください。

用語説明：
*   **SUSE Linux Enterprise Server (SLES)**: SUSE社が開発・提供する商用Linuxディストリビューション。
*   **Btrfs (B-tree file system)**: Linux向けの最新のコピーオンライト (CoW) ファイルシステム。スナップショット、ボリューム管理、データチェックサムなどの機能を持つ。
*   **XFS**: 高性能なジャーナリングファイルシステム。大規模なファイルシステムや並列I/Oに適している。
# Title: October 15, 2025 
Link: https://cloud.google.com/release-notes#October_15_2025<br>
はい、承知いたしました。
Google Cloudのインフラエンジニアとして、提供されたリリースノートに基づき、構築済みのサービスへの影響有無を調査し、簡潔に回答いたします。

---

# Cloud Service Mesh

## Announcement

原文: **1.25.5-asm.7 is now available for in-cluster Cloud Service Mesh.**

 You can now download 1.25.5-asm.7 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.25.5 subject to the list of supported features. Cloud Service Mesh version 1.25.5-asm.7 uses envoy v1.33.10-dev.

[Istio 1.25.5](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.5/)
[supported features](https://cloud.google.com/service-mesh/v1.25/docs/supported-features-in-cluster)
 For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade)

説明: Cloud Service Meshの新しいバージョン「1.25.5-asm.7」がリリースされました。このバージョンはIstio 1.25.5をベースとし、Envoy v1.33.10-devを使用しています。利用可能な機能は[サポートされる機能リスト](https://cloud.google.com/service-mesh/v1.25/docs/supported-features-in-cluster)を参照してください。

影響有無: **影響あり（推奨）**
既存のCloud Service Meshデプロイメントがこのバージョンよりも古い場合、新機能の利用や、次の「Fixed」セクションで説明されるセキュリティ修正の適用のため、アップグレードを検討する契機となります。即座の機能的な変更や互換性の問題は発生しませんが、セキュリティや機能向上を目的とした計画的なアップグレードが推奨されます。

対処方法: 現在のCloud Service Meshのバージョンを確認し、必要に応じて[アップグレードドキュメント](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade)を参照して「1.25.5-asm.7」へのアップグレードを計画・実行してください。

用語説明:
*   **in-cluster Cloud Service Mesh**: GKEクラスタ内にデプロイされるCloud Service Mesh (Anthos Service Mesh) の管理プレーンを指します。
*   **Istio**: サービスメッシュの実装を提供するオープンソースプラットフォームです。
*   **Envoy**: サービスメッシュ内の全てのサービス通信を処理する高性能なプロキシです。

## Fixed

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

説明: Cloud Service Mesh 1.25.5-asm.7には、複数の共通脆弱性識別子（CVE）に対するセキュリティ修正が含まれています。これらの脆弱性は、プロキシ、コントロールプレーン、CNI、およびディストロレスイメージに影響を与える可能性があります。

影響有無: **影響あり（セキュリティ強化）**
既存のCloud Service Meshデプロイメントがこれらの脆弱性の影響を受ける可能性を低減するため、このバージョンへのアップグレードはセキュリティ体制の強化に直結します。

対処方法: 既存のCloud Service Meshが1.25.5-asm.7より古いバージョンの場合、セキュリティリスクを軽減するために速やかにこのバージョンへのアップグレードを検討してください。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されている既知のサイバーセキュリティ脆弱性およびエクスポージャを識別するための標準的な名称です。
*   **Proxy**: サービス間の通信を仲介するコンポーネントで、通常はサイドカープロキシとしてワークロードのPodにデプロイされます。
*   **Control Plane**: サービスメッシュ全体の構成、ポリシー、トラフィックルーティングなどを管理するコンポーネント群です。
*   **CNI (Container Network Interface)**: Kubernetesクラスタ内のコンテナがネットワークに接続するためのプラグイン仕様です。
*   **Distroless**: 最小限のランタイム依存関係しか含まないコンテナイメージで、攻撃対象領域を減らすことを目的としています。

## Announcement

原文: **1.26.4-asm.7 is now available for in-cluster Cloud Service Mesh.**

 You can now download 1.26.4-asm.7 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.26.4 subject to the list of supported features.

[Istio 1.26.4](https://istio.io/latest/news/releases/1.26.x/announcing-1.26.4/)
[supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster)
 For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.26.4-asm.7 uses Envoy v1.34.8-dev.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明: Cloud Service Meshの新しいバージョン「1.26.4-asm.7」がリリースされました。このバージョンはIstio 1.26.4をベースとし、Envoy v1.34.8-devを使用しています。

影響有無: **影響あり（推奨）**
前述の1.25.5-asm.7と同様、既存のCloud Service Meshデプロイメントがこのバージョンよりも古い場合、新機能の利用やセキュリティ修正の適用のため、アップグレードを検討する契機となります。

対処方法: 現在のCloud Service Meshのバージョンを確認し、必要に応じて[アップグレードドキュメント](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)を参照して「1.26.4-asm.7」へのアップグレードを計画・実行してください。

## Fixed

原文: 1.26.4-asm.7 includes the fixes for the following CVEs:

| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| CVE-2024-10963 | Yes | Yes | Yes | - |
| CVE-2025-8058 | Yes | Yes | Yes | Yes |
| CVE-2025-4802 | - | - | - | Yes |
[CVE-2024-10963](https://ubuntu.com/security/CVE-2024-10963)
[CVE-2025-8058](https://ubuntu.com/security/CVE-2025-8058)
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802)

説明: Cloud Service Mesh 1.26.4-asm.7には、複数のCVEに対するセキュリティ修正が含まれています。

影響有無: **影響あり（セキュリティ強化）**
既存のCloud Service Meshデプロイメントがこれらの脆弱性の影響を受ける可能性を低減するため、このバージョンへのアップグレードはセキュリティ体制の強化に直結します。

対処方法: 既存のCloud Service Meshが1.26.4-asm.7より古いバージョンの場合、セキュリティリスクを軽減するために速やかにこのバージョンへのアップグレードを検討してください。

## Announcement

原文: **1.27.1-asm.5 is now available for in-cluster Cloud Service Mesh.**

 You can now download 1.27.1-asm.5 for in-cluster Cloud Service Mesh. It includes the features of Istio 1.27.1 subject to the list of supported features.

[Istio 1.27.1](https://istio.io/latest/news/releases/1.27.x/announcing-1.27/)
[supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster)
 For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh version 1.27.1-asm.5 uses Envoy v1.35.4-dev.

[Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)

説明: Cloud Service Meshの新しいバージョン「1.27.1-asm.5」がリリースされました。このバージョンはIstio 1.27.1をベースとし、Envoy v1.35.4-devを使用しています。

影響有無: **影響あり（推奨）**
前述のバージョンと同様、既存のCloud Service Meshデプロイメントがこのバージョンよりも古い場合、新機能の利用やセキュリティ修正の適用のため、アップグレードを検討する契機となります。

対処方法: 現在のCloud Service Meshのバージョンを確認し、必要に応じて[アップグレードドキュメント](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)を参照して「1.27.1-asm.5」へのアップグレードを計画・実行してください。

## Fixed

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

説明: Cloud Service Mesh 1.27.1-asm.5には、複数のCVEに対するセキュリティ修正が含まれています。

影響有無: **影響あり（セキュリティ強化）**
既存のCloud Service Meshデプロイメントがこれらの脆弱性の影響を受ける可能性を低減するため、このバージョンへのアップグレードはセキュリティ体制の強化に直結します。

対処方法: 既存のCloud Service Meshが1.27.1-asm.5より古いバージョンの場合、セキュリティリスクを軽減するために速やかにこのバージョンへのアップグレードを検討してください。

## Announcement

原文: In-cluster Cloud Service Mesh 1.24 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see Supported versions.

[Supported versions](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)

説明: in-cluster Cloud Service Meshバージョン1.24がサポート対象外となりました。他のバージョンのサポート終了（EOL）日については、[サポートされるバージョン](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions)ドキュメントを参照してください。

影響有無: **重大な影響あり**
もし現在、Cloud Service Mesh 1.24を使用している場合、このバージョンはサポート対象外となり、セキュリティパッチや重要なバグ修正、テクニカルサポートが提供されなくなります。これは運用リスクを大幅に高めます。

対処方法: もし現在Cloud Service Mesh 1.24を使用している場合は、速やかにサポートされているバージョン（1.25.x以降）へのアップグレード計画を立て、実行してください。アップグレードパスと手順については、[Cloud Service Meshのアップグレードドキュメント](https://cloud.google.com/service-mesh/docs/upgrade/upgrade)を参照してください。

用語説明:
*   **EOL (End-of-Life)**: 製品やバージョンのサポートが終了し、それ以降は修正や更新が提供されなくなる期間を指します。

---

# Google Kubernetes Engine

## Changed

原文: GKE cluster versions have been updated.

 **New versions available for upgrades and new clusters.**

 The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.

[GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)

説明: GKEクラスターのバージョンが更新され、新しいバージョンが新規クラスターの作成、既存クラスターのコントロールプレーンおよびノードのアップグレードで利用可能になりました。

影響有無: **間接的な影響あり（要確認）**
Google Cloud Composer 2はGKEクラスターを基盤としています。GKEのバージョンが更新されることで、Composer 2の既存環境に直接的な影響はありませんが、ComposerがサポートするGKEバージョン範囲内であることを継続的に確認する必要があります。提供されているComposer 2.7.1はGKE 1.27.x, 1.28.x, 1.29.x をサポートしています。もしGKEの自動アップグレードが有効で、ComposerがサポートしないGKEバージョンにアップグレードされた場合、Composer環境の安定性に影響が出る可能性があります。

対処方法:
1.  現在利用中のGKEクラスターのバージョンが、Composer 2.7.1がサポートするバージョン範囲（GKE 1.27.x, 1.28.x, 1.29.x）内にあることを確認してください。
2.  GKEクラスターの自動アップグレード設定（リリースチャンネル、メンテナンスウィンドウ、メンテナンス除外設定など）を確認し、Composerのサポート範囲外のバージョンに自動でアップグレードされないよう必要に応じて調整してください。
3.  新しいGKEバージョンでComposer環境の動作検証を行う場合は、ステージング環境などで十分なテストを実施してください。

用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービスです。
*   **Control Plane**: Kubernetesクラスターの管理を行うコンポーネント群（APIサーバー、スケジューラー、コントローラーマネージャーなど）です。
*   **Node**: Kubernetesクラスターでコンテナ化されたワークロードを実行する仮想マシンまたは物理マシンです。

## Security

原文: This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

 To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

 GKE version
Container-Optimized OS version
Details


1.34.1-gke.1431000
cos-beta-125-19216-0-76
cos-beta-125-19216-0-76 release notes

| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.34.1-gke.1431000 | cos-beta-125-19216-0-76 | cos-beta-125-19216-0-76 release notes |
[cos-beta-125-19216-0-76 release notes](https://cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-beta-125-19216-0-76_)

説明: このリリースでは、セキュリティ修正を含む更新されたContainer-Optimized OS (COS) イメージを使用するGKEの新しいバージョンが含まれています。これらの更新は、前回のGKEリリース以降にリリースされた全てのCOSバージョンからの累積的なセキュリティ修正を組み込んでいます。

影響有無: **影響あり（セキュリティ強化）**
GKEノードの基盤となるOSのセキュリティが強化されるため、GKEクラスター全体のセキュリティ体制が向上します。これはポジティブな影響です。

対処方法: GKEクラスターのノードを、更新されたCOSイメージを使用する最新のGKEバージョンにアップグレードすることを推奨します。自動アップグレードが有効になっている場合は、メンテナンスウィンドウ内で自動的に適用されます。

用語説明:
*   **Container-Optimized OS (COS)**: Google Cloud向けに最適化されたコンテナ実行環境に特化したオペレーティングシステムです。

## Changed

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.33.5-gke.1080000 is now the default version for cluster creation in the Extended channel.
- The following versions are now available in the Extended channel:

- 1.28.15-gke.2740000
- 1.28.15-gke.2767000
- 1.29.15-gke.1979000
- 1.29.15-gke.2002000
- 1.30.14-gke.1349000
- 1.31.13-gke.1008000
- 1.32.9-gke.1092000
- 1.33.5-gke.1125000

- The following versions are no longer available in the Extended channel:

- 1.28.15-gke.2697000
- 1.28.15-gke.2751000
- 1.29.15-gke.1936000
- 1.29.15-gke.1989000
- 1.30.14-gke.1336000
- 1.31.12-gke.1220000
- 1.32.9-gke.1010000
- 1.33.4-gke.1350000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.27 to 1.28.15-gke.2730000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:

- 1.28 to 1.28.15-gke.2730000
- 1.29 to 1.29.15-gke.1971000
- 1.31 to 1.31.12-gke.1265000
- 1.32 to 1.32.9-gke.1072000
- 1.33 to 1.33.5-gke.1080000

[1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
... (各バージョンのリンク)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
... (各バージョンのリンク)

説明: GKEのExtendedチャンネルにおいて、新しいバージョンが利用可能になり、一部の古いバージョンは利用できなくなりました。また、Extendedチャンネルにおける新規クラスター作成時のデフォルトバージョンが1.33.5-gke.1080000に設定され、自動アップグレードのターゲットバージョンが更新されました。

影響有無: **間接的な影響あり（要確認）**
利用しているGKEクラスターがExtendedチャンネルに属している場合、自動アップグレードによってバージョンが更新される可能性があります。Composer 2.7.1はGKE 1.27.x, 1.28.x, 1.29.xをサポートしており、Extendedチャンネルで提供される1.30.x以降のバージョンにアップグレードされると、Composerのサポート範囲を超える可能性があります。

対処方法:
1.  現在利用中のGKEクラスターがExtendedチャンネルに属しているか確認してください。
2.  GKEクラスターの現在のバージョンと、Composer 2.7.1がサポートするGKEバージョン範囲（1.27.x, 1.28.x, 1.29.x）を比較してください。
3.  自動アップグレードのターゲットバージョン（例: 1.31, 1.32, 1.33）がComposerのサポート範囲を超える場合は、[メンテナンス除外](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)などの設定を利用して、Composerがサポートするバージョン範囲内でアップグレードが実行されるように制御してください。
4.  GKEバージョンアップに起因する影響を回避するため、Composer環境を定期的に最新バージョンに更新することも検討してください。

用語説明:
*   **GKEリリースチャンネル**: GKEが提供する安定性の異なるバージョンリリースストリーム（Stable, Regular, Rapid, Extended）です。
*   **デフォルトバージョン**: 新規クラスター作成時に自動的に選択されるバージョンです。
*   **自動アップグレード**: GKEがクラスターのコントロールプレーンとノードを自動的に最新バージョンに更新する機能です。
*   **メンテナンス除外 (Maintenance exclusions)**: GKEの自動アップグレードが特定の期間、実行されないように設定する機能です。

## Changed

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.33.5-gke.1080000 is now the default version for cluster creation.
- The following versions are now available:

- 1.31.13-gke.1040000
- 1.32.9-gke.1130000
- 1.33.5-gke.1201000

- The following node versions are now available:

- 1.28.15-gke.2767000
- 1.29.15-gke.2002000
- 1.30.14-gke.1349000
- 1.31.13-gke.1040000
- 1.32.9-gke.1130000
- 1.33.5-gke.1201000

- The following versions are no longer available:

- 1.32.8-gke.1134000
- 1.33.4-gke.1134000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:

- 1.30 to 1.31.12-gke.1265000
- 1.31 to 1.32.9-gke.1072000

# Title: October 14, 2025 
Link: https://cloud.google.com/release-notes#October_14_2025<br>
Google Cloud のリリースノートに対する調査結果を以下に報告します。

---

# Apigee X

## Deprecated

**原文:** `Removal of deprecated Gemini Code Assist @Apigee tool. The Gemini Code Assist @Apigee tool is shut down as of October 14, 2025. See Gemini Code Assist @Apigee tool deprecation for information.`

**説明:**
Apigee向けのAIコード支援ツールである `Gemini Code Assist @Apigee tool` が非推奨となり、**2025年10月14日**をもってサービスが完全に終了することが発表されました。これは、現在このツールを利用してApigee上でのAPI開発を行っているユーザーに影響します。

**影響有無:**
*   **影響あり:**
    *   現在、Apigee X環境において `Gemini Code Assist @Apigee tool` を利用してAPIプロキシや共有フローなどの開発、テスト、デバッグを行っている組織は影響を受けます。
    *   2025年10月14日以降、このツールは利用できなくなるため、代替手段への移行計画が必要です。
*   **影響なし:**
    *   このツールをこれまで利用したことがない組織や、現在Apigee Xを運用していない組織には直接的な影響はありません。

**対処方法:**
*   現在 `Gemini Code Assist @Apigee tool` を利用している場合は、ツールがシャットダウンされる2025年10月14日までに、代替のAI支援ツールや開発手法への移行を検討し、計画を策定してください。
*   Google Cloudの他のAI/MLサービス（例: Vertex AI、またはCloud CodeのGemini機能など）を活用した開発支援の可能性を調査し、Apigee開発プロセスへの統合を検討することをお勧めします。
*   詳細情報については、公式ドキュメントの「Gemini Code Assist @Apigee tool deprecation」を参照してください。

**用語説明:**
*   **Apigee X**: Google Cloudが提供するフルマネージドのAPI管理プラットフォームです。APIの設計、セキュリティ、デプロイ、監視、収益化などを包括的に行い、デジタルエクスペリエンスを加速させます。
*   **Gemini Code Assist**: Google Cloudが提供する、生成AIモデル「Gemini」を活用したコード支援機能の総称です。開発者がコードの生成、補完、説明、デバッグ支援などを受けられます。特定の製品（ここではApigee）に特化した機能も提供されます。

---

# BigQuery

## Announcement

**原文:** `The BigQuery Data Transfer API (bigquerydatatransfer.googleapis.com) is now enabled by default for every new Google Cloud project. This feature is generally available (GA).`

**説明:**
新規に作成される全てのGoogle Cloudプロジェクトにおいて、BigQuery Data Transfer API (bigquerydatatransfer.googleapis.com) がデフォルトで有効化されるようになりました。この機能は一般提供 (GA) されており、安定した状態で利用可能です。

**影響有無:**
*   **影響なし:**
    *   既存のGoogle Cloudプロジェクトには影響しません。これらのプロジェクトでBigQuery Data Transfer APIを利用するには、これまで通り手動での有効化が必要です。
    *   新規プロジェクトでBigQuery Data Transfer APIを利用する予定がある場合、APIの有効化手順が不要となるため、利便性が向上します。
*   **セキュリティ/リソース観点:**
    *   APIがデフォルトで有効化されることによる直接的なセキュリティリスクやリソース消費の増大は通常ありません。API自体は呼び出されない限り課金やリソース消費は発生しません。
    *   不要なAPIが有効になることに対する懸念がある場合でも、BigQuery Data Transfer APIはデータ転送に特化したAPIであり、通常はプロジェクト運用に大きな影響を与えるものではありません。IAMポリシーによって、誰がこのAPIを利用できるかを細かく制御することが可能です。

**対処方法:**
*   特段の対処は不要です。新規プロジェクトでBigQuery Data Transferサービスを利用する際の初期設定が簡素化されます。
*   もし何らかの理由でこのAPIが有効になることを避けたい場合は、プロジェクト作成後にAPIを無効化することも技術的には可能ですが、通常は推奨されません。APIの利用を制限したい場合は、適切なIAMロールとポリシーを設定することが、より推奨されるセキュリティプラクティスです。

**用語説明:**
*   **BigQuery Data Transfer API**: Google Cloud BigQueryへのSaaSアプリケーション（例: Google Ads, YouTube Analytics）、オブジェクトストレージ（Cloud Storage）、データウェアハウス（Teradata, Amazon S3）など、様々なソースからのデータ転送を自動化および管理するためのAPIです。
*   **Generally Available (GA)**: Google Cloudの製品または機能が、安定稼働が保証され、SLA（サービスレベル契約）が適用され、本番環境での利用が推奨される段階であることを示します。

---

# Google Kubernetes Engine

## Issue

**原文:** `In GKE versions 1.32.4-gke.1029000 and later, MountVolume calls for network file system (NFS) volumes might fail with the following error: mount.nfs:rpc.statd is not running but is required for remote locking. This failure can occur if a Pod mounting an NFS volume runs on the same node as an NFS server Pod, and the NFS server Pod starts before the client Pod attempts to mount the volume. This scenario causes a conflict over the rpcbind service, which prevents the service from starting correctly on the node for the client Pod, leading to the mount failure. As a workaround, deploy this DaemonSet on all nodes where you mount the NFS volumes.`

**説明:**
Google Kubernetes Engine (GKE) のバージョン **1.32.4-gke.1029000以降**において、NFS (Network File System) ボリュームのマウントが失敗する既知の問題が報告されています。エラーメッセージは `mount.nfs:rpc.statd is not running but is required for remote locking` です。
この問題は、NFSボリュームをマウントするクライアントPodとNFSサーバーPodが同じGKEノード上で実行され、かつNFSサーバーPodがクライアントPodより先に起動した場合に発生する可能性があります。原因は、`rpcbind` サービスに関する競合により、クライアントPod側のノードでサービスが正しく起動できないことです。
ワークアラウンドとして、NFSボリュームをマウントする全てのノードに特定のDaemonSetをデプロイすることが推奨されています。

**影響有無:**
*   **影響あり:**
    *   運用中のGKEクラスターのバージョンが **1.32.4-gke.1029000以降**である。
    *   GKEクラスター内でNFSボリュームをPodにマウントして利用している。
    *   特に、GKEクラスター内部でNFSサーバーPodを稼働させ、かつNFSクライアントPodがそのNFSサーバーPodと同じノードにスケジューリングされる可能性がある構成の場合、この問題の影響を受けやすくなります。
*   **影響なし:**
    *   上記バージョンより古いGKEクラスターを使用している。
    *   GKEクラスターでNFSボリュームを全く利用していない。
    *   NFSサーバーがGKEクラスターの外部（例: Cloud Filestore、またはオンプレミスNFSサーバーなど）にあり、GKEクラスター内部でNFSサーバーPodを稼働させていない。

**対処方法:**
*   影響を受ける可能性のある環境では、Google Cloudが提供しているワークアラウンドのDaemonSetを、NFSボリュームをマウントする全てのノードにデプロイしてください。
    *   DaemonSetのYAMLファイルは [https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/troubleshooting/nfs-mount-workaround/daemonset.yaml](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/troubleshooting/nfs-mount-workaround/daemonset.yaml) で参照できます。
*   DaemonSetをデプロイする前に、その内容（特に特権要件やリソース消費）を確認し、環境への影響を評価することをお勧めします。
*   将来的にGKEの新しいバージョンでこの問題が修正される可能性があります。GKEのリリースノートを定期的に確認し、修正が提供され次第、DaemonSetの削除を検討してください。

**用語説明:**
*   **NFS (Network File System)**: ネットワーク越しにファイルシステムを共有するための分散ファイルシステムプロトコルです。Linux/Unix環境で広く利用されます。
*   **rpc.statd / rpcbind**: NFSが機能するために必要なRPC (Remote Procedure Call) サービス群の一部です。
    *   `rpcbind` はRPCプログラム番号をポート番号にマッピングする役割を持ち、クライアントがNFSサービスを見つけるために必要です。
    *   `rpc.statd` はNFSサーバーとクライアント間の状態監視（特にロック関連）を担当します。
*   **DaemonSet**: KubernetesのワークロードAPIオブジェクトの一つです。指定されたPodのコピーを、全ての（または一部の）ノード上で動作させることを保証します。システムデーモンやノードレベルのユーティリティのデプロイに適しています。今回のケースでは、NFS関連サービスがノード上で適切に起動するよう調整するために使用されます。
*   **Pod**: Kubernetesでデプロイ可能な最小の計算単位です。1つまたは複数のコンテナ、ストレージリソース、ユニークなネットワークIP、およびコンテナの実行方法をKubernetesに指示するオプションが含まれます。
# Title: October 13, 2025 
Link: https://cloud.google.com/release-notes#October_13_2025<br>
ご担当者様

Google Cloudのリリースノートに基づき、各製品の変更点、影響有無、および対応策について調査結果を以下の通りご報告いたします。

---

# Cloud Storage

## Libraries

### Node.js

#### Changed

原文:
- Common Service: should retry a request failed (#2652) (b38b5d2)
- Implement path containment to prevent traversal attacks (#2654) (08d7abf)

説明：
Cloud StorageのNode.jsクライアントライブラリ`@google-cloud/storage`がバージョン7.17.2に更新されました。この更新には以下の変更が含まれます。
*   一般的なサービスリクエストの失敗時にリトライを試行するように改善されました。これにより、一時的なネットワーク問題などに対する耐性が向上します。
*   パスの包含（path containment）を実装し、ディレクトリトラバーサル攻撃（Traversal Attacks）を防ぐためのセキュリティ対策が強化されました。

影響有無：なし（軽微）
当社の環境ではCloud Composer 2 (Airflow 2.7.3) を利用しており、これはPythonベースのサービスです。Node.jsアプリケーションを直接運用していない限り、このNode.jsクライアントライブラリの変更による直接的な影響はありません。ただし、もしAirflow DAGsからNode.jsアプリケーションを呼び出し、それがCloud Storageと連携している場合は、そのアプリケーションのセキュリティと信頼性が向上する可能性があります。

対処方法：
Node.jsでCloud Storageと連携するアプリケーションを運用している場合は、最新版のクライアントライブラリへのアップデートを検討してください。これにより、アプリケーションの堅牢性とセキュリティが向上します。

用語説明：
*   **クライアントライブラリ (Client Library):** 特定のAPIやサービスと連携するためのSDK (Software Development Kit) の一部。開発者がコード内でサービスを容易に操作できるようにするための事前にビルドされたコード群。
*   **ディレクトリトラバーサル攻撃 (Traversal Attack):** Webアプリケーションなどの脆弱性を利用して、本来アクセスが許可されていないサーバー上のディレクトリやファイルにアクセスしようとする攻撃手法。
*   **リトライ (Retry):** ネットワークの一時的な問題やAPIのレート制限などにより失敗したリクエストを、一定時間後に再試行すること。システムの堅牢性を高めるために用いられる。

### Java

#### Changed

原文:
- **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 (ba84793)
- Update BlobReadSession ScatteringByteChannel projection to use less CPU (#3324) (678fecc)
- Update DefaultRetryContext to trap and forward RejectedExceptionException to onFailure (#3327) (1be31bd)
- Update PCU request building logic to properly clear crc32c and md5 (#3323) (4da9f31)
- Update dependency com.google.apis:google-api-services-storage to v1-rev20250925-2.0.0 (#3313) (ab310eb)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 (#3325) (4d3e3be)
- Update googleapis/sdk-platform-java action to v2.62.3 (#3322) (a5808ea)

説明：
Cloud StorageのJavaクライアントライブラリ`google-cloud-storage`がバージョン2.58.1に更新されました。この更新には、主に以下の修正と依存関係の更新が含まれます。
*   BlobReadSessionの`ScatteringByteChannel`のプロジェクションを更新し、CPU使用率を削減しました。これにより、Blob読み取り時のパフォーマンスが向上する可能性があります。
*   デフォルトのリトライコンテキストが`RejectedExceptionException`を適切に捕捉し、失敗ハンドラーに転送するように改善されました。
*   PCU（Precondition Update）リクエストの構築ロジックが更新され、`crc32c`と`md5`チェックサムが適切にクリアされるように修正されました。これはデータ整合性に関わる重要な修正です。
*   依存するJavaコードジェネレーターや他のGoogle Cloud Java SDKコンポーネントのバージョンが更新されました。

影響有無：なし（軽微）
当社の環境ではCloud Composer 2 (Airflow 2.7.3) を利用しており、これはPythonベースのサービスです。Javaアプリケーションを直接運用していない限り、このJavaクライアントライブラリの変更による直接的な影響はありません。ただし、もしAirflow DAGsからJavaアプリケーションを呼び出し、それがCloud Storageと連携している場合は、そのアプリケーションのパフォーマンス、信頼性、データ整合性が向上する可能性があります。

対処方法：
JavaでCloud Storageと連携するアプリケーションを運用している場合は、特にCPU使用率削減やチェックサム関連の修正が含まれるため、最新版のクライアントライブラリへのアップデートを検討してください。

用語説明：
*   **BlobReadSession:** Cloud Storageからオブジェクト（Blob）を読み取る際のセッション。
*   **ScatteringByteChannel:** Java NIO (New I/O) の一部で、複数のバッファにデータを読み書きするためのインターフェース。
*   **CRC32C (Cyclic Redundancy Check 32-bit Castagnoli):** データ転送や保存中にデータが破損していないかを確認するためのチェックサムアルゴリズムの一つ。Cloud Storageではオブジェクトの整合性検証に用いられる。
*   **MD5 (Message-Digest Algorithm 5):** データの完全性を検証するための一方向ハッシュ関数。
*   **PCU (Precondition Update):** Cloud Storageにおける条件付きリクエストの一部で、オブジェクトの状態（例：特定の世代番号）が前提条件を満たした場合にのみ操作を実行するためのロジック。

### Python

#### Fixed

原文:
- Fixes #1561 by adding an option to specify the entire object checksum for resumable uploads via the `upload_from_string`, `upload_from_file`, and `upload_from_filename` methods (acb918e)

説明：
Cloud StorageのPythonクライアントライブラリ`google-cloud-storage`がバージョン3.4.1に更新されました。この更新には、以下のバグ修正が含まれます。
*   `upload_from_string`、`upload_from_file`、`upload_from_filename`といった再開可能なアップロード（resumable uploads）メソッドにおいて、オブジェクト全体のチェックサムを指定するオプションが追加され、問題#1561が修正されました。これにより、大規模なファイルのアップロード時におけるデータ整合性の検証がより確実になります。

影響有無：軽微（機能改善）
当社が利用しているCloud Composer 2 (Airflow 2.7.3) 環境はPythonベースであり、Airflow DAGsで`google-cloud-storage`ライブラリを間接的または直接的に使用してCloud Storageへのアップロードを行う可能性があります。この修正は機能追加（オプションの追加）とバグ修正であり、既存のコードの動作に破壊的な変更をもたらすものではありません。むしろ、再開可能なアップロードにおけるデータ整合性の向上に寄与するため、ポジティブな影響です。
Cloud Composer環境にデフォルトでインストールされている`google-cloud-storage`のバージョンが3.4.1より古い場合、この修正は適用されません。Airflow DAGsで明示的に`google-cloud-storage`のバージョンを固定している、またはカスタムPyPIパッケージとして指定している場合は、そのバージョンに依存します。

対処方法：
*   現在Cloud Composer環境で使用されている`google-cloud-storage`ライブラリのバージョンを確認してください。（例: Airflowのターミナルから`pip list | grep google-cloud-storage`）
*   もし、Airflow DAGsでCloud Storageへの大規模なファイルアップロード（特に再開可能なアップロード）を行っており、データ整合性についてより厳密な保証が必要な場合は、このライブラリバージョンへのアップデートを検討してください。
*   ライブラリのバージョンアップは、Cloud Composer環境のPyPIパッケージとして最新版を追加するか、将来的なComposerのバージョンアップを待つことになります。PyPIパッケージとして追加する場合は、既存のDAGsへの影響がないか十分にテストしてください。

用語説明：
*   **再開可能なアップロード (Resumable Uploads):** ネットワークの中断などが発生した場合でも、中断された時点からアップロードを再開できるCloud Storageの機能。大規模なファイルや不安定なネットワーク環境でのアップロードに適している。
*   **チェックサム (Checksum):** データのエラー検出のために、データのブロックから計算される短い固定長のデータ。データ転送中にデータが破損したり変更されたりしていないかを確認するために使用される。

---

# Pub/Sub

## Libraries

### Java

#### Changed

原文:
- Support the protocol version in StreamingPullRequest (af40810)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 (af40810)
- Update actions/checkout action to v5 (#2562) (b7fa499)
- Update actions/checkout action to v5 (#2573) (4153dba)
- Update dependency com.google.cloud:google-cloud-bigquery to v2.55.1 (#2566) (66c9ec4)
- Update dependency com.google.cloud:google-cloud-core to v2.60.2 (#2557) (460bcd9)
- Update dependency com.google.cloud:google-cloud-core to v2.60.3 (#2571) (ac2c85a)
- Update dependency com.google.cloud:google-cloud-storage to v2.58.0 (#2561) (0189388)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 (#2572) (0785ee4)
- Update dependency org.assertj:assertj-core to v3.27.6 (#2560) (c82766a)

説明：
Pub/SubのJavaクライアントライブラリ`google-cloud-pubsub`がバージョン1.142.0に更新されました。この更新には、主に以下の機能改善と依存関係の更新が含まれます。
*   `StreamingPullRequest`においてプロトコルバージョンがサポートされるようになりました。これにより、Pub/Subサービスの新しい機能や動作に対応できるようになります。
*   Javaコードジェネレーター（`gapic-generator-java`）やその他のGoogle Cloud SDKコンポーネント、およびテスト関連の依存関係が更新されました。

影響有無：なし（軽微）
当社の環境ではCloud Composer 2 (Airflow 2.7.3) を利用しており、これはPythonベースのサービスです。Javaアプリケーションを直接運用していない限り、このJavaクライアントライブラリの変更による直接的な影響はありません。ただし、もしAirflow DAGsからJavaアプリケーションを呼び出し、それがPub/Subと連携している場合は、そのアプリケーションが新しいプロトコルバージョンを利用できるようになります。

対処方法：
JavaでPub/Subと連携するアプリケーションを運用している場合は、最新版のクライアントライブラリへのアップデートを検討してください。これにより、新しいプロトコルバージョンに関連する機能が利用可能になります。

用語説明：
*   **StreamingPullRequest:** Pub/Subサブスクリプションからメッセージをストリーミング形式で受信するためのリクエスト。クライアントは一つの接続を通じて継続的にメッセージを受信できる。
*   **gapic-generator-java:** Google CloudサービスのAPI定義からJavaクライアントライブラリのコードを自動生成するためのツール。