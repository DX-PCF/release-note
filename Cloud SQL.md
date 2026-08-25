# PostgreSQL 14.23 影響評価及び運用保守報告書

本報告書は、2026年5月14日にリリースされた **PostgreSQL 14.23** における各変更点について、インフラ構成・運用への影響、およびアプリケーション開発への確認・テスト要否を整理したものです。
PostgreSQL 14.X 系のサポート終了期限が **2026年11月** [2] に迫っているため、速やかなアップデート計画の策定を推奨します。

---

## 1. 移行の基本情報
* **移行要件:**
  * 既存の 14.X からのアップデートにおいて、**ダンプおよびリストアは不要**です [2]。
  * ただし、14.19 より前のバージョンからアップグレードする場合は、リリースノートのセクション E.6 を確認する必要があります [2]。
* **重要期限:**
  * PostgreSQL コミュニティは **2026年11月** に 14.X リリースシリーズのアップデートリリースを終了（EOL）します [2]。新しいメジャーバージョン（15〜18等）への移行を並行して計画することをお勧めします [1, 2]。

---

## 2. 変更点影響評価サマリー（全38項目）

| 項番 | 変更点概要 | インフラ影響 | アプリ確認 | セキュリティ (CVE) |
| :--- | :--- | :---: | :---: | :---: |
| 1 | 起動パケット処理における無限再帰の防止 | **有** | 無 | CVE-2026-6479 |
| 2 | メモリ割り当て計算における整数オーバーフローの修正 | **有** | 無 | CVE-2026-6473 |
| 3 | ts_headline() における制限超過オプションの拒否 | 無 | **有** | CVE-2026-6473 |
| 4 | timeofday() と pg_strftime() における脆弱性への防御 | 無 | **有** | CVE-2026-6474 |
| 5 | マルチレンジ型作成時のスキーマ権限確認の修正 | 無 | **有** | CVE-2026-6472 |
| 6 | 認証コードにおけるタイミング安全な比較の使用 | **有** | 無 | CVE-2026-6478 |
| 7 | PQfn() の非推奨マークと libpq 内部での使用回避 | 無 | **有** | CVE-2026-6477 |
| 8 | pg_basebackup および pg_rewind におけるパストラバーサルの防止 | **有** | 無 | CVE-2026-6475 |
| 9 | contrib/intarray / contrib/ltree のフィールドオーバーフロー防御 | 無 | **有** | CVE-2026-6473 |
| 10 | contrib/ltree の lquery 型における極端に長い値への防御 | 無 | **做** | CVE-2026-6473 |
| 11 | contrib/spi におけるSQLインジェクションとバッファオーバーラン防止 | 無 | **有** | CVE-2026-6637 |
| 12 | 非決定的照合順序におけるユニーク性仮定の確認 | 無 | **有** | - |
| 13 | ルールアクションおよびルール条件における NEW 生成列の処理修正 | 無 | **有** | - |
| 14 | COPY FROM WHERE 条件におけるシステム列エラーの修正 | 無 | **有** | - |
| 15 | ドロップ列がある場合の CREATE TABLE ... LIKE の統計コピーの修正 | 無 | **有** | - |
| 16 | ALTER INDEX ... ATTACH PARTITION による親インデックス有効化 | 無 | **有** | - |
| 17 | ALTER FOREIGN DATA WRAPPER の依存関係削除の修正 | 無 | **有** | - |
| 18 | マルチレンジを介した複合型の自己メンバー化禁止 | 無 | **有** | - |
| 19 | 符号拡張の変動に影響されない datum-image 比較の修正 | 無 | **有** | - |
| 20 | 非厳格な等価演算子による hashed IN / NOT IN ロジックの修正 | 無 | **有** | - |
| 21 | to_char() における極端に長いロケール固有数値記号の切り捨て | 無 | **有** | - |
| 22 | Ispell 辞書アフィックスファイル解析時のバッファオーバーラン防止 | 無 | **有** | - |
| 23 | ウィンドウ集約のフレーム位置計算における整数オーバーフロー防御 | 無 | **有** | - |
| 24 | pglz_decompress() のバッファオーバーリードの修正 | 無 | **有** | - |
| 25 | エラー発生後における tuplestore データ構造の一貫性保証 | 無 | **有** | - |
| 26 | pg_stat_replication における早期の NULL 遅延報告の修正 | **有** | 無 | - |
| 27 | 非WALログ GiST インデックス使用時の稀なフラッシュ失敗の回避 | 無 | **有** | - |
| 28 | 奇数サイズセグメントにおける DSA ページマップの計算修正 | **有** | 無 | - |
| 29 | 拡張データ型式の拡張統計処理時のサーバークラッシュ可能性の修正 | 無 | **有** | - |
| 30 | チェックポイント WAL 再生と multixact ID 作成の競合状態修正 | **有** | 無 | - |
| 31 | walsender プロセスシャットダウン時の無期限待機防止 | **有** | 無 | - |
| 32 | リカバリ中のテーブル空き領域マップ（FSM）変更の永続化保証 | **有** | 無 | - |
| 33 | 確立された接続なしで呼び出された一部の ecpg 関数のクラッシュ修正 | 無 | **有** | - |
| 34 | pg_upgrade における正しいプロトコルバージョンの使用 | **有** | 無 | - |
| 35 | ケースフォールディングが文字列長を変える場合の ltree の対応修正 | 無 | **有** | - |
| 36 | pg_stat_statements におけるエラー時のメモリリーク防止 | **有** | 無 | - |
| 37 | postgres_fdw における接続クリーンアップ時のクラッシュ回避 | 無 | **商** | - |
| 38 | タイムゾーンデータファイルの tzdata 2026b への更新 | **有** | **有** | - |

---

## 3. 各変更点の詳細影響分析（全38項目）

### [1] 起動パケット処理における無限再帰の防止 (CVE-2026-6479)
* **英語原文:** Prevent unbounded recursion while processing startup packets (Michael Paquier)
  A malicious client could crash the connected backend by alternating rejected SSL and GSS encryption requests indefinitely. The PostgreSQL Project thanks Calif.io (in collaboration with Claude and Anthropic Research) for reporting this problem.
* **日本語訳:** 起動パケット処理中の無限再帰の防止 (Michael Paquier)
  悪意のあるクライアントが、拒否されたSSLおよびGSS暗号化リクエストを無期限に交互に送信することで、接続されたバックエンドをクラッシュさせる可能性がありました。 PostgreSQLプロジェクトは、この問題を報告してくれたCalif.io（ClaudeおよびAnthropic Researchとの共同研究）に感謝します。
* **インフラ影響: 有**
  * **理由・対策:** 接続要求を受け取るPostgreSQLの待ち受けポート（通常5432）に対して、外部（インターネットやパブリック環境等）からアクセス可能になっている場合に深刻度を増す脆弱性です。インフラ側として、`pg_hba.conf`による接続可能なホストIPの制限（ホワイトリスト化）、不要な外部アクセスの制限、セキュリティ製品による拒否されたSSL/GSS通信の多重要求監視などの防御策を確認してください。本パッチの適用により、このクラッシュが防止されます。
* **アプリ確認: 無**
  * **理由・対策:** バックエンド起動パケット処理の不具合であるため、通常のアプリケーションプログラム（SQL等の実装）がこの挙動に影響を受けることはありません。

### [2] メモリ割り当て計算における整数オーバーフローの修正 (CVE-2026-6473)
* **英語原文:** Fix assorted integer overflows in memory-allocation calculations (Tom Lane, Nathan Bossart, Heikki Linnakangas)
  Various places were incautious about the possibility of integer overflow in calculations of how much memory to allocate. Overflow would lead to allocating a too-small buffer which the caller would then write past the end of. This would at least trigger server crashes, and probably could be exploited for arbitrary code execution. In many but by no means all cases, the hazard exists only in 32-bit builds. The PostgreSQL Project thanks Xint Code, Bruce Dang, Sven Klemm, and Pavel Kohout for reporting these problems.
* **日本語訳:** メモリ割り当て計算における各種整数オーバーフローの修正 (Tom Lane, Nathan Bossart, Heikki Linnakangas)
  様々な場所で、割り当てるメモリ量の計算において整数オーバーフローが発生する可能性に対して不注意でした。 オーバーフローが発生すると、小さすぎるバッファが割り当てられ、呼び出し元がそのバッファの末尾を超えて書き込みを行う原因となります。 これは少なくともサーバーのクラッシュを引き起こし、おそらく任意コードの実行に悪用される可能性があります。 すべてのケースに当てはまるわけではありませんが、多くのケースにおいて、この危険性は32ビットビルドでのみ存在します。 PostgreSQLプロジェクトは、これらの問題を報告してくれたXint Code、Bruce Dang、Sven Klemm、およびPavel Kohoutに感謝します。
* **インフラ影響: 有**
  * **理由・対策:** クラッシュだけでなく任意コード実行の可能性がある極めて重要な脆弱性対策です。特に32ビットビルド環境にて稼働しているサーバーにおいては影響が大きいため、移行パッチの早急な適用を推奨します。また、インフラとしてはホストOSのメモリリソース監視やプロセス再起動設定（Systemdなどの異常終了時の自動再起動設定）を確認してください。
* **アプリ確認: 無**
  * **理由・対策:** メモリ割り当てという低レイヤーの実装問題であるため、アプリケーションコードの変更は不要です。

### [3] ts_headline() における制限超過オプションの拒否 (CVE-2026-6473)
* **英語原文:** Reject over-length options in ts_headline() (Michael Paquier)
  The StartSel, StopSel and FragmentDelimiter strings must not exceed 32Kb in length, but this was not checked for. An over-length value would typically crash the server. The PostgreSQL Project thanks Xint Code for reporting this problem.
* **日本語訳:** ts_headline() における極端に長いオプションの拒否 (Michael Paquier)
  `StartSel`、`StopSel`、および`FragmentDelimiter`文字列の長さは32Kbを超えてはなりませんが、これがチェックされていませんでした。 制限を超える長さの値は、通常サーバーをクラッシュさせます。 PostgreSQLプロジェクトは、この問題を報告してくれたXint Codeに感謝します。
* **インフラ影響: 無**
  * **理由・対策:** アプリケーションおよびクエリパラメータのバリデーションに起因します。
* **アプリ確認: 有**
  * **理由・対策:** 全文検索機能（`ts_headline()`）を利用しているかどうかを確認してください。特に、ユーザー入力値を `StartSel` や `StopSel`、`FragmentDelimiter` などのオプション引数にそのままバインド、もしくは連結して渡している箇所がある場合、32KBを超える値が渡されるとエラーが発生するようになります（これまではクラッシュしていました）。アプリケーション側でこれらオプションの文字数（32KB以下）をバリデーションするロジンスを設けてください。

### [4] timeofday() と pg_strftime() における悪意のあるタイムゾーン名への防御 (CVE-2026-6474)
* **英語原文:** Guard against malicious time zone names in timeofday() and pg_strftime() (Tom Lane)
  A crafted time zone setting could pass % sequences to snprintf(), potentially causing crashes or disclosure of server memory. Another path to similar results was to overflow the limited-size output buffer used by pg_strftime(). The PostgreSQL Project thanks Xint Code for reporting this problem.
* **日本語訳:** timeofday() および pg_strftime() における悪意のあるタイムゾーン名への防御 (Tom Lane)
  巧妙に細工されたタイムゾーン設定が `%` シーケンスを `snprintf()` に渡す可能性があり、これによりクラッシュやサーバーメモリの漏洩が引き起こされる恐れがありました。 同様の結果をもたらすもう一つの経路は、`pg_strftime()` が使用する制限されたサイズの出力バッファをオーバーフローさせることでした。 PostgreSQLプロジェクトは、この問題を報告してくれたXint Codeに感謝します。
* **インフラ影響: 無**
  * **理由・対策:** サーバー側の環境設定（タイムゾーン設定など）に不正な値を設定可能かどうかに依存しますが、これはアプリケーションクエリや接続時のパラメータ設定からも悪用可能な可能性があります。
* **アプリ確認: 有**
  * **理由・対策:** アプリケーション接続時に動的に `SET TIME ZONE` などを設定する機能があるか確認してください。ユーザー入力や、信頼できない外部データソースから得た文字列をそのままタイムゾーン名として渡す処理がないかコードレビューを行い、事前に正規のタイムゾーン形式であることをチェック・サニタイズするようにしてください。

### [5] マルチレンジ型作成時におけるスキーマの CREATE 権限確認 (CVE-2026-6472)
* **英語原文:** When creating a multirange type, ensure the user has CREATE privilege on the schema specified for the multirange type (Jelte Fennema-Nio)
  The multirange type can be put into a different schema than its parent range type, but we neglected to apply the required privilege check when doing so. The PostgreSQL Project thanks Jelte Fennema-Nio for reporting this problem.
* **日本語訳:** マルチレンジ型の作成時、マルチレンジ型に指定されたスキーマに対してユーザーが CREATE 権限を持っていることの保証 (Jelte Fennema-Nio)
  マルチレンジ型は、その親となるレンジ型とは異なるスキーマに配置することができますが、その際に必要な権限チェックの適用を怠っていました。 PostgreSQLプロジェクトは、この問題を報告してくれたJelte Fennema-Nioに感謝します。
* **インフラ影響: 無**
  * **理由・対策:** 権限のチェック漏れ問題の修正です。
* **アプリ確認: 有**
  * **理由・対策:** データベースのセットアップスクリプトや、アプリケーション動作用のマイグレーションツール（Rails Active Record, Prisma, Django等）で動的にレンジ・マルチレンジ型（`multirange`）を定義・作成しているか確認してください。異なるスキーマに対してマルチレンジ型を作成する際、そのスキーマへの `CREATE` 権限がないスキーマユーザーで実行していた場合、今回のアップデートにより権限不足（Permission Denied）のエラーを吐くようになります。マイグレーションを実行するDBユーザーの権限を事前に精査してください。

### [6] 認証コードにおけるタイミング安全な文字列比較の使用 (CVE-2026-6478)
* **英語原文:** Use timing-safe string comparisons in authentication code (Michael Paquier)
  Use timingsafe_bcmp() instead of memcmp() or strcmp() when checking passwords, hashes, etc. It is not known whether the data dependency of those functions is usefully exploitable in any of these places, but in the interests of safety, replace them. The PostgreSQL Project thanks Joe Conway for reporting this problem.
* **日本語訳:** 認証コードにおけるタイミング安全な文字列比較の使用 (Michael Paquier)
  パスワードやハッシュなどをチェックする際、`memcmp()` や `strcmp()` の代わりに `timingsafe_bcmp()` を使用します。 これらの関数のデータ依存性が、これらのいずれかの場所で有用に悪用可能かどうかは分かっていませんが、安全のためにこれらを置き換えます。 PostgreSQLプロジェクトは、この問題を報告してくれたJoe Conwayに感謝します。
* **インフラ影響: 有**
  * **理由・対策:** データベースへのログイン認証（hba）処理に関わる修正です。インフラ観点では、不審なタイミングに基づく攻撃（サイドチャネル攻撃など、パスワード解析の試み）への耐久性が向上します。インフラ側での特段の設定変更やスクリプト変更は必要ありませんが、認証機構全体の強健化の一環としてセキュリティチームへの展開情報を共有しておくと有用です。
* **アプリ確認: 無**
  * **理由・対策:** 内部の認証比較関数の入れ替えであり、外部のアプリケーションがSQLを発行する際の挙動、ユーザー認証機能へ悪影響を及ぼすことはありません。

### [7] PQfn() の非推奨マークと libpq 内部での使用回避 (CVE-2026-6477)
* **英語原文:** Mark PQfn() as unsafe, and avoid using it within libpq (Nathan Bossart)
  For a non-integral result type, PQfn() is not passed the size of the output buffer, so it cannot check that the data returned by the server will fit. A malicious server could therefore overwrite client memory. This is unfixable without an API change, so mark the function as deprecated. Internally to libpq, use a variant version that can apply the missing check. The PostgreSQL Project thanks Yu Kunpeng and Martin Heistermann for reporting this problem.
* **日本語訳:** PQfn() を安全ではないとマークし、libpq 内部での使用を避ける (Nathan Bossart)
  非整数（non-integral）の結果型について、`PQfn()` には出力バッファのサイズが渡されないため、サーバーから返されたデータが収まるかどうかを確認できません。 したがって、悪意のあるサーバーがクライアントメモリを上書きする可能性があります。 これはAPIの変更なしには修正できないため、この関数を非推奨（deprecated）としてマークします。 libpqの内部では、不足しているチェックを適用できるバリアントバージョンを使用します。 PostgreSQLプロジェクトは、この問題を報告してくれたYu KunpengおよびMartin Heistermannに感謝します。
* **インフラ影響: 無**
  * **理由・対策:** クライアントライブラリ（libpq）の脆弱性・非推奨化に関する変更です。
* **アプリ確認: 有**
  * **理由・対策:** 自社でC/C++言語を使用したアプリケーション（あるいはPHPの特定の古いPostgreSQL接続ドライバやPythonの低レベルラッパー、インハウスのC言語拡張機能など）を構築しており、`PQfn()` 関数（ファストパス・インターフェース経由での関数呼び出し）をコード内で明示的に呼び出しているかどうかを確認してください。この関数は非推奨（deprecated）となったため、中長期的に標準のクエリ発行方式（`PQexec` など）へと書き換える必要があります。また、非推奨マークによりコンパイル時に警告（Warning）が出るようになる可能性があります。

### [8] pg_basebackup および pg_rewind におけるパストラバーサルの防止 (CVE-2026-6475)
* **英語原文:** Prevent path traversal in pg_basebackup and pg_rewind (Michael Paquier)
  These applications failed to validate output file paths read from their input, so that a malicious source could overwrite any file writable by these applications. Constrain where data can be written by rejecting paths that are absolute or contain parent-directory references. The PostgreSQL Project thanks XlabAI Team of Tencent Xuanwu Lab and Valery Gubanov for reporting this problem.
* **日本語訳:** pg_basebackup および pg_rewind におけるパストラバーサルの防止 (Michael Paquier)
  これらのアプリケーションは入力から読み込まれた出力ファイルパスの検証に失敗していたため、悪意のあるソースがこれらのアプリケーションによって書き込み可能な任意のファイルを上書きする可能性がありました。 絶対パス、または親ディレクトリへの参照を含むパスを拒否することにより、データの書き込み先を制限します。 PostgreSQLプロジェクトは、この問題を報告してくれたTencent Xuanwu LabのXlabAIチームおよびValery Gubanovに感謝します。
* **インフラ影響: 有**
  * **理由・対策:** インフラ運用で `pg_basebackup` を用いたバックアップ取得（cronやバッチなど）、または `pg_rewind` を用いた高可用性（HA）クラスターのフェイルバック自動化を行っている場合が対象です。攻撃的なデータベースサーバーを誤って複製・同期元として指定した場合に、バックアップ実行ホスト上のファイルシステムを破壊（パストラバーサルによる任意のファイル上書き）されるリスクを防ぐ重要な修正です。運用スクリプト内で指定する接続先（ソースDBサーバー）が意図した本物のマスターであることを適切に制限（SSHトンネルや専用サブネット、TLSクライアント認証等）してください。
* **アプリ確認: 無**
  * **理由・対策:** アプリケーションシステムから直接これらのインフラユーティリティを実行することは通常ないため、確認不要です。

### [9] contrib/intarray および contrib/ltree におけるフィールドオーバーフローへの防御 (CVE-2026-6473)
* **英語原文:** Guard against field overflow within contrib/intarray's query_int type and contrib/ltree's ltxtquery type (Tom Lane)
  Parsing of these query structures did not check for overflow of 16-bit fields, so that construction of an invalid query tree was possible. This can crash the server when executing the query. The PostgreSQL Project thanks Xint Code for reporting this problem.
* **日本語訳:** contrib/intarray の query_int 型および contrib/ltree の ltxtquery type におけるフィールドオーバーフローへの防御 (Tom Lane)
  これらのクエリ構造の解析において16ビットフィールドのオーバーフローがチェックされていなかったため、無効なクエリツリーが構築される可能性がありました。 これはクエリの実行時にサーバーをクラッシュさせる可能性があります。 PostgreSQLプロジェクトは、この問題を報告してくれたXint Codeに感謝します。
* **インフラ影響: 無**
  * **理由・対策:** 拡張モジュールのデータ処理に起因します。
* **アプリ確認: 有**
  * **理由・対策:** 拡張機能（Extension）の `contrib/intarray`（query_int型）や `contrib/ltree`（ltxtquery型）を導入しているか確認してください。利用している場合、ユーザーの検索文字列（クエリ）のパーサーが、16ビット（65,535）を超えるような過度な値に対してクラッシュする不具合が修正されました。アプリケーション内で生成される、または入力されるツリー状・配列状の検索クエリ条件が極端に巨大にならないよう配慮・チェックしてください。

### [10] contrib/ltree の lquery 型における極端に長い値への防御 (CVE-2026-6473)
* **英語原文:** Guard against overly long values of contrib/ltree's lquery type (Michael Paquier)
  Values with more than 64K items caused internal overflows, potentially resulting in stack smashes or wrong answers. The PostgreSQL Project thanks Vergissmeinnicht, A1ex, and Jihe Wang for reporting this problem.
* **日本語訳:** contrib/ltree の lquery 型における極端に長い値への防御 (Michael Paquier)
  64K個を超える項目を持つ値は内部オーバーフローを引き起こし、スタックスマッシュや誤った回答をもたらす可能性がありました。 PostgreSQLプロジェクトは、この問題を報告してくれたVergissmeinnicht、A1ex、およびJihe Wangに感謝します。
* **インフラ影響: 無**
  * **理由・対策:** 拡張モジュールの内部処理に起因します。
* **アプリ確認: 有**
  * **理由・対策:** `contrib/ltree` の `lquery` 型を利用し、階層ツリー検索等を行っているか確認してください。1つのlqueryパスパターンに含まれるラベルや項目数が64Kを超えるケースにおいて、スタックスマッシュや間違ったクエリ結果が返る深刻なエラーが修正されました。64K項目以上の膨大な階層データ・検索パターンを作成することがあるか、業務ロジックのチェックをしてください。

### [11] contrib/spi におけるSQLインジェクションとバッファオーバーランの防止 (CVE-2026-6637)
* **英語原文:** Prevent SQL injection and buffer overruns in contrib/spi (Nathan Bossart)
  check_foreign_key() was insufficiently careful about quoting key values, and also used fixed-length buffers for constructing queries. While this module is only meant as example code, it still shouldn't contain such dangerous errors. The PostgreSQL Project thanks Nikolay Samokhvalov for reporting this problem.
* **日本語訳:** contrib/spi におけるSQLインジェクションとバッファオーバーランの防止 (Nathan Bossart)
  check_foreign_key() はキー値のエスケープ（引用符の付加）について十分に注意を払おっておらず、クエリを構築するために固定長バッファを使用していました。 このモジュールは単なるサンプルコードとして意図されているものですが、それでもこのような危険なエラーを含めるべきではありません。 PostgreSQLプロジェクトは、この問題を報告してくれたNikolay Samokhvalovに感謝します。
* **インフラ影響: 無**
  * **理由・対策:** 拡張プラグイン内の処理に起因します。
* **アプリ確認: 有**
  * **理由・対策:** 外部キー違反などの検証用トリガーとして、`contrib/spi` に含まれる `check_foreign_key()` 関数を本番環境等で利用・参照していないか、またはそのコード（C言語）を自社のストアドファンクションのサンプルとしてコピーして再利用していないか確認してください。もし利用している場合はSQLインジェクションの脆弱性やバッファオーバーランが発生する可能性があるため、コードレビューや修正コードへの移行、代替の実装への移行を強く推奨します。

### [12] 非決定的照合順序におけるユニーク性仮定の確認
* **英語原文:** Check for nondeterministic collations before assuming that an equality condition on a collatable type implies uniqueness (Richard Guo)
  Numerous planner optimizations assume that, for example, at most one table row can satisfy WHERE x = 'abc' if there is a unique index on x. However this conclusion is unsafe in general if the index and the WHERE clause have different collations attached. It is safe when both collations are deterministic, because that property essentially requires that equality of two strings means bitwise equality. But nondeterministic collations don't act that way, so that optimizing on the assumption of unique matches can give wrong query answers if either the WHERE clause or the index has a nondeterministic collation.
* **日本語訳:** 照合可能型における一致条件がユニーク性を意味すると仮定する前に、非決定的照合順序を確認する (Richard Guo)
  プランナの多数の最適化は、例えば `x` にユニークインデックスがある場合、多くとも1つのテーブル行が `WHERE x = 'abc'` を満たすことができると仮定しています。 しかし、インデックスと `WHERE` 句に異なる照合順序が割り当てられている場合、この結論は一般に安全ではありません。 両方の照合順序が決定的（deterministic）である場合は安全です。なぜなら、その性質は本質的に2つの文字列の一致がビット単位での一致を意味することを要求するためです。 しかし、非決定的照合順序はそのようには機能しないため、`WHERE` 句またはインデックスのいずれかが非決定的照合順序を持っている場合、ユニーク一致の前提に基づいて最適化を行うと、誤ったクエリ回答が得られる可能性があります。
* **インフラ影響: 無**
  * **理由・対策:** クエリプランナーの最適化に関する不具合です。
* **アプリ確認: 有**
  * **理由・対策:** **アプリケーション全体の検索クエリに関係する非常に重要な変更項目です。**
    システムで「非決定的（nondeterministic）な照合順序（Collation）」を定義・使用して文字列の比較（例: 大文字小文字やアクセントの有無を無視する比較など）を行い、かつその列にユニークインデックスを張っている箇所があるか確認してください。
    これまでは、クエリプランナが「該当レコードは高々1行しか存在しない」と誤認して（ユニークインデックスを信頼しすぎて）無理に高速な実行計画を立てた結果、誤ったクエリ回答（wrong query answers）を返すことがありました。アップデート後はこの最適化が厳格に行われ、正しい実行計画・結果になるため、実行プランの変化によるクエリ速度（インデックススキャンからシーケンシャルスキャンへの移行等）や、返却データが意図したものになるか検証してください。

### [13] ルールアクションおよびルール条件における NEW 生成列の不正確な処理の修正
* **英語原文:** Fix incorrect handling of NEW generated columns in rule actions and rule qualifications (Richard Guo, Dean Rasheed)
  Previously, such column references would produce NULL in INSERT cases, or be equivalent to the OLD value in UPDATE cases.
* **日本語訳:** ルールアクションおよびルール条件における NEW 生成列の不正確な処理の修正 (Richard Guo, Dean Rasheed)
  以前は、このような列への参照は、`INSERT` の場合には `NULL` を生成するか、`UPDATE` の場合には `OLD` の値と同等になっていました。
* **インフラ影響: 無**
  * **理由・対策:** データベース内のルール定義の挙動修正です。
* **アプリ確認: 有**
  * **理由・対策:** 生成列（Generated Columns）とPostgreSQLの「ルール（`CREATE RULE`）」機能、特に `INSERT` や `UPDATE` のアクション（あるいは `INSTEAD OF` ルール等）を組み合わせて使用しているスキーマ設計があるか確認してください。
    これまでルール内で `NEW.生成列名` を参照した際、`INSERT` 時には `NULL` が返り、`UPDATE` 時には `OLD`（更新前）の値が返るというバグがありました。アップデート後は期待通り算術された正しい `NEW` の生成列値が返るようになります。これにより、ルール（またはビューを介したルール）を利用しているアプリケーションは動作結果が変わる可能性があるため、テスト環境での動作検証が必要です。

### [14] COPY FROM WHERE 条件における誤ったエラーの修正
* **英語原文:** Fix spurious “generated columns are not supported in COPY FROM WHERE conditions” errors (Tom Lane)
  Use of a system column in a COPY FROM WHERE condition could sometimes incorrectly report this error.
* **日本語訳:** COPY FROM WHERE 条件における誤ったエラーの修正 (Tom Lane)
  `COPY FROM WHERE` 条件でシステム列（例: `ctid` 等）を使用すると、「生成列はサポートされていません」というエラーが誤って報告されることがありました。
* **インフラ影響: 無**
  * **理由・対策:** DBパーサーのエラー誤判定に関するバグです。
* **アプリ確認: 有**
  * **理由・対策:** CSVなどのデータロード処理として、`COPY FROM` に `WHERE` 句を組み合わせてフィルターを行っているバッチ処理や移行スクリプトが存在するか確認してください。特にシステム列によるフィルタリングを行っていた箇所において、この誤ったエラー（Spurious Error）が解消されます。

### [15] ソーステーブルに削除列がある場合の CREATE TABLE ... LIKE ... INCLUDING STATISTICS の修正
* **英語原文:** Fix CREATE TABLE ... LIKE ... INCLUDING STATISTICS for cases where the source table has dropped column(s) (Julien Tachoires)
  In such cases, extended statistics objects could be copied incorrectly, or the command could give an incorrect error.
* **日本語訳:** ソーステーブルに削除列がある場合の CREATE TABLE ... LIKE ... INCLUDING STATISTICS の修正 (Julien Tachoires)
  このような場合、拡張統計オブジェクトが不正確にコピーされたり、コマンドが不正確なエラーを発生させたりする可能性がありました。
* **インフラ影響: 無**
  * **理由・対策:** DDLコマンドの動作不具合に該当します。
* **アプリ確認: 有**
  * **理由・対策:** 開発ツール、テストの初期化処理、またはアプリケーション内で一時テーブルやコピーテーブルを `CREATE TABLE ... LIKE ... INCLUDING STATISTICS` を使って動的生成しているか確認してください。コピー元に `ALTER TABLE ... DROP COLUMN` された形跡がある場合、この変更を入れないとコピーに失敗したり、拡張統計が引き継がれなかったりする現象を防止できます。

### [16] ALTER INDEX ... ATTACH PARTITION による親インデックス有効化マークの許可
* **英語原文:** Allow ALTER INDEX ... ATTACH PARTITION to mark the parent index valid if appropriate (Sami Imseih)
  There are edge cases in which a partitioned index might remain marked as invalid even when all its leaf indexes are valid. This change provides a mechanism whereby a user can correct such a situation without resorting to manual catalog updates.
* **日本語訳:** ALTER INDEX ... ATTACH PARTITION による親インデックス有効化マークの許可 (Sami Imseih)
  すべてのリーフインデックスが有効であっても、パーティションインデックスが無効としてマークされたままになるというエッジケースが存在します。 この変更は、ユーザーが手動でカタログを更新することに頼らずに、このような状況を修正できるメカニズムを提供します。
* **インフラ影響: 無**
  * **理由・対策:** システムカタログ管理レベルの変更点です。
* **アプリ確認: 有**
  * **理由・対策:** 大規模なパーティション（分割）テーブルを利用し、アプリケーション側（あるいは運用バッチ）で動的にパーティションインデックスの作成・割り当て（`ATTACH PARTITION`）をしているか確認してください。これまでは、エッジケースにおいて親インデックスが無効（`invalid`）な状態のままになってしまう不具合を回避するため、手動でシステムカタログを書き換えるというハイリスクな対処が必要でした。今後は `ALTER INDEX ... ATTACH PARTITION` で適切に有効状態（valid）へマークされるため、運用ツール・スクリプトを更新して本コマンドが適切に適用されるように確認してください。

### [17] ALTER FOREIGN DATA WRAPPER の依存関係削除の修正
* **英語原文:** Fix ALTER FOREIGN DATA WRAPPER to not drop the wrapper object's dependency on its handler function (Jeff Davis)
* **日本語訳:** ALTER FOREIGN DATA WRAPPER の依存関係削除の修正 (Jeff Davis)
  `ALTER FOREIGN DATA WRAPPER` 実行時に、ラッパーオブジェクトが持つハンドラ関数への依存関係が誤って削除されてしまうバグを修正しました。
* **インフラ影響: 無**
  * **理由・対策:** カタログ依存関係の管理バグ修正です。
* **アプリ確認: 有**
  * **理由・対策:** 外部データラッパー（FDW、例：`postgres_fdw`, `mysql_fdw`など）をインフラ構成内に定義・追加しており、その定義を変更する DDL メンテナンス（`ALTER FOREIGN DATA WRAPPER`）を実行することがあるか確認してください。この修正により、ハンドラ関数のみを誤ってドロップしてしまい FDW が整合性を失うなどの重大なシステムトラブルを未然に防止できます。

### [18] マルチレンジを介した複合型の自己メンバー化禁止
* **英語原文:** Disallow making a composite type be a member of itself via a multirange (Heikki Linnakangas)
  We already forbade such cases when the intermediate type is a domain, array, composite type, or range; but multiranges were overlooked.
* **日本語訳:** マルチレンジを介した複合型の自己メンバー化禁止 (Heikki Linnakangas)
  中間タイプがドメイン、配列、複合型、またはレンジである場合は、このようなケースをすでに禁止していましたが、マルチレンジが見落とされていました。
* **インフラ影響: 無**
  * **理由・対策:** DDLの妥当性検査（バリデーション）の不整合修正です。
* **アプリ確認: 有**
  * **理由・対策:** 複雑なカスタムスキーマにおいて、複合型（Composite Type）がマルチレンジ型をメンバに持ち、かつそのマルチレンジが自分自身の複合型を参照するような「循環参照」の定義を作っていないか確認してください。このような整合性の取れない極端なスキーマはアップデート後にエラーとなるため、事前に定義を確認してください。

### [19] 符号拡張の変動に影響されない datum-image 比較の修正
* **英語原文:** Fix datum-image comparisons to be insensitive to sign-extension variations (David Rowley)
  This fixes some situations that previously led to “could not find memoization table entry” errors or wrong query results.
* **日本語訳:** 符号拡張の変動に影響されない datum-image 比較の修正 (David Rowley)
  これにより、以前「メモ化テーブルエントリが見つかりませんでした」というエラーや、誤ったクエリ結果を引き起こしていたいくつかの状況が修正されます。
* **インフラ影響: 無**
  * **理由・対策:** クエリ実行エンジンの内部演算の修正です。
* **アプリ確認: 有**
  * **理由・対策:** 符号付き整数データ型（`smallint`, `integer`など）を使用しており、特にメモ化（Memoize）ノードが適用された複雑なJOINを含むクエリを実行した際、「`could not find memoization table entry`」というシステムエラーが発生したり、クエリの検索結果が不安定（Wrong Results）になったりしていなかったか確認してください。同様の事象が発生していた、あるいは複雑な集計クエリを処理するアプリケーションにおいては、動作検証を行うと安定性が確認できます。

### [20] 非厳格な等価演算子による hashed IN / NOT IN ロジックの修正
* **英語原文:** Fix incorrect logic for hashed IN / NOT IN with non-strict equality operator (Chengpeng Yan)
  The previous coding could crash or give wrong answers. All built-in data types have strict equality operators, so that this issue could only arise with an extension data type.
* **日本語訳:** 非厳格な等価演算子による hashed IN / NOT IN ロジックの修正 (Chengpeng Yan)
  以前のコーディングではクラッシュや誤った回答を引き起こす可能性がありました。 すべての組み込みデータ型は厳格な等価演算子を持っているため、この問題は拡張データ型でのみ発生する可能性がありました。
* **インフラ影響: 無**
  * **理由・対策:** 拡張データ型用の内部バグ修正です。
* **アプリ確認: 有**
  * **理由・対策:** サードパーティ製の拡張モジュールや自作のカスタム拡張データ型を使用しており、そのデータ型に **「非厳格な（non-strict、NULLを許容、あるいは入力がNULLでもNULL以外を返し得る）等価演算子」** を定義している場合、それを対象にした `IN` や `NOT IN` クエリを実行しているか確認してください。以前のコードでは、ハッシュベースのIN実行時にクラッシュや誤った真偽判定を返す深刻なバグがありましたが、これが修正されています。独自データ型を多用するシステムでは要テストです。

### [21] to_char() における極端に長いロケール固有数値記号の切り捨て
* **英語原文:** Truncate overly-long locale-specific numeric symbols in to_char() (Tom Lane)
  If a locale specified a currency symbol, thousands separator, or decimal or sign symbol more than 8 bytes long, a buffer overrun was possible. No such locales exist in the real world, and it's impractical for an unprivileged attacker to install a malicious locale definition underneath a Postgres server; but for safety's sake check for overlength symbols and truncate if needed.
* **日本語訳:** to_char() における極端に長いロケール固有数値記号の切り捨て (Tom Lane)
  ロケールが8バイトを超える長さの通貨記号、千の位の区切り文字、小数点または符号記号を指定した場合、バッファオーバーランが発生する可能性がありました。 現実世界にはそのようなロケールは存在せず、非特権の攻撃者がPostgresサーバーの下に悪意のあるロケール定義をインストールすることは非現実的ですが、安全のために、制限を超える長さの記号をチェックし、必要に応じて切り捨てます。
* **インフラ影響: 無**
  * **理由・対策:** ロケール定義とライブラリ処理に関する保安対策です。
* **アプリ確認: 有 (低)**
  * **理由・対策:** `to_char()` を使用して数値の書式化（通貨、少数表記など）をミリ秒単位や高精度で行っている場合、特殊なカスタムロケール環境、あるいは異常なロケールデータが設定されていると、8バイトを超える記号部分が自動的に切り捨てられるようになります。標準的な日本語ロケール（`ja_JP.UTF-8`等）では問題ありませんが、多国籍向けの独自フォーマット処理がある場合は画面表示の崩れがないか確認してください。

### [22] Ispell 辞書アフィックスファイル解析時のバッファオーバーラン防止
* **英語原文:** Prevent buffer overruns when parsing an affix file for an Ispell dictionary (Tom Lane)
  A corrupt or malicious affix file could crash the server. This is not considered a security issue because text search configuration files are presumed trustworthy, but it still seems worth fixing.
* **日本語訳:** Ispell 辞書アフィックスファイル解析時のバッファオーバーラン防止 (Tom Lane)
  破損した、または悪意のあるアフィックス（接辞）ファイルがサーバーをクラッシュさせる可能性がありました。 テキスト検索設定ファイルは信頼できると想定されているため、これはセキュリティ問題とは見なされませんが、修正する価値は十分にあります。
* **インフラ影響: 無**
  * **理由・対策:** サーバーファイルの破損に対処する修正です。
* **アプリ確認: 有 (低)**
  * **理由・対策:** テキスト検索（Full Text Search）機能に Ispell 辞書とアフィックス定義ファイルをインポートして使用しているか確認してください。もし利用している場合は、破損ファイルの読み込み時にサーバーを巻き込んで強制終了するバグが防がれるようになったため、辞書ファイルのデプロイ・更新フローのテストを実施してください。

### [23] ウィンドウ集約のフレーム開始・終了位置計算における整数オーバーフローへの防御
* **英語原文:** Guard against integer overflow in calculations of frame start and end positions for window aggregates (Richard Guo)
  Very large user-specified offsets (close to INT64_MAX) could result in errors or incorrect query results.
* **日本語訳:** ウィンドウ集約におけるフレーム開始および終了位置の計算における整数オーバーフローへの防御 (Richard Guo)
  ユーザーが指定した非常に大きなオフセット（`INT64_MAX`に近い値）により、エラーや誤ったクエリ結果が引き起こされる可能性がありました。
* **インフラ影響: 無**
  * **理由・対策:** ウィンドウ関数のクエリ演算に起因する修正です。
* **アプリ確認: 有**
  * **理由・対策:** 分析クエリやレポート表示用の SQL にて、ウィンドウ関数（`ROWS`、`RANGE`、`GROUPS`）のフレーム指定オフセット値として、プログラム上の最大値や動的な巨大数値（`INT64_MAX` 付近）が指定される可能性がないか確認してください。これまでは、このような極端な値を指定すると、計算オーバーフローによりサイレントに「誤った順序、範囲、集計結果」が返されるか、あるいはエラーになっていました。アップデート後は、正しく安全にオーバーフローがチェックされます。

### [24] pglz_decompress() のバッファオーバーリードの修正
* **英語原文:** Fix buffer overread when pglz_decompress() receives corrupt input (Andrew Dunstan)
  It was possible to read a few bytes past the end of the input, which in very unlucky cases might cause a crash.
* **日本語訳:** pglz_decompress() のバッファオーバーリードの修正 (Andrew Dunstan)
  入力の末尾を数バイト超えて読み取ってしまう可能性があり、非常に運が悪い場合にはクラッシュを引き起こす可能性がありました。
* **インフラ影響: 無**
  * **理由・対策:** 内部圧縮解凍関数のメモリ読み込み安全性修正です。
* **アプリ確認: 有 (低)**
  * **理由・対策:** アプリケーション自体に大きな影響はありませんが、内部のデータ格納（TOAST等による暗黙の圧縮データ、あるいは独自の圧縮関数呼び出し）において、稀に発生していたバックエンドプロセスの不安定化（予期せぬクラッシュ）を解消します。壊れたTOASTデータが存在するような破損ファイルシステム等でリカバリをかける際、安全性が向上します。

### [25] エラー発生後における tuplestore データ構造の一貫性保証
* **英語原文:** Ensure that tuplestore data structures are internally consistent even after an error (Tom Lane)
  The code was previously careless about this, which is fine most of the time but is problematic for the tuplestore backing a WITH HOLD cursor. In v15 and before this leads to easily-reproducible crashes; later branches are not known to be vulnerable, but it seems best to preserve consistency in all.
* **日本語訳:** エラー発生後における tuplestore データ構造の一貫性保証 (Tom Lane)
  以前のコードではこれに関して不注意でした。ほとんどの場合は問題ありませんが、`WITH HOLD` カーソルをバッキング（支援）する tuplestore においては問題となります。 v15以前では、これにより簡単に再現可能なクラッシュが発生します。それ以降のブランチでは脆弱であることは知られていませんが、すべてのブランチで一貫性を保つのが最善と考えられます。
* **インフラ影響: 無**
  * **理由・対策:** 内部の一時データストアのメモリ状態を回復するための修正です。
* **アプリ確認: 有**
  * **理由・対策:** アプリケーション内で **「`DECLARE ... CURSOR WITH HOLD`（トランザクション終了後も維持されるカーソル）」** を使用し、かつトランザクション中のエラー（クエリ失敗など）が発生した後の後続処理、またはロールバック時においてカーソルの操作を行っているか確認してください。
    これまで、エラー発生後のクリーンアップ中に tuplestore（一時メモリテーブル構造）の不整合が発生し、データベースのクラッシュを引き起こし、他のクライアントセッションへ影響を及ぼす可能性がありました。本アップデートを適用することで、このバグが修正され、エラー時処理の可用性が大幅に向上します。

### [26] pg_stat_replication における早期の NULL 遅延報告の修正
* **英語原文:** Fix premature NULL lag reporting in pg_stat_replication (Shinya Kato)
  The lag columns frequently read as NULL even while replication activity was happening.
* **日本語訳:** pg_stat_replication における早期の NULL 遅延（lag）報告の修正 (Shinya Kato)
  レプリケーション活動が行われている間でも、遅延列が頻繁に `NULL` として読み取られていました。
* **インフラ影響: 有**
  * **理由・対策:** **インフラのレプリケーション監視（マスター・スタンバイ間の遅延監視）において非常に重要な修正です。**
    インフラ運用保守チームが `pg_stat_replication` の `write_lag`, `flush_lag`, `replay_lag` などのカラムを監視（Zabbix, Datadog, Prometheus等）し、レプリケーションの健全性を評価しているか確認してください。これまでは、実際はレプリケーション中であるにもかかわらず頻繁に `NULL` が返ってしまい、誤検知や監視の欠落が発生しやすくなっていました。アップデート後は正しく正確な遅延時間が報告されるようになるため、監視しきい値や監視スクリプトの評価（`NULL` 扱い部分の再設計など）を実施してください。
* **アプリ確認: 無**
  * **理由・対策:** システム運用統計ビューの修正であり、通常のビジネスロジックを実行するアプリには影響ありません。

### [27] 非WALログ GiST インデックス使用時の稀なフラッシュ失敗の回避
* **英語原文:** Avoid rare flush failure when working with non-WAL-logged GiST indexes (Tomas Vondra)
  A non-logged GiST index could nonetheless sometimes produce “xlog flush request n/nnnn is not satisfied” errors, due to incorrect selection of a “fake LSN” to represent an insertion point.
* **日本語訳:** 非WALログ GiST インデックス使用時の稀なフラッシュ失敗の回避 (Tomas Vondra)
  ログに記録されない GiST インデックスであっても、挿入地点を表す「偽の LSN」の誤った選択により、時々「xlog flush request n/nnnn is not satisfied」エラーが発生することがありました。
* **インフラ影響: 無**
  * **理由・対策:** 非ログ機能とGiSTインデックスの処理不具合に関する修正です。
* **アプリ確認: 有**
  * **理由・対策:** 地理空間データ（PostGISなど）や、高速なデータ挿入のために **「`UNLOGGED`（非WALログ記録）テーブル」に「GiST インデックス」** を作成して運用している機能があるか確認してください。
    データ挿入時に稀に「`xlog flush request is not satisfied`（WALフラッシュ要求未充足）」エラーが発生し、処理が異常終了・ロールバックしていたバグが解消されます。バッチの異常終了が頻発していた場合、この不具合に該当していた可能性があります。

### [28] 奇数サイズセグメントにおける DSA ページマップの必要サイズ過小評価の修正
* **英語原文:** Fix underestimate of required size of DSA page maps for odd-size segments (Paul Bunn)
  This miscalculation led to out-of-bounds accesses and hence server crashes.
* **日本語訳:** 奇数サイズセグメントにおける DSA ページマップの必要サイズ過小評価の修正 (Paul Bunn)
  この誤計算は範囲外（out-of-bounds）へのアクセスを招き、結果としてサーバーのクラッシュを引き起こしました。
* **インフラ影響: 有**
  * **理由・対策:** 動的共有メモリ（Dynamic Shared Memory Allocator: DSA）の不具合は、特にメモリを激しく消費する並列クエリ（Parallel Query）実行時など、共有メモリセグメントが動的に作成されるインフラ環境下でサーバーを不意にクラッシュさせる深刻なリスクがありました。本修正により、DSA ページマップのサイズ計算バグが修正され、共有メモリを有効活用するデータベースサーバー全体の安定性が大幅に向上します。インフラとしては並列ワーカー数（`max_parallel_workers` など）や共有メモリ容量（`shared_buffers` ほか）の変更は必要ありませんが、安定性向上の恩恵を受けられます。
* **アプリ確認: 無**
  * **理由・対策:** 内部のメモリマッピング最適化であるため、アプリケーション側での処理への直接的な変更はありません。

### [29] 拡張データ型式の拡張統計処理時のサーバークラッシュ可能性の修正
* **英語原文:** Fix possible server crash when processing extended statistics on expressions of extension data types (Michael Paquier)
  NULL pointer dereferences were possible if the data type's typanalyze function does not compute any useful statistics. No in-core typanalyze function behaves that way, but extensions could.
* **日本語訳:** 拡張データ型式の拡張統計処理時のサーバークラッシュ可能性の修正 (Michael Paquier)
  データ型の `typanalyze` 関数が有用な統計を計算しない場合、`NULL` ポインタの参照剥がし（dereference）が発生する可能性がありました。 組み込み（in-core）の `typanalyze` 関数はそのようには動作しませんが、拡張モジュールでは動作する可能性がありました。
* **インフラ影響: 無**
  * **理由・対策:** 拡張モジュール側の解析関数に関するバグ修正です。
* **アプリ確認: 有**
  * **理由・対策:** サードパーティ製の特殊な拡張モジュール（データ型）をインストールして使用しており、さらにそのカラムに対して `CREATE STATISTICS`（拡張統計機能）を設定し、且つそのデータ型の解析ロジック（`typanalyze`）が特定の例外を返す、または何も返さない（統計情報を計算しない）場合、`ANALYZE` 実行時やクエリプラン立案時にサーバーがクラッシュする不具合がありました。お使いのサードパーティ型（独自実装含む）の統計情報の設計や、`CREATE STATISTICS` を使用している箇所の確認を行ってください。

### [30] チェックポイント WAL 再生と multixact ID 作成の競合状態修正
* **英語原文:** Fix race condition between WAL replay of checkpoints and multixact ID creations (Heikki Linnakangas)
  A standby server following WAL from a primary of an older minor version could get into a crash-and-restart loop complaining about “could not access status of transaction”.
* **日本語訳:** チェックポイント WAL 再生と multixact ID 作成の競合状態修正 (Heikki Linnakangas)
  古いマイナーバージョンのプライマリからの WAL に追従しているスタンバイサーバーが、「トランザクションのステータスにアクセスできませんでした (could not access status of transaction)」と訴えて、クラッシュと再起動のループに陥る可能性がありました。
* **インフラ影響: 有**
  * **理由・対策:** **クラスタ構成（レプリケーションによるマスター・スタンバイ構成）を採用しているインフラにおいて重大な修正です。**
    特にプライマリとスタンバイでマイナーバージョンのアップデート時期がズレた際（あるいは異なるマイナーバージョンからレプリケーションを開始した際）、スタンバイサーバーで WAL 再生（リカバリ）中に競合が発生し、スタンバイが「`could not access status of transaction`」エラーを吐いてクラッシュと再起動の無限ループに入る致命的なリスクがありました。パッチ適用後は競合状態が解消されます。アップデート作業手順において、マスターとスタンバイのマイナーバージョンを同時、もしくは短い時間差で確実に合わせることが運用のセキュリティ（可用性）を保つ鍵となります。
* **アプリ確認: 無**
  * **理由・対策:** インフラ・レプリケーションの内部整合性の不具合であるため、アプリケーション接続には関係しません。

### [31] walsender プロセスシャットダウン時の無期限待機防止
* **英語原文:** Prevent indefinite wait in shutdown of a walsender process (Anthonin Bonnefoy)
  At shutdown of a cluster that is publishing logical replication data, the walsender waits for all pending WAL to be written out. But it did not correctly request that to happen, so that in some cases this could become an indefinite wait.
* **日本語訳:** walsender プロセスシャットダウン時の無期限待機防止 (Anthonin Bonnefoy)
  ロジカルレプリケーションデータをパブリッシュしているクラスターのシャットダウン時、`walsender` はすべての保留中の WAL が書き出されるのを待ちます。 しかし、そうするように正しく要求していなかったため、場合によっては無期限の待機状態になることがありました。
* **インフラ影響: 有**
  * **理由・対策:** **インフラの計画メンテナンス時間（メンテナンスに伴うPostgreSQLシャットダウンなど）に大きな影響を及ぼします。**
    ロジカルレプリケーション（論理複製）を使用しているシステムで、データベースをシャットダウンしようとした際に `walsender` プロセスがWALの掃き出しを待ち続けてフリーズし、サーバーの自動シャットダウンがタイムアウト（あるいは無期限に終了しない）事象がありました。本バグ修正により、シャットダウン要求が確実に完了するようになります。運用保守の移行計画において、アップデート適用後のシャットダウン応答がスムーズになることを確認してください。
* **アプリ確認: 無**
  * **理由・対策:** システムメンテナンス・シャットダウン時の不具合であり、アプリケーション起動中（アクティブ中）の通常のクエリ実行には関係ありません。

### [32] リカバリ中のテーブル空き領域マップ（FSM）変更の永続化保証
* **英語原文:** Ensure that changes to tables' free space maps are persisted during recovery (Alexey Makhmutov)
  Previously, while WAL replay did update the free space map while replaying operations that should change it, the map page buffer did not get marked dirty if checksums are enabled, so that the changes might never get written out. On a standby server, over time this would result in a map wildly at variance with the table's actual contents. While the map is only used as a hint, this condition could cause significant performance degradation for some period of time after the standby server is promoted to be active, until most of the map has been repaired by updates.
* **日本語訳:** リカバリ中のテーブル空き領域マップ（FSM）変更の永続化保証 (Alexey Makhmutov)
  以前は、変更すべき操作を再生する間に WAL 再生が空き領域マップを更新していたものの、チェックサムが有効な場合にマップページバッファがダーティ（変更あり）としてマークされず、結果として変更が書き出されない可能性がありました。 スタンバイサーバー上では、時間が経つにつれて、テーブルの実際の内容と大きく乖離したマップになっていました。 マップはヒントとしてのみ使用されますが、この状況は、スタンバイサーバーがアクティブに昇格した後、アップデートによってマップの大部分が修復されるまでの一定期間、大幅なパフォーマンスの低下を引き起こす可能性がありました。
* **インフラ影響: 有**
  * **理由・対策:** **フェイルオーバー時のインフラ信頼性およびパフォーマンス面における超重要バグ修正です。**
    インフラ側でデータベースのデータページチェックサム（`data_checksums`）を有効化し、かつリードレプリカ（スタンバイ）を運用しているシステムにおいて、スタンバイ上での空き領域マップ（FSM）の変更が物理ディスクに永続化（書き出し）されていませんでした。この状態が長く続くと、フェイルオーバーしてスタンバイがプライマリ（書き込み可能マスター）に昇格した直後、空き領域マップの不整合により、新しいレコードを書き込む際に空きスペースを効率よく見つけられず、ディスクI/Oが激増し、急激な性能低下を引き起こしていました。このアップデートを適用することで、スタンバイ上の空き領域情報が正しく永続化され、昇格直後のシステムクラッシュや遅延を予防できます。
* **アプリ確認: 無**
  * **理由・対策:** 内部の物理ストレージ・マップの最適化および書き込み管理に起因するものであり、アプリ側のSQL記述や接続に変更はありません。

### [33] 確立された接続なしで呼び出された一部の ecpg 関数のクラッシュ修正
* **英語原文:** Fix crashes in some ecpg functions when called without any established connection (Shruthi Gowda)
* **日本語訳:** 確立された接続なしで呼び出された一部の ecpg 関数のクラッシュ修正 (Shruthi Gowda)
  データベースとの接続が確立されていない状態で特定の ecpg 関数（C言語埋め込みSQL）が呼び出された場合に、NULLポインタ等の原因でクライアントプログラムがクラッシュ（コアダンプ）するバグを修正しました。
* **インフラ影響: 無**
  * **理由・対策:** クライアントプロセスにおける処理です。
* **アプリ確認: 有**
  * **理由・対策:** C言語ベースの埋め込みSQL（`ecpg`）を用いてデータベース通信を行っているレガシープログラム、または高性能なバッチプログラムがあるか確認してください。これまでは、ネットワーク切断後や初期の接続処理失敗時に、接続状態を適切に検証せずに ecpg 関連の特定関数（内部APIなど）を実行した際にプログラム本体がクラッシュ（強制終了）する不具合があり、アプリ側のエラーハンドリングを妨げていました。本パッチ適用により、エラーハンドリング（接続切れのエラーを正しくコードでキャッチする等）が安定して行えるようになります。

### [34] pg_upgrade における正しいプロトコルバージョンの使用
* **英語原文:** In pg_upgrade, take care to use the correct protocol version when connecting to older source servers (Jacob Champion)
  This could be problematic when attempting to upgrade from a pre-2018 server.
* **日本語訳:** pg_upgrade における正しいプロトコルバージョンの使用 (Jacob Champion)
  `pg_upgrade` において、古いソースサーバーに接続する際に正しいプロトコルバージョンを使用するように配慮しました。 これは、2018年より前の古い PostgreSQL サーバーからアップグレードしようとする場合に問題となる可能性がありました。
* **インフラ影響: 有**
  * **理由・対策:** インフラ移行（メジャーバージョンアップ）作業を行う際のバグ修正です。2018年以前の非常に古いバージョン（例: PostgreSQL 9.X や 10等）から `pg_upgrade` を使って一気に 14 系にアップグレードしようとする、歴史的なスキーマを抱えたシステムがある場合にのみ影響します。これに該当する古いDBの統合・移行作業を計画している場合は、インフラ担当者が使用する `pg_upgrade` ツールのバージョンを 14.23（またはそれ以降の最新）に保ってアップグレード作業を実行するようにしてください。
* **アプリ確認: 無**
  * **理由・対策:** データベースのインプレース・アップグレード用の管理コマンドの挙動であり、アプリケーションには一切影響しません。

### [35] ケースフォールディングが文字列のバイト長を変更する場合の contrib/ltree の対応修正
* **英語原文:** Fix contrib/ltree to cope when case-folding changes a string's byte length (Jeff Davis)
  Previously, lquery patterns specifying case-insensitive matching might fail to match labels they should match.
* **日本語訳:** ケースフォールディングが文字列のバイト長を変更する場合の contrib/ltree の対応修正 (Jeff Davis)
  ケースフォールディング（大文字小文字の変換・正規化）によって文字列のバイト長が変化する場合に対応するよう `contrib/ltree` を修正しました。 以前は、大文字小文字を区別しない一致（case-insensitive matching）を指定する `lquery` パターンが、一致するはずのラベルと一致しないことがありました。
* **インフラ影響: 無**
  * **理由・対策:** 拡張モジュールにおける文字列評価ロジックに起因します。
* **アプリ確認: 有**
  * **理由・対策:** 階層パス検索を処理する `contrib/ltree` モジュールを導入しており、さらに `lquery` において大文字小文字を区別しない（`*` 修飾子などによる）マッチング機能を使用しているか確認してください。
    特に、ドイツ語の「ß」（大文字化すると「SS」になりバイト長が変わる）などの特殊文字やマルチバイトの特殊言語表現において、ケース変換時のバイト長変化を正しく扱えずに、一致するべきデータが不一致（検索漏れ）になるバグが修正されています。多言語対応を行っている、または特殊記号を階層ラベル（ツリーパス）に含むアプリケーションにおいてテスト環境での検索動作再確認を推奨します。

### [36] contrib/pg_stat_statements におけるエラー時のメモリリーク防止
* **英語原文:** In contrib/pg_stat_statements, don't leak memory if an error occurs while parsing the pgss_query_texts.stat file (Heikki Linnakangas)
* **日本語訳:** contrib/pg_stat_statements におけるエラー時のメモリリーク防止 (Heikki Linnakangas)
  `contrib/pg_stat_statements` において、`pgss_query_texts.stat` ファイルの解析中にエラー（破損など）が発生した場合に、メモリリークが発生する不具合を修正しました。
* **インフラ影響: 有**
  * **理由・対策:** クエリ実行統計情報（`pg_stat_statements`）を長時間にわたり稼働させて統計を収集し続けている監視重視のインフラ環境が対象です。ディスクI/O、ファイル破損、または極端なタイミングによるパースエラー発生時に、データベースメモリ（RAM）がじわじわと圧迫されるリスクを防止します。インフラのメモリリソース枯渇（OOM KillerによるPostgresプロセスの強制終了）の危険を回避する安定化機能です。
* **アプリ確認: 無**
  * **理由・対策:** サーバー側の監視用ライブラリのバグ修正であり、アプリの通常動作やSQLに影響はありません。

### [37] contrib/postgres_fdw における失敗した接続の早期クリーンアップに起因するクラッシュの回避
* **英語原文:** In contrib/postgres_fdw, avoid crash due to premature cleanup of a failed connection (Etsuro Fujita)
  If a remote connection fails abort cleanup, we can't use it any longer. But delay closing the connection object until end of transaction, because there might still be references to it within data structures such as open cursors.
* **日本語訳:** contrib/postgres_fdw における失敗した接続の早期クリーンアップに起因するクラッシュの回避 (Etsuro Fujita)
  `contrib/postgres_fdw`（外部データラッパー）において、リモートへの接続（通信）失敗クリーンアップ中に早期のオブジェクトクローズにより発生していたクラッシュを回避します。
  リモート接続が失敗した場合、その接続はこれ以上使用できません。 しかし、開いているカーソルなどの内部データ構造内にまだその参照が存在している可能性があるため、トランザクションの終了まで接続オブジェクトを閉じるのを遅らせるよう改善しました。
* **インフラ影響: 無**
  * **理由・対策:** 拡張モジュール内部の接続破棄フローに関する設計修正です。
* **アプリ確認: 有**
  * **理由・対策:** **外部のPostgreSQLデータベースとデータを相互リンクさせる `postgres_fdw`（Foreign Data Wrapper）を頻繁に利用しているシステムが対象です。**
    リモート先（連携先）のデータベースが一時的なネットワーク断線やサーバー停止などにより接続不可・タイムアウトに陥った際、自クラスタ側のバックエンドプロセスが「クリーンアップの不備によるポインタ参照不整合」でクラッシュ（強制切断）してしまうのを防ぎます。これにより、リモート先がダウンしていても、自システムはクラッシュせず正常にアプリケーションのエラーハンドリング（または他の独立したローカルクエリの実行）を維持できるようになります。フェイルオーバーや通信障害テストのシナリオにおいて、期待通りエラー終了しクラッシュしないか検証してください。

### [38] タイムゾーンデータファイルの tzdata 2026b への更新
* **英語原文:** Update time zone data files to tzdata release 2026b (Tom Lane)
  British Columbia (America/Vancouver) will be on year-round UTC-07 (effectively, permanent DST) beginning in November 2026. This release assumes that their TZ abbreviation will be MST from that time forward. That seems likely to change, but it's unclear what new abbreviation will be used. Also a historical correction for Moldova: they have followed EU DST transition times since 2022.
* **日本語訳:** タイムゾーンデータファイルを tzdata リリース 2026b に更新 (Tom Lane)
  ブリティッシュコロンビア州（America/Vancouver）は、2026年11月から通年でUTC-07（事実上、永久的な夏時間）を導入します。 このリリースでは、これ以降の彼らのTZ（タイムゾーン）略称が `MST` になると想定しています。 これは変更される可能性がありますが、どのような新しい略称が使用されるかは不明です。 また、モルドバに関する歴史的な修正として、彼らは2022年以降、EUの夏時間（DST）移行時間を追従しています。
* **インフラ影響: 有**
  * **理由・対策:** データベース内の組み込みタイムゾーンテーブルが最新に更新されます。インフラでOS側の tzdata 更新と足並みを揃え、サーバー日時のずれを防止してください。
* **アプリ確認: 有**
  * **理由・対策:** 予約システム、タイムスタンプ記録、履歴分析などで、**カナダ・ブリティッシュコロンビア（バンクーバー等）やモルドバ** 地域の現地日時を処理しているアプリケーションがあるか確認してください。2026年11月以降の夏時間の自動切替フラグが廃止され恒久的なUTC-07に移行するため、日時計算の挙動（特にサマータイム有無に基づく時差計算処理）がローカルサーバー内で正しく反映されるか、テストデータを使用して稼働確認を実施してください。

---

## 4. 運用保守担当者への推奨ロードマップ

本リリースノート（PostgreSQL 14.23）の評価結果に基づき、以下の移行プロセスを推奨します。

1. **インフラセキュリティ優先適用:**
   * 特にインターネット、パブリックネットワークから接続可能、または複数ユーザーが利用する共有環境の場合、**[1] (CVE-2026-6479)** および **[2] (CVE-2026-6473)** の対策が急務です。テスト環境での短時間の機能テスト完了後、本マイナーバージョンアップを計画的に進めてください。
2. **クラスタ・高可用性環境の検証:**
   * レプリケーション構成を取っている場合、**[30] (WAL再生競合)** と **[32] (FSM永続化)** の修正により、障害発生時の安定性が大きく向上します。プライマリをアップグレードした後は速やかにスタンバイ側もアップデートする手順を用意してください。
3. **アプリケーション影響範囲の棚卸し:**
   * 開発・アプリ保守チームに対し、以下の機能の利用有無についてヒアリング・棚卸しを依頼してください：
     * **[12] 非決定的照合順序（Collation）を使用したユニークインデックス**
     * **[13] 生成列（Generated Columns）とルール（Rule）の併用**
     * **[25] DECLARE ... CURSOR WITH HOLD（保持カーソル）**
     * **[37] postgres_fdw による外部テーブル通信**
4. **テスト環境での回帰テスト:**
   * アプリケーションが主に使用する主要クエリ（特にウィンドウ関数、IN/NOT IN句、外部データアクセス、例外処理等）を、アップデート後のデータベーステスト環境で稼働させ、エラーや結果の不整合が起きないか疎通確認を行います。
