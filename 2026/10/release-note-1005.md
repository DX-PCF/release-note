
# Title: October 02, 2026 
Link: https://docs.cloud.google.com/release-notes#October_02_2026<br>
Google Cloud インフラエンジニアとして、リリースノートに基づく影響調査の結果を以下にご報告いたします。

---

# Apigee X

## Announcement

原文: On October 2, 2026, we released an updated version of Apigee (1-18-0-apigee-6).
> **Note:** Rollouts of this release began today and can take four or more business days to complete across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.

説明: Apigeeの更新バージョン(1-18-0-apigee-6)がリリースされました。このバージョンは2026年10月2日に公開され、リリースノート発行時点からGoogle Cloudの全ゾーンへの展開には4営業日以上かかる可能性があります。展開が完了するまでは、新しい機能や修正がお客様のインスタンスで利用できない場合があります。

影響有無:
Apigee XはGoogleが管理するフルマネージドサービスであるため、この更新はGoogleによって自動的に適用されます。お客様側での手動によるバージョンアップ作業は不要です。展開期間中は、一部のインスタンスで新機能や修正が一時的に利用できない可能性がありますが、サービスの連続性には影響しない見込みです。

対処方法:
特段の対処は不要です。リリースがロールアウトされる期間中は、お客様の環境に適用されるまでに時間差があることをご理解ください。

用語説明:
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームのSaaS（Software as a Service）版です。APIの設計、公開、セキュリティ、監視、分析などをフルマネージドで提供します。

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **564386425** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway (ASM) to patch security vulnerabilities. |
| **561666530** | **Security fix for Apigee.** Upgraded the Prometheus library to patch the following vulnerabilities: - CVE-2026-42151- CVE-2026-42154- CVE-2026-44903- CVE-2026-40179 |
| **N/A** | **Security fix for Apigee infrastructure.** |
 - CVE-2026-42151- CVE-2026-42154- CVE-2026-44903- CVE-2026-40179
- CVE-2026-42151- CVE-2026-42154- CVE-2026-44903- CVE-2026-40179
[CVE-2026-42151](https://nvd.nist.gov/vuln/detail/CVE-2026-42151)
[CVE-2026-42154](https://nvd.nist.gov/vuln/detail/CVE-2026-42154)
[CVE-2026-44903](https://nvd.nist.gov/vuln/detail/CVE-2026-44903)
[CVE-2026-40179](https://nvd.nist.gov/vuln/detail/CVE-2026-40179)

説明:
Apigeeのセキュリティに関する複数の修正が実施されました。
*   Apigeeのイングレスゲートウェイ (ASM) がアップグレードされ、セキュリティ脆弱性に対するパッチが適用されました。
*   Prometheusライブラリがアップグレードされ、複数のCVE（CVE-2026-42151, CVE-2026-42154, CVE-2026-44903, CVE-2026-40179）に対する脆弱性が修正されました。
*   Apigeeインフラストラクチャ全般のセキュリティ修正も含まれています。

影響有無:
Apigee XはGoogle Cloudが管理するサービスであるため、これらのセキュリティ修正は自動的に適用されます。お客様側でのセキュリティ対策の実施は不要であり、お客様のAPIプラットフォームのセキュリティ体制が強化されます。サービスへの直接的な影響（ダウンタイムなど）は想定されません。

対処方法:
特段の対処は不要です。これらの修正により、お客様の環境がよりセキュアになります。

用語説明:
*   **Ingress Gateway (ASM)**: Apigeeに送信されるAPIトラフィックを受け入れるためのエントリポイントとなるゲートウェイです。Anthos Service Mesh (ASM) を基盤としています。
*   **Prometheus library**: オープンソースの監視システムであるPrometheusで、メトリクス収集のために使用されるクライアントライブラリです。
*   **CVE (Common Vulnerabilities and Exposures)**: 一般に公開されている情報セキュリティ脆弱性と暴露のリストであり、特定の脆弱性に対して一意の識別子が割り当てられます。

## Fixed

原文:
| Bug ID | Description |
| --- | --- |
| **432315283** | Fixed a multi-certificate truststore so that its trust anchors take effect without a Message Processor restart when `features.truststore.multi_cert_bundle.enabled` is toggled at runtime; the outbound SSL context is now rebuilt automatically on any trust-anchor change. |
| **565072374** | VerifyJWT policies that use a JWKS `uriRef` no longer return `steps.jwt.NoMatchingPublicKey` on the first request after the JWKS cache TTL expires when the identity provider has rotated to a new key ID. The cache now re-fetches synchronously when its entry expires. |
| **535395491** | Extension Processor (ext_proc) denials now return the status and body that the policy or FaultRule produced, instead of always returning HTTP 500. |
| **558421499** | Apigee runtime runs on JRE 21. |
| **517953321** | The `lookupcache.<n>.isEncrypted` and `responsecache.<n>.isEncrypted` flow variables now report the per-entry on-disk encryption state of the L2 cache, rather than approximating whether the cache-encryption key is loaded. L1 cache hits report `false`. Review any policy conditions that rely on these flow variables. |
| **563557547** | Fixed EventFlow (Server-Sent Events) coalescing multiple events into a single policy invocation under burst load on the http-adaptor data path, which produced malformed SSE output to the client. |
| **562740573** | Apigee Analytics now populates the `processing_mode` dimension, distinguishing proxy traffic from extension-processor traffic. This dimension is not populated in billing-only analytics mode. |
| **357042873** | Stopped redirecting `apigee-cassandra-schema-readiness` init container logs to `/dev/null`, improving troubleshooting. Workloads undergo a rolling restart upon upgrade. |
| **N/A** | Updates to infrastructure and libraries. |

### Bug ID: 432315283
説明: `features.truststore.multi_cert_bundle.enabled` 設定がランタイムで変更された際、マルチ証明書トラストストアの信頼アンカーがMessage Processorの再起動なしで即座に有効になるようになりました。信頼アンカーが変更されると、アウトバウンドSSLコンテキストが自動的に再構築されます。
影響有無: トラストストアを使用してアウトバウンドSSL/TLS接続を確立している場合、設定変更が即時に反映されるようになるため、運用性が向上します。サービスのダウンタイムなしで証明書の更新が可能になります。
対処方法: 特段の対処は不要です。この改善により、関連する運用手順を見直すことが可能です。

用語説明:
*   **Multi-certificate truststore**: 複数の証明書（ルート証明書、中間証明書など）を格納し、外部システムとのSSL/TLS通信において信頼性を確立するために使用される証明書ストアです。
*   **Trust anchor**: 信頼の連鎖の起点となる、自己署名された信頼されたルート証明書を指します。
*   **Outbound SSL context**: Apigeeから外部のバックエンドサービスへのアウトバウンド（発信）SSL/TLS接続の設定やコンテキストのことです。

### Bug ID: 565072374
説明: JWKS `uriRef` を使用するVerifyJWTポリシーにおいて、IDプロバイダが新しい鍵IDにローテーションした後、JWKSキャッシュのTTL期限切れ後の初回リクエストで `steps.jwt.NoMatchingPublicKey` エラーが返される問題が修正されました。キャッシュは有効期限が切れると同期的に再フェッチされるようになりました。
影響有無: VerifyJWTポリシーを使用してJWTの検証を行っている場合、鍵のローテーション時における初回リクエストの失敗が解消され、APIの信頼性が向上します。特に、鍵の自動ローテーションを導入している環境にとっては重要な改善です。
対処方法: 特段の対処は不要です。この修正により、APIの安定性が向上したことを確認してください。

用語説明:
*   **VerifyJWT policy**: Apigeeのポリシーの一つで、JSON Web Token (JWT) の署名を検証し、トークンが有効であることを確認する機能を提供します。
*   **JWKS (JSON Web Key Set)**: JWTの署名検証に使用される公開鍵のセットをJSON形式で表現したものです。`uriRef` は、JWKSが配置されているURI（Uniform Resource Identifier）を参照します。
*   **TTL (Time To Live)**: キャッシュされたデータが有効である期間を示します。この期間が過ぎるとデータは無効となり、再取得が必要になります。

### Bug ID: 535395491
説明: Extension Processor (ext_proc) の拒否応答が、常にHTTP 500を返す代わりに、ポリシーまたはFaultRuleによって生成された正確なステータスコードとボディを返すように改善されました。
影響有無: Extension Processor (ext_proc) を利用している場合、エラー発生時のレスポンスがより具体的になり、デバッグやトラブルシューティングが容易になります。既存のクライアントアプリケーションがHTTP 500を前提にエラーハンドリングを行っている場合は、影響を考慮する必要がありますが、通常は改善として捉えられます。
対処方法: ext_procを利用している場合、エラーレスポンスの形式がより正確になったことを認識し、必要に応じてエラーハンドリングロジックの改善を検討してください。

用語説明:
*   **Extension Processor (ext_proc)**: ApigeeのAPIプロキシフロー内で、外部のカスタムロジックやサービス（例: Cloud Functions、Cloud Runなど）を呼び出すための機能です。

### Bug ID: 558421499
説明: ApigeeランタイムがJRE 21で動作するようになりました。
影響有無: 内部的なランタイム環境のアップグレードであり、Apigeeの機能や挙動に直接的な変更はありません。通常、パフォーマンスの向上やセキュリティの強化が期待されます。
対処方法: 特段の対処は不要です。

用語説明:
*   **JRE (Java Runtime Environment)**: Javaアプリケーションを実行するために必要なソフトウェア環境です。Java仮想マシン(JVM)
# Title: October 01, 2026 
Link: https://docs.cloud.google.com/release-notes#October_01_2026<br>
# BigQuery
## Change
原文: An updated version of the
Simba JDBC driver for BigQuery
is now available.

[Simba JDBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#current_jdbc_driver)

説明：
Google Cloud BigQuery に接続するための Simba JDBC ドライバーの最新バージョンがリリースされました。このアナウンスは、Simba Technologies が提供するBigQuery向けJDBCドライバーがアップデートされ、利用可能になったことを示しています。通常、ドライバーの更新には、バグ修正、パフォーマンス改善、新しいBigQuery機能への対応、またはセキュリティ強化が含まれます。

影響有無：
**影響なし（ただし、Simba JDBCドライバー利用組織は検討推奨）**

直接的な影響は現在ありません。既存のシステムが直ちに動作しなくなるわけではありません。
ただし、BigQueryへの接続にSimba JDBCドライバーを使用しているアプリケーションやBIツール（例: Tableau, Looker, DBeaverなど）がある場合、この新しいバージョンへのアップグレードを検討する価値があります。

理由としては以下の通りです。
*   このアナウンスは「新しいバージョンが利用可能になった」というものであり、既存のドライバーが即座に利用不可になることを意味するものではありません。
*   既存のGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)環境では、通常、BigQueryへの接続にはPythonクライアントライブラリやAirflowのBigQuery Hookが使用されるため、Simba JDBCドライバーを直接利用するケースは稀です。そのため、Composer環境への直接的な影響は考えられません。
*   もし何らかの理由で、Airflow環境内でJavaベースのカスタムアプリケーションがBigQueryにJDBC経由で接続している場合は、影響範囲となります。

対処方法：
1.  **利用状況の確認:** BigQueryへの接続にSimba JDBCドライバーを使用している社内システムやアプリケーション（BIツール、データ連携ツール、自社開発アプリケーションなど）があるかを確認してください。
2.  **アップグレードの検討:** もし使用している場合は、新しいドライバーのリリースノートや変更点を確認し、既存システムへの影響（互換性、新機能、バグ修正、セキュリティ改善など）を評価してください。
3.  **テスト環境での検証:** アップグレードを決定した場合は、本番環境に適用する前に、必ず開発/テスト環境で十分な動作確認（特に回帰テスト）を実施してください。

用語説明：
*   **Simba JDBC driver for BigQuery:** Simba Technologies社が開発・提供している、JavaアプリケーションからBigQueryに接続するためのJava Database Connectivity (JDBC) ドライバーです。BigQueryはリレーショナルデータベースではないため、このドライバーがBigQueryのREST APIとJDBCインターフェース間の変換を行い、標準的なSQLクエリをJavaアプリケーションから実行できるようにします。
*   **JDBC (Java Database Connectivity):** Javaアプリケーションから様々な種類のデータベース（リレーショナルデータベース、データウェアハウスなど）に接続するための標準的なAPI（Application Programming Interface）です。
*   **BigQuery:** Google Cloudが提供する、フルマネージドでスケーラブルなサーバーレスエンタープライズデータウェアハウスです。ペタバイト規模のデータをSQLで高速に分析できます。