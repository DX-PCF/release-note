
# Title: October 28, 2026 
Link: https://docs.cloud.google.com/release-notes#October_28_2026<br>
Google Cloud のインフラエンジニアとして、AlloyDB for PostgreSQL のリリースノートを調査し、構築済みのサービスへの影響についてご説明します。

---

# AlloyDB for PostgreSQL

## Announcement
### AlloyDB AI & Vector Search features and improvements GA (Part 1)
原文: The following AlloyDB AI and vector search features and improvements are generally available (GA):
- The `alloydb_scann` extension supports four-level tree (4LT) ScaNN vector indexes on PostgreSQL 17 and later, providing support for tables with up to 10 billion vector rows. For more information, see Four-level ScaNN tree indexes.
- 4LT ScaNN vector indexes support automatic index maintenance. For more information, see Create a ScaNN index and Maintain vector indexes automatically.
説明：AlloyDB AI およびベクトル検索機能において、以下の機能がGA（一般提供）されました。
1.  `alloydb_scann`拡張機能が、PostgreSQL 17以降のAlloyDBインスタンスで、4レベルツリー（4LT）ScaNNベクトルインデックスをサポートしました。これにより、最大100億行のベクトルデータを格納するテーブルに対応します。
2.  4LT ScaNNベクトルインデックスの自動メンテナンス機能が利用可能になりました。
影響有無：影響なし。
これは新機能のGAであり、既存のAlloyDBインスタンスの動作に直接的な変更や非互換性はありません。現在の環境がPostgreSQL 17以降でない場合、この機能は利用できません。
対処方法：なし。
AlloyDBで大規模なベクトル検索ワークロードを計画している場合、これらの機能は非常に有用です。特に、大規模なベクトルデータの管理と検索の効率化が期待できます。

用語説明：
*   **ScaNN (Scalable Nearest Neighbors)**: Googleが開発した、大規模なベクトルデータセットから類似するベクトルを高速に検索するためのライブラリ。
*   **ベクトルインデックス**: 機械学習モデルによって生成される「埋め込みベクトル」を効率的に検索するためのデータベースインデックス。
*   **4レベルツリー (4LT)**: ScaNNインデックスの内部構造の一つで、大規模なデータセットに対応するためにインデックスが階層的に構築されることを指します。
*   **GA (General Availability)**: 一般提供。製品や機能が正式にリリースされ、SLA（サービスレベル契約）に準拠した本番環境での利用が推奨される状態。

### AlloyDB AI & Vector Search features and improvements GA (Part 2)
原文: You can enable streaming functionality for ScaNN vector indexes by setting the `scann.satisfy_limit` parameter to `relaxed_order`. When enabled, the vector scan continues searching through additional leaf partitions until it finds enough results to satisfy the `LIMIT` clause of your query, improving recall on filtered searches. Additionally, you can enable this feature for parallel process scans by setting the `scann.enable_parallel_satisfy_limit` database flag to `on`. For more information, see ScaNN index reference and Best practices for tuning ScaNN indexes.
説明：ScaNNベクトルインデックスにおいて、ストリーミング機能がGAとなりました。`scann.satisfy_limit`パラメータを`relaxed_order`に設定することで有効になります。これにより、クエリの`LIMIT`句を満たすのに十分な結果が見つかるまで追加のリーフパーティションを検索し続けることで、フィルタリングされた検索におけるリコール（再現率）を向上させます。また、`scann.enable_parallel_satisfy_limit`データベースフラグを`on`に設定することで、並列プロセススキャンでもこの機能を有効にできます。
影響有無：影響なし。
これは新しいオプションの提供であり、既存のScaNNベクトルインデックスの挙動に自動的な変更はありません。明示的に設定しない限り、既存のワークロードに影響はありません。
対処方法：なし。
既存のベクトル検索ワークロードで、フィルタリングされた検索における再現率の向上を求める場合に、この設定の適用を検討できます。

用語説明：
*   **リコール (Recall)**: 情報検索や機械学習の文脈で用いられる評価指標の一つで、関連するアイテムのうち、システムがどれだけを検出できたかを示す割合。

### AlloyDB AI & Vector Search features and improvements GA (Part 3)
原文: Vector assist simplifies the deployment and management of your AlloyDB vector workloads by helping you set up production-ready vector search capabilities, including embedding generation, query optimization, and index creation for vector types such as Hierarchical Navigable Small World (HNSW). For more information, see Vector assist overview.
説明：Vector assist 機能がGAとなりました。この機能は、埋め込み生成、クエリ最適化、Hierarchical Navigable Small World (HNSW)のようなベクトルタイプのインデックス作成など、本番環境対応のベクトル検索機能を設定することで、AlloyDBのベクトルワークロードのデプロイと管理を簡素化します。
影響有無：影響なし。
これはベクトルワークロードの管理を支援する新しいツール/機能であり、既存のデプロイ済みのAlloyDBインスタンスの動作に直接的な影響はありません。
対処方法：なし。
AlloyDBでベクトル検索機能の導入や管理を検討している場合、Vector assistを利用することで、より効率的にセットアップを進めることができます。

用語説明：
*   **埋め込み (Embedding)**: 単語、画像、その他データを数値のベクトル空間に変換したもの。このベクトル空間では、意味的に近いアイテムが互いに近い位置に配置されます。
*   **HNSW (Hierarchical Navigable Small World)**: 大規模なデータセットで高速な近傍検索を可能にするためのグラフベースのアルゴリズムの一つ。

### AlloyDB AI & Vector Search features and improvements GA (Part 4)
原文: For AlloyDB for PostgreSQL instances running PostgreSQL 17 and later, the maximum supported value for `num_leaves` when building ScaNN vector indexes is increased from 30,000,000 to 104,857,600. For more information, see Create a ScaNN index and ScaNN index reference.
説明：PostgreSQL 17以降のAlloyDB for PostgreSQLインスタンスにおいて、ScaNNベクトルインデックス構築時の`num_leaves`の最大サポート値が、30,000,000から104,857,600に増加しました。
影響有無：影響なし。
これは上限値の緩和であり、既存のScaNNインデックスの動作には影響しません。より大規模なインデックスの構築が可能になったものです。現在のシステムがPostgreSQL 17以降でない場合、この機能強化は適用されません。
対処方法：なし。
より大規模なベクトルインデックスの構築を計画している場合に、この上限緩和を考慮できます。

### AlloyDB AI & Vector Search features and improvements GA (Part 5)
原文: You can use the `external_search_fdw` extension to connect to external search clusters and query their data directly from your database using the following search sources:
- Elasticsearch
- Solr
- OpenSearch
説明：`external_search_fdw`拡張機能がGAとなりました。この機能を使用すると、AlloyDB for PostgreSQLから以下の外部検索クラスターに接続し、そのデータを直接クエリできるようになります。
*   Elasticsearch
*   Solr
*   OpenSearch
影響有無：影響なし。
これは新たな統合機能の提供であり、既存のAlloyDBインスタンスの動作に直接的な変更はありません。
対処方法：なし。
AlloyDBのデータベースから外部の全文検索エンジンに保存されたデータを統合的にクエリしたい場合に、この機能の利用を検討できます。

用語説明：
*   **FDW (Foreign Data Wrapper)**: PostgreSQLの拡張機能の一つで、外部データソース（他のデータベース、ファイル、Webサービスなど）にアクセスし、あたかもローカルテーブルであるかのようにクエリを可能にするインターフェース。

### AlloyDB AI & Vector Search features and improvements GA (Part 6)
原文: AlloyDB supports the `rum` extension for high-performance full-text search operations on PostgreSQL 17 and earlier. The `rum` extension extends standard GIN indexes by storing positional information directly in the index, letting you perform faster phrase searches and relevance ranking without accessing the table data. For more information, see Create and manage a RUM index.
説明：AlloyDBが、PostgreSQL 17およびそれ以前のインスタンスで、高性能な全文検索操作のための`rum`拡張機能をサポートしました。`rum`拡張機能は、標準のGINインデックスを拡張し、位置情報を直接インデックスに格納することで、テーブルデータにアクセスすることなく、より高速なフレーズ検索と関連性ランキングを可能にします。
影響有無：影響なし。
これは新機能の提供であり、既存のAlloyDBインスタンスの動作に直接的な変更はありません。
対処方法：なし。
AlloyDBで既存の全文検索機能を改善したい場合、特にPostgreSQL 17以前のバージョンを利用している場合に、`rum`拡張機能の導入を検討できます。

用語説明：
*   **GIN (Generalized Inverted Index)**: PostgreSQLのインデックスタイプの一つで、複数カラムや配列、JSONデータなど、複雑なデータ型に対する高速な検索を可能にする。全文検索にも利用される。
*   **RUM (Ranked inverted multi-index)**: PostgreSQLのGINインデックスをベースにした拡張機能で、特に全文検索の性能向上を目指したもの。単語の位置情報をインデックス内に保持することで、フレーズ検索や関連性による順位付けを高速化する。

## Fixed
### Improved memory estimation for ScaNN index builds
原文: AlloyDB provides more accurate memory usage estimation and prevents out-of-memory (OOM) errors when you build a ScaNN four-level tree index. This feature is in Preview. This update improves the stability of index builds by enforcing memory limits and improving memory estimation under constrained conditions.
説明：ScaNN 4レベルツリーインデックス構築時において、AlloyDBのメモリ使用量見積もりがより正確になり、メモリ不足（OOM）エラーの発生を防ぐようになりました。この機能はプレビュー段階です。この更新により、メモリ制限を適用し、制約条件下でのメモリ見積もりを改善することで、インデックス構築の安定性が向上します。
影響有無：影響なし（ポジティブな影響）。
これは、ScaNNインデックス構築時の安定性を向上させる修正であり、既存のシステムに悪影響を与えるものではありません。むしろ、将来的にScaNNインデックスを構築する際にOOMエラーのリスクが低減され、安定性が向上します。
対処方法：なし。
本修正はAlloyDB内部で適用されるため、ユーザー側で特別な対応は不要です。

用語説明：
*   **OOM (Out Of Memory)**: メモリ不足。プログラムが利用可能なメモリを使い果たし、これ以上処理を継続できない状態。

## Security
### GCP-2026-071 Update
原文: In response to GCP-2026-071, Google is updating AlloyDB managed components. The fix to the certificate store is shipped in a new maintenance version that AlloyDB applies during scheduled maintenance, so you don't need to manually update AlloyDB managed instances. You can also apply the fix by performing self-service maintenance.
説明：GCP-2026-071に対応するため、GoogleがAlloyDBのマネージドコンポーネントを更新しました。証明書ストアへの修正は新しいメンテナンスバージョンで提供され、AlloyDBはこれを定期メンテナンス中に自動的に適用します。そのため、AlloyDBマネージドインスタンスを手動で更新する必要はありません。セルフサービスメンテナンスを実行することでも、この修正を適用できます。
影響有無：影響なし（自動適用されるため）。
このセキュリティ修正はAlloyDBのマネージドサービス側で自動的に適用されるため、お客様の既存のAlloyDBインスタンスには直接的な作業は発生しません。システムのセキュリティが向上します。
対処方法：なし。
定期メンテナンスのタイミングを待つか、必要に応じてセルフサービスメンテナンスを実行して早期に適用することも可能です。

用語説明：
*   **GCP-2026-071**: Google Cloud Platformにおけるセキュリティ脆弱性識別子。詳細な内容は公開されているセキュリティ速報で確認できます。

### Client-side component updates for security (AlloyDB Auth Proxy)
原文: If you use the AlloyDB Auth Proxy, then upgrade it to v1.17.2 or later. If you run the standalone proxy binary, then also update the host's certificate authority (CA) certificates.
説明：AlloyDB Auth Proxyを使用している場合、バージョンv1.17.2以降にアップグレードしてください。スタンドアロンのプロキシバイナリを実行している場合は、ホストの認証局（CA）証明書も更新してください。
影響有無：あり。
もし現在、AlloyDB Auth Proxyを利用してAlloyDBに接続している場合、セキュリティ強化のため、手動でのアップデートが必要です。特に、AlloyDBへの接続を仲介している環境（例えば、GKE上のアプリケーションやCompute Engine上のVM）でAuth Proxyを使用している場合は影響があります。Composer 2.7.1, Airflow 2.7.3 からAlloyDBに接続する際にAuth Proxyを使用している可能性もあります。
対処方法：
AlloyDB Auth Proxy を利用しているシステム（例: Composer環境内のカスタムコンテナ、AirflowのWorkerがAlloyDBに接続するためのサイドカーなど）において、Auth Proxyのバージョンがv1.17.2未満の場合は、速やかにv1.17.2以降にアップグレードしてください。
スタンドアロンバイナリを使用している場合は、Auth Proxyの更新に加え、ホストOSのCA証明書も最新の状態に保つようにしてください。

用語説明：
*   **AlloyDB Auth Proxy**: AlloyDBへのセキュアな接続を確立するためのツール。IAM認証を利用し、SSL/TLS接続を自動的に処理することで、安全かつ簡素な接続を可能にする。
*   **CA (Certificate Authority) certificates**: 認証局の証明書。通信相手の正当性を検証するために使用される。

### Client-side component updates for security (AlloyDB Language Connectors)
原文: If you use the AlloyDB Language Connectors, then update the language runtime and operating system CA certificates (for example, Go 1.26.10 or 1.27.3 or later).
説明：AlloyDB Language Connectorsを使用している場合、言語ランタイムとオペレーティングシステムの認証局（CA）証明書を更新してください（例: Go 1.26.10または1.27.3以降）。
影響有無：あり。
もし現在、AlloyDB Language Connectorsを利用してAlloyDBに接続している場合、セキュリティ強化のため、Language Connectorsが動作する環境の言語ランタイムやOSのCA証明書の手動での更新が必要です。
対処方法：
AlloyDB Language Connectors を利用しているアプリケーションの実行環境（例: Go言語アプリケーションを実行しているサーバー）において、使用している言語ランタイム（Go、Java、Pythonなど）およびOSのCA証明書を最新の状態に更新してください。推奨バージョンが具体的に示されている場合はそれに従ってください。

用語説明：
*   **AlloyDB Language Connectors**: 各プログラミング言語（Go, Java, Pythonなど）からAlloyDBに接続するためのクライアントライブラリや接続支援機能の総称。

---
# Title: October 27, 2026 
Link: https://docs.cloud.google.com/release-notes#October_27_2026<br>
Google Cloudインフラエンジニアとして、ご提示いただいたリリースノートについて、構築済みのサービスへの影響有無を調査し、以下の通りご報告いたします。

---

# AlloyDB for PostgreSQL

## Announcement
原文: The following AlloyDB AI functions and improvements are available in Preview:

- The `ai.extract` function lets you extract structured data from unstructured text directly within your database queries without needing external extraction pipelines. For more information, see Extract structured data.
- The `ai.classify` function lets you categorize unstructured text into predefined labels directly within your database queries. For more information, see Classify text.
- Parameter names and signatures for AI query engine functions (`ai.analyze_sentiment`, `ai.summarize`, and `ai.agg_summarize`) are updated. For more information, see Model endpoint reference.
    - The `prompt` and `prompts` parameters are renamed to `input` and `inputs` in scalar and batch functions respectively.
    - An optional `additional_instructions` parameter is added to `ai.summarize` and `ai.agg_summarize` to provide custom instructions to guide summary formatting, length, and tone.
    - In cursor-based versions of `ai.analyze_sentiment` and `ai.summarize`, the `prompt` parameter is removed.
    - `ai.agg_summarize` supports multiple positional signatures, including passing optional additional instructions and specifying model IDs.

説明：AlloyDB for PostgreSQLにおいて、AI機能の強化と新機能がプレビュー段階で利用可能になりました。
具体的には、以下の点が挙げられます。
*   非構造化テキストから構造化データを抽出する`ai.extract`関数、およびテキストを事前定義されたラベルに分類する`ai.classify`関数が追加されました。
*   既存のAIクエリエンジン関数（`ai.analyze_sentiment`、`ai.summarize`、`ai.agg_summarize`）のパラメータ名とシグネチャが更新されました。
    *   `prompt`および`prompts`パラメータがそれぞれ`input`および`inputs`に名称変更されました。
    *   `ai.summarize`と`ai.agg_summarize`に、サマリーのフォーマット、長さ、トーンを指示するためのオプションの`additional_instructions`パラメータが追加されました。
    *   カーソルベースの`ai.analyze_sentiment`と`ai.summarize`から`prompt`パラメータが削除されました。
    *   `ai.agg_summarize`が複数の位置シグネチャ（オプションの追加指示やモデルIDの指定を含む）をサポートするようになりました。

影響有無：**既存のAlloyDB AIクエリ機能を利用している場合、影響があります。**
特に、プレビュー段階のAIクエリエンジン既存関数（`ai.analyze_sentiment`, `ai.summarize`, `ai.agg_summarize`）のパラメータが変更されたため、これらの関数を利用している既存のクエリやアプリケーションコードに修正が必要となる可能性があります。新機能（`ai.extract`, `ai.classify`）の追加自体は、既存の利用に直接的な影響はありませんが、新たな機能利用の機会を提供します。プレビュー機能はGA (General Availability) 前に仕様が変更される可能性があるため、常に注意が必要です。

対処方法：
1.  現在、AlloyDB AIクエリエンジン関数を利用しているか確認してください。
2.  利用している場合は、更新されたパラメータ名とシグネチャに合わせて、既存のクエリやアプリケーションコードを修正する必要があります。特に`prompt`から`input`への変更や、カーソルベース関数からのパラメータ削除に注意してください。
3.  プレビュー機能の利用にあたっては、公式ドキュメント（[Extract structured data](https://docs.cloud.google.com/alloydb/docs/ai/extract-structured-data), [Classify text](https://docs.cloud.google.com/alloydb/docs/ai/classify-text), [Model endpoint reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint)）で最新の仕様を確認し、本番環境での利用は慎重に検討してください。

用語説明：
*   **AI関数 (AI Functions)**: データベース内で直接、人工知能や機械学習の機能を利用できるようにする関数群。
*   **プレビュー (Preview)**: Google Cloudのサービスや機能が一般公開される前に、ユーザーに提供される初期段階。この段階の機能は変更される可能性があり、SLA保証がない場合が多いため、本番環境での利用は推奨されない場合があります。
*   **スカラー関数 (Scalar function)**: SQLにおいて、1つの入力値に対して1つの出力値を返す関数。
*   **バッチ関数 (Batch function)**: 複数の入力値に対して、それぞれに対応する複数の出力値を一括で返す関数。
*   **カーソルベースの関数 (Cursor-based function)**: データベースのカーソルを利用して、結果セットを反復処理しながら動作する関数。大量のデータを効率的に処理する場合に用いられます。
*   **モデルエンドポイント参照 (Model endpoint reference)**: AIモデルへのアクセス方法やその機能、パラメータに関する情報を提供する公式ドキュメントやリファレンス。

---

# Cloud DNS

## Announcement
原文: Starting January 5, 2027, CNAME chasing behavior will change so that Cloud DNS follows CNAME chains between public and private zones. If your private zones or response policies have overlapping domain names with public CNAME targets, queries might resolve to unintended internal IP addresses or return resolution errors. ...
説明：2027年1月5日以降、Cloud DNSのCNAMEチェイシング（CNAMEの連鎖解決）の挙動が変更されます。現在の動作では、パブリックゾーンとプライベートゾーン間のCNAMEチェーンは追跡されませんが、変更後はVPCの名前解決順序（応答ポリシー、プライベートゾーン、転送またはピアリングゾーン、内部DNS、パブリックゾーン）に従って、より広範なCNAMEチェーンが追跡されるようになります。
この変更により、プライベートゾーンや応答ポリシーに、パブリックCNAMEターゲットとドメイン名が重複しているレコードがある場合、DNSクエリが意図しない内部IPアドレスに解決されたり、解決エラーが発生したりする可能性があります。

影響有無：**既存のDNS構成、特にパブリックゾーンとプライベートゾーンを組み合わせて使用している環境では、潜在的な影響があります。**
現在の設定でCNAMEの連鎖がパブリックゾーンとプライ
# Title: October 26, 2026 
Link: https://docs.cloud.google.com/release-notes#October_26_2026<br>
各製品・アナウンス単位に、以下の通り回答いたします。

---

# Apigee X

## Security

原文: On October 24, 2026, we published a security bulletin for Apigee.
Two vulnerabilities in PHP core
(CVE-2026-109618
and
CVE-2026-109619,
"PHP2Shell") allow an unauthenticated attacker to execute code remotely on a
server running a vulnerable PHP version. The impact is limited to Drupal-based
Apigee developer portals, which customers deploy and operate. Apigee, Apigee
Hybrid, and the Apigee integrated portal don't use PHP and aren't affected.

[CVE-2026-109618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-109618)
[CVE-2026-109619](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-109619)
**Security bulletin published: GCP-2026-072**

[GCP-2026-072](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-072)

説明：
2026年10月24日にApigeeに関するセキュリティ速報が公開されました。この速報は、PHPのコアにおける2つの脆弱性（CVE-2026-109618およびCVE-2026-109619、通称 "PHP2Shell"）に関するもので、認証されていない攻撃者が脆弱なPHPバージョンを実行しているサーバー上でリモートコード実行を可能にするものです。この脆弱性の影響は、顧客がデプロイおよび運用するDrupalベースのApigeeデベロッパーポータルに限定されます。Apigee本体、Apigee Hybrid、およびApigee統合ポータルはPHPを使用していないため、この脆弱性の影響を受けません。

影響有無：
**影響なし（ただし条件付き）**
現在、当社のサービスでApigee XおよびApigeeのDrupalベースのデベロッパーポータルを運用していないため、直接的な影響はありません。Apigee、Apigee Hybrid、またはApigee統合ポータルを使用している場合でも、それらはPHPを使用していないため影響はありません。

対処方法：
現在、当社がApigee XのDrupalベースのデベロッパーポータルを運用していない限り、特段の対処は不要です。もし将来的にDrupalベースのApigeeデベロッパーポータルを構築・運用する場合には、このセキュリティ情報を参照し、PHPのバージョン管理と脆弱性対応計画に含める必要があります。

用語説明：
*   **CVE (Common Vulnerabilities and Exposures)**: 公開されているソフトウェアの脆弱性および曝露のリストに付けられる識別子。セキュリティ上の問題を一意に特定するために使用されます。
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォーム。APIの設計、開発、公開、運用、監視、分析を可能にします。
*   **Drupal**: PHPで開発されたオープンソースのコンテンツ管理システム（CMS）。多くのウェブサイトやアプリケーションの基盤として利用されています。
*   **デベロッパーポータル (Developer Portal)**: API提供者が、そのAPIを利用する開発者向けに、APIドキュメント、利用規約、FAQなどを提供するウェブサイト。通常、APIキーの管理やアプリケーション登録機能も提供されます。

---

# Compute Engine

## Security

原文: A vulnerability (CVE-2026-85299) about incorrect authorization in
Compute Engine was discovered and has been addressed. For more information,
see the
GCP-2026-073 security bulletin.

[GCP-2026-073 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2026-073)

説明：
Compute Engineにおける誤った認可設定に関する脆弱性（CVE-2026-85299）が発見され、Googleによって既に修正されました。詳細はGCP-2026-073セキュリティ速報を参照してください。

影響有無：
**影響なし**
この脆弱性はGoogle側で既に修正済みであり、「has been addressed」と明記されているため、ユーザー側で直接的な対処は不要です。Google Cloud Composer2はCompute Engine上で動作しますが、基盤側の修正であるため、Composer2への直接的な影響はありません。

対処方法：
Google側で修正が完了しているため、ユーザー側での直接的な対処は不要です。

用語説明：
*   **認可 (Authorization)**: あるユーザーやシステムが、特定のリソースや操作を行う権限を持っているかどうかを判断するプロセス。認証（Authentication）が行われた後に行われます。
*   **Compute Engine**: Google Cloudが提供するIaaS (Infrastructure as a Service) で、仮想マシン（VM）インスタンスを作成および実行できるサービスです。Google Cloud Composer2の基盤としても利用されます。

---

# Google Kubernetes Engine

## Change

原文: GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see GKE versioning and
support and About GKE
cluster upgrades.

[GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning)
[About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades)
## No channel (deprecated)

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.36.4-gke.2046003 is now the default version for cluster creation.
- The following versions are now available:
- 1.34.12-gke.1363000
- 1.35.8-gke.2308000
- 1.36.5-gke.1259000
- 1.37.1-gke.1552000
- 1.37.1-gke.1697000
- 1.37.1-gke.2097000
- The following node versions are now available:
- 1.31.14-gke.3042000
- 1.32.13-gke.2788000
- 1.33.13-gke.2074000
- 1.34.12-gke.1363000
- 1.35.8-gke.2308000
- 1.36.5-gke.1259000
- 1.37.1-gke.1552000
- 1.37.1-gke.1697000
- 1.37.1-gke.2097000
- The following versions are no longer available:
- 1.34.11-gke.1056000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.6-gke.1250000 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.4-gke.1391002 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.4-gke.1495003 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.4-gke.2046002 is deprecated. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.33 to 1.34.12-gke.1011000
- 1.34 to 1.35.8-gke.1439001
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.34 to 1.34.12-gke.1011000
- 1.35 to 1.35.8-gke.1439001
- 1.36 to 1.36.4-gke.2046003
- 1.37 to 1.37.1-gke.1552000

説明：
GKEクラスタのバージョンが更新され、新しいクラスタの作成や既存クラスタのアップグレードに利用可能なバージョンが追加されました。これにはコントロールプレーンとノードのバージョンが含まれます。また、一部の古いバージョン（Deprecatedと表示されたもの）は90日以内にサポート終了となるため、使用しないよう推奨されています。GKEクラスタは、メンテナンス除外期間や非推奨APIの使用などの要因がない場合、新しいマイナーバージョンまたはパッチバージョンに自動アップグレードされます。

影響有無：
**間接的に影響あり（ただし、ユーザーによる直接の対処は不要）**
Google Cloud Composer2 (Compoer version 2.7.1) はGKEクラスタを基盤として動作します。Composerはマネージドサービスであるため、基盤となるGKEのバージョン管理とアップグレードは通常、Google Cloud側で自動的に行われます。今回のGKEバージョン更新は、Composerの基盤の安定性と機能向上が期待できます。
現在Composer2が利用しているGKEバージョンが、今回「no longer available」（利用不可になる）とリストされたバージョンに含まれる可能性は低いですが、ComposerのドキュメントでサポートされているGKEバージョンを確認し、最新の状態を維持することが推奨されます。

対処方法：
ユーザーが利用中のComposer2のGKE基盤はGoogle Cloud側で管理されるため、**ユーザーによる直接的なGKEクラスタのアップグレード操作は不要です。** ComposerのリリースノートやFAQを確認し、ComposerがサポートするGKEバージョンの範囲や、Composerの今後のバージョンアップグレード計画とGKEの関連性について把握しておくことが推奨されます。

用語説明：
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドなKubernetesサービス。コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **GKE Release Channels (リリースチャンネル)**: GKEクラスタのバージョンアップグレード頻度と安定性を選択するための仕組み。`Stable`、`Regular`、`Rapid`、`Extended`などのチャンネルがあり、それぞれに提供されるバージョンと自動アップグレードの挙動が異なります。今回、`No channel (deprecated)`という古い提供形態も記載されています。
*   **コントロールプレーン (Control Plane)**: Kubernetesクラスタの脳のような部分で、APIサーバー、スケジューラー、コントローラーマネージャーなどが含まれます。クラスタの状態を管理し、リソースのデプロイやスケーリングを調整します。
*   **ノード (Node)**: Kubernetesクラスタ内のワーカーマシン。アプリケーションのコンテナを実行する仮想マシンまたは物理マシンです。
*   **自動アップグレード (Auto-upgrade)**: GKEクラスタが自動的に新しいバージョンにアップグレードされる機能。これにより、セキュリティパッチや新機能が適用され、運用負担が軽減されます。
*   **メンテナンス除外期間 (Maintenance Exclusions)**: GKEの自動アップグレードを特定の期間に実施しないように設定する期間。システムの可用性を確保するために使用されます。

---

# Google Kubernetes Engine

## Security

原文: This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

GKE version
Container-Optimized OS version
Details

1.31.14-gke.3042000
cos-121-18867-638-5
cos-121-18867-638-5 release notes

1.32.13-gke.2788000
cos-121-18867-638-5
cos-121-18867-638-5 release notes

1.33.13-gke.2074000
cos-121-18867-638-5
cos-121-18867-638-5 release notes

1.35.8-gke.2308000
cos-125-19216-739-5
cos-125-19216-739-5 release notes

1.37.1-gke.1552000
cos-133-19999-44-85
cos-133-19999-44-85 release notes

1.37.1-gke.2097000
cos-133-19999-44-106
cos-133-19999-44-106 release notes

1.38.0-gke.3229000+preview
cos-133-19999-44-85
cos-133-19999-44-85 release notes

説明：
このGKEリリースには、更新されたContainer-Optimized OS (COS) イメージを使用する新しいGKEバージョンが含まれています。これらのCOSイメージには、前回のGKEリリース以降に公開されたすべてのCOSバージョンからの累積的なセキュリティ修正が含まれています。各COSイメージで解決された特定の脆弱性については、それぞれのリリースノートを参照してください。

影響有無：
**ポジティブな影響あり（ユーザーによる直接の対処は不要）**
Google Cloud Composer2の基盤であるGKEクラスタのノードは、Container-Optimized OSイメージを使用しています。今回の更新により、基盤となるOSのセキュリティが強化され、Composer2を含むワークロードのセキュリティ向上に貢献します。これはサービス全体のセキュリティ体制を強化するポジティブな変更であり、ユーザーによる直接の対処は不要です。

対処方法：
Google Cloud側で基盤のセキュリティ強化が行われるため、ユーザー側での直接的な対処は不要です。

用語説明：
*   **Container-Optimized OS (COS)**: Googleによって最適化された、コンテナの実行に特化したオペレーティングシステム。GKEのノードとして利用され、セキュリティと効率性が強化されています。
*   **累積的なセキュリティ修正 (Cumulative Security Fixes)**: 過去のすべてのセキュリティパッチや修正が含まれている更新。これにより、最新のバージョンに更新するだけで、それまでの全ての既知の脆弱性への対策が適用されます。

---

# Google Kubernetes Engine

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.35.8-gke.1439001 is now the default version for cluster creation in the Stable channel.
- The following versions are now available in the Stable channel:
- 1.34.11-gke.1209000
- 1.35.8-gke.1626001
- The following versions are no longer available in the Stable channel:
- 1.34.11-gke.1056000 is deprecated in the Stable channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.35.6-gke.1250001
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.33 to 1.34.11-gke.1102000
- 1.34 to 1.35.8-gke.1439001
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.34 to 1.34.11-gke.1102000
- 1.35 to 1.35.8-gke.1439001

説明：
GKE Stableチャネルにおいて、クラスタ作成時のデフォルトバージョンが1.35.8-gke.1439001に変更され、新しいバージョンが利用可能になりました。一部の古いバージョンは非推奨となり、90日以内にサポートが終了します。このチャネルのクラスタは、設定に応じて新しいマイナーバージョンまたはパッチバージョンに自動アップグレードされます。

影響有無：
**間接的に影響あり（ただし、ユーザーによる直接の対処は不要）**
Google Cloud Composer2はGKEを基盤としていますが、Composer2自体はマネージドサービスであり、基盤のGKEバージョンはGoogleによって管理されます。Stableチャネルの更新は、Composerが利用するGKE基盤の安定性向上に寄与します。当社のComposer2環境に直接的な影響はありませんが、最新の安定バージョンが提供されることで、Composer2の基盤のセキュリティと機能が継続的に向上します。

対処方法：
Composer2のGKE基盤はGoogle Cloudによって管理されるため、ユーザーによる直接のGKEバージョンアップグレードは不要です。

用語説明：
*   **Stable channel (安定チャネル)**: GKEリリースチャンネルの一つで、安定性を重視し、十分なテスト期間を経たバージョンが提供されます。ビジネスに不可欠なワークロードに適しています。

---

# Google Kubernetes Engine

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.36.4-gke.2046003 is now the default version for cluster creation in the Regular channel.
- The following versions are now available in the Regular channel:
- 1.34.12-gke.1153000
- 1.35.8-gke.1919000
- 1.36.4-gke.2326000
- 1.37.1-gke.1552000
- The following versions are no longer available in the Regular channel:
- 1.34.11-gke.1209000
- 1.35.8-gke.1626001
- 1.36.4-gke.1495002
- 1.36.4-gke.1495003 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
- 1.36.4-gke.2046002 is deprecated in the Regular channel. This version will be removed in 90 days, or at the end of support, if sooner.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.33 to 1.34.12-gke.1011000
- 1.34 to 1.35.8-gke.1796000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.34 to 1.34.12-gke.1011000
- 1.35 to 1.35.8-gke.1796000
- 1.36 to 1.36.4-gke.2046003
- 1.37 to 1.37.1-gke.1552000

説明：
GKE Regularチャネルにおいて、クラスタ作成時のデフォルトバージョンが1.36.4-gke.2046003に変更され、新しいバージョンが利用可能になりました。一部の古いバージョンは非推奨となり、90日以内にサポートが終了します。このチャネルのクラスタは、設定に応じて新しいマイナーバージョンまたはパッチバージョンに自動アップグレードされます。

影響有無：
**間接的に影響あり（ただし、ユーザーによる直接の対処は不要）**
Google Cloud Composer2はGKEを基盤としていますが、Composer2自体はマネージドサービスであり、基盤のGKEバージョンはGoogleによって管理されます。Regularチャネルの更新は、Composerが利用するGKE基盤の安定性向上に寄与します。当社のComposer2環境に直接的な影響はありませんが、最新の安定バージョンが提供されることで、Composer2の基盤のセキュリティと機能が継続的に向上します。

対処方法：
Composer2のGKE基盤はGoogle Cloudによって管理されるため、ユーザーによる直接のGKEバージョンアップグレードは不要です。

用語説明：
*   **Regular channel (標準チャネル)**: GKEリリースチャンネルの一つで、比較的新しい機能と安定性のバランスが取れており、より頻繁なアップデートを受け入れることができるワークロードに適しています。

---

# Google Kubernetes Engine

## Change

原文: **Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.37.1-gke.1697000 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
- 1.34.12-gke.1363000
- 1.35.8-gke.2308000
- 1.36.5-gke.1259000
- 1.37.1-gke.2097000
- Alpha version 1.38.0-gke.3229000+preview is now available for GKE alpha clusters in the Rapid channel.
- The following versions are no longer available in the Rapid channel:
- 1.34.12-gke.1153000
- 1.35.8-gke.1919000
- 1.36.4-gke.2326000
- 1.37.1-gke.1552000
- Alpha version 1.38.0-gke.2240000+preview is no longer available in the Rapid channel.
- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
- 1.33 to 1.34.12-gke.1209000
- 1.34 to 1.35.8-gke.1975000
- 1.35 to 1.36.4-gke.2377000
- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
- 1.34 to 1.34.12-gke.1209000
- 1.35 to 1.35.8-gke.1975000
- 1.36 to 1.36.4-gke.237