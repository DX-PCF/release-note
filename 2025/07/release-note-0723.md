
# Title: July 21, 2025 
Link: https://cloud.google.com/release-notes#July_21_2025<br>
Google Cloudのリリースノートに基づき、ご利用中のGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) 環境への影響を調査しました。

---

# BigQuery
## Libraries
### Java
### Changed
原文:
- **bigquery:** Add OpenTelemetry support to BigQuery rpcs (#3860) (e2d23c1)
- **bigquery:** Add support for custom timezones and timestamps (#3859) (e5467c9)
- Next release from main branch is 2.53.0 (#3879) (c47a062)
- Load jobs preserve ascii control characters configuration (#3876) (5cfdf85)
- Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.69.0 (#3870) (a7f1007)
- Update dependency com.google.apis:google-api-services-bigquery to v2-rev20250615-2.0.0 (#3872) (f081589)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 (#3878) (0e971b8)
- Update maven format command (#3877) (d2918da)

説明：
BigQueryのJavaクライアントライブラリがバージョン2.53.0に更新されました。主な変更点として、OpenTelemetryのサポート追加、カスタムタイムゾーンとタイムスタンプのサポート、ロードジョブにおけるASCII制御文字の設定保持機能の追加、および内部依存関係の更新が含まれます。

影響有無：なし
Google Cloud ComposerはPythonベースのサービスであり、Airflow DAGの実行環境もPythonで構築されています。Javaクライアントライブラリの更新は、Composer環境やDAGの実行には直接的な影響を与えません。BigQuery操作には通常、Pythonクライアントライブラリが利用されます。

対処方法：不要

用語説明：
*   **OpenTelemetry**: ベンダーニュートラルなオープンソースのオブザーバビリティフレームワークです。トレース、メトリクス、ログの収集・エクスポートを標準化し、分散システムの可視化を助けます。
*   **ASCII制御文字**: ASCII文字セットのうち、印刷可能な文字ではなく、通信プロトコルやテキストのフォーマットを制御するために使われる文字です。例えば、タブ、改行、キャリッジリターンなどがあります。
*   **Maven**: Javaプロジェクトのビルド、依存関係管理、ドキュメント生成などを自動化するためのツールです。

### Python
### Changed
原文:
- Add null_markers property to LoadJobConfig and CSVOptions (#2239) (289446d)
- Add total slot ms to RowIterator (#2233) (d44bf02)
- Add UpdateMode to update_dataset (#2204) (eb9c2af)
- Adds dataset_view parameter to get_dataset method (#2198) (28a5750)
- Adds date_format to load job and external config (#2231) (7d31828)
- Adds datetime_format as an option (#2236) (54d3dc6)
- Adds source_column_match and associated tests (#2227) (6d5d236)
- Adds time_format and timestamp_format and associated tests (#2238) (371ad29)
- Adds time_zone to external config and load job (#2229) (b2300d0)
- Adds magics.context.project to eliminate issues with unit tests … (#2228) (27ff3a8)
- Fix rows returned when both start_index and page_size are provided (#2181) (45643a2)
- Make AccessEntry equality consistent with from_api_repr (#2218) (4941de4)
- Update type hints for various BigQuery files (#2206) (b863291)
- Improve clarity of "Output Only" fields in Dataset class (#2201) (bd5aba8)

説明：
BigQueryのPythonクライアントライブラリがバージョン3.35.0に更新されました。このバージョンでは、ロードジョブ設定（`LoadJobConfig`）やCSVオプションに`null_markers`プロパティが追加されたほか、`RowIterator`に処理スロット時間（`total slot ms`）、`update_dataset`に`UpdateMode`、`get_dataset`に`dataset_view`パラメータが追加されるなど、多くの新機能やオプションが導入されました。また、日付/時刻フォーマット、タイムゾーンの指定オプションがロードジョブや外部構成に追加されています。一部のバグ修正（`start_index`と`page_size`同時指定時の行数返却）や内部的な改善も含まれます。

影響有無：なし（または低）
Google Cloud Composerの環境（Composer 2.7.1, Airflow 2.7.3）では、通常`apache-airflow-providers-google`パッケージを介して`google-cloud-bigquery`ライブラリが利用されます。
これらの更新は、ライブラリのバージョンが3.35.0に明示的にアップグレードされない限り、既存のComposer環境に直接影響しません。
更新内容は主に機能追加であり、既存のAPIの破壊的変更は報告されていません。したがって、仮にライブラリをアップグレードした場合でも、既存のDAGコードが予期せぬ動作変更を引き起こす可能性は低いと考えられます。バグ修正は、特定の条件で発生していた問題が改善される可能性があります。

対処方法：
現在のところ対応は不要です。
もし、これらの新機能を利用したい場合や、修正されたバグによる影響を受けている場合は、Composer環境のPyPIパッケージとして`google-cloud-bigquery`をバージョン3.35.0にアップグレードすることを検討してください。アップグレードの際は、テスト環境で十分な動作確認を実施することを推奨します。

用語説明：
*   **LoadJobConfig**: BigQueryのロードジョブ（データをテーブルにロードする操作）を設定するためのオブジェクトです。CSV形式のデータロード時にnull値をどのように解釈するかを指定する`null_markers`などが追加されました。
*   **RowIterator**: BigQueryのクエリ結果やテーブルデータをイテレート（反復処理）するためのオブジェクトです。クエリ実行に費やされた総スロット時間を`total slot ms`として取得できるようになりました。
*   **UpdateMode**: BigQueryのデータセットを更新する際の動作モードを指定するオプションです。
*   **Type hints**: Python 3.5以降で導入された機能で、変数や関数の引数、戻り値の型をアノテーションとして記述することで、コードの可読性向上や静的解析ツールによる型チェックを可能にします。

---

# Cloud Service Mesh
## Changed
原文:
Managed Cloud Service Mesh will start using proxy version `csm_mesh_proxy.20250623b_RC00` for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.35. This change is rolling out to all release channels.

説明：
マネージドCloud Service Meshが、GKEクラスタ上のGateway APIに対して、プロキシバージョン`csm_mesh_proxy.20250623b_RC00`の使用を開始します。このプロキシバージョンはEnvoyバージョン1.35に最も近いです。この変更は、すべてのリリースチャネルに段階的に適用されます。

影響有無：なし
Google Cloud Composerはマネージドサービスであり、基盤となるGKEクラスタやService Meshのインフラストラクチャの管理はGoogle Cloud側で行われます。ユーザーが直接Cloud Service Meshを構成したり、GKEのGateway APIを利用してComposer環境のネットワークを設定したりすることは一般的ではありません。
この変更は、Service Meshの内部的なコンポーネントの更新であり、通常、ComposerのDAG実行やAirflowの動作に直接的な影響を与えるものではありません。

対処方法：不要

用語説明：
*   **Cloud Service Mesh**: Google Cloudが提供するマネージドなサービスメッシュプラットフォームです。サービス間の通信の可視化、制御、セキュリティを強化します。Istioをベースにしています。
*   **Gateway API**: Kubernetesにおける外部からのクラスタへのアクセスを管理するための新しい標準APIです。従来のIngress APIよりも柔軟で拡張性が高い設計になっています。
*   **Envoy**: クラウドネイティブアプリケーション向けに設計された高性能なオープンソースのプロキシサーバです。サービスメッシュのデータプレーンとして広く利用されています。