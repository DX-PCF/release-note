
# Title: September 17, 2025 
Link: https://cloud.google.com/release-notes#September_17_2025<br>
# Cloud Load Balancing
## Changed
原文: A security fix was made which changes the behavior of requests and responses sent with the `Transfer-Encoding: Chunked` header to be more RFC 9112 compliant. The RFC states that both the `chunked_body` and the `last-chunk` fields must end in `CRLF`. This is now enforced.

[RFC states](https://datatracker.ietf.org/doc/html/rfc9112#name-chunked-transfer-coding)

説明：
Cloud Load Balancingにおいて、`Transfer-Encoding: Chunked` ヘッダーを使用するHTTPリクエストおよびレスポンスの処理方法にセキュリティ修正が適用されました。この修正により、RFC 9112（HTTP/1.1 Semantics and Content）で規定されているチャンクエンコーディングの厳格な要件、特に `chunked_body` と `last-chunk` の両フィールドが `CRLF` (Carriage Return Line Feed) で終端されなければならないというルールが、ロードバランサによって強制されるようになりました。

影響有無：
**影響がある可能性があります。**
理由：ほとんどの標準的なHTTPクライアントやサーバーはRFC 9112に準拠しており、通常は `CRLF` でチャンクを終端します。しかし、RFCに厳密に従わない非標準的なHTTP実装、またはバグのあるカスタムアプリケーションが `Transfer-Encoding: Chunked` を使用しており、チャンクの終端が `CRLF` でない場合、Cloud Load Balancingがこれを不正な形式とみなし、通信が失敗する可能性があります。

対処方法：
1.  **アプリケーションの確認:** お客様のアプリケーション（特にバックエンドサービスやクライアント）が `Transfer-Encoding: Chunked` を使用しているかどうかを確認してください。
2.  **RFC準拠の確認:** `Transfer-Encoding: Chunked` を使用している場合、それらの実装がRFC 9112の規定に従い、`chunked_body` と `last-chunk` の両方が `CRLF` で正しく終端されていることを確認してください。
3.  **監視:** リリース後に、ロードバランサを介した通信でHTTPエラー（特に5xx系エラー）が増加していないか、Cloud Monitoring や Cloud Logging で監視してください。
4.  **必要に応じた修正:** もし影響が確認された場合、RFC 9112に準拠していないアプリケーション側のチャンクエンコーディング処理を修正する必要があります。

用語説明：
*   **Transfer-Encoding: Chunked:** HTTP/1.1で、メッセージボディを複数のチャンク（断片）に分割して送信するエンコーディング方式。メッセージボディの長さを事前に決定できない場合などに利用されます。
*   **RFC 9112:** IETF (Internet Engineering Task Force) によって発行された「HTTP/1.1 Semantics and Content」を定義する標準ドキュメントです。HTTP/1.1のメッセージフォーマットやセマンティクスに関する詳細な規定が含まれています。
*   **chunked_body:** `Transfer-Encoding: Chunked` で送信される、実際のデータチャンクの集合です。各チャンクはサイズとデータ本体から構成されます。
*   **last-chunk:** `Transfer-Encoding: Chunked` において、全てのデータチャンクの送信が完了したことを示すために送られる、サイズがゼロの特別なチャンクです。
*   **CRLF (Carriage Return Line Feed):** `\r\n` のシーケンスで表される、多くのインターネットプロトコルで改行コードとして使用される文字の組み合わせです。チャンクエンコーディングでは、各チャンクのサイズ行やデータ本体、そして `last-chunk` の終端にこのCRLFが必須とされています。
# Title: September 15, 2025 
Link: https://cloud.google.com/release-notes#September_15_2025<br>
# BigQuery
## Changed
原文:
- **bigquery:** Add custom ExceptionHandler to BigQueryOptions (#3937) (de0914d)
- Update dependency com.google.cloud:google-cloud-bigquerystorage-bom to v3.17.0 (#3954) (e73deed)
- Update dependency com.google.google.cloud:sdk-platform-java-config to v3.52.1 (#3952) (79b7557)
説明：BigQuery Javaクライアントライブラリ (google-cloud-bigquery 2.55.0) の変更です。
`BigQueryOptions` にカスタムの `ExceptionHandler` を追加する機能が導入されました。これにより、BigQuery API呼び出しにおける例外処理の柔軟性が向上します。
また、`google-cloud-bigquerystorage-bom` が `v3.17.0` に、`sdk-platform-java-config` が `v3.52.1` に、それぞれ内部的な依存ライブラリのバージョンが更新されました。
影響有無：なし。
Google Cloud Composer 2.7.1 (Airflow 2.7.3) 環境ではPythonベースのAirflow DAGが主に利用されるため、Javaクライアントライブラリの変更が直接影響することはありません。これらの変更は、JavaアプリケーションでBigQueryクライアントライブラリを使用している場合に適用されます。
対処方法：不要。
用語説明：
*   **ExceptionHandler**: プログラム実行中に発生する例外（エラー）を捕捉し、処理するためのメカニズムです。カスタム `ExceptionHandler` を実装することで、開発者は特定の例外タイプに対して独自の処理ロジックを定義できます。
*   **BigQueryOptions**: BigQueryクライアントライブラリの動作を設定するためのオプションを保持するオブジェクトです。
*   **BOM (Bill of Materials)**: Mavenなどのビルドツールで使用される依存関係管理の仕組みで、複数の関連ライブラリのバージョンを一括で管理するために使用されます。

## Changed
原文:
- Updates to fastpath query execution (#2268) (ef2740a)
- Remove deepcopy while setting properties for _QueryResults (#2280) (33ea296)
- Clarify that the presence of `XyzJob.errors` doesn't necessarily mean that the job has not completed or was unsuccessful (#2278) (6e88d7d)
- Clarify the api_method arg for client.query() (#2277) (8a13c12)
説明：BigQuery Pythonクライアントライブラリ (google-cloud-bigquery 3.37.0) の変更です。
クエリ実行の「fastpath」処理が更新され、パフォーマンスの向上が期待されます。
`_QueryResults` オブジェクトのプロパティを設定する際に、`deepcopy` を行わないように変更されました。これにより、オブジェクトのコピーにかかるオーバーヘッドが削減されます。
また、`XyzJob.errors` フィールドの存在が必ずしもジョブの失敗を意味しないこと、および `client.query()` メソッドの `api_method` 引数に関するドキュメントの明確化が行われました。
影響有無：限定的な影響の可能性あり。
Google Cloud Composer 2.7.1 (Airflow 2.7.3) はPythonベースであるため、このライブラリが使用されている可能性があります。
「fastpath query execution」の更新により、既存のBigQueryクエリを使用するAirflow DAGのパフォーマンスが向上する可能性があります。
「Remove deepcopy」の変更はパフォーマンス改善を目的としていますが、`_QueryResults` オブジェクトのプロパティを直接操作するような稀なケースでは、参照渡しによる意図しない副作用が発生する可能性も考慮する必要があります。ただし、一般的なデータ取得・処理においては問題ないと考えられます。
ドキュメントの明確化は動作には影響しません。
対処方法：BigQueryを多用するAirflow DAGがある場合、テスト環境で新しいライブラリバージョンでの動作確認（特にパフォーマンスやデータ処理の正確性）を推奨します。Composer環境のAirflowは、`requirements.txt`でライブラリバージョンを固定していない限り、更新される可能性があります。
用語説明：
*   **Fastpath query execution**: 特定の条件を満たすクエリに対して、より最適化された高速な実行経路を指すことがあります。
*   **deepcopy**: Pythonにおいて、オブジェクトとその中のすべての要素を再帰的にコピーすること。元のオブジェクトと完全に独立した新しいオブジェクトを作成します。これにより、元のオブジェクトへの変更がコピーに影響しないようにできますが、オーバーヘッドが発生します。
*   **_QueryResults**: BigQueryのクエリ実行結果を表す内部オブジェクトです。

# Cloud Logging
## Changed
原文:
- **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 (1438bff)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 (#1853) (c21a635)
- Update googleapis/sdk-platform-java action to v2.62.1 (#1855) (b6ce498)
説明：Cloud Logging Javaクライアントライブラリ (google-cloud-logging 3.23.4) の変更です。
Javaコード生成ツール (`gapic-generator-java`) が `2.62.1` に、内部的な依存ライブラリ (`sdk-platform-java-config`) が `v3.52.1` に、それぞれバージョンが更新されました。また、GitHub Actionsの関連アクションも更新されています。
影響有無：なし。
Google Cloud Composer 2.7.1 (Airflow 2.7.3) 環境ではPythonベースのAirflow DAGが主に利用されるため、Javaクライアントライブラリの変更が直接影響することはありません。これらの変更は、JavaアプリケーションでCloud Loggingクライアントライブラリを使用している場合に適用されます。
対処方法：不要。
用語説明：
*   **GAPIC (Google API Client Libraries)**: GoogleのAPIにアクセスするためのクライアントライブラリを自動生成するフレームワークです。
*   **gapic-generator-java**: Java用のGAPICクライアントライブラリを生成するツールです。

# Pub/Sub
## Changed
原文:
- **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 (ac08d5f)
- Update actions/checkout action to v5 (#2531) (f687f11)
- Update actions/setup-java action to v5 (#2535) (2ed87d2)
- Update dependency com.google.cloud:google-cloud-bigquery to v2.54.2 (#2538) (10a8283)
- Update dependency com.google.cloud:google-cloud-storage to v2.56.0 (#2536) (80d9ca1)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 (#2544) (9fe7550)
- Update googleapis/sdk-platform-java action to v2.62.1 (#2545) (17f28ef)
説明：Pub/Sub Javaクライアントライブラリ (google-cloud-pubsub 1.141.4) の変更です。
Javaコード生成ツール (`gapic-generator-java`) および内部的な依存ライブラリ (`google-cloud-bigquery`, `google-cloud-storage`, `sdk-platform-java-config`) のバージョンが更新されました。また、GitHub Actionsの関連アクションも更新されています。
影響有無：なし。
Google Cloud Composer 2.7.1 (Airflow 2.7.3) 環境ではPythonベースのAirflow DAGが主に利用されるため、Javaクライアントライブラリの変更が直接影響することはありません。これらの変更は、JavaアプリケーションでPub/Subクライアントライブラリを使用している場合に適用されます。
対処方法：不要。
用語説明：
*   **GAPIC (Google API Client Libraries)**: GoogleのAPIにアクセスするためのクライアントライブラリを自動生成するフレームワークです。
*   **gapic-generator-java**: Java用のGAPICクライアントライブラリを生成するツールです。