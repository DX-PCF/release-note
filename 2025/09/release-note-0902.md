
# Title: August 29, 2025 
Link: https://cloud.google.com/release-notes#August_29_2025<br>
以下は、提供されたリリースノートに基づいた、各製品への影響分析です。

---

# Artifact Registry

## Changed
原文: The Container Analysis API now supports the option of returning partial results during region-down failure conditions when listing notes, listing occurrences, or generating vulnerability summaries. For more information, view the `returnPartialSuccess` parameter for the following requests:
- v1.projects.locations.notes.list
- v1.projects.locations.occurrences.getVulnerabilitySummary
- v1.projects.locations.occurrences.list
- v1.projects.notes.list
- v1.projects.occurrences.getVulnerabilitySummary
- v1.projects.occurrences.list
- v1beta1.projects.locations.notes.list
- v1beta1.projects.locations.occurrences.getVulnerabilitySummary
- v1beta1.projects.locations.occurrences.list
- v1beta1.projects.notes.list
- v1beta1.projects.occurrences.getVulnerabilitySummary
- v1beta1.projects.occurrences.list

説明: Container Analysis APIが強化され、リージョン障害発生時でも、`notes`のリスト取得、`occurrences`のリスト取得、脆弱性サマリーの生成といった操作において、部分的な結果を返すオプション(`returnPartialSuccess`パラメータ)が利用可能になりました。これにより、完全なデータが取得できない状況でも、利用可能な情報の一部を取得できるようになります。

影響有無: 影響なし。
理由: この変更はAPIの新たな機能追加であり、既存のAPI呼び出しの動作を変更するものではありません。デフォルトで部分的な結果が返されるようになるわけではなく、明示的に`returnPartialSuccess`パラメータを指定した場合にのみ有効になります。

対処方法: 特になし。耐障害性の向上を目的として、APIクライアント側でこの新機能を活用することを検討できます。

用語説明:
*   **Container Analysis API**: Google Cloud Artifact Registry などに保存されたコンテナイメージやその他の成果物のセキュリティメタデータ（脆弱性、ビルド情報、デプロイ情報など）を管理および分析するためのAPIです。
*   **Notes**: コンテナイメージなどに関連する特定の情報や定義（例：既知の脆弱性、ライセンス規定）を表現するリソースです。
*   **Occurrences**: 特定のイメージに対してNoteが「発生した」という事実（例：このイメージにCVE-XXXXの脆弱性が検出された）を表現するリソースです。
*   **Vulnerability summaries**: プロジェクトやリソースにおける脆弱性の集計レポートです。
*   **`returnPartialSuccess` parameter**: APIリクエストにおいて、一部のデータが取得できない場合に完全なエラーを返すのではなく、取得できた部分的なデータを返すことを許可するかどうかを制御するブール値パラメータです。

---

# Google Kubernetes Engine

## Fixed
原文: A fix is available for an issue with Cloud Storage FUSE CSI driver that could cause Pod to be stuck during startup after a node restart event. Cloud Storage FUSE CSI driver now gracefully handles a node restart behavior.
The fix is available in the following GKE versions:
- 1.32.6-gke.1125000 and later
- 1.33.1-gke.1959000 and later

説明: Cloud Storage FUSE CSI ドライバーに存在する、ノード再起動後にPodが起動中にスタックする可能性のある問題が修正されました。この修正により、Cloud Storage FUSE CSI ドライバーがノードの再起動イベントをより適切に処理し、Podの安定した起動を保証します。この修正は、GKEバージョン1.32.6-gke.1125000以降および1.33.1-gke.1959000以降で適用されます。

影響有無: 影響あり（潜在的）。
理由: Google Cloud Composer2はGKEを基盤として動作し、Cloud Storage FUSE CSI ドライバーを使用してDAGファイル、ログ、プラグインなどをCloud Storageに永続化している可能性があります。もし現在ご利用のComposer環境のGKEバージョンが、上記修正バージョンより古い場合、ノードの再起動時にPodがスタックする問題が発生する可能性があります。これは、ワークロードの可用性と信頼性に直接影響する重要な修正です。

対処方法:
1.  **現在ご利用のComposer環境の基盤GKEバージョンを確認してください。** Google Cloud コンソールでComposer環境の詳細画面を開き、「基盤となるクラスタ」または関連するGKEクラスタのバージョンを確認します。
2.  確認したGKEバージョンが、上記の修正バージョン（1.32.6-gke.1125000または1.33.1-gke.1959000）より古い場合、**Composer環境のアップグレードを強く推奨します。** Composerのアップグレードにより、基盤となるGKEも更新され、この修正が適用されます。アップグレードの際は、ComposerとAirflowのバージョン互換性や、カスタムコードへの影響を事前に評価してください。
3.  Cloud Storage FUSE CSI ドライバーを明示的に使用していない場合でも、Composerの内部動作で利用されている可能性があるため、バージョン確認と必要に応じたアップグレードは推奨されます。

用語説明:
*   **Cloud Storage FUSE CSI driver**: Google Kubernetes Engine (GKE) において、Google Cloud Storage バケットをKubernetes Pod内にファイルシステムとしてマウントすることを可能にするContainer Storage Interface (CSI) ドライバーです。これにより、PodがCloud Storage上のファイルに直接アクセスできるようになります。
*   **Pod stuck during startup**: Kubernetes Podが起動処理中に停止し、正常に稼働状態に移行できない状況です。これはアプリケーションのデプロイやサービスの可用性に影響を与えます。
*   **Node restart event**: GKEクラスタ内のCompute Engine VMインスタンス（ノード）が再起動される事象です。これは計画的なメンテナンス（ノードの自動アップグレードなど）や、予期せぬ基盤インフラストラクチャの障害によって発生する可能性があります。
*   **GKE versions**: Google Kubernetes Engineのバージョン管理体系。`X.Y.Z-gke.A`形式で、`X.Y.Z`がKubernetesのバージョン、`-gke.A`がGKE固有のパッチレベルを示します。

---

# Spanner

## Libraries

Spannerのリリースノートは、主に各プログラミング言語向けクライアントライブラリの更新に関するものです。Spannerサービス本体の変更ではないため、既存のアプリケーションが明示的にこれらのライブラリバージョンにアップグレードしない限り、直接的な影響は生じません。

### Go

## Changes for spanner/admin/database/apiv1
原文:
[1.84.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.83.0...spanner/v1.84.0)
- **spanner/adapter:** Add last field in AdaptMessageResponse for internal optimization usage (c574e28)
- **spanner/admin/database:** Proto changes for an internal api (eeb4b1f)
- **spanner:** A new field `snapshot_timestamp` is added to message `.google.spanner.v1.CommitResponse` (ac4970b)
- **spanner:** Add Google Cloud standard otel attributes (#11652) (f59fcff)
- **spanner:** Context cancel in traces in case of skipping trailers (#12635) (509dc90)
- **spanner:** Enforce only one resource header (#12618) (4e04b7e)
- **spanner:** Fix blind retry for ResourceExhausted (#12523) (f9b6e88)
- **spanner:** Remove stream wrapper for direct path check (#12622) (88a36cd)
- **spanner:** A comment for enum value `OPTIMISTIC` in enum `ReadLockMode` is changed (ac4970b)
- **spanner:** A comment for enum value `PESSIMISTIC` in enum `ReadLockMode` is changed (ac4970b)
- **spanner:** A comment for enum value `READ_LOCK_MODE_UNSPECIFIED` in enum `ReadLockMode` is changed (ac4970b)
- **spanner:** A comment for field `commit_stats` in message `.google.spanner.v1.CommitResponse` is changed (ac4970b)
- **spanner:** A comment for field `exclude_txn_from_change_streams` in message `.google.spanner.v1.TransactionOptions` is changed (ac4970b)
- **spanner:** A comment for field `multiplexed_session_previous_transaction_id` in message `.google.spanner.v1.TransactionOptions` is changed (ac4970b)
- **spanner:** A comment for field `precommit_token` in message `.google.spanner.v1.CommitResponse` is changed (ac4970b)
- **spanner:** A comment for message `.google.spanner.v1.MultiplexedSessionPrecommitToken` is changed (ac4970b)
- **spanner:** A comment for message `.google.spanner.v1.TransactionOptions` is changed (ac4970b)

[1.84.1](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.84.0...spanner/v1.84.1)
- **spanner:** Release 1.84.1 (#12663) (8b410ec)
- **spanner:** Release 1.84.1 (#12665) (a1ce8c2)
**DO NOT USE** This version is retracted due to https://github.com/googleapis/google-cloud-go/issues/12659, use version >=v1.84.1

説明: Google Cloud GoクライアントライブラリのSpannerモジュールに複数の変更が加えられました。内部最適化、APIプロトコル定義の変更、`CommitResponse`に`snapshot_timestamp`フィールドの追加、OpenTelemetry属性のサポート、トレースやリトライメカニズムに関する修正、リソースヘッダーの強制に関する改善が含まれます。特に、バージョン1.84.0には既知の問題があるため、使用を避けてバージョン1.84.1以降を使用するよう推奨されています。

影響有無: 影響なし。
理由: これらの変更はGo言語向けSpannerクライアントライブラリの更新であり、Google Cloud Composer2はPythonベースであるため、直接的な影響はありません。もしGo言語でSpannerを利用するカスタムアプリケーションがある場合、影響が生じる可能性がありますが、既存の利用を破壊する変更は含まれていません。

対処方法: 特になし。
もしGo言語でSpannerを利用する独自のアプリケーションがある場合は、クライアントライブラリをバージョン1.84.1以降にアップグレードすることを検討し、変更点を評価した上でテストを行ってください。バージョン1.84.0は使用しないでください。

用語説明:
*   **OpenTelemetry**: 分散トレース、メトリクス、ログなどのテレメトリーデータを収集・エクスポートするためのベンダーニュートラルなオープンソースフレームワークです。
*   **`CommitResponse`**: Spannerトランザクションのコミット操作が成功した際に返されるレスポンスオブジェクトです。
*   **`snapshot_timestamp`**: Spannerトランザクションがコミットされた時点のタイムスタンプ情報です。

### Java

## Changes for google-cloud-spanner
原文:
[6.98.0](https://github.com/googleapis/java-spanner/compare/v6.97.1...v6.98.0)
- Proto changes for an internal api (675e90b)
- **spanner:** A new field `snapshot_timestamp` is added to message `.google.spanner.v1.CommitResponse` (675e90b)
- Support Exemplar (#3997) (fcf0a01)
- Use multiplex sessions for RW and Partition Ops (#3996) (a882204)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 (675e90b)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 (#4004) (986c0e0)

[6.98.1](https://github.com/googleapis/java-spanner/compare/v6.98.0...v6.98.1)
- Add missing span.end calls for AsyncTransactionManager (#4012) (1a4adb4)
- **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 (8156ef3)
- Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 (#4013) (4e90c29)

説明: Google Cloud JavaクライアントライブラリのSpannerモジュールに更新が加えられました。内部APIのプロトコル変更、`CommitResponse`に`snapshot_timestamp`フィールドの追加、Exemplarのサポート、読み書きおよびパーティション操作でのマルチプレックスセッションの利用、依存関係の更新、`AsyncTransactionManager`におけるトレース関連の修正などが含まれます。

影響有無: 影響なし。
理由: これらの変更はJava言語向けSpannerクライアントライブラリの更新であり、Google Cloud Composer2はPythonベースであるため、直接的な影響はありません。もしJava言語でSpannerを利用するカスタムアプリケーションがある場合、影響が生じる可能性がありますが、既存の利用を破壊する変更は含まれていません。

対処方法: 特になし。
もしJava言語でSpannerを利用する独自のアプリケーションがある場合は、クライアントライブラリをアップグレードすることを検討し、変更点を評価した上でテストを行ってください。

用語説明:
*   **Exemplar**: 分散トレースの特定のトレースIDをメトリクスに関連付けることで、メトリクスが生成された特定のイベントのコンテキストを理解するのに役立つ機能です。
*   **Multiplex sessions**: Spannerクライアントが複数の並行トランザクションや操作に対して単一のセッション（バックエンド接続）を再利用する機能です。これにより、セッション管理のオーバーヘッドが削減され、効率が向上します。

### Node.js

## Changes for @google-cloud/spanner
原文:
[8.1.0](https://github.com/googleapis/nodejs-spanner/compare/v8.0.0...v8.1.0)
- Add Custom OpenTelemetry Exporter in for Service Metrics (#2272) (610d1b9)
- Add methods from gax to cache proto root and process custom error details (#2330) (1b3931a)
- Add metrics tracers (#2319) (192bf2b)
- Add support for AFE latency metrics (#2348) (0666f05)
- Add throughput_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https://github.com/GoogleCloudPlatform/spanner-migration-tool (#2304) (a29af56)
- Operation, Attempt, and GFE metrics (#2328) (646e6ea)
- Proto changes for an internal api (#2356) (380e770)
- **spanner:** A new field `snapshot_timestamp` is added to message `.google.spanner.v1.CommitResponse` (#2350) (0875cd8)
- **spanner:** Add new change_stream.proto (#2315) (57d67be)
- **spanner:** Add tpc support (#2333) (a381cab)
- Track precommit token in r/w apis(multiplexed session) (#2312) (3676bfa)
- Docs-test (#2297) (61c571c