
# Title: October 31, 2025 
Link: https://docs.cloud.google.com/release-notes#October_31_2025<br>
インフラエンジニアとして、提供されたGoogle Cloudのリリースノートについて、構築済みのサービスへの影響を調査し、以下の通りご報告いたします。

---

# AlloyDB for PostgreSQL
## Announcement
原文: The `alloydb_scann` extension version `0.1.3` is updated to include the following vector search improvements, which are now Generally Available (GA):

[GA](https://cloud.google.com/products#product-launch-stages)
- The columnar engine now automatically includes vector columns in searches, so you don't need to add them to the table manually.
For more information, see Perform a vector search.
- You can use the `pg_stat_ann_index_creation` view for metrics about the number of rows at index creation. For more information, see Vector index metrics.

[Perform a vector search](https://docs.cloud.google.com/alloydb/docs/ai/perform-vector-search#accelerate-filtered-vector-search)
[Vector index metrics](https://docs.cloud.com/alloydb/docs/ai/tune-indexes?resource=scann#vector-index-metrics)

説明: AlloyDB for PostgreSQLのベクトル検索機能を提供する`alloydb_scann`拡張機能がバージョン`0.1.3`に更新され、以下の改善点がGA（Generally Available）となりました。
1.  カラム型エンジンにおいて、ベクトルカラムが検索に自動的に含まれるようになり、手動での追加が不要になりました。
2.  `pg_stat_ann_index_creation`ビューを使用して、インデックス作成時の行数に関するメトリクスが取得可能になりました。これにより、ベクトルインデックスのチューニングと監視が強化されます。

影響有無: 影響なし。
本更新は、AlloyDB for PostgreSQLの`alloydb_scann`拡張機能に新機能を追加し、既存機能の改善を行うものです。既存のワークロードに非互換性のある変更は含まれておらず、既存のAlloyDB for PostgreSQLインスタンスの動作に直接的な影響はありません。ベクトル検索機能を利用している場合は、パフォーマンス向上や運用監視の恩恵を受けることができます。

対処方法: 特段の対応は不要です。
既存のAlloyDB for PostgreSQLをご利用の場合、この更新は自動的に適用されます。ベクトル検索機能のパフォーマンス最適化や監視強化をご検討の際は、上記の新機能の活用を推奨します。

用語説明:
*   **AlloyDB for PostgreSQL**: Google Cloudが提供する、エンタープライズグレードのフルマネージドなPostgreSQL互換データベースサービスです。高性能と高可用性を特長とします。
*   **`alloydb_scann` extension**: AlloyDBにおいて、高性能なベクトル検索機能を提供する拡張機能です。AI/MLアプリケーションにおける類似性検索などで利用されます。
*   **ベクトル検索**: データ（テキスト、画像など）を多次元の数値ベクトルに変換し、ベクトル間の類似性に基づいて情報を検索する手法です。
*   **GA (Generally Available)**: Google Cloud製品や機能が一般提供され、SLA（Service Level Agreement）によってサポートされる状態を指します。

---

# Apigee X
## Announcement
原文: On October 31, 2025, we released an updated version of Apigee (1-16-0-apigee-4).

> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigeeの新しいバージョン`1-16-0-apigee-4`がリリースされました。リリースは2025年10月31日から開始され、全てのGoogle Cloudゾーンへの展開には4営業日以上かかる可能性があります。このロールアウト期間中、ご利用のApigeeインスタンスでは、新しい機能や修正がすぐに利用できない場合があります。

影響有無: 影響なし。
Apigee Xはフルマネージドサービスであるため、ユーザー側でのバージョンアップ作業は不要です。アップデートはGoogle Cloudによって自動的に適用されます。ただし、リリースノートに記載されている通り、新機能や修正が全てのゾーンに反映されるまでには時間を要する可能性があるため、その期間は注意が必要です。

対処方法: 特段の対応は不要です。
新機能の利用を計画している場合は、展開状況を考慮し、ロールアウト完了後に利用可能となることを確認してください。

## Security
原文: | Bug ID | Description |
| --- | --- |
| **452621774, 452381632, 441266643, 448498138** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:- CVE-2025-53864Updated Nimbus JWT library from 9.37.2 to 9.37.4, which introduced changes in behavior including changes to error string verbiage.- CVE-2025-8916- CVE-2025-5115- CVE-2024-40094 |
This addresses the following vulnerabilities:- CVE-2025-53864Updated Nimbus JWT library from 9.37.2 to 9.37.4, which introduced changes in behavior including changes to error string verbiage.- CVE-2025-8916- CVE-2025-5115- CVE-2024-40094

- CVE-2025-53864Updated Nimbus JWT library from 9.37.2 to 9.37.4, which introduced changes in behavior including changes to error string verbiage.- CVE-2025-8916- CVE-2025-5115- CVE-2024-40094

[CVE-2025-53864](https://nvd.nist.gov/vuln/detail/CVE-2025-53864)
Updated Nimbus JWT library from 9.37.2 to 9.37.4, which introduced changes in behavior including changes to error string verbiage.

[CVE-2025-8916](https://nvd.nist.gov/vuln/detail/CVE-2025-8916)
[CVE-2025-5115](https://nvd.nist.gov/vuln/detail/CVE-2025-5115)
[CVE-2024-40094](https://nvd.nist.gov/vuln/detail/CVE-2024-53864)

説明: Apigeeインフラストラクチャに対してセキュリティ修正が適用されました。この修正は、以下の複数の脆弱性に対処するものです。
*   CVE-2025-53864: Nimbus JWTライブラリがバージョン9.37.2から9.37.4に更新されました。これにより、エラー文字列の表現など、一部の動作に変更が生じる可能性があります。
*   CVE-2025-8916
*   CVE-2025-5115
*   CVE-2024-40094

影響有無: 影響は限定的。
本修正により、Apigee環境のセキュリティ体制が強化されます。機能的な非互換性はありませんが、CVE-2025-53864に関連して、JWTの処理においてエラーメッセージの文字列表現が変更される可能性があります。もし、ApigeeのJWT関連のエラーメッセージに特定のパターンマッチングなどを依存している場合は、影響を受ける可能性があります。

対処方法: 特段の対応は不要です。
Apigee Xはフルマネージドサービスであり、セキュリティパッチはGoogle Cloudによって自動的に適用されます。Nimbus JWTライブラリのエラー文字列の変更が懸念される場合は、テスト環境でJWT関連の処理が期待通りに動作することを確認することを推奨します。

用語説明:
*   **Apigee X**: Google Cloudが提供するフルマネージドなAPI管理プラットフォームです。APIの設計、セキュリティ、デプロイ、監視、収益化を支援します。
*   **CVE (Common Vulnerabilities and Exposures)**: ソフトウェアやシステムのセキュリティ脆弱性に割り当てられる共通の識別子です。
*   **JWT (JSON Web Token)**: JSON形式のデータを安全に表現するためのコンパクトな標準規格です。API認証などで広く利用されます。

## Fixed
原文: | Bug ID | Description |
| --- | --- |
| **448647917** | **Fixed a issue where non-SSL connections through a forward proxy could be improperly shared.** |
| **N/A** | **Updates to security, infrastructure, and libraries.** |

説明: 以下の問題が修正されました。
*   フォワードプロキシ経由の非SSL接続が不適切に共有される問題が修正されました。
*   セキュリティ、インフラストラクチャ、およびライブラリの更新が含まれています。

影響有無: 影響なし（機能改善）。
これらの修正は、Apigeeの安定性と信頼性を向上させるものです。特に、フォワードプロキシを介した非SSL接続を利用している環境では、安定性の向上が期待できます。

対処方法: 特段の対応は不要です。
バグ修正は自動的に適用されます。

---

# Cloud Load Balancing
## Changed
原文: The global and classic external Application Load Balancers implemented on
Google Front-Ends (GFEs) now reject TLS connections when the client and the load
balancer support ALPN (Application-Layer Protocol Negotiation), but don't share
common ALPN protocols.

Previously, if a client proposed a list of application protocols during the TLS
handshake using the ALPN extension and none were supported by the load balancer,
ALPN would be deactivated and the connection would default to using HTTP/1 as
the default application protocol. After this update, the GFE instead returns
an `SSL_TLSEXT_ERR_ALERT_FATAL` response which causes the load balancer to
terminate the TLS handshake, and the connection to close. This change ensures
that an application-layer protocol is always explicitly negotiated between the
clients and the load balancers that support ALPN.

説明: Google Front-Ends (GFE) 上に実装されているグローバルおよびクラシックな外部アプリケーションロードバランサーにおいて、ALPN（Application-Layer Protocol Negotiation）をサポートするクライアントとロードバランサー間で共通のALPNプロトコルが合意できない場合、TLS接続を拒否するようになりました。
これまでは、クライアントが提示したALPNプロトコルリストにロードバランサーがサポートするプロトコルが含まれていない場合、ALPNは無効化され、接続はHTTP/1にフォールバックしていました。この変更により、ロードバランサーは`SSL_TLSEXT_ERR_ALERT_FATAL`エラーを返し、TLSハンドシェイクを終了させ、接続を閉じます。これにより、ALPNをサポートするクライアントとロードバランサー間では、常にアプリケーション層プロトコルが明示的にネゴシエートされることが保証されます。

影響有無: 影響あり。
ALPNを使用してCloud Load Balancingに接続するクライアントで、過去にロードバランサーと共通のプロトコルが合意できず、HTTP/1への暗黙的なフォールバックに依存していたものがある場合、今回の変更により接続が失敗するようになります。これにより、該当するクライアントアプリケーションからのアクセスが停止する可能性があります。

対処方法:
1.  Cloud Load Balancingを使用している環境で、ALPNを有効にしているクライアントアプリケーションがないか確認してください。
2.  ALPNを使用するクライアントが存在する場合、そのクライアントがCloud Load BalancingがサポートするALPNプロトコル（例: HTTP/1.1, HTTP/2）を正しくネゴシエートできることを確認してください。
3.  特に、ALPNネゴシエーションに失敗した場合にHTTP/1へのフォールバックに依存していたレガシーなクライアントアプリケーションがないか、影響を受ける可能性のあるクライアントについてテスト環境で接続検証を実施してください。
4.  必要に応じて、クライアント側のALPN設定を調整するか、ロードバランサーがサポートするプロトコルに適合させるようにクライアントアプリケーションを更新してください。

用語説明:
*   **Google Front-Ends (GFEs)**: Googleのグローバルネットワークエッジに配置された分散システムで、Google Cloudのロードバランシング、DDoS保護、TLS終端などの機能を提供します。
*   **ALPN (Application-Layer Protocol Negotiation)**: TLSハンドシェイク中に、クライアントとサーバー間でアプリケーション層プロトコル（例: HTTP/1.1やHTTP/2）を安全にネゴシエートするためのTLS拡張機能です。
*   **TLSハンドシェイク**: TLS (Transport Layer Security) セッションを確立するために、クライアントとサーバー間で通信を暗号化するための鍵交換や認証などが行われる初期プロセスです。

---

# Compute Engine
## Fixed
原文: Version `20251030.02` includes fixes for the plugin-based architecture that is used by guest agent. For more information about the plugin-based architecture, see Guest agent.

[Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent)
- The Clock Skew module no longer causes time inconsistencies on VMs. The agent no longer attempts to synchronize the hardware clock (`hwclock`) when the VM's Real-time Clock (RTC) isn't set to Coordinated Universal Time 0(UTC). For more information about how the guest agent handles clock synchronization, see Clock Synchronization.
- The Dynamic VLAN module now correctly sets up VLAN network interface cards (NICs). Dynamic VLAN connections now initialize reliably.
- The agent now prevents a race condition in network interface and route setup. Previously, routes were temporarily flushed if they were added before a DHCP lease was acquired. The agent now ensures routes persist correctly, preventing a brief period of missing routes. These routes were previously auto-corrected after approximately one minute.

[Clock Synchronization](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#clock-synchronization)
[Dynamic VLAN](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)

説明: Compute Engineのゲストエージェントが使用するプラグインベースのアーキテクチャに対して、バージョン`20251030.02`で以下の修正が含まれました。
1.  Clock SkewモジュールがVM上で時刻の不整合を引き起こさなくなりました。VMのリアルタイムクロック（RTC）がUTCに設定されていない場合、ゲストエージェントはハードウェアクロック（`hwclock`）の同期を試みなくなります。
2.  Dynamic VLANモジュールがVLANネットワークインターフェースカード（NIC）を正しくセットアップするようになり、動的VLAN接続が安定して初期化されるようになりました。
3.  ネットワークインターフェースとルート設定における競合状態が防止されます。以前は、DHCPリース取得前にルートが追加された場合、一時的にルートが失われることがありましたが、エージェントはルートが正しく永続化されることを保証し、一時的なルートの欠落を防ぎます。

影響有無: 影響なし（安定性向上）。
本修正はCompute Engine VMのゲストエージェントに関するものであり、VMの時刻同期、ネットワークインターフェース設定、ルーティングの信頼性と安定性が向上します。既存のVMの動作に非互換性のある変更はなく、潜在的な問題の解消につながるため、プラスの影響です。

対処方法: 特段の対応は不要です。
Compute Engineのゲストエージェントは通常、自動的に更新されます。これにより、VMの安定性と信頼性が向上します。VMの時刻不整合やVLAN接続の不安定さ、ネットワークルートの一時的な欠落といった問題に遭遇していた場合、これらの修正により問題が解消されることが期待されます。

用語説明:
*   **ゲストエージェント (Guest agent)**: Compute Engine VMインスタンス内で動作し、VMとGoogle Cloudプラットフォーム間の通信や、特定のVM機能（例: 時刻同期、Windowsでのパスワードリセットなど）をサポートするソフトウェアです。
*   **Clock Skew**: コンピュータシステムにおいて、内部クロックと参照時刻源との間に生じるずれや不整合を指します。
*   **Real-time Clock (RTC)**: コンピュータの電源が切れている間も、日付と時刻を保持するために使用される独立した時計です。
*   **UTC (Coordinated Universal Time)**: 協定世界時。国際的な時刻の基準です。
*   **Dynamic VLAN**: ネットワーク接続要件に応じて、動的にVLAN（Virtual Local Area Network）接続を確立する機能です。
*   **競合状態 (Race condition)**: 複数のプロセスやスレッドが共有リソースに同時にアクセスしようとすることで、その実行順序によって結果が変化する、予期せぬ動作を引き起こす可能性のある状況を指します。