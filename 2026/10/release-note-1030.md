
# Title: October 28, 2026 
Link: https://docs.cloud.google.com/release-notes#October_28_2026<br>
AlloyDB for PostgreSQL

## Announcement
原文: The following AlloyDB AI and vector search features and improvements are generally available (GA):
- The `alloydb_scann` extension supports four-level tree (4LT) ScaNN vector indexes on PostgreSQL 17 and later, providing support for tables with up to 10 billion vector rows. For more information, see Four-level ScaNN tree indexes.
- 4LT ScaNN vector indexes support automatic index maintenance. For more information, see Create a ScaNN index and Maintain vector indexes automatically.
- You can enable streaming functionality for ScaNN vector indexes by setting the `scann.satisfy_limit` parameter to `relaxed_order`. When enabled, the vector scan continues searching through additional leaf partitions until it finds enough results to satisfy the `LIMIT` clause of your query, improving recall on filtered searches. Additionally, you can enable this feature for parallel process scans by setting the `scann.enable_parallel_satisfy_limit` database flag to `on`. For more information, see ScaNN index reference and Best practices for tuning ScaNN indexes.
- Vector assist simplifies the deployment and management of your AlloyDB vector workloads by helping you set up production-ready vector search capabilities, including embedding generation, query optimization, and index creation for vector types such as Hierarchical Navigable Small World (HNSW). For more information, see Vector assist overview.
- For AlloyDB for PostgreSQL instances running PostgreSQL 17 and later, the maximum supported value for `num_leaves` when building ScaNN vector indexes is increased from 30,000,000 to 104,857,600. For more information, see Create a ScaNN index and ScaNN index reference.
- You can use the `external_search_fdw` extension to connect to external search clusters and query their data directly from your database using the following search sources:
    - Elasticsearch
    - Solr
    - OpenSearch
- AlloyDB supports the `rum` extension for high-performance full-text search operations on PostgreSQL 17 and earlier. The `rum` extension extends standard GIN indexes by storing positional information directly in the index, letting you perform faster phrase searches and relevance ranking without accessing the table data. For more information, see Create and manage a RUM index.

説明：
AlloyDB AIおよびベクトル検索に関する複数の新機能と改善点がGA（一般提供）になりました。主な内容は以下の通りです。
*   `alloydb_scann` 拡張機能がPostgreSQL 17以降で、最大100億行をサポートする4レベルツリー (4LT) ScaNNベクターインデックスに対応しました。
*   4LT ScaNNベクターインデックスの自動メンテナンス機能がサポートされました。
*   `scann.satisfy_limit` パラメータを `relaxed_order` に設定することで、ScaNNベクターインデックスのストリーミング機能が有効になり、フィルタリングされた検索でのリコールが向上します。並列処理スキャンでも利用可能です。
*   Vector Assistが導入され、AlloyDBにおけるベクトルワークロードのデプロイと管理が簡素化されます。これには、埋め込み生成、クエリ最適化、HNSWなどのベクトルタイプのインデックス作成が含まれます。
*   PostgreSQL 17以降のAlloyDBインスタンスにおいて、ScaNNベクターインデックス構築時の `num_leaves` の最大値が、3千万から約1億4百万に引き上げられました。
*   `external_search_fdw` 拡張機能を使用することで、Elasticsearch、Solr、OpenSearchといった外部検索クラスターにAlloyDBから直接接続し、データをクエリできるようになりました。
*   PostgreSQL 17以前のAlloyDBインスタンス向けに、高性能な全文検索操作のための `rum` 拡張機能がサポートされました。`rum` 拡張機能は、標準のGINインデックスを拡張し、位置情報を直接インデックスに保存することで、テーブルデータにアクセスすることなく、より高速なフレーズ検索や関連性ランキングを可能にします。

影響有無：影響なし
これらの変更は既存機能の動作を変更するものではなく、新たな機能の追加および機能改善であるため、既存のワークロードに直接的な影響はありません。新規にAI/ベクトル検索機能や全文検索機能をAlloyDBに統合したい場合に、選択肢が広がります。特にPostgreSQL 17以降で利用可能な機能が多く、バージョンアップ後にメリットを享受できます。

対処方法：なし
新機能の導入を検討する場合は、公式ドキュメントを参照し、要件に応じて活用してください。

用語説明：
*   **GA (General Availability)**: 一般提供。製品や機能が正式にリリースされ、SLA（サービスレベル契約）に裏付けられた本番環境での利用が推奨される状態です。
*   **ベクトル検索**: データを多次元ベクトルとして表現し、そのベクトル間の距離や類似度に基づいて関連性の高い情報を検索する技術です。セマンティック検索、レコメンデーション、類似画像検索などに利用されます。
*   **ScaNN (Scalable Nearest Neighbors)**: Googleが開発した大規模なベクトルデータセットからの近似最近傍探索（ANN）のためのライブラリです。
*   **4LT (Four-level Tree)**: ScaNNインデックスの内部構造の一つで、非常に大規模なデータセットに対応するために設計された階層的なインデックス構造を指します。
*   **`alloydb_scann` 拡張機能**: AlloyDBでScaNNベクトル検索機能を利用するためのPostgreSQLの拡張機能です。
*   **Vector Assist**: AlloyDBにおけるベクトルワークロードのデプロイ、管理、最適化を支援する機能群です。埋め込み（Embedding）生成、クエリ最適化、インデックス作成などが含まれます。
*   **`num_leaves`**: ScaNNインデックス構築時の重要なパラメータの一つで、インデックスの「葉」の数を指定します。この値が検索の精度と速度に影響を与えます。
*   **`external_search_fdw`**: PostgreSQLのForeign Data Wrapper (外部データラッパー) の一種です。これにより、PostgreSQLから外部のデータソース（この場合は外部検索クラスター）に接続し、あたかもPostgreSQLのテーブルであるかのように外部データをクエリできるようになります。
*   **Elasticsearch, Solr, OpenSearch**: 主に全文検索、ログ分析、データ分析などに用いられる、分散型のオープンソース検索エンジンです。
*   **`rum` 拡張機能**: PostgreSQLの全文検索機能を強化する拡張機能です。標準のGIN (Generalized Inverted Index) インデックスに加えて、インデックスに単語の位置情報なども格納することで、より高速で高精度なフレーズ検索や関連性ランキングを可能にします。

## Fixed
原文: AlloyDB provides more accurate memory usage estimation and prevents out-of-memory (OOM) errors when you build a ScaNN four-level tree index. This feature is in Preview. This update improves the stability of index builds by enforcing memory limits and improving memory estimation under constrained conditions.

説明：
ScaNN 4レベルツリーインデックス構築時のメモリ使用量推定精度が向上し、OutOfMemory (OOM) エラーの発生が防止されるようになりました。この機能は現在プレビュー段階ですが、メモリ制約下でのインデックス構築の安定性が向上します。

影響有無：影響なし（むしろ改善）
これは既存の機能における安定性の改善（バグ修正）であるため、既存のワークロードにマイナスの影響はありません。ScaNN 4LTインデックス構築時にOOMエラーに直面していた場合、その問題が解決され、安定性が向上することが期待されます。

対処方法：なし
ユーザー側での特別な対応は不要です。この改善は、AlloyDBの基盤レベルで行われます。

用語説明：
*   **OOM (Out Of Memory) エラー**: アプリケーションやプロセスがシステムに要求するメモリ量が、利用可能な物理メモリや仮想メモリの量を上回った際に発生するエラーです。
*   **プレビュー (Preview)**: 製品や機能が公開されているが、まだ開発段階にあり、将来的に変更される可能性がある状態を指します。通常、SLAの対象外です。

## Security
原文: In response to GCP-2026-071, Google is updating AlloyDB managed components. The fix to the certificate store is shipped in a new maintenance version that AlloyDB applies during scheduled maintenance, so you don't need to manually update AlloyDB managed instances. You can also apply the fix by performing self-service maintenance.
Depending on how you connect to AlloyDB, take the following actions:
- If you use the AlloyDB Auth Proxy, then upgrade it to v1.17.2 or later. If you run the standalone proxy binary, then also update the host's certificate authority (CA) certificates.
- If you use the AlloyDB Language Connectors, then update the language runtime and operating system CA certificates (for example, Go 1.26.10 or 1.27.3 or later).

説明：
セキュリティ脆弱性「GCP-2026-071」への対応として、AlloyDBのマネージドコンポーネントが更新されます。この証明書ストアの修正は、AlloyDBがスケジュールされたメンテナンス中に自動的に適用する新しいメンテナンスバージョンに含まれるため、AlloyDBマネージドインスタンスの手動更新は不要です。セルフサービスメンテナンスを実行して早期に適用することも可能です。

ただし、AlloyDBへの接続方法によってはユーザー側での対応が必要です。
*   **AlloyDB Auth Proxy を利用している場合**: Auth Proxy を **v1.17.2 以降** にアップグレードする必要があります。スタンドアロンのプロキシバイナリを使用している場合は、ホストのCA証明書も更新してください。
*   **AlloyDB Language Connectors を利用している場合**: 使用している言語ランタイムおよびオペレーティングシステムのCA証明書を更新する必要があります（例: Go 1.26.10 または 1.27.3 以降）。

影響有無：影響あり（AlloyDB Auth Proxy または AlloyDB Language Connectors を利用している場合）
AlloyDBマネージドインスタンス自体は自動で更新されますが、クライアント側でAlloyDB Auth Proxy や AlloyDB Language Connectors を使用している場合、これらのコンポーネントの手動アップグレードまたは関連するCA証明書の更新が必要となります。これらを更新しない場合、AlloyDBへの接続に問題が発生する可能性があります。

対処方法：
*   **AlloyDBマネージドインスタンス**: スケジュールされたメンテナンス中に自動的に修正が適用されるため、ユーザー側での手動操作は不要です。必要に応じて、セルフサービスメンテナンスで早期適用することも可能です。
*   **AlloyDB Auth Proxy を利用している場合**:
    *   Auth Proxy を **v1.17.2 以降** のバージョンにアップグレードしてください。
    *   スタンドアロンのプロキシバイナリを使用している場合は、Auth Proxy を実行しているホストのCA証明書も併せて更新してください。
*   **AlloyDB Language Connectors を利用している場合**:
    *   使用している言語ランタイムおよびオペレーティングシステムのCA証明書を更新してください（例: Go 1.26.10 または 1.27.3 以降へのアップデート）。

用語説明：
*   **GCP-2026-071**: Google Cloud Platform (GCP) において特定されたセキュリティ脆弱性の識別子です。具体的な内容は公式のセキュリティ速報（サポート掲示板）で確認できます。
*   **AlloyDB Auth Proxy**: AlloyDBインスタンスへのセキュアな接続を確立するためのプロキシツールです。認証情報を自動的に管理し、SSL/TLS接続を確立します。
*   **CA (Certificate Authority) 証明書**: 信頼された認証局（CA）によって発行されるデジタル証明書で、Webサイトやソフトウェアの身元を検証するために使用されます。システムのCA証明書を最新に保つことで、安全な通信を確立できます。
*   **AlloyDB Language Connectors**: さまざまなプログラミング言語からAlloyDBに接続するためのGoogleが提供するライブラリやコネクタです。
# Title: October 27, 2026 
Link: https://docs.cloud.google.com/release-notes#October_27_2026<br>
Google Cloudのリリースノートに関する調査結果を製品ごとにご報告いたします。

---

# AlloyDB for PostgreSQL
## Announcement
原文: The following AlloyDB AI functions and improvements are available in Preview:

[Preview](https://cloud.google.com/products#product-launch-stages)
- The `ai.extract` function lets you extract structured data from unstructured text directly within your database queries without needing external extraction pipelines. For more information, see Extract structured data.
- The `ai.classify` function lets you categorize unstructured text into predefined labels directly within your database queries. For more information, see Classify text.
- Parameter names and signatures for AI query engine functions (`ai.analyze_sentiment`, `ai.summarize`, and `ai.agg_summarize`) are updated. For more information, see Model endpoint reference.
- The `prompt` and `prompts` parameters are renamed to `input` and `inputs` in scalar and batch functions respectively.
- An optional `additional_instructions` parameter is added to `ai.summarize` and `ai.agg_summarize` to provide custom instructions to guide summary formatting, length, and tone.
- In cursor-based versions of `ai.analyze_sentiment` and `ai.summarize`, the `prompt` parameter is removed.
- `ai.agg_summarize` supports multiple positional signatures, including passing optional additional instructions and specifying model IDs.

[Extract structured data](https://docs.cloud.google.com/alloydb/docs/ai/extract-structured-data)
[Classify text](https://docs.cloud.google.com/alloydb/docs/ai/classify-text)
[Model endpoint reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint)

説明: AlloyDB for PostgreSQLにおいて、AI機能のプレビュー版が利用可能になったこと、および既存のAIクエリエンジンの関数のパラメータ名やシグネチャが更新されたことがアナウンスされています。具体的には、非構造化テキストから構造化データを抽出する`ai.extract`関数、テキストを事前定義されたラベルに分類する`ai.classify`関数が追加されました。また、`ai.analyze_sentiment`、`ai.summarize`、`ai.agg_summarize`の各関数において、`prompt`/`prompts`パラメータが`input`/`inputs`に名称変更され、`ai.summarize`と`ai.agg_summarize`にはオプションの`additional_instructions`パラメータが追加されました。カーソルベースの`ai.analyze_sentiment`と`ai.summarize`からは`prompt`パラメータが削除され、`ai.agg_summarize`は複数の位置シグネチャをサポートするようになりました。

影響有無: 影響なし。
理由: Google Cloud Composer2の基盤データベースとしては通常AlloyDB for PostgreSQLは使用されません。また、今回のアナウンスはAI機能の追加と既存AI機能のパラメータ変更であり、もしComposer環境内でAlloyDBを利用していたとしても、AI機能を利用していなければ直接的な影響はありません。AI機能を利用している場合でも、今回の変更はプレビュー版の機能追加・変更であるため、現時点での既存運用への影響は少ないと考えられます。

対処方法: なし。
補足: AlloyDB for PostgreSQLをAI機能と連携して利用している場合は、Preview機能の利用状況や、将来的なGA化に伴うAPIの安定化について継続的に情報収集することをお勧めします。

用語説明:
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、PostgreSQLと互換性のあるフルマネージドデータベースサービス。高いパフォーマンスと可用性を特徴とします。
*   **Preview (プレビュー)**: Google Cloudの製品リリースステージの一つ。機能が公開され、一般利用可能になる前の段階であり、機能が変更される可能性や、互換性の保証がされない場合があります。本番環境での利用は推奨されません。
*   **AI Query Engine Functions**: データベース内で直接AIモデルを活用するための関数。これにより、データ抽出、分類、要約、センチメント分析などをSQLクエリを通じて実行できます。
*   **Signature (シグネチャ)**: プログラミングにおける関数やメソッドの名前、パラメータの型と順序、戻り値の型などを定義したもので、関数の呼び出し方法を規定します。

---

# Cloud DNS
## Announcement
原文: Starting January 5, 2027, CNAME chasing behavior will change so that Cloud DNS follows CNAME chains between public and private zones. If your private zones or response policies have overlapping domain names with public CNAME targets, queries might resolve to unintended internal IP addresses or return resolution errors.

| Source of CNAME answer | Current behavior (until January 5, 2027) | New behavior (starting January 5, 2027) |
| --- | --- | --- |
| Cloud DNS public zone | Subsequent queries search only public DNS zones and internal DNS. Private zones, forwarding zones, and response policies are ignored. | Subsequent queries follow the complete VPC name resolution order: response policies, private zones, forwarding or peering zones, internal DNS, and public zones. |
| Cloud DNS private zone | Subsequent queries search only authorized private zones. Public DNS zones are ignored. | Subsequent queries follow the complete VPC name resolution order. If the target isn't found in authorized private zones, Cloud DNS queries public DNS zones. |
| Cloud DNS response policy zone | Cloud DNS systems don't perform queries for CNAME answers received from response policy local data rules. | Subsequent queries follow the complete VPC name resolution order. If the target isn't found in response policies or private zones, Cloud DNS queries public DNS zones. |

Review your CNAME chasing needs before January 5, 2027. Test your DNS query paths using `dig` or `nslookup` to identify CNAME chasing scenarios.
- **Look for private-to-public CNAME chasing scenarios**: Look for CNAME answers from response policies or private zones that don't match any response policy or record in a private zone. Previously, these queries resulted in a `NXDOMAIN` answer but after January 5, 2027, these scenarios might match a record in a public zone or continue to be `NXDOMAIN` responses.
- **Look for public-to-private CNAME chasing scenarios**: Look for CNAME answers from public zones that don't match any record in a public zone. Previously, these CNAME chasing scenarios would have resulted in a `NXDOMAIN` response. After January 5, 2027, these scenarios might match a response policy or record in a private zone or continue to be `NXDOMAIN` responses if the private zone doesn't have the record.
- **For CNAME chasing scenarios under your control**: As best practice, configure matching time-to-live (TTL) values for all records in the CNAME chain.

説明: Cloud DNSのCNAMEチェイシング（CNAMEレコードの連鎖を辿って最終的なA/AAAAレコードを解決する動作）の挙動が2027年1月5日から変更されます。この変更により、パブリックゾーンとプライベートゾーン間でのCNAMEチェイシングが可能になります。もしプライベートゾーンやレスポンスポリシーがパブリックCNAMEターゲットとドメイン名で重複している場合、意図しない内部IPアドレスに解決されたり、解決エラーが発生したりする可能性があります。現行の挙動と新挙動の違いが示されており、2027年1月5日までにDNSクエリパスの確認とテスト、CNAMEチェイシングシナリオの特定、およびCNAMEチェーン内のTTL値の一致設定が推奨されています。

影響有無: 影響あり（将来的な影響）。
理由: Google Cloud Composer2は内部でCloud DNSを利用しており、Airflow DAGsやワーカーが外部リソースや内部リソースにアクセスする際にDNS解決が行われます。この変更は2027年1月5日という将来の日付に適用されますが、現行のDNS設定がパブリックゾーンとプライベートゾーンのCNAMEチェイシングに依存している場合、または将来的にそのような構成を導入する可能性がある場合に影響を受けます。特に、VPC Service Controlsなどのセキュリティ境界を構成している環境では、内部リソースへの予期せぬルーティングが発生するリスクが考えられます。

対処方法:
1.  2027年1月5日までに、現在のCloud DNSの利用状況（特にプライベートゾーン、レスポンスポリシー、パブリックゾーン間のCNAMEレコードの使用状況）を詳細に調査してください。
2.  `dig`や`nslookup`などのツールを使用して、既存のDNSクエリパスをテストし、プライベートとパブリックのCNAMEチェイシングシナリオを特定してください。
3.  特定されたシナリオにおいて、意図しない解決が発生しないか、あるいは解決エラーが発生しないかを検証してください。
4.  必要に応じて、CNAMEレコードの構成を見直すか、CNAMEチェーン内の全レコードでTTL値を一致させるなどの対策を検討してください。

用語説明:
*   **Cloud DNS**: Google Cloudが提供する高性能で可用性の高いDNSサービス。ドメイン名の登録、パブリックDNSゾーンとプライベートDNSゾーンの管理が可能です。
*   **CNAME (Canonical Name) Record**: DNSレコードの一種で、あるドメイン名を別のドメイン名（正規名）の別名として定義します。
*   **CNAME Chasing (CNAMEチェイシング)**: DNSリゾルバがCNAMEレコードを辿って、最終的なAレコード（IPv4アドレス）やAAAAレコード（IPv6アドレス）を見つけるプロセス。
*   **Private Zone (プライベートゾーン)**: VPCネットワーク内でしか解決できないDNSゾーン。内部リソースの名前解決に使用されます。
*   **Public Zone (パブリックゾーン)**: インターネットから解決可能なDNSゾーン。公開リソースの名前解決に使用されます。
*   **Response Policy (レスポンスポリシー)**: Cloud DNSにおいて、特定のドメイン名に対するDNSクエリの挙動をカスタマイズするためのルールセット。特定のIPアドレスへの強制解決や、DNSSECの有効化などが可能です。
*   **VPC Service Controls (VPCサービスコントロール)**: Google Cloudリソースのデータ漏洩を防ぐためのセキュリティ機能。サービス境界を定義し、境界内外でのデータ移動を制限します。

## Announcement
原文: Starting January 5, 2027, Cloud DNS will disable full responses to DNS queries of type `ANY` (`QTYPE=ANY`) in public authoritative zones. Instead, a single resource record will return for `ANY` queries, chosen from the existing resource record sets that match the query.

[public authoritative zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview)
Standard traffic from web browsers, applications, and API traffic query specific record types directly and are therefore unaffected with no action required.

However, certain legacy scripts, automated health checkers, debugging commands (for example, `dig example.com ANY`), or custom third-party monitoring systems that explicitly query `ANY` records will receive the first available record instead of a full zone inventory. You must complete the following configuration updates before January 5, 2027:
- **Identify legacy queries**: Review internal tools, deployment scripts, or third-party DNS monitoring configurations for commands or API calls that request the `ANY` record type. Cloud DNS logs in Cloud Logging can be helpful with this.
- **Transition to specific queries**: Update the tools to query the specific, individual record types they require (for example, querying for `A`, `AAAA`, `MX`, or `TXT` records separately).
- **Retrieve full zone records**: If you use `ANY` queries to retrieve all records in a zone, use the Cloud DNS REST API (`resourceRecordSets.list`), the gcloud CLI (`gcloud dns record-sets list`), or the Google Cloud Console instead.

Risks associated with not making these changes include the following:
- **False monitoring alarms**
- **Broken automation pipelines**
- **Disrupted IT diagnostics**

説明: 2027年1月5日から、Cloud DNSのパブリックオーソリティゾーンにおいて、DNSクエリタイプ`ANY` (`QTYPE=ANY`)に対する完全なレスポンスが廃止されます。今後は、`ANY`クエリに対しては、クエリに一致する既存のリソースレコードセットから選択された単一のレコードのみが返されるようになります。通常のWebブラウザやアプリケーションからのトラフィックは影響を受けませんが、レガシーなスクリプト、自動ヘルスチェッカー、デバッグコマンド（例: `dig example.com ANY`）、カスタム監視システムなどで`ANY`レコードタイプを明示的にクエリしている場合は影響を受けます。2027年1月5日までに、`ANY`クエリを使用しているツールを特定し、必要な特定のレコードタイプを個別にクエリするように移行するか、ゾーンの全レコードを取得する場合はCloud DNS API、gcloud CLI、またはGoogle Cloud Consoleを使用するよう促しています。変更を行わない場合のリスクとして、誤った監視アラーム、自動化パイプラインの破損、IT診断の中断が挙げられています。

影響有無: 影響あり（将来的な影響）。
理由: Google Cloud Composer2の運用において、Airflow DAGs、カスタムスクリプト、監視システム、またはデバッグ手順でCloud DNSのパブリックゾーンに対して`ANY`クエリを使用している場合、2027年1月5日以降に意図しない挙動が発生する可能性があります。例えば、Airflowのジョブが外部サービスの健全性チェックのために`ANY`クエリを使っている場合、誤った結果を返す可能性があります。

対処方法:
1.  2027年1月5日までに、Google Cloud Composer環境で利用しているカスタムスクリプト、監視システム、CI/CDパイプライン、デバッグ手順などにおいて、Cloud DNSのパブリックオーソリティゾーンに対する`ANY`クエリの使用状況を調査してください。Cloud LoggingのCloud DNSログを活用することで、`ANY`クエリを発行しているクライアントを特定できる可能性があります。
2.  `ANY`クエリを使用している箇所が見つかった場合、必要なレコードタイプ（例: `A`, `AAAA`, `MX`, `TXT`など）を個別にクエリするようにコードや設定を修正してください。
3.  ゾーンの全レコードを取得する必要がある場合は、Cloud DNS REST APIの`resourceRecordSets.list`メソッド、`gcloud dns record-sets list`コマンド、またはGoogle Cloud Consoleを使用するように移行してください。
4.  変更後の挙動をテストし、本番環境への影響がないことを確認してください。

用語説明:
*   **QTYPE=ANY**: DNSクエリのタイプの一つで、指定されたドメイン名に対するすべてのレコードタイプ（A, AAAA, MX, TXTなど）を返すようにリゾルバに要求します。
*   **Public Authoritative Zone (パブリックオーソリティゾーン)**: 特定のドメイン名に対する権限を持つパブリ
# Title: October 26, 2026 
Link: https://docs.cloud.google.com/release-notes#October_26_2026<br>
以下は、提供されたリリースノートに対する製品ごとの影響調査結果です。

---

# Apigee X

## Security
原文: On October 24, 2026, we published a security bulletin for Apigee. Two vulnerabilities in PHP core (CVE-2026-109618 and CVE-2026-109619, "PHP2Shell") allow an unauthenticated attacker to execute code remotely on a server running a vulnerable PHP version. The impact is limited to Drupal-based Apigee developer portals, which customers deploy and operate. Apigee, Apigee Hybrid, and the Apigee integrated portal don't use PHP and aren't affected.
[CVE-2026-109618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-109618)
[CVE-2026-109619](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-109619)
Security bulletin published: GCP-2026-072
[GCP-2026-072](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-072)

説明: Apigeeに関するセキュリティ速報で、PHPの2つの脆弱性(CVE-2026-109618, CVE-2026-109619)が発表されました。これらの脆弱性は「PHP2Shell」と呼ばれ、認証されていない攻撃者が脆弱なPHPバージョンを実行しているサーバー上でリモートからコードを実行できる可能性があります。この影響は、お客様が独自にデプロイ・運用しているDrupalベースのApigee開発者ポータルに限定されます。Apigee、Apigee Hybrid、およびApigee統合ポータルはPHPを使用していないため、この脆弱性の影響を受けません。

影響有無:
**影響あり（条件付き）**: お客様が独自にデプロイ・運用しているDrupalベースのApigee開発者ポータルを使用している場合は影響があります。これは、DrupalがPHPを利用しているためです。
**影響なし（ほとんどの場合）**: Apigee本体、Apigee Hybrid、またはGoogleが管理するApigee統合ポータルを利用している場合は影響ありません。これらはPHPを使用していません。

対処方法:
お客様がDrupalベースのApigee開発者ポータルを運用している場合、速やかに当該PHPの脆弱性に対するパッチ適用やバージョンアップを検討してください。詳細はセキュリティ速報GCP-2026-072を確認し、DrupalおよびPHPのセキュリティアップデートを適用してください。

用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアの脆弱性に割り当てられる識別子。
*   **PHP**: ウェブ開発で広く使われるスクリプト言語。
*   **Drupal**: PHPで書かれたオープンソースのコンテンツ管理システム (CMS)。
*   **Apigee Developer Portal**: APIの利用者がAPIドキュメントの参照やAPIキーの管理を行うためのポータルサイト。

---

# Compute Engine

## Security
原文: A vulnerability (CVE-2026-85299) about incorrect authorization in Compute Engine was discovered and has been addressed. For more information, see the GCP-2026-073 security bulletin.
[GCP-2026-073 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-073)

説明: Compute Engineにおける不適切な認証に関する脆弱性(CVE-2026-85299)が発見され、Googleによって既に対処済みです。詳細はセキュリティ速報GCP-2026-073を参照してください。

影響有無:
**影響なし**: この脆弱性はGoogleによって既に修正済みであり、お客様側での直接的な緊急対応は不要です。Google Cloud Composer2はCompute Engine上に構築されますが、基盤の脆弱性はGoogleによって管理・修正されています。

対処方法:
お客様側で特に必要な対応はありません。Google Cloudのインフラストラクチャレベルで修正が完了しています。

用語説明:
*   **Compute Engine**: Google Cloudが提供する、仮想マシンを実行するためのインフラストラクチャサービス。

---

# Google Kubernetes Engine

## Change / Security (統合的な評価)

GKEのリリースノートは複数の変更点とセキュリティアップデートを報告しています。Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) は内部でGKEを利用していますが、GKEのバージョン管理はComposerサービスによって抽象化されています。したがって、GKEのバージョンアップデートは直接お客様が操作するものではなく、Composerのアップデートサイクルに組み込まれます。

### 全体的な説明:
Google Kubernetes Engine (GKE) の各リリースチャネル（No channel (非推奨), Stable, Regular, Rapid, Extended）において、クラスターのバージョンが更新されました。これには、新しいデフォルトバージョン、利用可能になった新バージョン、非推奨となったバージョンが含まれます。また、GKEの自動アップグレードターゲットも更新されています。特に、セキュリティの項目では、更新されたContainer-Optimized OS (COS) イメージに累積的なセキュリティ修正が含まれていることが強調されています。

### 影響有無:
**影響なし（直接的な操作は不要）**: Google Cloud Composer2はGKEを基盤として利用していますが、GKEのバージョン管理はComposerサービスが自動的に行います。お客様が直接GKEクラスターのバージョンアップを行う必要はありません。このリリースノートに記載されているGKEバージョン（1.3x系）は、現在のComposer 2.7.1が利用しているGKEバージョン（通常は1.2x系）よりも新しいもののため、既存のComposer環境にすぐに直接的な影響はありません。Composerの将来のバージョンアップ時に、これらの新しいGKEバージョンが基盤として採用される可能性があります。セキュリティ修正がCOSイメージに組み込まれることで、基盤のセキュリティは向上します。

### 対処方法:
お客様側で直接的な対応は不要です。

*   **継続的な情報収集**: 将来的にComposerサービス自体が基盤GKEバージョンを更新する可能性があるため、Composerのリリースノートも継続的に確認し、新しいGKEバージョンへの移行がComposerの動作に影響を与える可能性がないか確認することをお勧めします。
*   **GKE Auto-Upgradeの理解**: Composer環境のGKEクラスターは自動アップグレードの対象となります。これらのリリースノートは、どのようなバージョンへ自動アップグレードが行われるかの参考情報となります。メンテナンス期間の設定などを確認してください。

### 用語説明:
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するマネージドなKubernetesサービス。
*   **GKE Release Channels**: GKEクラスターのバージョン管理戦略。提供されるKubernetesバージョンの安定性、新機能の導入速度、サポート期間が異なる。
    *   **No channel (deprecated)**: 特定のチャネルに属さない、非推奨のバージョン提供方法。
    *   **Stable channel**: 安定性が重視され、長期的な安定稼働に適している。
    *   **Regular channel**: StableとRapidの中間のバランスを持つチャネル。
    *   **Rapid channel**: 最新のKubernetesバージョンが最も早く提供される。
    *   **Extended channel**: 特定のKubernetesバージョンを長期サポートするチャネル。
*   **Container-Optimized OS (COS)**: Google Compute Engine仮想マシン向けの、コンテナ実行に最適化されたOSイメージ。セキュリティと管理の容易さが特徴。
*   **Google Cloud Composer2**: Google Cloudが提供するフルマネージドなApache Airflowサービス。内部でGKEクラスターを利用してAirflowワーカーなどを実行する。Composerのバージョンアップに伴い、基盤となるGKEのバージョンもGoogleによって管理・更新される。