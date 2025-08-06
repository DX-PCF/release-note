
# Title: August 05, 2025 
Link: https://cloud.google.com/release-notes#August_05_2025<br>
# Google Kubernetes Engine
## Fixed
原文: A fix is available for an issue in which the Compute Engine Persistent Disk CSI driver failed with an `invalid cpuString` error on GKE nodes that used custom machine types. This issue prevented successful attachment and mounting of Persistent Disk volumes on affected nodes. The fix is available in the following GKE versions:
- 1.31.10-gke.1034000 and later
- 1.32.4-gke.1698000 and later
- 1.33.1-gke.1386000 and later

説明:
このリリースは、Google Kubernetes Engine (GKE) における既知の不具合に対する修正です。具体的には、カスタムマシンタイプを使用するGKEノードにおいて、Compute Engine Persistent Disk CSIドライバが `invalid cpuString` エラーで失敗するという問題が解決されました。この問題により、影響を受けるノードではPersistent Diskボリュームのアタッチやマウントが正常に行えませんでした。この修正は、GKEバージョン1.31.10-gke.1034000以降、1.32.4-gke.1698000以降、および1.33.1-gke.1386000以降で利用可能です。

影響有無:
**影響あり（条件付き）**
- 貴社のGKEクラスタがカスタムマシンタイプを使用しており、かつ現在のGKEバージョンが上記の修正バージョンよりも古い場合、本問題の影響を受ける可能性があります。
- 既にこの問題に遭遇している場合は、この修正によって解消されます。
- 標準マシンタイプのみを使用しているクラスタ、または既に上記の修正バージョン以降にアップグレード済みのクラスタは影響を受けません。

対処方法:
- 現在カスタムマシンタイプを使用しており、かつGKEバージョンが上記の修正バージョンより古い場合、影響を回避または解消するために、GKEクラスタを最新の安定版、または上記修正バージョン以降のバージョンにアップグレードすることを推奨します。
- クラスタのアップグレードは計画的に実施し、ダウンタイムが発生しないようPod Disruption Budget (PDB) の設定やワークロードの冗長化を考慮してください。
- アップグレード計画の詳細は、[GKE のアップグレード](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrades) を参照してください。

用語説明:
- **Compute Engine Persistent Disk CSI driver**: GKEクラスタがCompute Engineの永続ディスク（Persistent Disk）を、Kubernetesの永続ボリューム（Persistent Volume）として利用するために必要なインターフェースを提供するドライバです。Container Storage Interface (CSI) 標準に準拠しています。
- **`invalid cpuString` error**: CPU情報の文字列解析に失敗した際に発生するエラーコードの一つで、GKEノードのVMインスタンスに関するCPU構成情報の処理に問題があったことを示唆します。
- **Custom machine types**: Compute Engineにおいて、定義済みのマシンタイプ（例: e2-standard-4）ではなく、ユーザーがvCPU数とメモリサイズを自由に組み合わせて作成する仮想マシンインスタンスのタイプです。特定のワークロード要件に最適化するために利用されます。
- **Persistent Disk volumes**: Google Cloudの永続ストレージサービスであるPersistent Diskを、KubernetesのPodがデータ保存に使用できるように抽象化したストレージリソースです。Podが再起動または再スケジュールされてもデータが保持されます。
# Title: August 04, 2025 
Link: https://cloud.google.com/release-notes#August_04_2025<br>
# BigQuery
## Changed
原文:
### Libraries
 A weekly digest of client library updates from across the Cloud SDK.

[Cloud SDK](https://cloud.google.com/sdk)
### Java

### Changes for google-cloud-bigquery

[google-cloud-bigquery](https://github.com/googleapis/java-bigquery)
[2.54.0](https://github.com/googleapis/java-bigquery/compare/v2.53.0...v2.54.0)
- **bigquery:** Add OpenTelemetry Samples (#3899) (e3d9ed9)
- **bigquery:** Add otel metrics to request headers (#3900) (4071e4c)

[#3899](https://github.com/googleapis/java-bigquery/issues/3899)
[e3d9ed9](https://github.com/googleapis/java-bigquery/commit/e3d9ed92ca5d9b58b5747960d74f895ed8733ebf)
[#3900](https://github.com/googleapis/java-bigquery/issues/3900)
[4071e4c](https://github.com/googleapis/java-bigquery/commit/4071e4cb2547b236183fd4fbb92c73f074cf2fa0)
- update dependency com.google.cloud:google-cloud-bigquerystorage-bom to v3.16.1 (#3912) (https://github.com/googleapis/java-bigquery/commit/bb6f6dcb90b1ddf72e630c4dc64737cf2c2ebd2e)
- Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.70.0 (#3890) (84207e2)
- Update dependency com.google.apis:google-api-services-bigquery to v2-rev20250706-2.0.0 (#3910) (ae5c971)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 (#3901) (8205623)
- Update dependency io.opentelemetry:opentelemetry-api to v1.52.0 (#3902) (772407b)
- Update dependency io.opentelemetry:opentelemetry-bom to v1.52.0 (#3903) (509a6fc)
- Update dependency io.opentelemetry:opentelemetry-context to v1.52.0 (#3904) (96c1bae)
- Update dependency io.opentelemetry:opentelemetry-exporter-logging to v1.52.0 (#3905) (28ee4c9)

[#3890](https://github.com/googleapis/java-bigquery/issues/3890)
[84207e2](https://github.com/googleapis/java-bigquery/commit/84207e297eec75bcb4f1cc1b64423d7c2ddd6c30)
[#3910](https://github.com/googleapis/java-bigquery/issues/3910)
[ae5c971](https://github.com/googleapis/java-bigquery/commit/ae5c97146c7076e90c000fd98b797ec8e08a9cd8)
[#3901](https://github.com/googleapis/java-bigquery/issues/3901)
[8205623](https://github.com/googleapis/java-bigquery/commit/82056237f194a6c99ec4fb3a4315023efdedff1b)
[#3902](https://github.com/googleapis/java-bigquery/issues/3902)
[772407b](https://github.com/googleapis/java-bigquery/commit/772407b12f4da005f79eafc944d4c53f0eec5c27)
[#3903](https://github.com/googleapis/java-bigquery/commit/509a6fc0bb7e7a101bf0d4334a3ff1adde2cab09)
[#3904](https://github.com/googleapis/java-bigquery/commit/96c1bae0fcdfdfc2dbb25dcae5007c5d02111a8c)
[#3905](https://github.com/googleapis/java-bigquery/commit/28ee4c941b99b1fe3803aefbe7a8ae57100d76cb)

説明：
BigQuery Javaクライアントライブラリ `google-cloud-bigquery` がバージョン2.54.0に更新されました。
主な変更点は以下の通りです。
1.  **OpenTelemetryの統合**: OpenTelemetryのサンプルコードと、OpenTelemetryメトリクスをリクエストヘッダに追加する機能が導入されました。これにより、BigQuery操作の可観測性が向上します。
2.  **依存ライブラリの更新**: `google-cloud-bigquerystorage-bom`, `proto-google-cloud-bigqueryconnection-v1`, `google-api-services-bigquery`, `sdk-platform-java-config` などの内部依存ライブラリ、およびOpenTelemetry関連ライブラリのバージョンが更新されました。これらは主にバグ修正、パフォーマンス改善、セキュリティ強化などが含まれる可能性があります。

影響有無：
**影響なし**
当社のGoogle Cloud Composer2環境 (Composer version 2.7.1, Airflow version 2.7.3) はPythonベースであり、DAGsやカスタムロジックはPythonで実装されています。今回のリリースはJavaクライアントライブラリの更新であるため、直接的な影響はありません。Composer環境内でJavaアプリケーションやJavaベースのOperatorを利用していない限り、この更新による影響は生じません。

対処方法：
不要。

用語説明：
*   **クライアントライブラリ**: プログラミング言語（例: Java, Python）からGoogle Cloudサービス（例: BigQuery）を操作するためのSDK（Software Development Kit）の一部。APIを直接呼び出す代わりに、より扱いやすい形式でサービスと連携できる機能を提供します。
*   **OpenTelemetry (OTel)**: クラウドネイティブなソフトウェアのテレメトリーデータ（メトリクス、ログ、トレース）を収集・エクスポートするためのベンダーニュートラルなオープンスタンダードおよびツールキットです。システムの状態を監視し、問題を診断するために使用されます。
*   **依存ライブラリ**: あるソフトウェアが機能するために必要とする、外部のライブラリやモジュール。今回のケースでは、BigQuery Javaクライアントライブラリが動作するために、他のGoogle Cloud関連のライブラリやOpenTelemetry関連のライブラリに依存しています。