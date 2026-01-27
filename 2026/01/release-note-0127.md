
# Title: January 26, 2026 
Link: https://docs.cloud.google.com/release-notes#January_26_2026<br>
はい、承知いたしました。Google Cloud のリリースノートを元に、Cloud Logging の変更点について影響有無を調査し、簡潔に回答いたします。

---

# Cloud Logging
## Change
原文:
To support correlation between log and trace data, the following changes have been made:
- The required format for the `LogEntry.trace` field has been relaxed. The preferred format for this field is the trace ID. However, you can continue to provide the full resource name. For more information, see [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).
- If you open the **Trace Details flyout** page by using options provided in a log entry, then the resources listed in the default trace scope are searched for the trace data.
- If you open the **Logs Explorer** page by using options on span data, then the resources listed in the default log scope are searched for log data.
To learn more about default scopes, see [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).

説明：
このリリースでは、ログとトレースデータの関連付けをサポートするために、以下の改善が実施されました。

1.  **`LogEntry.trace` フィールドのフォーマット緩和**:
    *   ログエントリの `LogEntry.trace` フィールドに指定するトレースIDの必須フォーマットが緩和されました。
    *   これまでは完全なリソース名（例: `projects/PROJECT_ID/traces/TRACE_ID`）が必要でしたが、今後は単にトレースID（例: `TRACE_ID`）のみを指定することも可能になります。
    *   既存の完全なリソース名形式も引き続きサポートされます。

2.  **UIにおける検索挙動の改善**:
    *   ログエントリから **Trace Details flyout** ページ（トレース詳細サイドバー）を開いた際に、デフォルトのトレーススコープ内でトレースデータが検索されるようになりました。
    *   スパンデータから **Logs Explorer** ページ（ログエクスプローラ）を開いた際に、デフォルトのログスコープ内でログデータが検索されるようになりました。

これにより、ログとトレースの間のナビゲーションとデータ検索の利便性が向上します。

影響有無：
**影響なし**
*   **`LogEntry.trace` フィールドのフォーマット緩和**: 既存のログ記録プロセスが完全なリソース名形式で `LogEntry.trace` を出力している場合でも、引き続き正常に動作します。これは互換性を維持した上での機能改善であり、既存のシステムに悪影響を与えるものではありません。
*   **UI検索挙動の改善**: これはGoogle CloudコンソールUIにおけるユーザーエクスペリエンス（UX）の向上を目的としたものであり、既存のログ収集、保存、分析のパイプラインやワークロードに直接的な変更や影響はありません。

対処方法：
**不要**
*   既存のシステム構成や運用に変更の必要はありません。
*   もし今後、ログにトレースIDを付与する実装を行う場合は、より簡潔なトレースIDのみの形式を採用することが可能です。

用語説明：
*   **`LogEntry.trace`**: Cloud Logging のログエントリ（`LogEntry`）の構造に含まれるフィールドの一つで、このログエントリが関連付けられているトレースのIDを指定するために使用されます。これにより、分散トレーシングにおいて特定のログがどのリクエストの一部であるかを追跡しやすくなります。
*   **Trace ID**: 分散システムにおいて、単一のエンドツーエンドのリクエストのライフサイクル全体を追跡するための、一意の識別子です。Google Cloud Trace などで利用され、異なるサービス間をまたがるリクエストのパスとレイテンシを可視化するのに役立ちます。
*   **Resource name (リソース名)**: Google Cloud における特定のリソースを一意に識別するための標準的なパス形式です。例えば、Cloud Storage バケット、Compute Engine インスタンス、あるいは特定のトレースなど、あらゆるリソースに適用されます。`projects/PROJECT_ID/traces/TRACE_ID` のように階層的に構成されます。
*   **Trace Details flyout**: Google Cloud コンソールの Cloud Trace サービスUIにおいて、特定のトレースの詳細情報を表示する際に現れる、画面のサイドから飛び出す（flyout）形式のパネルまたはウィンドウのことです。トレース内の個々のスパンやその属性を確認できます。
*   **Logs Explorer**: Google Cloud コンソールの Cloud Logging サービスUIにおける主要なツールで、プロジェクト内のログデータを検索、フィルタリング、表示、分析するためのインタフェースです。
*   **Span data (スパンデータ)**: 分散トレースにおいて、単一の論理的な操作（例：関数呼び出し、APIリクエスト、データベースクエリ）を表すデータ単位です。一つのトレースは複数のネストされたスパンで構成され、各スパンは開始時間、終了時間、属性などの情報を含みます。
*   **Observability scopes (オブザーバビリティスコープ)**: Google Cloud Monitoring、Logging、Trace などのオブザーバビリティサービスにおいて、複数のGoogle Cloudプロジェクトにまたがるデータを一元的に表示・管理するための機能です。特定のプロジェクト（スコーププロジェクト）を設定することで、そのプロジェクトおよび関連付けられた他のプロジェクト（監視対象プロジェクト）のメトリクス、ログ、トレースを統合的に確認できるようになります。
# Title: January 23, 2026 
Link: https://docs.cloud.google.com/release-notes#January_23_2026<br>
Google Cloud のリリースノート調査結果をご報告いたします。

---

# BigQuery
## Change
原文: You can now optionally specify which model to use by passing an endpoint argument to the `AI.IF`, `AI.SCORE`, and `AI.CLASSIFY` functions.

説明：
BigQuery MLのAI関数（`AI.IF`、`AI.SCORE`、`AI.CLASSIFY`）において、新しくオプションの`endpoint`引数を指定できるようになりました。これにより、これらの関数が推論に利用する特定のモデル（例えば、Vertex AIでデプロイされたGenerative AIモデルなど）を明示的に選択し、指定することが可能になります。

影響有無：
**影響なし**
この変更は、既存の関数に新しいオプション引数が追加されたものです。既存のクエリやこれらの関数の使用方法が変更されるわけではなく、`endpoint`引数を指定しない場合は、これまで通りデフォルトの動作が維持されます。そのため、現在のワークロードやサービス運用に直接的な影響はありません。

対処方法：
**対応不要**
この機能は追加機能であるため、即座に対応する必要はありません。
将来的に、BigQuery MLのAI関数を利用して、より詳細なモデル制御や特定のモデルバージョンを指定した推論を行いたい場合に、この新機能を活用することを検討できます。

用語説明：
*   **BigQuery ML:** BigQuery内でSQL構文を使用して機械学習モデルを構築、学習、評価、デプロイできる機能です。データがBigQueryに保存されているため、データを移動させることなく機械学習を実行できます。
*   **AI関数 (`AI.IF`, `AI.SCORE`, `AI.CLASSIFY`):** BigQuery MLで提供される、生成AIや予測AIといった高度な機械学習機能をSQLから直接呼び出すための関数群です。
    *   `AI.IF`: 一般的に、条件に基づいてAI推論を実行する際に使用されます。
    *   `AI.SCORE`: モデルから予測スコア（例: 回帰モデルの予測値、異常度など）を取得する際に使用されます。
    *   `AI.CLASSIFY`: 分類モデルから予測クラスラベル（例: スパム判定、顧客セグメントなど）を取得する際に使用されます。
*   **endpoint argument:** AI関数が推論を実行するために接続する特定のモデルやAPIの場所（エンドポイント）を指定するための引数です。例えば、Vertex AIでデプロイされたカスタムモデルや、特定のGenerative AIモデルのエンドポイントを明示的に指定することで、利用可能な複数のモデルの中から目的のモデルを選択して推論を実行できるようになります。