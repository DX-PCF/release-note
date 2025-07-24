
# Title: July 21, 2025 
Link: https://cloud.google.com/release-notes#July_21_2025<br>
承知いたしました。Google Cloudのリリースノートを基に、製品ごとの影響有無を調査し、簡潔に回答します。

---

# BigQuery
## Changed (Java Client Library)
原文:
```
## Java

## Changes for google-cloud-bigquery

[google-cloud-bigquery](https://github.com/googleapis/java-bigquery)
[2.53.0](https://github.com/googleapis/java-bigquery/compare/v2.52.0...v2.53.0)
- **bigquery:** Add OpenTelemetry support to BigQuery rpcs (#3860) (e2d23c1)
- **bigquery:** Add support for custom timezones and timestamps (#3859) (e5467c9)
- Next release from main branch is 2.53.0 (#3879) (c47a062)

[#3860](https://github.com/googleapis/java-bigquery/issues/3860)
[e2d23c1](https://github.com/googleapis/java-bigquery/commit/e2d23c1b15f2c48a4113f82b920f5c29c4b5dfea)
[#3859](https://github.com/googleapis/java-bigquery/issues/3859)
[e5467c9](https://github.com/googleapis/java-bigquery/commit/e5467c917c63ac066edcbcd902cc2093a39971a3)
[#3879](https://github.com/googleapis/java-bigquery/issues/3879)
[c47a062](https://github.com/googleapis/java-bigquery/commit/c47a062136fea4de91190cafb1f11bac6abbbe3a)
- Load jobs preserve ascii control characters configuration (#3876) (5cfdf85)

[#3876](https://github.com/googleapis/java-bigquery/issues/3876)
[5cfdf85](https://github.com/googleapis/java-bigquery/commit/5cfdf855fa0cf206660fd89743cbaabf3afa75a3)
- Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.69.0 (#3870) (a7f1007)
- Update dependency com.google.apis:google-api-services-bigquery to v2-rev20250615-2.0.0 (#3872) (f081589)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 (#3878) (0e971b8)

[#3870](https://github.com/googleapis/java-bigquery/issues/3870)
[a7f1007](https://github.com/googleapis/java-bigquery/commit/a7f1007b5242da2c0adebbb309a908d7d4db5974)
[#3872](https://github.com/googleapis/java-bigquery/issues/3872)
[f081589](https://github.com/googleapis/java-bigquery/commit/f08158955b7fec3c2ced6332b6e4d76cc13f2e90)
[#3878](https://github.com/googleapis/java-bigquery/commit/0e971b8ace013caa31b8a02a21038e94bebae2a5)
- Update maven format command (#3877) (d2918da)

[#3877](https://github.com/googleapis/java-bigquery/issues/3877)
[d2918da](https://github.com/googleapis/java-bigquery/commit/d2918da844cd20ca1602c6fcf9fa1df685f261fc)
```
説明:
BigQueryのJavaクライアントライブラリ `google-cloud-bigquery` がバージョン 2.53.0 にアップデートされました。主な変更点は以下の通りです。
*   BigQuery RPCsに対するOpenTelemetryのサポートが追加され、トレースとメトリクス収集が可能になります。
*   カスタムタイムゾーンとタイムスタンプのサポートが追加され、より柔軟な時間データ処理が可能になります。
*   ロードジョブにおけるASCII制御文字の保持設定が追加されました。
*   内部依存ライブラリが複数バージョンアップされました。

影響有無:
影響なし。
Google Cloud Composer2 (Airflow) は主にPythonで動作し、BigQueryとの連携にはPythonクライアントライブラリを使用します。このJavaクライアントライブラリの更新は直接的な影響はありません。もしJavaベースのカスタムアプリケーションでBigQueryを利用している場合でも、これらの変更は機能追加であり、既存の動作に影響を与える非互換な変更ではありません。

対処方法:
対応不要です。新機能を利用したい場合は、ご自身のアプリケーションでJavaクライアントライブラリのバージョンを2.53.0以降に更新し、コードを修正する必要があります。

用語説明:
*   **OpenTelemetry**: 分散トレーシング、メトリクス収集、ログ収集のためのオープンソースのオブザーバビリティフレームワークです。これにより、アプリケーションのパフォーマンス監視や問題診断が容易になります。
*   **RPC (Remote Procedure Call)**: ネットワーク上の異なるプロセス（通常は異なるマシン上）で実行されている関数やサブルーチンを、ローカル関数を呼び出すのと同じように呼び出すためのプロトコルです。

---

# BigQuery
## Changed (Python Client Library)
原文:
```
## Python

## Changes for google-cloud-bigquery

[google-cloud-bigquery](https://github.com/googleapis/python-bigquery)
[3.35.0](https://github.com/googleapis/python-bigquery/compare/v3.34.0...v3.35.0)
- Add null_markers property to LoadJobConfig and CSVOptions (#2239) (289446d)
- Add total slot ms to RowIterator (#2233) (d44bf02)
- Add UpdateMode to update_dataset (#2204) (eb9c2af)
- Adds dataset_view parameter to get_dataset method (#2198) (28a5750)
- Adds date_format to load job and external config (#2231) (7d31828)
- Adds datetime_format as an option (#2236) (54d3dc6)
- Adds source_column_match and associated tests (#2227) (6d5d236)
- Adds time_format and timestamp_format and associated tests (#2238) (371ad29)
- Adds time_zone to external config and load job (#2229) (b2300d0)

[#2239](https://github.com/googleapis/python-bigquery/issues/2239)
[289446d](https://github.com/googleapis/python-bigquery/commit/289446dd8c356d11a0b63b8e6275629b1ae5dc08)
[#2233](https://github.com/googleapis/python-bigquery/issues/2233)
[d44bf02](https://github.com/googleapis/python-bigquery/commit/d44bf0231e6e96369e4e03667a3f96618fb664e2)
[#2204](https://github.com/googleapis/python-bigquery/issues/2204)
[eb9c2af](https://github.com/googleapis/python-bigquery/commit/eb9c2aff242c5107f968bbd8b6a9d30cecc877f6)
[#2198](https://github.com/googleapis/python-bigquery/issues/2198)
[28a5750](https://github.com/googleapis/python-bigquery/commit/28a5750d455f0381548df6f9b1f7661823837d81)
[#2231](https://github.com/googleapis/python-bigquery/issues/2231)
[7d31828](https://github.com/googleapis/python-bigquery/commit/7d3182802deccfceb0646b87fc8d12275d0a569b)
[#2236](https://github.com/googleapis/python-bigquery/issues/2236)
[54d3dc6](https://github.com/googleapis/python-bigquery/commit/54d3dc66244d50a031e3c80d43d372d2743ecbc3)
[#2227](https://github.com/googleapis/python-bigquery/issues/2227)
[6d5d236](https://github.com/googleapis/python-bigquery/commit/6d5d23685cd457d85955356705c1101e9ec3cdcd)
[#2238](https://github.com/googleapis/python-bigquery/issues/2238)
[371ad29](https://github.com/googleapis/python-bigquery/commit/371ad292df537278767dba71d81822ed57dd8e7d)
[#2229](https://github.com/googleapis/python-bigquery/commit/b2300d032843512b7e4a5703377632fe60ef3f8d)
- Adds magics.context.project to eliminate issues with unit tests … (#2228) (27ff3a8)
- Fix rows returned when both start_index and page_size are provided (#2181) (45643a2)
- Make AccessEntry equality consistent with from_api_repr (#2218) (4941de4)
- Update type hints for various BigQuery files (#2206) (b863291)

[#2228](https://github.com/googleapis/python-bigquery/issues/2228)
[27ff3a8](https://github.com/googleapis/python-bigquery/commit/27ff3a89a5f97305fa3ff673aa9183baa7df200f)
[#2181](https://github.com/googleapis/python-bigquery/issues/2181)
[45643a2](https://github.com/googleapis/python-bigquery/commit/45643a2e20ce5d503118522dd195aeca00dec3bc)
[#2218](https://github.com/googleapis/python-bigquery/issues/2218)
[4941de4](https://github.com/googleapis/python-bigquery/commit/4941de441cb32cabeb55ec0320f305fb62551155)
[#2206](https://github.com/googleapis/python-bigquery/issues/2206)
[b863291](https://github.com/googleapis/python-bigquery/commit/b86329188ba35e61871db82ae1d95d2a576eed1b)
- Improve clarity of "Output Only" fields in Dataset class (#2201) (bd5aba8)

[#2201](https://github.com/googleapis/python-bigquery/issues/2201)
[bd5aba8](https://github.com/googleapis/python-bigquery/commit/bd5aba8ba40c2f35fb672a68eed11d6baedb304f)
```
説明:
BigQueryのPythonクライアントライブラリ `google-cloud-bigquery` がバージョン 3.35.0 にアップデートされました。主な変更点は以下の通りです。
*   `LoadJobConfig`および`CSVOptions`に`null_markers`プロパティが追加され、ロードジョブでNULL値のマーカーを指定できるようになりました。
*   `RowIterator`に`total_slot_ms`が追加され、クエリ実行に消費されたスロット時間の総計を取得できるようになりました。
*   `update_dataset`メソッドに`UpdateMode`が追加され、データセットの更新挙動をより詳細に制御できるようになりました。
*   `get_dataset`メソッドに`dataset_view`パラメータが追加され、取得するデータセット情報の詳細度を指定できるようになりました。
*   ロードジョブおよび外部構成に、日付・時刻形式を指定する`date_format`, `datetime_format`, `time_format`, `timestamp_format`, `time_zone`などのプロパティが追加され、データロード時の日付・時刻のパースがより柔軟になりました。
*   `start_index`と`page_size`が同時に指定された場合の行数取得に関するバグが修正されました。
*   `AccessEntry`の等価性評価が改善され、型ヒントの更新や`Dataset`クラスのフィールド説明の改善が行われました。

影響有無:
影響なし。
これらの変更は主に新機能の追加や既存機能の改善であり、既存のAPIの動作を破壊するような変更（Breaking Change）は含まれていません。そのため、既存のAirflow DAGsがこのライブラリを使用している場合でも、明示的にこれらの新機能を利用しない限り、動作に変化はありません。ただし、`start_index`と`page_size`の組み合わせに関するバグ修正が含まれているため、この条件に合致する処理がある場合は、意図した正しい結果が返るようになる可能性があります。

対処方法:
対応不要です。新機能を利用したい場合や、バグ修正による影響を確実に適用したい場合は、Google Cloud Composer環境のPyPIパッケージとして`google-cloud-bigquery`をバージョン3.35.0以降にアップグレードし、必要に応じてDAGsのコードを修正してください。

用語説明:
*   **LoadJobConfig**: BigQueryでデータロードジョブを作成する際に、そのジョブの動作を定義するための設定オブジェクトです。
*   **CSVOptions**: CSV形式のデータをBigQueryにロードする際、CSVファイルのパース方法（区切り文字、引用符、NULLマーカーなど）を指定するためのオプションです。
*   **RowIterator**: BigQueryのクエリ結果やテーブルから行データを取得する際に、結果セットを一つずつ反復処理するためのイテレータオブジェクトです。
*   **Dataset**: BigQueryにおいて、テーブル、ビュー、その他のデータエンティティを論理的にグループ化するための最上位コンテナです。
*   **AccessEntry**: BigQueryのデータセットやテーブルに対するアクセス権限（誰が、どのようなロールでアクセスできるか）を定義するエントリです。

---

# Cloud Service Mesh
## Changed
原文:
```
 Managed Cloud Service Mesh will start using proxy version `csm_mesh_proxy.20250623b_RC00` for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.35. This change is rolling out to all release channels.
```
説明:
マネージドCloud Service Meshは、GKEクラスタ上のGateway APIに対して、新しいプロキシバージョン `csm_mesh_proxy.20250623b_RC00` の使用を開始します。この新しいプロキシバージョンは、Envoyバージョン1.35に最も近いものとなります。この変更は、すべてのリリースチャネルに順次展開されます。

影響有無:
影響なし。
このリリースノートはCloud Service Meshに関するものであり、現在の環境（Google Cloud Composer2）ではCloud Service Meshの利用が明示されていないため、直接的な影響はありません。
仮にCloud Service Meshを利用しているGKEクラスタがあったとしても、これはマネージドサービスによるプロキシの自動更新であり、通常は下位互換性が保たれるため、アプリケーションへの直接的な影響は少ないと想定されます。

対処方法:
対応不要です。これはマネージドサービスによる自動的なアップデートであり、ユーザー側での操作は必要ありません。
もしCloud Service Meshを利用しており、Envoyプロキシの特定の挙動に依存するワークロードがある場合は、Envoy 1.35のリリースノートを確認し、互換性に関する潜在的な影響がないか確認することをお勧めします。

用語説明:
*   **Cloud Service Mesh**: Google Cloudが提供するマネージドサービスメッシュソリューションです。Istioベースで、サービス間のトラフィック管理、セキュリティ、オブザーバビリティなどを提供します。
*   **Gateway API**: KubernetesのIngress APIの進化版であり、より表現力豊かで拡張性の高いAPIとして設計されています。クラスタ内外のトラフィックルーティングを管理します。
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドKubernetesサービスです。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **Envoy**: クラウドネイティブアプリケーションのために設計された高性能なオープンソースのエッジ/サービスプロキシです。Istioなどのサービスメッシュのデータプレーンとして広く利用されています。