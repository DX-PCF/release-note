
# Title: August 25, 2025 
Link: https://cloud.google.com/release-notes#August_25_2025<br>
---

# BigQuery

## Changes (Python Client Library: google-cloud-bigquery 3.36.0)

原文:
- Add created/started/ended properties to RowIterator. (#2260) (0a95b24)
- Retry query jobs if `jobBackendError` or `jobInternalError` are encountered (#2256) (3deff1d)
- Add a TROUBLESHOOTING.md file with tips for logging (#2262) (b684832)
- Update README to break infinite redirect loop (#2254) (8f03166)

説明：
`google-cloud-bigquery` Python クライアントライブラリのバージョン 3.36.0 における変更点です。
1.  **RowIteratorへのプロパティ追加**: `RowIterator` オブジェクトに、クエリジョブの作成時刻 (`created`)、開始時刻 (`started`)、終了時刻 (`ended`) を示す新しいプロパティが追加されました。これにより、クエリ結果を反復処理する際に、そのクエリジョブのライフサイクル情報をプログラムから直接取得できるようになります。
2.  **クエリジョブの自動再試行機能**: `jobBackendError` (バックエンドサービスエラー) または `jobInternalError` (内部エラー) が発生した場合に、クエリジョブが自動的に再試行されるようになりました。これにより、一時的なサービス側の問題によるクエリの失敗が減少し、アプリケーションの堅牢性が向上します。
3.  **ドキュメントの追加と更新**: トラブルシューティングガイド `TROUBLESHOOTING.md` が追加され、README ファイルが更新されました。

影響有無：
**影響：限定的、またはポジティブな影響の可能性あり**

*   **RowIteratorプロパティ追加**: 既存のコードがこれらの新しいプロパティを参照していない限り、直接的な影響はありません。今後これらの情報を利用したい場合に活用できます。
*   **クエリジョブの自動再試行**: この変更は、`jobBackendError`や`jobInternalError`といった一時的なBigQueryサービス側の問題が発生した場合に、アプリケーション側での特別なエラーハンドリングなしにクエリが成功する確率を高めます。これはシステムの堅牢性を向上させるポジティブな変更であり、既存のワークロードに対して安定性向上の恩恵をもたらす可能性があります。
*   **Google Cloud Composer への関連**: Composer 2.7.1 環境で実行されるAirflow DAGsが `google-cloud-bigquery` Pythonクライアントライブラリを使用している場合に関連します。Composer環境のPythonライブラリバージョンは、利用しているComposerイメージバージョンに依存します。この変更はライブラリのバージョンアップによって提供されるため、現在のComposer環境でこのバージョン（3.36.0）が使用されているか、または使用されるように更新された場合に適用されます。

対処方法：
*   **ライブラリのバージョン確認と更新の検討**: もしAirflow DAGsでBigQuery Pythonクライアントライブラリを利用しており、`jobBackendError`や`jobInternalError`によるクエリ失敗に悩まされている場合、または新しい`RowIterator`プロパティを利用したい場合は、Airflowの`requirements.txt`ファイルを通じて`google-cloud-bigquery`ライブラリのバージョンを`>=3.36.0`に更新することを検討してください。
*   **テストの実施**: ライブラリのバージョンアップを行う際は、必ず本番環境にデプロイする前に開発環境またはステージング環境で十分なテストを実施し、既存のDAGsやアプリケーションに予期せぬ非互換性がないことを確認してください。

用語説明：
*   **`RowIterator`**: BigQuery Pythonクライアントライブラリにおいて、クエリ結果の行を反復処理するためのオブジェクトです。大量のデータをメモリに一度にロードすることなく、効率的に処理するために使用されます。
*   **`jobBackendError` / `jobInternalError`**: BigQueryジョブ実行中に発生する可能性のあるエラーコードの一種です。これらは通常、BigQueryサービスの内部的な問題や一時的な障害を示し、ユーザー側のコードのバグではないことが多いです。
*   **Google Cloud Composer**: Apache Airflowをフルマネージドサービスとして提供するGoogle Cloudのサービスです。Pythonで記述されたDAG (Directed Acyclic Graph) を利用してワークフローを定義し、実行します。

---

# Cloud Logging

## Changes (Java Client Library: google-cloud-logging 3.23.3)

原文:
- Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 (#1848) (162ef56)

説明：
`google-cloud-logging` Java クライアントライブラリのバージョン 3.23.3 における変更点です。
1.  **依存ライブラリの更新**: 内部的な依存ライブラリである `com.google.cloud:sdk-platform-java-config` がバージョン 3.52.0 に更新されました。

影響有無：
**影響：なし**

*   Google Cloud Composer は Python ベースのサービスであり、Javaアプリケーションを直接ホストするものではありません。
*   この変更はJavaクライアントライブラリに関するものであり、もしお客様の環境でGoogle Cloud Logging Java Client Libraryを直接利用するJavaアプリケーション（例: Compute Engine上のJavaアプリケーション、Cloud Run/FunctionsのJavaサービスなど）が構築されていない限り、直接的な影響はありません。

対処方法：
*   特段の対処は不要です。もしJavaアプリケーションで当該ライブラリを利用している場合は、通常通り依存ライブラリのバージョンアップを検討し、互換性を確認してください。

用語説明：
*   **Java クライアントライブラリ**: Java言語でGoogle Cloudのサービスと連携するためのSDK (Software Development Kit) コンポーネントです。開発者が自身のJavaアプリケーションからGoogle CloudのAPIを簡単に利用できるようにします。

---

# Pub/Sub

## Changes (Java Client Library: google-cloud-pubsub 1.141.3)

原文:
- Use the system executor instead of a separate thread pool for EOD ack/modack callbacks (#2526) (ffeb017)
- Update actions/checkout action to v5 (#2520) (409398a)
- Update dependency com.google.cloud:google-cloud-bigquery to v2.54.1 (#2523) (0678a74)
- Update dependency com.google.cloud:google-cloud-core to v2.60.0 (#2527) (0166e21)
- Update dependency com.google.cloud:google-cloud-storage to v2.55.0 (#2517) (b67acf1)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 (#2528) (e424d11)
- Update dependency com.google.protobuf:protobuf-java-util to v4.32.0 (#2524) (44ff087)
- Update dependency org.assertj:assertj-core to v3.27.4 (#2518) (67695bc)

説明：
`google-cloud-pubsub` Java クライアントライブラリのバージョン 1.141.3 における変更点です。
1.  **EOD Ack/ModackコールバックのExecutor変更**: Exactly-Once Delivery (EOD) 機能における確認応答 (ack) や変更確認応答 (modack) のコールバック処理に、専用のスレッドプールではなくシステムエクゼキュータが使用されるようになりました。これにより、リソース管理がより効率的になり、Pub/Subサブスクライバーアプリケーションの安定性やパフォーマンスが向上する可能性があります。
2.  **複数の依存ライブラリの更新**: `google-cloud-bigquery`, `google-cloud-core`, `google-cloud-storage`, `sdk-platform-java-config`, `protobuf-java-util`, `assertj-core` など、多数の内部依存ライブラリが最新バージョンに更新されました。これらは通常、セキュリティ修正、バグ修正、パフォーマンス改善を含んでいます。

影響有無：
**影響：なし**

*   Google Cloud Composer は Python ベースのサービスであり、Javaアプリケーションを直接ホストするものではありません。
*   この変更はJavaクライアントライブラリに関するものであり、もしお客様の環境でGoogle Cloud Pub/Sub Java Client Libraryを直接利用するJavaアプリケーション（例: Compute Engine上のJavaアプリケーション、Cloud Run/FunctionsのJavaサービスなど）が構築されていない限り、直接的な影響はありません。

対処方法：
*   特段の対処は不要です。もしJavaアプリケーションで当該ライブラリを利用している場合は、通常通り依存ライブラリのバージョンアップを検討し、互換性を確認してください。特にEOD Ack/Modackコールバックの改善は、サブスクライバーアプリケーションの安定性向上が期待されます。

用語説明：
*   **Exactly-Once Delivery (EOD)**: Pub/Sub のメッセージ配信保証の一つで、特定のメッセージがサブスクライバーアプリケーションに重複なく、かつ欠落なく一度だけ配信されることを保証する機能です。
*   **Ack (Acknowledgment)**: Pub/Subにおいて、サブスクライバーがメッセージの受信と処理が完了したことをサービスに通知する操作です。
*   **Modack (Modify Acknowledgment Deadline)**: Pub/Subにおいて、メッセージの確認応答期限を変更する操作です。これにより、メッセージの処理に時間がかかる場合に、メッセージが再配信されるのを防ぐことができます。
*   **Executor**: Javaにおけるスレッドプールの概念で、タスクを実行するためのスレッド管理メカニズムを提供します。システムエクゼキュータは、アプリケーション全体で共有されるリソース効率の良いスレッドプールを指す場合があります。
