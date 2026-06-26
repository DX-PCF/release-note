
# Title: June 25, 2026 
Link: https://docs.cloud.google.com/release-notes#June_25_2026<br>
# BigQuery
## Change
原文: An updated version of the Simba ODBC driver for BigQuery is now available.
[Simba ODBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_odbc_driver)

説明:
Google BigQueryへの接続に使用されるSimba ODBCドライバーの新しいバージョンがリリースされました。この更新は、通常、バグ修正、パフォーマンス改善、新機能のサポート、またはセキュリティ強化などを含んでいます。BigQueryに外部のBIツールやデータ分析アプリケーションなどからODBCインターフェースを介して接続している環境では、このドライバーが利用されている可能性があります。

影響有無:
**影響あり（利用している場合）**

BigQueryに対しSimba ODBCドライバー経由で接続している既存のアプリケーションやサービスがある場合、ドライバーの更新によって動作に影響が出る可能性があります。特に、セキュリティの脆弱性修正やパフォーマンスの向上、あるいは既存機能の動作変更（Breaking Changeを含む）が含まれる場合があるため、確認が必要です。現在このドライバーを利用していない場合は、直接的な影響はありません。

対処方法:
1.  **利用状況の確認**: 現在、BigQueryへの接続にSimba ODBCドライバーを使用しているかを確認してください。特に、Windows/Linuxサーバー上で動作するレポートツールやデータ連携ミドルウェア、カスタムアプリケーションなどが該当する可能性があります。
2.  **変更内容の確認**: ドライバーを使用している場合は、提供されているリンク先のドキュメントやSimba社のリリースノート/変更ログを確認し、今回の更新に含まれる具体的な変更点（特に破壊的変更や重要なバグ修正、セキュリティアップデート）を把握してください。
3.  **テストと適用計画**: 新しいドライバーを本番環境に適用する前に、開発/ステージング環境で十分なテストを実施し、既存のクエリやデータ連携処理が正常に動作することを確認してください。問題がないことを確認した後、計画的に本番環境への適用を進めることを推奨します。

用語説明:
*   **ODBC (Open Database Connectivity)**: データベースにアクセスするための標準的なAPI（アプリケーションプログラミングインターフェース）です。異なるデータベース管理システム（DBMS）に対して共通のインターフェースを提供し、アプリケーションが特定のデータベースに依存することなくデータにアクセスできるようにします。
*   **Simba ODBC Driver for BigQuery**: Simba Technologies（Progress Softwareの子会社）によって開発された、Google BigQueryにODBCインターフェースを介して接続するためのデータコネクタです。多くのBI（ビジネスインテリジェンス）ツールやデータ分析ツールがODBC接続をサポートしており、これらのツールからBigQueryのデータにアクセスする際に利用されます。
# Title: June 24, 2026 
Link: https://docs.cloud.google.com/release-notes#June_24_2026<br>
# Apigee X
## Announcement

原文:
```
## Apigee Emulator v2.0.1

 On June 24, 2026, we released Apigee Emulator version 2.0.1.

 This is a security-only hotfix release on top of v2.0.0 that addresses
10 security vulnerabilities in the Netty networking library and the embedded
Cassandra Go standard library health-check binary. There are no functional,
API, or configuration changes -- v2.0.1 is a drop-in replacement for v2.0.0.

 The emulator image is available at
Google Artifact Registry.

[Google Artifact Registry](https://console.cloud.google.com/artifacts/docker/apigee-release/us/gcr.io/hybrid%2Fapigee-emulator)
 To upgrade, update the emulator version in your VS Code Cloud Code settings
to `2.0.1`. See
Manage the Apigee Emulator
for details.

[Manage the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#choose_the_emulator_version)
## Security

 **Apigee Emulator**

 This release addresses 10 security vulnerabilities in the Netty networking
library and the embedded Go standard library. All Netty fixes come from
upgrading to `4.1.135.Final`; all Go standard library fixes come from a
Cassandra base image rebuild against Go `1.25.11`.

| CVE | Component |
| --- | --- |
| CVE-2026-50010 | Netty (`netty-handler`) |
| CVE-2026-50020 | Netty (`netty-codec-http`) |
| CVE-2026-50560 | Netty (`netty-codec-http2`) |
| CVE-2026-48043 | Netty (`netty-codec-http2`) |
| CVE-2026-44249 | Netty (`netty-handler`) |
| CVE-2026-45416 | Netty (`netty-handler`) |
| CVE-2026-47244 | Netty (`netty-codec-http2`) |
| CVE-2026-27145 | Go standard library |
| CVE-2026-42504 | Go standard library |
| CVE-2026-42507 | Go standard library |
[CVE-2026-50010](https://nvd.nist.gov/vuln/detail/CVE-2026-50010)
[CVE-2026-50020](https://nvd.nist.gov/vuln/detail/CVE-2026-50020)
[CVE-2026-50560](https://nvd.nist.gov/vuln/detail/CVE-2026-50560)
[CVE-2026-48043](https://nvd.nist.gov/vuln/detail/CVE-2026-48043)
[CVE-2026-44249](https://nvd.nist.gov/vuln/detail/CVE-2026-44249)
[CVE-2026-45416](https://nvd.nist.gov/vuln/detail/CVE-2026-45416)
[CVE-2026-47244](https://nvd.nist.gov/vuln/detail/CVE-2026-47244)
[CVE-2026-27145](https://nvd.nist.gov/vuln/detail/CVE-2026-27145)
[CVE-2026-42504](https://nvd.nist.gov/vuln/detail/CVE-2026-42504)
[CVE-2026-42507](https://nvd.nist.gov/vuln/detail/CVE-2026-42507)
```
説明：
Apigee Emulatorのバージョン2.0.1が2026年6月24日にリリースされました。このバージョンは、v2.0.0に対するセキュリティホットフィックスであり、Nettyネットワークライブラリと、組み込みのCassandra Go標準ライブラリのヘルスチェックバイナリに存在する合計10のセキュリティ脆弱性に対処しています。機能、API、または設定に関する変更は一切なく、v2.0.0の完全なドロップイン（直接置き換え可能）です。新しいエミュレータイメージはGoogle Artifact Registryで入手可能です。アップグレードは、VS CodeのCloud Code設定でエミュレータのバージョンを`2.0.1`に更新することで実施できます。セキュリティ修正には、Nettyを`4.1.135.Final`へ、Go標準ライブラリをGo `1.25.11`に基づきCassandraベースイメージをリビルドすることで対応した複数のCVEが含まれます。

影響有無：
Apigee Emulatorをローカル開発環境として利用している場合、セキュリティ強化の観点から影響があります。機能的な変更や互換性の問題は報告されていないため、既存の開発ワークフローに直接的な負の影響はありません。脆弱性修正により、開発環境のセキュリティ体制が向上します。

対処方法：
Apigee Emulator v2.0.0を使用している場合は、既知のセキュリティ脆弱性に対応するため、速やかにv2.0.1へのアップグレードを強く推奨します。アップグレードは、VS CodeのCloud Code拡張機能の設定内で、エミュレータのバージョンを`2.0.1`に指定するだけで完了します。詳細な手順は、公式ドキュメント「Manage the Apigee Emulator」を参照してください。

用語説明：
*   **Apigee Emulator**: Google Cloud Apigee X (旧Apigee Edge) のAPIゲートウェイ機能をローカル環境でシミュレートし、APIプロキシの開発とテストをオフラインで可能にするツールです。VS CodeのCloud Code拡張機能を通じて提供されます。
*   **Netty**: 高性能なネットワークアプリケーション（特にクライアントとサーバ）を開発するための非同期イベント駆動型ネットワークアプリケーションフレームワークです。Javaで実装されており、多くのJavaベースのサービスで利用されています。
*   **Cassandra**: Apache Cassandraは、高いスケーラビリティと可用性を持つ、オープンソースの分散型NoSQLデータベースです。大規模なデータセットを複数のサーバーに分散して保存し、障害耐性を提供します。
*   **Go standard library**: Go言語の標準ライブラリは、ネットワーク通信、ファイルI/O、データ処理、暗号化など、Go言語でアプリケーションを構築するために必要な基本的な機能やツールを提供する組み込みパッケージのセットです。
*   **Hotfix**: ソフトウェア製品のリリース後に発見された、緊急性の高いバグやセキュリティ脆弱性を修正するために、迅速にリリースされるパッチやアップデートのことです。
*   **Drop-in replacement**: 既存のソフトウェアコンポーネントやシステムを、設定やコードの変更をほとんど、あるいは全く行わずにそのまま置き換えることができるもののことを指します。
*   **CVE (Common Vulnerabilities and Exposures)**: サイバーセキュリティの脆弱性を識別し、公開するための標準的な命名規則です。各CVEは特定のセキュリティ脆弱性に対して一意の識別子を付与し、情報共有と追跡を容易にします。
# Title: June 23, 2026 
Link: https://docs.cloud.google.com/release-notes#June_23_2026<br>
優秀なインフラエンジニアの皆様、お疲れ様です。
Google Cloudの最新リリースノートに基づき、構築済みのサービスへの影響有無について調査結果を報告いたします。

---

# Cloud SDK
## Change
原文: (リリースノートに具体的な変更内容の記載なし)

説明：
Cloud SDKの変更カテゴリに「Change」と記載されていますが、具体的な変更内容はリリースノートに明記されていません。一般的にSDKの変更は、新機能の追加、既存機能の改善、バグ修正などが含まれます。

影響有無：
**不明**。具体的な変更内容が不明であるため、現在の環境への影響を断定することはできません。通常、SDKの変更は後方互換性が保たれることが多いですが、稀に破壊的な変更が含まれる可能性もゼロではありません。

対処方法：
現在利用しているCloud SDKのバージョンと、このリリースノートの対象バージョンが一致するか確認してください。もし自動更新などでバージョンが上がる場合、利用中のスクリプトやツールとの互換性を念のため確認することを推奨します。

用語説明：
なし (Cloud SDKは一般的な用語のため)

---

# Cloud Service Mesh

## Security
原文:
**1.29.5-asm.3 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in
GCP-2026-040.

[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.29.5-asm.3 uses Envoy v1.37.5-dev.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)

## Fixed
原文:
This patch release also contain the fixes for the following CVEs:

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

説明：
インクラスターデプロイメントのCloud Service Meshバージョン 1.29.5-asm.3 がリリースされました。このパッチリリースには、[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)に記載されているセキュリティ脆弱性の修正が含まれています。また、上記の複数のCVE（共通脆弱性識別子）に対する修正も含まれており、特にSeverityがHigh (8.8) の[CVE-2026-45447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-45447)が含まれます。このバージョンはEnvoy v1.37.5-devを使用します。

影響有無：
**あり**。現在、Cloud Service Meshのインクラスターデプロイメントを利用している場合、本リリースで修正されたセキュリティ脆弱性（GCP-2026-040および関連CVE）の影響を受ける可能性があります。特に、深刻度の高い脆弱性が含まれているため、速やかな対応が推奨されます。

対処方法：
現在運用中のCloud Service Meshがインクラスターデプロイメントであり、かつバージョンが1.29.5-asm.3より古い場合は、速やかに1.29.5-asm.3へのアップグレードを検討してください。アップグレード手順については、リリースノートに記載されている[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade)ドキュメントを参照してください。

用語説明：
*   **In-cluster Cloud Service Mesh**: ユーザーがGoogle Kubernetes Engine (GKE) クラスタ内にCloud Service Mesh (Istio) のコントロールプレーンおよびデータプレーンのコンポーネントをデプロイして運用する形態を指します。Googleによってコントロールプレーンが管理されるマネージド版（Anthos Service Mesh）とは異なります。
*   **CVE (Common Vulnerabilities and Exposures)**: 既知のサイバーセキュリティの脆弱性や露出を一意に識別するための、共通の国際的な識別子です。
*   **Envoy**: Cloud Service Meshのデータプレーンとして機能する、高性能なオープンソースのエッジおよびサービスプロキシです。

---

## Security
原文:
**1.28.9-asm.2 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in
GCP-2026-040.

[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.28.9-asm.2 uses Envoy v1.36.9-dev.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)

## Fixed
原文:
This patch release also contain the fixes for the following CVEs:

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

説明：
インクラスターデプロイメントのCloud Service Meshバージョン 1.28.9-asm.2 がリリースされました。このパッチリリースには、GCP-2026-040に記載されているセキュリティ脆弱性の修正と、上記の複数のCVEに対する修正が含まれています。このバージョンはEnvoy v1.36.9-devを使用します。

影響有無：
**あり**。上記1.29.5-asm.3と同様に、現在Cloud Service Meshのインクラスターデプロイメントを利用しており、本リリースで修正されたセキュリティ脆弱性の影響を受ける可能性があります。

対処方法：
現在運用中のCloud Service Meshがインクラスターデプロイメントであり、かつバージョンが1.28.9-asm.2より古い場合は、速やかに1.28.9-asm.2へのアップグレードを検討してください。アップグレード手順については、リリースノートに記載されている[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade)ドキュメントを参照してください。

用語説明：
上記Cloud Service Mesh 1.29.5-asm.3と同様。

---

## Security
原文:
**1.27.9-asm.8 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in
GCP-2026-040.

[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
For details on upgrading Cloud Service Mesh, see
Upgrade Cloud Service Mesh. Cloud Service
Mesh 1.27.9-asm.8 uses Envoy v1.35.13-dev.

[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade)

## Fixed
原文:
This patch release also contain the fixes for the following CVEs:

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

説明：
インクラスターデプロイメントのCloud Service Meshバージョン 1.27.9-asm.8 がリリースされました。このパッチリリースには、GCP-2026-040に記載されているセキュリティ脆弱性の修正と、上記の複数のCVEに対する修正が含まれています。このバージョンはEnvoy v1.35.13-devを使用します。

影響有無：
**あり**。上記1.29.5-asm.3、1.28.9-asm.2と同様に、現在Cloud Service Meshのインクラスターデプロイメントを利用しており、本リリースで修正されたセキュリティ脆弱性の影響を受ける可能性があります。

対処方法：
現在運用中のCloud Service Meshがインクラスターデプロイメントであり、かつバージョンが1.27.9-asm.8より古い場合は、速やかに1.27.9-asm.8へのアップグレードを検討してください。アップグレード手順については、リリースノートに記載されている[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade)ドキュメントを参照してください。

用語説明：
上記Cloud Service Mesh 1.29.5-asm.3と同様。

---

## Security
原文:
The following images are now rolling out for managed Cloud Service Mesh:

- Sidecar version 1.21.6-asm.38, is rolling out to the rapid release channel.
- Sidecar version 1.20.8-asm.88 is rolling out to the regular release channel.
- Sidecar version 1.19.10-asm.78 is rolling out to the stable release channel.

These patch releases contain the fix for the vulnerability listed in
GCP-2026-040.

[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)
These rollouts will preempt those previously announced on
June 12, 2026.

[June 12, 2026](#June_12_2026)

説明：
マネージドCloud Service Mesh (Anthos Service Mesh) 向けに、[GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040)の脆弱性修正を含むサイドカーイメージが各リリースチャネルで順次ロールアウトされています。具体的には、rapidチャネル向けに1.21.6-asm.38、regularチャネル向けに1.20.8-asm.88、stableチャネル向けに1.19.10-asm.78が提供されます。これらのロールアウトは、以前2026年6月12日にアナウンスされたものを上書きするものです。

影響有無：
**あり（ポジティブな影響）**。マネージドCloud Service Meshを利用している場合、これらのセキュリティ修正はGoogle Cloudによって自動的に適用されます。これにより、ユーザー側の明示的な操作なしに、サービスメッシュ環境が既知の脆弱性から保護されます。

対処方法：
マネージドCloud Service MeshはGoogle Cloudによって自動的に更新されるため、ユーザー側での明示的な操作は通常不要です。しかし、サイドカーインジェクションが有効になっているワークロードや、アプリケーションの挙動に影響がないか、アップデート後も監視を続けることを推奨します。

用語説明：
*   **Managed Cloud Service Mesh**: Google Cloudがコントロールプレーンの運用を管理するCloud Service Mesh (Anthos Service Mesh) の形態です。これにより、ユーザーはデータプレーン（サイドカープロキシ）の管理に注力できます。
*   **Sidecar**: アプリケーションコンテナと一緒にKubernetes Pod内にデプロイされる、サービスメッシュの機能（トラフィックルーティング、ポリシー適用、メトリクス収集など）を提供するプロキシコンテナです。
*   **Release Channel (Rapid, Regular, Stable)**: Google Kubernetes Engine (GKE) やAnthos Service MeshなどのGoogle Cloudサービスにおいて、リリースされる機能の頻度と安定性のレベルを示すチャネルです。Rapidは最新機能が早く提供されますが安定性は低い可能性があり、Stableは最も安定性が高いです。

---

# Google Kubernetes Engine

## Issue
原文:
For GKE cluster version 1.34.1-gke.3899001 (sidecar mounter image version
1.21.9) and later affected versions, Cloud Storage FUSE volumes might fail to
mount if the GKE metadata service isn't ready when the Cloud Storage FUSE
sidecar initiates.

When this issue occurs, you might see the following error:

Additionally, the `gcsfuse-sidecar` container displays the following error:

**Mitigation**

To resolve this issue, perform one of the following mitigations:

- Upgrade your cluster to one of the following fixed GKE versions:

- `1.34.8-gke.1218000` or later
- `1.35.3-gke.2347000` or later
- `1.36.0-gke.1266000` or later.

- Create an init container in your Pod that validates metadata service
availability.
- Manually inject the sidecar to ensure the sidecar is blocked by an init
container.

Upgrade your cluster to one of the following fixed GKE versions:

- `1.34.8-gke.1218000` or later
- `1.35.3-gke.2347000` or later
- `1.36.0-gke.1266000` or later.

Create an init container in your Pod that validates metadata service
availability.

Manually inject the sidecar to ensure the sidecar is blocked by an init
container.

For more information, see the Cloud Storage FUSE CSI driver troubleshooting
guide.

[Cloud Storage FUSE CSI driver troubleshooting
guide](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md#limitations)

説明：
GKEクラスタバージョン 1.34.1-gke.3899001（および影響を受けるそれ以降のバージョン）において、Cloud Storage FUSEサイドカーが初期化される際にGKEメタデータサービスがまだ準備できていない場合、Cloud Storage FUSEボリュームのマウントに失敗する可能性がある問題が確認されました。これにより、Podの起動エラーが発生する可能性があります。

影響有無：
**あり**。現在、GKEクラスタでCloud Storage FUSEボリュームを使用しており、対象となる影響を受けるGKEバージョン（1.34.1-gke.3899001 から修正バージョン未満）を利用している場合、この問題によりボリュームのマウントが失敗し、アプリケーションの起動や動作に支障をきたす可能性があります。

対処方法：
以下のいずれかの方法で対処してください。
1.  **GKEクラスタのアップグレード**: クラスタを修正済みのGKEバージョン（`1.34.8-gke.1218000`以降、`1.35.3-gke.2347000`以降、または`1.36.0-gke.1266000`以降）にアップグレードすることを強く推奨します。
2.  **Init Containerの導入**: Pod内にメタデータサービスの可用性を検証するinitコンテナを作成し、
# Title: June 22, 2026 
Link: https://docs.cloud.google.com/release-notes#June_22_2026<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、構築済みのサービスへの影響有無を調査し、簡潔に回答いたします。

---

# Apigee X

## Announcement

原文: On June 22nd, 2026, we released an updated version of Apigee (1-17-0-apigee-10).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigee X の新しいバージョン (1-17-0-apigee-10) が2026年6月22日にリリースされました。このリリースは本日より段階的に展開（ロールアウト）が開始されており、すべてのGoogle Cloudゾーンへの適用完了には4営業日以上かかる可能性があります。そのため、お客様のApigeeインスタンスに新機能や修正が反映されるまで、時間がかかる場合があります。

影響有無: 影響なし。
これは新しいバージョンがリリースされたことのアナウンスであり、Apigee Xサービス自体はGoogle Cloudによって管理・運用されているため、お客様側で特別な操作は必要ありません。新機能や修正が自動的に適用されるのを待つことになります。

対処方法: 特になし。
ロールアウトの完了を待機してください。新しい機能の利用や修正の恩恵を享受できます。

用語説明:
*   **ロールアウト (Rollout)**: 新しいソフトウェアバージョンや機能が、システム全体に段階的に適用されていくプロセスです。サービス中断を最小限に抑えるために、一度に全てではなく、時間をかけて徐々に展開されます。
*   **Google Cloud zones**: Google Cloudリソースが物理的に配置される地理的なエリア内の論理的な分離単位です。可用性向上のために、各リージョンには複数のゾーンが存在します。

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **519996459** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway to patch the following vulnerabilities: - CVE-2026-27143- CVE-2019-14993- CVE-2021-39155- CVE-2021-39156- CVE-2022-23635- CVE-2026-27140- CVE-2026-27144- CVE-2026-29181- CVE-2026-32280- CVE-2026-32281- CVE-2026-32283- CVE-2026-33811- CVE-2026-33814- CVE-2026-34986- CVE-2026-35469- CVE-2026-39820- CVE-2026-39836- CVE-2026-39883- CVE-2026-4046- CVE-2026-42499- CVE-2026-42501- CVE-2026-42504- CVE-2022-31045- CVE-2026-27145- CVE-2026-32282- CVE-2026-32288- CVE-2026-32289- CVE-2026-39350- CVE-2026-39817- CVE-2026-39819- CVE-2026-39823- CVE-2026-39825- CVE-2026-39826- CVE-2026-41413- CVE-2026-42507- CVE-2026-4437- CVE-2026-4438 |
| **N/A** | **Security fix for Apigee infrastructure.** |
[CVEs list and links omitted for brevity in原文 but implied to be present]

説明: Apigee のイングレスゲートウェイおよび基盤となるインフラストラクチャに対して、複数のセキュリティ脆弱性（CVEs）の修正が適用されました。これにより、サービスが強化され、既知の脆弱性からの保護が図られます。

影響有無: 影響なし。
これはサービス提供者側で自動的に適用されるセキュリティ修正であり、お客様のApigee利用環境やAPI動作に直接的な影響はありません。むしろ、セキュリティ体制が向上するというポジティブな影響があります。

対処方法: 特になし。
Google Cloudによってセキュリティパッチが適用されるため、お客様側でのアクションは不要です。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: 広く認知されている情報セキュリティ脆弱性や露出に一意の識別子を付与し、カタログ化したものです。これにより、セキュリティ上の問題が共通の識別子で参照・管理できるようになります。
*   **イングレスゲートウェイ (Ingress Gateway)**: 外部からのトラフィックがサービスに入る際の入口となるコンポーネントです。Apigeeにおいては、クライアントからのAPIリクエストを受け付ける役割を担います。

## Fixed

原文:
| Bug ID | Description |
| --- | --- |
| **515788622** | Upgraded the default outbound TLS protocol from TLSv1.2 to TLSv1.3 on JVMs that support it. Per-proxy `<SSLInfo><Protocols>` settings continue to take precedence, and the new `HTTPClient.outbound.tls.protocol` override lets operators force a specific protocol. |
| **184266748** | Fixed an issue where ApigeeDatastore TLS certificate creation could fail in namespaces with longer names when the certificate common name exceeded the 64-byte limit. |
| **286069772** | Added a per-gateway `proxyProtocol.mode` property (strict, permissive, disable) on Apigee ingress gateway components to opt in to HAProxy PROXY-protocol parsing. The property defaults to disable. |
| **N/A** | Updates to infrastructure and libraries. |

### Bug ID 515788622

説明: ApigeeのアウトバウンドTLSプロトコルのデフォルトが、JVMがサポートしている場合はTLSv1.2からTLSv1.3にアップグレードされました。既存のAPIプロキシごとの`<SSLInfo><Protocols>`設定は引き続き優先されます。また、`HTTPClient.outbound.tls.protocol`という新しいプロパティを使用することで、特定のプロトコルを強制的に使用する設定が可能になりました。

影響有無: 影響の可能性あり。
*   **ポジティブな影響**: デフォルトでTLSv1.3が使用されることで、セキュリティと通信パフォーマンスの向上が期待されます。
*   **ネガティブな影響**: Apigeeから接続する外部システムがTLSv1.3に対応していない場合、接続に問題が発生する可能性があります。ただし、プロキシごとの設定が優先される点、および新しい`HTTPClient.outbound.tls.protocol`で特定のTLSバージョンを明示的に指定できるため、互換性の問題は回避可能です。

対処方法:
1.  Apigeeから外部システムへのアウトバウンドTLS接続を行っている場合、接続先のTLSv1.3対応状況を確認してください。
2.  もしTLSv1.3非対応のシステムへの接続で問題が発生した場合、Apigeeプロキシの`<SSLInfo><Protocols>`設定を見直すか、新しく追加された`HTTPClient.outbound.tls.protocol`プロパティを使用して、TLSv1.2などの特定のプロトコルを明示的に設定してください。詳細はApigeeの公式ドキュメント（[Apigee documentation](https://cloud.google.com/apigee/docs)）を参照し、`HTTPClient.outbound.tls.protocol`の構成方法を確認してください。

用語説明:
*   **TLS (Transport Layer Security)**: インターネット上での通信を暗号化し、データの機密性、完全性、認証性を保証するためのセキュリティプロトコルです。TLSv1.3は最新のバージョンであり、TLSv1.2と比較してセキュリティとパフォーマンスが向上しています。
*   **JVM (Java Virtual Machine)**: Javaプログラムを実行するためのソフトウェア仮想マシンです。

### Bug ID 184266748

説明: Kubernetesの名前空間の長さが原因で、ApigeeDatastoreのTLS証明書作成時に、証明書の共通名が64バイトの制限を超えて失敗する問題が修正されました。

影響有無: 影響なし。
これは特定の条件下で発生していたバグの修正であり、お客様のApigeeDatastoreのTLS証明書作成プロセスが過去にこの問題で影響を受けていなければ、直接的な影響はありません。もし影響を受けていた場合は、この修正により問題が解決されます。

対処方法: 特になし。
もし過去にこの問題に遭遇していた場合、今後のApigeeDatastoreのTLS証明書作成が正常に行われることを期待できます。

用語説明:
*   **ApigeeDatastore**: Apigee内部で使用されるデータストアシステムです。
*   **TLS証明書 (TLS Certificate)**: TLSプロトコルで通信相手の身元を認証し、安全な暗号化通信を確立するために使用されるデジタル証明書です。
*   **共通名 (Common Name / CN)**: TLS証明書に含まれる重要なフィールドの一つで、証明書が発行されたエンティティ（例: ホスト名、ドメイン名）を示します。
*   **Kubernetes namespace**: Kubernetesクラスター内のリソースを論理的に分割し、管理するためのメカニズムです。

### Bug ID 286069772

説明: Apigeeのイングレスゲートウェイコンポーネントに、HAProxy PROXYプロトコルの解析を有効化するためのゲートウェイごとのプロパティ`proxyProtocol.mode` (`strict`, `permissive`, `disable`) が追加されました。このプロパティのデフォルト値は`disable`（無効）です。

影響有無: 影響なし。
新しい機能が追加されましたが、デフォルトが無効であるため、既存の運用に意図しない変更は発生しません。HAProxy PROXYプロトコルを使用する環境で、Apigeeイングレスゲートウェイがクライアントの真のIPアドレス情報を取得する必要がある場合に、この機能を明示的に有効化できます。

対処方法:
HAProxy PROXYプロトコルを使用している環境で、イングレスゲートウェイがクライアントの真のIPアドレス情報を正確に取得する必要がある場合、`proxyProtocol.mode`プロパティを`strict`または`permissive`に設定することを検討してください。設定方法の詳細は、Apigeeの公式ドキュメント（[Apigee documentation](https://cloud.google.com/apigee/docs)）を参照してください。

用語説明:
*   **HAProxy PROXYプロトコル (PROXY protocol)**: ロードバランサーやプロキシサーバーを介して接続される際に、クライアントの実際のIPアドレスやポート番号などの接続メタデータを、アプリケーションプロトコルデータストリームの先頭に付加して後続のサーバーに伝えるためのプロトコルです。

### N/A

説明: Apigeeの基盤インフラストラクチャおよび利用されているライブラリのアップデートが行われました。

影響有無: 影響なし。
これは一般的なメンテナンスと改善であり、通常お客様に直接的な影響はありません。サービスの安定性、セキュリティ、パフォーマンスの向上に寄与します。

対処方法: 特になし。

用語説明:
*   **インフラストラクチャ (Infrastructure)**: ITシステムを構成するハードウェア、ソフトウェア、ネットワークなどの基盤となる要素です。
*   **ライブラリ (Library)**: ソフトウェア開発において、特定の機能を提供する再利用可能なコードの集合体です。

---

# Cloud Logging

## Security

原文: If the parent project for a Cloud Storage bucket changes, a log sink stops routing log entries to that bucket. For more information about error messages and recovery options, see Errors routing to Cloud Storage.

説明: Cloud Storage バケットの親プロジェクトが変更された場合、そのバケットへのログエントリーのルーティングが、関連するログシンクによって停止されるようになりました。エラーメッセージと復旧オプションに関する詳細情報は、提供されたドキュメントを参照してください。

影響有無: 影響の可能性あり。
*   **既存のログルーティングへの影響**: お客様のCloud Loggingにおいて、ログシンクがCloud Storageバケットにログをエクスポートしており、かつ将来的にそのCloud Storageバケットの親プロジェクトを変更する可能性がある場合、ログのルーティングが中断し、ログが失われる可能性があります。
*   **セキュリティの強化**: この変更は、プロジェクトの変更に伴う意図しないデータ露出やアクセス権限の不整合を防ぐためのセキュリティ強化策と考えられます。

対処方法:
1.  現在Cloud Loggingのログシンクを使用してCloud Storageバケットにログをエクスポートしている場合は、エクスポート先のCloud Storageバケットの親プロジェクトを安易に変更しないように運用してください。
2.  もしやむを得ずCloud Storageバケットの親プロジェクトを変更する必要がある場合は、**変更前に既存のログシンクを一時停止または削除し、プロジェクト変更後に新しいログシンクを再作成するなどの計画的な対応が必須となります**。
3.  具体的なエラーメッセージや復旧オプションについては、以下のGoogle Cloud公式ドキュメントを事前に確認し、対応計画を策定してください。
    *   [Errors routing to Cloud Storage](https://cloud.google.com/logging/docs/export/troubleshoot#errors_exporting_to_cloud_storage)

用語説明:
*   **Cloud Logging**: Google Cloudが提供するフルマネージドのログ管理サービスで、アプリケーションやGoogle Cloudサービスのログを収集、保存、分析できます。
*   **ログシンク (Log Sink)**: Cloud Loggingで収集されたログエントリーを、Cloud Storage、BigQuery、Pub/Subなどの他のGoogle Cloudサービスにエクスポート（ルーティング）するための設定です。
*   **Cloud Storage バケット (Cloud Storage Bucket)**: Google Cloud Storageにおけるデータの格納単位です。
*   **親プロジェクト (Parent Project)**: Google Cloudリソースが属するGoogle Cloudプロジェクトを指します。すべてのGoogle Cloudリソースはいずれかのプロジェクトに属しています。

---