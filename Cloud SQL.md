# 14.19
Tighten security checks in planner estimation functions (Dean Rasheed) §

The fix for CVE-2017-7484, plus followup fixes, intended to prevent leaky functions from being applied to statistics data for columns that the calling user does not have permission to read. Two gaps in that protection have been found. One gap applies to partitioning and inheritance hierarchies where RLS policies on the tables should restrict access to statistics data, but did not.

The other gap applies to cases where the query accesses a table via a view, and the view owner has permissions to read the underlying table but the calling user does not have permissions on the view. The view owner's permissions satisfied the security checks, and the leaky function would get applied to the underlying table's statistics before we check the calling user's permissions on the view. This has been fixed by making security checks on views occur at the start of planning. That might cause permissions failures to occur earlier than before.

The PostgreSQL Project thanks Dean Rasheed for reporting this problem. (CVE-2025-8713)


**Translating the Details**

I'm currently translating the PostgreSQL release notes, specifically focusing on CVE-2025-8713. My approach is to render the original English text into precise Japanese, breaking it down section by section for clarity. I'm meticulously working to maintain the original meaning.


**Defining the Scope**

I'm now focusing on identifying the core elements of the vulnerability description. It appears to involve security checks in planner estimation functions and gaps related to RLS policies within partitioning, inheritance, and views. My task is to precisely capture the nuances of these technical concepts in Japanese.


**Dissecting the Problem**

Now, I'm focusing on how the vulnerability works and how to best explain it. The core issue involves weaknesses in security checks within PostgreSQL. Specifically, there are two gaps: one relates to partition and inheritance hierarchies with RLS policies, and another to access through views. I'm outlining the steps involved in the attack, and how the fix prevents information leaks.


**Summarizing the Vulnerability**

I'm now outlining the impact analysis in Japanese, considering the users' perspectives. I'm currently highlighting those affected by the vulnerability, focusing on those with RLS and view access with differing permission levels. My aim is to provide a clear explanation of potential information leakage and the circumstances under which it can occur, along with an assessment of the potential damage.


**Interpreting the Request**

I'm now evaluating the user's prompt. The task involves translating the PostgreSQL release notes for CVE-2025-8713 into Japanese. Additionally, I need to create a comment outlining the potential impact, considering how it affects different user setups and emphasizing the perspective of a Google Cloud infrastructure engineer.


**Constructing the Response**

I'm now preparing the final response. I'll structure it by providing a Japanese translation of the release notes, followed by an impact assessment. The assessment will cover the vulnerability's potential consequences and specifically address the needs of a Google Cloud infrastructure engineer, ensuring clarity and actionable advice.


**Crafting the Translation**

I'm now refining the Japanese translation, organizing it in a structured manner to mirror the original English text. The bullet points are in place, with the Google search code in mind, and the impact comment is ready for polishing.


承知いたしました。ご指定のリリースノートの内容について、日本語訳とGoogle Cloud上のインフラエンジニアとしての影響有無に関するコメントを以下に記載します。

---

### 日本語訳

**プランナーの推定関数におけるセキュリティチェックを強化 (Dean Rasheed)** §

CVE-2017-7484に対する修正およびその後の修正は、呼び出し元のユーザーが読み取り権限を持たない列の統計情報に対して、情報漏洩の可能性がある関数（leaky functions）が適用されるのを防ぐことを意図していました。その保護には2つの抜け穴が見つかりました。

1.  1つ目の抜け穴は、パーティショニングと継承階層に適用されます。この構成では、テーブルのRLS（行レベルセキュリティ）ポリシーが統計情報へのアクセスを制限すべきであるにもかかわらず、そうなっていませんでした。

2.  もう1つの抜け穴は、クエリがビューを介してテーブルにアクセスし、ビューの所有者は基になるテーブルを読み取る権限を持っているが、呼び出し元のユーザーはビューに対する権限を持っていない場合に適用されます。この場合、ビュー所有者の権限でセキュリティチェックが通過してしまい、呼び出し元のユーザーのビューに対する権限をチェックする前に、情報漏洩の可能性がある関数が基になるテーブルの統計情報に適用されてしまいました。

この問題は、ビューに対するセキュリティチェックをプランニングの開始時に行うようにすることで修正されました。これにより、以前よりも早い段階で権限エラーが発生する可能性があります。

PostgreSQLプロジェクトは、この問題を報告したDean Rasheed氏に感謝します。(CVE-2025-8713)

---

### 影響有無とコメント

**影響有無：あり（重大）**

#### コメント

これは **CVE-2025-8713** として追跡されている**重大なセキュリティ脆弱性**の修正です。 Google Cloud上でPostgreSQLを運用するインフラエンジニアとして、速やかな内容の理解と対応が求められます。

*   **脆弱性の内容**:
    権限のないユーザーが、特定の巧妙なクエリを実行することで、本来アクセスできないはずのテーブルの**統計情報（データの分布、ヒストグラム、最頻値など）を推測できる**という情報漏洩の脆弱性です。 直接的にテーブルの行データが抜き取られるわけではありませんが、データの傾向が漏洩することは重大なセキュリティリスクです。

*   **影響を受ける環境**:
    特に以下の機能を利用している環境でリスクが高まります。
    1.  **行レベルセキュリティ (RLS)** を利用して、ユーザーごとにアクセスできる行を制限している環境。
    2.  テーブルに対する直接の権限を持たないユーザーに、**ビュー**を介してデータへのアクセスを許可している環境。

*   **インフラエンジニアとしての対応**:
    1.  **アップデートの適用**: この脆弱性は14.19で修正されています。 Cloud SQL for PostgreSQLを利用している場合、メンテナンスウィンドウなどを利用して、速やかにこの修正が含まれたバージョンへアップデートすることを強く推奨します。Compute Engine上のセルフマネージド環境でも同様にアップデートが必要です。
    2.  **動作変更の認識**: この修正により、これまで実行できていたクエリが、プランニングの早い段階で「権限エラー」として失敗する可能性があります。これは脆弱性を塞ぐための正しい挙動への変更ですが、アプリケーションの挙動に変化がないか、ステージング環境などで事前にテストすることが望ましいです。
    3.  **リスクの認識**: RLSやビューによる権限管理は、マルチテナントのサービスなど、堅牢なデータ分離が求められるシステムで多用されます。この脆弱性はそうしたシステムの根幹を揺るがす可能性があるため、セキュリティインシデントとして扱い、迅速に対応計画を立てるべきです。

==================================================
**Initiating the Analysis**

I'm starting to break down the user's request. First, I'm focusing on what the user actually needs: a Japanese translation and an impact analysis. I'm thinking through the specifics of the PostgreSQL release notes, particularly the security fix section related to `pg_dump` and `psql`, to understand the context.


**Deconstructing the Problem**

I'm now focusing on the attack vector. The core issue is malicious code injected into the `pg_dump` output. This code, disguised as data, gets executed by `psql` during the restore process. I'm outlining the attack's mechanics, emphasizing the importance of the OS user's privileges. The goal is to understand what triggers the exploit and the implications.


**Unpacking the Details**

I'm now refining the translation and expanding the impact analysis. I've identified the core elements of the security issue: the `pg_dump` output vulnerability, the `psql` meta-command exploit, and the privilege escalation risk. The translation is progressing. I'm formulating the analysis from a Google Cloud infrastructure perspective, considering the implications within managed database services.


**Finalizing the Translation**

I've refined the Japanese translation, aiming for natural phrasing, especially in more complex sentences. I've focused on accurately conveying the technical details and the potential attack scenarios. I'm satisfied with the accuracy and clarity of the translation. Now I will work on the final impact analysis.


**Refining the Analysis**

I'm now focusing on the specifics of Google Cloud's PostgreSQL offerings. The impact assessment requires a deep understanding of how Cloud SQL, for example, manages backups, restores, and user privileges. This includes how they handle `pg_dump` and `psql` operations in the background, and what level of control the customer has.


**Impact Assessment Deep Dive**

I'm now diving deep into the specifics of Google Cloud's PostgreSQL offering, particularly Cloud SQL. I'm focusing on the backup and restore mechanisms, examining how `pg_dump` and `psql` are used internally. I must know exactly what privileges a customer has, and what Google handles in the background, to properly assess the risk profile within this infrastructure.


**Impact Analysis Focus**

I'm now turning to the impact analysis, specifically within the context of Google Cloud's PostgreSQL services. I am evaluating the potential risks associated with this vulnerability for customers using Cloud SQL, examining how their backups and restores are handled and the level of control they have. Also looking at the mitigation strategies Google can provide to its users.


**Assessing Cloud SQL Impact**

I'm now thinking about the Google Cloud SQL impact. The main point: Cloud SQL users are potentially vulnerable during database restores, especially if their backups are taken from untrusted sources. The risk stems from the possibility of malicious code execution via the `psql` client during the restore process, hence,  updates are critical.


**Prioritizing Google Cloud Concerns**

I'm now focusing on refining the impact assessment within the Google Cloud ecosystem. I'm weighing the specific risks for Cloud SQL users, considering various operational scenarios, and thinking through the required security measures. My aim is to provide clear and actionable guidance for Google Cloud users.


承知いたしました。ご指定のリリースノートの内容について、日本語訳とGoogle Cloud上のインフラエンジニアとしての影響有無に関するコメントを以下に記載します。

---

### 日本語訳

**`pg_dump`スクリプトがリストアを実行するユーザーを攻撃するために使用されるのを防ぐ (Nathan Bossart)** § §

ダンプ/リストア操作は通常、スーパーユーザーとしてSQLコマンドを実行するため、ターゲットのデータベースインスタンスはソースサーバーを信頼する必要があります。しかしだからと言って、リストアのために`psql`を実行するオペレーティングシステムユーザーまでがソースサーバーを信頼しなければならないということにはなりません。

ここでのリスクは、ソースサーバー上でスーパーユーザーレベルの制御権を得た攻撃者が、`psql`のメタコマンドとして解釈されるようなテキストを（訳注: データやオブジェクト名に仕込み）`pg_dump`に出力させることが可能になる点です。これにより、ターゲットデータベースへのアクセスとは無関係に、**リストアを実行しているユーザー自身のOSアカウントへのシェルレベルのアクセス**が可能になってしまいます。

これが起こり得ないことを確実に保証するため、`psql`に以降のメタコマンドの実行を禁止する `\restrict` コマンドを追加し、`pg_dump`がソースサーバーからのデータをダンプする前にこのコマンドを出力するようにしました。

PostgreSQLプロジェクトは、この問題を報告したMartin Rakhmanov氏、Matthieu Denais氏、RyotaK氏に感謝します。(CVE-2025-8714)

---

### 影響有無とコメント

**影響有無：あり（極めて重大）**

#### コメント

これは **CVE-2025-8714** として追跡されている、**リモートコード実行（RCE）につながる可能性のある極めて重大なセキュリティ脆弱性**の修正です。すべてのPostgreSQL運用担当者は、この問題を最優先で認識し、対応する必要があります。

*   **脆弱性の内容**:
    この脆弱性はデータベースサーバー自体ではなく、**`pg_dump` と `psql` というクライアントツール**の組み合わせに存在します。攻撃者が侵害済みのDBサーバー（ソース）に悪意のあるデータ（例: `\n\! rm -rf ~` のような文字列を含むテーブル名）を仕込むと、管理者がそのDBから`pg_dump`で作成したダンプファイルを`psql`でリストアする際に、`psql`がその悪意のある文字列を「メタコマンド」として解釈・実行してしまいます。結果として、**リストアを実行した管理者やCI/CDパイプラインのOSユーザー権限で、任意のシェルコマンドが実行されてしまいます**。

*   **Google Cloud環境でのシナリオ**:
    1.  **Cloud SQLへのインポート**: 開発環境や信頼できないソースから提供されたダンプファイルを、Compute Engine VMやCloud Shell上の`psql`を使ってCloud SQLインスタンスにインポートする際に、VMやCloud Shellが乗っ取られる危険性があります。
    2.  **PostgreSQL on GCE**: GCE上でセルフマネージドしているPostgreSQLのバックアップ・リストア運用は、この攻撃の典型的な対象です。日次のリストアテストなどを自動化している場合、サービスアカウントの権限で意図しないコマンドが実行されるリスクがあります。
    3.  **開発者のローカルPC**: 開発者が自身のPC上の`psql`を使い、本番DBのダンプをリストアして調査を行うようなケースも危険です。本番DBが万が一侵害されていた場合、開発者のPCが攻撃の標的となります。

*   **インフラエンジニアとしての対応**:
    1.  **クライアントツールの即時アップデート**: この脆弱性から保護するためには、**`pg_dump`と`psql`の両方を、この修正が含まれたバージョン（14.19以降）にアップデートする**ことが不可欠です。新しい`pg_dump`が保護コマンド (`\restrict`) を出力し、新しい`psql`がそれを解釈してメタコマンドを無効化するため、片方だけのアップデートでは不十分です。
    2.  **影響範囲の確認**: データベースサーバーだけでなく、`psql`や`pg_dump`がインストールされているすべての環境（**Compute Engine VM、踏み台サーバー、CI/CD実行環境、管理者のPCなど**）がアップデートの対象となります。
    3.  **運用手順の見直し**: アップデートが即時適用できない場合、信頼できないソースからのダンプファイルを`psql`で直接リストアする行為は絶対に避けるべきです。しかし、根本的な解決策はツールのアップデート以外にありません。

この脆弱性は、DBAやインフラエンジニアの日常的な信頼された運用プロセスを逆手に取った非常に危険なものであるため、最優先での対応を強く推奨します。

===============================
**Interpreting PostgreSQL Notes**

I'm working on translating the PostgreSQL release notes, specifically focusing on CVE-2025-8715. The initial focus is on accurately rendering the text regarding `pg_dump`'s output, including the crucial point about newline characters. This translation is to be in Japanese, with the goal of clarity and precision.


**Clarifying Vulnerability Details**

I've now translated the specific text excerpts related to CVE-2025-8715. The focus has been on rendering the information clearly in Japanese, maintaining accuracy regarding the newline vulnerability within `pg_dump`'s output. I've also incorporated supplementary notes to clarify technical aspects.


**Translating and Analyzing**

I've completed the Japanese translation of the PostgreSQL release notes related to CVE-2025-8715, focusing on `pg_dump` and the newline vulnerability. Now, I'm drafting the "impact" and "commentary" sections. This involves characterizing the SQL injection type and outlining the attack vector, including the role of newline characters and how attackers could exploit the vulnerability through malformed database object names to inject commands into `pg_dump`'s output.


**Summarizing the SQL Injection**

I've completed the Japanese translation of the provided PostgreSQL release notes excerpts concerning the `pg_dump` newline vulnerability (CVE-2025-8715). My focus now centers on crafting an "impact" and "commentary" section for the report. I'm detailing how attackers can exploit the newline vulnerability through malicious database object names to inject commands into `pg_dump`'s output, thereby achieving SQL injection, including the role of the newline characters and the potential consequences of this vulnerability. I am particularly noting how this is different from CVE-2025-8714.


**Analyzing the Japanese Translations**

I've translated the PostgreSQL release notes into Japanese, including all the critical sections. Now, I'm carefully constructing the "impact" and "commentary" portions. This includes pinpointing the vulnerability as SQL injection, detailing the attack vector exploiting newline characters within `pg_dump`, and assessing the risks associated with it. I'm also comparing and contrasting it with the earlier CVE-2025-8714 vulnerability.


承知いたしました。ご指定のリリースノートの内容について、日本語訳とGoogle Cloud上のインフラエンジニアとしての影響有無に関するコメントを以下に記載します。

---

### 日本語訳

**`pg_dump`出力のコメントに含まれる名前の改行をスペースに変換 (Noah Misch)** §

改行を含むオブジェクト名は、出力スクリプトに任意のSQLコマンドを注入する可能性を提供してしまっていました。（先行する修正がなければ、この方法で`psql`メタコマンドの注入も可能でした。）

CVE-2012-0868で当時この種の問題は修正されましたが、その後の作業でいくつかのケースが再発していました。

PostgreSQLプロジェクトは、この問題を報告したNoah Misch氏に感謝します。(CVE-2025-8715)

---

### 影響有無とコメント

**影響有無：あり（重要）**

#### コメント

これは **CVE-2025-8715** として追跡されている、**SQLインジェクション**につながるセキュリティ脆弱性の修正です。先に解説したCVE-2025-8714と密接に関連しており、`pg_dump`を利用するすべての環境で注意が必要です。

*   **脆弱性の内容**:
    攻撃者がデータベース内に改行文字を含む名前のオブジェクト（テーブル、カラムなど）を作成した場合、`pg_dump`はそのオブジェクト名をコメントとしてダンプファイルに出力する際に、改行を適切に処理（エスケープ）しませんでした。
    その結果、生成されたバックアップ用のSQLスクリプト内に、攻撃者が意図した任意のSQLコマンドが埋め込まれてしまう可能性がありました。この悪意のあるスクリプトをリストアすると、通常はスーパーユーザー権限で実行されるため、データベース上で任意の操作（ユーザー権限の昇格、データの削除など）が可能になってしまいます。

*   **CVE-2025-8714との関係**:
    この脆弱性は、`pg_dump`の出力ファイルに悪意のあるコードを仕込むという点で、前のCVE-2025-8714と根本原因が似ています。リリースノートに「（先行する修正がなければ、この方法で`psql`メタコマンドの注入も可能でした。）」とある通り、この脆弱性単体でも、`psql`のメタコマンド (`\!`) を注入し、結果としてOSコマンド実行につながる可能性がありました。これら2つの修正は、`pg_dump`/`psql`を使ったリストアプロセスを安全にするための一連の対策と考えるべきです。

*   **インフラエンジニアとしての対応**:
    1.  **クライアントツールのアップデート**: この脆弱性から保護するためには、**`pg_dump`がインストールされているすべての環境で、ツールを修正済みのバージョン（14.19以降）にアップデートする**必要があります。
    2.  **バックアップの信頼性**: この脆弱性は、バックアップの信頼性を根本から損なうものです。バックアップはシステムの最終防衛ラインであり、そのバックアップファイル自体が攻撃ベクトルになることは避けなければなりません。
    3.  **影響範囲**: `pg_dump`を使用しているすべてのバックアップ運用が対象です。これには、Cloud SQLからエクスポート機能を利用する場合や、Compute Engine上で`pg_dump`コマンドを定期実行しているバッチ処理、開発者が手動でダンプを取得する作業などが含まれます。

この修正も、PostgreSQLの安全な運用を維持するために不可欠なセキュリティアップデートです。前述のCVE-2025-8714と合わせて、クライアントツールのアップデートを徹底することが強く推奨されます。

=======================================
**Identifying Release Notes**

I'm working on pinpointing the relevant sections of the PostgreSQL release notes requested by the user. Currently, I am focused on isolating the specific parts that require translation and commentary regarding their impact. This involves carefully reviewing the notes to identify the pertinent information.


**Isolating Key Sections**

I've identified a specific section concerning `BRIN numeric_minmax_multi_ops` and its fix. I am now concentrating on translating the relevant phrases, such as the fix description, and the details of the impact on 64-bit and 32-bit platforms. My goal is to ensure the translation accurately reflects the technical content.


**Evaluating Impact Analysis**

I've moved on to assessing the impact of the fix, and I'm focusing on the potential implications for infrastructure engineers. I am analyzing the use cases of `numeric_minmax_multi_ops` and identifying scenarios where the index might be affected. This requires determining the scope and possible failures.


**Summarizing Translation & Impact**

Okay, I've translated the fix description and impact details, now concentrating on the implications for infrastructure engineers. I've determined the impact is "yes," specifically for BRIN indexes on numeric data types. This includes outlining the performance degradation potential due to incorrect merging of values within the index, and I am detailing the necessary corrective actions, including the need to reindex after upgrading.


**Refining the Infrastructure Analysis**

I've finalized the impact analysis for infrastructure engineers, clarifying the issues and the necessary steps. The key is identifying and reindexing BRIN indexes using `numeric_minmax_multi_ops` on numeric types after upgrading. I'm preparing a query to find these indexes, starting with `pg_index` and `pg_opclass`. My next step is to formulate the correct SQL query.


**Synthesizing the Analysis**

I've now gathered all the required information. I am ready to present a comprehensive summary to the user. This includes the translated release note content, the "yes" impact assessment, the technical explanation of the issues, and the actionable steps for infrastructure engineers.


**Formulating a Summary**

I'm now integrating the translation and impact analysis into a comprehensive summary. My goal is to incorporate the relevant details of the fix and the associated consequences for infrastructure engineers. I'm structuring it in a way that provides actionable steps for the user, considering the technical issues and potential downtime involved.


承知いたしました。ご指定のリリースノートの内容について、日本語訳とGoogle Cloud上のインフラエンジニアとしての影響有無に関するコメントを以下に記載します。

---

### 日本語訳

**BRIN `numeric_minmax_multi_ops` サポート関数における不正確な距離計算を修正 (Peter Eisentraut, Tom Lane)** §

このバグにより、64ビットプラットフォームでは時々結果が間違っており、32ビットプラットフォームでは全く見当違いな結果になっていました。

このロジックは値を範囲にマージする方法を選択するためにのみ使用されるため、明らかな障害は発生しませんでした。最悪の場合でも、インデックスが非効率になり肥大化するだけでした。

それでもなお、`numeric_minmax_multi_ops` 演算子クラスを使用するBRINインデックスは再インデックス（`REINDEX`）することが推奨されます。

---

### 影響有無とコメント

**影響有無：あり**

#### コメント

これはデータの破損やクエリ結果の間違いを引き起こすバグではありませんが、**データベースのパフォーマンスとストレージ効率に影響を与える**重要な修正です。

*   **問題の内容**:
    `numeric`型などの数値型に対して `numeric_minmax_multi_ops` 演算子クラスを指定して作成されたBRINインデックスにおいて、インデックスを構築・更新する際の内部計算に誤りがありました。
    BRINインデックスは、データの物理的なブロック範囲ごとに最小値と最大値を保持することで効率化を図りますが、この計算が不正確なため、インデックスの各エントリが最適な範囲を表現できなくなっていました。
    その結果、本来スキャンする必要のないデータブロックまで読み込んでしまい**クエリパフォーマンスが劣化**したり、インデックス自体が最適な状態よりも大きくなって**ストレージを余分に消費（肥大化）**したりする問題が発生していました。

*   **影響を受ける環境**:
    `numeric`型、`decimal`型、`money`型などの列に対して、`USING BRIN (column_name numeric_minmax_multi_ops)` のように、明示的に`numeric_minmax_multi_ops`演算子クラスを指定してBRINインデックスを作成しているテーブルが対象です。
    大規模なテーブルで、データの物理的な並びと値の順序に相関がある場合にBRINインデックスは採用されやすいため、時系列データやログデータを扱うテーブルなどが該当する可能性があります。

*   **インフラエンジニアとしての対応**:
    1.  **アップデートの適用**: まず、PostgreSQLインスタンスをこの修正が含まれたバージョン（14.19以降）にアップデートします。これにより、今後作成・更新されるBRINインデックスは正しく動作するようになります。
    2.  **既存インデックスの修正**: しかし、アップデートだけでは既存の非効率なインデックスは修正されません。リリースノートの勧告通り、**対象となるインデックスを再構築（`REINDEX`）する**必要があります。
    3.  **再インデックスの計画**: `REINDEX INDEX your_index_name;` を実行すると、完了するまでテーブルへの書き込みがブロックされる可能性があります。サービスへの影響を避けるためには、以下のいずれかの方法を検討してください。
        *   メンテナンスウィンドウを設けてオフラインで`REINDEX`を実行する。
        *   `REINDEX INDEX CONCURRENTLY your_index_name;` を使用する。`CONCURRENTLY`オプションはテーブルのロックを最小限に抑えますが、通常の`REINDEX`よりも時間がかかり、CPUやI/Oリソースを多く消費します。

この対応により、潜在的なパフォーマンス問題を解消し、ストレージ効率を改善できるため、対象となるインデックスが存在するか確認し、計画的に対応することを推奨します。
=======================
