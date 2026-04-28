
# Title: April 27, 2026 
Link: https://docs.cloud.google.com/release-notes#April_27_2026<br>
Google Cloud リリースノートに関する影響調査の結果を以下に報告します。

---

# API Gateway

## Change

**原文:**
> **New validations on paths in API configurations**
> API Gateway now enforces stricter syntax validations on templated paths when you create new API configurations and gateways.
> See path templating syntax rules and limits for more information.
> [path templating syntax rules](https://docs.cloud.google.com/api-gateway/docs/path-templating#syntax_rules)
> [limits](https://docs.cloud.google.com/api-gateway/docs/path-templating#limits)

**説明:**
API Gatewayにおいて、新しいAPI設定やゲートウェイを作成する際に、テンプレート化されたパス（例: `/users/{user_id}`）に対する構文検証がより厳格になりました。これにより、定義された構文ルールに準拠しないパスは拒否されるようになります。

**影響有無:**
**影響あり（潜在的）**

*   **既存のデプロイ済みAPI Gateway:** 直接的な影響はありません。既にデプロイされているAPI Gatewayの設定は変更されずに動作し続けます。
*   **新規デプロイまたは既存設定の更新時:** 影響があります。今後API Gatewayで新しいAPI設定をデプロイする場合や、既存のAPI設定を更新して再デプロイする場合に、この新しい厳格な検証ルールが適用されます。もし現在のOpenAPI SpecificationなどのAPI定義が、新しい検証ルールに合致しないパステンプレートを使用している場合、デプロイや更新時にエラーが発生する可能性があります。

**対処方法:**
*   新規のAPI Gatewayデプロイメントや、既存のAPI設定を更新する際には、API Gatewayが要求するパスのテンプレート構文ルールと制限事項を事前に確認してください。
*   特に、以下の公式ドキュメントを参照し、必要に応じてAPI定義（OpenAPI Specificationなど）内のパスを修正してください。
    *   [Path templating syntax rules](https://docs.cloud.google.com/api-gateway/docs/path-templating#syntax_rules)
    *   [Limits](https://docs.cloud.google.com/api-gateway/docs/path-templating#limits)
*   CI/CDパイプラインなどでAPI Gatewayのデプロイを自動化している場合は、テスト環境で影響がないか事前に確認することを推奨します。

**用語説明:**
*   **API Gateway:** Google Cloudが提供するフルマネージドのAPI管理サービスで、バックエンドサービス（Cloud Functions、Cloud Run、App Engine、Compute Engineなど）へのAPIアクセスをセキュアに公開し、管理します。
*   **テンプレート化されたパス (Templated paths):** APIのパスの一部を動的に変更可能にするために使用されるプレースホルダーを含むパス。例えば、`/products/{product_id}` における `{product_id}` のような形式です。
*   **構文検証 (Syntax validations):** データやコードが特定の定義されたルール（構文）に準拠しているかを確認するプロセスです。ここでは、APIのパス定義がAPI Gatewayの要求する形式に則っているかを確認します。

---

# Cloud Service Mesh

## Announcement

**原文:**
> **Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the regular channel now supports a limited implementation of the `EnvoyFilter` API.**
> To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see
> Data plane extensibility with `EnvoyFilter`.
> [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility)
> To troubleshoot any issue while configuring, see
> Resolving data plane extensibility issues.
> [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility)

**説明:**
マネージドCloud Service Meshの `TRAFFIC_DIRECTOR` 実装（レギュラーチャネル）において、`EnvoyFilter` APIの限定的な実装がサポートされるようになりました。これにより、Traffic Director を利用しているサービスメッシュのデータプレーン（Envoyプロキシ）に対して、より詳細なカスタマイズ（例: ローカルレートリミット）が可能になります。

**影響有無:**
**影響なし（機能追加のため）**

*   これは新機能の追加であり、既存のCloud Service Meshの構成や動作に破壊的な変更をもたらすものではありません。
*   現在 `EnvoyFilter` を利用していない環境では、直接的な影響はありません。
*   将来的にEnvoyプロキシの動作をより詳細にカスタマイズしたい場合に、この新機能を活用できるようになります。

**対処方法:**
*   現時点での対処は不要です。
*   もし、サービスメッシュ内で高度なEnvoyプロキシのカスタマイズ（例：きめ細やかなトラフィック制御、ポリシー適用、ローカルレートリミットなど）を検討している場合は、この新機能を活用できる可能性があります。
*   サポートされるフィールド、拡張、および使用方法の詳細については、以下の公式ドキュメントを参照してください。
    *   [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility)

**用語説明:**
*   **Cloud Service Mesh:** Google Cloudが提供するサービスメッシュソリューションの総称で、サービス間通信の管理、セキュリティ、可観測性を向上させます。通常、Anthos Service MeshとTraffic Directorの2つのデプロイオプションがあります。
*   **Traffic Director:** Google Cloudのフルマネージドなアプリケーションネットワーキングコントロールプレーンです。マイクロサービス向けのグローバルなトラフィック管理、サービスディスカバリ、ロードバランシング、ヘルスチェックなどの機能を提供します。Envoyプロキシと連携して動作します。
*   **EnvoyFilter API:** Istioのカスタムリソースであり、Envoyプロキシの構成を直接変更することで、Istioの標準機能では提供されない詳細なトラフィック制御やポリシー適用を実現するための高度な機能です。
*   **データプレーン (Data plane):** サービスメッシュにおいて、サービス間の通信を実際にインターセプトし、トラフィックルーティング、ポリシー適用、メトリクス収集などを実行する部分を指します。Cloud Service Meshでは主にEnvoyプロキシがこの役割を担います。
*   **ローカルレートリミット (Local Rate Limiting):** 各サービスインスタンス（Envoyプロキシ）が、中央のレートリミットサービスに依存せず、自身のトラフィックのレートを独立して制限する機能です。これにより、サービスが過負荷になるのを防ぎます。