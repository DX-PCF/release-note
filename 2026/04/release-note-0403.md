
# Title: April 02, 2026 
Link: https://docs.cloud.google.com/release-notes#April_02_2026<br>
Google Cloudのリリースノートに関する調査依頼、承知いたしました。
以下に、各製品の変更点について、影響有無と対処方法をまとめています。

---

# AlloyDB for PostgreSQL
## Change
原文: You can now enable Advanced Query Insights on primary
clusters
which have secondary clusters configured. Advanced Query Insights is not supported on secondary
clusters. If you perform a switchover, you must re-enable Advanced Query
Insights on the new primary cluster.

[Advanced Query Insights on primary
clusters](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#secondary-cluster-instance)

説明：
AlloyDB for PostgreSQLにおいて、セカンダリクラスタが設定されているプライマリクラスタでもAdvanced Query Insightsを有効にできるようになりました。以前はこれが制限されていましたが、今回の変更によりサポートされます。
ただし、Advanced Query Insights自体はセカンダリクラスタではサポートされません。
また、プライマリクラスタのスイッチオーバー（計画的な切り替え）を実施した場合は、新しいプライマリクラスタでAdvanced Query Insightsを再度有効にする必要がある点にご注意ください。

影響有無：
軽微な影響あり。
この変更は機能追加であり、既存のAlloyDBクラスタの動作に直接的な影響を与えるものではありません。
しかし、AlloyDBを高可用性構成（セカンダリクラスタを保持）で運用しており、Advanced Query Insightsを活用したい場合は、この機能を利用できるようになります。
現在、Advanced Query Insightsを利用していない場合、あるいは単一クラスタ構成の場合は、直接的な影響はありません。
影響として考慮すべきは、**将来的にスイッチオーバーを実施した場合に、新しいプライマリクラスタでAdvanced Query Insightsの再有効化が必要になる運用上の手間**が発生する可能性があることです。

対処方法：
原則として即座の対処は不要です。
*   **Advanced Query Insightsを利用したい場合:** 高可用性構成のAlloyDBクラスタでAdvanced Query Insightsによる詳細なクエリ分析を行いたい場合は、この新機能を活用することを検討してください。
*   **スイッチオーバーを計画している場合:** 計画的なスイッチオーバーを行う際は、新しいプライマリクラスタでAdvanced Query Insightsを再度有効にする手順を運用手順書に組み込むことを推奨します。これにより、分析の中断を防ぐことができます。

用語説明：
*   **AlloyDB for PostgreSQL:** Google Cloudが提供する、PostgreSQL互換の高性能で高可用性、スケーラビリティに優れたマネージドデータベースサービスです。主にトランザクション処理（OLTP）ワークロード向けに設計されています。
*   **Advanced Query Insights:** AlloyDBの機能の一つで、データベースで実行されるクエリのパフォーマンスを詳細に分析し、ボトルネックを特定するための情報を提供する可観測性ツールです。実行時間の長いクエリ、待機イベント、実行プランなどを視覚的に確認できます。
*   **Primary Cluster (プライマリクラスタ):** AlloyDBクラスタにおける、読み書き両方の操作を受け付ける主要なインスタンス群です。
*   **Secondary Cluster (セカンダリクラスタ):** プライマリクラスタの読み取りレプリカとして機能するクラスタで、高可用性、読み取りスケールアウト、または災害復旧（DR）のために利用されます。通常、プライマリとは異なるリージョンやゾーンに配置されます。
*   **Switchover (スイッチオーバー):** 計画的に、現在のプライマリクラスタからセカンダリクラスタへロールを切り替え、セカンダリクラスタを新しいプライマリクラスタに昇格させる操作です。通常、メンテナンスやバージョンアップなどの目的で実行されます。

---

# Cloud Service Mesh
## Announcement
原文: Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation now
supports a limited implementation of the `EnvoyFilter` API. To learn about the
supported fields, extensions, and how to use `EnvoyFilter` for features like
local rate limiting see
Data plane extensibility with `EnvoyFilter`.

[Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility)
 To troubleshoot any issue while configuring, see
Resolving data plane extensibility issues.

[Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility)

説明：
Google CloudのマネージドなサービスメッシュソリューションであるCloud Service Mesh（`TRAFFIC_DIRECTOR`実装）において、`EnvoyFilter` APIの限定的なサポートが開始されました。
これにより、ユーザーはEnvoyプロキシのデータプレーンの動作をより細かくカスタマイズできるようになり、例えばローカルレートリミットなどの特定の機能を実装することが可能になります。
サポートされるフィールドや拡張機能、および`EnvoyFilter`の使用方法に関する詳細情報は、提供されたドキュメントを参照してください。また、設定時のトラブルシューティングガイドも利用可能です。

影響有無：
影響なし。
このアナウンスは新機能の追加であり、既存のCloud Service Meshのデプロイや動作に直接的な影響を与えるものではありません。
Cloud Service Meshを利用している顧客は、この新機能をオプションとして利用するかどうかを選択できます。
**既存のサービスに非互換性のある変更やパフォーマンスへの影響はありません。**
ただし、この機能を利用してEnvoyプロキシをカスタマイズする場合、誤った設定はトラフィックに悪影響を及ぼす可能性があるため、慎重な計画とテストが必要です。

対処方法：
原則として即座の対処は不要です。
Cloud Service Meshを利用しており、以下のようなユースケースがある場合に、この機能の利用を検討してください。
*   Envoyプロキシのデータプレーンの挙動を、既存のCloud Service MeshのAPIでは実現できないレベルでカスタマイズしたい場合。
*   ローカルレートリミットなど、特定の高度なトラフィック管理ポリシーを実装したい場合。
*   Envoyの特定のフィルタや機能を活用したい場合。

機能の利用を検討する際は、必ず提供されている公式ドキュメント（[Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility)）を熟読し、サポートされる機能範囲、ベストプラクティス、および潜在的なリスクを十分に理解した上で、十分なテストを実施してから本番環境に適用してください。

用語説明：
*   **Cloud Service Mesh:** Google Cloudが提供する、Anthos Service Meshを含むサービスメッシュソリューションの総称です。マイクロサービス間のトラフィック管理、セキュリティ、可観測性を一元的に提供します。
*   **Traffic Director:** Google Cloudのマネージドなトラフィックコントロールプレーンサービスです。グローバルなロードバランシング、サービスディスカバリ、ヘルスチェックなど、大規模なマイクロサービス環境におけるネットワークトラフィックの管理と制御を担います。Cloud Service Meshのコントロールプレーンとしても機能します。
*   **Envoy:** Lyftによって開発され、Cloud Native Computing Foundation (CNCF) がホストするオープンソースの高性能なL7（アプリケーション層）プロキシです。サービスメッシュアーキテクチャにおいて、サイドカープロキシとして各サービスインスタンスにデプロイされ、マイクロサービス間のすべてのネットワークトラフィックを処理するデータプレーンの役割を果たします。
*   **EnvoyFilter API:** Istio（そしてCloud Service Meshの基盤となるEnvoy）において、Envoyプロキシの構成を直接カスタマイズするためのAPIリソースです。既存のIstio APIでは表現できないような、より低レベルで詳細なEnvoyの挙動制御を可能にします。非常に強力である反面、誤った設定はトラフィックフローに深刻な影響を与える可能性があります。
*   **Local Rate Limiting (ローカルレートリミット):** レートリミット（一定期間内のリクエスト数を制限する機能）の一種で、各Envoyプロキシインスタンスが自身で処理するリクエストのレートを制限するものです。これは、複数のプロキシインスタンス間で共有されるグローバルなレートリミットとは異なり、個々のインスタンスが過負荷にならないように保護するために使用されます。
# Title: March 31, 2026 
Link: https://docs.cloud.google.com/release-notes#March_31_2026<br>
Google Cloudのインフラエンジニアとして、提供されたリリースノートに基づき、既存サービスへの影響調査結果を以下に報告します。

---

# Apigee X

## Change
原文: **Updated MCP server target endpoint for MCP Discovery Proxies**
With the GA launch of Model Context Protocol (MCP) in Apigee, the structure of the MCP server target endpoint for MCP Discover Proxies has changed to `ORG_NAME.mcp.apigee.internal`.
Private preview customers using the previous format (`mcp.apigee.internal`) are encouraged to update their proxies to reflect the new structure. Existing endpoints using the old format will continue to work, but new endpoints will use the new structure.

説明:
ApigeeのModel Context Protocol (MCP) が一般提供（GA）されたことに伴い、MCP Discovery Proxiesのターゲットエンドポイントのフォーマットが変更されました。以前のプライベートプレビュー版では`mcp.apigee.internal`でしたが、GA版では`ORG_NAME.mcp.apigee.internal`となります。既存の古いフォーマットのエンドポイントは引き続き動作しますが、新規に作成されるエンドポイントは新しいフォーマットを使用します。プライベートプレビュー版を利用していた顧客は、新しいフォーマットに更新することが推奨されています。

影響有無:
*   **影響なし**: 現在、Apigee X でMCP Discovery Proxiesを使用していない場合、直接的な影響はありません。
*   **影響あり（要確認）**: 既存のMCP Discovery Proxiesをプライベートプレビュー版から利用している場合、既存のエンドポイントは動作を継続しますが、新規作成または更新の際には新しいフォーマットを使用する必要があります。互換性の問題ではないため、既存のサービスが即座に停止することはありませんが、将来的な運用を考慮し確認が必要です。

対処方法:
1.  現在MCP Discovery Proxiesを利用していない場合、特に対処は不要です。
2.  将来的にMCP Discovery Proxiesの利用を計画している場合は、新しいエンドポイントフォーマット（`ORG_NAME.mcp.apigee.internal`）を使用して構築してください。
3.  プライベートプレビュー版からMCP Discovery Proxiesを利用している場合は、公式ドキュメントを参照し、必要に応じてプロキシのターゲットエンドポイントを新しいフォーマットに更新することを検討してください。

用語説明:
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームです。APIの設計、デプロイ、セキュリティ、モニタリング、アナリティクスなどを包括的に提供します。
*   **Model Context Protocol (MCP)**: Apigeeのデータプレーンとコントロールプレーン間の通信や、特定の内部サービスの発見（Discovery）に関連するプロトコルです。
*   **MCP Discovery Proxies**: MCPを利用して内部サービスを検出し、トラフィックをルーティングするためのプロキシコンポーネントです。

## Announcement
原文: On March 31st, 2026, we released an updated version of Apigee.
> **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明:
2026年3月31日にApigeeの更新バージョンがリリースされました。このリリースは、全てのGoogle Cloudゾーンにわたって展開が完了するまでに4営業日以上かかる場合があります。展開が完了するまで、お客様のApigeeインスタンスで新機能や修正が利用できない可能性があります。

影響有無:
*   **影響なし**: これはリリース展開に関するアナウンスであり、既存のApigeeサービスに直接的な運用上の影響（サービス停止や設定変更の必要性）はありません。新機能や修正の利用開始時期に関する情報です。

対処方法:
特に対処は不要です。リリースされた新機能や修正を利用する際は、お客様のインスタンスでそれらが利用可能になるまで待機する必要があります。

## Issue
原文: **Known Issue 496552286: Deployment fails for MCP Discovery Proxies in regions with capacity limitations.**
For more information, see Apigee known issues.
[Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)

説明:
既知の問題として、一部のキャパシティ制限があるリージョンにおいて、MCP Discovery Proxiesのデプロイが失敗する事象が報告されています。詳細については、Apigeeの既知の問題ページを参照してください。

影響有無:
*   **影響あり（要確認）**: 現在、MCP Discovery Proxiesを特定のリージョン（特にキャパシティ制限がある可能性のあるリージョン）にデプロイしようとしている場合に影響があります。既にデプロイ済みのサービスには直接影響しませんが、再デプロイや更新時に発生する可能性も考慮すべきです。

対処方法:
1.  もし該当のリージョンでMCP Discovery Proxiesのデプロイを計画している場合は、[Apigee の既知の問題](https://docs.cloud.google.com/apigee/docs/release/known-issues)ページを参照し、この問題の最新情報、ステータス、および推奨される回避策を確認してください。
2.  可能であれば、この問題が解消されるまで、他のリージョンでのデプロイを検討してください。

---

# Cloud NAT

## Announcement
原文: The default TCP `TIME_WAIT` timeout for Cloud NAT is scheduled to decrease from 120 seconds to 30 seconds, across all regions, as follows:
[`TIME_WAIT`](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts)
- **From June 30 to September 29, 2026**: new Cloud NAT gateways will use either the 120-second or 30-second default, depending on when the update is deployed in a specific region.
- **On or after September 30, 2026**: all new Cloud NAT gateways in all regions will use the 30-second default.

**Impact on gateways**
- **New gateways**: after the update is deployed in a region, all new Cloud NAT gateways created in that region will use the 30-second default. This change also applies if a pre-update gateway is deleted and then recreated.
- **Existing gateways**: Cloud NAT gateways created before the regional update will retain the 120-second default. You can adjust this value by using the `--tcp-time-wait-timeout` flag at any time. Cloud NAT gateways configured with a custom `TIME_WAIT` value aren't affected and will continue to use your configured custom value.

The following table outlines the applicable default timeout for new gateways throughout the deployment timeline.

| Gateway type | Default timeout(before June 30) | Default timeout(June 30—September 29) | Default timeout(on or after September 30) |
| --- | --- | --- | --- |
| New | 120 seconds | 30 or 120 seconds | 30 seconds |

説明:
Cloud NATのデフォルトTCP `TIME_WAIT`タイムアウトが、2026年6月30日から9月29日にかけて段階的に、そして2026年9月30日以降は完全に、120秒から30秒に短縮される予定です。

*   **新規ゲートウェイ**: 地域ごとのアップデート後、および2026年9月30日以降に新規作成されるCloud NATゲートウェイは、デフォルトで30秒のTCP `TIME_WAIT`タイムアウトが適用されます。既存のゲートウェイを削除して再作成した場合も同様です。
*   **既存ゲートウェイ**: この変更の影響を受けず、引き続き120秒のデフォルト値を使用します。カスタムで`TIME_WAIT`値を設定しているゲートウェイは、その設定値が維持されます。必要に応じて、`--tcp-time-wait-timeout`フラグを使用して手動で値を調整することも可能です。

影響有無:
*   **既存のCloud NATゲートウェイ**: 既に稼働中のCloud NATゲートウェイは、明示的にタイムアウト値を設定していない場合でも、デフォルトの120秒が維持されるため、直接的な影響はありません。
*   **新規または再作成されるCloud NATゲートウェイ**: 2026年6月30日以降に新規作成または再作成されるCloud NATゲートウェイは、デフォルトのTCP `TIME_WAIT`タイムアウトが30秒となります。TCP `TIME_WAIT`時間が短縮されることで、システムが占有するポートをより早く解放し、新しい接続に利用できるようになるため、高負荷時のポート枯渇のリスクを低減し、TCPコネクションの処理効率が向上する可能性があります。しかし、アプリケーションによっては、短すぎる`TIME_WAIT`タイムアウトがTCP接続の再利用やポート枯渇の挙動に影響を与える可能性がないか確認が必要です。特に、多数の短命なTCP接続を頻繁に行うワークロードにおいては、潜在的な影響を評価する必要があります。

対処方法:
1.  **既存のCloud NATゲートウェイ**: 特に対処は不要です。
2.  **新規または再作成を予定しているCloud NATゲートウェイ**:
    *   アプリケーションが短い`TIME_WAIT`タイムアウト（30秒）で適切に動作するかどうかを評価します。
    *   もし、30秒ではアプリケーションの要件に対して不十分と判断される場合（例：特定のリトライロジックや接続プーリングに影響が出る場合）、Cloud NATゲートウェイ作成時に`--tcp-time-wait-timeout`フラグを用いて、明示的に希望するタイムアウト値（例: `120s`）を設定し、デフォルトの変更の影響を受けないようにしてください。
    *   設定可能な最小値は30秒、最大値は7200秒（2時間）です。
3.  今後の新規NATゲートウェイ作成時には、このデフォルト値変更を念頭に置き、必要に応じて適切な`TIME_WAIT`タイムアウト値を設定するように、構成管理やデプロイスクリプトを見直すことを推奨します。

用語説明:
*   **Cloud NAT**: Google Cloud Virtual Private Cloud (VPC) ネットワーク内のプライベートIPアドレスを持つ仮想マシンインスタンスが、インターネットへのアウトバウンド接続を確立できるようにするサービスです。
*   **TCP `TIME_WAIT`**: TCP接続が正常に終了した後、ソケットが一定期間（デフォルト120秒）保持される状態です。この状態は、遅延したパケットが誤って新しい接続として解釈されるのを防ぎ、前の接続のポートが完全に解放されるまで待機する役割があります。この時間が短いと、ポートの再利用が早まりますが、まれに遅延パケットによる問題が発生する可能性もあります（通常はアプリケーションレベルで適切に処理されます）。
# Title: March 30, 2026 
Link: https://docs.cloud.google.com/release-notes#March_30_2026<br>
Google Cloudのインフラエンジニアとして、ご提示いただいたリリースノートに基づき、構築済みのサービスへの影響有無を調査しました。以下に各製品ごとの分析結果を簡潔にまとめます。

---

# Cloud Logging
## Change
原文: For any new project that is created on or after March 30, 2026, if the project enables the Cloud Logging API, then Google Cloud Observability also enables the Telemetry API.

説明：
2026年3月30日以降に新規作成されるGoogle Cloudプロジェクトにおいて、Cloud Logging APIを有効化すると、Google Cloud Observabilityの一環としてTelemetry APIも自動的に有効化されるようになります。

影響有無：
**無し**。
この変更は「2026年3月30日以降に新規作成されるプロジェクト」にのみ適用されます。現在運用中の既存プロジェクトや、お客様が利用されているCloud Composer2の環境には影響ありません。

対処方法：
**不要**。
既存プロジェクトには影響がないため、特別な対処は必要ありません。将来的に新規プロジェクトを立ち上げる際には、Telemetry APIが自動的に有効化されることを認識しておいてください。

用語説明：
*   **Cloud Logging API**: Google Cloudにおけるログデータを収集、保存、分析するためのプログラマブルインターフェースです。
*   **Google Cloud Observability**: Google Cloudのモニタリング、ロギング、トレースといった機能群を統合したプラットフォームです。旧称はStackdriver。
*   **Telemetry API**: Google Cloud Observabilityの一部として、メトリクス、ログ、トレースなどの様々なテレメトリーデータを収集・処理するための基盤APIです。

---

# Cloud Monitoring
## Change
原文: For any new project that is created on or after March 30, 2026, if the project enables the Cloud Monitoring API, Telemetry API.

説明：
2026年3月30日以降に新規作成されるGoogle Cloudプロジェクトにおいて、Cloud Monitoring APIを有効化すると、Telemetry APIも自動的に有効化されるようになります。

影響有無：
**無し**。
この変更は「2026年3月30日以降に新規作成されるプロジェクト」にのみ適用されます。現在運用中の既存プロジェクトや、お客様が利用されているCloud Composer2の環境には影響ありません。

対処方法：
**不要**。
既存プロジェクトには影響がないため、特別な対処は必要ありません。将来的に新規プロジェクトを立ち上げる際には、Telemetry APIが自動的に有効化されることを認識しておいてください。

用語説明：
*   **Cloud Monitoring API**: Google Cloudのリソースやアプリケーションのパフォーマンス、稼働状況を監視するためのAPIです。カスタムメトリクスやアラート設定などにも利用されます。
*   **Telemetry API**: Google Cloud Observabilityの一部として、メトリクス、ログ、トレースなどの様々なテレメトリーデータを収集・処理するための基盤APIです。

---

# Cloud SQL for PostgreSQL
## Breaking
原文: Vector assist (Preview) is temporarily disabled for all Cloud SQL for PostgreSQL instances.

説明：
Cloud SQL for PostgreSQLインスタンスで提供されていた「Vector assist（プレビュー版）」機能が、一時的に無効化されました。

影響有無：
**利用している場合は影響あり、利用していない場合は影響無し**。
この変更は、Cloud SQL for PostgreSQLの「Vector assist (Preview)」機能を明示的に利用していたお客様のインスタンスに直接的な影響があります。この機能に依存するアプリケーションやワークロードは、機能が利用できなくなるため影響を受けます。
お客様がご利用中のCloud Composer2は内部データベースとしてCloud SQLを使用していますが、通常この「Vector assist (Preview)」機能は明示的に有効にしない限り利用されないため、Cloud Composer2の運用自体には直接的な影響はないと判断できます。

対処方法：
**Vector assist (Preview) 機能を利用している場合のみ対応が必要**。
*   この機能に依存しているワークロードがある場合は、機能の再開を待つか、代替のベクトル検索ソリューションへの移行を検討してください。
*   プレビュー機能であるため、本番環境での利用は推奨されていません。
*   この機能を利用していない場合は、特段の対処は必要ありません。

用語説明：
*   **Vector assist**: Cloud SQL for PostgreSQLにおいて、ベクトルデータ（AI/MLアプリケーションで生成される埋め込みデータなど）の効率的な検索を支援する、ベクトル検索関連の機能（プレビュー版）です。
*   **Preview (プレビュー)**: Google Cloudの製品や機能のリリース段階の一つです。一般公開（GA: General Availability）前の段階であり、機能が変更される可能性や、SLA（Service Level Agreement）が提供されないことがあります。本番環境での使用は推奨されません。