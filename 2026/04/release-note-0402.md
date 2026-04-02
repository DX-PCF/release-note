
# Title: March 31, 2026 
Link: https://docs.cloud.google.com/release-notes#March_31_2026<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、構築済みのサービスへの影響調査を以下の通り実施し、専門的な言葉遣いと書式でご報告いたします。

---

# Apigee X

## Change
原文: **Updated MCP server target endpoint for MCP Discovery Proxies**
 With the GA launch of Model Context Protocol (MCP) in Apigee, the structure of the MCP server target endpoint for MCP Discover Proxies has changed to `ORG_NAME.mcp.apigee.internal`.

 Private preview customers using the previous format (`mcp.apigee.internal`) are encouraged to update their proxies to reflect the new structure. Existing endpoints using the old format will continue to work, but new endpoints will use the new structure.

説明：
ApigeeのModel Context Protocol (MCP) が一般提供（GA）されたことに伴い、MCP Discovery Proxiesのターゲットエンドポイントの形式が変更されました。新しい形式は `ORG_NAME.mcp.apigee.internal` となります。
以前のプライベートプレビュー版で旧形式 (`mcp.apigee.internal`) を使用していたユーザーは、新しい構造に更新することが推奨されています。ただし、既存の旧形式のエンドポイントは引き続き動作し、非互換性のある変更ではありません。今後新規作成されるエンドポイントは新しい構造が適用されます。

影響有無：
**影響軽微**。
既存のApigee X環境でMCP Discovery Proxiesを運用している場合、既存のエンドポイントは変更なく動作を継続するため、即座の業務影響はありません。新規でMCP Discovery Proxiesを作成する場合、または既存のプロキシを再構成する場合は、新しいエンドポイント形式が適用されます。

対処方法：
*   現在Apigee Xのプライベートプレビュー版でMCP Discovery Proxiesを利用しており、旧形式のエンドポイントを使用している場合は、将来的なベストプラクティスに沿うため、新しい `ORG_NAME.mcp.apigee.internal` 形式への更新を検討してください。
*   今後、MCP Discovery Proxiesを新規に作成する際は、新しいエンドポイント形式である `ORG_NAME.mcp.apigee.internal` を使用して設定してください。

用語説明：
*   **Model Context Protocol (MCP)**: Apigeeが内部的に使用するプロトコルの一つで、サービスのコンテキスト情報などを連携するために用いられます。
*   **MCP Discovery Proxies**: MCPプロトコルを利用して、サービスやAPIの情報を検出・連携する役割を持つApigeeプロキシを指します。
*   **GA (General Availability)**: プロダクトや機能が一般向けに広く提供され、本番環境での利用が推奨される状態を指します。

## Announcement
原文: On March 31st, 2026, we released an updated version of Apigee.

 > **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明：
Apigeeの新しいバージョンがリリースされました（リリースノートの記載は2026年3月31日となっていますが、通常はリリースノート発行時点の「本日」を指します）。このリリースは、すべてのGoogle Cloudゾーンへの展開（ロールアウト）に4営業日以上かかる場合があります。そのため、お客様のApigeeインスタンスに新しい機能や修正が適用されるまでには、時間差が生じる可能性があります。

影響有無：
**影響なし**。
これは一般的なリリースアナウンスであり、特定の機能変更や非互換性に関する情報ではありません。新しい機能やバグ修正が順次適用されるプロセスに関する通知です。既存のワークロードに直接的な影響を及ぼすものではありませんが、新しい機能の利用や特定の修正の適用を期待する場合は、ロールアウトが完了するまで待つ必要があります。

対処方法：
特に必要な対処はありません。新しい機能や修正が利用可能になるまで待機してください。

用語説明：
*   **ロールアウト (Rollout)**: ソフトウェアの更新や新機能を段階的に、あるいは一斉に本番環境に展開するプロセスを指します。Google Cloudでは通常、リージョンやゾーンごとに順次適用されます。

## Issue
原文: **Known Issue 496552286: Deployment fails for MCP Discovery Proxies in regions with capacity limitations.**

 For more information, see Apigee known issues.

 [Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)

説明：
既知の問題として、一部のキャパシティ制限のあるリージョンにおいて、MCP Discovery Proxiesのデプロイが失敗するケースがあることが報告されています。詳細については、Apigeeの既知の問題に関する公式ドキュメントを参照してください。

影響有無：
**影響あり（条件付き）**。
構築済みのApigee X環境でMCP Discovery Proxiesをデプロイしている、または今後デプロイを予定している場合、特にキャパシティ制限のあるリージョンで作業を行う際に、デプロイが失敗する可能性があります。現在、MCP Discovery Proxiesを使用していない場合は影響ありません。

対処方法：
*   MCP Discovery Proxiesを利用している、または利用を計画している場合は、Apigeeの[既知の問題](https://docs.cloud.google.com/apigee/docs/release/known-issues)ドキュメントを定期的に確認し、この問題の最新状況、影響を受ける可能性のあるリージョン、および利用可能な回避策や解決策がないか確認してください。
*   もしデプロイに失敗した場合は、エラーメッセージを確認し、既知の問題に該当するかどうかを判断してください。必要に応じて、Google Cloudサポートに問い合わせてください。

用語説明：
*   **既知の問題 (Known Issue)**: ソフトウェア開発元が認識しており、対応中または回避策が提示されている未解決の不具合を指します。
*   **キャパシティ制限 (Capacity Limitations)**: 特定のクラウドリージョンやゾーンにおいて、リソース（CPU、メモリ、ネットワーク帯域、IPアドレスなど）の利用可能な上限がある状態を指します。需要が供給を上回る場合に発生することがあります。

---

# Cloud NAT

## Announcement
原文: The default TCP `TIME_WAIT`
timeout for Cloud NAT is scheduled to decrease from 120 seconds to 30 seconds,
across all regions, as follows:

 [`TIME_WAIT`](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts)
 - **From June 30 to September 29, 2026**: new Cloud NAT gateways will use either
 the 120-second or 30-second default, depending on when the update is
 deployed in a specific region.
 - **On or after September 30, 2026**: all new Cloud NAT gateways in all regions
 will use the 30-second default.

 **Impact on gateways**

 - **New gateways**: after the update is deployed in a region, all new Cloud NAT
 gateways created in that region will use the 30-second default.
 This change also applies if a pre-update gateway is deleted and then recreated.
 - **Existing gateways**: Cloud NAT gateways created before the regional update
 will retain the 120-second default. You can adjust this value by using the
 `--tcp-time-wait-timeout`
 flag at any time.
 Cloud NAT gateways configured with a custom `TIME_WAIT` value
 aren't affected and will continue to use your configured custom value.

 The following table outlines the applicable default timeout for new gateways throughout the deployment timeline.

| Gateway type | Default timeout(before June 30) | Default timeout(June 30—September 29) | Default timeout(on or after September 30) |
| --- | --- | --- | --- |
| New | 120 seconds | 30 or 120 seconds | 30 seconds |

説明：
Cloud NATのデフォルトのTCP `TIME_WAIT` タイムアウト値が、現在の120秒から30秒に短縮される予定です。この変更は、2026年6月30日から9月29日にかけて段階的に各リージョンに展開され、2026年9月30日以降は、すべての新規Cloud NATゲートウェイで30秒がデフォルト値として適用されます。

**ゲートウェイへの影響:**
*   **既存のCloud NATゲートウェイ**: この変更による影響は受けません。引き続きデフォルト値は120秒が維持されます。ユーザーが `--tcp-time-wait-timeout` フラグでカスタム値を設定している場合は、そのカスタム値が適用され続けます。
*   **新規Cloud NATゲートウェイ**: 各リージョンでアップデートが展開された後、新しく作成されるCloud NATゲートウェイは30秒のデフォルト値を使用します。既存のゲートウェイを削除して再作成した場合も、新規ゲートウェイと見なされ、新しいデフォルト値が適用されます。

影響有無：
**影響軽微（将来的な新規作成時に考慮が必要）**。
現在稼働しているCloud NATゲートウェイでデフォルト値（120秒）を使用している場合でも、この変更による影響は受けません。カスタム値を設定している場合も影響ありません。
将来的にCloud NATゲートウェイを新規作成する際、または既存のゲートウェイを削除して再作成する際には、デフォルトの`TIME_WAIT`タイムアウトが30秒になることを考慮する必要があります。これはTCPポートの枯渇リスクを低減する効果がある一方で、特定のネットワーク条件下では稀に接続再利用の振る舞いに影響を与える可能性がありますが、多くの一般的なワークロードではパフォーマンス上の問題は発生しないと予想されます。

対処方法：
*   現在利用しているCloud NATゲートウェイでデフォルトのTCP `TIME_WAIT` タイムアウト値が120秒であることが必須である、または30秒への短縮がワークロードに悪影響を及ぼす可能性があると判断される場合は、ゲートウェイ作成時または更新時に `--tcp-time-wait-timeout` フラグを使用して明示的に120秒以上の値を設定することを検討してください。これにより、将来のデフォルト値の変更の影響を受けなくなります。
*   今後のCloud NATゲートウェイの新規デプロイメント計画においては、デフォルトの`TIME_WAIT`タイムアウト値が30秒になることを認識し、必要に応じて設定を調整する計画に含めてください。

用語説明：
*   **TCP `TIME_WAIT`**: TCP接続が正常に終了した後、その接続に関連するポートとソケット情報が、一定期間システム内で保持される状態を指します。この期間は、ネットワーク上の遅延パケットが原因で新しい接続が誤って確立されることを防ぐために設けられています。`TIME_WAIT`タイムアウトが短いほど、ポートの再利用が早くなり、ポート枯渇のリスクが減少しますが、まれに遅延パケットによる問題のリスクがわずかに増加する可能性があります。
*   **Cloud NAT (Network Address Translation)**: Google Cloud VPCネットワーク内のプライベートIPアドレスを持つ仮想マシンインスタンスが、外部ネットワーク（インターネットなど）にアウトバウンド接続を行うためのマネージドサービスです。これにより、インスタンスに外部IPアドレスを付与することなく、インターネットアクセスを可能にします。
# Title: March 30, 2026 
Link: https://docs.cloud.google.com/release-notes#March_30_2026<br>
Google Cloud のリリースノートに基づく、構築済みサービスへの影響調査結果を報告します。

---

# Cloud Logging
## Change
原文: For any new project that is created on or after March 30, 2026, if the project enables the Cloud Logging API, then Google Cloud Observability also enables the Telemetry API.
説明：2026年3月30日以降に新規作成されるプロジェクトにおいて、Cloud Logging APIが有効化されると、同時にGoogle Cloud Observabilityの一部であるTelemetry APIも自動的に有効化されるようになります。これは、モニタリングやロギングデータの収集をより包括的に行うための変更です。
影響有無：**影響なし**。
理由：この変更は、2026年3月30日以降に新規作成されるプロジェクトのみに適用されるため、既存のプロジェクトや構築済みのサービスには影響を与えません。
対処方法：特段の対処は不要です。将来的に新規プロジェクトを立ち上げる際に、このデフォルト設定を認識しておいてください。

### 用語説明
*   **Cloud Logging API**: Google Cloud のログ管理サービスであるCloud Loggingの機能にプログラムからアクセスするためのAPIです。ログのエクスポート、フィルタリング、表示などが可能です。
*   **Google Cloud Observability**: Google Cloud のモニタリング、ロギング、トレース機能（旧称 Stackdriver）を統合したプラットフォームです。システムの健全性、パフォーマンス、可用性を可視化し、トラブルシューティングを支援します。
*   **Telemetry API**: Google Cloud Observabilityの一環として、各種テレメトリデータ（指標、ログ、トレースなど）を収集し、処理するための基盤を提供するAPIです。これにより、リソースの使用状況やアプリケーションのパフォーマンスに関する詳細な洞察を得ることができます。

---

# Cloud Monitoring
## Change
原文: For any new project that is created on or after March 30, 2026, if the project enables the Cloud Monitoring API, Telemetry API.
説明：2026年3月30日以降に新規作成されるプロジェクトにおいて、Cloud Monitoring APIが有効化されると、同時にTelemetry APIも自動的に有効化されるようになります。これはCloud Loggingの変更と同様に、Google Cloud Observabilityにおけるモニタリングデータ収集の統合を目的としています。
影響有無：**影響なし**。
理由：この変更は、2026年3月30日以降に新規作成されるプロジェクトのみに適用されるため、既存のプロジェクトや構築済みのサービスには影響を与えません。
対処方法：特段の対処は不要です。将来的に新規プロジェクトを立ち上げる際に、このデフォルト設定を認識しておいてください。

### 用語説明
*   **Cloud Monitoring API**: Google Cloud のモニタリングサービスであるCloud Monitoringの機能にプログラムからアクセスするためのAPIです。カスタム指標の作成、アラートポリシーの設定、ダッシュボードの構築などが可能です。
*   **Telemetry API**: (上記Cloud Loggingのセクションを参照)

---

# Cloud SQL for PostgreSQL
## Breaking
原文: Vector assist (Preview) is temporarily disabled for all Cloud SQL for PostgreSQL instances.
説明：Cloud SQL for PostgreSQLのプレビュー機能である「Vector assist」が、全てのアクティブなインスタンスにおいて一時的に無効化されました。これは、非互換性のある変更（Breaking Change）としてアナウンスされています。
影響有無：**影響あり**。
理由：現在、当社のCloud SQL for PostgreSQLインスタンスで「Vector assist」機能を**利用している場合**、その機能が一時的に使用できなくなります。これにより、当該機能に依存するアプリケーションやワークロードがある場合、機能停止やエラーが発生する可能性があります。ただし、「Preview」段階の機能であるため、本番環境での利用は限定的であると想定されます。
対処方法：
1.  **利用状況の確認**: 当社のCloud SQL for PostgreSQLインスタンスで「Vector assist」機能を利用しているか、または過去に有効化したことがあるかを確認してください。
2.  **依存関係の評価**: もし利用している場合、その機能がどのようなワークロードやアプリケーションに依存しているかを評価してください。
3.  **代替策の検討**: Vector assistに依存する処理がある場合、代替手段の検討（例: 他のベクトルデータベースソリューションの利用、Vector assistなしでのアプリケーションの動作検証）または、その機能が一時的に利用できないことによる影響を許容してください。
4.  **再開アナウンスの監視**: Google CloudからのVector assistの再開、または今後の提供に関するアナウンスを継続的に監視してください。

### 用語説明
*   **Vector assist**: Cloud SQL for PostgreSQLにおいて、ベクトル埋め込み（Vector Embeddings）の効率的な管理と検索をサポートするためのプレビュー機能です。機械学習モデルからの出力など、高次元ベクトルデータをデータベース内で扱う用途を想定しています。
*   **Preview (プレビュー)**: Google Cloudのプロダクトのリリース段階の一つです。プレビュー段階の機能は、一般提供（GA: General Availability）前の試験的な提供であり、機能が変更される可能性や、互換性のない変更、サービスの停止などが予告なく行われる場合があります。本番環境での利用は推奨されません。