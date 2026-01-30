
# Title: January 28, 2026 
Link: https://docs.cloud.google.com/release-notes#January_28_2026<br>
以下は、BigQueryのリリースノートに対する調査結果です。

---

# BigQuery

## Change
原文: The BigQuery change data capture feature has been renamed to BigQuery change data capture ingestion.
[BigQuery change data capture ingestion](https://docs.cloud.google.com/bigquery/docs/change-data-capture)

説明:
BigQueryの既存機能である「Change Data Capture (CDC)」の名称が「BigQuery change data capture ingestion」に変更されました。これは機能自体の変更ではなく、名称のみの変更です。ドキュメントのURLは変更後の名称に合わせて更新されていますが、参照先の内容に変更はありません。

影響有無:
**影響なし。**
この変更は、BigQueryのChange Data Capture (CDC) 機能の名称変更のみであり、機能の動作、API、構成、パフォーマンス、料金体系に一切の変更はありません。既存のデータパイプラインやアプリケーションへの影響は発生しません。

対処方法:
特別なシステム的な対処は不要です。
社内ドキュメント、運用手順書、またはアプリケーションコード内で「BigQuery Change Data Capture」という旧名称を使用している場合は、将来的な混乱を避けるため、「BigQuery change data capture ingestion」という新名称への更新を推奨します。

用語説明:
*   **Change Data Capture (CDC):** データベースにおけるデータの変更（挿入、更新、削除）を検出し、その変更イベントを捕捉する技術です。これにより、データウェアハウスへの差分データのリアルタイムまたは準リアルタイムでの取り込み、データのレプリケーション、監査ログの生成などが可能になります。
*   **Ingestion:** データをシステムに取り込む、または取り込み処理を行うことを指します。この文脈では、変更されたデータ（差分データ）をBigQueryに取り込む処理を意味します。
# Title: January 27, 2026 
Link: https://docs.cloud.google.com/release-notes#January_27_2026<br>
はい、Google Cloudのリリースノートに関する調査結果を報告します。

---

# BigQuery
## Change
原文: An updated version of the Simba JDBC driver for BigQuery is now available.
[Simba JDBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_jdbc_driver)

説明：
Google BigQueryへの接続に使用されるSimba JDBC (Java Database Connectivity) ドライバーの新しいバージョンがリリースされました。このドライバーは、JavaアプリケーションがBigQueryに接続し、クエリの実行やデータ操作を行うための標準インターフェースを提供します。通常、ドライバーの更新には、パフォーマンスの改善、バグ修正、新しい機能のサポート、およびセキュリティ強化が含まれます。

影響有無：
**直接的な影響はありません。**
このリリースはBigQueryサービス本体（データウェアハウス機能）の変更ではなく、BigQueryに接続するためのクライアント側ドライバーの更新です。

ただし、以下の場合には**間接的な影響があり、対応を検討する必要があります。**
*   **Simba JDBCドライバーを利用している場合:** 貴社のシステム内でBigQueryへJavaアプリケーションがSimba JDBCドライバーを介して接続している場合、新しいバージョンに更新することで、パフォーマンスの向上、安定性の改善（バグ修正）、または新機能の利用が可能になります。
*   **Google Cloud Composer 2 (Airflow) について:** Google Cloud Composer 2 は主にPythonベースで動作するため、通常はPythonのBigQueryクライアントライブラリを使用します。そのため、Composer環境自体が直接Simba JDBCドライバーを利用している可能性は極めて低いと考えられます。しかし、Composerから呼び出される外部システムやカスタムアプリケーション（例えば、Javaで開発されたカスタムオペレーターや外部連携ツール）がBigQueryへの接続にJDBCを利用している場合は、関連する可能性があります。

対処方法：
1.  **利用状況の確認:** 貴社のシステムでBigQueryへの接続にSimba JDBCドライバーが使用されているかを確認してください。特に、JavaベースのETLツール、BIツール、カスタムアプリケーションなどでBigQueryに接続している場合は、そのドライバーのバージョンを確認してください。
2.  **アップグレードの検討:** Simba JDBCドライバーを利用している場合、提供されたリンク先のドキュメントを参照し、新しいドライバーへのアップグレードを検討してください。アップグレードの際には、テスト環境での互換性確認と動作検証を十分に行い、本番環境への影響がないことを確認してください。
3.  **リリースノートの詳細確認:** 新しいドライバーバージョンに含まれる具体的な変更点（新機能、修正されたバグ、パフォーマンス改善など）をリリースノートやドキュメントで確認し、ご自身のシステムにとってのメリットを評価してください。

用語説明：
*   **Simba JDBC driver for BigQuery**: Javaアプリケーションが標準的なJava Database Connectivity (JDBC) APIを介してGoogle BigQueryに接続できるようにするためにSimba Technologies社が提供するソフトウェアドライバーです。これにより、Javaで書かれたプログラムからBigQueryのデータにアクセスし、SQLクエリを実行することが可能になります。
*   **JDBC (Java Database Connectivity)**: JavaプログラムからリレーショナルデータベースにアクセスするためのAPI（Application Programming Interface）の標準仕様です。JDBCドライバーは、このAPIを実装し、特定のデータベース（この場合はBigQuery）との通信を可能にします。
# Title: January 26, 2026 
Link: https://docs.cloud.google.com/release-notes#January_26_2026<br>
# Cloud Logging

## Change
原文:
```
 To support correlation between log and trace data, the following changes have
been made:

- The required format for the `LogEntry.trace` field has been relaxed. The
preferred format for this field is the trace ID. However, you can continue
to provide the full resource name. For more information, see
`LogEntry`.
- If you open the **Trace Details flyout** page by using options provided in a
log entry, then the resources listed in the default trace scope are searched
for the trace data.
- If you open the **Logs Explorer** page by using options on span data, then
the resources listed in the default log scope are searched for log data.

 The required format for the `LogEntry.trace` field has been relaxed. The
preferred format for this field is the trace ID. However, you can continue
to provide the full resource name. For more information, see
`LogEntry`.

[`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)
 If you open the **Trace Details flyout** page by using options provided in a
log entry, then the resources listed in the default trace scope are searched
for the trace data.

 If you open the **Logs Explorer** page by using options on span data, then
the resources listed in the default log scope are searched for log data.

 To learn more about default scopes, see
Configure observability scopes for multi-project queries.

[Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes)
```

説明：
このリリースでは、Cloud LoggingとCloud Trace間のログおよびトレースデータの相関を強化するための機能改善が行われました。

主な変更点は以下の3つです。

1.  **`LogEntry.trace` フィールドのフォーマット要件緩和**:
    ログエントリ内のトレース情報を格納する `LogEntry.trace` フィールドについて、そのフォーマット要件が緩和されました。これまでは完全なリソース名形式が必要でしたが、今後は単一のトレースID形式での指定が推奨されるようになります。既存の完全なリソース名形式も引き続きサポートされるため、互換性は維持されます。
2.  **ログエントリからのトレース詳細表示時の検索挙動改善**:
    Cloud Loggingのログエントリから「Trace Details flyout」（トレース詳細サイドバー）ページを開く際に、デフォルトで定義されているトレーススコープ内でトレースデータが自動的に検索されるようになりました。これにより、関連するトレースデータの発見が容易になります。
3.  **スパンデータからのログエクスプローラ表示時の検索挙動改善**:
    Cloud Traceのスパンデータから「Logs Explorer」（ログエクスプローラ）ページを開く際に、デフォルトで定義されているログスコープ内で関連するログデータが自動的に検索されるようになりました。これにより、トレースからログへの連携がスムーズになります。

これらの変更は、複数のプロジェクトにまたがる観測可能性データ（ログ、トレース）の関連付けと調査の利便性を向上させることを目的としています。

影響有無：
**影響なし（ポジティブな改善）**

*   **理由**:
    *   `LogEntry.trace` フィールドのフォーマット要件緩和は、既存の利用方法に対する後方互換性を維持しつつ、より柔軟な指定が可能になったことを意味します。既存のログ取り込みパイプラインやアプリケーションコードに破壊的な変更は生じません。
    *   UIからのトレース・ログ連携の挙動改善は、ユーザーエクスペリエンスの向上とトラブルシューティングの効率化を目的としたものであり、既存のシステム運用に悪影響を与えるものではありません。
    *   本リリースには、既存サービスの動作変更（Breaking Change）、料金体系の変更、パフォーマンスの低下、セキュリティ上の脆弱性、リージョン/ゾーンに関する変更は含まれていません。

対処方法：
**特に対処は不要です。**

*   既存のログ取り込み設定やアプリケーションコードを変更する必要はありません。
*   もし将来的に `LogEntry.trace` フィールドへの書き込み形式をトレースIDのみに統一することを検討する場合でも、このリリースによってそれが可能になったと理解してください。

用語説明：
*   **LogEntry.trace**: Cloud Loggingの各ログエントリに付与できるフィールドで、そのログがどのCloud Traceのトレースに関連するかを示すための情報（トレースIDや完全なリソース名）を格納します。これにより、分散システムにおける処理の流れをログとトレースで紐付けて追跡できます。
*   **トレースID (Trace ID)**: Cloud Traceで一連のリクエストや操作全体を一意に識別するために用いられるIDです。複数のサービスやコンポーネントを跨がる処理の最初から最後までを追跡する際に使用されます。
*   **リソース名 (Resource Name)**: Google Cloudのリソース（例: プロジェクト、トレース、バケットなど）を一意に識別するためのURI形式の文字列です。例えば、トレースのリソース名は `projects/PROJECT_ID/traces/TRACE_ID` のようになります。
*   **Trace Details flyout**: Cloud LoggingやCloud Traceのユーザーインターフェースにおいて、特定のログエントリやスパンに関連する詳細なトレース情報を表示する、画面の側面から飛び出す形式のペイン（サイドバー）です。
*   **Logs Explorer**: Cloud LoggingのWeb UIの一部で、収集されたログを検索、フィルタリング、表示、分析するための主要なツールです。
*   **スパンデータ (Span Data)**: Cloud Traceにおいて、トレースを構成する個々の論理的な作業単位（例: 関数の実行、HTTPリクエスト、データベースクエリなど）を表すデータ構造です。各スパンは、その操作名、開始/終了時刻、属性などを含みます。
*   **デフォルトスコープ (Default Scope)**: Google Cloudの観測可能性（Observability）機能（Cloud Logging, Cloud Traceなど）において、特定のクエリを実行する際に、デフォルトで検索対象とするプロジェクトやリソースの範囲を定義する設定です。これにより、マルチプロジェクト環境で複数のプロジェクトのログやトレースを横断的に調査する際の範囲を指定できます。詳細については、提供されているリンク「Configure observability scopes for multi-project queries」を参照してください。