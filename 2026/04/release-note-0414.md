
# Title: April 13, 2026 
Link: https://docs.cloud.google.com/release-notes#April_13_2026<br>
ご担当者様

Google Cloud のリリースノートに基づき、構築済みのサービスへの影響調査結果を以下にご報告いたします。

---

# Cloud Logging
## Libraries
原文: [v1.15.0](https://github.com/googleapis/google-cloud-go/compare/logging/v1.14.0...logging/v1.15.0)
説明：
Go言語向けCloud Loggingクライアントライブラリがバージョン `v1.15.0` にアップデートされました。このアップデートには、内部的な依存関係の更新や、`logging.BatchConfig` および `logging.Config` に新しいフィールドが追加されています。
影響有無：
*   **直接的なサービスへの影響**: なし。これはクライアントライブラリのアップデートであり、Google Cloudのバックエンドサービス自体に直接的な変更はありません。
*   **アプリケーションへの影響**:
    *   Go言語でCloud Loggingクライアントライブラリを使用しているアプリケーションがある場合、影響の可能性があります。
    *   今回の変更はマイナーバージョンアップであるため、通常、既存のAPI利用方法に対する後方非互換性のある変更は含まれていません。主に新機能の追加や内部改善が主眼です。
    *   アプリケーションがライブラリの特定の内部実装に依存している場合や、厳密な依存関係の固定を行っている場合は、影響の可能性があります。
対処方法：
*   Go言語でCloud Loggingクライアントライブラリを使用しているアプリケーションが存在する場合、テスト環境でライブラリのバージョンを `v1.15.0` にアップデートし、既存のログ出力処理および関連機能が期待通りに動作するか十分な回帰テストを実施することを推奨します。
*   新たに追加された機能（例: `logging.BatchConfig.WriteTimeout`, `logging.Config.EnableGRPC`, `logging.Config.GRPCWriteTimeout`）を利用する場合は、アプリケーションコードの修正が必要です。
用語説明：
*   **クライアントライブラリ**: プログラムから特定のサービス（この場合はCloud Logging）を利用するためのAPIを提供するソフトウェアライブラリ。
*   **マイナーバージョンアップ**: セマンティックバージョニング（`MAJOR.MINOR.PATCH`）における`MINOR`部分の変更。通常、後方互換性を保ちつつ、新機能の追加や機能改善が行われる。
*   **後方非互換性 (Breaking Change)**: 新しいバージョンにアップデートした際に、以前のバージョンで動作していたコードや設定が動作しなくなる変更。

---

# Cloud Service Mesh
## Announcement
原文: `1.28.5-asm.12 is now available for in-cluster Cloud Service Mesh. This patch release contains fixes for the following platform CVEs:` (CVEリスト)
説明：
自己管理型（in-cluster）のCloud Service Meshバージョン `1.28.5-asm.12` がリリースされました。このパッチリリースには、複数のプラットフォーム共通脆弱性識別子（CVEs）に対するセキュリティ修正が含まれています。特に、深刻度Critical（9.1）の `CVE-2026-33186` を含む重要な修正が含まれています。本バージョンはEnvoy `1.36.5-dev` を使用しています。
影響有無：
*   **セキュリティへの影響**: 深刻度の高い脆弱性を含む複数の脆弱性が修正されるため、本バージョンにアップグレードすることでセキュリティ体制が大幅に向上します。
*   **機能への影響**: パッチリリースであるため、機能変更や後方非互換性のある変更は通常含まれていません。既存のサービス機能への影響は限定的であると想定されます。
*   **パフォーマンスへの影響**: 脆弱性修正が直接パフォーマンスに大きな影響を与えることは稀ですが、アップグレード後の監視は推奨されます。
*   **利用中のサービスへの影響**: `in-cluster` Cloud Service Mesh を現在利用している場合、セキュリティ強化のため本バージョンへのアップグレードが強く推奨されます。
対処方法：
*   `in-cluster` Cloud Service Mesh を利用している場合、速やかに `1.28.5-asm.12` へのアップグレードを計画・実行してください。
*   アップグレード手順については、公式ドキュメント [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) を参照してください。
*   アップグレード前にテスト環境で十分な回帰テストを実施し、既存のワークロードに影響がないことを確認してください。
用語説明：
*   **in-cluster Cloud Service Mesh**: ユーザーのGKEクラスタ内にコントロールプレーンとデータプレーンがデプロイされる自己管理型のService Mesh。Anthos Service Meshの一部。
*   **CVE (Common Vulnerabilities and Exposures)**: 共通脆弱性識別子。公開されている情報セキュリティの脆弱性に関するデータベースのエントリー。
*   **Envoy**: Cloud Service Meshのデータプレーンとして使用される高性能なオープンソースのプロキシ。

## Announcement
原文: `1.27.8-asm.9 is now available for in-cluster Cloud Service Mesh. This patch release contains fixes for the following platform CVEs:` (CVEリスト)
説明：
自己管理型（in-cluster）のCloud Service Meshバージョン `1.27.8-asm.9` がリリースされました。このパッチリリースには、バージョン `1.28.5-asm.12` と同様に複数のプラットフォームCVEsに対するセキュリティ修正が含まれており、Critical（9.1）の `CVE-2026-33186` を含む重要な修正が含まれています。本バージョンはEnvoy `1.35.10-dev` を使用しています。
影響有無：
*   **セキュリティへの影響**: 深刻度の高い脆弱性を含む複数の脆弱性が修正されるため、本バージョンにアップグレードすることでセキュリティ体制が大幅に向上します。
*   **機能への影響**: パッチリリースであるため、機能変更や後方非互換性のある変更は通常含まれていません。既存のサービス機能への影響は限定的であると想定されます。
*   **利用中のサービスへの影響**: `in-cluster` Cloud Service Mesh の `1.27.x` 系バージョンを利用している場合、セキュリティ強化のため本バージョンへのアップグレードが強く推奨されます。
対処方法：
*   `in-cluster` Cloud Service Mesh の `1.27.x` 系バージョンを利用している場合、速やかに `1.27.8-asm.9` へのアップグレードを計画・実行してください。
*   アップグレード手順については、公式ドキュメント [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade) を参照してください。
*   アップグレード前にテスト環境で十分な回帰テストを実施し、既存のワークロードに影響がないことを確認してください。

## Announcement
原文: `The following images are now rolling out for managed Cloud Service Mesh:` (バージョンリストとCVEリスト)
説明：
マネージドCloud Service Mesh向けに以下の新しいイメージが各リリースチャネルでロールアウトされています。
*   `rapid` チャネル: `1.21.6-asm.19`
*   `regular` チャネル: `1.20.8-asm.73`
*   `stable` チャネル: `1.19.10-asm.66`
これらのパッチリリースには、複数のプラットフォームCVEsに対するセキュリティ修正が含まれており、特にCritical（9.1）の `CVE-2026-33186` を含む重要な修正が含まれています。
影響有無：
*   **セキュリティへの影響**: 深刻度の高い脆弱性を含む複数の脆弱性が修正されるため、自動的にセキュリティ体制が向上します。
*   **機能への影響**: マネージドサービスであるため、Googleが互換性を考慮してアップデートを適用します。通常、ユーザー側で機能変更や後方非互換性による直接的な影響は発生しません。
*   **運用への影響**: マネージドサービスのため、ユーザー側で手動によるアップグレード作業は不要です。Googleによって段階的にロールアウトが適用されます。
対処方法：
*   マネージドCloud Service Meshを利用している場合、ユーザー側で直接的なアクションは不要です。
*   ただし、ロールアウト後にアプリケーションの動作に異常がないか、定期的にシステムを監視することを推奨します。

## Announcement
原文: `1.26.8-asm.5 is now available for in-cluster Cloud Service Mesh. This patch release contains fixes for the following platform CVEs:` (CVEリスト)
説明：
自己管理型（in-cluster）のCloud Service Meshバージョン `1.26.8-asm.5` がリリースされました。このパッチリリースには、他のバージョンと同様に複数のプラットフォームCVEsに対するセキュリティ修正が含まれており、Critical（9.1）の `CVE-2026-33186` を含む重要な修正が含まれています。本バージョンはEnvoy `1.34.14-dev` を使用しています。
影響有無：
*   **セキュリティへの影響**: 深刻度の高い脆弱性を含む複数の脆弱性が修正されるため、本バージョンにアップグレードすることでセキュリティ体制が大幅に向上します。
*   **機能への影響**: パッチリリースであるため、機能変更や後方非互換性のある変更は通常含まれていません。既存のサービス機能への影響は限定的であると想定されます。
*   **利用中のサービスへの影響**: `in-cluster` Cloud Service Mesh の `1.26.x` 系バージョンを利用している場合、セキュリティ強化のため本バージョンへのアップグレードが強く推奨されます。
対処方法：
*   `in-cluster` Cloud Service Mesh の `1.26.x` 系バージョンを利用している場合、速やかに `1.26.8-asm.5` へのアップグレードを計画・実行してください。
*   アップグレード手順については、公式ドキュメント [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade) を参照してください。
*   アップグレード前にテスト環境で十分な回帰テストを実施し、既存のワークロードに影響がないことを確認してください。

---

# Google Kubernetes Engine
## Change
原文: `The validation of the HealthCheckPolicy custom resource from the GKE Gateway API is more rigorous in GKE version 1.34 and later. Existing HealthCheckPolicy resources that already contain mismatched type fields in the config are exempted and continue to function. However, updates to any existing policy must not introduce a mismatched type field in the config or change currently mismatched fields to new invalid values. When the HealthCheckPolicy custom resource is validated, the type field is now verified against the specified health check. For example, if type: TCP is specified but httpHealthCheck is configured, then the fields are mismatched and kubectl rejects the policy. However, for this same example, if type: TCP is specified and tcpHealthCheck is configured, then the fields are valid. Earlier versions of GKE accept custom resources that don't have matching fields. If you use an earlier version, the type field is used and the configuration in the health check field is ignored. For more details, see Configure health checks.`
説明：
GKE Gateway APIの `HealthCheckPolicy` カスタムリソースのバリデーションが、GKEバージョン `1.34` 以降でより厳格になります。具体的には、`type` フィールド（例: `TCP`, `HTTP`）と実際のヘルスチェック設定（例: `tcpHealthCheck`, `httpHealthCheck`）が一致しているか厳密に検証されるようになります。
既存のデプロイ済み `HealthCheckPolicy` リソースで `type` と設定が不一致であっても、引き続き動作しますが、そのポリシーを更新する際に、不一致を導入したり、既存の不一致なフィールドを無効な値に変更したりすることはできなくなります。不一致がある場合、`kubectl` によるポリシーの適用が拒否されます。
以前のGKEバージョンでは、不一致な設定も受け入れられ、その場合 `type` フィールドが優先され、不一致なヘルスチェック設定は無視されていました。
影響有無：
*   **機能への影響**:
    *   GKE `1.34` 以降のバージョンを利用している、またはアップグレードを予定している場合、`GKE Gateway API` を利用しているサービスに影響があります。
    *   現在 `HealthCheckPolicy` で `type` フィールドとヘルスチェック設定（例: `httpHealthCheck`）が一致しない定義を使用している場合：
        *   **既存のデプロイ済みリソース**: そのままでは動作し続けます。ただし、設定の不一致は是正されるべき状態です。
        *   **既存のデプロイ済みリソースの更新**: 不一致なフィールドを修正しない限り、`kubectl apply` などによる更新が拒否されます。
        *   **新規リソースの作成**: 不一致なフィールドがあると、`kubectl apply` などによる作成が拒否されます。
    *   これにより、意図しないヘルスチェック設定がデプロイされることを防ぎ、設定の信頼性が向上します。
*   **運用への影響**: `HealthCheckPolicy` を更新または新規作成する際に、厳格なバリデーションによってエラーが発生し、CI/CDパイプラインなどに影響を及ぼす可能性があります。
対処方法：
*   GKE `1.34` 以降のバージョンを利用している、またはアップグレードを計画している場合、`GKE Gateway API` を使用するすべての `HealthCheckPolicy` リソース定義をレビューし、`type` フィールドと実際のヘルスチェック設定が一致していることを確認してください。
*   不一致がある場合は、ポリシーの定義を修正してください。例えば、`type: TCP` が設定されているにもかかわらず `httpHealthCheck` が定義されている場合は、`type` を `HTTP` に変更するか、`tcpHealthCheck` に変更する必要があります。
*   特に、以前のGKEバージョンでデプロイされた不一致な設定が、意図せず動作していたケースでは、今回の修正により実際のヘルスチェックの動作が変わる可能性があります。更新前にテスト環境で入念な検証を実施し、サービスへの影響がないことを確認してください。
*   詳細については、公式ドキュメント [Configure health checks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_health_check) を参照してください。
用語説明：
*   **GKE Gateway API**: KubernetesのGateway API仕様に基づき、GKEクラスタにおけるロードバランシングとトラフィック管理を統一的に行うためのAPI。
*   **HealthCheckPolicy**: Gateway APIでバックエンドサービスに対するヘルスチェックの振る舞いを定義するためのカスタムリソース（Custom Resource）。
*   **バリデーション**: 入力されたデータや設定が、定義されたルールやスキーマに準拠しているかを確認するプロセス。

---
ご不明な点がございましたら、お気軽にお問い合わせください。