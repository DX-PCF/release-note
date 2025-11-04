
# Title: October 31, 2025 
Link: https://docs.cloud.google.com/release-notes#October_31_2025<br>
承知いたしました。Google Cloudのリリースノートに基づき、各製品の変更点についてインフラエンジニアの視点から調査し、影響有無と対処方法を以下の通り回答いたします。

---

# AlloyDB for PostgreSQL
## Announcement
原文: The `alloydb_scann` extension version `0.1.3` is updated to include the following vector search improvements, which are now Generally Available (GA):
- The columnar engine now automatically includes vector columns in searches, so you don't need to add them to the table manually.
- You can use the `pg_stat_ann_index_creation` view for metrics about the number of rows at index creation.

説明：
AlloyDB for PostgreSQLの `alloydb_scann` 拡張機能がバージョン `0.1.3` に更新され、ベクタ検索機能がGA（一般提供）として利用可能になりました。今回の更新により、列指向エンジンはベクタ検索時にベクタ列を自動的に含めるため、手動でのテーブル追加が不要になります。また、インデックス作成時の行数に関するメトリックを取得するために `pg_stat_ann_index_creation` ビューが提供されます。

影響有無：影響なし。
理由：これは既存機能の強化および新機能のGAアナウンスであり、既存のシステム構成や動作に破壊的な変更をもたらすものではありません。AlloyDBでベクタ検索を利用していない環境には直接的な影響はありません。利用している場合でも、既存のアプリケーションに修正は不要で、利便性の向上と追加の監視機能が提供されるため、ポジティブな影響のみとなります。

対処方法：なし。
必要であれば、新機能を活用してベクタ検索の効率化（ベクタ列の自動インクルード）やモニタリング強化（`pg_stat_ann_index_creation`ビューの利用）を検討できます。

用語説明：
- **AlloyDB for PostgreSQL**: Google Cloudが提供するエンタープライズグレードのPostgreSQL互換リレーショナルデータベースサービスです。高いパフォーマンス、可用性、スケーラビリティを特徴とします。
- **`alloydb_scann` 拡張機能**: AlloyDBで高性能なベクタ検索を実現するためのPostgreSQL拡張機能です。Googleが開発した近傍検索ライブラリであるScannを利用しています。
- **ベクタ検索 (Vector Search)**: テキスト、画像、音声などの非構造化データを数値ベクトル（埋め込みベクトル）に変換し、ベクトル間の類似度に基づいて関連性の高いデータを検索する技術です。AIアプリケーションやレコメンデーションシステムなどで利用されます。
- **GA (Generally Available)**: Google Cloudにおける製品や機能のライフサイクル段階の一つで、一般提供状態を指します。本番環境での利用が推奨され、SLA（サービスレベル契約）が適用されるのが一般的です。
- **列指向エンジン (Columnar Engine)**: データを列ごとに物理的に格納するデータベースエンジンです。行指向に比べて、特定の列に対する集計クエリや分析クエリのパフォーマンスが優れています。

---

# Apigee X
## Announcement
原文: On October 31, 2025, we released an updated version of Apigee (1-16-0-apigee-4).
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
Apigeeの新しいバージョン（1-16-0-apigee-4）がリリースされました。このリリースは2025年10月31日に開始され、すべてのGoogle Cloudゾーンへのロールアウトが完了するまでに4営業日以上かかる場合があります。ロールアウトが完了するまでは、各インスタンスで新しい機能や修正が利用できない可能性があります。

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **452621774, 452381632, 441266643, 448498138** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:- CVE-2025-53864Updated Nimbus JWT library from 9.37.2 to 9.37.4, which introduced changes in behavior including changes to error string verbiage.- CVE-2025-8916- CVE-2025-5115- CVE-2024-40094 |

説明：
Apigeeインフラストラクチャに対する複数のセキュリティ修正が適用されました。これには、以下のCVE（Common Vulnerabilities and Exposures）に特定される脆弱性への対応が含まれます。
- CVE-2025-53864: Nimbus JWTライブラリがバージョン9.37.2から9.37.4に更新され、これによりエラー文字列の表現など一部の動作に変更が生じています。
- CVE-2025-8916
- CVE-2025-5115
- CVE-2024-40094

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **448647917** | **Fixed a issue where non-SSL connections through a forward proxy could be improperly shared.** |
| **N/A** | **Updates to security, infrastructure, and libraries.** |

説明：
以下の不具合が修正されました。
- フォワードプロキシを介した非SSL接続が不適切に共有される問題が修正されました。
- セキュリティ、インフラストラクチャ、および各種ライブラリに対する一般的な更新が含まれています。

影響有無：影響あり（ポジティブな影響）。
理由：このリリースには複数のセキュリティ脆弱性への対応とバグ修正が含まれており、Apigeeサービスの安定性、セキュリティ、および信頼性が向上します。特に、CVE脆弱性への対応はセキュリティリスクを低減する上で重要です。Apigeeはマネージドサービスであるため、通常、ユーザー側での明示的なアップグレード作業は不要ですが、ロールアウト期間中（数日間）は、新機能や修正が環境に完全に反映されていない可能性がある点に留意が必要です。Nimbus JWTライブラリの更新によるエラーメッセージの変更は、ログ解析システムや監視アラートに微細な影響を与える可能性がゼロではありませんが、一般的な運用には直接影響しないと想定されます。

対処方法：なし。
Google Cloudによって自動的に修正が適用されます。ただし、リリースノートに記載されている通り、ロールアウトには時間がかかる場合があるため、その期間はサービスが意図したバージョンで動作しているか、または必要な修正が適用されているかについて監視を継続することが推奨されます。更新されたNimbus JWTライブラリのエラーメッセージ変更が既存のログ解析や自動化ワークフローに影響を与えないか、必要に応じて確認することを検討してください。

用語説明：
- **Apigee X**: Google Cloud上で提供される、API（Application Programming Interface）の設計、保護、デプロイ、監視、分析を包括的に行うためのAPI管理プラットフォームです。
- **CVE (Common Vulnerabilities and Exposures)**: 広く認識されているソフトウェアのセキュリティ脆弱性に対して割り当てられる、一意の識別子を持つリストです。
- **Nimbus JWT library**: JavaでJSON Web Token (JWT) の生成、署名、検証、解析を行うためのオープンソースライブラリです。
- **フォワードプロキシ (Forward Proxy)**: クライアントからのリクエストを受け取り、そのリクエストをインターネット上のサーバーに中継するプロキシサーバーです。クライアントの匿名性を確保したり、アクセス制御を行ったりする目的で利用されます。

---

# Cloud Load Balancing
## Changed
原文: The global and classic external Application Load Balancers implemented on Google Front-Ends (GFEs) now reject TLS connections when the client and the load balancer support ALPN (Application-Layer Protocol Negotiation), but don't share common ALPN protocols.
Previously, if a client proposed a list of application protocols during the TLS handshake using the ALPN extension and none were supported by the load balancer, ALPN would be deactivated and the connection would default to using HTTP/1 as the default application protocol. After this update, the GFE instead returns an `SSL_TLSEXT_ERR_ALERT_FATAL` response which causes the load balancer to terminate the TLS handshake, and the connection to close. This change ensures that an application-layer protocol is always explicitly negotiated between the clients and the load balancers that support ALPN.

説明：
グローバルおよび従来の外部アプリケーションロードバランサ（Google Front-Ends (GFEs) 上で実装）は、クライアントとロードバランサがALPN（Application-Layer Protocol Negotiation）をサポートしているにもかかわらず、共通のALPNプロトコル（例: HTTP/1.1, HTTP/2）を共有しない場合に、TLS接続を拒否するようになりました。
以前は、このような状況ではALPNが無効化され、接続はデフォルトでHTTP/1プロトコルにフォールバックしていました。しかし今回の更新により、GFEは `SSL_TLSEXT_ERR_ALERT_FATAL` レスポンスを返し、ロードバランサがTLSハンドシェイクを終了させ、接続を閉じるようになります。この変更は、ALPNをサポートするクライアントとロードバランサ間でアプリケーション層プロトコルが常に明示的にネゴシエートされることを保証するためのものです。

影響有無：影響あり。
理由：これまではALPNネゴシエーションが失敗した場合にHTTP/1にフォールバックして接続が維持されていましたが、今回の変更により、共通のALPNプロトコルがない場合はTLSハンドシェイク自体が失敗し、接続が確立されなくなります。これにより、特定のALPNプロトコル（例: HTTP/2）を期待して接続を試みるクライアントが、ロードバランサ側でそのプロトコルがサポートされていない場合、接続エラーが発生する可能性があります。サービスによっては、クライアント側のアプリケーションの接続挙動に影響が出る可能性があります。

対処方法：
ロードバランサを介して接続するクライアントが、ロードバランサがサポートするALPNプロトコル（例：HTTP/1.1、HTTP/2）を正しくネゴシエートできることを確認してください。特に、HTTP/2など特定のアプリケーションプロトコルを期待しているクライアントや、多様なALPN設定を持つクライアントからの接続について、接続エラーが発生していないかモニタリングを強化してください。必要に応じて、クライアント側のALPN設定や、ロードバランサのプロトコル設定（例えば、HTTPSターゲットプロキシの `alpn_protocols` 設定など）を見直してください。

用語説明：
- **Cloud Load Balancing**: Google Cloudが提供するフルマネージドのロードバランシングサービスです。ネットワークトラフィックを複数のバックエンドインスタンスに効率的に分散し、サービスの可用性とスケーラビリティを向上させます。
- **Google Front-Ends (GFE)**: Googleのグローバルネットワークエッジに配置された、高度に分散されたシステムです。Google Cloudの多くのサービス（Cloud Load Balancingを含む）への入り口として機能し、TLS終端、DDoS防御、ルーティングなどを担当します。
- **ALPN (Application-Layer Protocol Negotiation)**: TLS（Transport Layer Security）ハンドシェイク中に、クライアントとサーバーがどのアプリケーション層プロトコル（例: HTTP/1.1, HTTP/2）を使用するかを安全にネゴシエートするためのTLS拡張です。
- **TLSハンドシェイク**: クライアントとサーバー間で安全な通信チャネルを確立するために行われる一連のプロトコルステップです。暗号スイートの選択、キーの交換、サーバー認証などが行われます。
- **HTTP/1.1 と HTTP/2**: HTTP/1.1は広く利用されてきたHTTPプロトコルの標準バージョンです。HTTP/2はHTTP/1.1を基盤とし、多重化、ヘッダー圧縮、サーバープッシュなどの新機能により、Webパフォーマンスを大幅に向上させたプロトコルです。

---

# Compute Engine
## Fixed
原文: Version `20251030.02` includes fixes for the plugin-based architecture that is used by guest agent.
- The Clock Skew module no longer causes time inconsistencies on VMs. The agent no longer attempts to synchronize the hardware clock (`hwclock`) when the VM's Real-time Clock (RTC) isn't set to Coordinated Universal Time 0(UTC).
- The Dynamic VLAN module now correctly sets up VLAN network interface cards (NICs). Dynamic VLAN connections now initialize reliably.
- The agent now prevents a race condition in network interface and route setup. Previously, routes were temporarily flushed if they were added before a DHCP lease was acquired. The agent now ensures routes persist correctly, preventing a brief period of missing routes.

説明：
Compute Engineのゲストエージェントが使用するプラグインベースのアーキテクチャに対する修正を含むバージョン `20251030.02` がリリースされました。具体的には以下の点が修正されています。
- クロックスキューモジュールがVMの時刻不整合を引き起こさなくなりました。VMのReal-time Clock (RTC) がUTC（協定世界時）に設定されていない場合、ゲストエージェントはハードウェアクロック（`hwclock`）の同期を試みなくなります。
- Dynamic VLANモジュールが、VLANネットワークインターフェースカード (NICs) を正しく設定できるようになりました。これにより、Dynamic VLAN接続が安定して初期化されるようになります。
- ゲストエージェントがネットワークインターフェースとルーティング設定における競合状態（race condition）を防ぐようになりました。以前は、DHCPリースが取得される前にルートが追加されると、一時的にルートがフラッシュされていましたが、今後はルートが正しく永続化され、一時的なルーティングの欠落が防止されます。

影響有無：影響あり（ポジティブな影響）。
理由：これらの修正はCompute Engine VMのゲストエージェントにおける複数の既知の問題を解決し、VMの安定性、時刻同期の正確性、およびネットワーク接続の信頼性を向上させます。特に、時刻のずれ、VLAN NIC設定の不具合、ネットワークルーティングの一時的な喪失といった問題に起因する障害のリスクが低減されます。既存のVMの運用において、これらの問題が発生していた場合は改善が見込まれます。

対処方法：なし。
これらの修正はCompute Engineのゲストエージェントの更新によって自動的に適用されます。VMインスタンス上でゲストエージェントが正しく動作していることを確認し、これらの問題に起因する過去の事象が改善されているか継続的に監視することが推奨されます。

用語説明：
- **Compute Engine**: Google Cloudが提供するIaaS（Infrastructure as a Service）であり、柔軟かつスケーラブルな仮想マシン（VM）インスタンスを構築、実行、管理できるサービスです。
- **ゲストエージェント (Guest Agent)**: Compute EngineのVMインスタンス上で動作するソフトウェアコンポーネントです。VMとCompute Engineのインフラストラクチャとの連携を可能にし、OSのメタデータアクセス、シャットダウン、ネットワーク設定など、様々な機能を提供します。
- **クロックスキュー (Clock Skew)**: 分散システムにおいて、異なるコンピュータの時刻がずれること。時刻同期の不整合は、データの一貫性やシステム動作に影響を与える可能性があります。
- **`hwclock`**: Linuxシステムにおいて、ハードウェアクロック（Real-time Clock: RTC）の時刻を設定したり、読み込んだりするためのコマンドです。
- **RTC (Real-time Clock)**: コンピュータのマザーボードに搭載された、電源がオフになっても時刻情報を保持する独立した時計機能です。BIOS/UEFIやOSがこの時刻を参照します。
- **UTC (Coordinated Universal Time)**: 協定世界時。国際的な時間基準であり、世界中の時刻の標準として利用されています。
- **Dynamic VLAN**: Google CloudのDedicated Interconnectなどのサービスで、VLAN（Virtual Local Area Network）アタッチメントを動的に設定・管理する機能です。
- **NIC (Network Interface Card)**: ネットワークインターフェースカード。コンピュータをネットワークに接続するためのハードウェアコンポーネントです。仮想マシンでは仮想NICとして提供されます。
- **競合状態 (Race Condition)**: 複数のプロセスやスレッドが共有リソースに同時にアクセスしようとした際に、それらの実行順序によって結果が不確定になる状況です。

---