
# Title: September 10, 2026 
Link: https://docs.cloud.google.com/release-notes#September_10_2026<br>
Google Cloudのリリースノートに関するお問い合わせ、ありがとうございます。
以下に、各製品のリリースノートについて、影響調査と対応策をまとめました。

---

# Apigee X
## Fixed
原文: Addendum to Apigee release notes dated August 27, 2026 (1-18-0-apigee-4).

August 27, 2026
| Bug ID | Description |
| --- | --- |
| **502540992** | Fixed an issue where the SemanticCacheLookup policy was incompatible with Vertex AI Vector Search Private Service Connect (PSC) endpoints. |

説明：
Apigee Xにおいて、`SemanticCacheLookup`ポリシーがVertex AI Vector SearchのPrivate Service Connect (PSC) エンドポイントと互換性がなかった問題（バグID: 502540992）が修正されました。この修正は、2026年8月27日付けのApigeeリリースノートの追記として公開されています。

影響有無：
**影響なし（ポジティブな影響）**

この変更は「Fixed（修正済み）」であるため、既存のサービスに負の影響を与えるものではなく、潜在的な問題が解決されたことを意味します。
もしお客様の環境でこれまで`SemanticCacheLookup`ポリシーをVertex AI Vector Search PSCエンドポイントと組み合わせて利用しており、互換性の問題に直面していた場合、この修正により問題が解消され、正常に機能するようになります。この構成を利用していなかった場合でも、将来的な利用の際に問題が発生するリスクが低減されます。

対処方法：
お客様側で特に対処は不要です。この修正はサービス側で適用されます。
もし過去にこの互換性の問題により機能利用を断念していた場合は、改めて`SemanticCacheLookup`ポリシーとVertex AI Vector Search PSCエンドポイントの連携をご検討いただけます。

用語説明：
*   **Apigee X**: Google Cloudが提供するフルマネージド型のAPI管理プラットフォームです。APIの設計、デプロイ、セキュリティ保護、監視、分析などを一元的に行い、APIエコシステムの管理を効率化します。
*   **SemanticCacheLookup policy**: Apigeeが提供するポリシーの一つで、APIプロキシがバックエンドサービスを呼び出す前に、キャッシュから意味的に関連性の高い情報を検索し、利用することでAPIのパフォーマンスを向上させるために使用されます。
*   **Vertex AI Vector Search**: Google Cloudの機械学習プラットフォームであるVertex AIの一部として提供されるベクトル検索サービスです。大量のベクトルデータを高速かつ高精度に検索し、類似性に基づいて結果を返すことができます。以前はMatching Engineという名称でした。
*   **Private Service Connect (PSC)**: Google CloudのVPCネットワークからGoogleのマネージドサービス（または他のVPC）へ、インターネットを経由せずにプライベートIPアドレスのみで安全に接続するためのネットワークサービスです。セキュリティとネットワークパフォーマンスの向上に貢献します。

---

# Cloud SQL for PostgreSQL
## Breaking
原文: Appending `sqlcommenter` tags using the `sql_commenter_enabled` parameter when executing SQL queries on a Cloud SQL remote MCP server is temporarily disabled.

For more information, see [sqlcommenter tags](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp#sqlcommenter).

説明：
Cloud SQL for PostgreSQLにおいて、`sql_commenter_enabled`パラメータを有効にしてSQLクエリを実行する際に、`sqlcommenter`タグがCloud SQLリモートMCPサーバーに付与される機能が一時的に無効化されました。

影響有無：
**影響あり（特定の利用ケース）**

この変更は「Breaking（互換性を損なう変更）」として分類されており、お客様の環境で以下の条件をすべて満たす場合に影響があります。
1.  Cloud SQL for PostgreSQL を利用している。
2.  `sql_commenter_enabled`パラメータを有効にしている。
3.  Cloud SQLリモートMCPサーバーに対してSQLクエリを実行している。
4.  `sqlcommenter`タグによって付与される情報（アプリケーション名、トレースIDなど）に依存する監視、ログ収集、または分析を行っている。

上記に該当する場合、`sqlcommenter`タグが一時的に付与されなくなるため、これに依存するシステムが正しく動作しなくなる可能性があります。`sqlcommenter`機能自体を利用していない場合、またはリモートMCPサーバー以外の環境での利用の場合は影響ありません。

対処方法：
*   お客様のCloud SQL for PostgreSQL環境で`sql_commenter_enabled`パラメータが有効になっており、かつCloud SQLリモートMCPサーバーとの連携を行っている場合は、影響の範囲を評価してください。
*   `sqlcommenter`タグのデータに依存している監視、ロギング、トレーシングシステムがある場合、一時的にこれらのデータの収集ができなくなるか、精度が低下する可能性があります。この期間におけるデータ欠損を許容できるか、または代替手段の検討が必要かを確認してください。
*   本機能は「一時的に無効化」とされているため、将来的に再開される可能性があります。Google Cloudの公式アナウンスやCloud SQLのリリースノートを継続的に監視し、機能再開の情報を確認してください。
*   現時点では、この機能が利用できないことによるエラーが発生するのか、単にタグが付与されないだけなのかはリリースノートからは明確ではありませんが、後者の可能性が高いです。

用語説明：
*   **Cloud SQL for PostgreSQL**: Google Cloudが提供するフルマネージド型のリレーショナルデータベースサービスで、PostgreSQLデータベースエンジンを実行します。インフラ管理なしでPostgreSQLを利用できます。
*   **`sqlcommenter`**: オープンソースのライブラリおよび仕様であり、アプリケーションがデータベースに送信するSQLクエリに、フレームワーク、コントローラ、アクション、トレースIDなどのコンテキスト情報をコメントとして自動的に追加するものです。これにより、データベースのパフォーマンス分析やトラブルシューティング、オブザーバビリティが向上します。
*   **`sql_commenter_enabled` parameter**: Cloud SQL for PostgreSQLのインスタンス設定パラメータの一つで、`sqlcommenter`機能の有効/無効を制御するために使用されます。
*   **Cloud SQL remote MCP server**: ここでの "MCP" はMulti-Cloud Platformを指すと考えられます。Cloud SQLインスタンスが、Google Cloud以外のプラットフォーム（他のクラウドプロバイダなど）上に存在するサーバーと連携する特定の構成やユースケースを指している可能性があります。詳細については、提供されたドキュメントリンク（`sqlcommenter tags`）をご参照ください。