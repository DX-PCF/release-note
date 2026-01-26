
# Title: January 23, 2026 
Link: https://docs.cloud.google.com/release-notes#January_23_2026<br>
# BigQuery

## Change
原文: You can now optionally specify which model to use by passing an endpoint argument to the `AI.IF`, `AI.SCORE`, and `AI.CLASSIFY` functions.
[`AI.IF`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-if)
[`AI.SCORE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-score)
[`AI.CLASSIFY`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-classify)

説明：
BigQuery MLのAIファンクション（`AI.IF`, `AI.SCORE`, `AI.CLASSIFY`）を使用する際に、オプションとして利用するモデルの特定のエンドポイントを指定できるようになりました。これにより、より詳細にどのモデル（例：異なるバージョンやカスタムチューニングされたモデル）で推論を実行するかを制御することが可能になります。以前は、これらの関数はデフォルトで自動的に最適なモデルを選択していました。

影響有無：
**影響なし。**
これはBigQuery MLの既存のAIファンクションに対する**機能追加**であり、既存の動作に非互換性のある変更（Breaking Change）はありません。`endpoint`引数はオプションであるため、既存のクエリが影響を受けることはありません。BigQuery MLのGenerative AI機能をより柔軟に利用したい場合に、この新機能が活用できます。

対処方法：
**不要。**
既存のBigQuery MLの利用方法を変更する必要はありません。もし特定のGenerative AIモデルのエンドポイントを指定して推論を実行したい場合は、この新機能を活用できます。詳細は、各関数の公式ドキュメント（上記リンク参照）をご確認ください。

用語説明：
*   **BigQuery ML (BQML):** Google CloudのデータウェアハウスであるBigQuery内で、SQLクエリを使って機械学習モデルを直接構築、トレーニング、評価、デプロイできる機能。データ移動なしで分析と機械学習を統合できます。
*   **AI Functions (BigQuery ML):** BigQuery MLが提供する、SQLクエリからGenerative AIモデル（例: Geminiモデルなど）や他のAIサービスを直接呼び出せる関数群。`AI.GENERATE_TEXT`などもこれに含まれます。
*   **Endpoint:** 機械学習モデルがデプロイされ、外部からの推論リクエストを受け付けるために公開されているネットワークアドレス。特定のエンドポイントを指定することで、特定のモデルバージョンや、特定のカスタムチューニングが施されたモデルを利用できます。
*   **Generative AI (生成AI):** テキスト、画像、音声、コードなどの新しいコンテンツを生成する能力を持つ人工知能モデルの総称。
# Title: January 22, 2026 
Link: https://docs.cloud.google.com/release-notes#January_22_2026<br>
## BigQuery

### Change
原文: You can now run queries that use the `AI.IF`, `AI.SCORE`, and `AI.CLASSIFY` functions by using your end-user credentials instead of a BigQuery connection.
[`AI.IF`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-if)
[`AI.SCORE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-score)
[`AI.CLASSIFY`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-classify)
[end-user credentials](https://cloud.google.com/bigquery/docs/permissions-for-ai-functions)

説明：
BigQuery MLが提供するGenerative AI関数である`AI.IF`、`AI.SCORE`、`AI.CLASSIFY`を実行する際、従来のBigQuery Connection（接続）を使用する代わりに、エンドユーザー自身の認証情報（End-user credentials）を利用できるようになりました。これにより、AI関数を利用する際の認証の柔軟性が向上します。

影響有無：
**影響なし（ポジティブな追加機能）**
この変更は、既存の認証方法が無効になるものではなく、新たな認証オプションが追加されたものです。したがって、現在BigQuery ConnectionでAI関数を利用している既存のワークロードに直接的な影響はありません。
エンドユーザー認証を利用することで、よりきめ細やかな権限管理が可能となり、最小権限の原則に基づいたセキュリティ体制を強化できる可能性があります。

対処方法：
既存のワークロードに変更の必要はありません。
もし、より柔軟な認証メカニズムを導入したい場合や、エンドユーザーの権限で直接AI関数を実行したい特定のユースケースがある場合は、[BigQuery AI関数の権限に関するドキュメント](https://cloud.google.com/bigquery/docs/permissions-for-ai-functions)を参照し、この新機能を活用することを検討してください。

用語説明：
*   **`AI.IF`, `AI.SCORE`, `AI.CLASSIFY`**: BigQuery MLによって提供される、Generative AI機能をSQLクエリ内で直接利用するための関数群です。これらを使用することで、大規模言語モデル (LLM) やその他のAIモデルを活用した予測、分類、条件分岐などをBigQuery内で実行できます。
*   **BigQuery Connection**: BigQueryが外部のデータソース（例：Cloud Storage、Cloud SQL）や特定のBIツールなどと連携する際に使用される接続リソースです。通常、この接続にはサービスアカウントが紐付けられており、そのサービスアカウントの権限で操作が実行されます。
*   **End-user credentials**: BigQueryコンソール、bqコマンドラインツール、クライアントライブラリなどを通じてクエリを実行するユーザー自身のGoogleアカウント（またはサービスアカウント）の認証情報を指します。ユーザーがインタラクティブに操作する場合や、ユーザーの権限で実行したい場合に利用されます。

---

### Fixed
原文: Support for table parameters in table-valued functions is restored.
[table parameters in table-valued functions](https://cloud.google.com/bigquery/docs/table-functions#table_parameters)

説明：
BigQueryのテーブル値関数（TVF: Table-Valued Function）において、テーブルパラメータを使用する機能のサポートが復元されました。これは、以前にこの機能が一時的に利用できない、または不安定な状態にあったものが、修正され正常に動作するようになったことを意味します。

影響有無：
**ポジティブな影響**
以前にテーブルパラメータを使用するテーブル値関数で問題が発生していた場合、この修正によって機能が安定し、正常に動作するようになります。既存のワークロードにおいて、この機能に依存するものが安定化されるため、パフォーマンスや信頼性の向上が期待できます。新規にこの機能を利用する場合も、安心して設計・開発を進めることができます。

対処方法：
以前この機能に関連する不具合を経験していた場合、または機能が動作しなかった場合は、関連するクエリやデータパイプラインを再確認し、期待通りに動作するか検証することをお勧めします。
この機能を利用しているBigQuery Composer (Airflow) のDAGなどがある場合は、Airflowの再実行により安定した結果が得られることを確認してください。

用語説明：
*   **Table-Valued Function (TVF)**: BigQueryにおけるユーザー定義関数の一種で、入力としてスカラ値やテーブルを受け取り、結果としてテーブルを返す関数です。これにより、複雑なSQLロジックをモジュール化し、再利用可能な形で定義することができます。
*   **Table Parameters**: テーブル値関数に渡される引数として、テーブルそのものを指定する機能です。これにより、クエリ結果として得られる動的なテーブルデータを関数に渡し、関数内でさらにそのテーブルデータに対する操作を行うことが可能になります。通常のスカラパラメータ（例：整数、文字列）とは異なり、テーブルスキーマを持つデータセットを引数として扱います。