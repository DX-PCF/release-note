
# Title: September 17, 2025 
Link: https://cloud.google.com/release-notes#September_17_2025<br>
以下にGoogle Cloudのリリースノートに対する調査結果を報告します。

---

# Cloud Load Balancing
## Security
原文: A security fix was made which changes the behavior of requests and responses sent with the `Transfer-Encoding: Chunked` header to be more RFC 9112 compliant. The RFC states that both the `chunked_body` and the `last-chunk` fields must end in `CRLF`. This is now enforced.

説明: このセキュリティ修正により、`Transfer-Encoding: Chunked` ヘッダーを含むHTTPリクエストおよびレスポンスの処理方法が変更され、RFC 9112の規定に厳密に準拠するようになります。具体的には、チャンクボディと最終チャンクが `CRLF` (Carriage Return and Line Feed) で終端されていることがCloud Load Balancingによって強制されるようになります。

影響有無: 影響は限定的であると考えられます。
Google Cloud Composer 2.7.1 (Airflow 2.7.3) はCloud Load BalancingをWeb UIや様々な内部サービスで利用していますが、通常、これらのコンポーネントや標準的なHTTPクライアント/サーバーはRFCに準拠した形でチャンクエンコーディングを処理します。もしカスタムのHTTPクライアントや特定のサードパーティ製サービスが、RFC 9112に準拠しない不正なチャンクエンコーディングを使用している場合、接続の問題やHTTPエラー (例: 502 Bad Gateway) が発生する可能性があります。

対処方法:
基本的には特別な対処は不要ですが、Cloud Load Balancingを介してトラフィックを処理しているアプリケーションやサービスにおいて、以下の状況に該当する場合は確認および対応を検討してください。
1.  **異常監視**: ロードバランサーのログやバックエンドサービスのメトリクスを監視し、`Transfer-Encoding: Chunked`に関連する可能性のあるHTTPエラー（特に5xx系エラー）が増加していないか確認します。
2.  **アプリケーションの確認**: チャンクエンコーディングを使用するカスタムアプリケーションや統合ポイントで、HTTPリクエスト/レスポンスがRFC 9112に準拠しているかを確認し、必要に応じて修正します。特に古いシステムや非標準的な実装を使用している場合は注意が必要です。

用語説明:
*   **`Transfer-Encoding: Chunked`**: HTTP/1.1プロトコルで使用されるメカニズムで、メッセージボディのサイズを事前に知らなくてもデータを送信できるようにします。データは複数の「チャンク」（塊）に分割され、各チャンクの前にそのサイズが示されます。
*   **RFC 9112**: HTTP/1.1のメッセージフォーマットとセマンティクスを定義するIETFの標準ドキュメントです。以前のRFC 7230などを置き換えました。
*   **`CRLF`**: "Carriage Return" (ASCII 13) と "Line Feed" (ASCII 10) の組み合わせで、HTTPプロトコルを含む多くのネットワークプロトコルやテキストファイルで改行を示すのに使用されるバイトシーケンスです。

---

# Cloud Service Mesh
## Announcement
原文: The following rollouts have completed for managed Cloud Service Mesh:
- 1.21.5-asm.55 has rolled out to the rapid release channel.
- 1.20.8-asm.48 has rolled out to the regular release channel.
- 1.19.10-asm.48 has rolled out to the stable release channel.
While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

説明: マネージドCloud Service Mesh (ASM) の各リリースチャネル（rapid, regular, stable）において、新しいバージョンのロールアウトが完了したことがアナウンスされました。マネージドデータプレーンはワークロードの再起動によってEnvoyプロキシを自動的に更新しますが、**StatefulSetおよびJobとしてデプロイされているワークロードについては、手動での再起動が必要**です。

影響有無: 通常のGoogle Cloud Composer 2.7.1 (Airflow 2.7.3) 環境では、Cloud Service Mesh (ASM) はデフォルトでは使用されていません。したがって、**本環境への直接的な影響は無い**と判断されます。
ただし、もしお客様のComposer環境が、Service Meshが有効化されたGKEクラスタ上で稼働しており、AirflowのワークロードがService Meshのサイドカーインジェクションを受けている場合は影響の対象となります。

対処方法:
Composer環境がCloud Service Meshを利用している場合に限りますが、以下の対処が必要です。
1.  **StatefulSetとJobの手動再起動**: Cloud Service Meshの管理下にあるGKEクラスタでStatefulSetやJobとしてデプロイされているワークロード（Composerの特定のコンポーネントやカスタムワークロードなど）が存在する場合、Envoyプロキシの更新を完全に適用するために、それらのワークロードを手動で再起動してください。
    *   例えば、Kubernetes CLI (`kubectl`) を使用して、対象のStatefulSetやJobのPodを再起動します。`kubectl rollout restart statefulset <statefulset-name>` または `kubectl delete pod -l app=<app-label>` などのコマンドが利用できます。

用語説明:
*   **Cloud Service Mesh (ASM)**: Google Cloudが提供するフルマネージドなサービスメッシュソリューションで、Istioをベースとしています。トラフィック管理、ポリシー施行、セキュリティ、およびオブザーバビリティ機能を提供します。
*   **Envoy Proxy**: Cloud Service Mesh (Istio) でサービス間のトラフィックを処理するために使用される高性能なオープンソースエッジ/サービスプロキシです。通常、アプリケーションのPodにサイドカーとしてデプロイされます。
*   **StatefulSet**: Kubernetesにおけるワークロードリソースの一種で、永続的な識別子、安定したネットワーク名、順序保証などの機能を提供し、ステートフルなアプリケーション（データベースなど）をデプロイおよびスケーリングするために設計されています。
*   **Job**: Kubernetesにおけるワークロードリソースの一種で、指定されたタスクを一度だけ実行し、完了したら終了するような有限のタスク（バッチ処理など）を管理するために使用されます。

---

# Compute Engine
## Changed
原文: Compute Engine enforces limits to the total baseline performance that a project's Hyperdisk Balanced and Hyperdisk Balanced High Availability disks that are in the same zone can consume at the same time. The aggregate baseline performance limit is 50 GiB/s of throughput and 500,000 IOPS, and it only applies to baseline performance. For a detailed explanation, see Concurrent consumption limits for baseline performance.

説明: Compute Engineにおいて、同一ゾーン内の単一プロジェクトが使用するHyperdisk BalancedおよびHyperdisk Balanced High Availabilityディスクの**集約されたベースラインパフォーマンス**に対して、合計制限が適用されるようになりました。この制限は、スループットで50 GiB/s、IOPSで500,000であり、ディスクのバーストパフォーマンスではなく、保証されたベースラインパフォーマンスにのみ適用されます。

影響有無:
Google Cloud Composer 2.7.1 (Airflow 2.7.3) 環境では、通常、標準的なPersistent DiskまたはSSD Persistent Diskが使用され、Hyperdisk Balancedが明示的に使用される構成は稀です。したがって、**直接的な影響は無い**と考えられます。
ただし、以下の条件をすべて満たす場合にのみ影響を受ける可能性があります。
*   Composer環境の基盤となるGKEクラスタノードや、AirflowのDAG実行で利用されるカスタムVMインスタンスが**Hyperdisk BalancedまたはHyperdisk Balanced High Availability**を使用している。
*   同一プロジェクト、同一ゾーン内で、これらのHyperdisk Balancedディスクが**極めて大量に、かつ高負荷**で使用されており、その合計ベースラインパフォーマンスがスループット50 GiB/sまたはIOPS 500,000の制限に達する可能性がある。

対処方法:
現在のComposer環境または関連するCompute EngineリソースでHyperdisk Balancedを使用しており、かつI/O集中型のワークロードが多数稼働している場合は、以下の対策を検討してください。
1.  **使用状況の確認**: [Concurrent consumption limits for baseline performance](https://cloud.google.com/compute/docs/disks/hyperdisk-performance#baseline_consumption_limits) ドキュメントを参照し、Hyperdisk Balancedの利用状況と現在のI/O消費量を評価してください。Google Cloud Monitoringを使用して、プロジェクト内のHyperdisk Balancedディスクの合計IOPSとスループットを監視できます。
2.  **分散戦略の検討**:
    *   ワークロードを異なるゾーンやリージョンに分散させることで、集約制限の影響を回避できます。
    *   プロジェクトを分割し、ディスクI/Oを複数のプロジェクトに分散させることも有効です。
3.  **ディスクタイプの見直し**:
    *   もし現在の制限がワークロードにとってボトルネックとなる場合、Hyperdisk Extremeのような高性能なディスクタイプへの移行を検討します。Hyperdisk Extremeにはこの集約制限は適用されません。
    *   I/Oパターンを最適化し、ディスクへのアクセス回数やデータ転送量を減らすことも効果的です。

用語説明:
*   **Hyperdisk Balanced**: Compute Engineが提供する高性能ブロックストレージの一種で、高いIOPSとスループットをバランス良く提供し、幅広いワークロードに適しています。
*   **Hyperdisk Balanced High Availability**: Hyperdisk Balancedの機能に加え、ゾーン障害に対する耐性を持つ高可用性オプションを提供します。
*   **ベースラインパフォーマンス**: ディスクが常に提供できる保証された最低限のパフォーマンスレベルです。一時的に高負荷時に到達可能な「バーストパフォーマンス」とは異なります。
*   **IOPS (Input/Output Operations Per Second)**: ストレージデバイスが1秒間に処理できる読み書き操作の回数を示す指標です。
*   **スループット**: ストレージデバイスが1秒間に転送できるデータ量を示す指標です。通常、GiB/s (ギビバイト/秒) などの単位で表されます。
# Title: September 15, 2025 
Link: https://cloud.google.com/release-notes#September_15_2025<br>
回答します。

---

# BigQuery
## Changed
原文:
*   **bigquery:** Add custom ExceptionHandler to BigQueryOptions (#3937) (de0914d)
*   Update dependency com.google.cloud:google-cloud-bigquerystorage-bom to v3.17.0 (#3954) (e73deed)
*   Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 (#3952) (79b7557)

説明:
Google Cloud BigQuery Javaクライアントライブラリのバージョン2.55.0における変更です。
BigQueryOptionsにカスタム例外ハンドラを追加する機能が実装されました。また、依存ライブラリである`google-cloud-bigquerystorage-bom`がバージョン3.17.0に、`sdk-platform-java-config`がバージョン3.52.1にそれぞれ更新されました。

影響有無:
影響なし。
当社のGoogle Cloud Composer2環境はPythonベースであり、Javaクライアントライブラリの更新は直接的な影響を与えません。

対処方法:
不要です。

---

# BigQuery
## Changed
原文:
*   Updates to fastpath query execution (#2268) (ef2740a)
*   Remove deepcopy while setting properties for _QueryResults (#2280) (33ea296)
*   Clarify that the presence of `XyzJob.errors` doesn't necessarily mean that the job has not completed or was unsuccessful (#2278) (6e88d7d)
*   Clarify the api_method arg for client.query() (#2277) (8a13c12)

説明:
Google Cloud BigQuery Pythonクライアントライブラリのバージョン3.37.0における変更です。
クエリ実行の高速化パスに関する更新が行われました。`_QueryResults`のプロパティ設定時に不要な`deepcopy`が削除され、内部的な効率が改善されています。
また、`XyzJob.errors`フィールドの存在が必ずしもジョブの未完了や失敗を意味するわけではないこと、および`client.query()`メソッドの`api_method`引数に関する説明が明確化されました。

影響有無:
影響は極めて軽微であり、改善の可能性があります。
これらの変更は主にパフォーマンスの最適化とドキュメント/エラーメッセージの明確化であり、既存のAPIの破壊的変更は含まれていません。そのため、既存のComposer 2環境で動作するBigQuery連携DAGの挙動に悪影響を与える可能性は低いと考えられます。むしろ、クエリ実行のパフォーマンス向上が期待できる可能性があります。
Composer環境でこのライブラリのバージョンが更新された場合、パフォーマンス改善の恩恵を受けることが期待されます。

対処方法:
原則として不要です。
もし、カスタムの`requirements.txt`で`google-cloud-bigquery`の特定のバージョンを固定している場合は、本バージョンに更新することでパフォーマンス改善の恩恵を受けられる可能性があります。バージョン更新を行う場合は、ステージング環境での十分なテストを推奨します。

用語説明:
*   **fastpath query execution (高速化パスのクエリ実行)**: BigQuery APIクライアントライブラリにおいて、特定の条件を満たすクエリに対して、より効率的で低レイテンシな実行経路を使用する最適化手法。これにより、クエリの処理速度が向上することが期待されます。
*   **deepcopy**: Pythonの`copy`モジュールで提供される関数の一つで、オブジェクトとそのオブジェクトが参照する全ての子オブジェクトを再帰的に複製し、完全に独立した新しいオブジェクトを作成すること。不要な`deepcopy`はメモリ消費や処理時間の増加につながるため、これを削除することは最適化の一環です。

---

# Cloud Logging
## Changed
原文:
*   **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 (1438bff)
*   Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 (#1853) (c21a635)
*   Update googleapis/sdk-platform-java action to v2.62.1 (#1855) (b6ce498)

説明:
Google Cloud Logging Javaクライアントライブラリのバージョン3.23.4における変更です。
Javaコードジェネレータ（gapic-generator-java）がバージョン2.62.1に更新されました。また、依存ライブラリである`sdk-platform-java-config`がバージョン3.52.1に更新され、GitHub Actions関連の構成も更新されています。

影響有無:
影響なし。
当社のGoogle Cloud Composer2環境はPythonベースであり、Javaクライアントライブラリの更新は直接的な影響を与えません。

対処方法:
不要です。

---

# Cloud Storage
## Changed
原文:
*   Respect useAuthWithCustomEndpoint flag for resumable uploads (#2637) (707b4f2)

説明:
Google Cloud Storage Node.jsクライアントライブラリのバージョン7.17.1における変更です。
カスタムエンドポイントを使用する再開可能なアップロードにおいて、認証フラグ`useAuthWithCustomEndpoint`が正しく尊重されるように修正されました。

影響有無:
影響なし。
当社のGoogle Cloud Composer2環境はPythonベースであり、Node.jsクライブラリの更新は直接的な影響を与えません。

対処方法:
不要です。

---

# Cloud Storage
## Changed
原文:
*   Add BlobInfo.ObjectContexts (#3259) (485aefd)
*   **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 (0e348db)
*   Update BlobAppendableUpload implementation to periodically flush for large writes (#3278) (d0ffe18)
*   Update otel integration to properly activate span context for lazy RPCs such as reads & writes pt.2 (#3277) (3240f67)
*   Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 (#3280) (d046ea3)
*   Update googleapis/sdk-platform-java action to v2.62.1 (#3281) (c9078bb)

説明:
Google Cloud Storage Javaクライアントライブラリのバージョン2.57.0における変更です。
`BlobInfo`に`ObjectContexts`が追加されました。また、大容量書き込み時に定期的にフラッシュを行うように`BlobAppendableUpload`の実装が更新され、パフォーマンスが改善されています。OpenTelemetryとの連携が改善され、遅延RPC（読み書きなど）におけるスパンコンテキストが適切にアクティブ化されるようになりました。
その他、Javaコードジェネレータおよび依存ライブラリ（`sdk-platform-java-config`）の更新、GitHub Actions関連の構成変更が含まれます。

影響有無:
影響なし。
当社のGoogle Cloud Composer2環境はPythonベースであり、Javaクライアントライブラリの更新は直接的な影響を与えません。

対処方法:
不要です。

---

# Pub/Sub
## Changed
原文:
*   **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 (ac08d5f)
*   Update actions/checkout action to v5 (#2531) (f687f11)
*   Update actions/setup-java action to v5 (#2535) (2ed87d2)
*   Update dependency com.google.cloud:google-cloud-bigquery to v2.54.2 (#2538) (10a8283)
*   Update dependency com.google.cloud:google-cloud-storage to v2.56.0 (#2536) (80d9ca1)
*   Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 (#2544) (9fe7550)
*   Update googleapis/sdk-platform-java action to v2.62.1 (#2545) (17f28ef)

説明:
Google Cloud Pub/Sub Javaクライアントライブラリのバージョン1.141.4における変更です。
Javaコードジェネレータ（gapic-generator-java）がバージョン2.62.1に更新されました。また、各種依存ライブラリ（`google-cloud-bigquery`, `google-cloud-storage`, `sdk-platform-java-config`）の更新と、GitHub Actions関連の構成変更が含まれます。

影響有無:
影響なし。
当社のGoogle Cloud Composer2環境はPythonベースであり、Javaクライアントライブラリの更新は直接的な影響を与えません。

対処方法:
不要です。

---