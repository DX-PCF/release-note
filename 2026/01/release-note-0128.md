
# Title: January 26, 2026 
Link: https://docs.cloud.google.com/release-notes#January_26_2026<br>
Google Cloud のインフラエンジニアとして、リリースノートに基づき、お客様のサービスへの影響を調査し、以下の通りご報告いたします。

---

# Cloud Logging

## Change

原文: To support correlation between log and trace data, the following changes have been made:

- The required format for the `LogEntry.trace` field has been relaxed. The preferred format for this field is the trace ID. However, you can continue to provide the full resource name. For more information, see `LogEntry`.
- If you open the **Trace Details flyout** page by using options provided in a log entry, then the resources listed in the default trace scope are searched for the trace data.
- If you open the **Logs Explorer** page by using options on span data, then the resources listed in the default log scope are searched for log data.

The required format for the `LogEntry.trace` field has been relaxed. The preferred format for this field is the trace ID. However, you can continue to provide the full resource name. For more information, see `LogEntry`.

[`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
If you open the **Trace Details flyout** page by using options provided in a log entry, then the resources listed in the default trace scope are searched for the trace data.

If you open the **Logs Explorer** page by using options on span data, then the resources listed in the default log scope are searched for log data.

To learn more about default scopes, see Configure observability scopes for multi-project queries.

[Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes)

説明：
この変更は、ログとトレースデータの関連付けを強化するためにCloud Loggingに適用されるものです。主な内容は以下の3点です。

1.  **`LogEntry.trace`フィールドのフォーマット要件緩和**:
    *   ログエントリ内のトレースIDを示す`LogEntry.trace`フィールドにおいて、これまでより柔軟なフォーマットが許容されるようになりました。推奨されるフォーマットはシンプルに「Trace ID」ですが、これまで通り「完全なリソース名（Full Resource Name）」も引き続き使用可能です。
2.  **ログエントリからのトレース詳細表示時の検索範囲**:
    *   Cloud Loggingのログエクスプローラから特定のログを選択し、関連するトレースの詳細を表示する「Trace Details flyout」を開いた場合、トレースデータは「デフォルトのトレーススコープ」に設定されたリソース内で検索されるようになります。
3.  **スパンデータからのログエクスプローラ表示時の検索範囲**:
    *   Cloud Traceなどのスパンデータから、関連するログを表示するために「Logs Explorer」を開いた場合、ログデータは「デフォルトのログスコープ」に設定されたリソース内で検索されるようになります。

これらの変更は、ログとトレースの相関関係の視認性を向上させ、マルチプロジェクト環境におけるデータ検索の効率化を目的としています。

影響有無：
直接的な影響は軽微ですが、間接的な影響は発生する可能性があります。

1.  **`LogEntry.trace`フィールドのフォーマット要件緩和**:
    *   **影響なし（むしろ改善）**：既存のログ取り込み処理が`LogEntry.trace`フィールドに「完全なリソース名」を設定している場合でも、引き続き動作します。フォーマットが緩和されたことで、将来的なログ生成処理の柔軟性が向上します。Google Cloud Composer 2 (Compoer version 2.7.1, Airflow version 2.7.3)が内部的にログをCloud Loggingに送信する際の動作に影響はありません。
2.  **UIからの遷移時の検索範囲変更**:
    *   **間接的に影響あり**：ユーザーインターフェース（UI）上の動作変更であり、既存のログやトレースのデータ収集・処理には直接的な影響はありません。しかし、特定のトレースやログがデフォルトの観測スコープ外のプロジェクトに存在する場合、これまでは表示されていたものが見えなくなる可能性があります。これは、ログやトレースを利用してシステムの問題を調査する際のユーザーエクスペリエンスに影響を与える可能性があります。

対処方法：
特別なシステム変更は不要ですが、運用上の確認を推奨します。

1.  **`LogEntry.trace`フィールドのフォーマット要件緩和**:
    *   **対処不要**：既存のログ取り込みに影響はありません。
2.  **UIからの遷移時の検索範囲変更**:
    *   **運用上の確認**：
        *   複数のGoogle Cloudプロジェクトにまたがるシステムを運用しており、ログとトレースの相関関係を頻繁に調査している場合、`Configure observability scopes for multi-project queries` ドキュメントを参照し、現在のデフォルトの観測スコープが意図した範囲をカバーしているか確認してください。
        *   必要に応じて、観測スコープの設定を見直し、すべての関連プロジェクトが適切に含まれるように調整することで、ログとトレースの連携表示が期待通りに機能することを確認できます。これにより、Cloud Composerが出力するAirflowのログやタスク実行のトレース調査もスムーズに行えます。

用語説明：
*   **`LogEntry.trace`**: Cloud Loggingのログエントリの構造体に含まれるフィールドの一つで、そのログが関連する分散トレースのIDを示すために使用されます。ログとトレースを関連付けて表示する際のキーとなります。
*   **Trace ID**: 分散トレースを一意に識別するためのIDです。マイクロサービスアーキテクチャなどで、複数のサービスをまたがる単一のリクエストの処理経路を追跡するために使われます。
*   **フルリソース名 (Full Resource Name)**: Google Cloudリソースを一意に識別するための完全なパス（URI形式）です。例：`projects/PROJECT_ID/traces/TRACE_ID`。
*   **Trace Details flyout**: Cloud Loggingのログエクスプローラから特定のログエントリを選択した際に、そのログに関連するトレースの詳細情報を表示するためにポップアップ表示される小窓（サイドパネル）機能です。
*   **Logs Explorer**: Cloud LoggingのWeb UIで提供される、ログを検索、フィルタリング、表示するための主要なツールです。
*   **Span data (スパンデータ)**: 分散トレースを構成する最小単位の操作（例: 関数呼び出し、APIリクエスト、データベースクエリなど）を表すデータです。各スパンは開始時刻、終了時刻、処理内容、属性などの情報を含みます。
*   **Observability scopes (観測スコープ)**: Cloud Monitoring, Cloud Logging, Cloud TraceなどのGoogle Cloudの観測プロダクトで、複数のGoogle Cloudプロジェクトにまたがるデータを集約して表示・分析するための設定です。これにより、単一のビューで組織全体のシステムの状態を把握しやすくなります。