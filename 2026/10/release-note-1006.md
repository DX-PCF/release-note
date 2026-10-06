
# Title: October 02, 2026 
Link: https://docs.cloud.google.com/release-notes#October_02_2026<br>
Google Cloud Composer 2 (Compoer version 2.7.1、Airflow version 2.7.3) をご利用とのこと、承知いたしました。Google Cloud Composer は内部で Google Kubernetes Engine (GKE) を利用しているため、GKE のリリースノートは Composer 環境の基盤に影響を与える可能性があります。

---

# Apigee X

## Announcement

原文: On October 2, 2026, we released an updated version of Apigee (1-18-0-apigee-6).
> **Note:** Rollouts of this release began today and can take four or more business
days to complete across all Google Cloud zones. Your instances might not have
the features and fixes available until the rollout is complete.

説明：Apigee の新しいバージョン `1-18-0-apigee-6` がリリースされました。この更新は段階的に適用され、すべての Google Cloud ゾーンで完了するまでに 4 営業日以上かかる場合があります。ロールアウトが完了するまで、新しい機能や修正が利用できない可能性があります。

影響有無：影響なし。これは Apigee プラットフォームのバージョンアップに関するアナウンスであり、既存の環境は Google Cloud によって自動的に更新が適用されます。ユーザー側での操作は不要です。

対処方法：なし。ロールアウトの完了を待機してください。

用語説明：
*   **Apigee X**: Google Cloud 上で API を管理、公開、保護するための API 管理プラットフォームです。
*   **ロールアウト (Rollout)**: 新しいバージョンや機能が、システム全体に段階的に展開されていくプロセスを指します。

## Security

原文:
| Bug ID | Description |
| --- | --- |
| **564386425** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway (ASM) to patch security vulnerabilities. |
| **561666530** | **Security fix for Apigee.** Upgraded the Prometheus library to patch the following vulnerabilities: - CVE-2026-42151- CVE-2026-42154- CVE-2026-44903- CVE-2026-40179 |
| **N/A** | **Security fix for Apigee infrastructure.** |
 - CVE-2026-42151- CVE-2026-42154- CVE-2026-44903- CVE-2026-40179

説明：
*   Apigee のインgress ゲートウェイ（ASM）がセキュリティ脆弱性に対応するためにアップグレードされました。
*   Prometheus ライブラリが、複数の既知の脆弱性（CVE-2026-42151、CVE-2026-42154、CVE-2026-44903、CVE-2026-40179）のパッチ適用のためアップグレードされました。
*   Apigee インフラストラクチャに対してセキュリティ修正が適用されました。これには上記の Prometheus 関連の CVE 修正も含まれます。

影響有無：影響なし（ポジティブ）。これらの変更はセキュリティ強化を目的としており、お客様の Apigee 環境の安全性が向上します。ユーザー側での特別な対応は必要ありません。

対処方法：なし。

用語説明：
*   **Ingress Gateway (ASM)**: API トラフィックの入り口となるゲートウェイで、通常は Anthos Service Mesh (ASM) の一部として機能し、サービスメッシュ内のトラフィックルーティングとポリシー適用を担います。
*   **Prometheus**: オープンソースのモニタリングおよびアラートツールキットで、時系列データの収集と分析に使用されます。
*   **CVE (Common Vulnerabilities and Exposures)**: 一般に知られているサイバーセキュリティの脆弱性や露出に対して与えられる識別子です。

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

説明：
*   **Bug ID 432315283**: マルチ証明書トラストストアの修正。`features.truststore.multi_cert_bundle.enabled` がランタイムで切り替えられた際に、Message Processor の再起動なしでトラストアンカーが即座に有効になるよう修正されました。アウトバウンド SSL コンテキストも、トラストアンカーの変更時に自動で再構築されます。
*   **Bug ID 565072374**: JWKS `uriRef` を使用する VerifyJWT ポリシーで、JWKS キャッシュの TTL 期限切れ後、ID プロバイダーが新しいキー ID にローテーションした場合に、初回リクエストで `steps.jwt.NoMatchingPublicKey` エラーが返されなくなりました。キャッシュエントリが期限切れになると、同期的に再取得されるようになります。
*   **Bug ID 535395491**: Extension Processor (`ext_proc`) による拒否が、常に HTTP 500 を返すのではなく、ポリシーまたは FaultRule で生成されたステータスとボディを返すようになりました。
*   **Bug ID 558421499**: Apigee ランタイムが JRE 21 で動作するようになりました。
*   **Bug ID 517953321**: `lookupcache.<n>.isEncrypted` および `responsecache.<n>.isEncrypted` のフロー変数が、L2 キャッシュのエントリごとのオンディスク暗号化状態を報告するようになりました。L1 キャッシュヒットは常に `false` を報告します。これらのフロー変数に依存するポリシー条件を見直すことが推奨されています。
*   **Bug ID 563557547**: EventFlow (Server-Sent Events) で、バーストロード時に複数のイベントが単一のポリシー呼び出しに結合され、クライアントに不正な SSE 出力が生成される問題が修正されました。
*   **Bug ID 562740573**: Apigee Analytics が `processing_mode` ディメンションを生成し、プロキシトラフィックとエクステンションプロセッサートラフィックを区別できるようになりました（課金専用アナリティクスモードでは利用不可）。
*   **Bug ID 357042873**: `apigee-cassandra-schema-readiness` init コンテナのログが `/dev/null` にリダイレクトされなくなり、トラブルシューティングが改善されました。アップグレード時にはワークロードのローリング再起動が発生します。
*   **N/A**: インフラストラクチャとライブラリの更新が行われました。

影響有無：
*   **ポジティブな影響**: ほとんどの修正は、Apigee の安定性、信頼性、セキュリティ、および監視機能の改善に繋がります。特に、トラストストアの即時反映、JWT 検証エラーの改善、より正確なエラーレスポンス、SSE の安定性向上などは、サービスの品質向上に寄与します。
*   **注意が必要な影響**:
    *   **Bug ID 517953321**: `lookupcache.<n>.isEncrypted` および `responsecache.<n>.isEncrypted` フロー変数の挙動が変更されたため、これらの変数をポリシー条件で利用している場合は、既存のポリシーロジックに意図しない影響がないか確認が必要です。特に L1 キャッシュヒットの場合に `false` を返すようになった点は考慮してください。
    *   **Bug ID 535395491**: Extension Processor からのエラーレスポンスが HTTP 500 固定からポリシー設定に基づくものに変更されたため、もしアプリケーション側で HTTP 500 を前提としたエラー処理を行っている場合は、影響がないか確認が必要です。ただし、これは通常、より正確なエラー処理を可能にする改善です。
*   **Composer への影響**: Apigee X は Composer と直接連携するサービスではありません。

対処方法：
*   **Bug ID 517953321**: `lookupcache.<n>.isEncrypted` または `responsecache.<n>.isEncrypted` を利用している Apigee ポリシーがないか確認し、必要に応じてポリシーロジックを調整してください。
*   その他はユーザー側での対処は不要です。

用語説明：
*   **Truststore**: SSL/TLS 通信において、信頼できる証明書（トラストアンカー）を格納するリポジトリです。
*   **Message Processor**: Apigee ランタイムの主要コンポーネントで、API プロキシへのリクエストを処理し、バックエンドサービスにルーティングします。
*   **JWKS (JSON Web Key Set)**: JWT (JSON Web Token) の検証に使用される公開鍵が格納されているエンドポイントです。
*   **TTL (Time To Live)**: キャッシュされたデータが有効である期間です。
*   **Extension Processor (ext_proc)**: Apigee の機能を拡張し、カスタムロジックや外部サービスとの連携を可能にするコンポーネントです。
*   **FaultRule**: Apigee ポリシー実行中に発生したエラーを処理するためのルールです。
*   **JRE (Java Runtime Environment)**: Java アプリケーション