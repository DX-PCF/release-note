# PostgreSQL 14.24 リリースノート 変更点・影響度評価一覧

- **対象バージョン**: PostgreSQL 14.24
- **リリース日**: 2026-08-13
- **公式ドキュメント**: [PostgreSQL 14.24 Release Notes](https://www.postgresql.org/docs/release/14.24/)
- **PostgreSQL 14.X系列 EOL予定**: **2026年11月**
- **総項目数**: 84 件（移行要件 1件 ＋ 変更点 83件）

## 影響度サマリ集計

| 区分 | あり (要対応/確認) | 条件付きあり (特定機能利用時) | なし | 合計 |
| :--- | :---: | :---: | :---: | :---: |
| **インフラ影響** | **31** | **8** | **45** | 84 |
| **アプリ影響** | **10** | **36** | **38** | 84 |

---

## 変更点一覧インデックス

| No. | 大分類 | CVE番号 | 項目名・概要 | インフラ影響 | アプリ影響 |
| :---: | :--- | :---: | :--- | :---: | :---: |
| 移行要件 | 移行・前提条件 | - | [バージョン14.24への移行要件・注意事項](#item-0) | **あり** | 条件付きあり |
| 1 | セキュリティ (CVE) | CVE-2026-6471 | [論理デコーディング出力プラグインのホワイトリスト制限](#item-1) | **あり** | 条件付きあり |
| 2 | セキュリティ (CVE) | CVE-2026-14663 | [contrib/pgcryptoにおける非対応暗号検出と復号エラー化](#item-2) | 条件付きあり | **あり** |
| 3 | セキュリティ (CVE) | CVE-2026-6464 | [psqlにおけるCOPY FROM STDIN失敗時の後続インラインデータスキップ](#item-3) | 条件付きあり | 条件付きあり |
| 4 | セキュリティ (CVE) | CVE-2026-16239 | [EXECUTE/FETCH実行ポータルの出力行型クロスチェック](#item-4) | なし | なし |
| 5 | セキュリティ (CVE) | CVE-2026-14669 | [to_char()における長いタイムゾーン略称によるバッファオーバーラン修正](#item-5) | なし | なし |
| 6 | セキュリティ (CVE) | CVE-2026-14664 | [正規表現一致・分割関数におけるバッファオーバーラン修正](#item-6) | なし | 条件付きあり |
| 7 | セキュリティ (CVE) | CVE-2026-18024 | [不正入力に対するascii()関数の堅牢化](#item-7) | なし | なし |
| 8 | セキュリティ (CVE) | CVE-2026-16238 | [pg_restore_attribute_stats()におけるマルチレンジ型処理修正](#item-8) | なし | なし |
| 9 | セキュリティ (CVE) | CVE-2026-14668 | [scalarineqsel()におけるTID型定数チェックの追加](#item-9) | なし | なし |
| 10 | セキュリティ (CVE) | CVE-2026-14662 | [tsvector/tsqueryの極端に長い値に対する制限の厳格化](#item-10) | なし | 条件付きあり |
| 11 | セキュリティ (CVE) | CVE-2026-14679 | [FUNC_MAX_ARGS引数上限の強制と関連箇所の修正](#item-11) | なし | 条件付きあり |
| 12 | セキュリティ (CVE) | CVE-2026-14680 | [SQLからのinternal型関数呼び出しの明示的拒否](#item-12) | なし | 条件付きあり |
| 13 | セキュリティ (CVE) | CVE-2026-6469 | [ALTER TABLE再構築時における拡張統計オブジェクトの所有者保持](#item-13) | 条件付きあり | なし |
| 14 | セキュリティ (CVE) | CVE-2026-15741 | [EXTRACT()関数逆パース時のフィールド名クォート処理](#item-14) | **あり** | なし |
| 15 | セキュリティ (CVE) | CVE-2026-6470 | [CREATE TYPE AS RANGE等における型USAGE権限チェックの厳格化](#item-15) | 条件付きあり | 条件付きあり |
| 16 | セキュリティ (CVE) | CVE-2026-14666 | [ロール変更後のロール依存キャッシュプラン無効化（RLS対応）](#item-16) | なし | **あり** |
| 17 | セキュリティ (CVE) | CVE-2026-14681 | [直接SSL接続後のGSSEncRequest拒否](#item-17) | **あり** | なし |
| 18 | セキュリティ (CVE) | CVE-2026-14672 | [模擬SCRAM認証シークレットの再現性向上（ユーザー列挙対策）](#item-18) | なし | なし |
| 19 | セキュリティ (CVE) | CVE-2026-16241 | [ecpgにおける不正byteaデータによる境界外書き込み修正](#item-19) | なし | 条件付きあり |
| 20 | セキュリティ (CVE) | CVE-2026-18408 | [psqlの\unrestrictコマンド引数でのバッククォート展開禁止](#item-20) | **あり** | なし |
| 21 | セキュリティ (CVE) | CVE-2026-19385 | [pg_dumpにおけるprotrftypes上限仮定の撤廃](#item-21) | 条件付きあり | なし |
| 22 | セキュリティ (CVE) | CVE-2026-14670 | [PL/Perlのtied配列・ハッシュに対する堅牢化](#item-22) | なし | 条件付きあり |
| 23 | セキュリティ (CVE) | CVE-2026-14677 | [PL/PerlおよびPL/Tclのメモリ割り当て計算における整数オーバーフロー修正](#item-23) | なし | 条件付きあり |
| 24 | セキュリティ (CVE) | CVE-2026-14673 | [contrib/amcheckのインデックス式実行前search_path制限](#item-24) | 条件付きあり | なし |
| 25 | セキュリティ (CVE) | CVE-2026-15742 | [contrib/fuzzystrmatchのlevenshtein()における整数オーバーフロー修正](#item-25) | なし | 条件付きあり |
| 26 | セキュリティ (CVE) | CVE-2026-14676 | [contrib/pg_stat_statementsにおけるバッファオーバーラン修正](#item-26) | **あり** | なし |
| 27 | セキュリティ (CVE) | CVE-2026-14678 | [contrib/pg_trgmのGiST picksplitにおけるデータ型エラー修正](#item-27) | 条件付きあり | なし |
| 28 | セキュリティ (CVE) | CVE-2026-14671 | [contrib/refintにおけるプランキャッシュの廃止](#item-28) | なし | 条件付きあり |
| 29 | レプリケーション・WAL | - | [古いマイナーバージョン生成WAL再生時の自己デッドロック解消](#item-29) | **あり** | なし |
| 30 | プランナ・クエリ実行 | - | [非同期Appendプランノード再スキャン時の非同期読み取り誤処理修正](#item-30) | なし | 条件付きあり |
| 31 | プランナ・クエリ実行 | - | [RANGEパーティションにおけるDEFAULTパーティション除外バグの修正](#item-31) | なし | **あり** |
| 32 | プランナ・クエリ実行 | - | [value IN (array)式に対する空配列チェック不備の修正](#item-32) | なし | **あり** |
| 33 | プランナ・クエリ実行 | - | [コンテナデータ型の等価比較におけるハッシュ可能性チェック漏れ修正](#item-33) | なし | 条件付きあり |
| 34 | プランナ・クエリ実行 | - | [多階層パーティションにおけるDROP EXPRESSIONの動作修正](#item-34) | なし | 条件付きあり |
| 35 | プランナ・クエリ実行 | - | [ルールの名前を_RETURNに変更することの禁止](#item-35) | なし | 条件付きあり |
| 36 | インデックス・ストレージ | - | [遅延一意制約に対するREINDEX CONCURRENTLYの誤エラー修正](#item-36) | **あり** | なし |
| 37 | データ型・組込関数 | - | [to_date()におけるローカライズされた月名/曜日名の大文字小文字処理修正](#item-37) | なし | 条件付きあり |
| 38 | データ型・組込関数 | - | [ハングルU+11A7に対する不正なNFC再合成の修正](#item-38) | なし | 条件付きあり |
| 39 | データ型・組込関数 | - | [大文字小文字を区別しないsynonym辞書における語彙素切り捨て防止](#item-39) | なし | 条件付きあり |
| 40 | データ型・組込関数 | - | [hash_record_extended()における未初期化引数のタイポ修正](#item-40) | なし | 条件付きあり |
| 41 | データ型・組込関数 | - | [satisfies_hash_partition()のVARIADIC NULLによるクラッシュ防止](#item-41) | なし | 条件付きあり |
| 42 | データ型・組込関数 | - | [tsvector_filter()等での不正なweightエラー出力の改善](#item-42) | なし | 条件付きあり |
| 43 | データ型・組込関数 | - | [xpath()関数における名前空間ノード処理の修正](#item-43) | なし | 条件付きあり |
| 44 | データ型・組込関数 | - | [jsonbの@?および@@演算子での未定義jsonpath変数をエラーとして処理](#item-44) | なし | **あり** |
| 45 | データ型・組込関数 | - | [最小のmoney値を-1で除算した際のマシン依存挙動の解消](#item-45) | なし | 条件付きあり |
| 46 | データ型・組込関数 | - | [全文検索辞書キャッシュ作成途中のOOM発生後クラッシュ修正](#item-46) | なし | なし |
| 47 | データ型・組込関数 | - | [不正なispell/hunspell辞書ファイル処理時のメモリ安全性修正](#item-47) | 条件付きあり | なし |
| 48 | インデックス・ストレージ | - | [GINインデックスのposting-treeクリーンアップでのキャンセル・遅延尊重](#item-48) | **あり** | なし |
| 49 | インデックス・ストレージ | - | [GiST/SP-GiSTインデックスオンリースキャン時のタプル誤デコード修正](#item-49) | なし | 条件付きあり |
| 50 | インデックス・ストレージ | - | [ディレクトリ作成時の並行作成エラー許容](#item-50) | **あり** | なし |
| 51 | インデックス・ストレージ | - | [依存オブジェクトへの共有ロック獲得による孤立依存の防止](#item-51) | **あり** | 条件付きあり |
| 52 | インデックス・ストレージ | - | [空B-treeインデックスに対するSERIALIZABLE競合検出の競合状態修正](#item-52) | なし | **あり** |
| 53 | インデックス・ストレージ | - | [同一ロックグループプロセスの同時終了時競合状態（PANIC回避）修正](#item-53) | **あり** | なし |
| 54 | レプリケーション・WAL | - | [タイムラインジャンプ時のWALレシーバー接続文字列一時露出の防止](#item-54) | **あり** | なし |
| 55 | レプリケーション・WAL | - | [論理レプリケーション受信タプルの列数実行時チェックの追加](#item-55) | **あり** | なし |
| 56 | レプリケーション・WAL | - | [構築されたレプリケーションコマンド内パラメータのクォート処理改善](#item-56) | **あり** | なし |
| 57 | レプリケーション・WAL | - | [空のPREPAREDトランザクションの論理デコーディング修正](#item-57) | **あり** | なし |
| 58 | レプリケーション・WAL | - | [アーカイブフォールバック後のカスケードスタンバイ再接続失敗修正](#item-58) | **あり** | なし |
| 59 | レプリケーション・WAL | - | [エフェメラルレプリケーションスロット破棄時の競合状態回避](#item-59) | **あり** | なし |
| 60 | レプリケーション・WAL | - | [論理レプリケーション同期時のpg_stat_progress_copyスタール表示修正](#item-60) | **あり** | なし |
| 61 | 言語・クライアント | - | [PL/Perlにおける不正な配列オブジェクト処理時のNULLポインタ参照修正](#item-61) | なし | 条件付きあり |
| 62 | 言語・クライアント | - | [PL/Pythonにおけるシーケンス・マッピングオブジェクトのエラーチェック適正化](#item-62) | なし | 条件付きあり |
| 63 | 言語・クライアント | - | [libpqのpqReadData()で復号バッファの保留バイトを完全に排出するよう修正](#item-63) | **あり** | **あり** |
| 64 | 言語・クライアント | - | [libpqにおける30000バイト超のParameterDescriptionメッセージ受入](#item-64) | なし | 条件付きあり |
| 65 | 言語・クライアント | - | [ecpgのGET/SET DESCRIPTOR文での複数ヘッダー項目指定を拒否](#item-65) | なし | 条件付きあり |
| 66 | 言語・クライアント | - | [psqlの拡張表示フォーマット（\x）における行幅の統一](#item-66) | なし | なし |
| 67 | 言語・クライアント | - | [psqlの\l+コマンドにおけるDBサイズ表示権限チェックの修正](#item-67) | **あり** | なし |
| 68 | 言語・クライアント | - | [psqlの\dfコマンドのタブ補完でプロシージャも対象とするよう改善](#item-68) | なし | なし |
| 69 | 言語・クライアント | - | [pg_recvlogicalの出力ファイルに対するグループ読み取り権限適用](#item-69) | **あり** | なし |
| 70 | 拡張モジュール (contrib) | - | [contrib/amcheckにおけるショートヘッダーvarlenaデータの適切な処理](#item-70) | **あり** | なし |
| 71 | 拡張モジュール (contrib) | - | [contrib/btree_gistのfloat4/float8におけるNaN処理修正](#item-71) | **あり** | **あり** |
| 72 | 拡張モジュール (contrib) | - | [contrib/btree_gistの不等価演算子（<>）検索時の誤処理修正](#item-72) | なし | **あり** |
| 73 | 拡張モジュール (contrib) | - | [hstore/jsonbのPL/Perl・PL/Python連携における再帰・ループガード](#item-73) | なし | 条件付きあり |
| 74 | 拡張モジュール (contrib) | - | [contrib/intarrayにおける統計カタログキャッシュ解放漏れ修正](#item-74) | **あり** | なし |
| 75 | 拡張モジュール (contrib) | - | [contrib/ltreeにおける比較時の整数オーバーフロー修正](#item-75) | **あり** | **あり** |
| 76 | 拡張モジュール (contrib) | - | [contrib/pg_surgeryの配列境界外書き込み修正](#item-76) | **あり** | なし |
| 77 | 拡張モジュール (contrib) | - | [contrib/pg_surgeryにおける64K超のTID配列での無限ループ回避](#item-77) | **あり** | なし |
| 78 | 拡張モジュール (contrib) | 関連: CVE-2026-6637 | [contrib/refintのcheck_foreign_key()におけるNULLポインタ参照修正](#item-78) | なし | 条件付きあり |
| 79 | 拡張モジュール (contrib) | - | [contrib/segのチルダ（~）確実性インジケータ出力修正](#item-79) | なし | 条件付きあり |
| 80 | 拡張モジュール (contrib) | - | [contrib/xml2のxpath_nodeset()における名前空間ノードクラッシュ修正](#item-80) | なし | 条件付きあり |
| 81 | ビルド・プラットフォーム | - | [Visual Studio 2026によるPostgreSQLビルドのサポート](#item-81) | **あり** | なし |
| 82 | ビルド・プラットフォーム | - | [OpenSSL 4によるPostgreSQLビルドのサポート](#item-82) | **あり** | なし |
| 83 | ビルド・プラットフォーム | - | [タイムゾーンデータファイルのtzdata release 2026cへの更新](#item-83) | **あり** | 条件付きあり |

---

## 変更点・影響度評価 詳細

<a id="item-0"></a>

### [移行要件] バージョン14.24への移行要件・注意事項

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 移行・前提条件 |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- バイナリ更新とサービス再起動のみで適用可能（ダンプ/リストア不要）。
- btree_gist（float型でNaN含む可能性あり）および ltree（14,653ラベル超）利用環境では REINDEX 計画が必要。
- 論理レプリケーションでサードパーティプラグイン利用時は output_plugin_libraries の事前設定が必要。
- 2026年11月の14.X系EOLに向けた上位バージョン（16/17等）への移行計画が必要。

#### アプリ影響・対応策
- pgcryptoで古い暗号（blowfish/3des等）を使用している場合、復号不可となるため救済オプション対応およびデータ再暗号化が必要。
- 全文検索や特定インデックスクエリの挙動確認が必要。

#### 英語原文 (Original English)
```text
A dump/restore is not required for those running 14.X.

However, the first three security entries below describe configuration adjustments and data cleanups that you may need to make after updating.

Also, if you use contrib/btree_gist or contrib/ltree, you may need to reindex indexes made with those extensions; see the relevant entries below.

Also, if you are upgrading from a version earlier than 14.19, see Section&nbsp;E.6.
```

#### 日本語翻訳 (Japanese Translation)
> 14.X系を実行している環境では、ダンプ/リストアは不要です。

> ただし、後述の最初の3つのセキュリティ項目には、更新後に実施が必要となる可能性のある設定調整およびデータのクリーンアップについて記載されています。

> また、contrib/btree_gist または contrib/ltree を使用している場合、それらの拡張機能で作成されたインデックスの再構築（REINDEX）が必要となる可能性があります。詳細については該当する後述の項目を参照してください。

> さらに、14.19以前のバージョンからアップグレードする場合は、セクションE.6を参照してください。

> なお、PostgreSQLコミュニティは2026年11月をもって14.Xリリース系列に対するアップデートのリリースを停止します。ユーザーは速やかにより新しいリリースブランチにアップデートすることが推奨されます。

---

<a id="item-1"></a>

### [No.1] 論理デコーディング出力プラグインのホワイトリスト制限

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-6471` |
| **インフラ影響** | **あり** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 【要設定確認】外部CDCツール（Debezium等）やサードパーティ製論理レプリケーションプラグイン（wal2json, decoderbufs等）を利用している場合、postgresql.conf に `output_plugin_libraries = 'pgoutput, test_decoding, <プラグイン名>'` を追加し、リロード/再起動が必要です。未設定の場合レプリケーション接続が拒否されます。

#### アプリ影響・対応策
- 通常のアプリクエリへの影響はありませんが、論理レプリケーションやCDC連携による外部データ同期システムがある場合、プラグインが許可されていないと同期停止が発生します。

#### 英語原文 (Original English)
```text
Restrict logical decoding output plugins to the set specified by a new server parameter output_plugin_libraries (Jacob Champion)

Previously, a replication user could select any loadable library for logical decoding, allowing exploits of various sorts. To allow locking this down without breaking setups that worked before, introduce a whitelist of allowed output plugins.

By default, only the output plugins shipped as part of PostgreSQL (pgoutput and test_decoding) are included in output_plugin_libraries. Installations that rely on other output plugins must add them after updating the server, for example

output_plugin_libraries = 'pgoutput, test_decoding, my_trusted_decoder'

          Additionally, pg_upgrade --check will fail if the output_plugin_libraries parameter on the new cluster does not permit the plugins of logical replication slots on the old cluster, when migrating from versions 17 and later. Make necessary additions to the new cluster's setting before performing pg_upgrade.

The PostgreSQL Project thanks Vladimir Tokarev and Yu Kunpeng for reporting this problem. (CVE-2026-6471)
```

#### 日本語翻訳 (Japanese Translation)
> 論理デコーディング出力プラグインを、新しいサーバーパラメータ output_plugin_libraries で指定されたセットに制限します。(Jacob Champion)

> 従来、レプリケーションユーザーは論理デコーディング用にロード可能な任意のライブラリを選択することができ、さまざまな種類の悪用が可能でした。これまで動作していた構成を壊すことなくこれを厳格に制限できるようにするため、許可された出力プラグインのホワイトリストを導入しました。

> デフォルトでは、PostgreSQLの一部として同梱されている出力プラグイン（pgoutput および test_decoding）のみが output_plugin_libraries に含まれています。他の出力プラグインに依存している環境では、サーバーをアップデートした後にそれらをパラメータに追加する必要があります。例えば以下の通りです：

> output_plugin_libraries = 'pgoutput, test_decoding, my_trusted_decoder'

> さらに、バージョン17以降から移行する場合、新クラスタ上の output_plugin_libraries パラメータが旧クラスタの論理レプリケーションスロットのプラグインを許可していなければ、pg_upgrade --check は失敗します。pg_upgrade を実行する前に、新クラスタの設定に必要な追加を行ってください。

> PostgreSQLプロジェクトは、この問題を報告してくださった Vladimir Tokarev 氏および Yu Kunpeng 氏に感謝します。(CVE-2026-6471)

---

<a id="item-2"></a>

### [No.2] contrib/pgcryptoにおける非対応暗号検出と復号エラー化

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14663` |
| **インフラ影響** | **条件付きあり** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- OpenSSL 3.x以降のFIPSモード運用やレガシープロバイダ設定の確認が必要です。DBサーバー側の設定変更自体は必須ではありませんが、該当データが存在する場合の復旧方針策定が必要です。

#### アプリ影響・対応策
- 【要データ確認】pgcrypto の PGP 暗号化で非推奨アルゴリズム（blowfish, twofish, cast5, 3des）を使用している場合、復号時にエラーが発生します。アプリ側で `ignore-cipher-failure=1` を指定して復号した上で、AESなどの現行アルゴリズムへ移行・再暗号化するバッチ改修が必要です。

#### 英語原文 (Original English)
```text
Fix contrib/pgcrypto's PGP encryption to detect unsupported ciphers (Daniel Gustafsson)

Previously, if OpenSSL rejected the requested cipher (for example, because it is running in FIPS mode, or the legacy provider hasn't been loaded), pgcrypto failed to notice the failure and simply XOR'd the non-encrypted block with the plaintext, rendering the “encryption” trivially breakable. This will typically occur with deprecated or non-FIPS cipher algorithms (cipher-algo=blowfish/bf, twofish, cast5, or 3des).

By default, pgcrypto will now fail to decrypt any messages that were affected in this way. To allow retrieval of such data, a new option ignore-cipher-failure has been added to pgp_pub_decrypt() and pgp_sym_decrypt(). Setting ignore-cipher-failure=1 will restore their previous behavior, allowing the faulty encryption wrapper to be stripped off:

pgp_sym_decrypt(encrypted_column, any key, 'ignore-cipher-failure=1')

          Once the affected messages are identified and stripped of their wrappers, they can then be re-encrypted with a modern algorithm. It is important however that the behavior of OpenSSL be the same as it was when the faulty messages were created: if the set of unsupported algorithms is not the same, this approach will not work. See the documentation for ignore-cipher-failure.

The PostgreSQL Project thanks Shishir Sharma for reporting this problem. (CVE-2026-14663)
```

#### 日本語翻訳 (Japanese Translation)
> contrib/pgcrypto の PGP 暗号化において非対応の暗号を検出するよう修正しました。(Daniel Gustafsson)

> 従来、OpenSSLが要求された暗号を拒否した場合（例えば、FIPSモードで動作している場合や、レガシープロバイダがロードされていない場合など）、pgcrypto はその失敗を検知できず、暗号化されていないブロックと平文を単にXOR演算して出力していたため、その「暗号化」は極めて容易に解読可能な状態になっていました。これは通常、非推奨または非FIPSの暗号アルゴリズム（cipher-algo=blowfish/bf、twofish、cast5、または 3des）で発生します。

> デフォルトで、pgcrypto はこのように影響を受けたメッセージの復号を失敗（エラー）とするようになります。このようなデータを救出・取得できるようにするため、pgp_pub_decrypt() および pgp_sym_decrypt() に新しいオプション ignore-cipher-failure が追加されました。ignore-cipher-failure=1 を設定すると以前の動作が再現され、欠陥のある暗号化ラッパーを剥ぎ取ることが可能になります：

> pgp_sym_decrypt(encrypted_column, any key, 'ignore-cipher-failure=1')

> 影響を受けたメッセージを特定してそのラッパーを剥ぎ取った後は、現代的なアルゴリズムで再暗号化できます。ただし、欠陥のあるメッセージが作成されたときと OpenSSL の動作が同一であることが重要です。非対応アルゴリズムのセットが同じでない場合、この手法は機能しません。ignore-cipher-failure のドキュメントを参照してください。

> PostgreSQLプロジェクトは、この問題を報告してくださった Shishir Sharma 氏に感謝します。(CVE-2026-14663)

---

<a id="item-3"></a>

### [No.3] psqlにおけるCOPY FROM STDIN失敗時の後続インラインデータスキップ

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-6464` |
| **インフラ影響** | **条件付きあり** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 運用・リストア作業で psql を用いてデータ投入スクリプトを実行する際、テーブル不整合等のエラー発生時に後続データが誤ってSQL実行される二次被害が防止されます。

#### アプリ影響・対応策
- CI/CDやデプロイスクリプト、テストコードで psql 経由で COPY ... FROM STDIN を実行している場合、失敗時の動作が正しくスキップされます。COPY失敗をテストするケースでは `\.` 終端記号の追記が必要です。

#### 英語原文 (Original English)
```text
Fix psql to skip in-line data following a scripted COPY ... FROM STDIN command, even if the COPY fails before sending PGRES_COPY_IN (Tom Lane)

Previously, if a COPY command failed at startup (for instance, because the target table doesn't exist) psql would not realize that and would proceed to read the following in-line data as SQL commands. In the best case that's wrong and in the worst case it's a SQL-injection hazard. Teach psql to recognize syntactically-valid COPY ... FROM STDIN commands and to skip data on its own authority if the server doesn't respond with PGRES_COPY_IN.

While this fix is unlikely to affect any production SQL scripts, test scripts might intentionally exercise failing COPY ... FROM STDIN commands. Those will need to gain a \. data terminator line after each such command.

The PostgreSQL Project thanks Alexander Lakhin for reporting this problem. (CVE-2026-6464)
```

#### 日本語翻訳 (Japanese Translation)
> スクリプト化された COPY ... FROM STDIN コマンドにおいて、COPY が PGRES_COPY_IN を送信する前に失敗した場合でも、後続のインラインデータをスキップするよう psql を修正しました。(Tom Lane)

> 従来、COPY コマンドが起動時に失敗した場合（例えば対象テーブルが存在しないなど）、psql はそれに気づかず、後続のインラインデータを SQL コマンドとして読み取って実行してしまっていました。これは良くても誤作動であり、最悪の場合は SQL インジェクションの危険をもたらします。構文上有効な COPY ... FROM STDIN コマンドを認識し、サーバーが PGRES_COPY_IN で応答しない場合には psql 自身の判断でデータをスキップするよう改修しました。

> この修正が本番の SQL スクリプトに影響を与える可能性は低いですが、テストスクリプトでは意図的に失敗する COPY ... FROM STDIN コマンドを実行している場合があります。そのようなスクリプトでは、該当する各コマンドの後に \. データ終端行を追加する必要があります。

> PostgreSQLプロジェクトは、この問題を報告してくださった Alexander Lakhin 氏に感謝します。(CVE-2026-6464)

---

<a id="item-4"></a>

### [No.4] EXECUTE/FETCH実行ポータルの出力行型クロスチェック

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-16239` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- サーバーメモリ漏洩・任意コード実行脆弱性の解消。設定変更は不要です。

#### アプリ影響・対応策
- 不正な型不一致を伴うポータル操作が遮断されます。通常のアプリケーションクエリには影響ありません。

#### 英語原文 (Original English)
```text
Cross-check the output row type of a portal running EXECUTE or FETCH (Robert Haas)

EXECUTE and FETCH use two portals: an outer one for the statement itself, and an inner one running the query being executed on its behalf. It was previously possible to make the declared row types of the two portals diverge, leading to server memory disclosure and arbitrary code execution.

The PostgreSQL Project thanks Ben Morris (in collaboration with Claude and Anthropic Research) and Peter Geoghegan for reporting this problem. (CVE-2026-16239)
```

#### 日本語翻訳 (Japanese Translation)
> EXECUTE または FETCH を実行するポータルの出力行型をクロスチェック（相互検証）するよう修正しました。(Robert Haas)

> EXECUTE および FETCH は2つのポータルを使用します。文自体のための外部ポータルと、その代理として実行されるクエリを実行する内部ポータルです。従来はこれら2つのポータルの宣言された行型を乖離させることが可能であり、サーバーメモリの漏洩や任意のコード実行につながる脆弱性がありました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Ben Morris 氏（Claude および Anthropic Research との共同作業）ならびに Peter Geoghegan 氏に感謝します。(CVE-2026-16239)

---

<a id="item-5"></a>

### [No.5] to_char()における長いタイムゾーン略称によるバッファオーバーラン修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14669` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- サーバークラッシュおよび任意コード実行脆弱性の解消。インフラ変更なし。

#### アプリ影響・対応策
- to_char() でタイムゾーン書式を利用している場合でも安全に処理されるようになります。アプリ改修不要。

#### 英語原文 (Original English)
```text
Fix buffer overrun with long time zone abbreviation in to_char() (Tom Lane)

This can easily crash the server, and exploits leading to arbitrary code execution have been reported.

The PostgreSQL Project thanks Hcamael, Amjad Shahzad, Tan Zhen of AntAISecurityLab, Tomer Fichman, Zheng Yu, Amy Burnett (OpenAI Codex Security), Rick de Jager, Heewon Song, Sylvie Mayer, Aleksander Alekseev, and Hillai Ben Sasson for reporting this problem. (CVE-2026-14669)
```

#### 日本語翻訳 (Japanese Translation)
> to_char() における長いタイムゾーン略称によるバッファオーバーランを修正しました。(Tom Lane)

> これによりサーバーが容易にクラッシュする可能性があり、任意のコード実行に至る悪用事例が報告されていました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Hcamael 氏、Amjad Shahzad 氏、AntAISecurityLab の Tan Zhen 氏、Tomer Fichman 氏、Zheng Yu 氏、Amy Burnett 氏（OpenAI Codex Security）、Rick de Jager 氏、Heewon Song 氏、Sylvie Mayer 氏、Aleksander Alekseev 氏、および Hillai Ben Sasson 氏に感謝します。(CVE-2026-14669)

---

<a id="item-6"></a>

### [No.6] 正規表現一致・分割関数におけるバッファオーバーラン修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14664` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- サーバープロセスのメモリ破壊・クラッシュ防止。

#### アプリ影響・対応策
- 外部入力由来の不正バイト列が正規表現関数に渡された場合の脆弱性が解消され、安全にエラー処理されるようになります。

#### 英語原文 (Original English)
```text
Fix buffer overrun in regexp match/split functions (Masahiko Sawada)

If passed invalidly-encoded data, these functions could write past the end of their conversion buffer.

The PostgreSQL Project thanks Francesco Verardi for reporting this problem. (CVE-2026-14664)
```

#### 日本語翻訳 (Japanese Translation)
> 正規表現の一致および分割関数におけるバッファオーバーランを修正しました。(Masahiko Sawada)

> 不正にエンコードされたデータが渡された場合、これらの関数（regexp_match, regexp_split_to_table等）は変換バッファの終端を超えて書き込みを行ってしまう可能性がありました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Francesco Verardi 氏に感謝します。(CVE-2026-14664)

---

<a id="item-7"></a>

### [No.7] 不正入力に対するascii()関数の堅牢化

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-18024` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- メモリ情報漏洩脆弱性の解消。

#### アプリ影響・対応策
- 通常のアプリケーション利用に影響ありません。

#### 英語原文 (Original English)
```text
Harden the ascii() function against invalid input (Michael Paquier)

By supplying invalidly-encoded input, this function could be coaxed to read and return a few bytes of data that it shouldn't. In assert-enabled builds, its assertions could be triggered too.

The PostgreSQL Project thanks Hcamael for reporting this problem. (CVE-2026-18024)
```

#### 日本語翻訳 (Japanese Translation)
> 不正な入力に対して ascii() 関数を堅牢化しました。(Michael Paquier)

> 不正にエンコードされた入力を与えることで、本来返すべきでない数バイトのデータを読み取らせて返却させることが可能でした。アサート（Assert）が有効なビルドでは、アサーション違反を引き起こすことも可能でした。

> PostgreSQLプロジェクトは、この問題を報告してくださった Hcamael 氏に感謝します。(CVE-2026-18024)

---

<a id="item-8"></a>

### [No.8] pg_restore_attribute_stats()におけるマルチレンジ型処理修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-16238` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 統計情報の復元処理が正常化されます。

#### アプリ影響・対応策
- マルチレンジ型列を持つテーブルの統計情報復元が正確になります。

#### 英語原文 (Original English)
```text
Fix multirange type handling in pg_restore_attribute_stats() (OpenAI Security Research Team)

pg_restore_attribute_stats() treated multirange types just like their underlying range type. This works correctly for the bounds histogram, but it was wrong for all the other statistics kinds.

The PostgreSQL Project thanks Amy Burnett (OpenAI Codex Security) for reporting this problem. (CVE-2026-16238)
```

#### 日本語翻訳 (Japanese Translation)
> pg_restore_attribute_stats() におけるマルチレンジ型の処理を修正しました。(OpenAI Security Research Team)

> pg_restore_attribute_stats() は、マルチレンジ型をその基底となるレンジ型とまったく同様に扱っていました。これは境界ヒストグラムについては正しく機能しますが、他のすべての統計情報の種類については誤りでした。

> PostgreSQLプロジェクトは、この問題を報告してくださった Amy Burnett 氏（OpenAI Codex Security）に感謝します。(CVE-2026-16238)

---

<a id="item-9"></a>

### [No.9] scalarineqsel()におけるTID型定数チェックの追加

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14668` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- クラッシュおよびメモリ漏洩脆弱性の解消。

#### アプリ影響・対応策
- 通常のアプリケーション利用に影響ありません。

#### 英語原文 (Original English)
```text
Make scalarineqsel() check that a constant it expects to be of type tid actually is (Tom Lane)

This expectation will hold for all the built-in operators that use this estimator, but a maliciously-constructed operator could violate it, leading to a crash or server memory disclosure.

The PostgreSQL Project thanks Hcamael for reporting this problem. (CVE-2026-14668)
```

#### 日本語翻訳 (Japanese Translation)
> scalarineqsel() が tid 型であると期待する定数が実際にその型であるかを検証するよう修正しました。(Tom Lane)

> この前提はこの推定関数を使用するすべての組み込み演算子において成立しますが、悪意を持って構築された演算子によって違反される可能性があり、クラッシュやサーバーメモリの漏洩につながる恐れがありました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Hcamael 氏に感謝します。(CVE-2026-14668)

---

<a id="item-10"></a>

### [No.10] tsvector/tsqueryの極端に長い値に対する制限の厳格化

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14662` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- サーバーリソース枯渇・メモリ破損防止。

#### アプリ影響・対応策
- 全文検索機能（to_tsvector, to_tsquery等）で仕様上限（2046バイトの語彙素長など）を超える長大な文字列を入力していた場合、厳格にエラーが返されるようになります。

#### 英語原文 (Original English)
```text
Harden tsvector and tsquery code against overly long values (both individual lexemes and total vector/query length) (Tom Lane)

The documented limits were not enforced in all code paths.

The PostgreSQL Project thanks Yuhang Wu, Zhenpeng Lin, Zheng Yu, and Hcamael for reporting these problems. (CVE-2026-14662)
```

#### 日本語翻訳 (Japanese Translation)
> tsvector および tsquery コードを、極端に長い値（個々の語彙素およびベクター/クエリの合計長の両方）に対して堅牢化しました。(Tom Lane)

> ドキュメントに記載されている制限値が、一部のコードパスで強制されていませんでした。

> PostgreSQLプロジェクトは、これらの問題を報告してくださった Yuhang Wu 氏、Zhenpeng Lin 氏、Zheng Yu 氏、および Hcamael 氏に感謝します。(CVE-2026-14662)

---

<a id="item-11"></a>

### [No.11] FUNC_MAX_ARGS引数上限の強制と関連箇所の修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14679` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- パーサーレベルでの境界チェック正常化。

#### アプリ影響・対応策
- 引数が極端に多い（1000個近い）集約関数を動的生成・実行していた場合にパーサーエラーとなります。通常のSQLには影響ありません。

#### 英語原文 (Original English)
```text
Fix various places that mistakenly assumed they would not have to deal with more than FUNC_MAX_ARGS function arguments (Tom Lane)

Notably, the server's actual limit on the number of arguments to an aggregate function is FUNC_MAX_ARGS - 1, but the parser failed to enforce that, creating hazards downstream.

The PostgreSQL Project thanks Zheng Yu, ylwangtju, and Masahiko Sawada for reporting these problems. (CVE-2026-14679)
```

#### 日本語翻訳 (Japanese Translation)
> 関数引数が FUNC_MAX_ARGS を超えることはないと誤認していた各所を修正しました。(Tom Lane)

> 特に、集約関数の引数の数に対するサーバーの実際の制限は FUNC_MAX_ARGS - 1 ですが、パーサーがそれを強制できておらず、後続の処理で危険が生じていました。

> PostgreSQLプロジェクトは、これらの問題を報告してくださった Zheng Yu 氏、ylwangtju 氏、および Masahiko Sawada 氏に感謝します。(CVE-2026-14679)

---

<a id="item-12"></a>

### [No.12] SQLからのinternal型関数呼び出しの明示的拒否

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14680` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 不正な内部ポインタ操作によるメモリ破壊・クラッシュの防止。

#### アプリ影響・対応策
- アプリケーションから internal 型を扱う内部関数を直接呼び出していた場合（非推奨・イレギュラーな利用形態）、エラーとなります。

#### 英語原文 (Original English)
```text
Reject calls from SQL to functions that take or return type internal (Tom Lane)

The existing defenses against doing this have been shown to be insufficient, so add more explicit checks.

The PostgreSQL Project thanks Amy Burnett (OpenAI Codex Security) for reporting this problem. (CVE-2026-14680)
```

#### 日本語翻訳 (Japanese Translation)
> SQLから internal 型を受け取るまたは返す関数への呼び出しを拒否するよう修正しました。(Tom Lane)

> これを防止するための既存の防御策が不十分であることが判明したため、より明示的なチェックを追加しました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Amy Burnett 氏（OpenAI Codex Security）に感謝します。(CVE-2026-14680)

---

<a id="item-13"></a>

### [No.13] ALTER TABLE再構築時における拡張統計オブジェクトの所有者保持

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-6469` |
| **インフラ影響** | **条件付きあり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- DB管理者が ALTER TABLE 等のメンテナンスを実行した際、拡張統計オブジェクトの所有者が管理者ロールに上書きされる問題が是正され、元の所有権が維持されます。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Preserve the ownership of extended statistics objects when they are rebuilt by ALTER TABLE (Masahiko Sawada)

Previously, the role running ALTER TABLE gained ownership of such objects, but that seems inappropriate.

The PostgreSQL Project thanks Noah Misch for reporting this problem. (CVE-2026-6469)
```

#### 日本語翻訳 (Japanese Translation)
> ALTER TABLE によって再構築される際、拡張統計オブジェクトの所有権を保持するよう修正しました。(Masahiko Sawada)

> 従来は ALTER TABLE を実行したロールがそのような統計オブジェクトの所有権を取得していましたが、これは不適切でした。

> PostgreSQLプロジェクトは、この問題を報告してくださった Noah Misch 氏に感謝します。(CVE-2026-6469)

---

<a id="item-14"></a>

### [No.14] EXTRACT()関数逆パース時のフィールド名クォート処理

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-15741` |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- pg_dump によるバックアップおよびリストア時のSQLインジェクション脆弱性が解消されます。

#### アプリ影響・対応策
- EXTRACT(field FROM source) を使用したビューや関数定義が安全にダンプ・リストアされます。

#### 英語原文 (Original English)
```text
When deparsing an EXTRACT() function call, quote the field name if needed (Nathan Bossart)

The parser accepts any string literal as a field name in EXTRACT(), deferring validation to execution. If the call is stored and deparsed (for example during pg_dump), the string body was regurgitated verbatim, allowing SQL injection.

The PostgreSQL Project thanks Ben Morris (in collaboration with Claude and Anthropic Research) for reporting this problem. (CVE-2026-15741)
```

#### 日本語翻訳 (Japanese Translation)
> EXTRACT() 関数呼び出しを逆パース（deparse）する際、必要に応じてフィールド名を引用符で囲む（クォートする）よう修正しました。(Nathan Bossart)

> パーサーは EXTRACT() 内のフィールド名として任意の文字列リテラルを受け付け、検証を実行時まで遅延させます。その呼び出しが保存され逆パースされる際（例えば pg_dump の実行時など）、文字列の本体がそのまま展開されてしまい、SQLインジェクションが可能になっていました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Ben Morris 氏（Claude および Anthropic Research との共同作業）に感謝します。(CVE-2026-15741)

---

<a id="item-15"></a>

### [No.15] CREATE TYPE AS RANGE等における型USAGE権限チェックの厳格化

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-6470` |
| **インフラ影響** | **条件付きあり** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 一般ロールが他スキーマの型を参照してレンジ型や生成列を定義する場合、対象型に対する USAGE 権限の事前付与が必要です。

#### アプリ影響・対応策
- マイグレーションスクリプト等で USAGE 権限のない型を用いてレンジ型等を定義している場合、エラーとなるため GRANT USAGE ON TYPE の付与が必要です。

#### 英語原文 (Original English)
```text
Check for USAGE privilege on data types in places that formerly failed to check that (Nathan Bossart)

CREATE TYPE AS RANGE did not check, nor did ALTER TABLE OF, nor did commands that create stored expressions. These omissions allowed roles without USAGE privilege to nonetheless create objects depending on the type, possibly blocking the type's owner from changing the type later.

The PostgreSQL Project thanks Jingzhou Fu for reporting this problem. (CVE-2026-6470)
```

#### 日本語翻訳 (Japanese Translation)
> 従来チェックが漏れていた箇所において、データ型に対する USAGE 権限をチェックするよう修正しました。(Nathan Bossart)

> CREATE TYPE AS RANGE ではチェックが行われておらず、ALTER TABLE OF や、格納された式を作成するコマンドでもチェックされていませんでした。これらの見落としにより、USAGE 権限を持たないロールであってもその型に依存するオブジェクトを作成することができ、型の所有者が後から型を変更することを妨害できる可能性がありました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Jingzhou Fu 氏に感謝します。(CVE-2026-6470)

---

<a id="item-16"></a>

### [No.16] ロール変更後のロール依存キャッシュプラン無効化（RLS対応）

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14666` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- RLS利用環境でのセキュリティ保護。

#### アプリ影響・対応策
- Row-Level Security (RLS) を利用してマルチテナント制御や権限分離を行っているアプリケーションにおいて、SET ROLE等でロールを切り替えた際に古いロールの実行計画が漏洩・流用される重大な脆弱性が解消されます。

#### 英語原文 (Original English)
```text
Invalidate role-dependent cached plans after role changes (Ilya Staroverov, Shinya Kato, Nathan Bossart)

Role membership, role attribute, and database ownership changes may impact the expected behavior of row-level security policies, but previously we'd continue to use cached plans that were made according to the old state of affairs.

The PostgreSQL Project thanks Ilya Staroverov and Shinya Kato for reporting this problem. (CVE-2026-14666)
```

#### 日本語翻訳 (Japanese Translation)
> ロールの変更後に、ロールに依存するキャッシュされた実行計画を無効化するよう修正しました。(Ilya Staroverov, Shinya Kato, Nathan Bossart)

> ロールのメンバーシップ、ロールの属性、およびデータベースの所有権の変更は、行レベルセキュリティ（RLS）ポリシーの期待される動作に影響を与える可能性がありますが、従来は古い状態に基づいて作成されたキャッシュプランを継続して使用していました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Ilya Staroverov 氏および Shinya Kato 氏に感謝します。(CVE-2026-14666)

---

<a id="item-17"></a>

### [No.17] 直接SSL接続後のGSSEncRequest拒否

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14681` |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- pg_hba.conf による認証および暗号化ポリシーの厳格な適用。SSLとGSSAPIを併用している環境において意図通りのアクセス制御が保証されます。

#### アプリ影響・対応策
- 通常のクライアント接続には影響ありません。

#### 英語原文 (Original English)
```text
Reject GSSEncRequest after direct SSL connection (Michael Paquier)

After establishing a TLS-encrypted connection, the server would still accept a request for GSSAPI encryption. If that succeeded, the connection would proceed using TLS encryption, but it would look like a GSS connection to the pg_hba rules. Thus, a pg_hba policy intending to disallow TLS would not be enforced correctly.

The PostgreSQL Project thanks p4p3r for reporting this problem. (CVE-2026-14681)
```

#### 日本語翻訳 (Japanese Translation)
> 直接のSSL接続が確立した後に GSSEncRequest が送られた場合、これを拒否するよう修正しました。(Michael Paquier)

> TLS暗号化接続が確立された後でも、サーバーはGSSAPI暗号化の要求を受け入れていました。それが成功すると接続はTLS暗号化を使用して継続されますが、pg_hba ルールからはGSS接続のように見えてしまいます。そのため、TLSを禁止することを意図した pg_hba ポリシーが正しく強制されませんでした。

> PostgreSQLプロジェクトは、この問題を報告してくださった p4p3r 氏に感謝します。(CVE-2026-14681)

---

<a id="item-18"></a>

### [No.18] 模擬SCRAM認証シークレットの再現性向上（ユーザー列挙対策）

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14672` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- ユーザー列挙攻撃（タイミング攻撃・反復回数差異によるユーザー存在検知）に対する耐性が向上します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Make mock SCRAM authentication secrets more plausible (Nathan Bossart)

If a SCRAM login is attempted against a role that doesn't exist or doesn't have a SCRAM secret, we generate a mock secret and carry out the authentication handshake anyway, to avoid revealing these facts to an attacker. But the mock secret was made with a fixed iteration count, which in itself can be an observable response discrepancy. Use the configuration setting scram_iterations instead, to make the mock secret look more like the installation's real secrets.

The PostgreSQL Project thanks Radim Marek for reporting this problem. (CVE-2026-14672)
```

#### 日本語翻訳 (Japanese Translation)
> 模擬SCRAM認証シークレットをより本物らしく（妥当に）生成するよう改善しました。(Nathan Bossart)

> 存在しないロールや SCRAM シークレットを持たないロールに対して SCRAM ログインが試行された場合、攻撃者にこれらの事実を漏らさないようにするため、模擬シークレットを生成して認証ハンドシェイクを継続します。しかし、従来の模擬シークレットは固定の反復回数で作成されていたため、それ自体が観測可能な応答の差異となっていました。設定パラメータ scram_iterations を代わりに使用することで、インストール環境の実際のシークレットにより近い外見を持つようにしました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Radim Marek 氏に感謝します。(CVE-2026-14672)

---

<a id="item-19"></a>

### [No.19] ecpgにおける不正byteaデータによる境界外書き込み修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-16241` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- クライアントライブラリの安定性向上。

#### アプリ影響・対応策
- ecpg を用いてビルドされたC言語アプリケーションがある場合、最新の ecpg ライブラリとリンクし直す（再コンパイル/再リンクする）ことが推奨されます。

#### 英語原文 (Original English)
```text
Fix out-of-bounds writes in ecpg applications caused by invalid bytea data received from the server (Michael Paquier)

ecpg assumed without checking that any bytea value must begin with \x. A broken or malicious server might send a string shorter than 2 bytes, resulting in memory clobber in the application.

The PostgreSQL Project thanks ylwangtju for reporting this problem. (CVE-2026-16241)
```

#### 日本語翻訳 (Japanese Translation)
> サーバーから受信した不正な bytea データによって ecpg アプリケーションで発生する境界外書き込みを修正しました。(Michael Paquier)

> ecpg は検証を行うことなく、すべての bytea 値が必ず \x で始まると前提していました。破損したサーバーや悪意のあるサーバーが2バイト未満の文字列を送信した場合、アプリケーション内でメモリ破壊が発生していました。

> PostgreSQLプロジェクトは、この問題を報告してくださった ylwangtju 氏に感謝します。(CVE-2026-16241)

---

<a id="item-20"></a>

### [No.20] psqlの\unrestrictコマンド引数でのバッククォート展開禁止

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-18408` |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 管理者端末やリストア環境において、悪意のあるダンプファイルを psql で流し込む際のリモートコード実行（RCE）リスクが完全に遮断されます。

#### アプリ影響・対応策
- アプリケーションへの直接の影響はありません。

#### 英語原文 (Original English)
```text
Do not do backquote expansion on the argument of psql's \unrestrict command (Nathan Bossart)

This oversight in the fix for CVE-2025-8714 allows a malicious server to inject shell commands into plain-text dump output that will be run at restore time on the machine running psql, the exact scenario that CVE-2025-8714 intended to prevent.

The PostgreSQL Project thanks Lucas Velgus, Filip Janus, and Daniel Bakker for reporting this problem. (CVE-2026-18408)
```

#### 日本語翻訳 (Japanese Translation)
> psql の \unrestrict コマンドの引数においてバッククォート展開を行わないよう修正しました。(Nathan Bossart)

> CVE-2025-8714 の修正におけるこの見落としにより、悪意のあるサーバーがプレーンテキストのダンプ出力にシェルコマンドを注入することが可能になっていました。そのコマンドは、psql を実行しているマシン上でリストア時に実行されてしまうため、まさに CVE-2025-8714 が防止しようとしていたシナリオが発生していました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Lucas Velgus 氏、Filip Janus 氏、および Daniel Bakker 氏に感謝します。(CVE-2026-18408)

---

<a id="item-21"></a>

### [No.21] pg_dumpにおけるprotrftypes上限仮定の撤廃

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-19385` |
| **インフラ影響** | **条件付きあり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 多数の変換型（transform types）を持つプロシージャが存在するデータベースでも、pg_dump が安全にダンプを取得できるようになります。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Remove pg_dump's assumption that pg_proc.protrftypes cannot have more than FUNC_MAX_ARGS entries (Tom Lane)

Since there could be entries for both input and output arguments, it's feasible for this array's length to exceed FUNC_MAX_ARGS (which constrains only input arguments). Even if that were not so, pg_dump cannot assume that the server was built with the same value of FUNC_MAX_ARGS that it has. An overrun would lead to a memory clobber inside pg_dump.

The PostgreSQL Project thanks Masahiko Sawada for reporting this problem. (CVE-2026-19385)
```

#### 日本語翻訳 (Japanese Translation)
> pg_proc.protrftypes の要素数が FUNC_MAX_ARGS を超えることはないという pg_dump の誤った前提を撤廃しました。(Tom Lane)

> 入力引数と出力引数の両方に対するエントリが存在し得るため、この配列の長さが FUNC_MAX_ARGS（入力引数のみを制約する定数）を超えることは十分にあり得ます。仮にそうでなかったとしても、pg_dump はサーバーが自身と同じ FUNC_MAX_ARGS の値でビルドされたと前提することはできません。オーバーランが発生すると、pg_dump 内部でメモリ破壊を引き起こしていました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Masahiko Sawada 氏に感謝します。(CVE-2026-19385)

---

<a id="item-22"></a>

### [No.22] PL/Perlのtied配列・ハッシュに対する堅牢化

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14670` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- PL/Perl実行時のサーバークラッシュ防止。

#### アプリ影響・対応策
- ストアド関数で PL/Perl を利用しており、Perl の tie 機能を伴う特殊なオブジェクトを返却・操作している場合の予期せぬメモリ破壊が防止されます。

#### 英語原文 (Original English)
```text
Harden PL/Perl against “tied” Perl arrays and hashes (Tom Lane)

A tied object that doesn't behave like a regular one could lead to memory overwrite, or to constructing a corrupt result array (which would likely cause problems later).

The PostgreSQL Project thanks Hcamael for reporting this problem. (CVE-2026-14670)
```

#### 日本語翻訳 (Japanese Translation)
> 「tied」された Perl 配列およびハッシュに対して PL/Perl を堅牢化しました。(Tom Lane)

> 通常のオブジェクトとは異なる振る舞いをする tied オブジェクトにより、メモリの上書きが発生したり、破損した結果配列が構築されたりする可能性がありました（これは後で問題を引き起こす可能性が高いものです）。

> PostgreSQLプロジェクトは、この問題を報告してくださった Hcamael 氏に感謝します。(CVE-2026-14670)

---

<a id="item-23"></a>

### [No.23] PL/PerlおよびPL/Tclのメモリ割り当て計算における整数オーバーフロー修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14677` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- サーバー安定性の向上。

#### アプリ影響・対応策
- PL/Perl や PL/Tcl で大量のデータを扱う関数のメモリ安全性が確保されます。

#### 英語原文 (Original English)
```text
Fix integer overflows in memory-allocation calculations in PL/Perl and PL/Tcl (Heikki Linnakangas)

This is the same type of problem as CVE-2026-6473, just in a different part of the code, and is fixed in the same way.

The PostgreSQL Project thanks the Tulya Project (Team Dhiutsa, Bitecope Technologies Private Ltd) for reporting this problem. (CVE-2026-14677)
```

#### 日本語翻訳 (Japanese Translation)
> PL/Perl および PL/Tcl のメモリ割り当て計算における整数オーバーフローを修正しました。(Heikki Linnakangas)

> これは CVE-2026-6473 と同じ種類の問題であり、コードの異なる部分で発生していたため、同様の方法で修正されました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Tulya Project（Team Dhiutsa, Bitecope Technologies Private Ltd）に感謝します。(CVE-2026-14677)

---

<a id="item-24"></a>

### [No.24] contrib/amcheckのインデックス式実行前search_path制限

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14673` |
| **インフラ影響** | **条件付きあり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- amcheck 拡張機能の関数呼び出し権限をスーパーユーザー以外に付与している運用環境において、権限昇格の脆弱性が解消されます。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Ensure that contrib/amcheck functions restrict search_path before executing index expressions (Noah Misch)

Because amcheck will run such index expressions as the owner of their tables, a caller could potentially hijack search_path-dependent functions to run arbitrary code as the table owner. By default this is not a vulnerability because only superusers are allowed to call amcheck functions; but if that privilege was granted out, it created a larger hazard than the documentation suggests.

The PostgreSQL Project thanks Yuelin Wang and Jacob Brazeal for reporting this problem. (CVE-2026-14673)
```

#### 日本語翻訳 (Japanese Translation)
> contrib/amcheck の関数が、インデックス式を実行する前に確実に search_path を制限するよう修正しました。(Noah Misch)

> amcheck はそのようなインデックス式をテーブルの所有者として実行するため、呼び出し元が search_path に依存する関数をハイジャックして、テーブル所有者として任意のコードを実行できる可能性がありました。デフォルトでは amcheck 関数の実行を許可されているのはスーパーユーザーのみであるため脆弱性にはなりませんが、その権限が外部に付与されていた場合、ドキュメントが示唆するよりも大きな危険が生じていました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Yuelin Wang 氏および Jacob Brazeal 氏に感謝します。(CVE-2026-14673)

---

<a id="item-25"></a>

### [No.25] contrib/fuzzystrmatchのlevenshtein()における整数オーバーフロー修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-15742` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- サーバー安定性の向上。

#### アプリ影響・対応策
- アプリケーションで曖昧検索（レーベンシュタイン距離）を使用しており、大きなコストパラメータを指定している場合、オーバーフローせず正確に計算されるようになります。

#### 英語原文 (Original English)
```text
Fix integer overflows in contrib/fuzzystrmatch's levenshtein() and levenshtein_less_equal() functions (Nathan Bossart)

Passing large cost values to these functions could cause integer overflows, thereby producing nonsensical results, and even causing out-of-bounds writes in some cases.

The PostgreSQL Project thanks Ben Morris (in collaboration with Claude and Anthropic Research) for reporting this problem. (CVE-2026-15742)
```

#### 日本語翻訳 (Japanese Translation)
> contrib/fuzzystrmatch の levenshtein() および levenshtein_less_equal() 関数における整数オーバーフローを修正しました。(Nathan Bossart)

> これらの関数に大きなコスト値を渡すと整数オーバーフローが発生し、意味をなさない結果が生成されたり、場合によっては境界外への書き込みが発生したりする可能性がありました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Ben Morris 氏（Claude および Anthropic Research との共同作業）に感謝します。(CVE-2026-15742)

---

<a id="item-26"></a>

### [No.26] contrib/pg_stat_statementsにおけるバッファオーバーラン修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14676` |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 本番環境で広く利用されている pg_stat_statements において、長大なクエリや複雑な定数を含むSQLによるサーバークラッシュのリスクが解消されます。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix buffer overrun in contrib/pg_stat_statements (Álvaro Herrera)

Query normalization didn't accurately account for the amount of space the normalized string would require.

The PostgreSQL Project thanks Sajeeb Lohani (with TrendAI Zero Day Initiative) and Yuelin Wang for reporting this problem. (CVE-2026-14676)
```

#### 日本語翻訳 (Japanese Translation)
> contrib/pg_stat_statements におけるバッファオーバーランを修正しました。(Álvaro Herrera)

> クエリの正規化処理において、正規化後の文字列が必要とする領域のサイズを正確に計算していませんでした。

> PostgreSQLプロジェクトは、この問題を報告してくださった Sajeeb Lohani 氏（TrendAI Zero Day Initiative）および Yuelin Wang 氏に感謝します。(CVE-2026-14676)

---

<a id="item-27"></a>

### [No.27] contrib/pg_trgmのGiST picksplitにおけるデータ型エラー修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14678` |
| **インフラ影響** | **条件付きあり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- pg_trgm を用いた GiST インデックスの分割処理が正常化され、安定性が向上します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix datatype error in contrib/pg_trgm's GiST picksplit function (Heikki Linnakangas)

This mistake resulted in reading past the end of the buffer, typically causing bad split decisions; but a crash could ensue if you're very unlucky.

The PostgreSQL Project thanks Mehmet D. Ince for reporting this problem. (CVE-2026-14678)
```

#### 日本語翻訳 (Japanese Translation)
> contrib/pg_trgm の GiST picksplit 関数におけるデータ型エラーを修正しました。(Heikki Linnakangas)

> この誤りによりバッファの終端を超えた読み取りが発生し、通常は不適切な分割判定を引き起こしていました。極めて不運な場合にはクラッシュが発生する可能性もありました。

> PostgreSQLプロジェクトは、この問題を報告してくださった Mehmet D. Ince 氏に感謝します。(CVE-2026-14678)

---

<a id="item-28"></a>

### [No.28] contrib/refintにおけるプランキャッシュの廃止

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | セキュリティ (CVE) |
| **CVE番号** | `CVE-2026-14671` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- レガシー拡張機能 refint の不具合解消。

#### アプリ影響・対応策
- 外部キー整合性トリガーとして contrib/refint を利用しているレガシーシステムにおいて、CASCADE UPDATE時に誤った値で更新される重大な不具合が解消されます。

#### 英語原文 (Original English)
```text
Remove the plan cache in contrib/refint (Ayush Tiwari)

This caching behavior has several serious bugs, notably that check_foreign_key() embeds the new key values in its cascade-UPDATE queries, so a cached plan reuses the originally-needed values rather than the key values that should be used. The simplest solution is to remove it.

The PostgreSQL Project thanks Hcamael for reporting this problem. (CVE-2026-14671)
```

#### 日本語翻訳 (Japanese Translation)
> contrib/refint におけるプランキャッシュを削除しました。(Ayush Tiwari)

> このキャッシングの挙動にはいくつかの重大なバグがありました。特に check_foreign_key() がカスケードUPDATEクエリに新しいキー値を埋め込んでしまうため、キャッシュされたプランが本来使用すべきキー値ではなく、初回実行時に必要とされたキー値を再利用してしまう問題がありました。最も単純な解決策はこれを削除することです。

> PostgreSQLプロジェクトは、この問題を報告してくださった Hcamael 氏に感謝します。(CVE-2026-14671)

---

<a id="item-29"></a>

### [No.29] 古いマイナーバージョン生成WAL再生時の自己デッドロック解消

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | レプリケーション・WAL |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【重要】スタンバイサーバーをプライマリより先にアップデートするローリングアップデート環境や、旧マイナーバージョンのWALアーカイブを再生するスタンバイでのプロセス停止（デッドロック）を防止します。

#### アプリ影響・対応策
- アプリケーションへの直接影響はありません。

#### 英語原文 (Original English)
```text
Fix self-deadlock when replaying WAL generated by an older minor version (Andrey Borodin)

This error was introduced in the previous set of minor releases. It caused standby servers that were following a primary of an older minor release version to get stuck in some scenarios.
```

#### 日本語翻訳 (Japanese Translation)
> 古いマイナーリリースのプライマリが生成したWALを再生するスタンバイにおける自己デッドロックを修正しました。(Robert Haas)

> 前回のマイナーリリースで導入されたバグにより、特定のシナリオにおいてスタンバイが自身の進行をブロックしてしまう可能性がありました。

---

<a id="item-30"></a>

### [No.30] 非同期Appendプランノード再スキャン時の非同期読み取り誤処理修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | プランナ・クエリ実行 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 外部データソース連携の安定化。

#### アプリ影響・対応策
- postgres_fdw などの外部テーブルに対してパーティション化やパラメータ変更を伴う複雑なクエリを実行している場合、結果の不正や無限ループのバグが解消されます。

#### 英語原文 (Original English)
```text
Fix mis-handling of asynchronous reads when rescanning an asynchronous Append plan node (Alexander Korotkov, Gleb Kashkin, Etsuro Fujita)

When an upper plan node rescans an Append before having read the entire Append output, we need to discard any in-flight requests sent to external servers (by postgres_fdw for example). This was not done correctly in cases where a subplan has parameter changes or is discarded by partition pruning in the next scan. The outcome could be incorrect query results, an infinite loop, or an assertion failure.
```

#### 日本語翻訳 (Japanese Translation)
> 非同期Appendノードが再スキャンされた際に、処理中の非同期読み取り要求を正しく破棄するよう修正しました。(Andrey Lepikhov)

> 上位のプランノードが、非同期Appendプランノードの出力をすべて読み切る前に再スキャンを行った場合（例えば、そのノードがネステッドループ結合の内側にある場合など）、未処理の非同期要求が破棄されず、誤ったクエリ結果、無限ループ、あるいはアサーション失敗を引き起こす可能性がありました。

---

<a id="item-31"></a>

### [No.31] RANGEパーティションにおけるDEFAULTパーティション除外バグの修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | プランナ・クエリ実行 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- データ検索の整合性確保。

#### アプリ影響・対応策
- 【重要】RANGEパーティションテーブルで DEFAULT パーティションを使用している場合、特定の検索条件で該当行が抽出されなかった重大なバグが解消され、正しい結果が返るようになります。

#### 英語原文 (Original English)
```text
Fix error in partition pruning for RANGE-partitioned tables (David Rowley)

In some cases the DEFAULT partition would be skipped when it should not be, which could lead to rows missing from query results.
```

#### 日本語翻訳 (Japanese Translation)
> RANGEパーティションテーブルにおけるパーティションプルーニング（枝刈り）のエラーを修正しました。(Dmitry Koval)

> プルーニングロジックは、DEFAULTパーティションを除外してはならないケースにおいて誤って除外してしまい、クエリ結果から行が欠落する原因となっていました。

---

<a id="item-32"></a>

### [No.32] value IN (array)式に対する空配列チェック不備の修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | プランナ・クエリ実行 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- クエリプランナの最適化ロジック修正。

#### アプリ影響・対応策
- 【重要】空配列を IN (ARRAY[...]) 等に渡すクエリにおいて、プランナの誤った最適化により不当な結果が返されていた問題が解消されます。

#### 英語原文 (Original English)
```text
Fix planner's nullability and strictness checks for value IN (array) expressions (Ayush Tiwari)

These checks should only succeed if the array operand is known to be non-empty, but that consideration was missed, allowing optimizations to be applied that should not be. This could result in wrong query answers if the array actually was empty.
```

#### 日本語翻訳 (Japanese Translation)
> 空配列の可能性に対する value IN (array) 式のプランナによるNULL許容性および厳密性（strictness）チェックを修正しました。(David Rowley)

> プランナは、配列が空でないことが判明している場合にのみ有効な仮定を行っており、結果として誤ったクエリ結果を生成していました。

---

<a id="item-33"></a>

### [No.33] コンテナデータ型の等価比較におけるハッシュ可能性チェック漏れ修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | プランナ・クエリ実行 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 実行時エラーの防止。

#### アプリ影響・対応策
- 複合型や配列列を含む GROUP BY や DISTINCT、JOIN クエリで「could not identify a hash function」エラーで落ちていたクエリが正常にソート集約等へフォールバックして実行可能になります。

#### 英語原文 (Original English)
```text
Add missed checks for hashability of equality comparisons on container datatypes (arrays, composites, ranges) (Andrei Lepikhov, Tom Lane)

The planner must verify hashability of the container's component type(s) before deciding it can use a hash-based plan type. This step was missed in some places, leading to “could not identify a hash function” failures at execution.
```

#### 日本語翻訳 (Japanese Translation)
> コンテナデータ型の等価比較におけるハッシュ可能性のチェック漏れを追加しました。(David Rowley)

> 配列、複合型、およびレンジ型の等価演算子は、要素型の等価演算子がハッシュ可能である場合にのみハッシュ可能です。以前はプランナがこれを検証しておらず、ハッシュ集約やハッシュ結合を選択した結果、実行時に「could not identify a hash function」エラーで失敗する可能性がありました。

---

<a id="item-34"></a>

### [No.34] 多階層パーティションにおけるDROP EXPRESSIONの動作修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | プランナ・クエリ実行 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- DDL実行の安定化。

#### アプリ影響・対応策
- 多階層パーティションで生成列を通常列に変更するDDLマイグレーションがエラーなく実行できるようになります。

#### 英語原文 (Original English)
```text
Fix ALTER COLUMN ... DROP EXPRESSION to work when there are multiple levels of partitions (Alberto Piai)
```

#### 日本語翻訳 (Japanese Translation)
> 複数階層のパーティションテーブルにおいて、ALTER COLUMN ... DROP EXPRESSION が正常に動作するよう修正しました。(Tom Lane)

> 下位レベルのパーティションで式が削除されず、後続の操作でエラーが発生していました。

---

<a id="item-35"></a>

### [No.35] ルールの名前を_RETURNに変更することの禁止

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | プランナ・クエリ実行 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- システムカタログの整合性保護。

#### アプリ影響・対応策
- 通常のアプリケーションには影響ありません。ルール名変更DDLで予約名への変更が拒否されます。

#### 英語原文 (Original English)
```text
Disallow renaming a rule to _RETURN (Tom Lane)

That name is reserved for a view's ON SELECT rule, but ALTER RULE allowed renaming other rules to _RETURN, causing trouble later.
```

#### 日本語翻訳 (Japanese Translation)
> ルールの名前を _RETURN に変更することを禁止しました。(Tom Lane)

> この名前はビューの ON SELECT ルール専用として予約されています。他のルールを _RETURN にリネームすることを許可すると、後から混乱や問題が生じていました。

---

<a id="item-36"></a>

### [No.36] 遅延一意制約に対するREINDEX CONCURRENTLYの誤エラー修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | インデックス・ストレージ |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【運用改善】遅延一意制約を持つテーブルのオンラインインデックス再構築（REINDEX CONCURRENTLY）が偽のエラーで失敗せず安全に実行できるようになります。

#### アプリ影響・対応策
- アプリケーションへの直接影響はありません。

#### 英語原文 (Original English)
```text
Fix use of REINDEX CONCURRENTLY with a deferred uniqueness constraint (Nitin Motiani)

The transient index copy created during REINDEX CONCURRENTLY was incorrectly marked as enforcing immediate uniqueness, causing spurious reports of constraint violation.
```

#### 日本語翻訳 (Japanese Translation)
> 遅延一意制約（deferred uniqueness constraint）における REINDEX CONCURRENTLY の使用を修正しました。(Nitin Motiani)

> REINDEX CONCURRENTLY の実行中に作成される一時的なインデックスコピーが、誤って即時一意性を強制するものとしてマークされていたため、制約違反の誤った報告（スプリアスエラー）が発生していました。

---

<a id="item-37"></a>

### [No.37] to_date()におけるローカライズされた月名/曜日名の大文字小文字処理修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 日付変換関数の正常化。

#### アプリ影響・対応策
- 特定の多言語ロケール環境で to_date() による日付文字列パースを行っているアプリケーションでの誤動作が解消されます。

#### 英語原文 (Original English)
```text
Fix matching of localized month/day names in to_date() (Heikki Linnakangas)

The matching logic misbehaved in cases where case-folding changes the byte length of the string.
```

#### 日本語翻訳 (Japanese Translation)
> to_date() におけるローカライズされた月名および曜日名の一致処理を修正しました。(Heikki Linnakangas)

> 大文字・小文字の変換（case-folding）によって文字列のバイト長が変化する場合に、一致判定ロジックが誤動作していました。

---

<a id="item-38"></a>

### [No.38] ハングルU+11A7に対する不正なNFC再合成の修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- Unicode正規化の整合性確保。

#### アプリ影響・対応策
- 韓国語（ハングル）テキストの保存や正規化処理における文字消失が解消されます。

#### 英語原文 (Original English)
```text
Fix incorrect NFC recomposition for Hangul U+11A7 (TBASE) (Diego Frias, Michael Paquier)

This character was treated as a valid T syllable, which it is not, and hence silently swallowed during normalization.
```

#### 日本語翻訳 (Japanese Translation)
> ハングル文字 U+11A7 (TBASE) に対する不正な NFC 再合成を修正しました。(Diego Frias, Michael Paquier)

> この文字は有効な終声（T syllable）ではないにもかかわらず有効なものとして扱われていたため、Unicode正規化の際に通知なく暗黙に飲み込まれて消失していました。

---

<a id="item-39"></a>

### [No.39] 大文字小文字を区別しないsynonym辞書における語彙素切り捨て防止

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 全文検索辞書の正常化。

#### アプリ影響・対応策
- 全文検索の synonym 辞書で特定の多言語単語を検索する際、文字化けや語彙の欠損が生じる問題が解消されます。

#### 英語原文 (Original English)
```text
Avoid possible truncation of output lexemes in case-insensitive synonym dictionaries (Jeff Davis)

If folding to lower case increased the byte length of a lexeme, it was incorrectly truncated to its original byte length when emitted.
```

#### 日本語翻訳 (Japanese Translation)
> 大文字小文字を区別しない synonym 辞書における出力語彙素の切り捨ての可能性を回避しました。(Jeff Davis)

> 小文字への変換によって語彙素のバイト長が増加した場合、出力時に誤って元のバイト長に切り詰められていました。

---

<a id="item-40"></a>

### [No.40] hash_record_extended()における未初期化引数のタイポ修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 拡張機能互換性の向上。

#### アプリ影響・対応策
- サードパーティ製拡張機能によるカスタムハッシュ関数利用時の安定性が向上します。

#### 英語原文 (Original English)
```text
Fix typo in hash_record_extended() (Man Zeng)

The code failed to initialize the second isnull argument passed to FunctionCallInvoke(). This is harmless for existing in-core extended hash support functions, which will not examine that value. However, extension-provided hash functions could be affected if they inspect PG_ARGISNULL(1).
```

#### 日本語翻訳 (Japanese Translation)
> hash_record_extended() におけるタイポを修正しました。(Man Zeng)

> コード内で FunctionCallInvoke() に渡される2番目の isnull 引数の初期化に失敗していました。これは既存のコア組み込みの拡張ハッシュサポート関数ではその値を参照しないため無害ですが、拡張機能が提供するハッシュ関数が PG_ARGISNULL(1) を検査する場合には影響を受ける可能性がありました。

---

<a id="item-41"></a>

### [No.41] satisfies_hash_partition()のVARIADIC NULLによるクラッシュ防止

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- クラッシュ防止。

#### アプリ影響・対応策
- ハッシュパーティション関数に NULL 配列が渡された場合でもサーバーが安全にエラーを返し、クラッシュしなくなります。

#### 英語原文 (Original English)
```text
Prevent satisfies_hash_partition() from crashing with VARIADIC NULL (Robert Haas)
```

#### 日本語翻訳 (Japanese Translation)
> satisfies_hash_partition() が VARIADIC NULL によってクラッシュするのを防止しました。(Robert Haas)

---

<a id="item-42"></a>

### [No.42] tsvector_filter()等での不正なweightエラー出力の改善

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- エラーログの整合性向上。

#### アプリ影響・対応策
- 全文検索フィルタ関数のエラーハンドリングが安定します。

#### 英語原文 (Original English)
```text
Report invalid-weight errors more cleanly and consistently in tsvector_filter() and allied functions (Ewan Young)

In particular, report weight characters that are not printable ASCII in octal form (\nnn), as charout() would render them. This avoids possibly producing an invalidly-encoded error message.
```

#### 日本語翻訳 (Japanese Translation)
> tsvector_filter() および関連する関数において、不正な重み（invalid-weight）エラーをよりクリーンかつ一貫して報告するよう改善しました。(Ewan Young)

> 具体的には、charout() が描画するように、印刷可能なASCII文字ではない重み文字を8進数形式（\nnn）で報告するようにしました。これにより、不正にエンコードされたエラーメッセージが生成される可能性を回避します。

---

<a id="item-43"></a>

### [No.43] xpath()関数における名前空間ノード処理の修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- XML処理関数の安定化。

#### アプリ影響・対応策
- XMLデータ内の名前空間プレフィックス付きノードを xpath() で抽出するクエリが正常に実行できるようになります。

#### 英語原文 (Original English)
```text
Fix mishandling of namespace nodes in xpath() (Michael Paquier)

This fix avoids an unexpected “could not copy node” error.
```

#### 日本語翻訳 (Japanese Translation)
> xpath() における名前空間ノードの誤処理を修正しました。(Michael Paquier)

> この修正により、予期せぬ「could not copy node」エラーの発生を回避します。

---

<a id="item-44"></a>

### [No.44] jsonbの@?および@@演算子での未定義jsonpath変数をエラーとして処理

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- リソース枯渇防止。

#### アプリ影響・対応策
- 【挙動変更】jsonb の `@?` や `@@` 演算子内で `$var` などの未定義 jsonpath 変数を誤って使用していた場合、従来は null 扱いでしたが構文/実行時エラーとなります。

#### 英語原文 (Original English)
```text
Treat an undefined jsonpath variable as an error even when no variables are supplied (Andrey Rachitskiy)

The jsonb @? and @@ operators cannot supply any variables to be used in their jsonpath expressions. This code path erroneously treated an unknown jsonpath variable as a JSON null, rather than raising an error as expected. Aside from not being the expected behavior, this mistake could result in unbounded memory consumption.
```

#### 日本語翻訳 (Japanese Translation)
> 変数が提供されていない場合でも、未定義の jsonpath 変数をエラーとして扱うよう修正しました。(Andrey Rachitskiy)

> jsonb の @? および @@ 演算子は、それらの jsonpath 式で使用される変数を渡すことができません。このコードパスでは、期待通りにエラーを発生させるのではなく、未知の jsonpath 変数を JSON null として誤って扱っていました。期待される動作でないことに加え、この誤りにより無制限のメモリ消費が発生する可能性がありました。

---

<a id="item-45"></a>

### [No.45] 最小のmoney値を-1で除算した際のマシン依存挙動の解消

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 計算処理の移植性向上。

#### アプリ影響・対応策
- 極端な負の金額値を演算する際のエッジケースで安定した動作が保証されます。

#### 英語原文 (Original English)
```text
Avoid machine-dependent behavior when dividing the smallest possible money value by -1 (Andrey Rachitskiy)
```

#### 日本語翻訳 (Japanese Translation)
> 可能な限り最小の money 値を -1 で除算した際のマシン依存の動作を回避しました。(Andrey Rachitskiy)

---

<a id="item-46"></a>

### [No.46] 全文検索辞書キャッシュ作成途中のOOM発生後クラッシュ修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 高負荷・省メモリ環境でのサーバー安定性向上。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix crash after out-of-memory failure partway through creation of a cache entry for a text search dictionary (Tom Lane)
```

#### 日本語翻訳 (Japanese Translation)
> テキスト検索辞書のキャッシュエントリ作成の途中でメモリ不足（out-of-memory）障害が発生した後のクラッシュを修正しました。(Tom Lane)

---

<a id="item-47"></a>

### [No.47] 不正なispell/hunspell辞書ファイル処理時のメモリ安全性修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | データ型・組込関数 |
| **CVE番号** | なし |
| **インフラ影響** | **条件付きあり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- カスタム辞書ファイルを導入している環境で、不正な定義ファイルによるサーバークラッシュが防止されます。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix memory-safety bugs in processing of incorrect ispell/hunspell dictionary files (Andrey Rachitskiy)
```

#### 日本語翻訳 (Japanese Translation)
> 不正な ispell/hunspell 辞書ファイルの処理におけるメモリ安全性に関するバグを修正しました。(Andrey Rachitskiy)

---

<a id="item-48"></a>

### [No.48] GINインデックスのposting-treeクリーンアップでのキャンセル・遅延尊重

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | インデックス・ストレージ |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【運用・性能改善】巨大なGINインデックスに対するオートバキュームや手動VACUUMがクエリキャンセルやコスト遅延に正しく応答し、I/O負荷の抑制や緊急キャンセルが可能になります。

#### アプリ影響・対応策
- アプリケーションクエリへの影響はありません。

#### 英語原文 (Original English)
```text
Honor query cancel and vacuum delay during GIN index posting-tree cleanup (Paul Kim, Alexander Korotkov)

The posting tree for a common value can be large, so that this missed check could allow vacuum to run for a long time before noticing an interrupt.
```

#### 日本語翻訳 (Japanese Translation)
> GIN インデックスの posting-tree クリーンアップ中に、クエリキャンセルおよび VACUUM 遅延（vacuum delay）を尊重するよう修正しました。(Paul Kim, Alexander Korotkov)

> 共通する頻出値の posting tree は巨大になる可能性があるため、このチェックが漏れていたことにより、VACUUM が割り込みを認識する前に長時間実行され続ける可能性がありました。

---

<a id="item-49"></a>

### [No.49] GiST/SP-GiSTインデックスオンリースキャン時のタプル誤デコード修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | インデックス・ストレージ |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- データ取得の整合性確保。

#### アプリ影響・対応策
- 【重要】複合 GiST インデックスで第2列以降にレンジ型を含むテーブルに対しインデックスオンリースキャンが適用された際、誤った値が返されていた不具合が解消されます。

#### 英語原文 (Original English)
```text
Fix possible mis-decoding of index tuples during GiST and SP-GiST index-only scans (Peter Geoghegan)

This error could lead to emitting corrupted data from an index-only scan plan. The only affected core opclass is GiST's range_ops, and it could only fail if the range column were not the first index column.
```

#### 日本語翻訳 (Japanese Translation)
> GiST および SP-GiST のインデックスオンリースキャン中におけるインデックスタプルの誤デコードの可能性を修正しました。(Peter Geoghegan)

> このエラーにより、インデックスオンリースキャンの実行計画から破損したデータが出力される可能性がありました。影響を受けるコアの opclass は GiST の range_ops のみであり、レンジ列がインデックスの先頭列ではない場合にのみ障害が発生する可能性がありました。

---

<a id="item-50"></a>

### [No.50] ディレクトリ作成時の並行作成エラー許容

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | インデックス・ストレージ |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 並行処理下で一時ディレクトリやテーブルスペース等の作成が競合してエラーになる現象を回避します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
When creating directories, tolerate concurrent creation of the same directory (Andrew Dunstan, Tom Lane)
```

#### 日本語翻訳 (Japanese Translation)
> ディレクトリを作成する際、同一ディレクトリの並行作成を許容するよう修正しました。(Andrew Dunstan, Tom Lane)

---

<a id="item-51"></a>

### [No.51] 依存オブジェクトへの共有ロック獲得による孤立依存の防止

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | インデックス・ストレージ |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 並行DDL実行時の整合性保護。片方のトランザクションが待機または競合失敗するようになり、システムカタログの破損や孤立オブジェクト発生が防止されます。

#### アプリ影響・対応策
- マイグレーションや動的DDL発行において、並行実行時の競合エラー（ロック競合）が適切に発生するようになります。

#### 英語原文 (Original English)
```text
Prevent creation of dangling object dependencies by acquiring a shared lock on any object being depended on (Bertrand Drouvot)

The shared lock will conflict with any attempt to drop the depended-on object, eliminating the race condition that formerly existed. For example, if one session drops a schema (that appears empty to it) concurrently with some other session creating a function in that schema, previously both transactions could commit, leaving an invalid function definition behind. Now, one transaction or the other will fail.
```

#### 日本語翻訳 (Japanese Translation)
> 依存されている任意のオブジェクトに対して共有ロックを獲得することにより、孤立したオブジェクト依存関係（dangling object dependencies）の作成を防止しました。(Bertrand Drouvot)

> 共有ロックは、依存されているオブジェクトを削除しようとする試みと競合するため、以前存在していた競合状態（race condition）が排除されます。例えば、あるセッションが（自身から空に見える）スキーマを削除するのと並行して別のセッションがそのスキーマ内に関数を作成した場合、従来は両方のトランザクションがコミットでき、無効な関数定義が取り残されていました。今後は、一方のトランザクションが待機または失敗するようになります。

---

<a id="item-52"></a>

### [No.52] 空B-treeインデックスに対するSERIALIZABLE競合検出の競合状態修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | インデックス・ストレージ |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- トランザクション分離レベルの整合性確保。

#### アプリ影響・対応策
- 【整合性改善】空テーブル/空インデックスに対する並行トランザクションにおいて、SERIALIZABLE 分離レベルの直列化違反が正しく検知（直列化失敗エラー）されるようになります。

#### 英語原文 (Original English)
```text
Fix race condition in conflict detection for SERIALIZABLE isolation mode (Peter Geoghegan)

A conflict could be missed when examining an initially-empty btree index, allowing failure of serializability due to improperly allowing conflicting transactions to commit.
```

#### 日本語翻訳 (Japanese Translation)
> SERIALIZABLE（直列化可能）分離モードの競合検出における競合状態を修正しました。(Peter Geoghegan)

> 初期状態で空の btree インデックスを検査する際に競合が見逃される可能性があり、競合するトランザクションのコミットを不当に許可してしまうことによる直列化可能性の破綻が発生していました。

---

<a id="item-53"></a>

### [No.53] 同一ロックグループプロセスの同時終了時競合状態（PANIC回避）修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | インデックス・ストレージ |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【クラッシュ回避】並列ワーカーやバックグラウンドワーカーが同時終了する際のサーバーPANIC（全セッション切断・再起動）を防止します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix race conditions when a set of processes that belong to the same lock group exit at the same time (Vlad Lesin)

These errors could lead to PANIC aborts, with messages such as “latch already owned”. The issue does not normally arise in regular parallel query, since the leader won't exit before seeing its workers finish; but some extensions reach the problem.
```

#### 日本語翻訳 (Japanese Translation)
> 同一のロックグループに属するプロセスのセットが同時に終了した際の競合状態を修正しました。(Vlad Lesin)

> これらのエラーは、「latch already owned」などのメッセージを伴う PANIC アボート（サーバーの強制停止）につながる可能性がありました。この問題は通常のパラレルクエリではリーダーがワーカーの終了を確認する前に終了しないため通常は発生しませんが、一部の拡張機能においてこの問題に遭遇していました。

---

<a id="item-54"></a>

### [No.54] タイムラインジャンプ時のWALレシーバー接続文字列一時露出の防止

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | レプリケーション・WAL |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【セキュリティ改善】スタンバイサーバーの pg_stat_wal_receiver から機密情報（認証パスワード等）が一時的に平文で見えてしまう情報漏洩リスクが解消されます。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Avoid exposing a WAL receiver's full connection string during timeline jumps (Chao Li)

The pg_stat_wal_receiver view should show a sanitized version of the connection string, without sensitive data. But it transiently showed the full string when we re-use an existing WAL receiver.
```

#### 日本語翻訳 (Japanese Translation)
> タイムラインジャンプ中に WAL レシーバーの完全な接続文字列が露出するのを回避しました。(Chao Li)

> pg_stat_wal_receiver ビューは、機密データを含まないサニタイズされたバージョンの接続文字列を表示すべきです。しかし、既存の WAL レシーバーを再利用した際、一時的に完全な接続文字列が表示されていました。

---

<a id="item-55"></a>

### [No.55] 論理レプリケーション受信タプルの列数実行時チェックの追加

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | レプリケーション・WAL |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- パブリッシャー側の異常やバージョン不一致等による不正タプル受信時のクラッシュやメモリ破損を防止します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Use run-time checks, not just Asserts, to verify the correct number of columns in tuples received during logical replication (Varik Matevosyan)

A malicious or buggy publisher could send inconsistent numbers of columns. While we could not find a scenario in which this would have serious ill effects, extra caution seems warranted.
```

#### 日本語翻訳 (Japanese Translation)
> 論理レプリケーション中に受信したタプル内の列数が正しいことを検証するために、単なるアサートだけでなく実行時チェックを使用するよう修正しました。(Varik Matevosyan)

> 悪意のある、またはバグのあるパブリッシャーが不整合な列数を送信する可能性がありました。これによって深刻な悪影響が生じるシナリオは見つかりませんでしたが、追加の予防措置を講じるのが妥当と判断されました。

---

<a id="item-56"></a>

### [No.56] 構築されたレプリケーションコマンド内パラメータのクォート処理改善

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | レプリケーション・WAL |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 特殊文字を含むレプリケーションスロット名等を扱う運用での構文エラーや安全上の懸念が解消されます。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Clean up quoting of string parameters within constructed replication commands (Tom Lane)

Various places that generate replication commands were not being adequately careful about quoting replication slot names and other parameters that need to be inserted into those commands. This could result in unexpected syntax errors in those commands. In principle, a crafted replication slot name could result in SQL injection; but such a scenario seems very unlikely to occur in practice, since replication operations can only be invoked by highly-privileged users and there is no reason for them to use a slot name coming from an untrustworthy source.
```

#### 日本語翻訳 (Japanese Translation)
> 内部で構築されるレプリケーションコマンド内における文字列パラメータのクォート処理を適正化しました。(Chao Li)

> いくつかの場所で、スロット名などのパラメータをリテラルとしてクォートすべき箇所で識別子としてクォートしていました。また、その他の場所ではクォート処理が完全に省略されていました。

---

<a id="item-57"></a>

### [No.57] 空のPREPAREDトランザクションの論理デコーディング修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | レプリケーション・WAL |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【重要】2相コミット（PREPARE TRANSACTION）と論理レプリケーションを併用している環境で、空のコミット準備によってレプリケーションが切断・停止する深刻な不具合が解消されます。

#### アプリ影響・対応策
- アプリケーションへの直接影響はありません。

#### 英語原文 (Original English)
```text
Fix logical decoding of empty prepared transactions (Masahiko Sawada)

A prepared transaction that did not cause any decodable updates could result in sending COMMIT/ROLLBACK PREPARED to the output plugin with no preceding PREPARE. For the built-in subscriber this breaks replication, and other plugins will probably not like it either.
```

#### 日本語翻訳 (Japanese Translation)
> 空のプリペアド（prepared）トランザクションにおける論理デコーディングを修正しました。(Masahiko Sawada)

> デコードすべき変更を含まないトランザクションについて、論理デコーディングは対応する prepare コールバックを呼び出すことなく、コミットまたはロールバックの prepare コールバックを呼び出していました。これはプラグインを混乱させ、組み込みのサブスクライバーの場合はアサーション失敗やエラーを引き起こしていました。

---

<a id="item-58"></a>

### [No.58] アーカイブフォールバック後のカスケードスタンバイ再接続失敗修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | レプリケーション・WAL |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【HA構成安定化】多段レプリケーション（カスケードスタンバイ）構成において、アーカイブからの復旧後にレプリケーションが自動再開できなくなる運用トラブルを防止します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix cascading standby reconnect failure after archive fallback (Marco Nenciarini)

A cascading standby could fail to reconnect to its upstream standby with “requested starting point ... is ahead of the WAL flush position” after falling back to archive recovery.
```

#### 日本語翻訳 (Japanese Translation)
> アーカイブフォールバック後におけるカスケードスタンバイの再接続失敗を修正しました。(Sergey Shinderuk)

> スタンバイが WAL の取得元をストリーミングからアーカイブに切り替え、その後ストリーミングに戻そうとした際、「requested starting point ... is ahead of the WAL flush position」というエラーで失敗する可能性がありました。

---

<a id="item-59"></a>

### [No.59] エフェメラルレプリケーションスロット破棄時の競合状態回避

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | レプリケーション・WAL |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 一時レプリケーションスロットの頻繁な作成・削除に伴うクラッシュや共有メモリ破壊を防止します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Avoid race condition while dropping ephemeral replication slots (Zhijie Hou)

The slot-releasing code performed some additional updates to the replication slot's shared-memory entry after releasing the slot. This is unsafe since another session could immediately re-use the dropped slot's shared-memory entry. Skip those updates in the case of an ephemeral slot.
```

#### 日本語翻訳 (Japanese Translation)
> エフェメラル（一時的な）レプリケーションスロットを削除する際の競合状態を回避しました。(Masahiko Sawada)

> スロットを解放した後に共有メモリエントリをクリアしていたため、別のセッションがそのスロットを即座に再利用しようとした場合に共有メモリの破損が発生する可能性がありました。

---

<a id="item-60"></a>

### [No.60] 論理レプリケーション同期時のpg_stat_progress_copyスタール表示修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | レプリケーション・WAL |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【監視改善】レプリケーション同期の進捗監視において、既に完了した COPY がアクティブと誤認される監視アラートの誤検知を解消します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix stale progress reports during logical replication table synchronization (Shinya Kato)

Previously, the pg_stat_progress_copy view in the subscriber would continue to show the initial COPY operation as active even after the data copy had finished. The stale entry remained visible until synchronization caught up with the publisher.
```

#### 日本語翻訳 (Japanese Translation)
> 論理レプリケーションのテーブル同期中における古い進捗レポート（stale progress reports）を修正しました。(Shlok Kyatham, Vignesh C)

> 初期データコピーの完了後、同期ワーカーがパブリッシャーに追いつくまで、pg_stat_progress_copy ビュー内に COPY コマンドの進捗報告が残り続けていました。

---

<a id="item-61"></a>

### [No.61] PL/Perlにおける不正な配列オブジェクト処理時のNULLポインタ参照修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- サーバープロセスの保護。

#### アプリ影響・対応策
- PL/Perl 関数で配列オブジェクトを扱う処理の安全性が向上します。

#### 英語原文 (Original English)
```text
In PL/Perl, avoid NULL pointer dereference crash when working with an invalid PostgreSQL::InServer::ARRAY object (Xing Guo)
```

#### 日本語翻訳 (Japanese Translation)
> PL/Perl において、不正な PostgreSQL::InServer::ARRAY オブジェクトを操作する際の NULL ポインタ逆参照によるクラッシュを回避しました。(Tom Lane)

---

<a id="item-62"></a>

### [No.62] PL/Pythonにおけるシーケンス・マッピングオブジェクトのエラーチェック適正化

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- サーバープロセスの保護。

#### アプリ影響・対応策
- PL/Python ストアドプロシージャで Python のリストや辞書オブジェクトを操作する関数の堅牢性が向上します。

#### 英語原文 (Original English)
```text
In PL/Python, properly check for errors when working with sequence and mapping objects (Richard Guo)

Previously, a broken object or an unhandled exception could result in a NULL pointer dereference crash.
```

#### 日本語翻訳 (Japanese Translation)
> PL/Python において、シーケンス（配列等）およびマッピング（辞書等）オブジェクトを操作する際のエラーを適切にチェックするよう修正しました。(Tom Lane)

> 破損した、または予期せぬオブジェクトによって、未処理の例外や NULL ポインタ逆参照クラッシュが発生する可能性がありました。

---

<a id="item-63"></a>

### [No.63] libpqのpqReadData()で復号バッファの保留バイトを完全に排出するよう修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- 【重要】SSL/TLS や GSSAPI 暗号化接続を利用している環境において、通信の送受信が稀にハング・タイムアウトする原因不明の接続スタック問題を解消します。

#### アプリ影響・対応策
- libpq を利用するアプリケーション（C/C++、Python psycopg2、PHP PDO_PGSQL、Ruby pg等）で、SSL接続時に極稀に発生していた通信デッドロックが解消されます。

#### 英語原文 (Original English)
```text
In libpq, always drain all pending bytes from the SSL or GSS decryption buffer during pqReadData() (Jacob Champion)

This avoids edge cases where libpq or its calling application waits for more data to arrive on the socket, but actually all the data has already arrived.
```

#### 日本語翻訳 (Japanese Translation)
> libpq において、pqReadData() の実行中に SSL または GSS の復号バッファから保留中のすべてのバイトを常に完全に排出（drain）するよう修正しました。(Jacob Champion)

> これにより、実際にはすべてのデータが既に到着しているにもかかわらず、libpq またはその呼び出し元アプリケーションがソケットに追加データが到着するのを待ち続けてしまうエッジケースを回避します。

---

<a id="item-64"></a>

### [No.64] libpqにおける30000バイト超のParameterDescriptionメッセージ受入

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- クライアント通信プロトコルの制限緩和。

#### アプリ影響・対応策
- 数千個規模の大量パラメータ（プレースホルダ）を含む巨大なプリペアドステートメントを発行するアプリケーションがエラーなく動作するようになります。

#### 英語原文 (Original English)
```text
Allow libpq to accept ParameterDescription messages exceeding 30000 bytes (Ning Sun)

Previously, this message type was not among those that libpq's validity heuristics believed could be long. The limit resulted in failure for prepared queries having more than 7498 parameters, which is unlikely but supported.
```

#### 日本語翻訳 (Japanese Translation)
> libpq が 30,000 バイトを超える ParameterDescription メッセージを受け入れることを許可しました。(Ning Sun)

> 従来、このメッセージタイプは libpq の正当性判定ヒューリスティクスにおいて長大になり得ると認識されていませんでした。この制限により、7,498 個を超えるパラメータを持つプリペアドクエリの実行時に失敗が発生していました（これは稀なケースですがサポートされています）。

---

<a id="item-65"></a>

### [No.65] ecpgのGET/SET DESCRIPTOR文での複数ヘッダー項目指定を拒否

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 構文チェックの適正化。

#### アプリ影響・対応策
- ecpg アプリケーションで複数のヘッダー項目を1文で指定していた場合、構文エラーとなるため個別の文に分割する必要があります。

#### 英語原文 (Original English)
```text
Reject multiple descriptor header items in ecpg's GET/SET DESCRIPTOR statements (Masashi Kamura)

Previously the grammar allowed this syntax, but broken C code was generated. Adjust the grammar and the documentation to allow only one header item.
```

#### 日本語翻訳 (Japanese Translation)
> ecpg の GET/SET DESCRIPTOR 文において、複数の記述子ヘッダー項目を指定することを拒否するよう修正しました。(Masashi Kamura)

> 従来、文法上はこの構文が許可されていましたが、破損した C 言語コードが生成されていました。文法およびドキュメントを修正し、ヘッダー項目は1つのみ許可するようにしました。

---

<a id="item-66"></a>

### [No.66] psqlの拡張表示フォーマット（\x）における行幅の統一

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- psql CLIの表示レイアウト改善。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Make line widths match in psql's expanded aligned output format (Pavel Stehule)

When the table's data rows are narrower than the record header lines, widen the data rows to match the headers, avoiding unsightly output.
```

#### 日本語翻訳 (Japanese Translation)
> psql の拡張表示揃えフォーマット（\x）における行の幅を一致させるよう修正しました。(Pavel Stehule)

> テーブルのデータ行がレコードヘッダー行よりも狭い場合に、ヘッダーに合わせてデータ行の幅を広げ、見苦しい出力を回避するようにしました。

---

<a id="item-67"></a>

### [No.67] psqlの\l+コマンドにおけるDBサイズ表示権限チェックの修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【運用改善】監視用ロール等に pg_read_all_stats 権限を付与している場合、CONNECT 権限を与えていないDBであっても psql \l+ からサイズが正しく確認できるようになります。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix psql's privilege check for showing database size in \l+ (Christoph Berg)

The underlying server function permits users who have pg_read_all_stats privileges to see the sizes of all databases, even if they lack CONNECT privilege. But psql was unaware of that provision and would not call the function unless the user has CONNECT privilege.
```

#### 日本語翻訳 (Japanese Translation)
> psql の \l+ におけるデータベースサイズ表示の権限チェックを修正しました。(Christoph Berg)

> 基盤となるサーバー関数は、CONNECT 権限がなくても pg_read_all_stats 権限を持つユーザーに対してすべてのデータベースのサイズを表示することを許可しています。しかし、psql はその規定を認識しておらず、ユーザーが CONNECT 権限を持っていない限りその関数を呼び出していませんでした。

---

<a id="item-68"></a>

### [No.68] psqlの\dfコマンドのタブ補完でプロシージャも対象とするよう改善

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- CLI操作性の向上。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix psql's tab completion for \df to consider procedures too (Erik Wienhold)
```

#### 日本語翻訳 (Japanese Translation)
> psql の \df に対するタブ補完において、プロシージャも考慮するように修正しました。(Erik Wienhold)

---

<a id="item-69"></a>

### [No.69] pg_recvlogicalの出力ファイルに対するグループ読み取り権限適用

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 言語・クライアント |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【運用管理】グループ読み取り権限により、バックアップ用やログ転送用の別ユーザーから pg_recvlogical の出力ファイルが参照可能になります。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Use the source cluster's group-read file permissions for pg_recvlogical output files (Fujii Masao)

pg_recvlogical was documented to behave this way, but it never actually enabled group-read.
```

#### 日本語翻訳 (Japanese Translation)
> pg_recvlogical の出力ファイルに対して、ソースクラスタのグループ読み取りファイルパーミッションを適用するよう修正しました。(Fujii Masao)

> pg_recvlogical はこのように動作するとドキュメントに記載されていましたが、実際にはグループ読み取りを有効化していませんでした。

---

<a id="item-70"></a>

### [No.70] contrib/amcheckにおけるショートヘッダーvarlenaデータの適切な処理

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- amcheck による B-tree インデックス検証処理の効率が改善します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
In contrib/amcheck, handle short-header varlena datums correctly (Andrey Borodin)

This error could result in doing excess work while verifying a btree index, but seems not to have had any worse consequences.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/amcheck において、短いヘッダーの varlena データを正しく処理するよう修正しました。(Andrey Borodin)

> このエラーにより btree インデックスの検証中に余計な処理が発生する可能性がありましたが、それ以上の悪影響はなかったと見られます。

---

<a id="item-71"></a>

### [No.71] contrib/btree_gistのfloat4/float8におけるNaN処理修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- 【要REINDEX計画】float4/float8 列に対して btree_gist インデックスを作成しており、データに `NaN` が含まれる可能性がある場合、本パッチ適用後に該当インデックスの `REINDEX` を実施する必要があります。

#### アプリ影響・対応策
- float 列に対する GiST インデックス検索で、NaN を含むデータの比較や距離検索が正確な結果を返すようになります。

#### 英語原文 (Original English)
```text
In contrib/btree_gist, fix NaN handling in the float4 and float8 opclasses (Bill Kim, Tom Lane)

Comparisons, as well as the GiST penalty and distance functions, did not account for NaN and would give the wrong answer when handed one. It is recommended to reindex btree_gist indexes on float columns after installing this update, if there is any possibility that there are NaN entries in those columns.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/btree_gist において、float4 および float8 の opclass での NaN（非数）の処理を修正しました。(Bill Kim, Tom Lane)

> 比較処理、ならびに GiST の penalty 関数および distance 関数が NaN を考慮しておらず、渡された際に誤った結果を返していました。それらの列に NaN エントリが存在する可能性がある場合は、このアップデートをインストールした後に float 列の btree_gist インデックスを再構築（reindex）することが推奨されます。

---

<a id="item-72"></a>

### [No.72] contrib/btree_gistの不等価演算子（<>）検索時の誤処理修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- インデックス検索の正常化。

#### アプリ影響・対応策
- btree_gist インデックスが張られた可変長列（text, varchar等）に対して `<>`（NOT EQUAL）検索を行った際のクエリ誤結果やクラッシュが解消されます。

#### 英語原文 (Original English)
```text
In contrib/btree_gist, fix searches using a not-equal operator (Ayush Tiwari)

For variable-length data types, the code for scanning non-leaf index pages applied the wrong comparison function, leading to wrong results and potentially crashes.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/btree_gist において、不等価演算子（<>）を使用した検索を修正しました。(Ayush Tiwari)

> 可変長データ型において、非リーフのインデックスページを走査するコードが誤った比較関数を適用していたため、誤った結果や潜在的なクラッシュを引き起こしていました。

---

<a id="item-73"></a>

### [No.73] hstore/jsonbのPL/Perl・PL/Python連携における再帰・ループガード

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- サーバープロセスのスタック枯渇・ハング防止。

#### アプリ影響・対応策
- 巨大・複雑なネスト構造を持つ JSONB や、循環参照を含む Perl/Python 構造体を扱うストアド関数の安定性が大幅に向上します。

#### 英語原文 (Original English)
```text
Fix unguarded recursion and loops in contrib/hstore_plperl, contrib/jsonb_plperl, and contrib/jsonb_plpython (Aleksander Alekseev)

Prevent stack overflow when dealing with deeply nested jsonb values, and allow interruption of the infinite loop caused when attempting to dereference circular chains of Perl object references.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/hstore_plperl、contrib/jsonb_plperl、および contrib/jsonb_plpython における無防備な再帰およびループを修正しました。(Aleksander Alekseev)

> 深くネストされた jsonb 値を処理する際のスタックオーバーフローを防止し、Perl オブジェクト参照の循環チェーンを逆参照しようとした際に発生する無限ループの中断を可能にしました。

---

<a id="item-74"></a>

### [No.74] contrib/intarrayにおける統計カタログキャッシュ解放漏れ修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 【ログクリーン化】intarray 利用時に PostgreSQL ログに出力されていたリソース未解放警告メッセージが解消されます。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Fix missed release of statistics catcache entry in contrib/intarray (Man Zeng)

This oversight led to warnings like “resource was not closed: cache pg_statistic”.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/intarray において、統計カタログキャッシュエントリの解放漏れを修正しました。(Man Zeng)

> この見落としにより、「resource was not closed: cache pg_statistic」などの警告が発生していました。

---

<a id="item-75"></a>

### [No.75] contrib/ltreeにおける比較時の整数オーバーフロー修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **あり** |

#### インフラ影響・対応策
- 【要REINDEX確認】多数の階層（14,653ラベル超）を持つ ltree 値を格納しているインデックスが存在する場合、更新後に `REINDEX` の実行が必要です。

#### アプリ影響・対応策
- 超多階層の ltree データのソート・比較処理における不正確な結果が解消されます。

#### 英語原文 (Original English)
```text
In contrib/ltree, fix integer overflow in comparisons (Ayush Tiwari)

ltree values containing more than about 14,653 labels resulted in wrong comparison answers due to overflow. If a btree index contains such values, it is probably corrupt and should be reindexed after installing this update.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/ltree において、比較時における整数オーバーフローを修正しました。(Ayush Tiwari)

> 約 14,653 個を超えるラベルを含む ltree 値は、オーバーフローが原因で誤った比較結果をもたらしていました。btree インデックスにそのような値が含まれている場合、そのインデックスはおそらく破損しているため、このアップデートをインストールした後に再構築（reindex）する必要があります。

---

<a id="item-76"></a>

### [No.76] contrib/pg_surgeryの配列境界外書き込み修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 破損テーブル復旧用モジュール pg_surgery を実行した際の予期せぬサーバークラッシュを防止します。

#### アプリ影響・対応策
- 通常のアプリケーション利用には影響ありません。

#### 英語原文 (Original English)
```text
Fix array overrun in contrib/pg_surgery's heap_force_kill and heap_force_freeze functions (Michael Paquier)

Attempting to change a TID whose offset number equals MaxHeapTuplesPerPage wrote one byte past the end of the allocated array, potentially crashing the server.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/pg_surgery の heap_force_kill および heap_force_freeze 関数における配列オーバーランを修正しました。(Michael Paquier)

> オフセット番号が MaxHeapTuplesPerPage に等しい TID を変更しようとすると、確保された配列の終端を1バイト超えて書き込みが行われ、サーバーがクラッシュする可能性がありました。

---

<a id="item-77"></a>

### [No.77] contrib/pg_surgeryにおける64K超のTID配列での無限ループ回避

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 大量のタプル強制修復バッチ処理時のプロセスハングを防止します。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
In contrib/pg_surgery, avoid infinite loop with TID arrays having more than 64K elements (Andrey Rachitskiy)
```

#### 日本語翻訳 (Japanese Translation)
> contrib/pg_surgery において、64K（65,536）個を超える要素を持つ TID 配列での無限ループを回避しました。(Andrey Rachitskiy)

---

<a id="item-78"></a>

### [No.78] contrib/refintのcheck_foreign_key()におけるNULLポインタ参照修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | `関連: CVE-2026-6637` |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- クラッシュ防止。

#### アプリ影響・対応策
- レガシーな refint 拡張機能を用いて外部キーカスケード更新を行っている環境で、NULL値更新時のクラッシュが解消されます。

#### 英語原文 (Original English)
```text
Avoid NULL-pointer dereference in contrib/refint's check_foreign_key() (Ayush Tiwari)

In the on-update-cascade case, a null value of a referenced column led to a crash. This is an oversight in the fix for CVE-2026-6637, but the code that was there before that wasn't really right either.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/refint の check_foreign_key() における NULL ポインタ逆参照を回避しました。(Ayush Tiwari)

> ON UPDATE CASCADE のケースにおいて、参照される列が NULL 値である場合にクラッシュが発生していました。これは CVE-2026-6637 の修正における見落としですが、それ以前に存在していたコードも実際には正しくありませんでした。

---

<a id="item-79"></a>

### [No.79] contrib/segのチルダ（~）確実性インジケータ出力修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- データ出力フォーマットの正常化。

#### アプリ影響・対応策
- seg 型データ（間隔・範囲）を文字列出力・再入力する際の区間境界の欠落やフォーマット異常が解消されます。

#### 英語原文 (Original English)
```text
Fix contrib/seg to print segments with ~ certainty indicators correctly (Ewan Young)

Due to a typo, seg_out() did not print a ~ certainty indicator attached to a segment's upper boundary. Worse, if the lower boundary had ~ while the upper boundary had no indicator, the upper boundary was not printed at all, incorrectly converting the value into an open interval.
```

#### 日本語翻訳 (Japanese Translation)
> contrib/seg において、~ 確実性インジケータ（certainty indicators）を伴うセグメントを正しく出力するよう修正しました。(Ewan Young)

> タイポにより、seg_out() はセグメントの上限境界に付加された ~ 確実性インジケータを出力していませんでした。さらに悪いことに、下限境界に ~ があり上限境界にインジケータがない場合、上限境界がまったく出力されず、値が誤って開区間に変換されていました。

---

<a id="item-80"></a>

### [No.80] contrib/xml2のxpath_nodeset()における名前空間ノードクラッシュ修正

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | 拡張モジュール (contrib) |
| **CVE番号** | なし |
| **インフラ影響** | **なし** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- サーバークラッシュ防止。

#### アプリ影響・対応策
- contrib/xml2 を使用して名前空間を含む XML データを処理するクエリの安定性が向上します。

#### 英語原文 (Original English)
```text
Fix crash with namespace nodes in contrib/xml2's xpath_nodeset() function (Andrey Chernyy, Michael Paquier)
```

#### 日本語翻訳 (Japanese Translation)
> contrib/xml2 の xpath_nodeset() 関数において、名前空間ノードによるクラッシュを修正しました。(Andrey Chernyy, Michael Paquier)

---

<a id="item-81"></a>

### [No.81] Visual Studio 2026によるPostgreSQLビルドのサポート

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | ビルド・プラットフォーム |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- Windows 環境でソースコードからビルド・運用を行っているインフラにおいて、最新の MSVC 2026 ツールチェーンが利用可能になります。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Support building PostgreSQL with Visual Studio 2026 (Andrew Dunstan)
```

#### 日本語翻訳 (Japanese Translation)
> Visual Studio 2026 による PostgreSQL のビルドをサポートしました。(Andrew Dunstan)

---

<a id="item-82"></a>

### [No.82] OpenSSL 4によるPostgreSQLビルドのサポート

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | ビルド・プラットフォーム |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **なし** |

#### インフラ影響・対応策
- 次世代 OS や最新ディストリビューションに導入される OpenSSL 4 系とのライブラリ互換性が確保されます。

#### アプリ影響・対応策
- アプリケーションへの影響はありません。

#### 英語原文 (Original English)
```text
Support building PostgreSQL with OpenSSL 4 (Daniel Gustafsson)
```

#### 日本語翻訳 (Japanese Translation)
> OpenSSL 4 による PostgreSQL のビルドをサポートしました。(Daniel Gustafsson)

---

<a id="item-83"></a>

### [No.83] タイムゾーンデータファイルのtzdata release 2026cへの更新

| 属性 | 内容 |
| :--- | :--- |
| **大分類** | ビルド・プラットフォーム |
| **CVE番号** | なし |
| **インフラ影響** | **あり** |
| **アプリ影響** | **条件付きあり** |

#### インフラ影響・対応策
- 【時刻同期・TZ更新】データベース内のタイムゾーン定義が 2026c に更新されます。カナダ・アルバータ州およびモロッコの時間帯を扱うシステムにおいて、夏時間変更や標準時のずれが解消されます。

#### アプリ影響・対応策
- 該当地域（アルバータ州、モロッコ等）の現地時間と UTC の相互変換を行うアプリケーションにおいて、日付・時刻の計算結果が改定後のルールに従って正確になります。

#### 英語原文 (Original English)
```text
Update time zone data files to tzdata release 2026c (Tom Lane)

Alberta (America/Edmonton) will be on year-round UTC-06 (effectively, permanent DST) beginning in November 2026. This release assumes that their TZ abbreviation will be CST from that time forward. That seems likely to change, but it's unclear what new abbreviation will be used.

Morocco (Africa/Casablanca) will move to permanent UTC+00, without daylight saving time transitions, on 2026-09-20.
```

#### 日本語翻訳 (Japanese Translation)
> タイムゾーンデータファイルを tzdata release 2026c に更新しました。(Tom Lane)

> カナダ・アルバータ州（America/Edmonton）は、2026年11月より通年 UTC-06（事実上、恒久的な夏時間）に移行します。本リリースでは、その時点以降のタイムゾーン略称を CST と想定しています。これは変更される可能性が高そうですが、どのような新しい略称が使用されるかは現時点では不明です。

> モロッコ（Africa/Casablanca）は、2026年9月20日に夏時間への移行を行わず、恒久的な UTC+00 に移行します。

---
