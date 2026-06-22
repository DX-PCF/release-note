
# Title: June 18, 2026 
Link: https://docs.cloud.google.com/release-notes#June_18_2026<br>
Google Cloudのリリースノートに基づき、各製品の変更点、影響、および対処方法について以下の通り回答します。

---

# API Gateway
## Change
原文: Update to the API Gateway runtime architecture
The API Gateway runtime architecture is being updated to improve its integration with Google Cloud Platform and its services.
This update does not affect existing API Gateway features.
However, be aware of the following differences:
- Status code changes for **gRPC** API Gateways
    - Error: `Quota exceeded`, New status code: `ResourceExhausted`, Previous status code: `Unavailable`
    - Error: `Invalid API key`, New status code: `InvalidArgument`, Previous status code: `InternalError`
- For 4xx client-side quota failures, API Gateway will now reject requests (fail closed). This applies to both **gRPC** and **OpenAPI** API Gateways.
If you experience any other differences in behavior due to this update, contact Google Cloud Customer Care.
Note: Rollouts of this release to production instances might take up to 4 weeks to complete across all Google Cloud zones. Your instances might not be updated until the rollout is complete.

説明：
API GatewayのランタイムアーキテクチャがGoogle Cloud Platformおよびそのサービスとの統合を改善するために更新されます。この更新は既存のAPI Gatewayの機能には影響を与えませんが、以下の2点に変更があります。

1.  **gRPC API Gatewayのステータスコード変更**:
    *   クォータ超過 (`Quota exceeded`) 時のエラーステータスコードが `Unavailable` から `ResourceExhausted` に変更されます。
    *   無効なAPIキー (`Invalid API key`) 時のエラーステータスコードが `InternalError` から `InvalidArgument` に変更されます。
2.  **4xxクライアント側クォータ失敗時の挙動変更**:
    *   4xx系（クライアントエラー）のクォータ超過が発生した場合、API Gatewayはリクエストを拒否するようになります（Fail Closed）。これはgRPCとOpenAPIの両方のAPI Gatewayに適用されます。

この変更のロールアウトは、全てのGoogle Cloudゾーンで完了するまでに最大4週間かかる可能性があります。

影響有無：
**影響あり**。
特にgRPC API Gatewayを使用している場合、クライアント側のエラーハンドリングロジックやモニタリングシステムに影響を及ぼす可能性があります。既存のシステムが古いステータスコードを前提に動作している場合、これらを検出できなくなったり、予期せぬ動作を引き起こす可能性があります。また、4xx系クォータ失敗時の `fail closed` 挙動は、これまで処理されていたリクエストが明示的に拒否されるようになるため、アプリケーションの動作に影響がないか確認が必要です。

対処方法：
1.  **gRPC API Gatewayのエラーハンドリング見直し**: gRPC API Gatewayを使用している場合、クライアント側のコードで `Quota exceeded` や `Invalid API key` に対応するエラーハンドリングロジックを確認し、新しいステータスコード (`ResourceExhausted`, `InvalidArgument`) に対応するよう修正してください。
2.  **モニタリングおよびアラート設定の更新**: これらのステータスコードを監視しているログ収集システムやアラート設定があれば、新しいステータスコードを対象に含めるよう更新してください。
3.  **4xxクォータ失敗時の挙動確認**: アプリケーションがAPI Gateway経由でクォータ制限に達した場合の挙動について、`fail closed` が既存のワークフローに影響を与えないか確認し、必要であればテスト環境でシミュレーションを行ってください。
4.  **ロールアウトの監視**: 最大4週間のロールアウト期間中に、API Gatewayの挙動に予期せぬ変化がないか継続的に監視してください。
5.  **Google Cloud Customer Careへの連絡**: この更新によって上記以外の予期せぬ挙動が発生した場合は、速やかに[Google Cloud Customer Care](https://cloud.google.com/support-hub)に連絡してください。

用語説明：
*   **gRPC**: Googleが開発したオープンソースの高性能RPC (Remote Procedure Call) フレームワーク。HTTP/2をベースとし、Protocol Buffersを使用してデータ交換を行います。
*   **OpenAPI**: RESTful APIを記述するための標準的な言語に依存しないインターフェース定義形式（旧称Swagger Specification）。
*   **ステータスコード (Status Code)**: APIからのレスポンスにおいて、処理の結果を示す数値コード。HTTPステータスコードと同様に、成功、クライアントエラー、サーバーエラーなどを区別するために使われます。
*   **ResourceExhausted**: gRPCのステータスコードの一つで、システムリソース（クォータ、CPU、メモリなど）が枯渇したことを示します。
*   **Unavailable**: gRPCのステータスコードの一つで、サービスが一時的に利用できないことを示します（例：サーバーが過負荷、メンテナンス中など）。
*   **InvalidArgument**: gRPCのステータスコードの一つで、クライアントから渡された引数（リクエストパラメータなど）が無効であることを示します。
*   **InternalError**: gRPCのステータスコードの一つで、サーバー内部で予期せぬエラーが発生したことを示します。
*   **Fail Closed**: セキュリティポリシーにおいて、不測の事態や認証・認可の失敗時に、システムがアクセスを完全に拒否する（サービスを停止する）挙動のこと。安全を優先する考え方。対義語は「Fail Open」。

---

# Apigee X
## Announcement
原文: On June 18th, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-9**, your instance will be updated to **1-17-0-apigee-9** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.
Note: Instances that meet either of the following two criteria will not be updated:
- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.
For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.

説明：
2026年6月18日より、メンテナンスウィンドウが設定されているApigeeインスタンスのメンテナンスアップデートが開始されました。
もしお客様のApigeeインスタンスがメンテナンスウィンドウを設定しており、かつ現在のバージョンが **1-17-0-apigee-9** 未満の場合、今後7〜21日以内に自動的に **1-17-0-apigee-9** へとアップデートされます。アップデート予定日を含む通知が、今後2営業日以内に送信されます。
ただし、以下のいずれかの条件に該当するインスタンスは、このアップデートの対象外となります。

*   DNS設定に誤りがある場合（[Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues)参照）。
*   削除されたApigee Java Libraryを使用している場合（[Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)参照）。

影響有無：
**影響あり**。
Apigee Xを使用しており、かつメンテナンスウィンドウを設定している場合、インスタンスが自動的に指定バージョンにアップデートされます。メンテナンスウィンドウ内に実施されるため、サービスへの直接的な影響は最小限に抑えられるはずですが、バージョンアップに伴う動作変更や予期せぬ挙動が発生しないか確認が必要です。
また、アップデートされない条件に該当する場合、セキュリティアップデートや機能改善が適用されず、サービスが古い状態に留まるリスクがあります。

対処方法：
1.  **インスタンス情報の確認**: Apigee Xインスタンスのバージョンと、メンテナンスウィンドウの設定状況を確認してください。
2.  **通知の確認**: アップデート対象のインスタンスについては、今後2営業日以内に送られてくるアップグレード予定日の通知を確認し、社内関係者と共有してください。
3.  **アップデートバージョンの確認**: アップデートされるバージョン `1-17-0-apigee-9` のリリースノートを確認し、このバージョンに含まれる変更点や既知の問題がないか事前に把握してください。
4.  **アップデート対象外条件の確認と対応**:
    *   DNS設定ミスがないか確認し、もしあれば速やかに修正してください。
    *   削除されたApigee Java Libraryを使用していないか確認し、もし使用していれば代替手段への移行を検討してください。これらの問題を解決しない限り、インスタンスはアップデートされません。
5.  **事後確認**: アップデート後には、Apigee XインスタンスのAPIプロキシやアプリケーションの動作に問題がないか、念のためテスト環境や本番環境で動作確認を行うことを推奨します。

用語説明：
*   **Apigee X**: Google Cloudが提供するフルマネージドAPI管理プラットフォーム。APIの設計、セキュリティ、デプロイ、監視、分析などを一元的に行えます。
*   **メンテナンスウィンドウ (Maintenance Window)**: クラウドサービスなどのシステムにおいて、計画的なメンテナンス作業やアップデートが行われる、事前に定められた期間。通常、サービス停止やパフォーマンス低下のリスクを最小限に抑えるために、サービス利用が少ない時間帯に設定されます。
*   **DNS misconfiguration (DNS設定ミス)**: ドメインネームシステム (DNS) のレコード設定が正しくない状態。これにより、サービスへのアクセスや名前解決が正常に行えなくなる場合があります。

---

# Cloud Logging
## Change
原文: The Cloud Logging API adds support for the `ca` regional endpoint. For a complete list of regional endpoints, see the REST reference pages.

説明：
Cloud Logging APIが、カナダ（`ca`）リージョンのエンドポイント (`ca` regional endpoint) のサポートを追加しました。これにより、ログデータをカナダリージョン内で保持できるようになります。完全なリージョナルエンドポイントのリストは、[REST reference pages](https://docs.cloud.google.com/logging/docs/reference/v2/rest?rep_location=global)で確認できます。

影響有無：
**影響なし（機能追加のため）**。
この変更は、新しいリージョナルエンドポイントの追加であり、既存のCloud Loggingの機能や設定に直接的な影響はありません。現在利用中のCloud Loggingの挙動が変更されることはありません。
ただし、もしお客様がカナダリージョンにリソースを展開しており、かつログデータのデータ所在地（Data Residency）要件を満たす必要がある場合は、この新しいエンドポイントを利用する選択肢が増えます。

対処方法：
特別な対応は不要です。
現在のCloud Loggingの利用状況を確認し、必要に応じて新しい `ca` リージョナルエンドポイントの利用を検討してください。特に、カナダリージョンにリソースがあり、ログのデータ所在地に関する厳格な要件がある場合は、ログデータをこのリージョン内で収集・保存するように構成することで、要件を満たしやすくなります。通常、明示的にリージョナルエンドポイントを指定しない限り、Cloud Loggingはグローバルエンドポイントやデフォルトのエンドポイントを使用します。

用語説明：
*   **Cloud Logging**: Google Cloudが提供するフルマネージドのロギングサービス。アプリケーションやGoogle Cloudサービスから生成されるログデータを一元的に収集、保存、分析、モニタリングできます。
*   **API (Application Programming Interface)**: ソフトウェアコンポーネントが互いに通信するためのインターフェースのセット。
*   **Regional Endpoint (リージョナルエンドポイント)**: クラウドサービスが特定の地理的リージョン内に配置され、そのリージョン内のリソースとの通信を最適化するために提供されるネットワークアドレス。データ所在地の要件やネットワークレイテンシの削減のために利用されます。
*   **ca**: Google Cloudにおけるカナダ（Canada）のリージョンコード。